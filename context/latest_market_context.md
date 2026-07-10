# Market Overview

Generated: 2026-07-10T21:11:27
Stage: premarket | Report date: 2026-07-10

## Market Regime

当前市场状态：`tech_led_risk_on`

- Snapshot stage: premarket
- Snapshot generated at: 2026-07-10T21:11:17
- Execution boundary: L3_MANUAL_CONFIRM_REQUIRED
- Monitor fresh/stale: 42/13

## Index

- `QQQ` Nasdaq 100 ETF
  - price: 721.17
  - VWAP: 714.7677748287466
  - above_vwap: True
  - caution: price_stale_or_missing
- `SPY` S&P 500 ETF
  - price: 751.89
  - VWAP: 748.0100208011644
  - above_vwap: True
  - caution: price_stale_or_missing
- `SOXX` iShares Semiconductor ETF
  - price: 574.98
  - VWAP: 568.7557947393174
  - above_vwap: True
  - caution: price_stale_or_missing
- `SMH` VanEck Semiconductor ETF
  - price: 602.16
  - VWAP: 594.6966685539421
  - above_vwap: True
  - caution: spread_missing
- `IWM` Russell 2000 ETF
  - price: 297.55
  - above_vwap: False
  - caution: price_stale_or_missing

## Leaders

- `MU` Micron
  - chain: memory_hbm_storage
  - price: 975.33
  - VWAP: 962.75
  - score: 2.10
  - level: L3_MANUAL
  - caution: spread_missing
- `SMH` VanEck Semiconductor ETF
  - chain: semiconductor_index
  - price: 602.16
  - VWAP: 594.70
  - score: 0.93
  - level: L1
  - caution: spread_missing
- `CIEN` Ciena
  - chain: ai_networking_optical
  - score: -5.70
  - level: L3_MANUAL
  - caution: below_vwap
- `AMAT` Applied Materials
  - chain: semiconductor_equipment
  - score: -5.92
  - level: L3_MANUAL
  - caution: below_vwap
- `TT` Trane Technologies
  - chain: data_center_power_cooling
  - score: -6.11
  - level: L3_MANUAL
  - caution: below_vwap
- `KLAC` KLA
  - chain: semiconductor_equipment
  - score: -6.42
  - level: L1
  - caution: below_vwap
- `LRCX` Lam Research
  - chain: semiconductor_equipment
  - score: -6.51
  - level: L3_MANUAL
  - caution: below_vwap
- `ONTO` Onto Innovation
  - chain: semiconductor_test_packaging
  - score: -6.55
  - level: L3_MANUAL
  - caution: below_vwap
- `VRT` Vertiv
  - chain: data_center_power_cooling
  - score: -6.73
  - level: L3_MANUAL
  - caution: below_vwap
- `JCI` Johnson Controls
  - chain: data_center_power_cooling
  - score: -6.83
  - level: L3_MANUAL
  - caution: below_vwap
- `ETN` Eaton
  - chain: data_center_power_cooling
  - score: -6.96
  - level: L3_MANUAL
  - caution: below_vwap
- `PWR` Quanta Services
  - chain: data_center_power_cooling
  - score: -7.09
  - level: L3_MANUAL
  - caution: below_vwap

## Technical State

- `MU`
  - price: 975.33
  - VWAP: 962.75
  - above_vwap: True
  - caution: spread_missing
  - execution: L3_MANUAL
- `SMH`
  - price: 602.16
  - VWAP: 594.70
  - above_vwap: True
  - caution: spread_missing
  - execution: L1
- `CIEN`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL
- `AMAT`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL
- `TT`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL
- `KLAC`
  - above_vwap: False
  - caution: below_vwap
  - execution: L1
- `LRCX`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL
- `ONTO`
  - above_vwap: False
  - caution: below_vwap
  - execution: L3_MANUAL

## Risk Factors

- low: data_freshness - fresh=42, stale=13, stale_ratio=23.64%
- medium: execution_boundary - Automated output is capped at L3_MANUAL_CONFIRM_REQUIRED unless broker realtime
  data is verified.
- medium: market_or_data_caution - below_vwap: 33
- medium: market_or_data_caution - price_stale_or_missing: 13
- medium: market_or_data_caution - spread_too_wide_or_missing: 9
- info: market_breadth - latest breadth cache present; generated_at=2026-07-09T23:31:33

## Watch Items

- `NVDA` NVIDIA
  - tier: A_CORE
  - action: research_watch
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `ARM` Arm Holdings
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `TSM` TSMC ADR
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
- `AMD` AMD
  - tier: B_HIGH_BETA
  - action: core_watch_wait_for_pullback
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `ALAB` Astera Labs
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
- `KLAC` KLA
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `000660.KS` SK Hynix
  - tier: B_HIGH_BETA
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `AMAT` Applied Materials
  - tier: A_CORE
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `MRVL` Marvell Technology
  - tier: B_HIGH_BETA
  - action: watch_for_reclaim_and_support
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.
- `META` Meta Platforms
  - tier: B_HIGH_BETA
  - action: core_watch_wait_for_pullback
  - downgrade_if: Downgrade if earnings/order thesis is disproved, valuation rises without
    growth support,
    news risk becomes hard negative, or price loses medium-term trend support.

## Questions For Investment Committee

- Is current strength broad-based, or driven by a narrow group of AI, semiconductor, and infrastructure
  leaders?
- Which moves are supported by durable fundamental catalysts, and which are mainly news spikes or crowded
  trades?
- Are high-score names extended away from VWAP/opening range, or still near a reasonable support-check zone?
- Please judge whether the support behind these leaders is durable: MU, SMH, CIEN, AMAT, TT.
- Separate data-quality/execution-boundary risks from true market risks.

## Source Files

- Redacted in public bridge.
