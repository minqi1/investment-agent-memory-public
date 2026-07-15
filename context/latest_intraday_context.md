# Latest Intraday Context

- generated_at: `2026-07-16T01:01:40+08:00`
- stage: `intraday`
- Beijing time: `2026-07-16T01:01:40+08:00`
- US Eastern time: `2026-07-15T13:01:40-04:00`
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

- `QQQ` price=713.2 VWAP=716.3703 open15=724.31/721.08 spread=0.0743% lag=1.64m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SPY` price=751.94 VWAP=753.2064 open15=755.54/754.215 spread=0.0319% lag=1.64m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SMH` price=579.885 VWAP=587.4958 open15=606.85/597.81 spread=0.0448% lag=1.64m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SOXX` price=545 VWAP=551.4184 open15=575.7/565.33 spread=0.0642% lag=1.64m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=46.3 | price=713.2 | VWAP=716.3703 | open15=724.31/721.08 |
  spread=0.0743% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.8529pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.7214pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AAPL` Apple | raw_score=39.1 | price=327.865 | VWAP=325.149 | open15=321.14/317.4 |
  spread=0.0122% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.2779pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=2.1308pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.9993pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=545 | VWAP=551.4184 |
  open15=575.7/565.33 | spread=0.0642% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.7214pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.1315pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=579.885 | VWAP=587.4958 |
  open15=606.85/597.81 | spread=0.0448% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.8529pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.1315pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SPY` S&P 500 ETF | raw_score=50.9 | price=751.94 | VWAP=753.2064 | open15=755.54/754.215 |
  spread=0.0319% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.2744pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.1273pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.9958pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMZN` Amazon | raw_score=41.2 | price=255.645 | VWAP=254.368 | open15=252.89/249.98 |
  spread=0.0196% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.9446pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.7975pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.666pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `NVDA` NVIDIA | raw_score=57.2 | price=207.4 | VWAP=209.2294 | open15=213.775/211.225 |
  spread=0.053% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-0.4318pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.4211pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.2896pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MU` Micron | raw_score=54.9 | price=890.87 | VWAP=911.5946 | open15=977.7/953.67 |
  spread=1.1494% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.8309pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.978pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.1095pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `CIEN` Ciena | raw_score=54.8 | price=415.61 | VWAP=419.2002 | open15=438.14/427.54 |
  spread=4.254% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.4139pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.439pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.3075pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AVGO` Broadcom | raw_score=53.7 | price=389.88 | VWAP=391.6957 | open15=397.94/392.62 |
  spread=2.034% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.021pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.8319pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.7004pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `ASML` ASML Holding | raw_score=52.5 | price=1761.59 | VWAP=1770.1515 | open15=1829.9/1759.045
  | spread=1.6701% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.0411pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.8118pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.6803pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `ANET` Arista Networks | raw_score=51.3 | price=168.93 | VWAP=172.3403 |
  open15=186.095/178.355 | spread=0.2723% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-1.5363pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.6834pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.8148pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `STX` Seagate | raw_score=51.3 | price=802.85 | VWAP=819.3057 | open15=889.1/850.01 | spread=%
  | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_unavailable`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.566pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.713pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.8445pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMAT` Applied Materials | raw_score=51 | price=564.55 | VWAP=578.1852 | open15=610.62/586.86
  | spread=0.6306% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.9157pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.0628pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.1943pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SKHY` SK hynix ADR | raw_score=39.1 | price=173.13 | VWAP=175.7391 | open15=183.63/176.08 |
  spread=3.7255% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.64, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-1.0421pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.1892pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.3207pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
