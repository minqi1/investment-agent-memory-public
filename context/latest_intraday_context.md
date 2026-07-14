# Latest Intraday Context

- generated_at: `2026-07-14T22:28:16+08:00`
- stage: `intraday`
- Beijing time: `2026-07-14T22:28:16+08:00`
- US Eastern time: `2026-07-14T10:28:16-04:00`
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

- `QQQ` price=717.84 VWAP=718.069 open15=720.15/717.26 spread=0.0098% lag=2.23m
  risk=below_vwap,not_above_opening_15m_high
- `SPY` price=750.74 VWAP=750.455 open15=751.5/749.54 spread=0.008% lag=2.23m
  risk=not_above_opening_15m_high
- `SMH` price=596.06 VWAP=597.6212 open15=608.895/596.44 spread=0.104% lag=2.23m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SOXX` price=565.84 VWAP=570.7781 open15=580.67/567.78 spread=0.1202% lag=2.23m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=52.3 | price=717.84 | VWAP=718.069 | open15=720.15/717.26 |
  spread=0.0098% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.2293pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.8333pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `MSFT` Microsoft | raw_score=47.7 | price=384.315 | VWAP=382.8502 | open15=383.4/378.71 |
  spread=0.1535% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.4145pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.6438pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.2478pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `GOOGL` Alphabet | raw_score=49 | price=356.27 | VWAP=353.9667 | open15=354.29/351.19 |
  spread=0.3116% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.6826pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.9119pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.5159pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=565.84 | VWAP=570.7781 |
  open15=580.67/567.78 | spread=0.1202% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.8333pct; above_vwap=False/False;
    open15=below_opening_15m_low/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.6039pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=596.06 | VWAP=597.6212 |
  open15=608.895/596.44 | spread=0.104% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.2293pct; above_vwap=False/False;
    open15=below_opening_15m_low/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.6039pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SPY` S&P 500 ETF | raw_score=50.9 | price=750.74 | VWAP=750.455 | open15=751.5/749.54 |
  spread=0.008% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.0699pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.2992pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.9031pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `NVDA` NVIDIA | raw_score=57.2 | price=205.8 | VWAP=205.1494 | open15=208.25/203.84 |
  spread=0.0194% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=0.349pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.5784pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.1823pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `MU` Micron | raw_score=54.9 | price=963.275 | VWAP=971.6708 | open15=994.7/967.665 |
  spread=0.5294% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.8322pct; above_vwap=False/False;
    open15=below_opening_15m_low/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.6028pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.0011pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `CIEN` Ciena | raw_score=54.8 | price=461.735 | VWAP=461.6282 | open15=463.28/458.1 | spread=%
  | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.055pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.2844pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.8883pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `AVGO` Broadcom | raw_score=53.7 | price=393.29 | VWAP=389.7313 | open15=394.65/384.665 |
  spread=0.0661% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=0.945pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=1.1743pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.7783pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `ANET` Arista Networks | raw_score=53.7 | price=184.06 | VWAP=182.4453 | open15=185.24/175.76
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.9169pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=1.1463pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.7502pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `ASML` ASML Holding | raw_score=52.4 | price=1769.1 | VWAP=1776.1178 | open15=1792.835/1768.71
  | spread=0.3861% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.3632pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.1339pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.47pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `AMAT` Applied Materials | raw_score=51 | price=593.02 | VWAP=595.7866 | open15=613.945/594.87
  | spread=4.3506% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.4325pct; above_vwap=False/False;
    open15=below_opening_15m_low/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.2031pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.4008pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `TT` Trane Technologies | raw_score=50.3 | price=483.34 | VWAP=485.7813 |
  open15=490.755/482.83 | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_unavailable`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.4707pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.2413pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.3626pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `SKHY` SK hynix ADR | raw_score=39.1 | price=169.69 | VWAP=169.1106 | open15=170.74/166.91 |
  spread=0.884% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.23, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.3745pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.6039pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.2078pct; above_vwap=True/False;
    open15=inside_opening_15m_range/below_opening_15m_low
