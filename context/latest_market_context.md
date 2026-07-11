# Market Overview

Generated: 2026-07-11T09:01:37
Stage: eod | Report date: 2026-07-11

## Market Regime

当前市场状态：`tech_led_risk_on`

- Snapshot stage: postmarket_review
- Snapshot generated at: 2026-07-11T09:01:34
- Execution boundary: L3_MANUAL_CONFIRM_REQUIRED
- Monitor fresh/stale: 55/1

## Index

- `QQQ` Nasdaq 100 ETF
  - price: 726.27
  - VWAP: 723.7237227281722
  - above_vwap: True
  - caution: closed_market_eod_proxy
- `SPY` S&P 500 ETF
  - price: 755.1
  - VWAP: 753.6647630684664
  - above_vwap: True
  - caution: closed_market_eod_proxy
- `SOXX` iShares Semiconductor ETF
  - price: 581.13
  - VWAP: 578.3430980620037
  - above_vwap: True
  - caution: closed_market_eod_proxy
- `SMH` VanEck Semiconductor ETF
  - price: 611.42
  - VWAP: 607.1186391690582
  - above_vwap: True
  - caution: closed_market_eod_proxy
- `IWM` Russell 2000 ETF
  - price: 296.03
  - VWAP: 295.6958146782682
  - above_vwap: True
  - caution: closed_market_eod_proxy

## Leaders

- `SPY` S&P 500 ETF
  - chain: market_regime
  - price: 755.10
  - VWAP: 753.66
  - score: 71.55
  - level: L1
  - caution: closed_market_eod_proxy
- `MU` Micron
  - chain: memory_hbm_storage
  - price: 980.68
  - VWAP: 977.34
  - score: 69.10
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `CIEN` Ciena
  - chain: ai_networking_optical
  - price: 460.74
  - VWAP: 460.69
  - score: 67.30
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `ASML` ASML Holding
  - chain: semiconductor_equipment
  - price: 1797.32
  - VWAP: 1797.30
  - score: 66.49
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `PWR` Quanta Services
  - chain: data_center_power_cooling
  - price: 658.46
  - VWAP: 657.55
  - score: 65.91
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `MRVL` Marvell Technology
  - chain: custom_silicon_networking
  - price: 236.84
  - VWAP: 236.16
  - score: 65.19
  - level: L1
  - caution: closed_market_eod_proxy
- `ALAB` Astera Labs
  - chain: ai_networking_optical
  - price: 412.65
  - VWAP: 412.31
  - score: 65.09
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `ENTG` Entegris
  - chain: semiconductor_materials
  - price: 145.34
  - VWAP: 144.90
  - score: 64.11
  - level: L3_MANUAL
  - caution: closed_market_eod_proxy
- `IWM` Russell 2000 ETF
  - chain: market_regime
  - price: 296.03
  - VWAP: 295.70
  - score: 63.43
  - level: L1
  - caution: closed_market_eod_proxy
- `APD` Air Products
  - chain: industrial_gases
  - price: 299.48
  - VWAP: 299.27
  - score: 63.34
  - level: L1
  - caution: closed_market_eod_proxy
- `TER` Teradyne
  - chain: semiconductor_test_packaging
  - price: 359.61
  - VWAP: 358.42
  - score: 62.94
  - level: L1
  - caution: closed_market_eod_proxy
- `META` Meta Platforms
  - chain: cloud_ai_capex
  - price: 669.25
  - VWAP: 668.87
  - score: 61.23
  - level: L1
  - caution: closed_market_eod_proxy

## Technical State

- `SPY`
  - price: 755.10
  - VWAP: 753.66
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L1
- `MU`
  - price: 980.68
  - VWAP: 977.34
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `CIEN`
  - price: 460.74
  - VWAP: 460.69
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `ASML`
  - price: 1797.32
  - VWAP: 1797.30
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `PWR`
  - price: 658.46
  - VWAP: 657.55
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `MRVL`
  - price: 236.84
  - VWAP: 236.16
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L1
- `ALAB`
  - price: 412.65
  - VWAP: 412.31
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL
- `ENTG`
  - price: 145.34
  - VWAP: 144.90
  - above_vwap: True
  - caution: closed_market_eod_proxy
  - execution: L3_MANUAL

## Risk Factors

- low: data_freshness - fresh=55, stale=1, stale_ratio=1.79%
- medium: execution_boundary - Automated output is capped at L3_MANUAL_CONFIRM_REQUIRED unless broker realtime
  data is verified.
- medium: market_or_data_caution - below_vwap: 1
- medium: market_or_data_caution - closed_market_eod_proxy: 54
- medium: market_or_data_caution - price_stale_or_missing: 1
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
- Please judge whether the support behind these leaders is durable: SPY, MU, CIEN, ASML, PWR.
- Separate data-quality/execution-boundary risks from true market risks.

## Source Files

- Redacted in public bridge.
