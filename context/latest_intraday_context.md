# Latest Intraday Context

- generated_at: `2026-07-16T00:31:41+08:00`
- stage: `intraday`
- Beijing time: `2026-07-16T00:31:41+08:00`
- US Eastern time: `2026-07-15T12:31:41-04:00`
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

- `QQQ` price=712.13 VWAP=716.947 open15=724.31/721.08 spread=0.0491% lag=1.66m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SPY` price=751.065 VWAP=753.4676 open15=755.54/754.215 spread=0.004% lag=1.66m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SMH` price=576.61 VWAP=588.8697 open15=606.85/597.81 spread=0.085% lag=1.66m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SOXX` price=541.6 VWAP=553.3212 open15=575.7/565.33 spread=0.072% lag=1.66m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=46.3 | price=712.13 | VWAP=716.947 | open15=724.31/721.08 |
  spread=0.0491% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.41pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.4465pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MSFT` Microsoft | raw_score=47.8 | price=397.565 | VWAP=394.8376 | open15=391.33/387.05 |
  spread=0.0327% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.3627pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=2.7727pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=2.8091pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `AAPL` Apple | raw_score=39.1 | price=328.275 | VWAP=324.5143 | open15=321.14/317.4 |
  spread=0.0244% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.8308pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=3.2408pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=3.2772pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `GOOGL` Alphabet | raw_score=43.1 | price=372.71 | VWAP=368.0166 | open15=364.41/357.885 |
  spread=0.0215% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.9472pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=3.3572pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=3.3937pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=541.6 | VWAP=553.3212 |
  open15=575.7/565.33 | spread=0.072% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-1.4465pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.0364pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=576.61 | VWAP=588.8697 |
  open15=606.85/597.81 | spread=0.085% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-1.41pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.0364pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SPY` S&P 500 ETF | raw_score=50.9 | price=751.065 | VWAP=753.4676 | open15=755.54/754.215 |
  spread=0.004% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.353pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.763pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.7995pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMZN` Amazon | raw_score=41.2 | price=255.69 | VWAP=254.2205 | open15=252.89/249.98 |
  spread=0.0274% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.2499pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=2.6599pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=2.6964pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `META` Meta Platforms | raw_score=39.5 | price=683.35 | VWAP=675.1856 | open15=664.875/657.17
  | spread=0.1127% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.8811pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=3.2911pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=3.3275pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `NVDA` NVIDIA | raw_score=57.2 | price=206.895 | VWAP=209.633 | open15=213.775/211.225 |
  spread=0.0483% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-0.6342pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.7758pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.8122pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MU` Micron | raw_score=54.9 | price=883.605 | VWAP=915.3729 | open15=977.7/953.67 |
  spread=0.069% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-2.7986pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.3886pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.3522pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `CIEN` Ciena | raw_score=54.8 | price=406.89 | VWAP=421.0084 | open15=438.14/427.54 | spread=%
  | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_unavailable`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-2.6816pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.2716pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.2351pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AVGO` Broadcom | raw_score=53.7 | price=388.81 | VWAP=392.1743 | open15=397.94/392.62 |
  spread=2.5617% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.186pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.224pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.2605pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `ASML` ASML Holding | raw_score=52.5 | price=1749.57 | VWAP=1773.719 | open15=1829.9/1759.045
  | spread=0.0754% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-0.6896pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.7204pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.7568pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `ANET` Arista Networks | raw_score=51.3 | price=167.72 | VWAP=172.9602 |
  open15=186.095/178.355 | spread=2.3074% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-2.3579pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.9478pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.9114pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `STX` Seagate | raw_score=51.3 | price=794.38 | VWAP=820.7052 | open15=889.1/850.01 | spread=%
  | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_unavailable`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-2.5358pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.1257pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.0893pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMAT` Applied Materials | raw_score=51 | price=560.48 | VWAP=579.7474 | open15=610.62/586.86
  | spread=3.8324% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-2.6515pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.2415pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.2051pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SKHY` SK hynix ADR | raw_score=39.1 | price=169.135 | VWAP=176.1466 | open15=183.63/176.08 |
  spread=4.5053% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 1.66, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-3.3087pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.8986pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.8622pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
