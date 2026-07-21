# Intraday State

- Generated at: `2026-07-21T21:56:23+08:00`
- Market time ET: `2026-07-21T09:56:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 6, 'below_vwap': 23, 'watch_only': 4, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 20, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.51 |  | 705.1596 | -0.0921 | 707.09 | 704.52 | 0.0298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545.64 |  | 547.9926 | -0.4293 | 550.77 | 545.11 | 0.0825 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.855 |  | 577.967 | -0.1924 | 582.03 | 576.57 | 0.0693 | below_vwap | below_vwap |
| SPY | market_regime | 744.83 |  | 745.2224 | -0.0527 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.4 |  | 23.1746 | 0.9725 | 23.32 | 22.79 | 0.1282 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 42.15 |  | 41.161 | 2.4026 | 41.65 | 40.435 | 0.0712 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 509.57 |  | 509.53 | 0.0079 | 512.83 | 507.675 | 0.1217 | watch_only | none |
| 2 | MSFT | cloud_ai_capex | 400.4 |  | 399.2067 | 0.2989 | 401.45 | 396.36 | 0.1848 | watch_only | none |
| 3 | ANET | ai_networking_optical | 175.53 |  | 174.4585 | 0.6142 | 176.06 | 172.32 | 0.3076 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 23.4 |  | 23.1746 | 0.9725 | 23.32 | 22.79 | 0.1282 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 24.72 |  | 24.5635 | 0.6369 | 24.77 | 24.34 | 0.0809 | watch_only | none |
| 6 | COHU | semiconductor_test_packaging | 54.41 |  | 54.2295 | 0.3329 | 54.41 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | META | cloud_ai_capex | 648.825 |  | 647.2604 | 0.2417 | 655.425 | 643.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ALAB | ai_networking_optical | 326.825 |  | 326.6702 | 0.0474 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ENTG | semiconductor_materials | 140.51 |  | 140.4115 | 0.0702 | 142.09 | 139.56 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | APD | industrial_gases | 298.55 |  | 298.538 | 0.004 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | AMKR | semiconductor_test_packaging | 65.42 |  | 65.3252 | 0.1452 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ASML | semiconductor_equipment | 1799.4 |  | 1796.97 | 0.1352 | 1804.54 | 1786.51 | 0.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | DELL | ai_server_oem | 404.9 |  | 402.6898 | 0.5489 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ARM | ai_accelerator | 280.02 |  | 279.1811 | 0.3005 | 286.39 | 275.86 | 1.9356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 364.385 |  | 362.3575 | 0.5595 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1524.83 |  | 1521.2647 | 0.2344 | 1540.85 | 1490.29 | 1.4428 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MKSI | semiconductor_materials | 338.455 |  | 338.1146 | 0.1007 | 340.205 | 337.12 | 0.5259 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | IREN | high_beta_ai_infrastructure | 42.15 |  | 41.161 | 2.4026 | 41.65 | 40.435 | 0.0712 | buy_precheck_manual_confirm | none |
| 19 | STX | memory_hbm_storage | 869.39 |  | 862.9278 | 0.7489 | 866.73 | 845.78 | 1.1353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 534.9 |  | 532.2362 | 0.5005 | 533.56 | 517.335 | 0.5422 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.4 |  | 23.1746 | 0.9725 | 23.32 | 22.79 | 0.1282 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 42.15 |  | 41.161 | 2.4026 | 41.65 | 40.435 | 0.0712 | buy_precheck_manual_confirm | none |
| 3 | CIEN | ai_networking_optical | 403.42 |  | 399.8527 | 0.8922 | 401.91 | 397.18 | 4.3032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | STX | memory_hbm_storage | 869.39 |  | 862.9278 | 0.7489 | 866.73 | 845.78 | 1.1353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | WDC | memory_hbm_storage | 534.9 |  | 532.2362 | 0.5005 | 533.56 | 517.335 | 0.5422 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 175.53 |  | 174.4585 | 0.6142 | 176.06 | 172.32 | 0.3076 | watch_only | none |
| 7 | COHU | semiconductor_test_packaging | 54.41 |  | 54.2295 | 0.3329 | 54.41 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | AAOI | ai_networking_optical | 112.07 |  | 109.2161 | 2.6131 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | CRWV | gpu_cloud_ai_factory | 77.035 |  | 76.0215 | 1.3332 | 76.615 | 74.55 | 2.2068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | APLD | high_beta_ai_infrastructure | 30.06 |  | 29.5511 | 1.7221 | 29.735 | 28.785 | 0.3992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | LIN | industrial_gases | 509.57 |  | 509.53 | 0.0079 | 512.83 | 507.675 | 0.1217 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 400.4 |  | 399.2067 | 0.2989 | 401.45 | 396.36 | 0.1848 | watch_only | none |
| 13 | SMCI | ai_server_oem | 24.72 |  | 24.5635 | 0.6369 | 24.77 | 24.34 | 0.0809 | watch_only | none |
| 14 | TSM | foundry | 416.75 |  | 417.2384 | -0.1171 | 418.76 | 415.025 | 0.3143 | below_vwap | below_vwap |
| 15 | SMH | semiconductor_index | 576.855 |  | 577.967 | -0.1924 | 582.03 | 576.57 | 0.0693 | below_vwap | below_vwap |
| 16 | SOXX | semiconductor_index | 545.64 |  | 547.9926 | -0.4293 | 550.77 | 545.11 | 0.0825 | below_vwap | below_vwap |
| 17 | AMD | ai_accelerator | 528.29 |  | 529.9941 | -0.3215 | 532.365 | 524.72 | 1.8929 | below_vwap | below_vwap,spread_too_wide |
| 18 | SPY | market_regime | 744.83 |  | 745.2224 | -0.0527 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| 19 | MU | memory_hbm_storage | 932.53 |  | 934.8418 | -0.2473 | 944.99 | 923 | 0.1137 | below_vwap | below_vwap |
| 20 | LRCX | semiconductor_equipment | 317.18 |  | 320.0913 | -0.9095 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.51 |  | 705.1596 | -0.0921 | 707.09 | 704.52 | 0.0298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.14 |  | 70.3352 | -0.2775 | 70.84 | 70.09 | 0.0143 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 205.535 |  | 206.8587 | -0.6399 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.4 |  | 399.2067 | 0.2989 | 401.45 | 396.36 | 0.1848 | watch_only | none |
| AAPL | mega_cap_platform | 322.61 |  | 323.8139 | -0.3718 | 325.59 | 322.63 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 349.24 |  | 349.5073 | -0.0765 | 350.985 | 347.69 | 0.0487 | below_vwap | below_vwap |
| AMD | ai_accelerator | 528.29 |  | 529.9941 | -0.3215 | 532.365 | 524.72 | 1.8929 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 416.75 |  | 417.2384 | -0.1171 | 418.76 | 415.025 | 0.3143 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.64 |  | 547.9926 | -0.4293 | 550.77 | 545.11 | 0.0825 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.855 |  | 577.967 | -0.1924 | 582.03 | 576.57 | 0.0693 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 380.64 |  | 384.622 | -1.0353 | 390.11 | 382.13 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MU | memory_hbm_storage | 932.53 |  | 934.8418 | -0.2473 | 944.99 | 923 | 0.1137 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.3 |  | 206.5765 | -0.1338 | 208.61 | 205.31 | 1.2458 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 404.9 |  | 402.6898 | 0.5489 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.265 |  | 46.3092 | -0.0954 | 46.685 | 45.835 | 1.0375 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 24.72 |  | 24.5635 | 0.6369 | 24.77 | 24.34 | 0.0809 | watch_only | none |
| SPY | market_regime | 744.83 |  | 745.2224 | -0.0527 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.45 |  | 293.6879 | -0.081 | 294.51 | 292.72 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.75 |  | 124.8316 | 0.7357 | 126.01 | 122.48 | 0.9622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.035 |  | 76.0215 | 1.3332 | 76.615 | 74.55 | 2.2068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.48 |  | 300.2378 | -0.2524 | 305.09 | 299.13 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 405.84 |  | 406.1739 | -0.0822 | 411.01 | 404.21 | 0.1626 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 639.18 |  | 639.4393 | -0.0406 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1097.99 |  | 1113.7576 | -1.4157 | 1140.63 | 1103.815 | 4.4308 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 468.3 |  | 471.267 | -0.6296 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.43 |  | 140.6118 | -0.1293 | 142.15 | 140.23 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.53 |  | 174.4585 | 0.6142 | 176.06 | 172.32 | 0.3076 | watch_only | none |
| COHR | ai_networking_optical | 304.65 |  | 305.0246 | -0.1228 | 309.72 | 302.3 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 811.99 |  | 812.4954 | -0.0622 | 823.31 | 800.37 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 403.42 |  | 399.8527 | 0.8922 | 401.91 | 397.18 | 4.3032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 112.07 |  | 109.2161 | 2.6131 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 326.825 |  | 326.6702 | 0.0474 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1799.4 |  | 1796.97 | 0.1352 | 1804.54 | 1786.51 | 0.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 559.93 |  | 560.1063 | -0.0315 | 564.91 | 552.71 | 0.3893 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.18 |  | 320.0913 | -0.9095 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.75 |  | 216.1882 | -0.2027 | 220.76 | 214.41 | 0.0695 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 364.385 |  | 362.3575 | 0.5595 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 292.97 |  | 293.6544 | -0.2331 | 296.68 | 291.43 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.42 |  | 65.3252 | 0.1452 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.41 |  | 54.2295 | 0.3329 | 54.41 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 140.51 |  | 140.4115 | 0.0702 | 142.09 | 139.56 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 338.455 |  | 338.1146 | 0.1007 | 340.205 | 337.12 | 0.5259 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 509.57 |  | 509.53 | 0.0079 | 512.83 | 507.675 | 0.1217 | watch_only | none |
| APD | industrial_gases | 298.55 |  | 298.538 | 0.004 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.06 |  | 29.5511 | 1.7221 | 29.735 | 28.785 | 0.3992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 42.15 |  | 41.161 | 2.4026 | 41.65 | 40.435 | 0.0712 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.4 |  | 23.1746 | 0.9725 | 23.32 | 22.79 | 0.1282 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1524.83 |  | 1521.2647 | 0.2344 | 1540.85 | 1490.29 | 1.4428 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 534.9 |  | 532.2362 | 0.5005 | 533.56 | 517.335 | 0.5422 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 869.39 |  | 862.9278 | 0.7489 | 866.73 | 845.78 | 1.1353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 246.99 |  | 247.9522 | -0.388 | 248.915 | 247.32 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 648.825 |  | 647.2604 | 0.2417 | 655.425 | 643.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ARM | ai_accelerator | 280.02 |  | 279.1811 | 0.3005 | 286.39 | 275.86 | 1.9356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 164.46 |  | 163.8659 | 0.3625 | 165.88 | 160.77 | 1.5809 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
