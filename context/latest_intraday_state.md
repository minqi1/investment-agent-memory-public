# Intraday State

- Generated at: `2026-07-21T22:19:47+08:00`
- Market time ET: `2026-07-21T10:19:48-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'below_opening_15m_low': 7, 'manual_confirm_candidate': 5, 'below_vwap': 18, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 17}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.04 |  | 704.5838 | 0.0647 | 707.09 | 704.52 | 0.0085 | watch_only | none |
| SOXX | semiconductor_index | 545.055 |  | 546.1779 | -0.2056 | 550.77 | 545.11 | 0.0771 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.325 |  | 576.9507 | -0.1085 | 582.03 | 576.57 | 0.0694 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 746.12 |  | 745.244 | 0.1175 | 746.6 | 744.3 | 0.004 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.75 |  | 293.8085 | 0.3204 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.3112 | 0.9816 | 23.32 | 22.79 | 0.1274 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 41.74 |  | 41.4253 | 0.7597 | 41.65 | 40.435 | 0.0719 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.215 |  | 324.1032 | 0.6516 | 325.59 | 322.63 | 0.0858 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.9 |  | 29.7435 | 0.5262 | 29.735 | 28.785 | 0.1003 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.75 |  | 293.8085 | 0.3204 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 41.74 |  | 41.4253 | 0.7597 | 41.65 | 40.435 | 0.0719 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.215 |  | 324.1032 | 0.6516 | 325.59 | 322.63 | 0.0858 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 705.04 |  | 704.5838 | 0.0647 | 707.09 | 704.52 | 0.0085 | watch_only | none |
| 5 | SPY | market_regime | 746.12 |  | 745.244 | 0.1175 | 746.6 | 744.3 | 0.004 | watch_only | none |
| 6 | HPE | ai_server_oem | 46.32 |  | 46.2208 | 0.2146 | 46.685 | 45.835 | 0.0864 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 349.55 |  | 349.5027 | 0.0135 | 350.985 | 347.69 | 0.1001 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 399.77 |  | 399.4545 | 0.079 | 401.45 | 396.36 | 0.0375 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 29.9 |  | 29.7435 | 0.5262 | 29.735 | 28.785 | 0.1003 | buy_precheck_manual_confirm | none |
| 10 | CRWV | gpu_cloud_ai_factory | 76.51 |  | 76.3418 | 0.2203 | 76.615 | 74.55 | 0.1438 | watch_only | none |
| 11 | SMCI | ai_server_oem | 24.695 |  | 24.5739 | 0.4927 | 24.77 | 24.34 | 0.081 | watch_only | none |
| 12 | ANET | ai_networking_optical | 175.05 |  | 174.89 | 0.0915 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.3112 | 0.9816 | 23.32 | 22.79 | 0.1274 | buy_precheck_manual_confirm | none |
| 14 | ETN | data_center_power_cooling | 405.67 |  | 405.5944 | 0.0186 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ALAB | ai_networking_optical | 324.93 |  | 324.3041 | 0.193 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 293 |  | 292.9511 | 0.0167 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | COHU | semiconductor_test_packaging | 54.44 |  | 54.2793 | 0.296 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | APD | industrial_gases | 299.54 |  | 298.7707 | 0.2575 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LITE | ai_networking_optical | 814.51 |  | 811.8603 | 0.3264 | 823.31 | 800.37 | 0.8029 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CIEN | ai_networking_optical | 401.425 |  | 400.5067 | 0.2293 | 401.91 | 397.18 | 4.7157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.75 |  | 293.8085 | 0.3204 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.3112 | 0.9816 | 23.32 | 22.79 | 0.1274 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 41.74 |  | 41.4253 | 0.7597 | 41.65 | 40.435 | 0.0719 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.215 |  | 324.1032 | 0.6516 | 325.59 | 322.63 | 0.0858 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.9 |  | 29.7435 | 0.5262 | 29.735 | 28.785 | 0.1003 | buy_precheck_manual_confirm | none |
| 6 | TER | semiconductor_test_packaging | 366.37 |  | 363.2373 | 0.8624 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | QQQ | market_regime | 705.04 |  | 704.5838 | 0.0647 | 707.09 | 704.52 | 0.0085 | watch_only | none |
| 8 | SPY | market_regime | 746.12 |  | 745.244 | 0.1175 | 746.6 | 744.3 | 0.004 | watch_only | none |
| 9 | AAOI | ai_networking_optical | 111.45 |  | 109.9854 | 1.3317 | 109.39 | 107.58 | 4.1454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | HPE | ai_server_oem | 46.32 |  | 46.2208 | 0.2146 | 46.685 | 45.835 | 0.0864 | watch_only | none |
| 11 | GOOGL | cloud_ai_capex | 349.55 |  | 349.5027 | 0.0135 | 350.985 | 347.69 | 0.1001 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 399.77 |  | 399.4545 | 0.079 | 401.45 | 396.36 | 0.0375 | watch_only | none |
| 13 | SMCI | ai_server_oem | 24.695 |  | 24.5739 | 0.4927 | 24.77 | 24.34 | 0.081 | watch_only | none |
| 14 | CRWV | gpu_cloud_ai_factory | 76.51 |  | 76.3418 | 0.2203 | 76.615 | 74.55 | 0.1438 | watch_only | none |
| 15 | TQQQ | leveraged_tool | 70.24 |  | 70.2311 | 0.0127 | 70.84 | 70.09 | 0.0142 | watch_only | none |
| 16 | TSM | foundry | 415.29 |  | 416.4159 | -0.2704 | 418.76 | 415.025 | 0.0433 | below_vwap | below_vwap |
| 17 | AVGO | custom_silicon_networking | 383.78 |  | 383.8303 | -0.0131 | 390.11 | 382.13 | 0.1668 | below_vwap | below_vwap |
| 18 | AMD | ai_accelerator | 528.19 |  | 529.2878 | -0.2074 | 532.365 | 524.72 | 1.0129 | below_vwap | below_vwap,spread_too_wide |
| 19 | MU | memory_hbm_storage | 924.11 |  | 931.5616 | -0.7999 | 944.99 | 923 | 0.1991 | below_vwap | below_vwap |
| 20 | ASML | semiconductor_equipment | 1794.275 |  | 1796.6586 | -0.1327 | 1804.54 | 1786.51 | 0.8321 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.04 |  | 704.5838 | 0.0647 | 707.09 | 704.52 | 0.0085 | watch_only | none |
| TQQQ | leveraged_tool | 70.24 |  | 70.2311 | 0.0127 | 70.84 | 70.09 | 0.0142 | watch_only | none |
| NVDA | ai_accelerator | 205.09 |  | 206.3714 | -0.6209 | 208.61 | 206.275 | 0.863 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 399.77 |  | 399.4545 | 0.079 | 401.45 | 396.36 | 0.0375 | watch_only | none |
| AAPL | mega_cap_platform | 326.215 |  | 324.1032 | 0.6516 | 325.59 | 322.63 | 0.0858 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.55 |  | 349.5027 | 0.0135 | 350.985 | 347.69 | 0.1001 | watch_only | none |
| AMD | ai_accelerator | 528.19 |  | 529.2878 | -0.2074 | 532.365 | 524.72 | 1.0129 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.29 |  | 416.4159 | -0.2704 | 418.76 | 415.025 | 0.0433 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.055 |  | 546.1779 | -0.2056 | 550.77 | 545.11 | 0.0771 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.325 |  | 576.9507 | -0.1085 | 582.03 | 576.57 | 0.0694 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 383.78 |  | 383.8303 | -0.0131 | 390.11 | 382.13 | 0.1668 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 924.11 |  | 931.5616 | -0.7999 | 944.99 | 923 | 0.1991 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 205.51 |  | 206.1498 | -0.3104 | 208.61 | 205.31 | 0.4623 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.34 |  | 402.5139 | -0.2916 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.32 |  | 46.2208 | 0.2146 | 46.685 | 45.835 | 0.0864 | watch_only | none |
| SMCI | ai_server_oem | 24.695 |  | 24.5739 | 0.4927 | 24.77 | 24.34 | 0.081 | watch_only | none |
| SPY | market_regime | 746.12 |  | 745.244 | 0.1175 | 746.6 | 744.3 | 0.004 | watch_only | none |
| IWM | market_regime | 294.75 |  | 293.8085 | 0.3204 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.22 |  | 124.976 | 0.1953 | 126.01 | 122.48 | 1.2139 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 76.51 |  | 76.3418 | 0.2203 | 76.615 | 74.55 | 0.1438 | watch_only | none |
| VRT | data_center_power_cooling | 299.45 |  | 299.6684 | -0.0729 | 305.09 | 299.13 | 2.6716 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 405.67 |  | 405.5944 | 0.0186 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 633.34 |  | 637.3029 | -0.6218 | 645.815 | 635.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1084.41 |  | 1105.7652 | -1.9313 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 467.625 |  | 469.6161 | -0.424 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.2 |  | 140.3013 | -0.0722 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.05 |  | 174.89 | 0.0915 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 306.42 |  | 304.8593 | 0.512 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 814.51 |  | 811.8603 | 0.3264 | 823.31 | 800.37 | 0.8029 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 401.425 |  | 400.5067 | 0.2293 | 401.91 | 397.18 | 4.7157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 111.45 |  | 109.9854 | 1.3317 | 109.39 | 107.58 | 4.1454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 324.93 |  | 324.3041 | 0.193 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1794.275 |  | 1796.6586 | -0.1327 | 1804.54 | 1786.51 | 0.8321 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 564.27 |  | 559.992 | 0.7639 | 564.91 | 552.71 | 0.7319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 315.22 |  | 318.2571 | -0.9543 | 328.135 | 317.17 | 4.4604 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 216.15 |  | 215.8593 | 0.1347 | 220.76 | 214.41 | 0.7911 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 366.37 |  | 363.2373 | 0.8624 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 293 |  | 292.9511 | 0.0167 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.36 |  | 65.2566 | 0.1585 | 66.54 | 65 | 4.3911 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.2793 | 0.296 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 140.15 |  | 140.2104 | -0.0431 | 142.09 | 139.41 | 4.1741 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 336.76 |  | 337.7018 | -0.2789 | 340.205 | 336.3 | 0.4009 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 507.89 |  | 509.397 | -0.2958 | 512.83 | 507.675 | 1.0672 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 299.54 |  | 298.7707 | 0.2575 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.9 |  | 29.7435 | 0.5262 | 29.735 | 28.785 | 0.1003 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.74 |  | 41.4253 | 0.7597 | 41.65 | 40.435 | 0.0719 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.54 |  | 23.3112 | 0.9816 | 23.32 | 22.79 | 0.1274 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1504.59 |  | 1518.4381 | -0.912 | 1540.85 | 1490.29 | 1.5014 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 532.66 |  | 532.9779 | -0.0596 | 533.56 | 517.335 | 0.6101 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 863.01 |  | 864.0344 | -0.1186 | 866.73 | 845.78 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 247.275 |  | 247.7114 | -0.1762 | 248.915 | 247.32 | 0.0243 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 646.105 |  | 647.3047 | -0.1853 | 655.425 | 643.54 | 4.0752 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.605 |  | 281.5597 | 1.4367 | 286.39 | 275.86 | 3.1057 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 163.85 |  | 163.6042 | 0.1503 | 165.88 | 160.77 | 2.4413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
