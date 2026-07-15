# Live Endpoint Directory

- updated_at: `2026-07-15T23:16:19+08:00`
- source_updated_at: `2026-07-15T23:05:33`
- status: `healthy`
- ttl_seconds: `300`

## GPT Read Order

- Read context/live_endpoints.json from GitHub raw.
- If live.snapshot_public_url is reachable, use it for the freshest current state.
- If the live endpoint is unreachable, stale, or contradictory, fall back to
  raw_fallbacks.latest_intraday_state.
- Use context/gpt_handoff.md for role boundaries and required output format.

## Live Layer

- dashboard_public_url: https://topics-singles-focused-yields.trycloudflare.com/?board=us&t=committee
- snapshot_public_url: https://navy-kelly-initially-thumbnails.trycloudflare.com/live_intraday.json
- premarket_refresh_public_url: https://navy-kelly-initially-thumbnails.trycloudflare.com/refresh_snapshot.json?stage=premarket
- postmarket_refresh_public_url: https://navy-kelly-initially-thumbnails.trycloudflare.com/refresh_snapshot.json?stage=postmarket_review

## Live Health

- snapshot_public_url_ok: `True`
- snapshot_public_url_status_code: `200`
- snapshot_public_url_checked_at: `2026-07-15T23:16:15+08:00`
- dashboard_public_url_ok: `True`
- dashboard_public_url_status_code: `200`
- dashboard_public_url_checked_at: `2026-07-15T23:16:18+08:00`

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
