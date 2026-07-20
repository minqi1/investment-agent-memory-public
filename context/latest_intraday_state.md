# Intraday State

- Generated at: `2026-07-21T02:17:56+08:00`
- Market time ET: `2026-07-20T14:17:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `54`
- coverage_vwap: `54`
- caution_counts: `{'below_opening_15m_low': 25, 'manual_confirm_candidate': 3, 'below_vwap': 13, 'spread_too_wide_or_missing': 8, 'price_stale_or_missing': 3, 'watch_only': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701 |  | 701.6079 | -0.0867 | 705.51 | 701.82 | 0.0257 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 531.46 |  | 532.7907 | -0.2498 | 538.59 | 532.55 | 0.0677 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.41 |  | 566.277 | -0.3297 | 572.46 | 567.02 | 0.0549 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.11 |  | 745.509 | -0.0535 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 250.59 |  | 250.5473 | 0.0171 | 250.2 | 248.195 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.82 |  | 396.6884 | 1.2936 | 392.89 | 389.74 | 0.0249 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 40.825 |  | 39.5688 | 3.1747 | 39.16 | 36.335 | 0.0245 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 250.59 |  | 250.5473 | 0.0171 | 250.2 | 248.195 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 22.35 |  | 22.3464 | 0.0162 | 22.565 | 21.85 | 0.1342 | watch_only | none |
| 3 | APLD | high_beta_ai_infrastructure | 28.09 |  | 27.872 | 0.7822 | 28.39 | 27.11 | 0.1068 | watch_only | none |
| 4 | ARM | ai_accelerator | 273.29 |  | 272.5403 | 0.2751 | 277.4 | 271.455 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | COHU | semiconductor_test_packaging | 51.63 |  | 51.58 | 0.0969 | 52.74 | 50.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MSFT | cloud_ai_capex | 401.82 |  | 396.6884 | 1.2936 | 392.89 | 389.74 | 0.0249 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 123.59 |  | 122.3537 | 1.0104 | 125.41 | 123.57 | 0.0647 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.385 |  | 24.1678 | 0.8987 | 24.51 | 24.22 | 0.041 | watch_only | none |
| 9 | AVGO | custom_silicon_networking | 381.68 |  | 380.4794 | 0.3155 | 382.67 | 377.47 | 0.9301 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | AMD | ai_accelerator | 515.91 |  | 514.2683 | 0.3192 | 522.26 | 510.97 | 3.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | META | cloud_ai_capex | 648.56 |  | 646.1884 | 0.367 | 646.57 | 638.875 | 0.6954 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | GEV | data_center_power_cooling | 1081.73 |  | 1077.4917 | 0.3933 | 1103.11 | 1081.14 | 2.0883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | IWM | market_regime | 294.08 |  | 294.0782 | 0.0006 | 295.97 | 294.88 | 0.0102 | below_opening_15m_low | below_opening_15m_low |
| 14 | IREN | high_beta_ai_infrastructure | 40.825 |  | 39.5688 | 3.1747 | 39.16 | 36.335 | 0.0245 | buy_precheck_manual_confirm | none |
| 15 | MRVL | custom_silicon_networking | 198.22 |  | 197.4007 | 0.415 | 196.86 | 192.09 | 2.6435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SNDK | memory_hbm_storage | 1432.4 |  | 1425.0024 | 0.5191 | 1449.57 | 1394.24 | 1.4863 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LIN | industrial_gases | 511.915 |  | 513.4129 | -0.2917 | 514.7 | 511.78 | 0.0684 | below_vwap | below_vwap |
| 18 | GOOGL | cloud_ai_capex | 352.875 |  | 356.3457 | -0.974 | 358.795 | 350.875 | 0.0567 | below_vwap | below_vwap |
| 19 | TER | semiconductor_test_packaging | 339.325 |  | 341.3504 | -0.5933 | 349.43 | 335.335 | 0.1474 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 170.605 |  | 170.858 | -0.1481 | 171.39 | 168.79 | 0.3107 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 250.59 |  | 250.5473 | 0.0171 | 250.2 | 248.195 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.82 |  | 396.6884 | 1.2936 | 392.89 | 389.74 | 0.0249 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 40.825 |  | 39.5688 | 3.1747 | 39.16 | 36.335 | 0.0245 | buy_precheck_manual_confirm | none |
| 4 | APD | industrial_gases | 296.44 |  | 296.5392 | -0.0335 | 296.26 | 293.84 | 5.0364 | below_vwap | below_vwap,spread_too_wide |
| 5 | META | cloud_ai_capex | 648.56 |  | 646.1884 | 0.367 | 646.57 | 638.875 | 0.6954 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | MRVL | custom_silicon_networking | 198.22 |  | 197.4007 | 0.415 | 196.86 | 192.09 | 2.6435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ORCL | cloud_ai_capex | 123.59 |  | 122.3537 | 1.0104 | 125.41 | 123.57 | 0.0647 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.385 |  | 24.1678 | 0.8987 | 24.51 | 24.22 | 0.041 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.35 |  | 22.3464 | 0.0162 | 22.565 | 21.85 | 0.1342 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 28.09 |  | 27.872 | 0.7822 | 28.39 | 27.11 | 0.1068 | watch_only | none |
| 11 | ANET | ai_networking_optical | 170.605 |  | 170.858 | -0.1481 | 171.39 | 168.79 | 0.3107 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 882.44 |  | 886.0739 | -0.4101 | 898.57 | 878.92 | 0.2708 | below_vwap | below_vwap |
| 13 | WDC | memory_hbm_storage | 495.465 |  | 499.745 | -0.8564 | 504.53 | 490.68 | 1.7923 | below_vwap | below_vwap,spread_too_wide |
| 14 | LITE | ai_networking_optical | 778.525 |  | 788.2495 | -1.2337 | 790.59 | 767.2 | 2.8708 | below_vwap | below_vwap,spread_too_wide |
| 15 | CIEN | ai_networking_optical | 384.27 |  | 387.0367 | -0.7148 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | SKHY | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LIN | industrial_gases | 511.915 |  | 513.4129 | -0.2917 | 514.7 | 511.78 | 0.0684 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 352.875 |  | 356.3457 | -0.974 | 358.795 | 350.875 | 0.0567 | below_vwap | below_vwap |
| 20 | TER | semiconductor_test_packaging | 339.325 |  | 341.3504 | -0.5933 | 349.43 | 335.335 | 0.1474 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701 |  | 701.6079 | -0.0867 | 705.51 | 701.82 | 0.0257 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.09 |  | 69.2735 | -0.2649 | 70.43 | 69.35 | 0.0289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.84 |  | 205.5576 | -0.3491 | 207.71 | 205.095 | 0.1806 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.82 |  | 396.6884 | 1.2936 | 392.89 | 389.74 | 0.0249 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 325.59 |  | 326.4377 | -0.2597 | 333.63 | 330.03 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 352.875 |  | 356.3457 | -0.974 | 358.795 | 350.875 | 0.0567 | below_vwap | below_vwap |
| AMD | ai_accelerator | 515.91 |  | 514.2683 | 0.3192 | 522.26 | 510.97 | 3.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 403.665 |  | 404.6491 | -0.2432 | 409.82 | 405.51 | 0.1239 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 531.46 |  | 532.7907 | -0.2498 | 538.59 | 532.55 | 0.0677 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.41 |  | 566.277 | -0.3297 | 572.46 | 567.02 | 0.0549 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.68 |  | 380.4794 | 0.3155 | 382.67 | 377.47 | 0.9301 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 882.44 |  | 886.0739 | -0.4101 | 898.57 | 878.92 | 0.2708 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 198.22 |  | 197.4007 | 0.415 | 196.86 | 192.09 | 2.6435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 388.49 |  | 391.0471 | -0.6539 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.28 |  | 45.6327 | -0.7728 | 46.21 | 45.305 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.385 |  | 24.1678 | 0.8987 | 24.51 | 24.22 | 0.041 | watch_only | none |
| SPY | market_regime | 745.11 |  | 745.509 | -0.0535 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.08 |  | 294.0782 | 0.0006 | 295.97 | 294.88 | 0.0102 | below_opening_15m_low | below_opening_15m_low |
| ORCL | cloud_ai_capex | 123.59 |  | 122.3537 | 1.0104 | 125.41 | 123.57 | 0.0647 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 74.97 |  | 76.3534 | -1.8118 | 79.23 | 75.17 | 3.348 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 294.69 |  | 296.0653 | -0.4645 | 300.96 | 297.175 | 0.2206 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 403.215 |  | 403.8368 | -0.154 | 413.44 | 406.66 | 4.8113 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 634.71 |  | 637.4049 | -0.4228 | 644.7 | 636.38 | 1.492 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1081.73 |  | 1077.4917 | 0.3933 | 1103.11 | 1081.14 | 2.0883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.6 |  | 466.3523 | 0.0531 | 477.865 | 468.805 | 4.4514 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 140.05 |  | 140.4803 | -0.3063 | 143.075 | 141.14 | 4.5698 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 170.605 |  | 170.858 | -0.1481 | 171.39 | 168.79 | 0.3107 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 292.93 |  | 293.787 | -0.2917 | 296.46 | 286.91 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 778.525 |  | 788.2495 | -1.2337 | 790.59 | 767.2 | 2.8708 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 384.27 |  | 387.0367 | -0.7148 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 104.12 |  | 105.0808 | -0.9144 | 107.28 | 104.215 | 1.1429 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 312.46 |  | 314.2553 | -0.5713 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1742.38 |  | 1754.6992 | -0.7021 | 1797.04 | 1768.805 | 0.0947 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 531.3 |  | 536.674 | -1.0014 | 554.8 | 543 | 0.5534 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 309.21 |  | 312.3182 | -0.9952 | 324.32 | 319.39 | 3.3666 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 210.19 |  | 211.9866 | -0.8475 | 220.28 | 216.62 | 0.7945 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 339.325 |  | 341.3504 | -0.5933 | 349.43 | 335.335 | 0.1474 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 279.955 |  | 282.2994 | -0.8305 | 288.94 | 284 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 63.08 |  | 63.4579 | -0.5955 | 64.96 | 63.98 | 4.0742 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.63 |  | 51.58 | 0.0969 | 52.74 | 50.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.105 |  | 137.5896 | -0.3522 | 141.89 | 138.545 | 4.3835 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 327.32 |  | 329.5862 | -0.6876 | 338.1 | 328.505 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 511.915 |  | 513.4129 | -0.2917 | 514.7 | 511.78 | 0.0684 | below_vwap | below_vwap |
| APD | industrial_gases | 296.44 |  | 296.5392 | -0.0335 | 296.26 | 293.84 | 5.0364 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.09 |  | 27.872 | 0.7822 | 28.39 | 27.11 | 0.1068 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 40.825 |  | 39.5688 | 3.1747 | 39.16 | 36.335 | 0.0245 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.35 |  | 22.3464 | 0.0162 | 22.565 | 21.85 | 0.1342 | watch_only | none |
| SNDK | memory_hbm_storage | 1432.4 |  | 1425.0024 | 0.5191 | 1449.57 | 1394.24 | 1.4863 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 495.465 |  | 499.745 | -0.8564 | 504.53 | 490.68 | 1.7923 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 811.75 |  | 815.5772 | -0.4693 | 830.62 | 811.99 | 2.4182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 250.59 |  | 250.5473 | 0.0171 | 250.2 | 248.195 | 0.004 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 648.56 |  | 646.1884 | 0.367 | 646.57 | 638.875 | 0.6954 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.29 |  | 272.5403 | 0.2751 | 277.4 | 271.455 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
