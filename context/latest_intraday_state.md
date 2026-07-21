# Intraday State

- Generated at: `2026-07-22T01:00:55+08:00`
- Market time ET: `2026-07-21T13:00:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 19, 'below_opening_15m_low': 3, 'below_vwap': 4, 'watch_only': 5, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.31 |  | 706.4582 | 0.4037 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 553.48 |  | 548.3414 | 0.9371 | 550.77 | 545.11 | 0.0596 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.86 |  | 580.0862 | 0.6506 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.71 |  | 746.6308 | 0.2785 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.42 |  | 418.8787 | 0.8454 | 418.76 | 415.025 | 0.1089 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.86 |  | 580.0862 | 0.6506 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 553.48 |  | 548.3414 | 0.9371 | 550.77 | 545.11 | 0.0596 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.31 |  | 706.4582 | 0.4037 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.71 |  | 746.6308 | 0.2785 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 977.125 |  | 946.4246 | 3.2438 | 944.99 | 923 | 0.1218 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1816.11 |  | 1808.4248 | 0.425 | 1804.54 | 1786.51 | 0.0644 | buy_precheck_manual_confirm | none |
| 8 | LITE | ai_networking_optical | 832.69 |  | 822.4285 | 1.2477 | 823.31 | 800.37 | 0.2822 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 296.13 |  | 294.3855 | 0.5926 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.73 |  | 46.4857 | 0.5256 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1574.375 |  | 1536.9074 | 2.4379 | 1540.85 | 1490.29 | 0.0565 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.36 |  | 23.8604 | 2.0939 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.46 |  | 41.76 | 1.6763 | 41.65 | 40.435 | 0.0236 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 328.44 |  | 325.8993 | 0.7796 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 15 | AMKR | semiconductor_test_packaging | 66.805 |  | 65.8627 | 1.4307 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.28 |  | 24.8331 | 1.7998 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 79.66 |  | 77.9147 | 2.24 | 76.615 | 74.55 | 0.3138 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.42 |  | 30.1705 | 0.827 | 29.735 | 28.785 | 0.0986 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.5 |  | 70.7085 | 1.1193 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.71 |  | 746.6308 | 0.2785 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.86 |  | 580.0862 | 0.6506 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.31 |  | 706.4582 | 0.4037 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 4 | HPE | ai_server_oem | 46.73 |  | 46.4857 | 0.5256 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1816.11 |  | 1808.4248 | 0.425 | 1804.54 | 1786.51 | 0.0644 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 296.13 |  | 294.3855 | 0.5926 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 248.125 |  | 247.7309 | 0.1591 | 248.915 | 247.32 | 0.0161 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 349.43 |  | 349.1765 | 0.0726 | 350.985 | 347.69 | 0.0401 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 328.44 |  | 325.8993 | 0.7796 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 125.82 |  | 125.2448 | 0.4592 | 126.01 | 122.48 | 0.0795 | watch_only | none |
| 11 | SOXX | semiconductor_index | 553.48 |  | 548.3414 | 0.9371 | 550.77 | 545.11 | 0.0596 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 217.525 |  | 216.4973 | 0.4747 | 220.76 | 214.41 | 0.1839 | watch_only | none |
| 13 | TSM | foundry | 422.42 |  | 418.8787 | 0.8454 | 418.76 | 415.025 | 0.1089 | buy_precheck_manual_confirm | none |
| 14 | AMKR | semiconductor_test_packaging | 66.805 |  | 65.8627 | 1.4307 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 15 | LITE | ai_networking_optical | 832.69 |  | 822.4285 | 1.2477 | 823.31 | 800.37 | 0.2822 | buy_precheck_manual_confirm | none |
| 16 | APD | industrial_gases | 299.17 |  | 298.8654 | 0.1019 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 142.61 |  | 141.7897 | 0.5785 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | APLD | high_beta_ai_infrastructure | 30.42 |  | 30.1705 | 0.827 | 29.735 | 28.785 | 0.0986 | buy_precheck_manual_confirm | none |
| 19 | VRT | data_center_power_cooling | 305.08 |  | 301.0373 | 1.3429 | 305.09 | 299.13 | 0.177 | watch_only | none |
| 20 | TT | data_center_power_cooling | 471.77 |  | 469.6542 | 0.4505 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.42 |  | 418.8787 | 0.8454 | 418.76 | 415.025 | 0.1089 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.86 |  | 580.0862 | 0.6506 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 553.48 |  | 548.3414 | 0.9371 | 550.77 | 545.11 | 0.0596 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.31 |  | 706.4582 | 0.4037 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.71 |  | 746.6308 | 0.2785 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 977.125 |  | 946.4246 | 3.2438 | 944.99 | 923 | 0.1218 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1816.11 |  | 1808.4248 | 0.425 | 1804.54 | 1786.51 | 0.0644 | buy_precheck_manual_confirm | none |
| 8 | LITE | ai_networking_optical | 832.69 |  | 822.4285 | 1.2477 | 823.31 | 800.37 | 0.2822 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 296.13 |  | 294.3855 | 0.5926 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.73 |  | 46.4857 | 0.5256 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1574.375 |  | 1536.9074 | 2.4379 | 1540.85 | 1490.29 | 0.0565 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.36 |  | 23.8604 | 2.0939 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.46 |  | 41.76 | 1.6763 | 41.65 | 40.435 | 0.0236 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 328.44 |  | 325.8993 | 0.7796 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 15 | AMKR | semiconductor_test_packaging | 66.805 |  | 65.8627 | 1.4307 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.28 |  | 24.8331 | 1.7998 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 79.66 |  | 77.9147 | 2.24 | 76.615 | 74.55 | 0.3138 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.42 |  | 30.1705 | 0.827 | 29.735 | 28.785 | 0.0986 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.5 |  | 70.7085 | 1.1193 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 20 | AMD | ai_accelerator | 541.4 |  | 532.283 | 1.7128 | 532.365 | 524.72 | 1.0122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.31 |  | 706.4582 | 0.4037 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.5 |  | 70.7085 | 1.1193 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.46 |  | 205.9911 | -0.2578 | 208.61 | 206.275 | 0.0195 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.6 |  | 399.1993 | -0.1501 | 401.45 | 396.36 | 0.0301 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.44 |  | 325.8993 | 0.7796 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.43 |  | 349.1765 | 0.0726 | 350.985 | 347.69 | 0.0401 | watch_only | none |
| AMD | ai_accelerator | 541.4 |  | 532.283 | 1.7128 | 532.365 | 524.72 | 1.0122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.42 |  | 418.8787 | 0.8454 | 418.76 | 415.025 | 0.1089 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.48 |  | 548.3414 | 0.9371 | 550.77 | 545.11 | 0.0596 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.86 |  | 580.0862 | 0.6506 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.485 |  | 384.6091 | 0.4877 | 390.11 | 382.13 | 0.3545 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 977.125 |  | 946.4246 | 3.2438 | 944.99 | 923 | 0.1218 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 209.31 |  | 207.4881 | 0.8781 | 208.61 | 205.31 | 1.2661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 405.24 |  | 403.4678 | 0.4392 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.73 |  | 46.4857 | 0.5256 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.28 |  | 24.8331 | 1.7998 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.71 |  | 746.6308 | 0.2785 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.13 |  | 294.3855 | 0.5926 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.82 |  | 125.2448 | 0.4592 | 126.01 | 122.48 | 0.0795 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 79.66 |  | 77.9147 | 2.24 | 76.615 | 74.55 | 0.3138 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 305.08 |  | 301.0373 | 1.3429 | 305.09 | 299.13 | 0.177 | watch_only | none |
| ETN | data_center_power_cooling | 406.65 |  | 406.0803 | 0.1403 | 411.01 | 404.21 | 2.1665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 641.69 |  | 637.4455 | 0.6659 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1092.87 |  | 1097.5788 | -0.429 | 1140.63 | 1103.815 | 0.2123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 471.77 |  | 469.6542 | 0.4505 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.61 |  | 141.7897 | 0.5785 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175 |  | 175.2365 | -0.135 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 318.27 |  | 310.8995 | 2.3707 | 309.72 | 302.3 | 3.5065 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 832.69 |  | 822.4285 | 1.2477 | 823.31 | 800.37 | 0.2822 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 410.41 |  | 405.3212 | 1.2555 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 118.81 |  | 115.371 | 2.9808 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 325.67 |  | 325.9728 | -0.0929 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1816.11 |  | 1808.4248 | 0.425 | 1804.54 | 1786.51 | 0.0644 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 570.04 |  | 563.6524 | 1.1333 | 564.91 | 552.71 | 3.4419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 322.84 |  | 320.1741 | 0.8326 | 328.135 | 317.17 | 4.671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 217.525 |  | 216.4973 | 0.4747 | 220.76 | 214.41 | 0.1839 | watch_only | none |
| TER | semiconductor_test_packaging | 375.9 |  | 369.2054 | 1.8133 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.36 |  | 296.0315 | 1.8 | 296.68 | 291.36 | 3.7895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.805 |  | 65.8627 | 1.4307 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 56.2 |  | 54.9647 | 2.2475 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 142.52 |  | 141.0921 | 1.012 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346 |  | 339.5223 | 1.9079 | 340.205 | 336.3 | 0.4884 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.885 |  | 506.2925 | 0.117 | 512.83 | 507.675 | 4.2396 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 299.17 |  | 298.8654 | 0.1019 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.42 |  | 30.1705 | 0.827 | 29.735 | 28.785 | 0.0986 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.46 |  | 41.76 | 1.6763 | 41.65 | 40.435 | 0.0236 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.36 |  | 23.8604 | 2.0939 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1574.375 |  | 1536.9074 | 2.4379 | 1540.85 | 1490.29 | 0.0565 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 549.39 |  | 538.803 | 1.9649 | 533.56 | 517.335 | 0.759 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 894.78 |  | 875.2627 | 2.2299 | 866.73 | 845.78 | 0.456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.125 |  | 247.7309 | 0.1591 | 248.915 | 247.32 | 0.0161 | watch_only | none |
| META | cloud_ai_capex | 648.03 |  | 647.592 | 0.0676 | 655.425 | 643.54 | 1.0277 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 290.93 |  | 285.6613 | 1.8444 | 286.39 | 275.86 | 3.176 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 167.96 |  | 165.3764 | 1.5623 | 165.88 | 160.77 | 0.8573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
