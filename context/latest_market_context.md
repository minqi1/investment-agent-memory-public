# Market Overview

Generated: 2026-07-13T20:48:56
Stage: premarket | Report date: 2026-07-13

## Market Regime

当前市场状态：`data_quality_caution`

- Snapshot stage: premarket
- Snapshot generated at: 2026-07-13T20:48:52
- Execution boundary: L3_MANUAL_CONFIRM_REQUIRED
- Monitor fresh/stale: 37/19

## Index

- `QQQ` Nasdaq 100 ETF
  - price: 717.41
  - VWAP: 714.6926610159277
  - above_vwap: True
  - caution: price_stale_or_missing
- `SPY` S&P 500 ETF
  - price: 751.81
  - VWAP: 748.5993418751976
  - above_vwap: True
  - caution: price_stale_or_missing
- `SOXX` iShares Semiconductor ETF
  - price: 562.9734
  - VWAP: 565.9909318112418
  - above_vwap: False
  - caution: below_vwap
- `SMH` VanEck Semiconductor ETF
  - price: 596.496
  - VWAP: 592.9791113907456
  - above_vwap: True
  - caution: spread_missing
- `IWM` Russell 2000 ETF
  - above_vwap: False
  - caution: below_vwap

## Leaders

- `ARM` Arm Holdings
  - chain: ai_accelerator
  - price: 313.52
  - VWAP: 313.35
  - score: 43.34
  - level: L1
  - caution: spread_missing
- `AMZN` Amazon
  - chain: cloud_ai_capex
  - price: 244.65
  - VWAP: 244.43
  - score: 41.09
  - level: L1
  - caution: spread_missing
- `STX` Seagate
  - chain: memory_hbm_storage
  - price: 870.60
  - VWAP: 868.31
  - score: 37.08
  - level: L1
  - caution: spread_missing
- `SMH` VanEck Semiconductor ETF
  - chain: semiconductor_index
  - price: 596.50
  - VWAP: 592.98
  - score: 24.73
  - level: L1
  - caution: spread_missing
- `MSFT` Microsoft
  - chain: cloud_ai_capex
  - price: 387.33
  - VWAP: 385.21
  - score: 24.28
  - level: L3_MANUAL
  - caution: spread_missing
- `AVGO` Broadcom
  - chain: custom_silicon_networking
  - price: 393.30
  - VWAP: 388.07
  - score: 1.47
  - level: L3_MANUAL
  - caution: spread_missing
- `TT` Trane Technologies
  - chain: data_center_power_cooling
  - score: -6.02
  - level: L3_MANUAL
  - caution: below_vwap
- `JCI` Johnson Controls
  - chain: data_center_power_cooling
  - score: -6.47
  - level: L3_MANUAL
  - caution: below_vwap
- `KLAC` KLA
  - chain: semiconductor_equipment
  - score: -6.69
  - level: L3_MANUAL
  - caution: below_vwap
- `PWR` Quanta Services
  - chain: data_center_power_cooling
  - score: -7.23
  - level: L3_MANUAL
  - caution: below_vwap
- `VRT` Vertiv
  - chain: data_center_power_cooling
  - score: -7.37
  - level: L3_MANUAL
  - caution: below_vwap
- `AMAT` Applied Materials
  - chain: semiconductor_equipment
  - score: -7.41
  - level: L3_MANUAL
  - caution: below_vwap

## Technical State

- `ARM`
  - price: 313.52
  - VWAP: 313.35
  - above_vwap: True
  - caution: spread_missing
  - execution: L1
- `AMZN`
  - price: 244.65
  - VWAP: 244.43
  - above_vwap: True
  - caution: spread_missing
  - execution: L1
- `STX`
  - price: 870.60
  - VWAP: 868.31
  - above_vwap: True
  - caution: spread_missing
  - execution: L1
- `SMH`
  - price: 596.50
  - VWAP: 592.98
  - above_vwap: True
  - caution: spread_missing
  - execution: L1
- `MSFT`
  - price: 387.33
  - VWAP: 385.21
  - above_vwap: True
  - caution: spread_missing
  - execution: L3_MANUAL
- `AVGO`
  - price: 393.30
  - VWAP: 388.07
  - above_vwap: True
  - caution: spread_missing
  - execution: L3_MANUAL
- `TT`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL
- `JCI`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL

## GPT Overlay Continuity

- GPT overlay unavailable; establish a new baseline.

## Risk Factors

- high: data_freshness - fresh=37, stale=19, stale_ratio=33.93%
- medium: execution_boundary - Automated output is capped at L3_MANUAL_CONFIRM_REQUIRED unless
  broker realtime
  data is verified.
- medium: market_or_data_caution - below_vwap: 30
- medium: market_or_data_caution - price_stale_or_missing: 19
- medium: market_or_data_caution - spread_too_wide_or_missing: 7
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
- Please judge whether the support behind these leaders is durable: ARM, AMZN, STX, SMH, MSFT.
- Separate data-quality/execution-boundary risks from true market risks.

## Source Files

- Redacted in public bridge.
