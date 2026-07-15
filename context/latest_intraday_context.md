# Latest Intraday Context

- generated_at: `2026-07-16T01:19:21+08:00`
- stage: `intraday`
- Beijing time: `2026-07-16T01:19:21+08:00`
- US Eastern time: `2026-07-15T13:19:21-04:00`
- US session date: `2026-07-15`
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

- `QQQ` price=713.69 VWAP=716.2596 open15=724.31/721.08 spread=0.0308% lag=1.77m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SPY` price=751.98 VWAP=753.1559 open15=755.54/754.215 spread=0.0173% lag=1.77m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SMH` price=581.97 VWAP=587.3393 open15=606.85/597.81 spread=0.0705% lag=1.77m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SOXX` price=547.1 VWAP=551.1224 open15=575.7/565.33 spread=0.0896% lag=2.77m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=46.3 | price=713.69 | VWAP=716.2596 | open15=724.31/721.08 |
  spread=0.0308% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.5554pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.3711pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MSFT` Microsoft | raw_score=47.8 | price=395.91 | VWAP=395.0394 | open15=391.33/387.05 |
  spread=0.0783% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.5791pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.1346pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.9502pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `AAPL` Apple | raw_score=39.1 | price=326.635 | VWAP=325.2645 | open15=321.14/317.4 |
  spread=0.0092% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.7801pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.3355pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.1512pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `GOOGL` Alphabet | raw_score=43.1 | price=370.98 | VWAP=368.4743 | open15=364.41/357.885 |
  spread=0.0216% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.0388pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.5942pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.4099pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=547.1 | VWAP=551.1224 |
  open15=575.7/565.33 | spread=0.0896% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.3711pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.1843pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=581.97 | VWAP=587.3393 |
  open15=606.85/597.81 | spread=0.0705% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.5554pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.1843pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SPY` S&P 500 ETF | raw_score=50.9 | price=751.98 | VWAP=753.1559 | open15=755.54/754.215 |
  spread=0.0173% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.2026pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.758pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.5737pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMZN` Amazon | raw_score=41.2 | price=255.325 | VWAP=254.4071 | open15=252.89/249.98 |
  spread=0.0157% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.7196pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.275pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.0907pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `NVDA` NVIDIA | raw_score=57.2 | price=208.21 | VWAP=209.1612 | open15=213.775/211.225 |
  spread=0.0144% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-0.096pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.4594pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.2751pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MU` Micron | raw_score=54.9 | price=894.245 | VWAP=910.8054 | open15=977.7/953.67 |
  spread=0.1364% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-1.4595pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.904pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.0884pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `CIEN` Ciena | raw_score=54.8 | price=415.56 | VWAP=419.0164 | open15=438.14/427.54 | spread=%
  | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_unavailable`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.4661pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.0893pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.095pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AVGO` Broadcom | raw_score=53.7 | price=391.03 | VWAP=391.6617 | open15=397.94/392.62 |
  spread=1.7006% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.1975pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.7529pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.5686pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `ASML` ASML Holding | raw_score=52.5 | price=1767.61 | VWAP=1770.0125 | open15=1829.9/1759.045
  | spread=1.9212% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.223pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.7784pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.5941pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `ANET` Arista Networks | raw_score=51.3 | price=169.33 | VWAP=172.183 | open15=186.095/178.355
  | spread=1.7303% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.2982pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.7428pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.9271pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `STX` Seagate | raw_score=51.3 | price=800.75 | VWAP=818.2633 | open15=889.1/850.01 |
  spread=4.0624% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.7816pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.2261pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.4104pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMAT` Applied Materials | raw_score=51 | price=569.02 | VWAP=577.9728 | open15=610.62/586.86
  | spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_unavailable`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.1902pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.6348pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.8191pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SKHY` SK hynix ADR | raw_score=39.1 | price=173.175 | VWAP=175.6659 | open15=183.63/176.08 |
  spread=3.9844% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.77, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-1.0592pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.5038pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.6881pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
