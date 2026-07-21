# Intraday State

- Generated at: `2026-07-21T23:00:58+08:00`
- Market time ET: `2026-07-21T11:01:00-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 9, 'manual_confirm_candidate': 11, 'below_opening_15m_low': 3, 'below_vwap': 10, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.92 |  | 705.0739 | 0.2618 | 707.09 | 704.52 | 0.0552 | watch_only | none |
| SOXX | semiconductor_index | 547.86 |  | 546.3442 | 0.2774 | 550.77 | 545.11 | 0.0602 | watch_only | none |
| SMH | semiconductor_index | 579.2 |  | 577.2611 | 0.3359 | 582.03 | 576.57 | 0.0501 | watch_only | none |
| SPY | market_regime | 746.77 |  | 745.6568 | 0.1493 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.77 |  | 745.6568 | 0.1493 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 945.57 |  | 932.8034 | 1.3686 | 944.99 | 923 | 0.0899 | buy_precheck_manual_confirm | none |
| 3 | LITE | ai_networking_optical | 826.86 |  | 817.1413 | 1.1894 | 823.31 | 800.37 | 0.1911 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.6 |  | 294.045 | 0.1888 | 294.51 | 292.72 | 0.0136 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 23.87 |  | 23.5386 | 1.4077 | 23.32 | 22.79 | 0.0419 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 41.82 |  | 41.5597 | 0.6262 | 41.65 | 40.435 | 0.0478 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 327.105 |  | 324.6237 | 0.7644 | 325.59 | 322.63 | 0.0764 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.815 |  | 24.6385 | 0.7164 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 77.02 |  | 76.6626 | 0.4662 | 76.615 | 74.55 | 0.0909 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.91 |  | 29.7953 | 0.3848 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 70.84 |  | 70.3422 | 0.7077 | 70.84 | 70.09 | 0.0282 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.77 |  | 745.6568 | 0.1493 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.6 |  | 294.045 | 0.1888 | 294.51 | 292.72 | 0.0136 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 579.2 |  | 577.2611 | 0.3359 | 582.03 | 576.57 | 0.0501 | watch_only | none |
| 4 | SOXX | semiconductor_index | 547.86 |  | 546.3442 | 0.2774 | 550.77 | 545.11 | 0.0602 | watch_only | none |
| 5 | QQQ | market_regime | 706.92 |  | 705.0739 | 0.2618 | 707.09 | 704.52 | 0.0552 | watch_only | none |
| 6 | SMCI | ai_server_oem | 24.815 |  | 24.6385 | 0.7164 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 7 | IREN | high_beta_ai_infrastructure | 41.82 |  | 41.5597 | 0.6262 | 41.65 | 40.435 | 0.0478 | buy_precheck_manual_confirm | none |
| 8 | AAPL | mega_cap_platform | 327.105 |  | 324.6237 | 0.7644 | 325.59 | 322.63 | 0.0764 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 77.02 |  | 76.6626 | 0.4662 | 76.615 | 74.55 | 0.0909 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.91 |  | 29.7953 | 0.3848 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| 11 | MRVL | custom_silicon_networking | 206.74 |  | 206.1361 | 0.293 | 208.61 | 205.31 | 0.1645 | watch_only | none |
| 12 | ETN | data_center_power_cooling | 405.69 |  | 405.6293 | 0.015 | 411.01 | 404.21 | 0.1578 | watch_only | none |
| 13 | MU | memory_hbm_storage | 945.57 |  | 932.8034 | 1.3686 | 944.99 | 923 | 0.0899 | buy_precheck_manual_confirm | none |
| 14 | HPE | ai_server_oem | 46.55 |  | 46.2882 | 0.5657 | 46.685 | 45.835 | 0.1074 | watch_only | none |
| 15 | AMKR | semiconductor_test_packaging | 65.85 |  | 65.4198 | 0.6577 | 66.54 | 65 | 0.1215 | watch_only | none |
| 16 | AMAT | semiconductor_equipment | 564.14 |  | 561.5116 | 0.4681 | 564.91 | 552.71 | 0.2765 | watch_only | none |
| 17 | LITE | ai_networking_optical | 826.86 |  | 817.1413 | 1.1894 | 823.31 | 800.37 | 0.1911 | buy_precheck_manual_confirm | none |
| 18 | COHU | semiconductor_test_packaging | 54.745 |  | 54.6285 | 0.2133 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ANET | ai_networking_optical | 176.24 |  | 175.1988 | 0.5943 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 23.87 |  | 23.5386 | 1.4077 | 23.32 | 22.79 | 0.0419 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.77 |  | 745.6568 | 0.1493 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 945.57 |  | 932.8034 | 1.3686 | 944.99 | 923 | 0.0899 | buy_precheck_manual_confirm | none |
| 3 | LITE | ai_networking_optical | 826.86 |  | 817.1413 | 1.1894 | 823.31 | 800.37 | 0.1911 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.6 |  | 294.045 | 0.1888 | 294.51 | 292.72 | 0.0136 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 23.87 |  | 23.5386 | 1.4077 | 23.32 | 22.79 | 0.0419 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 41.82 |  | 41.5597 | 0.6262 | 41.65 | 40.435 | 0.0478 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 327.105 |  | 324.6237 | 0.7644 | 325.59 | 322.63 | 0.0764 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.815 |  | 24.6385 | 0.7164 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 77.02 |  | 76.6626 | 0.4662 | 76.615 | 74.55 | 0.0909 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.91 |  | 29.7953 | 0.3848 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 70.84 |  | 70.3422 | 0.7077 | 70.84 | 70.09 | 0.0282 | buy_precheck_manual_confirm | none |
| 12 | ANET | ai_networking_optical | 176.24 |  | 175.1988 | 0.5943 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 419.06 |  | 416.9579 | 0.5042 | 418.76 | 415.025 | 0.8972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ASML | semiconductor_equipment | 1806.71 |  | 1798.6188 | 0.4499 | 1804.54 | 1786.51 | 0.4256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 407.14 |  | 402.5307 | 1.1451 | 401.91 | 397.18 | 5.0548 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 879.04 |  | 865.745 | 1.5357 | 866.73 | 845.78 | 1.918 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ARM | ai_accelerator | 286.63 |  | 283.6534 | 1.0494 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 545.395 |  | 535.1183 | 1.9204 | 533.56 | 517.335 | 1.4155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 371.815 |  | 365.9823 | 1.5937 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SMH | semiconductor_index | 579.2 |  | 577.2611 | 0.3359 | 582.03 | 576.57 | 0.0501 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.92 |  | 705.0739 | 0.2618 | 707.09 | 704.52 | 0.0552 | watch_only | none |
| TQQQ | leveraged_tool | 70.84 |  | 70.3422 | 0.7077 | 70.84 | 70.09 | 0.0282 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.84 |  | 206.1062 | -0.1291 | 208.61 | 206.275 | 0.0243 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.295 |  | 399.7249 | -0.1076 | 401.45 | 396.36 | 0.0351 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.105 |  | 324.6237 | 0.7644 | 325.59 | 322.63 | 0.0764 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.9 |  | 349.3463 | -0.1277 | 350.985 | 347.69 | 1.0891 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 528.6 |  | 529.5036 | -0.1707 | 532.365 | 524.72 | 0.8343 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 419.06 |  | 416.9579 | 0.5042 | 418.76 | 415.025 | 0.8972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.86 |  | 546.3442 | 0.2774 | 550.77 | 545.11 | 0.0602 | watch_only | none |
| SMH | semiconductor_index | 579.2 |  | 577.2611 | 0.3359 | 582.03 | 576.57 | 0.0501 | watch_only | none |
| AVGO | custom_silicon_networking | 384.05 |  | 383.8808 | 0.0441 | 390.11 | 382.13 | 0.651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 945.57 |  | 932.8034 | 1.3686 | 944.99 | 923 | 0.0899 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 206.74 |  | 206.1361 | 0.293 | 208.61 | 205.31 | 0.1645 | watch_only | none |
| DELL | ai_server_oem | 403.54 |  | 402.4136 | 0.2799 | 405.78 | 397.185 | 1.3629 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.55 |  | 46.2882 | 0.5657 | 46.685 | 45.835 | 0.1074 | watch_only | none |
| SMCI | ai_server_oem | 24.815 |  | 24.6385 | 0.7164 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.77 |  | 745.6568 | 0.1493 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.6 |  | 294.045 | 0.1888 | 294.51 | 292.72 | 0.0136 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 124.955 |  | 125.0281 | -0.0584 | 126.01 | 122.48 | 0.048 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 77.02 |  | 76.6626 | 0.4662 | 76.615 | 74.55 | 0.0909 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 301.91 |  | 300.0088 | 0.6337 | 305.09 | 299.13 | 0.4306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.69 |  | 405.6293 | 0.015 | 411.01 | 404.21 | 0.1578 | watch_only | none |
| PWR | data_center_power_cooling | 634.755 |  | 636.712 | -0.3074 | 645.815 | 635.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1086.61 |  | 1101.6291 | -1.3634 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 468.515 |  | 469.0718 | -0.1187 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 141.12 |  | 140.4942 | 0.4455 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.24 |  | 175.1988 | 0.5943 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 310.255 |  | 306.3097 | 1.288 | 309.72 | 302.3 | 4.5221 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 826.86 |  | 817.1413 | 1.1894 | 823.31 | 800.37 | 0.1911 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 407.14 |  | 402.5307 | 1.1451 | 401.91 | 397.18 | 5.0548 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 114.22 |  | 111.6574 | 2.2951 | 109.39 | 107.58 | 3.6596 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 326.15 |  | 324.7932 | 0.4178 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.71 |  | 1798.6188 | 0.4499 | 1804.54 | 1786.51 | 0.4256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 564.14 |  | 561.5116 | 0.4681 | 564.91 | 552.71 | 0.2765 | watch_only | none |
| LRCX | semiconductor_equipment | 319.74 |  | 318.452 | 0.4044 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.48 |  | 215.8028 | -0.1496 | 220.76 | 214.41 | 0.1021 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 371.815 |  | 365.9823 | 1.5937 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.27 |  | 293.3956 | 0.9797 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.85 |  | 65.4198 | 0.6577 | 66.54 | 65 | 0.1215 | watch_only | none |
| COHU | semiconductor_test_packaging | 54.745 |  | 54.6285 | 0.2133 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 140.31 |  | 140.1084 | 0.1439 | 142.09 | 139.41 | 4.0981 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 338.97 |  | 337.7314 | 0.3667 | 340.205 | 336.3 | 4.0328 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 508.515 |  | 509.0695 | -0.1089 | 512.83 | 507.675 | 0.9479 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 298.86 |  | 299.3753 | -0.1721 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.91 |  | 29.7953 | 0.3848 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.82 |  | 41.5597 | 0.6262 | 41.65 | 40.435 | 0.0478 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.87 |  | 23.5386 | 1.4077 | 23.32 | 22.79 | 0.0419 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1540.61 |  | 1520.4243 | 1.3276 | 1540.85 | 1490.29 | 0.2512 | watch_only | none |
| WDC | memory_hbm_storage | 545.395 |  | 535.1183 | 1.9204 | 533.56 | 517.335 | 1.4155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 879.04 |  | 865.745 | 1.5357 | 866.73 | 845.78 | 1.918 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.71 |  | 247.7481 | -0.0154 | 248.915 | 247.32 | 0.0283 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.475 |  | 647.3737 | 0.0157 | 655.425 | 643.54 | 1.0888 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 286.63 |  | 283.6534 | 1.0494 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 166.38 |  | 164.1433 | 1.3627 | 165.88 | 160.77 | 3.3538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
