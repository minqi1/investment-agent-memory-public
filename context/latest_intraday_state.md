# Intraday State

- Generated at: `2026-07-16T23:09:31+08:00`
- Market time ET: `2026-07-16T11:09:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'below_opening_15m_low': 22, 'watch_only': 3, 'manual_confirm_candidate': 1, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.77 |  | 710.591 | -0.1155 | 713.55 | 708.25 | 0.0423 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 534.99 |  | 538.1061 | -0.5791 | 543.4 | 535.47 | 0.0897 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.34 |  | 576.0183 | -0.6386 | 580.31 | 572.21 | 0.0384 | below_vwap | below_vwap |
| SPY | market_regime | 753.18 |  | 752.6906 | 0.065 | 753.51 | 751.13 | 0.0279 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 329.8 |  | 329.2622 | 0.1633 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 329.8 |  | 329.2622 | 0.1633 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.18 |  | 752.6906 | 0.065 | 753.51 | 751.13 | 0.0279 | watch_only | none |
| 3 | META | cloud_ai_capex | 678.355 |  | 674.6654 | 0.5469 | 680.09 | 667.1 | 0.1032 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 397.17 |  | 395.5051 | 0.421 | 398.69 | 392.2 | 0.2417 | watch_only | none |
| 5 | MKSI | semiconductor_materials | 341.42 |  | 341.3627 | 0.0168 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 141.32 |  | 140.6855 | 0.451 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | LIN | industrial_gases | 516.485 |  | 513.539 | 0.5737 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | TT | data_center_power_cooling | 476.09 |  | 474.1212 | 0.4153 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ONTO | semiconductor_test_packaging | 291.68 |  | 290.6392 | 0.3581 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | COHU | semiconductor_test_packaging | 52.95 |  | 52.6766 | 0.5191 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | AMZN | cloud_ai_capex | 255.195 |  | 255.1783 | 0.0065 | 258.07 | 252.62 | 0.4467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | GEV | data_center_power_cooling | 1039.24 |  | 1031.8808 | 0.7132 | 1035.07 | 1021.09 | 0.714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TER | semiconductor_test_packaging | 330.45 |  | 328.9122 | 0.4675 | 332.49 | 326.685 | 0.4721 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | IWM | market_regime | 296.57 |  | 296.5856 | -0.0053 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 15 | TSM | foundry | 409.95 |  | 411.4922 | -0.3748 | 414.385 | 406.61 | 0.0415 | below_vwap | below_vwap |
| 16 | QQQ | market_regime | 709.77 |  | 710.591 | -0.1155 | 713.55 | 708.25 | 0.0423 | below_vwap | below_vwap |
| 17 | AVGO | custom_silicon_networking | 380.34 |  | 382.0632 | -0.451 | 386.58 | 378.53 | 0.0552 | below_vwap | below_vwap |
| 18 | SMH | semiconductor_index | 572.34 |  | 576.0183 | -0.6386 | 580.31 | 572.21 | 0.0384 | below_vwap | below_vwap |
| 19 | AMAT | semiconductor_equipment | 573.29 |  | 575.6702 | -0.4135 | 572.69 | 562.32 | 0.239 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 329.8 |  | 329.2622 | 0.1633 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 573.29 |  | 575.6702 | -0.4135 | 572.69 | 562.32 | 0.239 | below_vwap | below_vwap |
| 3 | IWM | market_regime | 296.57 |  | 296.5856 | -0.0053 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 4 | TT | data_center_power_cooling | 476.09 |  | 474.1212 | 0.4153 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | JCI | data_center_power_cooling | 141.32 |  | 140.6855 | 0.451 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1039.24 |  | 1031.8808 | 0.7132 | 1035.07 | 1021.09 | 0.714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 516.485 |  | 513.539 | 0.5737 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 295.38 |  | 292.518 | 0.9784 | 293.89 | 291.35 | 4.198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | COHU | semiconductor_test_packaging | 52.95 |  | 52.6766 | 0.5191 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SPY | market_regime | 753.18 |  | 752.6906 | 0.065 | 753.51 | 751.13 | 0.0279 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 397.17 |  | 395.5051 | 0.421 | 398.69 | 392.2 | 0.2417 | watch_only | none |
| 12 | META | cloud_ai_capex | 678.355 |  | 674.6654 | 0.5469 | 680.09 | 667.1 | 0.1032 | watch_only | none |
| 13 | TSM | foundry | 409.95 |  | 411.4922 | -0.3748 | 414.385 | 406.61 | 0.0415 | below_vwap | below_vwap |
| 14 | QQQ | market_regime | 709.77 |  | 710.591 | -0.1155 | 713.55 | 708.25 | 0.0423 | below_vwap | below_vwap |
| 15 | AVGO | custom_silicon_networking | 380.34 |  | 382.0632 | -0.451 | 386.58 | 378.53 | 0.0552 | below_vwap | below_vwap |
| 16 | VRT | data_center_power_cooling | 295.975 |  | 296.7161 | -0.2498 | 300.385 | 293.64 | 2.1792 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMD | ai_accelerator | 507.95 |  | 510.7937 | -0.5567 | 518.33 | 507.62 | 1.1832 | below_vwap | below_vwap,spread_too_wide |
| 18 | PWR | data_center_power_cooling | 633.17 |  | 633.628 | -0.0723 | 640.25 | 631.005 | 1.6315 | below_vwap | below_vwap,spread_too_wide |
| 19 | ASML | semiconductor_equipment | 1818.9 |  | 1826.8401 | -0.4346 | 1823.13 | 1796.26 | 0.6575 | below_vwap | below_vwap,spread_too_wide |
| 20 | KLAC | semiconductor_equipment | 221.73 |  | 222.9507 | -0.5475 | 222.19 | 218.09 | 0.1804 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.77 |  | 710.591 | -0.1155 | 713.55 | 708.25 | 0.0423 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.93 |  | 72.213 | -0.3919 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 206.14 |  | 207.9107 | -0.8517 | 211.03 | 207.49 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 397.17 |  | 395.5051 | 0.421 | 398.69 | 392.2 | 0.2417 | watch_only | none |
| AAPL | mega_cap_platform | 329.8 |  | 329.2622 | 0.1633 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.35 |  | 372.0529 | -0.1889 | 375.18 | 369.2 | 0.1939 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.95 |  | 510.7937 | -0.5567 | 518.33 | 507.62 | 1.1832 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 409.95 |  | 411.4922 | -0.3748 | 414.385 | 406.61 | 0.0415 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.99 |  | 538.1061 | -0.5791 | 543.4 | 535.47 | 0.0897 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.34 |  | 576.0183 | -0.6386 | 580.31 | 572.21 | 0.0384 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 380.34 |  | 382.0632 | -0.451 | 386.58 | 378.53 | 0.0552 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 862.53 |  | 866.4136 | -0.4482 | 887.1 | 866.765 | 0.3872 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 191.57 |  | 194.6775 | -1.5962 | 201.61 | 194.19 | 0.3758 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 402.19 |  | 405.4025 | -0.7924 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.8 |  | 46.5195 | -1.5466 | 47.65 | 46.165 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.52 |  | 25.8453 | -1.2588 | 26.71 | 25.74 | 0.0392 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.18 |  | 752.6906 | 0.065 | 753.51 | 751.13 | 0.0279 | watch_only | none |
| IWM | market_regime | 296.57 |  | 296.5856 | -0.0053 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.65 |  | 127.1596 | -0.4007 | 131.36 | 126.665 | 0.0947 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.975 |  | 74.0296 | -1.4245 | 75.54 | 73.985 | 1.6444 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 295.975 |  | 296.7161 | -0.2498 | 300.385 | 293.64 | 2.1792 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 397.15 |  | 401.9597 | -1.1966 | 406.24 | 399.495 | 5.0888 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 633.17 |  | 633.628 | -0.0723 | 640.25 | 631.005 | 1.6315 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1039.24 |  | 1031.8808 | 0.7132 | 1035.07 | 1021.09 | 0.714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.09 |  | 474.1212 | 0.4153 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.32 |  | 140.6855 | 0.451 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.915 |  | 166.3123 | -0.8402 | 169.91 | 165.6 | 2.2618 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 278.16 |  | 284.4443 | -2.2093 | 288.48 | 280.67 | 0.7046 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 711.56 |  | 720.9789 | -1.3064 | 737.175 | 720.21 | 0.1939 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 395.47 |  | 399.0457 | -0.8961 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.28 |  | 103.5053 | -2.1499 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 325.38 |  | 329.3127 | -1.1942 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1818.9 |  | 1826.8401 | -0.4346 | 1823.13 | 1796.26 | 0.6575 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 573.29 |  | 575.6702 | -0.4135 | 572.69 | 562.32 | 0.239 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 325.61 |  | 327.6219 | -0.6141 | 328.96 | 324.11 | 4.1829 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 221.73 |  | 222.9507 | -0.5475 | 222.19 | 218.09 | 0.1804 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 330.45 |  | 328.9122 | 0.4675 | 332.49 | 326.685 | 0.4721 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 291.68 |  | 290.6392 | 0.3581 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.29 |  | 64.7101 | -0.6492 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.95 |  | 52.6766 | 0.5191 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.67 |  | 136.0127 | -0.2519 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.42 |  | 341.3627 | 0.0168 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 516.485 |  | 513.539 | 0.5737 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.38 |  | 292.518 | 0.9784 | 293.89 | 291.35 | 4.198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.99 |  | 27.4581 | -1.7049 | 28.05 | 27.6 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.31 |  | 36.1814 | -2.4083 | 37.365 | 36.4 | 0.0566 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.23 |  | 21.5834 | -1.6372 | 22.18 | 21.78 | 0.0471 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1474.49 |  | 1497.9287 | -1.5647 | 1549.47 | 1482.06 | 3.391 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 477.94 |  | 483.9215 | -1.236 | 498.04 | 480.14 | 3.4691 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 778.1 |  | 778.4912 | -0.0502 | 797.155 | 768.7 | 0.2211 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 255.195 |  | 255.1783 | 0.0065 | 258.07 | 252.62 | 0.4467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| META | cloud_ai_capex | 678.355 |  | 674.6654 | 0.5469 | 680.09 | 667.1 | 0.1032 | watch_only | none |
| ARM | ai_accelerator | 255.985 |  | 259.1481 | -1.2206 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.36 |  | 164.3486 | -1.8185 | 168.11 | 162.41 | 0.9048 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
