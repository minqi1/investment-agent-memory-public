# Intraday State

- Generated at: `2026-07-21T02:42:37+08:00`
- Market time ET: `2026-07-20T14:42:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 30, 'manual_confirm_candidate': 2, 'below_vwap': 18, 'spread_too_wide_or_missing': 3, 'price_stale_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.39 |  | 701.5083 | -0.4445 | 705.51 | 701.82 | 0.0086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.11 |  | 532.6091 | -0.8447 | 538.59 | 532.55 | 0.0738 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 561.56 |  | 566.0683 | -0.7964 | 572.46 | 567.02 | 0.0748 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 743.3 |  | 745.4015 | -0.2819 | 748.69 | 746.87 | 0.0081 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.18 |  | 397.0184 | 1.0482 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.525 |  | 39.6423 | 2.2266 | 39.16 | 36.335 | 0.0494 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 24.31 |  | 24.1789 | 0.5423 | 24.51 | 24.22 | 0.0411 | watch_only | none |
| 2 | MSFT | cloud_ai_capex | 401.18 |  | 397.0184 | 1.0482 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.61 |  | 296.5414 | 0.0231 | 296.26 | 293.84 | 5.047 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | META | cloud_ai_capex | 647.785 |  | 646.2896 | 0.2314 | 646.57 | 638.875 | 1.5113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AMD | ai_accelerator | 514.79 |  | 514.3177 | 0.0918 | 522.26 | 510.97 | 4.0793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | IREN | high_beta_ai_infrastructure | 40.525 |  | 39.6423 | 2.2266 | 39.16 | 36.335 | 0.0494 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 249.87 |  | 250.5325 | -0.2644 | 250.2 | 248.195 | 0.016 | below_vwap | below_vwap |
| 8 | HPE | ai_server_oem | 45.37 |  | 45.6163 | -0.5398 | 46.21 | 45.305 | 0.0441 | below_vwap | below_vwap |
| 9 | GOOGL | cloud_ai_capex | 351.14 |  | 355.9939 | -1.3635 | 358.795 | 350.875 | 0.0199 | below_vwap | below_vwap |
| 10 | ANET | ai_networking_optical | 169.965 |  | 170.8464 | -0.5159 | 171.39 | 168.79 | 0.1589 | below_vwap | below_vwap |
| 11 | TT | data_center_power_cooling | 466.95 |  | 466.3934 | 0.1193 | 477.865 | 468.805 | 4.6215 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1078.59 |  | 1077.6571 | 0.0866 | 1103.11 | 1081.14 | 4.2648 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 14 | CORZ | high_beta_ai_infrastructure | 22.195 |  | 22.3432 | -0.6633 | 22.565 | 21.85 | 0.1352 | below_vwap | below_vwap |
| 15 | APLD | high_beta_ai_infrastructure | 27.76 |  | 27.872 | -0.402 | 28.39 | 27.11 | 0.1081 | below_vwap | below_vwap |
| 16 | TER | semiconductor_test_packaging | 336.13 |  | 341.105 | -1.4585 | 349.43 | 335.335 | 0.2053 | below_vwap | below_vwap |
| 17 | SNDK | memory_hbm_storage | 1405.76 |  | 1424.7021 | -1.3295 | 1449.57 | 1394.24 | 0.2867 | below_vwap | below_vwap |
| 18 | LIN | industrial_gases | 511.97 |  | 513.3482 | -0.2685 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ALAB | ai_networking_optical | 310.085 |  | 314.0685 | -1.2683 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 379.56 |  | 380.4875 | -0.2438 | 382.67 | 377.47 | 0.4084 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.18 |  | 397.0184 | 1.0482 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.525 |  | 39.6423 | 2.2266 | 39.16 | 36.335 | 0.0494 | buy_precheck_manual_confirm | none |
| 3 | MRVL | custom_silicon_networking | 197.095 |  | 197.4055 | -0.1573 | 196.86 | 192.09 | 3.9778 | below_vwap | below_vwap,spread_too_wide |
| 4 | APD | industrial_gases | 296.61 |  | 296.5414 | 0.0231 | 296.26 | 293.84 | 5.047 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | META | cloud_ai_capex | 647.785 |  | 646.2896 | 0.2314 | 646.57 | 638.875 | 1.5113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SMCI | ai_server_oem | 24.31 |  | 24.1789 | 0.5423 | 24.51 | 24.22 | 0.0411 | watch_only | none |
| 7 | ANET | ai_networking_optical | 169.965 |  | 170.8464 | -0.5159 | 171.39 | 168.79 | 0.1589 | below_vwap | below_vwap |
| 8 | AVGO | custom_silicon_networking | 379.56 |  | 380.4875 | -0.2438 | 382.67 | 377.47 | 0.4084 | below_vwap | below_vwap,spread_too_wide |
| 9 | AMZN | cloud_ai_capex | 249.87 |  | 250.5325 | -0.2644 | 250.2 | 248.195 | 0.016 | below_vwap | below_vwap |
| 10 | WDC | memory_hbm_storage | 491.925 |  | 499.4849 | -1.5135 | 504.53 | 490.68 | 2.846 | below_vwap | below_vwap,spread_too_wide |
| 11 | LITE | ai_networking_optical | 775.15 |  | 787.3278 | -1.5467 | 790.59 | 767.2 | 1.3752 | below_vwap | below_vwap,spread_too_wide |
| 12 | CIEN | ai_networking_optical | 381.62 |  | 386.9217 | -1.3702 | 393.855 | 377.005 | 3.59 | below_vwap | below_vwap,spread_too_wide |
| 13 | HPE | ai_server_oem | 45.37 |  | 45.6163 | -0.5398 | 46.21 | 45.305 | 0.0441 | below_vwap | below_vwap |
| 14 | LIN | industrial_gases | 511.97 |  | 513.3482 | -0.2685 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ARM | ai_accelerator | 271.52 |  | 272.4935 | -0.3573 | 277.4 | 271.455 | 1.7678 | below_vwap | below_vwap,spread_too_wide |
| 17 | GOOGL | cloud_ai_capex | 351.14 |  | 355.9939 | -1.3635 | 358.795 | 350.875 | 0.0199 | below_vwap | below_vwap |
| 18 | TER | semiconductor_test_packaging | 336.13 |  | 341.105 | -1.4585 | 349.43 | 335.335 | 0.2053 | below_vwap | below_vwap |
| 19 | COHR | ai_networking_optical | 290.29 |  | 293.6624 | -1.1484 | 296.46 | 286.91 | 2.687 | below_vwap | below_vwap,spread_too_wide |
| 20 | SNDK | memory_hbm_storage | 1405.76 |  | 1424.7021 | -1.3295 | 1449.57 | 1394.24 | 0.2867 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.39 |  | 701.5083 | -0.4445 | 705.51 | 701.82 | 0.0086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 68.38 |  | 69.2566 | -1.2657 | 70.43 | 69.35 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 203.86 |  | 205.5045 | -0.8002 | 207.71 | 205.095 | 0.0294 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.18 |  | 397.0184 | 1.0482 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 326.06 |  | 326.4251 | -0.1119 | 333.63 | 330.03 | 0.1411 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 351.14 |  | 355.9939 | -1.3635 | 358.795 | 350.875 | 0.0199 | below_vwap | below_vwap |
| AMD | ai_accelerator | 514.79 |  | 514.3177 | 0.0918 | 522.26 | 510.97 | 4.0793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 402.11 |  | 404.5385 | -0.6003 | 409.82 | 405.51 | 0.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.11 |  | 532.6091 | -0.8447 | 538.59 | 532.55 | 0.0738 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 561.56 |  | 566.0683 | -0.7964 | 572.46 | 567.02 | 0.0748 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.56 |  | 380.4875 | -0.2438 | 382.67 | 377.47 | 0.4084 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 872.52 |  | 885.3819 | -1.4527 | 898.57 | 878.92 | 0.3988 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 197.095 |  | 197.4055 | -0.1573 | 196.86 | 192.09 | 3.9778 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 387.125 |  | 390.9035 | -0.9666 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.37 |  | 45.6163 | -0.5398 | 46.21 | 45.305 | 0.0441 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.31 |  | 24.1789 | 0.5423 | 24.51 | 24.22 | 0.0411 | watch_only | none |
| SPY | market_regime | 743.3 |  | 745.4015 | -0.2819 | 748.69 | 746.87 | 0.0081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 293.36 |  | 294.0485 | -0.2341 | 295.97 | 294.88 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 123.45 |  | 122.3916 | 0.8647 | 125.41 | 123.57 | 2.5192 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.355 |  | 76.2844 | -2.5292 | 79.23 | 75.17 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 293.89 |  | 295.9672 | -0.7018 | 300.96 | 297.175 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 402.025 |  | 403.7622 | -0.4303 | 413.44 | 406.66 | 4.8853 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 635.06 |  | 637.3086 | -0.3528 | 644.7 | 636.38 | 3.7839 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1078.59 |  | 1077.6571 | 0.0866 | 1103.11 | 1081.14 | 4.2648 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 466.95 |  | 466.3934 | 0.1193 | 477.865 | 468.805 | 4.6215 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 139.82 |  | 140.4451 | -0.4451 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.965 |  | 170.8464 | -0.5159 | 171.39 | 168.79 | 0.1589 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 290.29 |  | 293.6624 | -1.1484 | 296.46 | 286.91 | 2.687 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 775.15 |  | 787.3278 | -1.5467 | 790.59 | 767.2 | 1.3752 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 381.62 |  | 386.9217 | -1.3702 | 393.855 | 377.005 | 3.59 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 103.24 |  | 105.0007 | -1.6768 | 107.28 | 104.215 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 310.085 |  | 314.0685 | -1.2683 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1736.585 |  | 1753.8263 | -0.9831 | 1797.04 | 1768.805 | 0.114 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 527.72 |  | 536.3853 | -1.6155 | 554.8 | 543 | 0.1933 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 306.91 |  | 312.0972 | -1.6621 | 324.32 | 319.39 | 0.0977 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 209.035 |  | 211.8619 | -1.3343 | 220.28 | 216.62 | 2.0571 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 336.13 |  | 341.105 | -1.4585 | 349.43 | 335.335 | 0.2053 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 280.44 |  | 281.8838 | -0.5122 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.6 |  | 63.425 | -1.3008 | 64.96 | 63.98 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.44 |  | 51.5762 | -0.2641 | 52.74 | 50.72 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.975 |  | 137.5355 | -1.1346 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 325.19 |  | 329.3291 | -1.2568 | 338.1 | 328.505 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 511.97 |  | 513.3482 | -0.2685 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.61 |  | 296.5414 | 0.0231 | 296.26 | 293.84 | 5.047 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 27.76 |  | 27.872 | -0.402 | 28.39 | 27.11 | 0.1081 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.525 |  | 39.6423 | 2.2266 | 39.16 | 36.335 | 0.0494 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.195 |  | 22.3432 | -0.6633 | 22.565 | 21.85 | 0.1352 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1405.76 |  | 1424.7021 | -1.3295 | 1449.57 | 1394.24 | 0.2867 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 491.925 |  | 499.4849 | -1.5135 | 504.53 | 490.68 | 2.846 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 807.99 |  | 815.2801 | -0.8942 | 830.62 | 811.99 | 3.0347 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 249.87 |  | 250.5325 | -0.2644 | 250.2 | 248.195 | 0.016 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.785 |  | 646.2896 | 0.2314 | 646.57 | 638.875 | 1.5113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.52 |  | 272.4935 | -0.3573 | 277.4 | 271.455 | 1.7678 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.23 |  | 157.7077 | -1.5711 | 163.02 | 159.54 | 1.4752 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
