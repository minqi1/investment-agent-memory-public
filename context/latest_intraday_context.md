# Latest Intraday Context

- generated_at: `2026-07-14T21:50:02+08:00`
- stage: `intraday`
- Beijing time: `2026-07-14T21:50:02+08:00`
- US Eastern time: `2026-07-14T09:50:02-04:00`
- US session date: `2026-07-14`
- is_open: `True`
- market_clock_source: `Alpaca trading clock`

## Safety Boundary

- No automated trading.
- Real-trade boundary remains `L3_MANUAL_CONFIRM_REQUIRED` / manual confirmation only.
- Do not overwrite `raw_score`, `data_quality`, `execution_level`, or `risk_reasons`.

## Data Quality

- total_rows: `56`
- index_symbols_present: `['QQQ', 'SMH', 'SOXX', 'SPY']`
- price_coverage: `55`
- vwap_coverage: `55`
- stale_count: `1`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- l4_blocked_reason: `Broker realtime execution gate is not satisfied; ALPACA_IEX_ONLY/proxy
  data supports research and manual confirmation only.`

## Indices

- `QQQ` price=719.25 VWAP=718.7246 open15=720.15/717.26 spread=0.0389% lag=2.02m
  risk=not_above_opening_15m_high
- `SPY` price=750.89 VWAP=750.5578 open15=751.5/749.54 spread=0.004% lag=2.02m
  risk=not_above_opening_15m_high
- `SMH` price=599.97 VWAP=600.7562 open15=608.895/596.44 spread=0.0883% lag=2.02m
  risk=below_vwap,not_above_opening_15m_high
- `SOXX` price=571.74 VWAP=573.0194 open15=580.67/567.78 spread=0.1032% lag=2.02m
  risk=below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=52.3 | price=719.25 | VWAP=718.7246 | open15=720.15/717.26 |
  spread=0.0389% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.204pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.2964pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=571.74 | VWAP=573.0194 |
  open15=580.67/567.78 | spread=0.1032% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.2964pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.0924pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=599.97 | VWAP=600.7562 |
  open15=608.895/596.44 | spread=0.0883% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.204pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.0924pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SPY` S&P 500 ETF | raw_score=50.9 | price=750.89 | VWAP=750.5578 | open15=751.5/749.54 |
  spread=0.004% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.0288pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.1751pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.2675pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `NVDA` NVIDIA | raw_score=57.2 | price=204.6 | VWAP=205.377 | open15=208.25/203.84 |
  spread=0.3617% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.4514pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.2475pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.155pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `MU` Micron | raw_score=54.9 | price=979.98 | VWAP=980.8301 | open15=994.7/967.665 |
  spread=0.5388% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.1598pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.0442pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.1366pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `CIEN` Ciena | raw_score=54.8 | price=464.5 | VWAP=460.7055 | open15=463.28/458.1 | spread=% |
  level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.7505pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.9545pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=1.0469pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
- `AVGO` Broadcom | raw_score=53.7 | price=389.83 | VWAP=388.3782 | open15=394.65/384.665 |
  spread=2.2907% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.3007pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.5047pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.5971pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `ANET` Arista Networks | raw_score=53.7 | price=183.315 | VWAP=181.7201 | open15=185.24/175.76
  | spread=4.5932% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.8046pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=1.0085pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=1.1009pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `ASML` ASML Holding | raw_score=52.4 | price=1783.66 | VWAP=1781.1285 |
  open15=1792.835/1768.71 | spread=0.7075% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.069pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.273pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.3654pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `AMAT` Applied Materials | raw_score=51 | price=598 | VWAP=600.3309 | open15=613.945/594.87 |
  spread=0.214% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=-0.4614pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.2574pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.165pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `TT` Trane Technologies | raw_score=50.3 | price=486.5 | VWAP=488.0668 | open15=490.755/486.16
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 3.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_unavailable`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.3941pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.1901pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.0977pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SKHY` SK hynix ADR | raw_score=39.1 | price=169.67 | VWAP=168.7553 | open15=170.74/166.91 |
  spread=1.1788% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.02, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.4689pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.6729pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.7653pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
