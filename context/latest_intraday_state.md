# Intraday State

- Generated at: `2026-07-21T01:31:39+08:00`
- Market time ET: `2026-07-20T13:31:39-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `53`
- coverage_vwap: `53`
- caution_counts: `{'below_opening_15m_low': 27, 'manual_confirm_candidate': 2, 'below_vwap': 18, 'price_stale_or_missing': 2, 'watch_only': 2, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 700.07 |  | 701.7571 | -0.2404 | 705.51 | 701.82 | 0.01 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.28 |  | 532.9942 | -0.5092 | 538.59 | 532.55 | 0.066 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 562.98 |  | 566.5526 | -0.6306 | 572.46 | 567.02 | 0.0693 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 744.14 |  | 745.6596 | -0.2038 | 748.69 | 746.87 | 0.0161 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.905 |  | 396.1365 | 1.4562 | 392.89 | 389.74 | 0.0995 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.575 |  | 39.4061 | 2.9662 | 39.16 | 36.335 | 0.0246 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 381.275 |  | 380.4295 | 0.2223 | 382.67 | 377.47 | 0.0761 | watch_only | none |
| 2 | APLD | high_beta_ai_infrastructure | 27.89 |  | 27.8686 | 0.0766 | 28.39 | 27.11 | 0.0717 | watch_only | none |
| 3 | COHU | semiconductor_test_packaging | 51.64 |  | 51.5844 | 0.1077 | 52.74 | 50.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | MSFT | cloud_ai_capex | 401.905 |  | 396.1365 | 1.4562 | 392.89 | 389.74 | 0.0995 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 197.54 |  | 197.4002 | 0.0708 | 196.86 | 192.09 | 0.9922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | MU | memory_hbm_storage | 888.45 |  | 886.2287 | 0.2507 | 898.57 | 878.92 | 0.8926 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SNDK | memory_hbm_storage | 1429.14 |  | 1424.3995 | 0.3328 | 1449.57 | 1394.24 | 1.7878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | META | cloud_ai_capex | 649.42 |  | 645.9224 | 0.5415 | 646.57 | 638.875 | 2.5284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | IREN | high_beta_ai_infrastructure | 40.575 |  | 39.4061 | 2.9662 | 39.16 | 36.335 | 0.0246 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.17 |  | 24.1507 | 0.0801 | 24.51 | 24.22 | 0.0414 | below_opening_15m_low | below_opening_15m_low |
| 11 | AMZN | cloud_ai_capex | 250.42 |  | 250.5604 | -0.056 | 250.2 | 248.195 | 0.028 | below_vwap | below_vwap |
| 12 | VRT | data_center_power_cooling |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | DELL | ai_server_oem |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | CORZ | high_beta_ai_infrastructure | 22.265 |  | 22.3553 | -0.4039 | 22.565 | 21.85 | 0.0898 | below_vwap | below_vwap |
| 16 | GOOGL | cloud_ai_capex | 352.695 |  | 356.7093 | -1.1254 | 358.795 | 350.875 | 0.1588 | below_vwap | below_vwap |
| 17 | ORCL | cloud_ai_capex | 122.66 |  | 122.2764 | 0.3137 | 125.41 | 123.57 | 0.7093 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 385.45 |  | 387.183 | -0.4476 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 511.78 |  | 513.9751 | -0.4271 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 271.58 |  | 272.5436 | -0.3536 | 277.4 | 271.455 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.905 |  | 396.1365 | 1.4562 | 392.89 | 389.74 | 0.0995 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.575 |  | 39.4061 | 2.9662 | 39.16 | 36.335 | 0.0246 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 250.42 |  | 250.5604 | -0.056 | 250.2 | 248.195 | 0.028 | below_vwap | below_vwap |
| 4 | META | cloud_ai_capex | 649.42 |  | 645.9224 | 0.5415 | 646.57 | 638.875 | 2.5284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AVGO | custom_silicon_networking | 381.275 |  | 380.4295 | 0.2223 | 382.67 | 377.47 | 0.0761 | watch_only | none |
| 6 | MRVL | custom_silicon_networking | 197.54 |  | 197.4002 | 0.0708 | 196.86 | 192.09 | 0.9922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APLD | high_beta_ai_infrastructure | 27.89 |  | 27.8686 | 0.0766 | 28.39 | 27.11 | 0.0717 | watch_only | none |
| 8 | ANET | ai_networking_optical | 170.73 |  | 170.8541 | -0.0726 | 171.39 | 168.79 | 4.387 | below_vwap | below_vwap,spread_too_wide |
| 9 | AMD | ai_accelerator | 511.84 |  | 514.4745 | -0.5121 | 522.26 | 510.97 | 1.4887 | below_vwap | below_vwap,spread_too_wide |
| 10 | WDC | memory_hbm_storage | 497.04 |  | 500.1618 | -0.6242 | 504.53 | 490.68 | 1.4606 | below_vwap | below_vwap,spread_too_wide |
| 11 | LITE | ai_networking_optical | 785.415 |  | 788.8024 | -0.4294 | 790.59 | 767.2 | 2.0893 | below_vwap | below_vwap,spread_too_wide |
| 12 | VRT | data_center_power_cooling |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | DELL | ai_server_oem |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | CIEN | ai_networking_optical | 385.45 |  | 387.183 | -0.4476 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | APD | industrial_gases | 296.045 |  | 296.5771 | -0.1794 | 296.26 | 293.84 | 4.8337 | below_vwap | below_vwap,spread_too_wide |
| 16 | LIN | industrial_gases | 511.78 |  | 513.9751 | -0.4271 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 271.58 |  | 272.5436 | -0.3536 | 277.4 | 271.455 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 352.695 |  | 356.7093 | -1.1254 | 358.795 | 350.875 | 0.1588 | below_vwap | below_vwap |
| 20 | TER | semiconductor_test_packaging | 337.54 |  | 341.8299 | -1.255 | 349.43 | 335.335 | 4.2899 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 700.07 |  | 701.7571 | -0.2404 | 705.51 | 701.82 | 0.01 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 68.84 |  | 69.3069 | -0.6737 | 70.43 | 69.35 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 203.74 |  | 205.6762 | -0.9414 | 207.71 | 205.095 | 0.0196 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.905 |  | 396.1365 | 1.4562 | 392.89 | 389.74 | 0.0995 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 324.71 |  | 326.6476 | -0.5932 | 333.63 | 330.03 | 0.1417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 352.695 |  | 356.7093 | -1.1254 | 358.795 | 350.875 | 0.1588 | below_vwap | below_vwap |
| AMD | ai_accelerator | 511.84 |  | 514.4745 | -0.5121 | 522.26 | 510.97 | 1.4887 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 403.36 |  | 404.811 | -0.3584 | 409.82 | 405.51 | 0.1488 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1899775.6883 | -7.1469 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.28 |  | 532.9942 | -0.5092 | 538.59 | 532.55 | 0.066 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 562.98 |  | 566.5526 | -0.6306 | 572.46 | 567.02 | 0.0693 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.275 |  | 380.4295 | 0.2223 | 382.67 | 377.47 | 0.0761 | watch_only | none |
| MU | memory_hbm_storage | 888.45 |  | 886.2287 | 0.2507 | 898.57 | 878.92 | 0.8926 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 197.54 |  | 197.4002 | 0.0708 | 196.86 | 192.09 | 0.9922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.26 |  | 45.6798 | -0.919 | 46.21 | 45.305 | 0.0442 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.17 |  | 24.1507 | 0.0801 | 24.51 | 24.22 | 0.0414 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 744.14 |  | 745.6596 | -0.2038 | 748.69 | 746.87 | 0.0161 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 293.68 |  | 294.1019 | -0.1435 | 295.97 | 294.88 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 122.66 |  | 122.2764 | 0.3137 | 125.41 | 123.57 | 0.7093 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.5 |  | 76.5245 | -2.6455 | 79.23 | 75.17 | 0.4161 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 401.655 |  | 404.0159 | -0.5844 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 631.69 |  | 637.744 | -0.9493 | 644.7 | 636.38 | 3.5302 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1068.76 |  | 1077.6887 | -0.8285 | 1103.11 | 1081.14 | 3.3806 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 465.46 |  | 466.3505 | -0.1909 | 477.865 | 468.805 | 4.2216 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 139.8 |  | 140.5492 | -0.533 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.73 |  | 170.8541 | -0.0726 | 171.39 | 168.79 | 4.387 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 292.765 |  | 293.9434 | -0.4009 | 296.46 | 286.91 | 3.0195 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 785.415 |  | 788.8024 | -0.4294 | 790.59 | 767.2 | 2.0893 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 385.45 |  | 387.183 | -0.4476 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 104.46 |  | 105.1959 | -0.6995 | 107.28 | 104.215 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 311.305 |  | 314.8193 | -1.1163 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1736.04 |  | 1755.3923 | -1.1025 | 1797.04 | 1768.805 | 0.1238 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 529.94 |  | 537.3229 | -1.374 | 554.8 | 543 | 0.9643 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 308.59 |  | 312.5945 | -1.281 | 324.32 | 319.39 | 4.9807 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 209.55 |  | 212.23 | -1.2628 | 220.28 | 216.62 | 0.1288 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 337.54 |  | 341.8299 | -1.255 | 349.43 | 335.335 | 4.2899 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 279.41 |  | 282.4895 | -1.0901 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.8 |  | 63.4895 | -1.086 | 64.96 | 63.98 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.64 |  | 51.5844 | 0.1077 | 52.74 | 50.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.605 |  | 137.6417 | -0.7532 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.055 |  | 330.459 | -0.7275 | 338.1 | 328.505 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 511.78 |  | 513.9751 | -0.4271 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.045 |  | 296.5771 | -0.1794 | 296.26 | 293.84 | 4.8337 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.89 |  | 27.8686 | 0.0766 | 28.39 | 27.11 | 0.0717 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 40.575 |  | 39.4061 | 2.9662 | 39.16 | 36.335 | 0.0246 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.265 |  | 22.3553 | -0.4039 | 22.565 | 21.85 | 0.0898 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1429.14 |  | 1424.3995 | 0.3328 | 1449.57 | 1394.24 | 1.7878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 497.04 |  | 500.1618 | -0.6242 | 504.53 | 490.68 | 1.4606 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 806.28 |  | 816.2195 | -1.2178 | 830.62 | 811.99 | 3.0436 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 250.42 |  | 250.5604 | -0.056 | 250.2 | 248.195 | 0.028 | below_vwap | below_vwap |
| META | cloud_ai_capex | 649.42 |  | 645.9224 | 0.5415 | 646.57 | 638.875 | 2.5284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.58 |  | 272.5436 | -0.3536 | 277.4 | 271.455 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 156.565 |  | 157.9246 | -0.8609 | 163.02 | 159.54 | 2.0375 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
