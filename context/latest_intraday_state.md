# Intraday State

- Generated at: `2026-07-21T21:52:31+08:00`
- Market time ET: `2026-07-21T09:52:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'below_opening_15m_low': 4, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 2, 'watch_only': 7, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.97 |  | 705.1992 | -0.0325 | 707.09 | 704.52 | 0.0199 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 546.635 |  | 548.032 | -0.2549 | 550.77 | 545.11 | 0.1079 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.445 |  | 578.0812 | -0.1101 | 582.03 | 576.57 | 0.0762 | below_vwap | below_vwap |
| SPY | market_regime | 744.44 |  | 745.256 | -0.1095 | 746.6 | 744.3 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | STX | memory_hbm_storage | 872.79 |  | 861.1848 | 1.3476 | 866.73 | 845.78 | 0.3071 | buy_precheck_manual_confirm | none |
| 2 | APLD | high_beta_ai_infrastructure | 29.8 |  | 29.4801 | 1.0852 | 29.735 | 28.785 | 0.1342 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 936.41 |  | 934.7811 | 0.1743 | 944.99 | 923 | 0.0982 | watch_only | none |
| 2 | HPE | ai_server_oem | 46.34 |  | 46.3134 | 0.0574 | 46.685 | 45.835 | 0.1295 | watch_only | none |
| 3 | SMCI | ai_server_oem | 24.62 |  | 24.5493 | 0.2881 | 24.77 | 24.34 | 0.0812 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 23.28 |  | 23.1503 | 0.5602 | 23.32 | 22.79 | 0.1289 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.8 |  | 29.4801 | 1.0852 | 29.735 | 28.785 | 0.1342 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 125.52 |  | 124.7026 | 0.6554 | 126.01 | 122.48 | 0.3426 | watch_only | none |
| 7 | STX | memory_hbm_storage | 872.79 |  | 861.1848 | 1.3476 | 866.73 | 845.78 | 0.3071 | buy_precheck_manual_confirm | none |
| 8 | COHU | semiconductor_test_packaging | 54.35 |  | 54.1981 | 0.2803 | 54.35 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ARM | ai_accelerator | 279.55 |  | 279.1762 | 0.1339 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | COHR | ai_networking_optical | 305.78 |  | 305.0042 | 0.2544 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MKSI | semiconductor_materials | 338.455 |  | 338.1146 | 0.1007 | 340.205 | 337.12 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.54 |  | 41.0491 | 1.1959 | 41.65 | 40.435 | 0.0963 | watch_only | none |
| 13 | ANET | ai_networking_optical | 175.03 |  | 174.3676 | 0.3799 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ASML | semiconductor_equipment | 1801.78 |  | 1796.4889 | 0.2945 | 1804.54 | 1786.51 | 0.8331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 401.47 |  | 399.3361 | 0.5344 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1538.71 |  | 1519.535 | 1.2619 | 1540.85 | 1490.29 | 0.1956 | watch_only | none |
| 17 | META | cloud_ai_capex | 648.78 |  | 647.166 | 0.2494 | 655.425 | 643.54 | 4.3281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ALAB | ai_networking_optical | 327.96 |  | 326.5971 | 0.4173 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | MSFT | cloud_ai_capex | 399.81 |  | 399.1296 | 0.1705 | 401.45 | 396.36 | 0.7679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMKR | semiconductor_test_packaging | 65.56 |  | 65.3053 | 0.39 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | STX | memory_hbm_storage | 872.79 |  | 861.1848 | 1.3476 | 866.73 | 845.78 | 0.3071 | buy_precheck_manual_confirm | none |
| 2 | APLD | high_beta_ai_infrastructure | 29.8 |  | 29.4801 | 1.0852 | 29.735 | 28.785 | 0.1342 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 533.155 |  | 529.5593 | 0.679 | 532.365 | 524.72 | 1.9638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | WDC | memory_hbm_storage | 537 |  | 530.5435 | 1.217 | 533.56 | 517.335 | 0.3538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | COHU | semiconductor_test_packaging | 54.35 |  | 54.1981 | 0.2803 | 54.35 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MU | memory_hbm_storage | 936.41 |  | 934.7811 | 0.1743 | 944.99 | 923 | 0.0982 | watch_only | none |
| 7 | AAOI | ai_networking_optical | 110.66 |  | 108.7338 | 1.7715 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | CRWV | gpu_cloud_ai_factory | 77.07 |  | 75.8688 | 1.5832 | 76.615 | 74.55 | 3.4255 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | HPE | ai_server_oem | 46.34 |  | 46.3134 | 0.0574 | 46.685 | 45.835 | 0.1295 | watch_only | none |
| 10 | SNDK | memory_hbm_storage | 1538.71 |  | 1519.535 | 1.2619 | 1540.85 | 1490.29 | 0.1956 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 23.28 |  | 23.1503 | 0.5602 | 23.32 | 22.79 | 0.1289 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 41.54 |  | 41.0491 | 1.1959 | 41.65 | 40.435 | 0.0963 | watch_only | none |
| 13 | ORCL | cloud_ai_capex | 125.52 |  | 124.7026 | 0.6554 | 126.01 | 122.48 | 0.3426 | watch_only | none |
| 14 | SMCI | ai_server_oem | 24.62 |  | 24.5493 | 0.2881 | 24.77 | 24.34 | 0.0812 | watch_only | none |
| 15 | TSM | foundry | 416.4 |  | 417.28 | -0.2109 | 418.76 | 415.025 | 0.6724 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMH | semiconductor_index | 577.445 |  | 578.0812 | -0.1101 | 582.03 | 576.57 | 0.0762 | below_vwap | below_vwap |
| 17 | SOXX | semiconductor_index | 546.635 |  | 548.032 | -0.2549 | 550.77 | 545.11 | 0.1079 | below_vwap | below_vwap |
| 18 | QQQ | market_regime | 704.97 |  | 705.1992 | -0.0325 | 707.09 | 704.52 | 0.0199 | below_vwap | below_vwap |
| 19 | SPY | market_regime | 744.44 |  | 745.256 | -0.1095 | 746.6 | 744.3 | 0.004 | below_vwap | below_vwap |
| 20 | LRCX | semiconductor_equipment | 317.89 |  | 320.7268 | -0.8845 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.97 |  | 705.1992 | -0.0325 | 707.09 | 704.52 | 0.0199 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.23 |  | 70.351 | -0.172 | 70.84 | 70.09 | 0.0285 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 205.975 |  | 207.0076 | -0.4988 | 208.61 | 206.275 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.81 |  | 399.1296 | 0.1705 | 401.45 | 396.36 | 0.7679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 322.915 |  | 323.9667 | -0.3246 | 325.59 | 322.63 | 0.1889 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 348.405 |  | 349.5444 | -0.326 | 350.985 | 347.69 | 0.2468 | below_vwap | below_vwap |
| AMD | ai_accelerator | 533.155 |  | 529.5593 | 0.679 | 532.365 | 524.72 | 1.9638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 416.4 |  | 417.28 | -0.2109 | 418.76 | 415.025 | 0.6724 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.635 |  | 548.032 | -0.2549 | 550.77 | 545.11 | 0.1079 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.445 |  | 578.0812 | -0.1101 | 582.03 | 576.57 | 0.0762 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.44 |  | 384.82 | -0.8783 | 390.11 | 382.13 | 0.9176 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 936.41 |  | 934.7811 | 0.1743 | 944.99 | 923 | 0.0982 | watch_only | none |
| MRVL | custom_silicon_networking | 205.86 |  | 206.6472 | -0.381 | 208.61 | 205.31 | 0.1166 | below_vwap | below_vwap |
| DELL | ai_server_oem | 405.05 |  | 402.622 | 0.603 | 405.78 | 397.185 | 4.3822 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.34 |  | 46.3134 | 0.0574 | 46.685 | 45.835 | 0.1295 | watch_only | none |
| SMCI | ai_server_oem | 24.62 |  | 24.5493 | 0.2881 | 24.77 | 24.34 | 0.0812 | watch_only | none |
| SPY | market_regime | 744.44 |  | 745.256 | -0.1095 | 746.6 | 744.3 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.105 |  | 293.7311 | -0.2131 | 294.51 | 292.72 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.52 |  | 124.7026 | 0.6554 | 126.01 | 122.48 | 0.3426 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.07 |  | 75.8688 | 1.5832 | 76.615 | 74.55 | 3.4255 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 298.745 |  | 300.5212 | -0.5911 | 305.09 | 299.13 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 405.85 |  | 406.184 | -0.0822 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 637.125 |  | 639.7425 | -0.4091 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1096.51 |  | 1116.0496 | -1.7508 | 1140.63 | 1103.815 | 4.4131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 468.56 |  | 471.4228 | -0.6073 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.24 |  | 140.9737 | -0.5205 | 142.15 | 140.24 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ANET | ai_networking_optical | 175.03 |  | 174.3676 | 0.3799 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 305.78 |  | 305.0042 | 0.2544 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 819.08 |  | 812.3099 | 0.8334 | 823.31 | 800.37 | 1.4516 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 401.47 |  | 399.3361 | 0.5344 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 110.66 |  | 108.7338 | 1.7715 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 327.96 |  | 326.5971 | 0.4173 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1801.78 |  | 1796.4889 | 0.2945 | 1804.54 | 1786.51 | 0.8331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 562.13 |  | 560.008 | 0.3789 | 564.91 | 552.71 | 0.7703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 317.89 |  | 320.7268 | -0.8845 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.39 |  | 216.2544 | -0.3997 | 220.76 | 214.41 | 2.4839 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 365.8 |  | 362.0833 | 1.0265 | 365.97 | 356.39 | 3.2121 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 291.89 |  | 293.6732 | -0.6072 | 296.68 | 291.43 | 1.85 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.56 |  | 65.3053 | 0.39 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.35 |  | 54.1981 | 0.2803 | 54.35 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 140.12 |  | 140.4188 | -0.2128 | 142.09 | 139.56 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 338.455 |  | 338.1146 | 0.1007 | 340.205 | 337.12 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.985 |  | 509.5848 | -0.1177 | 512.83 | 507.675 | 1.0157 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 298.14 |  | 298.5305 | -0.1308 | 301.84 | 296.5 | 0.3656 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.8 |  | 29.4801 | 1.0852 | 29.735 | 28.785 | 0.1342 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.54 |  | 41.0491 | 1.1959 | 41.65 | 40.435 | 0.0963 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 23.28 |  | 23.1503 | 0.5602 | 23.32 | 22.79 | 0.1289 | watch_only | none |
| SNDK | memory_hbm_storage | 1538.71 |  | 1519.535 | 1.2619 | 1540.85 | 1490.29 | 0.1956 | watch_only | none |
| WDC | memory_hbm_storage | 537 |  | 530.5435 | 1.217 | 533.56 | 517.335 | 0.3538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 872.79 |  | 861.1848 | 1.3476 | 866.73 | 845.78 | 0.3071 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.43 |  | 248.0638 | -0.2555 | 248.915 | 247.32 | 0.0485 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.78 |  | 647.166 | 0.2494 | 655.425 | 643.54 | 4.3281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.55 |  | 279.1762 | 0.1339 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 165.43 |  | 163.7145 | 1.0479 | 165.88 | 160.77 | 1.209 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
