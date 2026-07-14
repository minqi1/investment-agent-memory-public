# GPT Investment Committee Handoff

Use this file as the stable handoff prompt between Codex and ChatGPT.

## Current Context

- Generated: 2026-07-14T09:02:01
- Stage: `eod`
- Report date: `2026-07-14`
- Market regime from Codex: `weak_breadth_or_pullback`
- Current automated execution ceiling: `L3_MANUAL_CONFIRM_REQUIRED`
- GitHub repo: https://github.com/minqi1/investment-agent-memory-public
- Latest GPT premarket overlay date: `2026-07-13`
- Latest GPT postmarket overlay date: `None`
- GPT overlay gap days: `None`
- Latest intraday context generated: `2026-07-13T23:06:07+08:00`
- Latest intraday US/Eastern time: `2026-07-13T11:06:07-04:00`
- Latest intraday session open: `True`
- Latest intraday candidate count: `4`

## Files To Read

Read these files first, in this order:

1. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_context.md`
2. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_intraday_state.json`
3. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_market_context.md`
4. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/latest_market_state.json`
5. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/context/watchlist.md`
6. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/memory/investment_principles.md`
7. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/memory/mistakes.md`
8. `https://raw.githubusercontent.com/minqi1/investment-agent-memory-public/main/memory/stock_notes.md`

If raw GitHub URLs are unavailable, read the same paths inside the repo:

- `context/latest_intraday_context.md`
- `context/latest_intraday_state.json`
- `context/latest_market_context.md`
- `context/latest_market_state.json`
- `context/watchlist.md`
- `memory/investment_principles.md`
- `memory/mistakes.md`
- `memory/stock_notes.md`

## GPT Overlay Continuity

- Availability
  - latest_premarket_overlay_available: True
  - latest_postmarket_overlay_available: False
  - latest_premarket_overlay_date: 2026-07-13
  - continuity_status: new_baseline
- Latest Decision
  - decision: RISK_REDUCTION_REVIEW
  - decision_reason: 存储和半导体盘前处于宏观风险、拥挤交易、ADR与本股定价错位及杠杆去风险叠加阶段。对现有杠杆暴露先做风险检查；若无杠杆持仓则降级为NO_TRADE。

### Latest Thesis Ledger

- T-AI-CAPEX-20260713: AI资本开支基本面尚未出现明确下修，但油价、通胀和收益率上升正在提高估值风险。
- T-MEMORY-HBM-20260713: HBM供需逻辑尚未失效，但ADR溢价、拥挤持仓、杠杆产品和远期扩产使交易结构显著恶化。
- T-SEMI-EQUIPMENT-20260713: 设备链需要ASML订单和TSMC资本开支及指引确认，盘前价格变化不足以升级基本面判断。

### Latest Forecast Ledger

- F-20260713-05: 如果SOXX和SMH开盘首小时无法收复盘前跌幅的一半，且存储股继续跑输TSM和NVDA，则本轮下跌更可能属于拥挤交易去杠杆。 |
  confidence=medium | horizon=2026-07-13 US session | review_due=2026-07-14
  - expected: SOXX和SMH无法同步站回VWAP，存储股继续相对弱势。
  - invalidation: SOXX、SMH快速站回VWAP，存储股同步止跌且成交结构改善。
- F-20260713-06: 若油价和收益率继续上升，高估值AI与半导体将继续相对SPY承压，即使盈利预期暂未下修。 | confidence=medium_high |
  horizon=2026-07-13 to 2026-07-14 | review_due=2026-07-14
  - expected: 半导体和高估值科技相对SPY走弱。
  - invalidation: 油价和收益率上升但半导体仍形成广泛持续的相对强势。
- F-20260713-07: SKHY ADR与韩国本股的定价差异将在未来数日继续放大波动，普通技术支撑暂时失真。 | confidence=high | horizon=1-5
  trading days | review_due=2026-07-20
  - expected: ADR、本股和相关杠杆产品继续出现异常价差与高波动。
  - invalidation: 价差显著收敛，套利与成交机制恢复稳定。

### Candidate Conditions

- No buy precheck candidates supplied by GPT overlay.

### Review Due Forecast Claims

- No overdue unreviewed forecast claims.

## Your Role

You are the Investment Reasoning Layer.

Analyze:

- macro backdrop
- industry and supply-chain logic
- company fundamentals
- valuation expectations
- news/catalyst durability
- risk and invalidation
- what needs manual broker confirmation before any real trade

Codex is the Market Perception Layer.
Treat Codex outputs as market data, technical state, risk flags, and source-quality metadata.
Maintain continuity: review your previous thesis ledger and forecast ledger when available.
If GPT overlay continuity is gapped, do not invent missing forecasts or decisions.

## Hard Boundaries

- Do not issue unconditional buy or sell instructions.
- Do not overwrite `raw_score`, `price`, `vwap`, `data_quality`, `execution_level`, or
  `risk_reasons`.
- Do not upgrade anything to fully executable trading unless realtime broker data is explicitly
  confirmed.
- Current automated ceiling is `L3_MANUAL_CONFIRM_REQUIRED`.
- Separate observed fact, plausible inference, and weak speculation.
- If data is stale, missing, proxy-only, or contradictory, say so directly.
- GPT overlay can only be a research-layer patch; it cannot trigger real trades.
- Missing overlay days are allowed and must not block Codex refreshes.

## Questions To Answer

- Is current strength broad-based, or driven by a narrow group of AI, semiconductor, and
  infrastructure leaders?
- Which moves are supported by durable fundamental catalysts, and which are mainly news spikes
  or crowded trades?
- Are high-score names extended away from VWAP/opening range, or still near a reasonable
  support-check zone?
- Please judge whether the support behind these leaders is durable: MU, AVGO, ARM, SOXX, QQQ.
- Separate data-quality/execution-boundary risks from true market risks.

## Required Output

Return a concise continuity-aware committee response in Chinese with these sections:

1. `Decision`: one of NO_TRADE, INDEX_DCA_ONLY, HOLD_EXISTING, BUY_PRECHECK_1, BUY_PRECHECK_2,
   or RISK_REDUCTION_REVIEW.
2. `What Changed`: only the meaningful changes versus the latest valid GPT baseline.
3. `Thesis Ledger Review`: maintain durable thesis entries rather than replacing themes daily.
4. `Forecast Review`: review prior forecast claims as correct, partially_correct, wrong,
   unverifiable, or unverifiable_due_to_gap.
5. `Candidate Conditions`: buy-precheck candidates, expected observations, invalidation, and
   review_due.
6. `Risks`: macro, event, technical, valuation, data-quality, and execution-boundary risks.

Then output one machine-readable JSON block:

```json
{
  "gpt_overlay": {
    "date": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DDTHH:MM:SS",
    "stage": "premarket | postmarket",
    "source": "gpt_investment_committee",
    "decision": "NO_TRADE | INDEX_DCA_ONLY | HOLD_EXISTING | BUY_PRECHECK_1 | BUY_PRECHECK_2 | RISK_REDUCTION_REVIEW",
    "decision_reason": "string",
    "continuity": {
      "status": "continuous | gapped | new_baseline",
      "last_available_overlay_date": "YYYY-MM-DD or null",
      "gap_days": 0
    },
    "thesis_ledger": [
      {
        "thesis_id": "string",
        "thesis": "string",
        "status": "active | weakened | invalidated | retired",
        "supporting_evidence": ["string"],
        "counter_evidence": ["string"],
        "invalidation": "string"
      }
    ],
    "forecast_ledger": [
      {
        "claim_id": "string",
        "claim": "string",
        "confidence": "low | medium | high",
        "horizon": "string",
        "expected_observation": "string",
        "invalidation": "string",
        "review_due": "YYYY-MM-DD",
        "review_status": "pending | correct | partially_correct | wrong | unverifiable | unverifiable_due_to_gap"
      }
    ],
    "buy_precheck_candidates": [
      {
        "ticker": "string",
        "expected_observation": "string",
        "invalidation": "string",
        "review_due": "YYYY-MM-DD"
      }
    ],
    "candidate_overrides": [
      {
        "ticker": "string",
        "action": "near_entry_watch | wait_for_pullback | do_not_chase | high_risk_skip",
        "reason": "string",
        "invalidation": "string",
        "confidence": "low | medium | high"
      }
    ],
    "do_not_overwrite": [
      "raw_score",
      "price",
      "vwap",
      "data_quality",
      "execution_level",
      "risk_reasons"
    ]
  }
}
```

## Current Snapshot Summary

- Leaders available: 20
- Watchlist rows available: 20
- Risk flags available: 5
- Signals available: 12

Top leaders from Codex:
- `MU` Micron | chain=memory_hbm_storage | score=13.92 | exec=L3_MANUAL |
  flag=closed_market_eod_proxy
- `AVGO` Broadcom | chain=custom_silicon_networking | score=13.47 | exec=L3_MANUAL |
  flag=closed_market_eod_proxy
- `ARM` Arm Holdings | chain=ai_accelerator | score=13.34 | exec=L1 |
  flag=closed_market_eod_proxy
- `SOXX` iShares Semiconductor ETF | chain=semiconductor_index | score=12.98 | exec=L1 |
  flag=closed_market_eod_proxy
- `QQQ` Nasdaq 100 ETF | chain=market_regime | score=12.57 | exec=L1 |
  flag=closed_market_eod_proxy
- `TT` Trane Technologies | chain=data_center_power_cooling | score=11.98 | exec=L3_MANUAL |
  flag=closed_market_eod_proxy
- `ASML` ASML Holding | chain=semiconductor_equipment | score=11.62 | exec=L3_MANUAL |
  flag=closed_market_eod_proxy
- `JCI` Johnson Controls | chain=data_center_power_cooling | score=11.53 | exec=L3_MANUAL |
  flag=closed_market_eod_proxy
