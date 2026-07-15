# GPT Data Contract

This repository is the stable public directory for GPT investment review. GitHub raw is the
canonical GPT-readable source. Use it as a research interface only; it does not authorize
automated trading.

## Read Order

1. Live directory: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/live_endpoints.json`
2. Read raw intraday context: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md`.
3. Read raw intraday state JSON when details are needed: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json`.
4. Use handoff boundaries and narrative context from `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/gpt_handoff.md`.
5. Optionally try the Render live endpoint only as a freshness layer; if it fails, continue from
   GitHub raw.

## Fixed Live Links

- optional_render_current_intraday_json: `https://investment-agent-memory-public.onrender.com/latest_intraday.json`
- health: `https://investment-agent-memory-public.onrender.com/health`
- endpoint_directory: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/live_endpoints.json`
- raw_intraday_context: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md`
- raw_intraday_state: `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json`

## Premarket Packet

Premarket context is published through `context/latest_market_context.md` and
`context/latest_market_state.json` during the premarket refresh.

- `generated_at`: ISO-8601 timestamp with timezone.
- `stage`: expected to identify the premarket bridge stage.
- index and sector context: QQQ, SPY, SMH, SOXX, and relevant watchlist symbols when available.
- candidate fields: price, VWAP or proxy VWAP, spread/data-quality notes, raw_score,
  execution_level, and risk_reasons.
- GPT overlay continuity: latest available GPT overlay metadata, thesis ledger, forecast ledger,
  candidate conditions, and due reviews when present.
- buy-precheck posture: only describes research conditions; it does not permit live execution.

## Intraday Live Packet

Intraday data for GPT should come from GitHub raw first. The Render relay is optional because
GPT web openers may fail on dynamic API endpoints.

- `generated_at`: ISO-8601 timestamp with timezone for the uploaded live packet.
- converted US Eastern time and session status, when present.
- market rows for QQQ, SPY, SMH, SOXX, and current focus candidates.
- price, VWAP, opening 15 minute high/low, bid/ask spread, data_quality, and data-delay fields
  when available from the source.
- raw_score, execution_level, risk_reasons, and real_trade_allowed boundary fields.
- relative strength versus QQQ, SMH, and SOXX.
- buy-before-check conditions already met and not yet met.
- monitor metadata such as duration_seconds, stale_count, relay_ok or relay_upload.ok, and relay
  upload size.

## User Ranking Fields

The live intraday packet includes the user's lightweight algorithmic rankings so GPT can combine
market facts with the user's own scoring lens.

- `dynamic_score`: momentum and relative-strength oriented score for current leader detection.
- `dynamic_leaderboard`: sorted list of current stronger names under the user's scoring model.
- `comfortable_entry_score`: pullback/support quality score for calmer watch candidates.
- `comfortable_entry_leaderboard`: sorted list of candidates that may be more comfortable to
  review than pure momentum leaders.
- `overheat_penalty`: penalty when a move is stretched relative to support/VWAP/opening range.
- `vwap_distance_pct`: distance from VWAP; useful for avoiding late chase entries.
- `opening_15m_high_distance_pct`: distance from the opening 15 minute high.

Use these rankings as research signals only. Do not treat a high score as a trade instruction.

## Postmarket Packet

Postmarket context is published through `context/latest_market_context.md` and
`context/latest_market_state.json` during the postmarket or EOD refresh.

- session summary and market regime after the US close.
- index and sector performance review, especially QQQ, SPY, SMH, SOXX, and watchlist names.
- candidate review: what confirmed, what failed, what remains watch-only.
- thesis ledger and forecast ledger updates when GPT overlay continuity exists.
- expired or due forecast claims, including unverifiable or unverifiable_due_to_gap status when
  appropriate.
- next-session watch conditions and risk boundaries.

## Health Guardrails

For the 3 minute intraday monitor trial, treat the relay as operationally healthy only while
these checks remain true:

- `duration_seconds < 120`.
- `stale_count` is not obviously rising across consecutive refreshes.
- no `429` or `Too Many Requests` appears in monitor or relay status.
- `relay_ok` or `relay_upload.ok` remains `True`.

If these guardrails degrade, or if GPT reports a Render fetch/cache miss, use raw GitHub
context/state and mark the live API layer unavailable.

## Hard Boundaries

- Research and review only; no automated trading.
- Current automated ceiling remains `L3_MANUAL_CONFIRM_REQUIRED`.
- Do not overwrite Codex factual fields: raw_score, price, vwap, data_quality, execution_level,
  or risk_reasons.
- Do not upgrade execution permission from GPT overlay or public repo content.
- If data is stale, missing, contradictory, or delayed, downgrade confidence instead of filling
  gaps.
