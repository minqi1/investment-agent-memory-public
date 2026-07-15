from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


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


def decorate_payload(payload: dict[str, Any], source: str) -> dict[str, Any]:
    body = dict(payload)
    body.setdefault("schema_version", "live_intraday_snapshot_v1")
    body.setdefault("stage", "intraday_live")
    body["relay"] = {
        "source": source,
        "served_at": now_iso(),
        "latest_received_at": latest_received_at,
        "boundary": "research_only_no_automated_trading",
        "execution_ceiling": "L3_MANUAL_CONFIRM_REQUIRED",
    }
    return body


@app.get("/")
def root() -> dict[str, Any]:
    return {
        "ok": True,
        "service": "investment-live-relay",
        "read": "/latest_intraday.json",
        "health": "/health",
    }


@app.get("/health")
def health() -> dict[str, Any]:
    fallback = read_json(FALLBACK_INTRADAY_STATE)
    live_endpoints = read_json(FALLBACK_LIVE_ENDPOINTS)
    return {
        "ok": True,
        "has_uploaded_payload": latest_payload is not None,
        "latest_received_at": latest_received_at,
        "fallback_generated_at": fallback.get("generated_at"),
        "fallback_stage": fallback.get("stage"),
        "live_endpoint_status": live_endpoints.get("status"),
        "served_at": now_iso(),
    }


@app.get("/latest_intraday.json")
def latest_intraday() -> JSONResponse:
    if latest_payload is not None:
        return JSONResponse(decorate_payload(latest_payload, "uploaded"))
    fallback = read_json(FALLBACK_INTRADAY_STATE)
    if fallback:
        return JSONResponse(decorate_payload(fallback, "repo_fallback"))
    return JSONResponse(
        {
            "ok": False,
            "error": "no uploaded payload and no repo fallback available",
            "served_at": now_iso(),
        },
        status_code=503,
    )


@app.post("/update")
async def update(
    request: Request,
    authorization: str | None = Header(default=None),
    x_relay_token: str | None = Header(default=None),
) -> dict[str, Any]:
    check_token(authorization, x_relay_token)
    payload = await request.json()
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="JSON object required")
    global latest_payload, latest_received_at
    latest_payload = payload
    latest_received_at = now_iso()
    return {
        "ok": True,
        "latest_received_at": latest_received_at,
        "payload_generated_at": payload.get("generated_at"),
        "stage": payload.get("stage"),
    }
