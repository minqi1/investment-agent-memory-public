from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response


ROOT = Path(__file__).resolve().parent
FALLBACK_INTRADAY_STATE = ROOT / "context" / "latest_intraday_state.json"
FALLBACK_LIVE_ENDPOINTS = ROOT / "context" / "live_endpoints.json"

app = FastAPI(title="Investment Live Relay", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

latest_payload: dict[str, Any] | None = None
latest_received_at: str | None = None

INDEX_SYMBOLS = {"QQQ", "SPY", "SMH", "SOXX"}
CHAIN_GROUPS = {
    "AI Accelerator": {"ai_accelerator"},
    "Memory/HBM": {"memory_hbm_storage", "memory", "hbm", "storage"},
    "Semiconductor Equipment": {"semiconductor_equipment", "semi_equipment"},
    "Cloud AI": {"cloud_ai_capex", "mega_cap_platform"},
}
ALIASES = {
    "SKHYV": "SKHY",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8-sig"))


def expected_token() -> str:
    return os.environ.get("RELAY_TOKEN", "").strip()


def check_token(authorization: str | None, x_relay_token: str | None) -> None:
    token = expected_token()
    if not token:
        raise HTTPException(status_code=500, detail="RELAY_TOKEN is not configured")
    supplied = ""
    if authorization and authorization.lower().startswith("bearer "):
        supplied = authorization[7:].strip()
    if not supplied and x_relay_token:
        supplied = x_relay_token.strip()
    if supplied != token:
        raise HTTPException(status_code=401, detail="invalid relay token")


def no_store_headers(content_type: str) -> dict[str, str]:
    return {
        "Content-Type": content_type,
        "Cache-Control": "no-store, max-age=0",
        "Pragma": "no-cache",
    }


def pretty_json_response(payload: dict[str, Any], status_code: int = 200) -> Response:
    return Response(
        content=json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False, default=str),
        status_code=status_code,
        headers=no_store_headers("application/json; charset=utf-8"),
    )


def markdown_response(markdown: str, status_code: int = 200) -> Response:
    return Response(
        content=markdown,
        status_code=status_code,
        headers=no_store_headers("text/markdown; charset=utf-8"),
    )


def current_payload() -> tuple[dict[str, Any], str]:
    if latest_payload is not None:
        return latest_payload, "uploaded"
    fallback = read_json(FALLBACK_INTRADAY_STATE)
    if fallback:
        return fallback, "repo_fallback"
    return {}, "missing"


def relay_meta(source: str) -> dict[str, Any]:
    return {
        "source": source,
        "served_at": now_iso(),
        "latest_received_at": latest_received_at,
        "boundary": "research_only_no_automated_trading",
        "execution_ceiling": "L3_MANUAL_CONFIRM_REQUIRED",
    }


def first_value(row: dict[str, Any], names: list[str], default: Any = None) -> Any:
    for name in names:
        if name in row and row.get(name) not in ("", None):
            return row.get(name)
    return default


def as_float(value: Any) -> float | None:
    try:
        if value in ("", None):
            return None
        number = float(value)
        if number != number:
            return None
        return number
    except Exception:
        return None


def round_float(value: Any, digits: int = 4) -> float | None:
    number = as_float(value)
    return round(number, digits) if number is not None else None


def extract_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    intraday_refresh = payload.get("intraday_refresh")
    if isinstance(intraday_refresh, dict) and isinstance(intraday_refresh.get("rows"), list):
        return [row for row in intraday_refresh.get("rows") or [] if isinstance(row, dict)]
    if isinstance(payload.get("instruments"), list):
        return [row for row in payload.get("instruments") or [] if isinstance(row, dict)]
    rows: list[dict[str, Any]] = []
    indices = payload.get("indices")
    if isinstance(indices, dict):
        rows.extend(row for row in indices.values() if isinstance(row, dict))
    watchlist = payload.get("watchlist")
    if isinstance(watchlist, list):
        rows.extend(row for row in watchlist if isinstance(row, dict))
    return rows


def row_symbol(row: dict[str, Any]) -> str:
    return str(first_value(row, ["ticker", "symbol"], "")).upper()


def data_quality_for_row(row: dict[str, Any]) -> dict[str, Any]:
    nested = row.get("data_quality") if isinstance(row.get("data_quality"), dict) else {}
    return {
        "price_status": first_value(row, ["price_status"], nested.get("price_status")),
        "vwap_status": first_value(row, ["vwap_status"], nested.get("vwap_status")),
        "opening_15m_high_status": first_value(
            row, ["opening_15m_high_status"], nested.get("opening_15m_high_status")
        ),
        "opening_15m_low_status": first_value(row, ["opening_15m_low_status"], nested.get("opening_15m_low_status")),
        "spread_status": first_value(row, ["bid_ask_spread_status", "spread_status"], nested.get("bid_ask_spread_status")),
        "lag_minutes": round_float(first_value(row, ["lag_minutes", "data_delay_minutes"], nested.get("lag_minutes")), 2),
        "fresh_within_lag": first_value(row, ["fresh_within_lag", "live_fresh_within_lag"], nested.get("fresh_within_lag")),
    }


def risk_reasons_for_row(row: dict[str, Any]) -> list[str]:
    reasons = row.get("risk_reasons")
    if isinstance(reasons, list):
        return [str(item) for item in reasons if str(item)]
    caution = row.get("caution")
    if caution and str(caution) not in {"manual_confirm_candidate", "watch_only"}:
        return [str(caution)]
    return []


def codex_action_for_row(row: dict[str, Any], risk_reasons: list[str]) -> str:
    if row.get("manual_confirm_candidate") is True:
        return "buy_precheck_manual_confirm"
    precheck = row.get("buy_precheck")
    if isinstance(precheck, dict) and precheck.get("status") == "manual_confirm_candidate":
        return "buy_precheck_manual_confirm"
    if any("below_opening_15m_low" in item or "below_vwap" in item for item in risk_reasons):
        return "avoid_or_wait"
    if risk_reasons:
        return "wait_for_recheck"
    return "watch_only"


def benchmark_delta(row: dict[str, Any], qqq_vwap_distance: float | None) -> float | None:
    relative_strength = row.get("relative_strength")
    if isinstance(relative_strength, dict):
        qqq = relative_strength.get("QQQ")
        if isinstance(qqq, dict):
            value = as_float(qqq.get("vwap_distance_delta_pct"))
            if value is not None:
                return round(value, 4)
    row_distance = as_float(first_value(row, ["vwap_distance_pct", "vs_vwap_pct"]))
    if row_distance is not None and qqq_vwap_distance is not None:
        return round(row_distance - qqq_vwap_distance, 4)
    return None


def normalize_row(row: dict[str, Any], qqq_vwap_distance: float | None) -> dict[str, Any]:
    ticker = row_symbol(row)
    risk_reasons = risk_reasons_for_row(row)
    price = round_float(row.get("price"))
    bid = round_float(first_value(row, ["bid", "bid_price"]))
    ask = round_float(first_value(row, ["ask", "ask_price"]))
    return {
        "ticker": ticker,
        "name": row.get("name"),
        "chain": first_value(row, ["chain", "chain_segment"]),
        "price": price,
        "change_pct": round_float(first_value(row, ["change_pct", "day_change_pct", "regular_market_change_pct"])),
        "premarket_change_pct": round_float(first_value(row, ["premarket_change_pct", "pre_market_change_pct"])),
        "vwap": round_float(row.get("vwap")),
        "vs_vwap_pct": round_float(first_value(row, ["vs_vwap_pct", "vwap_distance_pct"])),
        "opening_15m_high": round_float(row.get("opening_15m_high")),
        "opening_15m_low": round_float(row.get("opening_15m_low")),
        "bid": bid,
        "ask": ask,
        "spread_pct": round_float(row.get("spread_pct")),
        "bid_ask_spread": round_float(first_value(row, ["bid_ask_spread", "spread"])),
        "volume": first_value(row, ["volume", "day_volume"]),
        "relative_strength_vs_qqq": benchmark_delta(row, qqq_vwap_distance),
        "execution_level": row.get("execution_level"),
        "real_trade_allowed": row.get("real_trade_allowed"),
        "risk_reasons": risk_reasons,
        "codex_action": codex_action_for_row(row, risk_reasons),
        "raw_score": round_float(first_value(row, ["raw_score", "daily_priority_score"])),
        "dynamic_score": round_float(row.get("dynamic_score")),
        "comfortable_entry_score": round_float(row.get("comfortable_entry_score")),
        "data_quality": data_quality_for_row(row),
    }


def market_regime_hint(indices: dict[str, Any]) -> str:
    qqq = indices.get("QQQ") or {}
    smh = indices.get("SMH") or {}
    soxx = indices.get("SOXX") or {}
    qqq_vwap = as_float(qqq.get("vs_vwap_pct"))
    smh_vwap = as_float(smh.get("vs_vwap_pct"))
    soxx_vwap = as_float(soxx.get("vs_vwap_pct"))
    if smh_vwap is not None and soxx_vwap is not None and smh_vwap < 0 and soxx_vwap < 0:
        return "semiconductor_pressure"
    if qqq_vwap is not None and qqq_vwap >= 0 and (smh_vwap is None or smh_vwap < 0):
        return "mega_cap_resilience_semiconductor_lag"
    if qqq_vwap is not None and qqq_vwap < 0:
        return "risk_off_or_below_vwap"
    return "mixed_or_unclassified"


def normalize_contract(payload: dict[str, Any], source: str) -> dict[str, Any]:
    rows = extract_rows(payload)
    raw_by_symbol = {row_symbol(row): row for row in rows if row_symbol(row)}
    qqq_distance = as_float(first_value(raw_by_symbol.get("QQQ", {}), ["vwap_distance_pct", "vs_vwap_pct"]))
    normalized_by_symbol = {
        symbol: normalize_row(row, qqq_distance)
        for symbol, row in raw_by_symbol.items()
    }
    indices = {symbol: normalized_by_symbol[symbol] for symbol in INDEX_SYMBOLS if symbol in normalized_by_symbol}
    watchlist = [
        row for symbol, row in sorted(normalized_by_symbol.items())
        if symbol not in INDEX_SYMBOLS
    ]
    buy_precheck_candidates = [
        row for row in watchlist
        if row.get("codex_action") == "buy_precheck_manual_confirm"
    ]
    avoid_or_wait = [
        row for row in watchlist
        if row.get("codex_action") in {"avoid_or_wait", "wait_for_recheck"}
    ]
    session = payload.get("market_session") or payload.get("session") or {}
    data_quality = payload.get("data_quality")
    if not isinstance(data_quality, dict):
        data_quality = {
            "total_rows": len(rows),
            "stale_count": sum(1 for row in watchlist if (row.get("data_quality") or {}).get("fresh_within_lag") is False),
            "current_max_execution_level": "L3_MANUAL_CONFIRM_REQUIRED",
        }
    return {
        "version": "intraday_gpt_contract_v1",
        "generated_at": payload.get("generated_at"),
        "market_time_et": payload.get("us_eastern_time") or session.get("us_eastern_time"),
        "stage": payload.get("stage") or "intraday_live",
        "execution_limit": "L3_MANUAL_CONFIRM_REQUIRED",
        "data_quality": data_quality,
        "market_regime_hint": market_regime_hint(indices),
        "indices": indices,
        "watchlist": watchlist,
        "buy_precheck_candidates": buy_precheck_candidates,
        "avoid_or_wait": avoid_or_wait,
        "user_position_notes": payload.get("user_position_notes") or payload.get("position_notes") or [
            "No live user position notes were supplied in this relay payload.",
            "Research only; real_trade_allowed remains bounded by L3_MANUAL_CONFIRM_REQUIRED.",
        ],
        "links": {
            "latest_intraday_json": "/latest_intraday.json",
            "latest_intraday_markdown": "/latest_intraday.md",
            "ticker_json_template": "/ticker/{symbol}.json",
            "raw_intraday_state": "https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json",
            "raw_intraday_context": "https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md",
            "data_contract": "https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/data_contract.md",
        },
        "relay": relay_meta(source),
    }


def format_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4g}"
    return str(value)


def markdown_table(rows: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| Ticker | Price | Chg % | VWAP | vs VWAP % | Open15 High | Open15 Low | Spread % | Action | Risk Reasons |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    if not rows:
        lines.append("|  |  |  |  |  |  |  |  |  |  |")
        return lines
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    format_value(row.get("ticker")),
                    format_value(row.get("price")),
                    format_value(row.get("change_pct")),
                    format_value(row.get("vwap")),
                    format_value(row.get("vs_vwap_pct")),
                    format_value(row.get("opening_15m_high")),
                    format_value(row.get("opening_15m_low")),
                    format_value(row.get("spread_pct")),
                    format_value(row.get("codex_action")),
                    ", ".join(row.get("risk_reasons") or []),
                ]
            )
            + " |"
        )
    return lines


def grouped_rows(contract: dict[str, Any], group_name: str) -> list[dict[str, Any]]:
    chain_values = CHAIN_GROUPS.get(group_name, set())
    return [
        row for row in contract.get("watchlist") or []
        if str(row.get("chain") or "").lower() in chain_values
    ]


def build_markdown(contract: dict[str, Any]) -> str:
    lines = [
        "# Latest Intraday Snapshot",
        "",
        f"- version: `{contract.get('version')}`",
        f"- generated_at: `{contract.get('generated_at')}`",
        f"- market_time_et: `{contract.get('market_time_et')}`",
        f"- stage: `{contract.get('stage')}`",
        f"- execution_limit: `{contract.get('execution_limit')}`",
        f"- market_regime_hint: `{contract.get('market_regime_hint')}`",
        "",
        "## Market Regime",
        "",
        f"- data_quality: `{json.dumps(contract.get('data_quality') or {}, ensure_ascii=False)}`",
        f"- relay: `{json.dumps(contract.get('relay') or {}, ensure_ascii=False)}`",
        "",
        "## Indices",
        "",
    ]
    lines.extend(markdown_table(list((contract.get("indices") or {}).values())))
    for section in ["AI Accelerator", "Memory/HBM", "Semiconductor Equipment", "Cloud AI"]:
        lines.extend(["", f"## {section}", ""])
        lines.extend(markdown_table(grouped_rows(contract, section)))
    lines.extend(["", "## Buy Precheck Candidates", ""])
    lines.extend(markdown_table(contract.get("buy_precheck_candidates") or []))
    lines.extend(["", "## Avoid / Wait", ""])
    lines.extend(markdown_table(contract.get("avoid_or_wait") or []))
    lines.extend(["", "## User Position Notes", ""])
    for note in contract.get("user_position_notes") or []:
        lines.append(f"- {note}")
    lines.append("")
    return "\n".join(lines)


@app.get("/")
def root() -> Response:
    return pretty_json_response({
        "ok": True,
        "service": "investment-live-relay",
        "read": "/latest_intraday.json",
        "markdown": "/latest_intraday.md",
        "ticker": "/ticker/{symbol}.json",
        "health": "/health",
    })


@app.get("/health")
def health() -> Response:
    fallback = read_json(FALLBACK_INTRADAY_STATE)
    live_endpoints = read_json(FALLBACK_LIVE_ENDPOINTS)
    return pretty_json_response({
        "ok": True,
        "has_uploaded_payload": latest_payload is not None,
        "latest_received_at": latest_received_at,
        "fallback_generated_at": fallback.get("generated_at"),
        "fallback_stage": fallback.get("stage"),
        "live_endpoint_status": live_endpoints.get("status"),
        "served_at": now_iso(),
    })


@app.get("/latest_intraday.json")
def latest_intraday() -> Response:
    payload, source = current_payload()
    if payload:
        return pretty_json_response(normalize_contract(payload, source))
    return pretty_json_response(
        {
            "ok": False,
            "error": "no uploaded payload and no repo fallback available",
            "served_at": now_iso(),
        },
        status_code=503,
    )


@app.get("/latest_intraday.md")
def latest_intraday_markdown() -> Response:
    payload, source = current_payload()
    if not payload:
        return markdown_response(
            "# Latest Intraday Snapshot\n\nNo uploaded payload and no repo fallback available.\n",
            status_code=503,
        )
    return markdown_response(build_markdown(normalize_contract(payload, source)))


@app.get("/ticker/{symbol}.json")
def ticker(symbol: str) -> Response:
    requested = symbol.removesuffix(".json").upper()
    lookup = ALIASES.get(requested, requested)
    payload, source = current_payload()
    if not payload:
        return pretty_json_response(
            {
                "ok": False,
                "ticker": requested,
                "error": "no uploaded payload and no repo fallback available",
                "served_at": now_iso(),
            },
            status_code=503,
        )
    contract = normalize_contract(payload, source)
    rows = list((contract.get("indices") or {}).values()) + list(contract.get("watchlist") or [])
    match = next((row for row in rows if row.get("ticker") == lookup), None)
    if not match:
        return pretty_json_response(
            {
                "ok": False,
                "ticker": requested,
                "normalized_ticker": lookup,
                "error": "ticker_not_found",
                "available_tickers": [row.get("ticker") for row in rows],
                "generated_at": contract.get("generated_at"),
                "market_time_et": contract.get("market_time_et"),
                "links": contract.get("links"),
                "relay": contract.get("relay"),
            },
            status_code=404,
        )
    return pretty_json_response(
        {
            "ok": True,
            "ticker": requested,
            "normalized_ticker": lookup,
            "generated_at": contract.get("generated_at"),
            "market_time_et": contract.get("market_time_et"),
            "stage": contract.get("stage"),
            "execution_limit": contract.get("execution_limit"),
            "data": match,
            "links": contract.get("links"),
            "relay": contract.get("relay"),
        }
    )


@app.post("/update")
async def update(
    request: Request,
    authorization: str | None = Header(default=None),
    x_relay_token: str | None = Header(default=None),
) -> Response:
    check_token(authorization, x_relay_token)
    payload = await request.json()
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="JSON object required")
    global latest_payload, latest_received_at
    latest_payload = payload
    latest_received_at = now_iso()
    return pretty_json_response({
        "ok": True,
        "latest_received_at": latest_received_at,
        "payload_generated_at": payload.get("generated_at"),
        "stage": payload.get("stage"),
    })
