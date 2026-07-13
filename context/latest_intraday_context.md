# Latest Intraday Context

- generated_at: `2026-07-13T23:06:07+08:00`
- stage: `intraday`
- Beijing time: `2026-07-13T23:06:07+08:00`
- US Eastern time: `2026-07-13T11:06:07-04:00`
- US session date: `2026-07-13`
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

- `QQQ` price=718.15 VWAP=715.443 open15=718.255/713.97 spread=0.046% lag=2.11m
  risk=not_above_opening_15m_high
- `SPY` price=752.31 VWAP=752.5978 open15=753.835/752.42 spread=0.004% lag=2.11m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SMH` price=596.42 VWAP=593.4267 open15=598.55/589.01 spread=0.0537% lag=2.11m
  risk=not_above_opening_15m_high
- `SOXX` price=562.85 VWAP=559.9701 open15=564.7/554.59 spread=0.0835% lag=2.11m
  risk=not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=54.6 | price=718.15 | VWAP=715.443 | open15=718.255/713.97 |
  spread=0.046% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.126pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.1359pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SOXX` iShares Semiconductor ETF | raw_score=55.5 | price=562.85 | VWAP=559.9701 |
  open15=564.7/554.59 | spread=0.0835% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.1359pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.0099pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SMH` VanEck Semiconductor ETF | raw_score=50.5 | price=596.42 | VWAP=593.4267 |
  open15=598.55/589.01 | spread=0.0537% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.126pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.0099pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SPY` S&P 500 ETF | raw_score=50.8 | price=752.31 | VWAP=752.5978 | open15=753.835/752.42 |
  spread=0.004% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.4166pct; above_vwap=False/True;
    open15=below_opening_15m_low/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.5427pct; above_vwap=False/True;
    open15=below_opening_15m_low/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.5525pct; above_vwap=False/True;
    open15=below_opening_15m_low/inside_opening_15m_range
- `CRWV` CoreWeave | raw_score=40.4 | price=87.145 | VWAP=86.2726 | open15=86.94/84.51 |
  spread=0.1377% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.6328pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.5068pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.4969pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `AMAT` Applied Materials | raw_score=50.2 | price=585.885 | VWAP=579.0799 |
  open15=583.85/568.665 | spread=0.2065% | level=L3_MANUAL_CONFIRM_REQUIRED |
  allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.7968pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.6707pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.6609pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `WDC` Western Digital | raw_score=50.2 | price=558.725 | VWAP=544.9698 | open15=553.495/532.85
  | spread=0.1754% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=2.1457pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=2.0196pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=2.0097pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `AMZN` Amazon | raw_score=51.3 | price=249.11 | VWAP=247.2531 | open15=248.56/244.18 |
  spread=0.0442% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.3726pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.2466pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.2367pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `MU` Micron | raw_score=57.6 | price=941.545 | VWAP=925.8494 | open15=929.76/903 |
  spread=2.549% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=1.3169pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=1.1908pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=1.181pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `AVGO` Broadcom | raw_score=56.6 | price=391.1 | VWAP=390.7659 | open15=394.81/387.98 |
  spread=2.066% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.2929pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.4189pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.4288pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `TT` Trane Technologies | raw_score=53.3 | price=478.485 | VWAP=479.8442 |
  open15=479.64/473.03 | spread=4.648% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 4.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.6616pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.7877pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.7976pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `ASML` ASML Holding | raw_score=52.5 | price=1759.72 | VWAP=1752.2055 |
  open15=1774.255/1738.94 | spread=0.703% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 3.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.0505pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.0756pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.0854pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `JCI` Johnson Controls | raw_score=52.3 | price=143.95 | VWAP=143.3772 | open15=143.43/140.87
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 3.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.0211pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.1049pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.1148pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `KLAC` KLA | raw_score=51.8 | price=224.66 | VWAP=222.764 | open15=225.15/219.8 |
  spread=1.1573% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.4728pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.3467pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.3368pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `PWR` Quanta Services | raw_score=50.6 | price=647.12 | VWAP=646.9455 | open15=652.475/643.23
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.3514pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.4774pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.4873pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `GEV` GE Vernova | raw_score=50.6 | price=1060 | VWAP=1065.7028 | open15=1087.78/1054.39 |
  spread=4.9708% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.9135pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-1.0395pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-1.0494pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SKHY` SK hynix ADR | raw_score=42.3 | price=158.09 | VWAP=156.5278 | open15=156.7/152.425 |
  spread=1.9103% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.11, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.6197pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.4936pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.4838pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
