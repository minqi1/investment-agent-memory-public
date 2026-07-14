# Market Overview

Generated: 2026-07-14T09:02:01
Stage: eod | Report date: 2026-07-14

## Market Regime

当前市场状态：`weak_breadth_or_pullback`

- Snapshot stage: postmarket_review
- Snapshot generated at: 2026-07-14T09:01:56
- Execution boundary: L3_MANUAL_CONFIRM_REQUIRED
- Monitor fresh/stale: 56/0

## Index

- `QQQ` Nasdaq 100 ETF
  - above_vwap: False
  - caution: closed_market_eod_proxy
- `SPY` S&P 500 ETF
  - above_vwap: False
  - caution: closed_market_eod_proxy
- `SOXX` iShares Semiconductor ETF
  - above_vwap: False
  - caution: closed_market_eod_proxy
- `SMH` VanEck Semiconductor ETF
  - above_vwap: False
  - caution: closed_market_eod_proxy
- `IWM` Russell 2000 ETF
  - above_vwap: False
  - caution: closed_market_eod_proxy

## Leaders

- `MU` Micron
  - chain: memory_hbm_storage
  - score: 13.92
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `AVGO` Broadcom
  - chain: custom_silicon_networking
  - score: 13.47
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `ARM` Arm Holdings
  - chain: ai_accelerator
  - score: 13.34
  - level: L1
  - caution: closed_market_eod_proxy
- `SOXX` iShares Semiconductor ETF
  - chain: semiconductor_index
  - score: 12.98
  - level: L1
  - caution: closed_market_eod_proxy
- `QQQ` Nasdaq 100 ETF
  - chain: market_regime
  - score: 12.57
  - level: L1
  - caution: closed_market_eod_proxy
- `TT` Trane Technologies
  - chain: data_center_power_cooling
  - score: 11.98
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `ASML` ASML Holding
  - chain: semiconductor_equipment
  - score: 11.62
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `JCI` Johnson Controls
  - chain: data_center_power_cooling
  - score: 11.53
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `KLAC` KLA
  - chain: semiconductor_equipment
  - score: 11.31
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `NVDA` NVIDIA
  - chain: ai_accelerator
  - score: 11.13
  - level: L1
  - caution: closed_market_eod_proxy
- `AMZN` Amazon
  - chain: cloud_ai_capex
  - score: 11.09
  - level: L1
  - caution: closed_market_eod_proxy
- `SPY` S&P 500 ETF
  - chain: market_regime
  - score: 10.86
  - level: L1
  - caution: closed_market_eod_proxy

## Technical State

- `MU`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `AVGO`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `ARM`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L1
- `SOXX`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L1
- `QQQ`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L1
- `TT`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `ASML`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `JCI`
  - above_vwap: False
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL

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
  confidence=medium |
  horizon=2026-07-13 US session | review_due=2026-07-14
  - expected: SOXX和SMH无法同步站回VWAP，存储股继续相对弱势。
  - invalidation: SOXX、SMH快速站回VWAP，存储股同步止跌且成交结构改善。
- F-20260713-06: 若油价和收益率继续上升，高估值AI与半导体将继续相对SPY承压，即使盈利预期暂未下修。 | confidence=medium_high |
  horizon=2026-07-13 to
  2026-07-14 | review_due=2026-07-14
  - expected: 半导体和高估值科技相对SPY走弱。
  - invalidation: 油价和收益率上升但半导体仍形成广泛持续的相对强势。
- F-20260713-07: SKHY ADR与韩国本股的定价差异将在未来数日继续放大波动，普通技术支撑暂时失真。 | confidence=high | horizon=1-5
  trading days |
  review_due=2026-07-20
  - expected: ADR、本股和相关杠杆产品继续出现异常价差与高波动。
  - invalidation: 价差显著收敛，套利与成交机制恢复稳定。

### Candidate Conditions

- No buy precheck candidates supplied by GPT overlay.

### Review Due Forecast Claims

- No overdue unreviewed forecast claims.

## Risk Factors

- low: data_freshness - fresh=56, stale=0, stale_ratio=0.00%
- medium: execution_boundary - Automated output is capped at L3_MANUAL_CONFIRM_REQUIRED unless
  broker realtime
  data is verified.
- medium: market_or_data_caution - below_vwap: 2
- medium: market_or_data_caution - closed_market_eod_proxy: 54
- info: market_breadth - latest breadth cache present; generated_at=2026-07-09T23:31:33

## Watch Items

- `ARM` Arm Holdings
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `NVDA` NVIDIA
  - tier: A_CORE
  - action: research_watch
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `TSM` TSMC ADR
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `ASML` ASML Holding
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `KLAC` KLA
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `ANET` Arista Networks
  - tier: B_HIGH_BETA
  - action: core_watch_wait_for_pullback
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `MU` Micron
  - tier: B_HIGH_BETA
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `AVGO` Broadcom
  - tier: A_CORE
  - action: research_watch
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `TT` Trane Technologies
  - tier: B_HIGH_BETA
  - action: core_watch_wait_for_pullback
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `AMAT` Applied Materials
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `ALAB` Astera Labs
  - tier: B_HIGH_BETA
  - action: core_watch_wait_for_pullback
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `LRCX` Lam Research
  - tier: B_HIGH_BETA
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.

## Questions For Investment Committee

- Is current strength broad-based, or driven by a narrow group of AI, semiconductor, and
  infrastructure
  leaders?
- Which moves are supported by durable fundamental catalysts, and which are mainly news spikes
  or crowded
  trades?
- Are high-score names extended away from VWAP/opening range, or still near a reasonable
  support-check zone?
- Please judge whether the support behind these leaders is durable: MU, AVGO, ARM, SOXX, QQQ.
- Separate data-quality/execution-boundary risks from true market risks.

## Source Files

- Redacted in public bridge.
