# Intraday State

- Generated at: `2026-07-21T21:48:39+08:00`
- Market time ET: `2026-07-21T09:48:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 5, 'below_vwap': 34, 'spread_too_wide_or_missing': 12, 'price_stale_or_missing': 1, 'watch_only': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.96 |  | 705.2768 | -0.1867 | 707.09 | 704.52 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 544.88 |  | 548.197 | -0.6051 | 550.77 | 545.11 | 0.1321 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.85 |  | 578.1794 | -0.2299 | 582.03 | 576.57 | 0.0416 | below_vwap | below_vwap |
| SPY | market_regime | 744.38 |  | 745.3232 | -0.1265 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ORCL | cloud_ai_capex | 124.62 |  | 124.6064 | 0.0109 | 126.01 | 122.48 | 0.1123 | watch_only | none |
| 2 | APLD | high_beta_ai_infrastructure | 29.51 |  | 29.4357 | 0.2524 | 29.735 | 28.785 | 0.0678 | watch_only | none |
| 3 | DELL | ai_server_oem | 403.12 |  | 402.5762 | 0.1351 | 405.78 | 397.185 | 0.2803 | watch_only | none |
| 4 | IREN | high_beta_ai_infrastructure | 41.205 |  | 41.0038 | 0.4908 | 41.65 | 40.435 | 0.0971 | watch_only | none |
| 5 | ANET | ai_networking_optical | 174.67 |  | 174.3283 | 0.196 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | COHU | semiconductor_test_packaging | 54.35 |  | 54.1981 | 0.2803 | 54.35 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | AMD | ai_accelerator | 528.8 |  | 528.3151 | 0.0918 | 532.365 | 524.72 | 1.3238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1797.27 |  | 1795.7747 | 0.0833 | 1804.54 | 1786.51 | 0.858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | AMAT | semiconductor_equipment | 561.6 |  | 559.7448 | 0.3314 | 564.91 | 552.71 | 0.8333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | META | cloud_ai_capex | 649.36 |  | 646.8921 | 0.3815 | 655.425 | 643.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | WDC | memory_hbm_storage | 530.04 |  | 528.4953 | 0.2923 | 533.56 | 517.335 | 0.4151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SKHY | memory_hbm_storage | 163.4 |  | 163.394 | 0.0037 | 165.88 | 160.77 | 2.2032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | CRWV | gpu_cloud_ai_factory | 75.935 |  | 75.7995 | 0.1788 | 76.615 | 74.55 | 0.619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | STX | memory_hbm_storage | 864.71 |  | 859.4637 | 0.6104 | 866.73 | 845.78 | 0.8037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 363.675 |  | 361.5947 | 0.5753 | 365.97 | 356.39 | 4.1301 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SNDK | memory_hbm_storage | 1527 |  | 1516.7734 | 0.6742 | 1540.85 | 1490.29 | 0.353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | NVDA | ai_accelerator | 206.49 |  | 207.1112 | -0.2999 | 208.61 | 206.275 | 0.0145 | below_vwap | below_vwap |
| 18 | SMH | semiconductor_index | 576.85 |  | 578.1794 | -0.2299 | 582.03 | 576.57 | 0.0416 | below_vwap | below_vwap |
| 19 | SPY | market_regime | 744.38 |  | 745.3232 | -0.1265 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| 20 | MU | memory_hbm_storage | 931.75 |  | 934.7609 | -0.3221 | 944.99 | 923 | 0.1395 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | COHU | semiconductor_test_packaging | 54.35 |  | 54.1981 | 0.2803 | 54.35 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | DELL | ai_server_oem | 403.12 |  | 402.5762 | 0.1351 | 405.78 | 397.185 | 0.2803 | watch_only | none |
| 3 | IREN | high_beta_ai_infrastructure | 41.205 |  | 41.0038 | 0.4908 | 41.65 | 40.435 | 0.0971 | watch_only | none |
| 4 | ORCL | cloud_ai_capex | 124.62 |  | 124.6064 | 0.0109 | 126.01 | 122.48 | 0.1123 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.51 |  | 29.4357 | 0.2524 | 29.735 | 28.785 | 0.0678 | watch_only | none |
| 6 | TSM | foundry | 416.535 |  | 417.3112 | -0.186 | 418.76 | 415.025 | 0.2905 | below_vwap | below_vwap |
| 7 | NVDA | ai_accelerator | 206.49 |  | 207.1112 | -0.2999 | 208.61 | 206.275 | 0.0145 | below_vwap | below_vwap |
| 8 | SMH | semiconductor_index | 576.85 |  | 578.1794 | -0.2299 | 582.03 | 576.57 | 0.0416 | below_vwap | below_vwap |
| 9 | AVGO | custom_silicon_networking | 382.51 |  | 385.0349 | -0.6558 | 390.11 | 382.13 | 3.3254 | below_vwap | below_vwap,spread_too_wide |
| 10 | SPY | market_regime | 744.38 |  | 745.3232 | -0.1265 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| 11 | MU | memory_hbm_storage | 931.75 |  | 934.7609 | -0.3221 | 944.99 | 923 | 0.1395 | below_vwap | below_vwap |
| 12 | LRCX | semiconductor_equipment | 317.89 |  | 321.2514 | -1.0464 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | LITE | ai_networking_optical | 811.18 |  | 811.1919 | -0.0015 | 823.31 | 800.37 | 0.3748 | below_vwap | below_vwap,spread_too_wide |
| 14 | CIEN | ai_networking_optical | 398.41 |  | 399.3027 | -0.2236 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TT | data_center_power_cooling | 468.28 |  | 472.5912 | -0.9123 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | VRT | data_center_power_cooling | 299.645 |  | 300.9232 | -0.4248 | 305.09 | 299.13 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | MRVL | custom_silicon_networking | 205.34 |  | 206.777 | -0.695 | 208.61 | 205.31 | 2.922 | below_vwap | below_vwap,spread_too_wide |
| 18 | PWR | data_center_power_cooling | 635.91 |  | 640.145 | -0.6616 | 645.815 | 635.91 | 0.5693 | below_vwap | below_vwap,spread_too_wide |
| 19 | IWM | market_regime | 293.3 |  | 293.7372 | -0.1488 | 294.51 | 292.72 | 0.0102 | below_vwap | below_vwap |
| 20 | ETN | data_center_power_cooling | 405.49 |  | 406.2472 | -0.1864 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.96 |  | 705.2768 | -0.1867 | 707.09 | 704.52 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.95 |  | 70.3796 | -0.6103 | 70.84 | 70.09 | 0.0286 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.49 |  | 207.1112 | -0.2999 | 208.61 | 206.275 | 0.0145 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 398.94 |  | 399.1001 | -0.0401 | 401.45 | 396.36 | 0.0426 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 323.14 |  | 324.1246 | -0.3038 | 325.59 | 322.63 | 0.0248 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 349.21 |  | 349.6183 | -0.1168 | 350.985 | 347.69 | 0.0515 | below_vwap | below_vwap |
| AMD | ai_accelerator | 528.8 |  | 528.3151 | 0.0918 | 532.365 | 524.72 | 1.3238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 416.535 |  | 417.3112 | -0.186 | 418.76 | 415.025 | 0.2905 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 544.88 |  | 548.197 | -0.6051 | 550.77 | 545.11 | 0.1321 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.85 |  | 578.1794 | -0.2299 | 582.03 | 576.57 | 0.0416 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.51 |  | 385.0349 | -0.6558 | 390.11 | 382.13 | 3.3254 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 931.75 |  | 934.7609 | -0.3221 | 944.99 | 923 | 0.1395 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 205.34 |  | 206.777 | -0.695 | 208.61 | 205.31 | 2.922 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.12 |  | 402.5762 | 0.1351 | 405.78 | 397.185 | 0.2803 | watch_only | none |
| HPE | ai_server_oem | 46.2 |  | 46.3099 | -0.2374 | 46.685 | 45.835 | 0.1732 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.47 |  | 24.5698 | -0.4061 | 24.77 | 24.34 | 0.1226 | below_vwap | below_vwap |
| SPY | market_regime | 744.38 |  | 745.3232 | -0.1265 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.3 |  | 293.7372 | -0.1488 | 294.51 | 292.72 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.62 |  | 124.6064 | 0.0109 | 126.01 | 122.48 | 0.1123 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 75.935 |  | 75.7995 | 0.1788 | 76.615 | 74.55 | 0.619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.645 |  | 300.9232 | -0.4248 | 305.09 | 299.13 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 405.49 |  | 406.2472 | -0.1864 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635.91 |  | 640.145 | -0.6616 | 645.815 | 635.91 | 0.5693 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1096.64 |  | 1119.704 | -2.0598 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 468.28 |  | 472.5912 | -0.9123 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.24 |  | 140.9737 | -0.5205 | 142.15 | 140.24 | 1.7042 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 174.67 |  | 174.3283 | 0.196 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 302.11 |  | 305.0528 | -0.9647 | 309.72 | 302.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 811.18 |  | 811.1919 | -0.0015 | 823.31 | 800.37 | 0.3748 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 398.41 |  | 399.3027 | -0.2236 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 108.4 |  | 108.621 | -0.2034 | 109.39 | 107.58 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.41 |  | 326.6134 | -0.0623 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1797.27 |  | 1795.7747 | 0.0833 | 1804.54 | 1786.51 | 0.858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 561.6 |  | 559.7448 | 0.3314 | 564.91 | 552.71 | 0.8333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 317.89 |  | 321.2514 | -1.0464 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.69 |  | 216.3131 | -0.2881 | 220.76 | 214.41 | 0.2782 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 363.675 |  | 361.5947 | 0.5753 | 365.97 | 356.39 | 4.1301 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.65 |  | 293.8595 | -0.0713 | 296.68 | 292.03 | 0.8377 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65 |  | 65.2751 | -0.4214 | 66.54 | 65 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.35 |  | 54.1981 | 0.2803 | 54.35 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.56 |  | 140.4518 | -0.635 | 142.09 | 139.56 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 338.55 |  | 338.9375 | -0.1143 | 340.205 | 338 | 0.6232 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 508.28 |  | 509.8416 | -0.3063 | 512.83 | 507.675 | 0.2715 | below_vwap | below_vwap |
| APD | industrial_gases | 296.86 |  | 299.2619 | -0.8026 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.51 |  | 29.4357 | 0.2524 | 29.735 | 28.785 | 0.0678 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.205 |  | 41.0038 | 0.4908 | 41.65 | 40.435 | 0.0971 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 23.09 |  | 23.1342 | -0.1912 | 23.32 | 22.79 | 0.1299 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1527 |  | 1516.7734 | 0.6742 | 1540.85 | 1490.29 | 0.353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 530.04 |  | 528.4953 | 0.2923 | 533.56 | 517.335 | 0.4151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 864.71 |  | 859.4637 | 0.6104 | 866.73 | 845.78 | 0.8037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.61 |  | 248.1605 | -0.2218 | 248.915 | 247.32 | 0.0404 | below_vwap | below_vwap |
| META | cloud_ai_capex | 649.36 |  | 646.8921 | 0.3815 | 655.425 | 643.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ARM | ai_accelerator | 276.13 |  | 279.7632 | -1.2987 | 286.39 | 275.86 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 163.4 |  | 163.394 | 0.0037 | 165.88 | 160.77 | 2.2032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
