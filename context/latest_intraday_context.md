# Latest Intraday Context

- generated_at: `2026-07-16T01:11:26+08:00`
- stage: `intraday`
- Beijing time: `2026-07-16T01:11:26+08:00`
- US Eastern time: `2026-07-15T13:11:26-04:00`
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

- `QQQ` price=713.97 VWAP=716.3034 open15=724.31/721.08 spread=0.0056% lag=2.29m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SPY` price=752.26 VWAP=753.1783 open15=755.54/754.215 spread=0.004% lag=2.29m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SMH` price=582 VWAP=587.3738 open15=606.85/597.81 spread=0.0344% lag=2.29m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high
- `SOXX` price=547.64 VWAP=551.1778 open15=575.7/565.33 spread=0.0876% lag=2.29m
  risk=below_opening_15m_low,below_vwap,not_above_opening_15m_high

## Focus Instruments

- `QQQ` Nasdaq 100 ETF | raw_score=46.3 | price=713.97 | VWAP=716.3034 | open15=724.31/721.08 |
  spread=0.0056% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.5891pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.3161pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MSFT` Microsoft | raw_score=47.8 | price=395.475 | VWAP=395.0232 | open15=391.33/387.05 |
  spread=0.0379% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.4401pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.0293pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.7562pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `AAPL` Apple | raw_score=39.1 | price=327.25 | VWAP=325.2196 | open15=321.14/317.4 |
  spread=0.0183% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.9501pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.5392pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.2662pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `GOOGL` Alphabet | raw_score=43.1 | price=372.18 | VWAP=368.425 | open15=364.41/357.885 |
  spread=0.0672% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=1.345pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.9341pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=1.6611pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `SOXX` iShares Semiconductor ETF | raw_score=54.2 | price=547.64 | VWAP=551.1778 |
  open15=575.7/565.33 | spread=0.0876% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.3161pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.273pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SMH` VanEck Semiconductor ETF | raw_score=47.9 | price=582 | VWAP=587.3738 |
  open15=606.85/597.81 | spread=0.0344% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.5891pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.273pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SPY` S&P 500 ETF | raw_score=50.9 | price=752.26 | VWAP=753.1783 | open15=755.54/754.215 |
  spread=0.004% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=0.2038pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.793pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.5199pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMZN` Amazon | raw_score=41.2 | price=255.03 | VWAP=254.3839 | open15=252.89/249.98 |
  spread=0.3176% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=manual_confirm_only
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `none`
  - buy_precheck_met: `fresh_data, price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `none`
  - relative_vs_QQQ: vwap_delta=0.5798pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=1.1689pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.8959pct; above_vwap=True/False;
    open15=above_opening_15m_high/below_opening_15m_low
- `NVDA` NVIDIA | raw_score=57.2 | price=208.24 | VWAP=209.1891 | open15=213.775/211.225 |
  spread=0.0192% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-0.1279pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.4612pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.1882pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `MU` Micron | raw_score=54.9 | price=894.535 | VWAP=911.1135 | open15=977.7/953.67 |
  spread=0.0492% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable,
    execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low`
  - relative_vs_QQQ: vwap_delta=-1.4938pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.9047pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.1777pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `CIEN` Ciena | raw_score=54.8 | price=416.805 | VWAP=419.0623 | open15=438.14/427.54 |
  spread=% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "UNAVAILABLE", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_unavailable`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.2129pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.3762pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.1032pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AVGO` Broadcom | raw_score=53.7 | price=390.33 | VWAP=391.6774 | open15=397.94/392.62 |
  spread=2.8181% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-0.0182pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.5709pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.2979pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `ASML` ASML Holding | raw_score=52.5 | price=1768.63 | VWAP=1770.0386 | open15=1829.9/1759.045
  | spread=2.0926% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_vwap, not_above_opening_15m_high, spread_too_wide`
  - buy_precheck_met: `fresh_data, not_below_opening_15m_low, execution_level_is_manual_confirm,
    no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=0.2462pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.8353pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=0.5623pct; above_vwap=False/False;
    open15=inside_opening_15m_range/below_opening_15m_low
- `ANET` Arista Networks | raw_score=51.3 | price=169.39 | VWAP=172.2446 |
  open15=186.095/178.355 | spread=0.9032% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 3.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.3315pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.7424pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.0154pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `STX` Seagate | raw_score=51.3 | price=800.84 | VWAP=818.5961 | open15=889.1/850.01 |
  spread=4.2468% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.8433pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-1.2542pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-1.5272pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `AMAT` Applied Materials | raw_score=51 | price=569.115 | VWAP=578.0716 | open15=610.62/586.86
  | spread=2.4178% | level=L3_MANUAL_CONFIRM_REQUIRED | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high,
    spread_too_wide`
  - buy_precheck_met: `fresh_data, execution_level_is_manual_confirm, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, spread_available_and_acceptable`
  - relative_vs_QQQ: vwap_delta=-1.2236pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=-0.6345pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.9075pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
- `SKHY` SK hynix ADR | raw_score=39.1 | price=174.22 | VWAP=175.6929 | open15=183.63/176.08 |
  spread=0.0402% | level=L1_WATCH | allowed=no
  - data_quality: `{"price_status": "ALPACA_IEX_ONLY", "vwap_status": "ALPACA_IEX_ONLY",
    "opening_15m_high_status": "ALPACA_IEX_ONLY", "opening_15m_low_status": "ALPACA_IEX_ONLY",
    "bid_ask_spread_status": "ALPACA_IEX_ONLY", "lag_minutes": 2.29, "fresh_within_lag": true,
    "live_fresh_within_lag": true}`
  - risk_reasons: `below_opening_15m_low, below_vwap, not_above_opening_15m_high`
  - buy_precheck_met: `fresh_data, spread_available_and_acceptable, no_auto_trade`
  - buy_precheck_unmet: `price_above_vwap, price_above_opening_15m_high,
    not_below_opening_15m_low, execution_level_is_manual_confirm`
  - relative_vs_QQQ: vwap_delta=-0.5126pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SMH: vwap_delta=0.0765pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
  - relative_vs_SOXX: vwap_delta=-0.1965pct; above_vwap=False/False;
    open15=below_opening_15m_low/below_opening_15m_low
