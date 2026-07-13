# Latest Intraday Context

- generated_at: `2026-07-13T22:06:39+08:00`
- stage: `intraday`
- Beijing time: `2026-07-13T22:06:39+08:00`
- US Eastern time: `2026-07-13T10:06:39-04:00`
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

- `QQQ` price=714.5 VWAP=714.9913 open15=718.255/713.97 spread=0.0336% lag=1.64m
  risk=below_vwap,not_above_opening_15m_high
- `SPY` price=752.62 VWAP=753.0669 open15=753.835/752.42 spread=0.085% lag=1.64m
  risk=below_vwap,not_above_opening_15m_high
- `SMH` price=591.99 VWAP=592.177 open15=598.55/589.01 spread=0.0389% lag=1.64m
  risk=below_vwap,not_above_opening_15m_high
- `SOXX` price=558.97 VWAP=558.5208 open15=564.7/554.59 spread=0.0948% lag=2.64m
  risk=not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=54.6 | price=714.5 | VWAP=714.9913 | open15=718.255/713.97 |
  spread=0.0336% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.0371pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.1491pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SOXX` iShares Semiconductor ETF | raw_score=55.5 | price=558.97 | VWAP=558.5208 |
  open15=564.7/554.59 | spread=0.0948% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.1491pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.112pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SMH` VanEck Semiconductor ETF | raw_score=50.5 | price=591.99 | VWAP=592.177 |
  open15=598.55/589.01 | spread=0.0389% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.0371pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.112pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SPY` S&P 500 ETF | raw_score=50.8 | price=752.62 | VWAP=753.0669 | open15=753.835/752.42 |
  spread=0.085% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.0094pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.0278pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.1398pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `MU` Micron | raw_score=57.6 | price=922.72 | VWAP=917.5611 | open15=929.76/903 |
  spread=0.6134% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.631pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.5938pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.4818pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `AVGO` Broadcom | raw_score=56.6 | price=390.84 | VWAP=389.6787 | open15=394.81/387.98 |
  spread=0.1586% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=0.3667pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.3296pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.2176pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `TT` Trane Technologies | raw_score=53.3 | price=480.64 | VWAP=478.2723 | open15=479.64/473.03
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.5638pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.5266pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.4146pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `ASML` ASML Holding | raw_score=52.5 | price=1751.85 | VWAP=1750.2006 |
  open15=1774.255/1738.94 | spread=0.6719% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.163pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.1258pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.0138pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `JCI` Johnson Controls | raw_score=52.3 | price=143.69 | VWAP=143.2113 | open15=143.43/140.87
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 5.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide_or_missing, spread_unavailable`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.403pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.3659pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.2539pct; above_vwap=True/True;
    open15=above_opening_15m_high/inside_opening_15m_range
- `KLAC` KLA | raw_score=51.8 | price=222.135 | VWAP=221.6829 | open15=225.15/219.8 |
  spread=0.081% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=0.2726pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.2355pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.1235pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `PWR` Quanta Services | raw_score=50.6 | price=646.28 | VWAP=647.532 | open15=652.475/643.23 |
  spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_unavailable`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.1246pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.1618pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.2738pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `GEV` GE Vernova | raw_score=50.6 | price=1059.715 | VWAP=1066.0865 | open15=1087.78/1054.39 |
  spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_unavailable`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.5289pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.5661pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.6781pct; above_vwap=False/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SKHY` SK hynix ADR | raw_score=42.3 | price=155.73 | VWAP=155.6083 | open15=156.7/152.425 |
  spread=2.8896% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high, spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high, spread_available_and_acceptable,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.1469pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.1098pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.0022pct; above_vwap=True/True;
    open15=inside_opening_15m_range/inside_opening_15m_range
