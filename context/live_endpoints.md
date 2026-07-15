# Live Endpoint Directory

- updated_at: `2026-07-15T23:46:26+08:00`
- source_updated_at: `2026-07-15T23:40:00`
- status: `healthy`
- ttl_seconds: `300`

## GPT Read Order

- Read context/live_endpoints.json from GitHub raw.
- Use live.snapshot_public_url as the fixed Render intraday relay endpoint.
- If the live endpoint is unreachable, stale, or contradictory, fall back to
  raw_fallbacks.latest_intraday_state.
- Use context/gpt_handoff.md for role boundaries and required output format.

## Live Layer

- dashboard_public_url:
- snapshot_public_url: https://investment-agent-memory-public.onrender.com/latest_intraday.json
- premarket_refresh_public_url:
- postmarket_refresh_public_url:

## Live Health

- snapshot_public_url_ok: `True`
- snapshot_public_url_status_code: `200`
- snapshot_public_url_checked_at: `2026-07-15T23:46:24+08:00`
- dashboard_public_url_ok: `True`
- dashboard_public_url_status_code: `200`
- dashboard_public_url_checked_at: `2026-07-15T23:46:25+08:00`

## Raw Fallbacks

- gpt_handoff: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/gpt_handoff.md
- latest_intraday_context: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md
- latest_intraday_state: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json
- latest_market_context: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_market_context.md
- latest_market_state: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_market_state.json

## Boundaries

- Research and review only; no automated trading.
- Current automated ceiling remains L3_MANUAL_CONFIRM_REQUIRED.
- Do not overwrite raw_score, price, vwap, data_quality, execution_level, or risk_reasons.
