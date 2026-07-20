# Intraday State

- Generated at: `2026-07-21T02:49:04+08:00`
- Market time ET: `2026-07-20T14:49:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 31, 'watch_only': 3, 'below_vwap': 20, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.31 |  | 701.4567 | -0.4486 | 705.51 | 701.82 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.32 |  | 532.5981 | -0.8032 | 538.59 | 532.55 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 561.54 |  | 566.0484 | -0.7965 | 572.46 | 567.02 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 742.98 |  | 745.2982 | -0.311 | 748.69 | 746.87 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 24.225 |  | 24.182 | 0.1778 | 24.51 | 24.22 | 0.0413 | watch_only | none |
| 2 | META | cloud_ai_capex | 646.56 |  | 646.3016 | 0.04 | 646.57 | 638.875 | 1.1615 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | MSFT | cloud_ai_capex | 400.49 |  | 397.1437 | 0.8426 | 392.89 | 389.74 | 0.0375 | watch_strength | none |
| 4 | GEV | data_center_power_cooling | 1078.42 |  | 1077.6478 | 0.0717 | 1103.11 | 1081.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 5 | IREN | high_beta_ai_infrastructure | 40.48 |  | 39.657 | 2.0753 | 39.16 | 36.335 | 0.0494 | watch_strength | none |
| 6 | AMZN | cloud_ai_capex | 249.32 |  | 250.5006 | -0.4713 | 250.2 | 248.195 | 0.012 | below_vwap | below_vwap |
| 7 | GOOGL | cloud_ai_capex | 351.305 |  | 355.823 | -1.2697 | 358.795 | 350.875 | 0.1281 | below_vwap | below_vwap |
| 8 | AVGO | custom_silicon_networking | 379.505 |  | 380.4757 | -0.2551 | 382.67 | 377.47 | 0.2846 | below_vwap | below_vwap |
| 9 | TT | data_center_power_cooling | 466.925 |  | 466.3983 | 0.1129 | 477.865 | 468.805 | 4.4483 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | CORZ | high_beta_ai_infrastructure | 22.09 |  | 22.3385 | -1.1122 | 22.565 | 21.85 | 0.0453 | below_vwap | below_vwap |
| 12 | APD | industrial_gases | 296.26 |  | 296.5395 | -0.0942 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | APLD | high_beta_ai_infrastructure | 27.775 |  | 27.8705 | -0.3428 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| 14 | AAPL | mega_cap_platform | 326.595 |  | 326.409 | 0.057 | 333.63 | 330.03 | 0.6736 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | LIN | industrial_gases | 512.11 |  | 513.3228 | -0.2363 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 51.43 |  | 51.5718 | -0.275 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ALAB | ai_networking_optical | 311.09 |  | 314.0225 | -0.9339 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ANET | ai_networking_optical | 170.12 |  | 170.8212 | -0.4105 | 171.39 | 168.79 | 4.1794 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMD | ai_accelerator | 514.25 |  | 514.3267 | -0.0149 | 522.26 | 510.97 | 4.0797 | below_vwap | below_vwap,spread_too_wide |
| 20 | MRVL | custom_silicon_networking | 197.055 |  | 197.3986 | -0.174 | 196.86 | 192.09 | 3.0956 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.49 |  | 397.1437 | 0.8426 | 392.89 | 389.74 | 0.0375 | watch_strength | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.48 |  | 39.657 | 2.0753 | 39.16 | 36.335 | 0.0494 | watch_strength | none |
| 3 | APD | industrial_gases | 296.26 |  | 296.5395 | -0.0942 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 4 | MRVL | custom_silicon_networking | 197.055 |  | 197.3986 | -0.174 | 196.86 | 192.09 | 3.0956 | below_vwap | below_vwap,spread_too_wide |
| 5 | SMCI | ai_server_oem | 24.225 |  | 24.182 | 0.1778 | 24.51 | 24.22 | 0.0413 | watch_only | none |
| 6 | ANET | ai_networking_optical | 170.12 |  | 170.8212 | -0.4105 | 171.39 | 168.79 | 4.1794 | below_vwap | below_vwap,spread_too_wide |
| 7 | AVGO | custom_silicon_networking | 379.505 |  | 380.4757 | -0.2551 | 382.67 | 377.47 | 0.2846 | below_vwap | below_vwap |
| 8 | AMD | ai_accelerator | 514.25 |  | 514.3267 | -0.0149 | 522.26 | 510.97 | 4.0797 | below_vwap | below_vwap,spread_too_wide |
| 9 | AMZN | cloud_ai_capex | 249.32 |  | 250.5006 | -0.4713 | 250.2 | 248.195 | 0.012 | below_vwap | below_vwap |
| 10 | WDC | memory_hbm_storage | 492.08 |  | 499.3694 | -1.4597 | 504.53 | 490.68 | 2.5931 | below_vwap | below_vwap,spread_too_wide |
| 11 | LITE | ai_networking_optical | 775.925 |  | 787.1937 | -1.4315 | 790.59 | 767.2 | 0.7436 | below_vwap | below_vwap,spread_too_wide |
| 12 | CIEN | ai_networking_optical | 382.26 |  | 386.8437 | -1.1849 | 393.855 | 377.005 | 0.3872 | below_vwap | below_vwap,spread_too_wide |
| 13 | LIN | industrial_gases | 512.11 |  | 513.3228 | -0.2363 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ARM | ai_accelerator | 271.765 |  | 272.4736 | -0.2601 | 277.4 | 271.455 | 1.5859 | below_vwap | below_vwap,spread_too_wide |
| 16 | GOOGL | cloud_ai_capex | 351.305 |  | 355.823 | -1.2697 | 358.795 | 350.875 | 0.1281 | below_vwap | below_vwap |
| 17 | TER | semiconductor_test_packaging | 336.21 |  | 341.0107 | -1.4078 | 349.43 | 335.335 | 3.8666 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 290.08 |  | 293.6249 | -1.2073 | 296.46 | 286.91 | 2.6889 | below_vwap | below_vwap,spread_too_wide |
| 19 | COHU | semiconductor_test_packaging | 51.43 |  | 51.5718 | -0.275 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | SNDK | memory_hbm_storage | 1414.21 |  | 1424.5609 | -0.7266 | 1449.57 | 1394.24 | 2.5399 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.31 |  | 701.4567 | -0.4486 | 705.51 | 701.82 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 68.33 |  | 69.2428 | -1.3183 | 70.43 | 69.35 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 203.595 |  | 205.4675 | -0.9113 | 207.71 | 205.095 | 0.2603 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.49 |  | 397.1437 | 0.8426 | 392.89 | 389.74 | 0.0375 | watch_strength | none |
| AAPL | mega_cap_platform | 326.595 |  | 326.409 | 0.057 | 333.63 | 330.03 | 0.6736 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GOOGL | cloud_ai_capex | 351.305 |  | 355.823 | -1.2697 | 358.795 | 350.875 | 0.1281 | below_vwap | below_vwap |
| AMD | ai_accelerator | 514.25 |  | 514.3267 | -0.0149 | 522.26 | 510.97 | 4.0797 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 402.255 |  | 404.5129 | -0.5582 | 409.82 | 405.51 | 0.174 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.32 |  | 532.5981 | -0.8032 | 538.59 | 532.55 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 561.54 |  | 566.0484 | -0.7965 | 572.46 | 567.02 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.505 |  | 380.4757 | -0.2551 | 382.67 | 377.47 | 0.2846 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 874.89 |  | 885.2098 | -1.1658 | 898.57 | 878.92 | 0.0652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 197.055 |  | 197.3986 | -0.174 | 196.86 | 192.09 | 3.0956 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 387.42 |  | 390.822 | -0.8705 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.29 |  | 45.6038 | -0.688 | 46.21 | 45.305 | 0.0883 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.225 |  | 24.182 | 0.1778 | 24.51 | 24.22 | 0.0413 | watch_only | none |
| SPY | market_regime | 742.98 |  | 745.2982 | -0.311 | 748.69 | 746.87 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 293.305 |  | 294.0308 | -0.2468 | 295.97 | 294.88 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 122.9 |  | 122.4051 | 0.4043 | 125.41 | 123.57 | 0.3662 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.135 |  | 76.2624 | -2.7895 | 79.23 | 75.17 | 3.8848 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.68 |  | 295.9084 | -0.7531 | 300.96 | 297.175 | 3.9839 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 401.855 |  | 403.7145 | -0.4606 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 632.94 |  | 637.2344 | -0.6739 | 644.7 | 636.38 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1078.42 |  | 1077.6478 | 0.0717 | 1103.11 | 1081.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 466.925 |  | 466.3983 | 0.1129 | 477.865 | 468.805 | 4.4483 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 139.615 |  | 140.4276 | -0.5786 | 143.075 | 141.14 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ANET | ai_networking_optical | 170.12 |  | 170.8212 | -0.4105 | 171.39 | 168.79 | 4.1794 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 290.08 |  | 293.6249 | -1.2073 | 296.46 | 286.91 | 2.6889 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 775.925 |  | 787.1937 | -1.4315 | 790.59 | 767.2 | 0.7436 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 382.26 |  | 386.8437 | -1.1849 | 393.855 | 377.005 | 0.3872 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 103.22 |  | 104.9729 | -1.6698 | 107.28 | 104.215 | 4.0787 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 311.09 |  | 314.0225 | -0.9339 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1737.34 |  | 1753.6394 | -0.9295 | 1797.04 | 1768.805 | 0.0599 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 528.78 |  | 536.21 | -1.3857 | 554.8 | 543 | 0.2345 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 307.46 |  | 311.9756 | -1.4474 | 324.32 | 319.39 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 209.38 |  | 211.7664 | -1.1269 | 220.28 | 216.62 | 0.1003 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 336.21 |  | 341.0107 | -1.4078 | 349.43 | 335.335 | 3.8666 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.22 |  | 281.8544 | -0.5799 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.58 |  | 63.4046 | -1.3006 | 64.96 | 63.98 | 0.1278 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 51.43 |  | 51.5718 | -0.275 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 136.07 |  | 137.5095 | -1.0469 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 324.71 |  | 329.3062 | -1.3957 | 338.1 | 328.505 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 512.11 |  | 513.3228 | -0.2363 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.26 |  | 296.5395 | -0.0942 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.775 |  | 27.8705 | -0.3428 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.48 |  | 39.657 | 2.0753 | 39.16 | 36.335 | 0.0494 | watch_strength | none |
| CORZ | high_beta_ai_infrastructure | 22.09 |  | 22.3385 | -1.1122 | 22.565 | 21.85 | 0.0453 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1414.21 |  | 1424.5609 | -0.7266 | 1449.57 | 1394.24 | 2.5399 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 492.08 |  | 499.3694 | -1.4597 | 504.53 | 490.68 | 2.5931 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 810.53 |  | 815.1597 | -0.568 | 830.62 | 811.99 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 249.32 |  | 250.5006 | -0.4713 | 250.2 | 248.195 | 0.012 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.56 |  | 646.3016 | 0.04 | 646.57 | 638.875 | 1.1615 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.765 |  | 272.4736 | -0.2601 | 277.4 | 271.455 | 1.5859 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.18 |  | 157.6697 | -1.5791 | 163.02 | 159.54 | 1.4757 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
