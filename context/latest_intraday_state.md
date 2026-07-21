# Intraday State

- Generated at: `2026-07-21T22:35:16+08:00`
- Market time ET: `2026-07-21T10:35:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 13, 'below_opening_15m_low': 2, 'spread_too_wide_or_missing': 23, 'below_vwap': 9, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.53 |  | 704.7871 | 0.2473 | 707.09 | 704.52 | 0.0283 | watch_only | none |
| SOXX | semiconductor_index | 547.22 |  | 546.0543 | 0.2135 | 550.77 | 545.11 | 0.0969 | watch_only | none |
| SMH | semiconductor_index | 578.11 |  | 576.9832 | 0.1953 | 582.03 | 576.57 | 0.0709 | watch_only | none |
| SPY | market_regime | 746.85 |  | 745.447 | 0.1882 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.85 |  | 745.447 | 0.1882 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 565.3 |  | 560.76 | 0.8096 | 564.91 | 552.71 | 0.1574 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 295 |  | 293.9424 | 0.3598 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 4 | STX | memory_hbm_storage | 867.86 |  | 864.0274 | 0.4436 | 866.73 | 845.78 | 0.3053 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 23.69 |  | 23.3453 | 1.4767 | 23.32 | 22.79 | 0.1266 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 42.06 |  | 41.4914 | 1.3705 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.825 |  | 24.5893 | 0.9584 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 30.13 |  | 29.7623 | 1.2356 | 29.735 | 28.785 | 0.0996 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.85 |  | 745.447 | 0.1882 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 295 |  | 293.9424 | 0.3598 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 578.11 |  | 576.9832 | 0.1953 | 582.03 | 576.57 | 0.0709 | watch_only | none |
| 4 | SOXX | semiconductor_index | 547.22 |  | 546.0543 | 0.2135 | 550.77 | 545.11 | 0.0969 | watch_only | none |
| 5 | QQQ | market_regime | 706.53 |  | 704.7871 | 0.2473 | 707.09 | 704.52 | 0.0283 | watch_only | none |
| 6 | MU | memory_hbm_storage | 933.96 |  | 930.8708 | 0.3319 | 944.99 | 923 | 0.0407 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 248.17 |  | 247.6552 | 0.2079 | 248.915 | 247.32 | 0.0645 | watch_only | none |
| 8 | STX | memory_hbm_storage | 867.86 |  | 864.0274 | 0.4436 | 866.73 | 845.78 | 0.3053 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 206.725 |  | 206.0994 | 0.3035 | 208.61 | 205.31 | 0.179 | watch_only | none |
| 10 | PWR | data_center_power_cooling | 638.66 |  | 636.8237 | 0.2884 | 645.815 | 635.91 | 0.191 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 400.43 |  | 399.6066 | 0.2061 | 401.45 | 396.36 | 0.2822 | watch_only | none |
| 12 | HPE | ai_server_oem | 46.48 |  | 46.2381 | 0.5231 | 46.685 | 45.835 | 0.1076 | watch_only | none |
| 13 | SNDK | memory_hbm_storage | 1523.91 |  | 1517.2709 | 0.4376 | 1540.85 | 1490.29 | 0.1207 | watch_only | none |
| 14 | SMCI | ai_server_oem | 24.825 |  | 24.5893 | 0.9584 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 15 | AMAT | semiconductor_equipment | 565.3 |  | 560.76 | 0.8096 | 564.91 | 552.71 | 0.1574 | buy_precheck_manual_confirm | none |
| 16 | APD | industrial_gases | 300.61 |  | 299.283 | 0.4434 | 301.84 | 296.5 | 0.1697 | watch_only | none |
| 17 | ORCL | cloud_ai_capex | 125.565 |  | 125.0164 | 0.4388 | 126.01 | 122.48 | 0.223 | watch_only | none |
| 18 | LRCX | semiconductor_equipment | 318.57 |  | 318.2108 | 0.1129 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | IREN | high_beta_ai_infrastructure | 42.06 |  | 41.4914 | 1.3705 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| 20 | APLD | high_beta_ai_infrastructure | 30.13 |  | 29.7623 | 1.2356 | 29.735 | 28.785 | 0.0996 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.85 |  | 745.447 | 0.1882 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 565.3 |  | 560.76 | 0.8096 | 564.91 | 552.71 | 0.1574 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 295 |  | 293.9424 | 0.3598 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 4 | STX | memory_hbm_storage | 867.86 |  | 864.0274 | 0.4436 | 866.73 | 845.78 | 0.3053 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 23.69 |  | 23.3453 | 1.4767 | 23.32 | 22.79 | 0.1266 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 42.06 |  | 41.4914 | 1.3705 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.825 |  | 24.5893 | 0.9584 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 30.13 |  | 29.7623 | 1.2356 | 29.735 | 28.785 | 0.0996 | buy_precheck_manual_confirm | none |
| 9 | AMD | ai_accelerator | 532.43 |  | 529.4307 | 0.5665 | 532.365 | 524.72 | 0.7212 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | LITE | ai_networking_optical | 829.165 |  | 813.7362 | 1.896 | 823.31 | 800.37 | 1.4605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | CIEN | ai_networking_optical | 406.59 |  | 401.2286 | 1.3363 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ARM | ai_accelerator | 287.88 |  | 283.3754 | 1.5896 | 286.39 | 275.86 | 0.8997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | WDC | memory_hbm_storage | 538.93 |  | 533.5826 | 1.0022 | 533.56 | 517.335 | 0.4379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TER | semiconductor_test_packaging | 371.24 |  | 364.4243 | 1.8703 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SMH | semiconductor_index | 578.11 |  | 576.9832 | 0.1953 | 582.03 | 576.57 | 0.0709 | watch_only | none |
| 16 | COHR | ai_networking_optical | 309.86 |  | 305.5133 | 1.4228 | 309.72 | 302.3 | 4.5601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | COHU | semiconductor_test_packaging | 54.79 |  | 54.4042 | 0.7092 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SOXX | semiconductor_index | 547.22 |  | 546.0543 | 0.2135 | 550.77 | 545.11 | 0.0969 | watch_only | none |
| 19 | QQQ | market_regime | 706.53 |  | 704.7871 | 0.2473 | 707.09 | 704.52 | 0.0283 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 326.62 |  | 324.323 | 0.7082 | 325.59 | 322.63 | 0.8787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.53 |  | 704.7871 | 0.2473 | 707.09 | 704.52 | 0.0283 | watch_only | none |
| TQQQ | leveraged_tool | 70.68 |  | 70.2669 | 0.588 | 70.84 | 70.09 | 0.0283 | watch_only | none |
| NVDA | ai_accelerator | 205.005 |  | 206.23 | -0.594 | 208.61 | 206.275 | 0.0195 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.43 |  | 399.6066 | 0.2061 | 401.45 | 396.36 | 0.2822 | watch_only | none |
| AAPL | mega_cap_platform | 326.62 |  | 324.323 | 0.7082 | 325.59 | 322.63 | 0.8787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 349.16 |  | 349.4961 | -0.0962 | 350.985 | 347.69 | 0.0831 | below_vwap | below_vwap |
| AMD | ai_accelerator | 532.43 |  | 529.4307 | 0.5665 | 532.365 | 524.72 | 0.7212 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 417.97 |  | 416.5655 | 0.3372 | 418.76 | 415.025 | 0.3589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.22 |  | 546.0543 | 0.2135 | 550.77 | 545.11 | 0.0969 | watch_only | none |
| SMH | semiconductor_index | 578.11 |  | 576.9832 | 0.1953 | 582.03 | 576.57 | 0.0709 | watch_only | none |
| AVGO | custom_silicon_networking | 383.61 |  | 383.7814 | -0.0447 | 390.11 | 382.13 | 0.1277 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 933.96 |  | 930.8708 | 0.3319 | 944.99 | 923 | 0.0407 | watch_only | none |
| MRVL | custom_silicon_networking | 206.725 |  | 206.0994 | 0.3035 | 208.61 | 205.31 | 0.179 | watch_only | none |
| DELL | ai_server_oem | 402.02 |  | 402.3443 | -0.0806 | 405.78 | 397.185 | 0.6194 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.48 |  | 46.2381 | 0.5231 | 46.685 | 45.835 | 0.1076 | watch_only | none |
| SMCI | ai_server_oem | 24.825 |  | 24.5893 | 0.9584 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.85 |  | 745.447 | 0.1882 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295 |  | 293.9424 | 0.3598 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.565 |  | 125.0164 | 0.4388 | 126.01 | 122.48 | 0.223 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.41 |  | 76.529 | 1.1512 | 76.615 | 74.55 | 2.4803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 301.07 |  | 299.5304 | 0.514 | 305.09 | 299.13 | 3.8264 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.4 |  | 405.5967 | 0.4446 | 411.01 | 404.21 | 4.6048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 638.66 |  | 636.8237 | 0.2884 | 645.815 | 635.91 | 0.191 | watch_only | none |
| GEV | data_center_power_cooling | 1093.28 |  | 1102.8616 | -0.8688 | 1140.63 | 1103.815 | 1.9748 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 468.79 |  | 469.2875 | -0.106 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 141 |  | 140.3399 | 0.4704 | 142.15 | 140.105 | 4.8085 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.89 |  | 174.9904 | 0.5141 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 309.86 |  | 305.5133 | 1.4228 | 309.72 | 302.3 | 4.5601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 829.165 |  | 813.7362 | 1.896 | 823.31 | 800.37 | 1.4605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 406.59 |  | 401.2286 | 1.3363 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 113.42 |  | 110.5476 | 2.5983 | 109.39 | 107.58 | 4.7434 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 328.2 |  | 324.4447 | 1.1575 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1800.94 |  | 1796.6028 | 0.2414 | 1804.54 | 1786.51 | 0.4342 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 565.3 |  | 560.76 | 0.8096 | 564.91 | 552.71 | 0.1574 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 318.57 |  | 318.2108 | 0.1129 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.625 |  | 215.8348 | -0.0972 | 220.76 | 214.41 | 2.4626 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.24 |  | 364.4243 | 1.8703 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 293.5 |  | 292.9762 | 0.1788 | 296.68 | 291.36 | 0.8245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 65.79 |  | 65.2676 | 0.8004 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.79 |  | 54.4042 | 0.7092 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.79 |  | 140.0768 | -0.2048 | 142.09 | 139.41 | 4.3136 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 337.955 |  | 337.6231 | 0.0983 | 340.205 | 336.3 | 4.3497 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 508.73 |  | 509.3351 | -0.1188 | 512.83 | 507.675 | 0.9671 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 300.61 |  | 299.283 | 0.4434 | 301.84 | 296.5 | 0.1697 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 30.13 |  | 29.7623 | 1.2356 | 29.735 | 28.785 | 0.0996 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.06 |  | 41.4914 | 1.3705 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.69 |  | 23.3453 | 1.4767 | 23.32 | 22.79 | 0.1266 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1523.91 |  | 1517.2709 | 0.4376 | 1540.85 | 1490.29 | 0.1207 | watch_only | none |
| WDC | memory_hbm_storage | 538.93 |  | 533.5826 | 1.0022 | 533.56 | 517.335 | 0.4379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 867.86 |  | 864.0274 | 0.4436 | 866.73 | 845.78 | 0.3053 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 248.17 |  | 247.6552 | 0.2079 | 248.915 | 247.32 | 0.0645 | watch_only | none |
| META | cloud_ai_capex | 647.235 |  | 647.2744 | -0.0061 | 655.425 | 643.54 | 1.7768 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 287.88 |  | 283.3754 | 1.5896 | 286.39 | 275.86 | 0.8997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 165.005 |  | 163.8234 | 0.7212 | 165.88 | 160.77 | 1.7636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
