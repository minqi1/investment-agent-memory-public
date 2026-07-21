# Intraday State

- Generated at: `2026-07-21T22:04:14+08:00`
- Market time ET: `2026-07-21T10:04:15-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 15, 'below_vwap': 24, 'spread_too_wide_or_missing': 8, 'price_stale_or_missing': 1, 'watch_only': 5, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.85 |  | 704.98 | -0.1603 | 707.09 | 704.52 | 0.0256 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 542.39 |  | 547.1206 | -0.8646 | 550.77 | 545.11 | 0.1051 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 574.27 |  | 577.2357 | -0.5138 | 582.03 | 576.57 | 0.0522 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.35 |  | 745.2282 | 0.0163 | 746.6 | 744.3 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.55 |  | 23.2669 | 1.2168 | 23.32 | 22.79 | 0.0849 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 41.765 |  | 41.3392 | 1.0301 | 41.65 | 40.435 | 0.0718 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6534 | 1.4723 | 29.735 | 28.785 | 0.0997 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.35 |  | 745.2282 | 0.0163 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| 2 | IWM | market_regime | 294.05 |  | 293.6889 | 0.123 | 294.51 | 292.72 | 0.0102 | watch_only | none |
| 3 | META | cloud_ai_capex | 648.5 |  | 647.336 | 0.1798 | 655.425 | 643.54 | 0.0802 | watch_only | none |
| 4 | ORCL | cloud_ai_capex | 125.18 |  | 124.9669 | 0.1705 | 126.01 | 122.48 | 0.1358 | watch_only | none |
| 5 | IREN | high_beta_ai_infrastructure | 41.765 |  | 41.3392 | 1.0301 | 41.65 | 40.435 | 0.0718 | buy_precheck_manual_confirm | none |
| 6 | ARM | ai_accelerator | 281.26 |  | 279.8483 | 0.5044 | 286.39 | 275.86 | 0.2667 | watch_only | none |
| 7 | ANET | ai_networking_optical | 174.835 |  | 174.8326 | 0.0014 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | CORZ | high_beta_ai_infrastructure | 23.55 |  | 23.2669 | 1.2168 | 23.32 | 22.79 | 0.0849 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6534 | 1.4723 | 29.735 | 28.785 | 0.0997 | buy_precheck_manual_confirm | none |
| 10 | ENTG | semiconductor_materials | 140.39 |  | 140.3766 | 0.0095 | 142.09 | 139.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | APD | industrial_gases | 298.56 |  | 298.5353 | 0.0083 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TER | semiconductor_test_packaging | 364.59 |  | 362.8697 | 0.4741 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SKHY | memory_hbm_storage | 163.92 |  | 163.8565 | 0.0388 | 165.88 | 160.77 | 1.7082 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AAPL | mega_cap_platform | 324.195 |  | 323.8097 | 0.119 | 325.59 | 322.63 | 0.3609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CRWV | gpu_cloud_ai_factory | 76.69 |  | 76.1976 | 0.6462 | 76.615 | 74.55 | 2.5427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 925.945 |  | 934.3895 | -0.9037 | 944.99 | 923 | 0.1134 | below_vwap | below_vwap |
| 17 | AMAT | semiconductor_equipment | 558.16 |  | 560.0177 | -0.3317 | 564.91 | 552.71 | 0.1165 | below_vwap | below_vwap |
| 18 | ETN | data_center_power_cooling | 404.53 |  | 405.9223 | -0.343 | 411.01 | 404.21 | 0.1162 | below_vwap | below_vwap |
| 19 | AMZN | cloud_ai_capex | 247.57 |  | 247.8491 | -0.1126 | 248.915 | 247.32 | 0.0444 | below_vwap | below_vwap |
| 20 | GOOGL | cloud_ai_capex | 349.49 |  | 349.5026 | -0.0036 | 350.985 | 347.69 | 0.123 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.55 |  | 23.2669 | 1.2168 | 23.32 | 22.79 | 0.0849 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 41.765 |  | 41.3392 | 1.0301 | 41.65 | 40.435 | 0.0718 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6534 | 1.4723 | 29.735 | 28.785 | 0.0997 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 745.35 |  | 745.2282 | 0.0163 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| 5 | AAOI | ai_networking_optical | 110.74 |  | 109.7058 | 0.9427 | 109.39 | 107.58 | 4.8402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | IWM | market_regime | 294.05 |  | 293.6889 | 0.123 | 294.51 | 292.72 | 0.0102 | watch_only | none |
| 7 | CRWV | gpu_cloud_ai_factory | 76.69 |  | 76.1976 | 0.6462 | 76.615 | 74.55 | 2.5427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | META | cloud_ai_capex | 648.5 |  | 647.336 | 0.1798 | 655.425 | 643.54 | 0.0802 | watch_only | none |
| 9 | ARM | ai_accelerator | 281.26 |  | 279.8483 | 0.5044 | 286.39 | 275.86 | 0.2667 | watch_only | none |
| 10 | ORCL | cloud_ai_capex | 125.18 |  | 124.9669 | 0.1705 | 126.01 | 122.48 | 0.1358 | watch_only | none |
| 11 | MU | memory_hbm_storage | 925.945 |  | 934.3895 | -0.9037 | 944.99 | 923 | 0.1134 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1793.2 |  | 1797.7897 | -0.2553 | 1804.54 | 1786.51 | 0.5565 | below_vwap | below_vwap,spread_too_wide |
| 13 | LITE | ai_networking_optical | 807.16 |  | 812.8916 | -0.7051 | 823.31 | 800.37 | 0.3048 | below_vwap | below_vwap |
| 14 | CIEN | ai_networking_optical | 400.04 |  | 400.3864 | -0.0865 | 401.91 | 397.18 | 4.3296 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 468.865 |  | 470.9682 | -0.4466 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | AMAT | semiconductor_equipment | 558.16 |  | 560.0177 | -0.3317 | 564.91 | 552.71 | 0.1165 | below_vwap | below_vwap |
| 17 | PWR | data_center_power_cooling | 637.295 |  | 638.8221 | -0.2391 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 404.53 |  | 405.9223 | -0.343 | 411.01 | 404.21 | 0.1162 | below_vwap | below_vwap |
| 19 | KLAC | semiconductor_equipment | 215.46 |  | 216.1341 | -0.3119 | 220.76 | 214.41 | 0.1903 | below_vwap | below_vwap |
| 20 | JCI | data_center_power_cooling | 140.32 |  | 140.4069 | -0.0619 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.85 |  | 704.98 | -0.1603 | 707.09 | 704.52 | 0.0256 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.86 |  | 70.297 | -0.6216 | 70.84 | 70.09 | 0.0286 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.69 |  | 206.6875 | -0.9664 | 208.61 | 206.275 | 0.0244 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.26 |  | 399.3909 | -0.0328 | 401.45 | 396.36 | 0.7664 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 324.195 |  | 323.8097 | 0.119 | 325.59 | 322.63 | 0.3609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 349.49 |  | 349.5026 | -0.0036 | 350.985 | 347.69 | 0.123 | below_vwap | below_vwap |
| AMD | ai_accelerator | 524.7 |  | 529.7783 | -0.9586 | 532.365 | 524.72 | 1.1435 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.595 |  | 416.9824 | -0.5725 | 418.76 | 415.025 | 0.1351 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 542.39 |  | 547.1206 | -0.8646 | 550.77 | 545.11 | 0.1051 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 574.27 |  | 577.2357 | -0.5138 | 582.03 | 576.57 | 0.0522 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.37 |  | 384.0889 | -0.7079 | 390.11 | 382.13 | 1.4684 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 925.945 |  | 934.3895 | -0.9037 | 944.99 | 923 | 0.1134 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 204.775 |  | 206.4601 | -0.8162 | 208.61 | 205.31 | 0.5421 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.815 |  | 402.6766 | -0.4623 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.82 |  | 46.2728 | -0.9786 | 46.685 | 45.835 | 0.1528 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.56 |  | 24.5722 | -0.0496 | 24.77 | 24.34 | 0.0814 | below_vwap | below_vwap |
| SPY | market_regime | 745.35 |  | 745.2282 | 0.0163 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| IWM | market_regime | 294.05 |  | 293.6889 | 0.123 | 294.51 | 292.72 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 125.18 |  | 124.9669 | 0.1705 | 126.01 | 122.48 | 0.1358 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 76.69 |  | 76.1976 | 0.6462 | 76.615 | 74.55 | 2.5427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 297.95 |  | 299.9041 | -0.6516 | 305.09 | 299.13 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 404.53 |  | 405.9223 | -0.343 | 411.01 | 404.21 | 0.1162 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 637.295 |  | 638.8221 | -0.2391 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1091.6 |  | 1111.2208 | -1.7657 | 1140.63 | 1103.815 | 4.3917 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 468.865 |  | 470.9682 | -0.4466 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.32 |  | 140.4069 | -0.0619 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.835 |  | 174.8326 | 0.0014 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 303.84 |  | 304.904 | -0.349 | 309.72 | 302.3 | 4.1107 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 807.16 |  | 812.8916 | -0.7051 | 823.31 | 800.37 | 0.3048 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 400.04 |  | 400.3864 | -0.0865 | 401.91 | 397.18 | 4.3296 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.74 |  | 109.7058 | 0.9427 | 109.39 | 107.58 | 4.8402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 323.06 |  | 326.2412 | -0.9751 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.2 |  | 1797.7897 | -0.2553 | 1804.54 | 1786.51 | 0.5565 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 558.16 |  | 560.0177 | -0.3317 | 564.91 | 552.71 | 0.1165 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 314.78 |  | 319.6439 | -1.5217 | 328.135 | 317.17 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.46 |  | 216.1341 | -0.3119 | 220.76 | 214.41 | 0.1903 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 364.59 |  | 362.8697 | 0.4741 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.5 |  | 293.3038 | -0.615 | 296.68 | 291.43 | 0.789 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.29 |  | 65.3426 | -0.0804 | 66.54 | 65 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.145 |  | 54.2068 | -0.114 | 54.41 | 54.03 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 140.39 |  | 140.3766 | 0.0095 | 142.09 | 139.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 335.89 |  | 337.9128 | -0.5986 | 340.205 | 336.3 | 0.7889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 508.64 |  | 509.4379 | -0.1566 | 512.83 | 507.675 | 0.2222 | below_vwap | below_vwap |
| APD | industrial_gases | 298.56 |  | 298.5353 | 0.0083 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6534 | 1.4723 | 29.735 | 28.785 | 0.0997 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.765 |  | 41.3392 | 1.0301 | 41.65 | 40.435 | 0.0718 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.55 |  | 23.2669 | 1.2168 | 23.32 | 22.79 | 0.0849 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1512.485 |  | 1521.5648 | -0.5967 | 1540.85 | 1490.29 | 1.1068 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 532.32 |  | 533.7616 | -0.2701 | 533.56 | 517.335 | 4.0408 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 863.645 |  | 864.6437 | -0.1155 | 866.73 | 845.78 | 0.3914 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 247.57 |  | 247.8491 | -0.1126 | 248.915 | 247.32 | 0.0444 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.5 |  | 647.336 | 0.1798 | 655.425 | 643.54 | 0.0802 | watch_only | none |
| ARM | ai_accelerator | 281.26 |  | 279.8483 | 0.5044 | 286.39 | 275.86 | 0.2667 | watch_only | none |
| SKHY | memory_hbm_storage | 163.92 |  | 163.8565 | 0.0388 | 165.88 | 160.77 | 1.7082 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
