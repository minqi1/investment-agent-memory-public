# Intraday State

- Generated at: `2026-07-17T03:11:26+08:00`
- Market time ET: `2026-07-16T15:11:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 3, 'below_vwap': 5, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.23 |  | 709.1636 | -0.5547 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.17 |  | 533.649 | -1.0267 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.26 |  | 571.5733 | -0.7546 | 580.31 | 572.21 | 0.0388 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.73 |  | 752.1852 | -0.3264 | 753.51 | 751.13 | 0.0013 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.32 |  | 295.005 | 0.4458 | 293.89 | 291.35 | 0.135 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.72 |  | 399.9017 | 0.7047 | 398.69 | 392.2 | 0.1018 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 334.05 |  | 331.0269 | 0.9132 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.32 |  | 295.005 | 0.4458 | 293.89 | 291.35 | 0.135 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.72 |  | 399.9017 | 0.7047 | 398.69 | 392.2 | 0.1018 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.86 |  | 140.5231 | 0.2398 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | TT | data_center_power_cooling | 475.1 |  | 474.1274 | 0.2051 | 474.085 | 467.64 | 4.7969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AAPL | mega_cap_platform | 334.05 |  | 331.0269 | 0.9132 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 166.83 |  | 166.5885 | 0.145 | 169.91 | 165.6 | 4.6754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | GEV | data_center_power_cooling | 1028.95 |  | 1027.0818 | 0.1819 | 1035.07 | 1021.09 | 3.7718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | LIN | industrial_gases | 518.94 |  | 515.2931 | 0.7077 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 219.3 |  | 220.9117 | -0.7296 | 222.19 | 218.09 | 0.1322 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 294.875 |  | 296.0643 | -0.4017 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | CRWV | gpu_cloud_ai_factory | 73.32 |  | 73.2953 | 0.0338 | 75.54 | 73.985 | 4.2144 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 13 | ENTG | semiconductor_materials | 134.1 |  | 134.7818 | -0.5058 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | TSM | foundry | 407.22 |  | 408.7021 | -0.3626 | 414.385 | 406.61 | 0.6532 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 528.17 |  | 533.649 | -1.0267 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 705.23 |  | 709.1636 | -0.5547 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 375.79 |  | 379.6902 | -1.0272 | 386.58 | 378.53 | 0.0266 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 207.025 |  | 207.347 | -0.1553 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1793.13 |  | 1817.1333 | -1.3209 | 1823.13 | 1796.26 | 0.1071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 567.26 |  | 571.5733 | -0.7546 | 580.31 | 572.21 | 0.0388 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.32 |  | 295.005 | 0.4458 | 293.89 | 291.35 | 0.135 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.72 |  | 399.9017 | 0.7047 | 398.69 | 392.2 | 0.1018 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 334.05 |  | 331.0269 | 0.9132 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.1 |  | 474.1274 | 0.2051 | 474.085 | 467.64 | 4.7969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | JCI | data_center_power_cooling | 140.86 |  | 140.5231 | 0.2398 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | LIN | industrial_gases | 518.94 |  | 515.2931 | 0.7077 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TSM | foundry | 407.22 |  | 408.7021 | -0.3626 | 414.385 | 406.61 | 0.6532 | below_vwap | below_vwap,spread_too_wide |
| 8 | KLAC | semiconductor_equipment | 219.3 |  | 220.9117 | -0.7296 | 222.19 | 218.09 | 0.1322 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 294.875 |  | 296.0643 | -0.4017 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 134.1 |  | 134.7818 | -0.5058 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ANET | ai_networking_optical | 166.83 |  | 166.5885 | 0.145 | 169.91 | 165.6 | 4.6754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | GEV | data_center_power_cooling | 1028.95 |  | 1027.0818 | 0.1819 | 1035.07 | 1021.09 | 3.7718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | CRWV | gpu_cloud_ai_factory | 73.32 |  | 73.2953 | 0.0338 | 75.54 | 73.985 | 4.2144 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | SOXX | semiconductor_index | 528.17 |  | 533.649 | -1.0267 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | CIEN | ai_networking_optical | 388.22 |  | 394.0428 | -1.4777 | 410 | 397.68 | 1.2261 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | QQQ | market_regime | 705.23 |  | 709.1636 | -0.5547 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AVGO | custom_silicon_networking | 375.79 |  | 379.6902 | -1.0272 | 386.58 | 378.53 | 0.0266 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | MU | memory_hbm_storage | 846.72 |  | 856.4571 | -1.1369 | 887.1 | 866.765 | 1.181 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | VRT | data_center_power_cooling | 290.245 |  | 293.2153 | -1.013 | 300.385 | 293.64 | 1.9053 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.23 |  | 709.1636 | -0.5547 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.55 |  | 71.7598 | -1.686 | 73.09 | 71.45 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.025 |  | 207.347 | -0.1553 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.72 |  | 399.9017 | 0.7047 | 398.69 | 392.2 | 0.1018 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 334.05 |  | 331.0269 | 0.9132 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 354.34 |  | 367.3106 | -3.5312 | 375.18 | 369.2 | 0.1834 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 496.165 |  | 503.4771 | -1.4523 | 518.33 | 507.62 | 1.048 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 407.22 |  | 408.7021 | -0.3626 | 414.385 | 406.61 | 0.6532 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.17 |  | 533.649 | -1.0267 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.26 |  | 571.5733 | -0.7546 | 580.31 | 572.21 | 0.0388 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.79 |  | 379.6902 | -1.0272 | 386.58 | 378.53 | 0.0266 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 846.72 |  | 856.4571 | -1.1369 | 887.1 | 866.765 | 1.181 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.575 |  | 190.8004 | -1.6904 | 201.61 | 194.19 | 1.1355 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 394.65 |  | 401.8921 | -1.802 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.31 |  | 45.7546 | -0.9717 | 47.65 | 46.165 | 0.0441 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.005 |  | 25.3043 | -1.1828 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.73 |  | 752.1852 | -0.3264 | 753.51 | 751.13 | 0.0013 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.875 |  | 296.0643 | -0.4017 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.01 |  | 126.5615 | -1.2259 | 131.36 | 126.665 | 3.8877 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.32 |  | 73.2953 | 0.0338 | 75.54 | 73.985 | 4.2144 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 290.245 |  | 293.2153 | -1.013 | 300.385 | 293.64 | 1.9053 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.41 |  | 399.2097 | -0.7013 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.14 |  | 631.1702 | -0.3217 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.95 |  | 1027.0818 | 0.1819 | 1035.07 | 1021.09 | 3.7718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.1 |  | 474.1274 | 0.2051 | 474.085 | 467.64 | 4.7969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.86 |  | 140.5231 | 0.2398 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.83 |  | 166.5885 | 0.145 | 169.91 | 165.6 | 4.6754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.91 |  | 280.5797 | -1.6643 | 288.48 | 280.67 | 1.2142 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.5 |  | 707.6294 | -1.2901 | 737.175 | 720.21 | 0.199 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 388.22 |  | 394.0428 | -1.4777 | 410 | 397.68 | 1.2261 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 98.96 |  | 101.2063 | -2.2195 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.99 |  | 323.2421 | -1.9342 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.13 |  | 1817.1333 | -1.3209 | 1823.13 | 1796.26 | 0.1071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.57 |  | 569.5928 | -1.4085 | 572.69 | 562.32 | 0.7871 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.52 |  | 322.7685 | -1.6261 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.3 |  | 220.9117 | -0.7296 | 222.19 | 218.09 | 0.1322 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.11 |  | 326.5299 | -1.3536 | 332.49 | 326.685 | 4.5419 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.7 |  | 286.2356 | -1.9339 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.955 |  | 63.8578 | -1.4137 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.05 |  | 51.7568 | -1.3656 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.1 |  | 134.7818 | -0.5058 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.55 |  | 334.044 | -1.6447 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.94 |  | 515.2931 | 0.7077 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.32 |  | 295.005 | 0.4458 | 293.89 | 291.35 | 0.135 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.5 |  | 26.7716 | -1.0145 | 28.05 | 27.6 | 0.0377 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.485 |  | 35.5021 | -0.0482 | 37.365 | 36.4 | 0.0564 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.165 |  | 21.2013 | -0.1713 | 22.18 | 21.78 | 0.0472 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1402.63 |  | 1458.1009 | -3.8043 | 1549.47 | 1482.06 | 4.6342 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 460.71 |  | 472.8975 | -2.5772 | 498.04 | 480.14 | 0.5361 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 745.18 |  | 763.2901 | -2.3726 | 797.155 | 768.7 | 0.1919 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 252.28 |  | 254.994 | -1.0644 | 258.07 | 252.62 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 665.68 |  | 671.1306 | -0.8122 | 680.09 | 667.1 | 0.8127 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 256.75 |  | 257.2736 | -0.2035 | 265.96 | 258.1 | 0.0896 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SKHY | memory_hbm_storage | 155.63 |  | 161.4729 | -3.6185 | 168.11 | 162.41 | 1.0795 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
