# Latest Intraday Context

- generated_at: `2026-07-15T21:45:05+08:00`
- stage: `intraday`
- Beijing time: `2026-07-15T21:45:05+08:00`
- US Eastern time: `2026-07-15T09:45:05-04:00`
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

- `QQQ` price=722.06 VWAP=722.2881 open15=724.31/721.08 spread=0.0831% lag=2.08m
  risk=below_vwap,not_above_opening_15m_high
- `SPY` price=754.76 VWAP=754.7858 open15=755.54/754.215 spread=0.0676% lag=2.08m
  risk=below_vwap,not_above_opening_15m_high
- `SMH` price=600.07 VWAP=600.4231 open15=606.85/597.81 spread=0.0483% lag=2.08m
  risk=below_vwap,not_above_opening_15m_high
- `SOXX` price=568.51 VWAP=569.3262 open15=575.7/565.33 spread=0.153% lag=2.08m
  risk=below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=46.3 | price=722.06 | VWAP=722.2881 | open15=724.31/721.08 |
  spread=0.0831% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.0272pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.1118pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=568.51 | VWAP=569.3262 |
  open15=575.7/565.33 | spread=0.153% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.1118pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.0846pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=600.07 | VWAP=600.4231 |
  open15=606.85/597.81 | spread=0.0483% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.0272pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.0846pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SPY` S&P 500 ETF | raw_score=50.9 | price=754.76 | VWAP=754.7858 | open15=755.54/754.215 |
  spread=0.0676% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.0282pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.0554pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.1399pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `NVDA` NVIDIA | raw_score=57.2 | price=212.265 | VWAP=212.3331 | open15=213.775/211.225 |
  spread=0.0236% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=-0.0005pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.0268pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.1113pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `MU` Micron | raw_score=54.9 | price=959.22 | VWAP=962.0571 | open15=977.7/953.67 |
  spread=0.1522% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=-0.2633pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.2361pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.1515pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `CIEN` Ciena | raw_score=54.8 | price=437.62 | VWAP=434.8382 | open15=437.62/432.14 |
  spread=0.633% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 3.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.6713pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.6986pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.7831pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
- `AVGO` Broadcom | raw_score=53.7 | price=397.1 | VWAP=395.0901 | open15=397.635/392.62 |
  spread=0.1536% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, price_above_vwap, not_below_opening_15m_low,
    spread_available_and_acceptable, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_opening_15m_high`
  - relative_vs_QQQ: vwap_delta=0.5403pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=0.5675pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=0.6521pct; above_vwap=True/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `ASML` ASML Holding | raw_score=52.5 | price=1774.38 | VWAP=1791.1593 | open15=1829.9/1766.9 |
  spread=0.6678% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.9052pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.878pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.7934pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `ANET` Arista Networks | raw_score=51.3 | price=179.42 | VWAP=181.991 | open15=186.095/178.5 |
  spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_unavailable`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.3811pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-1.3539pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-1.2694pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `STX` Seagate | raw_score=51.3 | price=855.05 | VWAP=860.3161 | open15=889.1/851.88 | spread=%
  | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 3.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_unavailable`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.5805pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.5533pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.4687pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `AMAT` Applied Materials | raw_score=51 | price=589.485 | VWAP=595.2544 | open15=610.62/588.71
  | spread=3.9289% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.9377pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=-0.9104pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=-0.8259pct; above_vwap=False/False;
    open15=inside_opening_15m_range/inside_opening_15m_range
- `SKHY` SK hynix ADR | raw_score=39.1 | price=183.39 | VWAP=178.5908 | open15=183.39/176.08 |
  spread=1.5759% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.08, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `spread_too_wide, spread_too_wide_or_missing`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, no_auto_trade`
  - buy_precheck_unmet: `spread_available_and_acceptable, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=2.7188pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SMH: vwap_delta=2.7461pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
  - relative_vs_SOXX: vwap_delta=2.8306pct; above_vwap=True/False;
    open15=above_opening_15m_high/inside_opening_15m_range
