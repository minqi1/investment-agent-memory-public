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

The GitHub Pages site and `context/live_endpoints.json` act as a stable directory for the fixed Render live intraday relay. If the Render endpoint is unreachable, stale, or degraded, use the GitHub raw fallback files.

## Intraday Monitor Guardrails

- Open-session monitor cadence is currently 180 seconds.
- Treat the live relay as healthy only while `duration_seconds < 120`, `stale_count` is not obviously rising, there are no `429` / `Too Many Requests` errors, and `relay_ok` or `relay_upload.ok` remains `True`.
- The live packet includes the user's `dynamic_leaderboard` and `comfortable_entry_leaderboard`; these are research signals, not trade instructions.
