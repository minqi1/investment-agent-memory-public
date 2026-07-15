# Investment Agent Memory Public Bridge

This public repository is a sanitized bridge for ChatGPT investment committee review.

## Read First

- `context/latest_intraday_state.md` for the GPT-readable intraday state. This is the primary high-frequency file.
- `context/gpt_handoff.md` for role boundaries, read order, and output requirements.
- `context/data_contract.md` for premarket, intraday, postmarket, and user-ranking field definitions
- `context/live_endpoints.json`
- `context/live_endpoints.md`
- `context/latest_intraday_state.jsonl` as the structured fallback if Markdown cannot be read.
- `context/latest_intraday_state.json` as the pretty JSON fallback.
- `context/latest_intraday_context.md`
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

- canonical_gpt_intraday_markdown: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.md`
- structured_intraday_jsonl_fallback: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.jsonl`
- pretty_intraday_json_fallback: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json`
- raw_intraday_context: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md`
- optional_render_current_intraday_json: `https://investment-agent-memory-public.onrender.com/latest_intraday.json`
- optional_render_current_intraday_markdown: `https://investment-agent-memory-public.onrender.com/latest_intraday.md`
- optional_render_ticker_template: `https://investment-agent-memory-public.onrender.com/ticker/{symbol}.json`
- optional_render_health: `https://investment-agent-memory-public.onrender.com/health`

The GitHub Pages site and `context/live_endpoints.json` act as a stable directory. GPT should treat GitHub raw as canonical and Render as optional. If the Render endpoint is unreachable, stale, degraded, or returns cache miss, use the GitHub raw fallback files.

## GPT Intraday Read Order

For intraday committee review, GPT should read the files in this order:

1. Markdown: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.md`
2. JSONL: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.jsonl`
3. Pretty JSON: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json`

Use the Markdown file first. It is intentionally multi-line and sectioned for GPT web reading. It includes:

- generated time, market time, session state, and execution limit
- data quality and freshness warnings
- market regime hint
- indices
- buy precheck candidates
- comfortable entry leaderboard
- dynamic leaderboard
- full watchlist rows
- price, VWAP, opening 15-minute high/low, spread, relative strength, execution level, and risk reasons

Only use JSONL or pretty JSON when Markdown cannot be read. Do not rely on single-line compressed JSON for GPT analysis.

## Intraday Monitor Guardrails

- Open-session monitor cadence is currently 180 seconds.
- Treat the live relay as healthy only while `duration_seconds < 120`, `stale_count` is not obviously rising, there are no `429` / `Too Many Requests` errors, and `relay_ok` or `relay_upload.ok` remains `True`.
- The live packet includes the user's `dynamic_leaderboard` and `comfortable_entry_leaderboard`; these are research signals, not trade instructions.
