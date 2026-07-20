# Intraday State

- Generated at: `2026-07-20T23:56:59+08:00`
- Market time ET: `2026-07-20T11:56:59-04:00`
- Session open: `None`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_vwap': 14, 'manual_confirm_candidate': 3, 'below_opening_15m_low': 23, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 702.2 |  | 701.7001 | 0.0712 | 705.51 | 701.82 | 0.0057 | watch_only | none |
| SOXX | semiconductor_index | 533.2 |  | 533.1823 | 0.0033 | 538.59 | 532.55 | 0.0581 | watch_only | none |
| SMH | semiconductor_index | 565.99 |  | 567.0389 | -0.185 | 572.46 | 567.02 | 0.053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 746.24 |  | 745.8259 | 0.0555 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 251.98 |  | 249.9667 | 0.8054 | 250.2 | 248.195 | 0.0079 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 398.88 |  | 393.8462 | 1.2781 | 392.89 | 389.74 | 0.0476 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 39.715 |  | 38.9144 | 2.0573 | 39.16 | 36.335 | 0.0504 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 702.2 |  | 701.7001 | 0.0712 | 705.51 | 701.82 | 0.0057 | watch_only | none |
| 2 | SOXX | semiconductor_index | 533.2 |  | 533.1823 | 0.0033 | 538.59 | 532.55 | 0.0581 | watch_only | none |
| 3 | HPE | ai_server_oem | 45.74 |  | 45.6835 | 0.1236 | 46.21 | 45.305 | 0.0656 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.41 |  | 22.374 | 0.1609 | 22.565 | 21.85 | 0.0446 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 27.88 |  | 27.8641 | 0.0571 | 28.39 | 27.11 | 0.1076 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 381.98 |  | 379.7515 | 0.5868 | 382.67 | 377.47 | 0.1021 | watch_only | none |
| 7 | SMCI | ai_server_oem | 24.22 |  | 24.1127 | 0.4451 | 24.51 | 24.22 | 0.0826 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 251.98 |  | 249.9667 | 0.8054 | 250.2 | 248.195 | 0.0079 | buy_precheck_manual_confirm | none |
| 9 | SNDK | memory_hbm_storage | 1425.75 |  | 1419.8682 | 0.4143 | 1449.57 | 1394.24 | 0.336 | watch_only | none |
| 10 | MU | memory_hbm_storage | 889.93 |  | 882.8323 | 0.804 | 898.57 | 878.92 | 0.1292 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 398.88 |  | 393.8462 | 1.2781 | 392.89 | 389.74 | 0.0476 | buy_precheck_manual_confirm | none |
| 12 | COHR | ai_networking_optical | 294.055 |  | 293.7598 | 0.1005 | 296.46 | 286.91 | 2.7818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ALAB | ai_networking_optical | 316.89 |  | 314.8767 | 0.6394 | 322.065 | 308.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 39.715 |  | 38.9144 | 2.0573 | 39.16 | 36.335 | 0.0504 | buy_precheck_manual_confirm | none |
| 15 | META | cloud_ai_capex | 647.76 |  | 643.6465 | 0.6391 | 646.57 | 638.875 | 1.1069 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SPY | market_regime | 746.24 |  | 745.8259 | 0.0555 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 17 | NVDA | ai_accelerator | 205.565 |  | 205.9882 | -0.2054 | 207.71 | 205.095 | 0.0535 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 357.175 |  | 357.3819 | -0.0579 | 358.795 | 350.875 | 0.1988 | below_vwap | below_vwap |
| 20 | CIEN | ai_networking_optical | 385.06 |  | 387.1392 | -0.5371 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 251.98 |  | 249.9667 | 0.8054 | 250.2 | 248.195 | 0.0079 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 398.88 |  | 393.8462 | 1.2781 | 392.89 | 389.74 | 0.0476 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 39.715 |  | 38.9144 | 2.0573 | 39.16 | 36.335 | 0.0504 | buy_precheck_manual_confirm | none |
| 4 | APD | industrial_gases | 296.53 |  | 296.7513 | -0.0746 | 296.26 | 293.84 | 0.6374 | below_vwap | below_vwap,spread_too_wide |
| 5 | META | cloud_ai_capex | 647.76 |  | 643.6465 | 0.6391 | 646.57 | 638.875 | 1.1069 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AVGO | custom_silicon_networking | 381.98 |  | 379.7515 | 0.5868 | 382.67 | 377.47 | 0.1021 | watch_only | none |
| 7 | MRVL | custom_silicon_networking | 200.08 |  | 196.5866 | 1.777 | 196.86 | 192.09 | 0.8047 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | QQQ | market_regime | 702.2 |  | 701.7001 | 0.0712 | 705.51 | 701.82 | 0.0057 | watch_only | none |
| 9 | MU | memory_hbm_storage | 889.93 |  | 882.8323 | 0.804 | 898.57 | 878.92 | 0.1292 | watch_only | none |
| 10 | SOXX | semiconductor_index | 533.2 |  | 533.1823 | 0.0033 | 538.59 | 532.55 | 0.0581 | watch_only | none |
| 11 | HPE | ai_server_oem | 45.74 |  | 45.6835 | 0.1236 | 46.21 | 45.305 | 0.0656 | watch_only | none |
| 12 | SNDK | memory_hbm_storage | 1425.75 |  | 1419.8682 | 0.4143 | 1449.57 | 1394.24 | 0.336 | watch_only | none |
| 13 | SMCI | ai_server_oem | 24.22 |  | 24.1127 | 0.4451 | 24.51 | 24.22 | 0.0826 | watch_only | none |
| 14 | CORZ | high_beta_ai_infrastructure | 22.41 |  | 22.374 | 0.1609 | 22.565 | 21.85 | 0.0446 | watch_only | none |
| 15 | APLD | high_beta_ai_infrastructure | 27.88 |  | 27.8641 | 0.0571 | 28.39 | 27.11 | 0.1076 | watch_only | none |
| 16 | TQQQ | leveraged_tool | 69.51 |  | 69.3149 | 0.2815 | 70.43 | 69.35 | 0.0144 | watch_only | none |
| 17 | ANET | ai_networking_optical | 169.98 |  | 170.9298 | -0.5557 | 171.39 | 168.79 | 0.3883 | below_vwap | below_vwap,spread_too_wide |
| 18 | NVDA | ai_accelerator | 205.565 |  | 205.9882 | -0.2054 | 207.71 | 205.095 | 0.0535 | below_vwap | below_vwap |
| 19 | AMD | ai_accelerator | 514.37 |  | 514.8604 | -0.0952 | 522.26 | 510.97 | 4.3218 | below_vwap | below_vwap,spread_too_wide |
| 20 | WDC | memory_hbm_storage | 499.02 |  | 500.1125 | -0.2185 | 504.53 | 490.68 | 0.8777 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 702.2 |  | 701.7001 | 0.0712 | 705.51 | 701.82 | 0.0057 | watch_only | none |
| TQQQ | leveraged_tool | 69.51 |  | 69.3149 | 0.2815 | 70.43 | 69.35 | 0.0144 | watch_only | none |
| NVDA | ai_accelerator | 205.565 |  | 205.9882 | -0.2054 | 207.71 | 205.095 | 0.0535 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 398.88 |  | 393.8462 | 1.2781 | 392.89 | 389.74 | 0.0476 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 326.295 |  | 327.5037 | -0.3691 | 333.63 | 330.03 | 0.3862 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 357.175 |  | 357.3819 | -0.0579 | 358.795 | 350.875 | 0.1988 | below_vwap | below_vwap |
| AMD | ai_accelerator | 514.37 |  | 514.8604 | -0.0952 | 522.26 | 510.97 | 4.3218 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 404.16 |  | 404.6615 | -0.1239 | 409.82 | 405.51 | 0.1608 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1899775.6883 | -7.1469 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 533.2 |  | 533.1823 | 0.0033 | 538.59 | 532.55 | 0.0581 | watch_only | none |
| SMH | semiconductor_index | 565.99 |  | 567.0389 | -0.185 | 572.46 | 567.02 | 0.053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.98 |  | 379.7515 | 0.5868 | 382.67 | 377.47 | 0.1021 | watch_only | none |
| MU | memory_hbm_storage | 889.93 |  | 882.8323 | 0.804 | 898.57 | 878.92 | 0.1292 | watch_only | none |
| MRVL | custom_silicon_networking | 200.08 |  | 196.5866 | 1.777 | 196.86 | 192.09 | 0.8047 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 388.16 |  | 392.1072 | -1.0067 | 402.76 | 392.82 | 4.8485 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.74 |  | 45.6835 | 0.1236 | 46.21 | 45.305 | 0.0656 | watch_only | none |
| SMCI | ai_server_oem | 24.22 |  | 24.1127 | 0.4451 | 24.51 | 24.22 | 0.0826 | watch_only | none |
| SPY | market_regime | 746.24 |  | 745.8259 | 0.0555 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 293.94 |  | 294.1865 | -0.0838 | 295.97 | 294.88 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 121.945 |  | 122.1695 | -0.1837 | 125.41 | 123.57 | 1.5909 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 75.13 |  | 77.1776 | -2.6531 | 79.23 | 75.17 | 2.9149 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 295.485 |  | 296.5771 | -0.3682 | 300.96 | 297.175 | 3.2083 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 401.7 |  | 404.6416 | -0.727 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 634.14 |  | 638.2197 | -0.6392 | 644.7 | 636.38 | 1.5202 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1058.85 |  | 1080.4281 | -1.9972 | 1103.11 | 1081.14 | 4.3528 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 464.765 |  | 466.2358 | -0.3155 | 477.865 | 468.805 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 139.58 |  | 140.9162 | -0.9482 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.98 |  | 170.9298 | -0.5557 | 171.39 | 168.79 | 0.3883 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.055 |  | 293.7598 | 0.1005 | 296.46 | 286.91 | 2.7818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 787.645 |  | 788.7101 | -0.135 | 790.59 | 767.2 | 1.4093 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 385.06 |  | 387.1392 | -0.5371 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 104.48 |  | 105.2995 | -0.7782 | 107.28 | 104.215 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.89 |  | 314.8767 | 0.6394 | 322.065 | 308.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1737.745 |  | 1758.8654 | -1.2008 | 1797.04 | 1768.805 | 4.6612 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 532.64 |  | 539.821 | -1.3303 | 554.8 | 543 | 0.2628 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 310.23 |  | 313.2789 | -0.9732 | 324.32 | 319.39 | 4.4354 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 211.05 |  | 212.9105 | -0.8739 | 220.28 | 216.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 340.3 |  | 342.6848 | -0.6959 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.46 |  | 283.728 | -1.5043 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.92 |  | 63.5925 | -1.0575 | 64.96 | 63.98 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.24 |  | 51.397 | -0.3055 | 52.74 | 50.72 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.375 |  | 137.7195 | -0.2502 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.84 |  | 330.575 | -0.2224 | 338.1 | 328.505 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 514.63 |  | 514.7378 | -0.0209 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.53 |  | 296.7513 | -0.0746 | 296.26 | 293.84 | 0.6374 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.88 |  | 27.8641 | 0.0571 | 28.39 | 27.11 | 0.1076 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.715 |  | 38.9144 | 2.0573 | 39.16 | 36.335 | 0.0504 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.41 |  | 22.374 | 0.1609 | 22.565 | 21.85 | 0.0446 | watch_only | none |
| SNDK | memory_hbm_storage | 1425.75 |  | 1419.8682 | 0.4143 | 1449.57 | 1394.24 | 0.336 | watch_only | none |
| WDC | memory_hbm_storage | 499.02 |  | 500.1125 | -0.2185 | 504.53 | 490.68 | 0.8777 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 811.63 |  | 818.9292 | -0.8913 | 830.62 | 811.99 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 251.98 |  | 249.9667 | 0.8054 | 250.2 | 248.195 | 0.0079 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 647.76 |  | 643.6465 | 0.6391 | 646.57 | 638.875 | 1.1069 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.65 |  | 272.446 | -0.2922 | 277.4 | 271.455 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 157.5 |  | 158.1215 | -0.393 | 163.02 | 159.54 | 1.5238 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
