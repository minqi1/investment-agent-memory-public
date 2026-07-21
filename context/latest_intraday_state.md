# Intraday State

- Generated at: `2026-07-21T22:15:53+08:00`
- Market time ET: `2026-07-21T10:15:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 12, 'watch_only': 6, 'manual_confirm_candidate': 5, 'below_vwap': 19, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 13}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.36 |  | 704.6992 | -0.0481 | 707.09 | 704.52 | 0.0653 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 543.71 |  | 546.2491 | -0.4648 | 550.77 | 545.11 | 0.1085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 574.92 |  | 577.0054 | -0.3614 | 582.03 | 576.57 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.725 |  | 745.2372 | 0.0655 | 746.6 | 744.3 | 0.008 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.6 |  | 293.7641 | 0.2845 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.297 | 1.0429 | 23.32 | 22.79 | 0.085 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 41.88 |  | 41.4095 | 1.1363 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.085 |  | 324.0308 | 0.6339 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 30.005 |  | 29.7355 | 0.9062 | 29.735 | 28.785 | 0.0667 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.6 |  | 293.7641 | 0.2845 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 326.085 |  | 324.0308 | 0.6339 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 745.725 |  | 745.2372 | 0.0655 | 746.6 | 744.3 | 0.008 | watch_only | none |
| 4 | HPE | ai_server_oem | 46.36 |  | 46.2182 | 0.3067 | 46.685 | 45.835 | 0.1079 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 349.69 |  | 349.5225 | 0.0479 | 350.985 | 347.69 | 0.1258 | watch_only | none |
| 6 | ORCL | cloud_ai_capex | 125.34 |  | 124.9717 | 0.2947 | 126.01 | 122.48 | 0.1117 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 400.03 |  | 399.4711 | 0.1399 | 401.45 | 396.36 | 0.175 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.67 |  | 24.5723 | 0.3976 | 24.77 | 24.34 | 0.0405 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 41.88 |  | 41.4095 | 1.1363 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.297 | 1.0429 | 23.32 | 22.79 | 0.085 | buy_precheck_manual_confirm | none |
| 11 | ETN | data_center_power_cooling | 406.09 |  | 405.5877 | 0.1239 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ALAB | ai_networking_optical | 324.425 |  | 324.3146 | 0.034 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APLD | high_beta_ai_infrastructure | 30.005 |  | 29.7355 | 0.9062 | 29.735 | 28.785 | 0.0667 | buy_precheck_manual_confirm | none |
| 14 | COHR | ai_networking_optical | 305.44 |  | 304.85 | 0.1935 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APD | industrial_gases | 299.025 |  | 298.6996 | 0.1089 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CIEN | ai_networking_optical | 402.585 |  | 400.4583 | 0.5311 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ANET | ai_networking_optical | 175.66 |  | 174.8884 | 0.4412 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMAT | semiconductor_equipment | 561.67 |  | 559.8557 | 0.3241 | 564.91 | 552.71 | 0.7976 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 300.005 |  | 299.7099 | 0.0985 | 305.09 | 299.13 | 2.3133 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMKR | semiconductor_test_packaging | 65.335 |  | 65.277 | 0.0888 | 66.54 | 65 | 4.8366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.6 |  | 293.7641 | 0.2845 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.297 | 1.0429 | 23.32 | 22.79 | 0.085 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 41.88 |  | 41.4095 | 1.1363 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.085 |  | 324.0308 | 0.6339 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 30.005 |  | 29.7355 | 0.9062 | 29.735 | 28.785 | 0.0667 | buy_precheck_manual_confirm | none |
| 6 | CIEN | ai_networking_optical | 402.585 |  | 400.4583 | 0.5311 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TER | semiconductor_test_packaging | 366.15 |  | 363.1418 | 0.8284 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SPY | market_regime | 745.725 |  | 745.2372 | 0.0655 | 746.6 | 744.3 | 0.008 | watch_only | none |
| 9 | AAOI | ai_networking_optical | 111.21 |  | 109.9389 | 1.1562 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | CRWV | gpu_cloud_ai_factory | 77.03 |  | 76.3207 | 0.9293 | 76.615 | 74.55 | 2.5315 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | HPE | ai_server_oem | 46.36 |  | 46.2182 | 0.3067 | 46.685 | 45.835 | 0.1079 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 349.69 |  | 349.5225 | 0.0479 | 350.985 | 347.69 | 0.1258 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 400.03 |  | 399.4711 | 0.1399 | 401.45 | 396.36 | 0.175 | watch_only | none |
| 14 | ORCL | cloud_ai_capex | 125.34 |  | 124.9717 | 0.2947 | 126.01 | 122.48 | 0.1117 | watch_only | none |
| 15 | SMCI | ai_server_oem | 24.67 |  | 24.5723 | 0.3976 | 24.77 | 24.34 | 0.0405 | watch_only | none |
| 16 | TSM | foundry | 415.635 |  | 416.5224 | -0.213 | 418.76 | 415.025 | 0.2983 | below_vwap | below_vwap |
| 17 | AVGO | custom_silicon_networking | 383.325 |  | 383.8902 | -0.1472 | 390.11 | 382.13 | 1.1739 | below_vwap | below_vwap,spread_too_wide |
| 18 | AMD | ai_accelerator | 526.25 |  | 529.3705 | -0.5895 | 532.365 | 524.72 | 1.391 | below_vwap | below_vwap,spread_too_wide |
| 19 | ASML | semiconductor_equipment | 1792.51 |  | 1796.9314 | -0.2461 | 1804.54 | 1786.51 | 0.1936 | below_vwap | below_vwap |
| 20 | LITE | ai_networking_optical | 810.8 |  | 811.97 | -0.1441 | 823.31 | 800.37 | 1.073 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.36 |  | 704.6992 | -0.0481 | 707.09 | 704.52 | 0.0653 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.03 |  | 70.2491 | -0.3119 | 70.84 | 70.09 | 0.0286 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.52 |  | 206.4413 | -0.9307 | 208.61 | 206.275 | 0.0244 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.03 |  | 399.4711 | 0.1399 | 401.45 | 396.36 | 0.175 | watch_only | none |
| AAPL | mega_cap_platform | 326.085 |  | 324.0308 | 0.6339 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.69 |  | 349.5225 | 0.0479 | 350.985 | 347.69 | 0.1258 | watch_only | none |
| AMD | ai_accelerator | 526.25 |  | 529.3705 | -0.5895 | 532.365 | 524.72 | 1.391 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.635 |  | 416.5224 | -0.213 | 418.76 | 415.025 | 0.2983 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 543.71 |  | 546.2491 | -0.4648 | 550.77 | 545.11 | 0.1085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 574.92 |  | 577.0054 | -0.3614 | 582.03 | 576.57 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 383.325 |  | 383.8902 | -0.1472 | 390.11 | 382.13 | 1.1739 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 922.9 |  | 932.5592 | -1.0358 | 944.99 | 923 | 0.1062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 204.36 |  | 206.1983 | -0.8915 | 208.61 | 205.31 | 1.5659 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.98 |  | 402.6 | -0.4024 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.36 |  | 46.2182 | 0.3067 | 46.685 | 45.835 | 0.1079 | watch_only | none |
| SMCI | ai_server_oem | 24.67 |  | 24.5723 | 0.3976 | 24.77 | 24.34 | 0.0405 | watch_only | none |
| SPY | market_regime | 745.725 |  | 745.2372 | 0.0655 | 746.6 | 744.3 | 0.008 | watch_only | none |
| IWM | market_regime | 294.6 |  | 293.7641 | 0.2845 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.34 |  | 124.9717 | 0.2947 | 126.01 | 122.48 | 0.1117 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.03 |  | 76.3207 | 0.9293 | 76.615 | 74.55 | 2.5315 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 300.005 |  | 299.7099 | 0.0985 | 305.09 | 299.13 | 2.3133 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.09 |  | 405.5877 | 0.1239 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 635.34 |  | 637.3919 | -0.3219 | 645.815 | 635.91 | 4.8321 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1087.83 |  | 1107.051 | -1.7362 | 1140.63 | 1103.815 | 3.4941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 469.1 |  | 469.9138 | -0.1732 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.28 |  | 140.3143 | -0.0245 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.66 |  | 174.8884 | 0.4412 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 305.44 |  | 304.85 | 0.1935 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 810.8 |  | 811.97 | -0.1441 | 823.31 | 800.37 | 1.073 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.585 |  | 400.4583 | 0.5311 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 111.21 |  | 109.9389 | 1.1562 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 324.425 |  | 324.3146 | 0.034 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1792.51 |  | 1796.9314 | -0.2461 | 1804.54 | 1786.51 | 0.1936 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 561.67 |  | 559.8557 | 0.3241 | 564.91 | 552.71 | 0.7976 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 315.355 |  | 318.4258 | -0.9644 | 328.135 | 317.17 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.32 |  | 215.8821 | -0.2604 | 220.76 | 214.41 | 2.9816 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 366.15 |  | 363.1418 | 0.8284 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.36 |  | 293.0832 | -0.5879 | 296.68 | 291.36 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.335 |  | 65.277 | 0.0888 | 66.54 | 65 | 4.8366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 54.17 |  | 54.2533 | -0.1535 | 54.45 | 54.03 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.97 |  | 140.261 | -0.9204 | 142.09 | 139.41 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 336.02 |  | 337.7547 | -0.5136 | 340.205 | 336.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.795 |  | 509.4116 | -0.3173 | 512.83 | 507.675 | 0.8783 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 299.025 |  | 298.6996 | 0.1089 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.005 |  | 29.7355 | 0.9062 | 29.735 | 28.785 | 0.0667 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.88 |  | 41.4095 | 1.1363 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.297 | 1.0429 | 23.32 | 22.79 | 0.085 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1501.88 |  | 1519.3812 | -1.1519 | 1540.85 | 1490.29 | 0.4141 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 532.51 |  | 533.0362 | -0.0987 | 533.56 | 517.335 | 3.1793 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 861.94 |  | 864.0677 | -0.2462 | 866.73 | 845.78 | 0.2854 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 247.55 |  | 247.7456 | -0.0789 | 248.915 | 247.32 | 0.0283 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.72 |  | 647.3933 | -0.104 | 655.425 | 643.54 | 4.079 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 284.02 |  | 280.9925 | 1.0774 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 163.175 |  | 163.6346 | -0.2809 | 165.88 | 160.77 | 1.1399 | below_vwap | below_vwap,spread_too_wide |
