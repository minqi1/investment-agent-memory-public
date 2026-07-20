# Intraday State

- Generated at: `2026-07-20T23:51:20+08:00`
- Market time ET: `2026-07-20T11:51:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 29, 'manual_confirm_candidate': 3, 'below_vwap': 16, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 4, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 700.795 |  | 701.7052 | -0.1297 | 705.51 | 701.82 | 0.0328 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 531.77 |  | 533.1833 | -0.2651 | 538.59 | 532.55 | 0.0884 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.485 |  | 567.0444 | -0.4514 | 572.46 | 567.02 | 0.0655 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.32 |  | 745.8268 | -0.068 | 748.69 | 746.87 | 0.0067 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 251.72 |  | 249.9255 | 0.718 | 250.2 | 248.195 | 0.0199 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 398.25 |  | 393.7645 | 1.1391 | 392.89 | 389.74 | 0.1281 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 39.34 |  | 38.8887 | 1.1605 | 39.16 | 36.335 | 0.0508 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 251.72 |  | 249.9255 | 0.718 | 250.2 | 248.195 | 0.0199 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 882.83 |  | 882.6434 | 0.0211 | 898.57 | 878.92 | 0.0578 | watch_only | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.52 |  | 22.3675 | 0.6817 | 22.565 | 21.85 | 0.0888 | watch_only | none |
| 4 | IREN | high_beta_ai_infrastructure | 39.34 |  | 38.8887 | 1.1605 | 39.16 | 36.335 | 0.0508 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 398.25 |  | 393.7645 | 1.1391 | 392.89 | 389.74 | 0.1281 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 380.83 |  | 379.7401 | 0.287 | 382.67 | 377.47 | 0.3519 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | META | cloud_ai_capex | 647.41 |  | 643.5083 | 0.6063 | 646.57 | 638.875 | 1.1847 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ALAB | ai_networking_optical | 316.485 |  | 314.8361 | 0.5237 | 322.065 | 308.955 | 4.7838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMCI | ai_server_oem | 24.12 |  | 24.1098 | 0.0424 | 24.51 | 24.22 | 0.0415 | below_opening_15m_low | below_opening_15m_low |
| 10 | HPE | ai_server_oem | 45.66 |  | 45.6833 | -0.0509 | 46.21 | 45.305 | 0.0657 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 169.61 |  | 170.9666 | -0.7935 | 171.39 | 168.79 | 0.3007 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | APD | industrial_gases | 296.72 |  | 296.8934 | -0.0584 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8647 | -0.2682 | 28.39 | 27.11 | 0.108 | below_vwap | below_vwap |
| 15 | GOOGL | cloud_ai_capex | 356.61 |  | 357.3857 | -0.217 | 358.795 | 350.875 | 0.3337 | below_vwap | below_vwap |
| 16 | CIEN | ai_networking_optical | 383.78 |  | 387.2088 | -0.8855 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | MKSI | semiconductor_materials | 329.22 |  | 330.6088 | -0.4201 | 338.1 | 328.505 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | MRVL | custom_silicon_networking | 199.23 |  | 196.5429 | 1.3672 | 196.86 | 192.09 | 4.7382 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 512.76 |  | 514.8672 | -0.4093 | 522.26 | 510.97 | 0.5851 | below_vwap | below_vwap,spread_too_wide |
| 20 | WDC | memory_hbm_storage | 496.17 |  | 500.1473 | -0.7952 | 504.53 | 490.68 | 0.7417 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 251.72 |  | 249.9255 | 0.718 | 250.2 | 248.195 | 0.0199 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 398.25 |  | 393.7645 | 1.1391 | 392.89 | 389.74 | 0.1281 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 39.34 |  | 38.8887 | 1.1605 | 39.16 | 36.335 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | APD | industrial_gases | 296.72 |  | 296.8934 | -0.0584 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 5 | META | cloud_ai_capex | 647.41 |  | 643.5083 | 0.6063 | 646.57 | 638.875 | 1.1847 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | MRVL | custom_silicon_networking | 199.23 |  | 196.5429 | 1.3672 | 196.86 | 192.09 | 4.7382 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | MU | memory_hbm_storage | 882.83 |  | 882.6434 | 0.0211 | 898.57 | 878.92 | 0.0578 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 22.52 |  | 22.3675 | 0.6817 | 22.565 | 21.85 | 0.0888 | watch_only | none |
| 9 | ANET | ai_networking_optical | 169.61 |  | 170.9666 | -0.7935 | 171.39 | 168.79 | 0.3007 | below_vwap | below_vwap |
| 10 | AMD | ai_accelerator | 512.76 |  | 514.8672 | -0.4093 | 522.26 | 510.97 | 0.5851 | below_vwap | below_vwap,spread_too_wide |
| 11 | WDC | memory_hbm_storage | 496.17 |  | 500.1473 | -0.7952 | 504.53 | 490.68 | 0.7417 | below_vwap | below_vwap,spread_too_wide |
| 12 | LITE | ai_networking_optical | 782.74 |  | 788.7344 | -0.76 | 790.59 | 767.2 | 3.2974 | below_vwap | below_vwap,spread_too_wide |
| 13 | CIEN | ai_networking_optical | 383.78 |  | 387.2088 | -0.8855 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | HPE | ai_server_oem | 45.66 |  | 45.6833 | -0.0509 | 46.21 | 45.305 | 0.0657 | below_vwap | below_vwap |
| 15 | LIN | industrial_gases | 514.42 |  | 514.7413 | -0.0624 | 514.7 | 511.78 | 4.8404 | below_vwap | below_vwap,spread_too_wide |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 356.61 |  | 357.3857 | -0.217 | 358.795 | 350.875 | 0.3337 | below_vwap | below_vwap |
| 18 | TER | semiconductor_test_packaging | 339.72 |  | 342.7325 | -0.879 | 349.43 | 335.335 | 4.4713 | below_vwap | below_vwap,spread_too_wide |
| 19 | MKSI | semiconductor_materials | 329.22 |  | 330.6088 | -0.4201 | 338.1 | 328.505 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 292.36 |  | 293.7652 | -0.4783 | 296.46 | 286.91 | 1.7239 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 700.795 |  | 701.7052 | -0.1297 | 705.51 | 701.82 | 0.0328 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.09 |  | 69.3155 | -0.3253 | 70.43 | 69.35 | 0.0289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.91 |  | 206.0026 | -0.5304 | 207.71 | 205.095 | 0.0098 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.25 |  | 393.7645 | 1.1391 | 392.89 | 389.74 | 0.1281 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 325.325 |  | 327.5425 | -0.677 | 333.63 | 330.03 | 0.1076 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 356.61 |  | 357.3857 | -0.217 | 358.795 | 350.875 | 0.3337 | below_vwap | below_vwap |
| AMD | ai_accelerator | 512.76 |  | 514.8672 | -0.4093 | 522.26 | 510.97 | 0.5851 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 403.875 |  | 404.6733 | -0.1973 | 409.82 | 405.51 | 0.1089 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1899775.6883 | -7.1469 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 531.77 |  | 533.1833 | -0.2651 | 538.59 | 532.55 | 0.0884 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.485 |  | 567.0444 | -0.4514 | 572.46 | 567.02 | 0.0655 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.83 |  | 379.7401 | 0.287 | 382.67 | 377.47 | 0.3519 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 882.83 |  | 882.6434 | 0.0211 | 898.57 | 878.92 | 0.0578 | watch_only | none |
| MRVL | custom_silicon_networking | 199.23 |  | 196.5429 | 1.3672 | 196.86 | 192.09 | 4.7382 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 387.425 |  | 392.1665 | -1.2091 | 402.76 | 392.82 | 0.3485 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 45.66 |  | 45.6833 | -0.0509 | 46.21 | 45.305 | 0.0657 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.12 |  | 24.1098 | 0.0424 | 24.51 | 24.22 | 0.0415 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 745.32 |  | 745.8268 | -0.068 | 748.69 | 746.87 | 0.0067 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.01 |  | 294.1905 | -0.0614 | 295.97 | 294.88 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 121.59 |  | 122.1752 | -0.479 | 125.41 | 123.57 | 0.074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 75.1 |  | 77.2034 | -2.7245 | 79.23 | 75.17 | 0.0533 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 294.105 |  | 296.603 | -0.8422 | 300.96 | 297.175 | 3.7402 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 401.365 |  | 404.6771 | -0.8184 | 413.44 | 406.66 | 4.4124 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 633.75 |  | 638.226 | -0.7013 | 644.7 | 636.38 | 3.7538 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1053.16 |  | 1080.9226 | -2.5684 | 1103.11 | 1081.14 | 4.7153 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 463.455 |  | 466.2892 | -0.6078 | 477.865 | 468.805 | 4.8376 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 139.68 |  | 140.9339 | -0.8897 | 143.075 | 141.14 | 4.3886 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 169.61 |  | 170.9666 | -0.7935 | 171.39 | 168.79 | 0.3007 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 292.36 |  | 293.7652 | -0.4783 | 296.46 | 286.91 | 1.7239 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 782.74 |  | 788.7344 | -0.76 | 790.59 | 767.2 | 3.2974 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 383.78 |  | 387.2088 | -0.8855 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 104.43 |  | 105.3221 | -0.847 | 107.28 | 104.215 | 1.0055 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 316.485 |  | 314.8361 | 0.5237 | 322.065 | 308.955 | 4.7838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1734 |  | 1759.1748 | -1.4311 | 1797.04 | 1768.805 | 0.8137 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 531.55 |  | 540.0388 | -1.5719 | 554.8 | 543 | 1.3169 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 309.57 |  | 313.3108 | -1.194 | 324.32 | 319.39 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 210.68 |  | 213.1375 | -1.153 | 220.28 | 216.62 | 0.1044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 339.72 |  | 342.7325 | -0.879 | 349.43 | 335.335 | 4.4713 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 278.9 |  | 283.866 | -1.7494 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.87 |  | 63.5949 | -1.1398 | 64.96 | 63.98 | 0.8271 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.24 |  | 51.397 | -0.3055 | 52.74 | 50.72 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 136.865 |  | 137.7331 | -0.6303 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.22 |  | 330.6088 | -0.4201 | 338.1 | 328.505 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 514.42 |  | 514.7413 | -0.0624 | 514.7 | 511.78 | 4.8404 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 296.72 |  | 296.8934 | -0.0584 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8647 | -0.2682 | 28.39 | 27.11 | 0.108 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 39.34 |  | 38.8887 | 1.1605 | 39.16 | 36.335 | 0.0508 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.52 |  | 22.3675 | 0.6817 | 22.565 | 21.85 | 0.0888 | watch_only | none |
| SNDK | memory_hbm_storage | 1415.52 |  | 1419.8559 | -0.3054 | 1449.57 | 1394.24 | 0.4776 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 496.17 |  | 500.1473 | -0.7952 | 504.53 | 490.68 | 0.7417 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 806.86 |  | 819.1096 | -1.4955 | 830.62 | 811.99 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 251.72 |  | 249.9255 | 0.718 | 250.2 | 248.195 | 0.0199 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 647.41 |  | 643.5083 | 0.6063 | 646.57 | 638.875 | 1.1847 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 270.77 |  | 272.4672 | -0.6229 | 277.4 | 271.455 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 156.7 |  | 158.1304 | -0.9046 | 163.02 | 159.54 | 1.94 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
