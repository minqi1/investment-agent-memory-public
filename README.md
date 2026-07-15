# Investment Agent Memory Public Bridge

This public repository is a sanitized bridge for ChatGPT investment committee review.

## Read First

- `index.html` for the stable live endpoint directory site
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

The GitHub Pages site and `context/live_endpoints.json` act as a stable directory for the current temporary trycloudflare live endpoints. If those URLs are unreachable, use the GitHub raw fallback files.
