# Live Endpoint Directory

- updated_at: `2026-07-16T00:40:45+08:00`
- source_updated_at: `2026-07-16T00:35:19`
- status: `healthy`
- ttl_seconds: `300`

## GPT Read Order

- Read context/data_contract.md for field definitions and usage boundaries.
- Read context/live_endpoints.json from GitHub raw.
- Use raw_fallbacks.latest_intraday_context and raw_fallbacks.latest_intraday_state as the
  canonical GPT-readable intraday source.
- Optionally try live.snapshot_markdown_public_url, live.snapshot_public_url, or
  live.ticker_public_url_template as fixed Render relay endpoints.
- If the live endpoint is unreachable, stale, returns cache miss, or is contradictory, continue
  from GitHub raw.
- Use context/gpt_handoff.md for role boundaries and required output format.

## Live Layer

- dashboard_public_url: https://topics-singles-focused-yields.trycloudflare.com/?board=us&t=committee
- snapshot_public_url: https://investment-agent-memory-public.onrender.com/latest_intraday.json
- snapshot_markdown_public_url: https://investment-agent-memory-public.onrender.com/latest_intraday.md
- ticker_public_url_template: https://investment-agent-memory-public.onrender.com/ticker/{symbol}.json
- premarket_refresh_public_url:
- postmarket_refresh_public_url:

## Live Health

- snapshot_public_url_ok: `True`
- snapshot_public_url_status_code: `200`
- snapshot_public_url_checked_at: `2026-07-16T00:40:41+08:00`
- dashboard_public_url_ok: `True`
- dashboard_public_url_status_code: `200`
- dashboard_public_url_checked_at: `2026-07-16T00:40:43+08:00`

## Raw Fallbacks

- data_contract: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/data_contract.md
- gpt_handoff: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/gpt_handoff.md
- latest_intraday_context: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md
- latest_intraday_state: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json
- latest_market_context: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_market_context.md
- latest_market_state: https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_market_state.json

## Monitor Guardrails

- interval_open_seconds: `180`
- duration_seconds_max: `120`
- stale_count_policy: should not obviously rise across consecutive refreshes
- rate_limit_policy: no 429 or Too Many Requests
- relay_ok_required: `True`

## Boundaries

- Research and review only; no automated trading.
- Current automated ceiling remains L3_MANUAL_CONFIRM_REQUIRED.
- Do not overwrite raw_score, price, vwap, data_quality, execution_level, or risk_reasons.
