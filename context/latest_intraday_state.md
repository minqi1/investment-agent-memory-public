# Intraday State

- Generated at: `2026-07-21T22:11:58+08:00`
- Market time ET: `2026-07-21T10:11:59-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 18, 'spread_too_wide_or_missing': 9, 'watch_only': 2, 'below_vwap': 23, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 702.93 |  | 704.8045 | -0.266 | 707.09 | 704.52 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 540.59 |  | 546.5369 | -1.0881 | 550.77 | 545.11 | 0.0888 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.14 |  | 577.1106 | -0.8613 | 582.03 | 576.57 | 0.0315 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.19 |  | 745.232 | -0.0056 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.365 |  | 23.2905 | 0.3201 | 23.32 | 22.79 | 0.1284 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 41.82 |  | 41.3921 | 1.0337 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 29.82 |  | 29.7246 | 0.3208 | 29.735 | 28.785 | 0.0335 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.365 |  | 23.2905 | 0.3201 | 23.32 | 22.79 | 0.1284 | buy_precheck_manual_confirm | none |
| 2 | APLD | high_beta_ai_infrastructure | 29.82 |  | 29.7246 | 0.3208 | 29.735 | 28.785 | 0.0335 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 294.34 |  | 293.7325 | 0.2068 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 325.46 |  | 323.9397 | 0.4693 | 325.59 | 322.63 | 0.0615 | watch_only | none |
| 5 | IREN | high_beta_ai_infrastructure | 41.82 |  | 41.3921 | 1.0337 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 647.5 |  | 647.4451 | 0.0085 | 655.425 | 643.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TER | semiconductor_test_packaging | 363.1 |  | 363.087 | 0.0036 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | COHU | semiconductor_test_packaging | 54.355 |  | 54.2629 | 0.1698 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | APD | industrial_gases | 299.575 |  | 298.6299 | 0.3165 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | CIEN | ai_networking_optical | 400.965 |  | 400.4097 | 0.1387 | 401.91 | 397.18 | 4.8683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | MSFT | cloud_ai_capex | 400.14 |  | 399.4199 | 0.1803 | 401.45 | 396.36 | 0.4998 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | CRWV | gpu_cloud_ai_factory | 76.83 |  | 76.2903 | 0.7074 | 76.615 | 74.55 | 2.5381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ARM | ai_accelerator | 282.22 |  | 280.851 | 0.4874 | 286.39 | 275.86 | 0.8681 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SPY | market_regime | 745.19 |  | 745.232 | -0.0056 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| 15 | HPE | ai_server_oem | 46.08 |  | 46.2207 | -0.3044 | 46.685 | 45.835 | 0.1302 | below_vwap | below_vwap |
| 16 | GOOGL | cloud_ai_capex | 349.46 |  | 349.5336 | -0.0211 | 350.985 | 347.69 | 0.0401 | below_vwap | below_vwap |
| 17 | LIN | industrial_gases | 509.17 |  | 509.431 | -0.0512 | 512.83 | 507.675 | 0.108 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | SMCI | ai_server_oem | 24.555 |  | 24.57 | -0.0611 | 24.77 | 24.34 | 0.0814 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 174.79 |  | 174.872 | -0.0469 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.365 |  | 23.2905 | 0.3201 | 23.32 | 22.79 | 0.1284 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 41.82 |  | 41.3921 | 1.0337 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 29.82 |  | 29.7246 | 0.3208 | 29.735 | 28.785 | 0.0335 | buy_precheck_manual_confirm | none |
| 4 | AAOI | ai_networking_optical | 111.06 |  | 109.8435 | 1.1075 | 109.39 | 107.58 | 4.394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | IWM | market_regime | 294.34 |  | 293.7325 | 0.2068 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| 6 | CRWV | gpu_cloud_ai_factory | 76.83 |  | 76.2903 | 0.7074 | 76.615 | 74.55 | 2.5381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AAPL | mega_cap_platform | 325.46 |  | 323.9397 | 0.4693 | 325.59 | 322.63 | 0.0615 | watch_only | none |
| 8 | ANET | ai_networking_optical | 174.79 |  | 174.872 | -0.0469 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | SPY | market_regime | 745.19 |  | 745.232 | -0.0056 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| 10 | ASML | semiconductor_equipment | 1787.26 |  | 1797.2884 | -0.558 | 1804.54 | 1786.51 | 0.8997 | below_vwap | below_vwap,spread_too_wide |
| 11 | LITE | ai_networking_optical | 804.93 |  | 812.1003 | -0.8829 | 823.31 | 800.37 | 0.8696 | below_vwap | below_vwap,spread_too_wide |
| 12 | TT | data_center_power_cooling | 467.97 |  | 470.0063 | -0.4332 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AMAT | semiconductor_equipment | 558.21 |  | 559.8369 | -0.2906 | 564.91 | 552.71 | 1.1071 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 404.38 |  | 405.6186 | -0.3053 | 411.01 | 404.21 | 5.1091 | below_vwap | below_vwap,spread_too_wide |
| 15 | KLAC | semiconductor_equipment | 214.59 |  | 215.9789 | -0.6431 | 220.76 | 214.41 | 2.8286 | below_vwap | below_vwap,spread_too_wide |
| 16 | JCI | data_center_power_cooling | 140.175 |  | 140.3419 | -0.1189 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | DELL | ai_server_oem | 400.07 |  | 402.6315 | -0.6362 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | STX | memory_hbm_storage | 855.99 |  | 864.1648 | -0.946 | 866.73 | 845.78 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | HPE | ai_server_oem | 46.08 |  | 46.2207 | -0.3044 | 46.685 | 45.835 | 0.1302 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 702.93 |  | 704.8045 | -0.266 | 707.09 | 704.52 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.65 |  | 70.2627 | -0.872 | 70.84 | 70.09 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.25 |  | 206.5426 | -1.11 | 208.61 | 206.275 | 0.798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 400.14 |  | 399.4199 | 0.1803 | 401.45 | 396.36 | 0.4998 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 325.46 |  | 323.9397 | 0.4693 | 325.59 | 322.63 | 0.0615 | watch_only | none |
| GOOGL | cloud_ai_capex | 349.46 |  | 349.5336 | -0.0211 | 350.985 | 347.69 | 0.0401 | below_vwap | below_vwap |
| AMD | ai_accelerator | 523.61 |  | 529.4777 | -1.1082 | 532.365 | 524.72 | 1.7876 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.09 |  | 416.6251 | -0.6085 | 418.76 | 415.025 | 0.0869 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 540.59 |  | 546.5369 | -1.0881 | 550.77 | 545.11 | 0.0888 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.14 |  | 577.1106 | -0.8613 | 582.03 | 576.57 | 0.0315 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.17 |  | 383.9679 | -0.7287 | 390.11 | 382.13 | 1.4692 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 919.14 |  | 933.2302 | -1.5098 | 944.99 | 923 | 1.4383 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 203.135 |  | 206.2544 | -1.5124 | 208.61 | 205.31 | 1.2701 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.07 |  | 402.6315 | -0.6362 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.08 |  | 46.2207 | -0.3044 | 46.685 | 45.835 | 0.1302 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.555 |  | 24.57 | -0.0611 | 24.77 | 24.34 | 0.0814 | below_vwap | below_vwap |
| SPY | market_regime | 745.19 |  | 745.232 | -0.0056 | 746.6 | 744.3 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 294.34 |  | 293.7325 | 0.2068 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| ORCL | cloud_ai_capex | 124.9 |  | 124.97 | -0.056 | 126.01 | 122.48 | 0.1761 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 76.83 |  | 76.2903 | 0.7074 | 76.615 | 74.55 | 2.5381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 298.72 |  | 299.7471 | -0.3427 | 305.09 | 299.13 | 0.626 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 404.38 |  | 405.6186 | -0.3053 | 411.01 | 404.21 | 5.1091 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 635.1 |  | 637.6777 | -0.4042 | 645.815 | 635.91 | 0.2976 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1089.78 |  | 1108.5915 | -1.6969 | 1140.63 | 1103.815 | 3.8485 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 467.97 |  | 470.0063 | -0.4332 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.175 |  | 140.3419 | -0.1189 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.79 |  | 174.872 | -0.0469 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 304.24 |  | 304.8354 | -0.1953 | 309.72 | 302.3 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 804.93 |  | 812.1003 | -0.8829 | 823.31 | 800.37 | 0.8696 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 400.965 |  | 400.4097 | 0.1387 | 401.91 | 397.18 | 4.8683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 111.06 |  | 109.8435 | 1.1075 | 109.39 | 107.58 | 4.394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 320.79 |  | 324.3113 | -1.0858 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1787.26 |  | 1797.2884 | -0.558 | 1804.54 | 1786.51 | 0.8997 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 558.21 |  | 559.8369 | -0.2906 | 564.91 | 552.71 | 1.1071 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 313.85 |  | 318.6465 | -1.5053 | 328.135 | 317.17 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.59 |  | 215.9789 | -0.6431 | 220.76 | 214.41 | 2.8286 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 363.1 |  | 363.087 | 0.0036 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.36 |  | 293.0832 | -0.5879 | 296.68 | 291.36 | 1.8465 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.78 |  | 65.2975 | -0.7925 | 66.54 | 65 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.355 |  | 54.2629 | 0.1698 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.41 |  | 140.3066 | -0.639 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.045 |  | 337.8056 | -0.8172 | 340.205 | 336.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 509.17 |  | 509.431 | -0.0512 | 512.83 | 507.675 | 0.108 | below_vwap | below_vwap |
| APD | industrial_gases | 299.575 |  | 298.6299 | 0.3165 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.82 |  | 29.7246 | 0.3208 | 29.735 | 28.785 | 0.0335 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.82 |  | 41.3921 | 1.0337 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.365 |  | 23.2905 | 0.3201 | 23.32 | 22.79 | 0.1284 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1493.07 |  | 1520.3805 | -1.7963 | 1540.85 | 1490.29 | 1.6088 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 527.59 |  | 533.1823 | -1.0489 | 533.56 | 517.335 | 1.3306 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 855.99 |  | 864.1648 | -0.946 | 866.73 | 845.78 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 247.27 |  | 247.7783 | -0.2052 | 248.915 | 247.32 | 0.0121 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 647.5 |  | 647.4451 | 0.0085 | 655.425 | 643.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ARM | ai_accelerator | 282.22 |  | 280.851 | 0.4874 | 286.39 | 275.86 | 0.8681 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 161.905 |  | 163.6961 | -1.0942 | 165.88 | 160.77 | 1.2353 | below_vwap | below_vwap,spread_too_wide |
