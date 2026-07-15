# Investment Agent Memory Public Bridge

This public repository is a sanitized bridge for ChatGPT investment committee review.

## Read First

- `index.html` for the stable live endpoint directory site
- `context/data_contract.md` for premarket, intraday, postmarket, and user-ranking field definitions
- `context/live_endpoints.json`
- `context/live_endpoints.md`
- `context/gpt_handoff.md`
- `context/latest_intraday_context.md`
- `context/latest_intraday_state.json`
- `context/latest_market_context.md`
- `context/latest_market_state.json`
- `context/watchlist.md`
- `gpt_outputs/summary.json` when GPT overlay continuity is available

## Redactions

- Real or simulated user action records are removed.
- Local workstation paths are removed.
- API keys, tokens, `.env`, and broker credentials are not included.

## Boundary

This bridge is for research and review only. It does not authorize automated trading. Current automated ceiling remains `L3_MANUAL_CONFIRM_REQUIRED` unless realtime broker data is explicitly verified.

## Live Endpoint Pattern

- raw_intraday_context: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md`
- raw_intraday_state: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json`
- optional_render_current_intraday_json: `https://investment-agent-memory-public.onrender.com/latest_intraday.json`
- optional_render_current_intraday_markdown: `https://investment-agent-memory-public.onrender.com/latest_intraday.md`
- optional_render_ticker_template: `https://investment-agent-memory-public.onrender.com/ticker/{symbol}.json`
- optional_render_health: `https://investment-agent-memory-public.onrender.com/health`

The GitHub Pages site and `context/live_endpoints.json` act as a stable directory. GPT should treat GitHub raw as canonical and Render as optional. If the Render endpoint is unreachable, stale, degraded, or returns cache miss, use the GitHub raw fallback files.

## Intraday Monitor Guardrails

- Open-session monitor cadence is currently 180 seconds.
- Treat the live relay as healthy only while `duration_seconds < 120`, `stale_count` is not obviously rising, there are no `429` / `Too Many Requests` errors, and `relay_ok` or `relay_upload.ok` remains `True`.
- The live packet includes the user's `dynamic_leaderboard` and `comfortable_entry_leaderboard`; these are research signals, not trade instructions.
