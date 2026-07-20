# Intraday State

- Generated at: `2026-07-21T02:11:37+08:00`
- Market time ET: `2026-07-20T14:11:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `54`
- coverage_vwap: `54`
- caution_counts: `{'below_opening_15m_low': 29, 'watch_only': 5, 'below_vwap': 14, 'spread_too_wide_or_missing': 5, 'price_stale_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 700.895 |  | 701.6171 | -0.1029 | 705.51 | 701.82 | 0.01 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.32 |  | 532.8121 | -0.4677 | 538.59 | 532.55 | 0.0679 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.45 |  | 566.3299 | -0.3319 | 572.46 | 567.02 | 0.0549 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 744.89 |  | 745.5191 | -0.0844 | 748.69 | 746.87 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APLD | high_beta_ai_infrastructure | 27.94 |  | 27.8701 | 0.2507 | 28.39 | 27.11 | 0.0716 | watch_only | none |
| 2 | AVGO | custom_silicon_networking | 382.01 |  | 380.4738 | 0.4038 | 382.67 | 377.47 | 0.0471 | watch_only | none |
| 3 | ARM | ai_accelerator | 273.37 |  | 272.5342 | 0.3067 | 277.4 | 271.455 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | SMCI | ai_server_oem | 24.41 |  | 24.1662 | 1.0088 | 24.51 | 24.22 | 0.041 | watch_only | none |
| 5 | AMD | ai_accelerator | 515.25 |  | 514.2543 | 0.1936 | 522.26 | 510.97 | 3.6875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | MRVL | custom_silicon_networking | 197.75 |  | 197.3947 | 0.18 | 196.86 | 192.09 | 2.9987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | MSFT | cloud_ai_capex | 401.65 |  | 396.6139 | 1.2698 | 392.89 | 389.74 | 0.0398 | watch_strength | none |
| 8 | TT | data_center_power_cooling | 466.88 |  | 466.3512 | 0.1134 | 477.865 | 468.805 | 0.1221 | below_opening_15m_low | below_opening_15m_low |
| 9 | META | cloud_ai_capex | 648.85 |  | 646.1709 | 0.4146 | 646.57 | 638.875 | 0.467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SNDK | memory_hbm_storage | 1432.115 |  | 1424.9555 | 0.5024 | 1449.57 | 1394.24 | 2.0948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | AMZN | cloud_ai_capex | 250.65 |  | 251.0849 | -0.1732 | 250.22 | 248.12 | 0.016 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 884.41 |  | 886.2131 | -0.2035 | 898.57 | 878.92 | 0.0611 | below_vwap | below_vwap |
| 13 | IREN | high_beta_ai_infrastructure | 40.75 |  | 39.5544 | 3.0226 | 39.16 | 36.335 | 0.0245 | watch_strength | none |
| 14 | GOOGL | cloud_ai_capex | 352.99 |  | 356.4438 | -0.969 | 358.795 | 350.875 | 0.119 | below_vwap | below_vwap |
| 15 | WDC | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GEV | data_center_power_cooling | 1079.115 |  | 1077.4454 | 0.155 | 1103.11 | 1081.14 | 2.1666 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | CORZ | high_beta_ai_infrastructure | 22.31 |  | 22.3466 | -0.1636 | 22.565 | 21.85 | 0.0448 | below_vwap | below_vwap |
| 19 | APD | industrial_gases | 296.37 |  | 296.5393 | -0.0571 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CIEN | ai_networking_optical | 384.32 |  | 387.0563 | -0.707 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.65 |  | 396.6139 | 1.2698 | 392.89 | 389.74 | 0.0398 | watch_strength | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.75 |  | 39.5544 | 3.0226 | 39.16 | 36.335 | 0.0245 | watch_strength | none |
| 3 | AMZN | cloud_ai_capex | 250.65 |  | 251.0849 | -0.1732 | 250.22 | 248.12 | 0.016 | below_vwap | below_vwap |
| 4 | APD | industrial_gases | 296.37 |  | 296.5393 | -0.0571 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 5 | META | cloud_ai_capex | 648.85 |  | 646.1709 | 0.4146 | 646.57 | 638.875 | 0.467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AVGO | custom_silicon_networking | 382.01 |  | 380.4738 | 0.4038 | 382.67 | 377.47 | 0.0471 | watch_only | none |
| 7 | MRVL | custom_silicon_networking | 197.75 |  | 197.3947 | 0.18 | 196.86 | 192.09 | 2.9987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SMCI | ai_server_oem | 24.41 |  | 24.1662 | 1.0088 | 24.51 | 24.22 | 0.041 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 27.94 |  | 27.8701 | 0.2507 | 28.39 | 27.11 | 0.0716 | watch_only | none |
| 10 | ANET | ai_networking_optical | 170.835 |  | 170.8664 | -0.0184 | 171.39 | 168.79 | 4.3083 | below_vwap | below_vwap,spread_too_wide |
| 11 | MU | memory_hbm_storage | 884.41 |  | 886.2131 | -0.2035 | 898.57 | 878.92 | 0.0611 | below_vwap | below_vwap |
| 12 | WDC | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | LITE | ai_networking_optical | 781.3 |  | 788.3775 | -0.8977 | 790.59 | 767.2 | 2.7429 | below_vwap | below_vwap,spread_too_wide |
| 14 | CIEN | ai_networking_optical | 384.32 |  | 387.0563 | -0.707 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | GOOGL | cloud_ai_capex | 352.99 |  | 356.4438 | -0.969 | 358.795 | 350.875 | 0.119 | below_vwap | below_vwap |
| 17 | TER | semiconductor_test_packaging | 338.92 |  | 341.3581 | -0.7142 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | COHR | ai_networking_optical | 292.59 |  | 293.8025 | -0.4127 | 296.46 | 286.91 | 1.4184 | below_vwap | below_vwap,spread_too_wide |
| 19 | ALAB | ai_networking_optical | 310.42 |  | 314.2679 | -1.2244 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 22.31 |  | 22.3466 | -0.1636 | 22.565 | 21.85 | 0.0448 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 700.895 |  | 701.6171 | -0.1029 | 705.51 | 701.82 | 0.01 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.02 |  | 69.2753 | -0.3685 | 70.43 | 69.35 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.77 |  | 205.5643 | -0.3864 | 207.71 | 205.095 | 0.0147 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.65 |  | 396.6139 | 1.2698 | 392.89 | 389.74 | 0.0398 | watch_strength | none |
| AAPL | mega_cap_platform | 325.425 |  | 326.4473 | -0.3132 | 333.63 | 330.03 | 0.0061 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 352.99 |  | 356.4438 | -0.969 | 358.795 | 350.875 | 0.119 | below_vwap | below_vwap |
| AMD | ai_accelerator | 515.25 |  | 514.2543 | 0.1936 | 522.26 | 510.97 | 3.6875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 403.86 |  | 404.6641 | -0.1987 | 409.82 | 405.51 | 0.0619 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.32 |  | 532.8121 | -0.4677 | 538.59 | 532.55 | 0.0679 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.45 |  | 566.3299 | -0.3319 | 572.46 | 567.02 | 0.0549 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 382.01 |  | 380.4738 | 0.4038 | 382.67 | 377.47 | 0.0471 | watch_only | none |
| MU | memory_hbm_storage | 884.41 |  | 886.2131 | -0.2035 | 898.57 | 878.92 | 0.0611 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 197.75 |  | 197.3947 | 0.18 | 196.86 | 192.09 | 2.9987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 387.2 |  | 391.1617 | -1.0128 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.27 |  | 45.6381 | -0.8066 | 46.21 | 45.305 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.41 |  | 24.1662 | 1.0088 | 24.51 | 24.22 | 0.041 | watch_only | none |
| SPY | market_regime | 744.89 |  | 745.5191 | -0.0844 | 748.69 | 746.87 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.045 |  | 294.0785 | -0.0114 | 295.97 | 294.88 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 123.48 |  | 122.3396 | 0.9321 | 125.41 | 123.57 | 0.0567 | below_opening_15m_low | below_opening_15m_low |
| CRWV | gpu_cloud_ai_factory | 74.825 |  | 76.3682 | -2.0208 | 79.23 | 75.17 | 0.0668 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 294.76 |  | 296.0806 | -0.446 | 300.96 | 297.175 | 3.8676 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 402.795 |  | 403.8506 | -0.2614 | 413.44 | 406.66 | 1.7999 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 634.66 |  | 637.4197 | -0.4329 | 644.7 | 636.38 | 1.5237 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1079.115 |  | 1077.4454 | 0.155 | 1103.11 | 1081.14 | 2.1666 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 466.88 |  | 466.3512 | 0.1134 | 477.865 | 468.805 | 0.1221 | below_opening_15m_low | below_opening_15m_low |
| JCI | data_center_power_cooling | 139.91 |  | 140.4878 | -0.4113 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.835 |  | 170.8664 | -0.0184 | 171.39 | 168.79 | 4.3083 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 292.59 |  | 293.8025 | -0.4127 | 296.46 | 286.91 | 1.4184 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 781.3 |  | 788.3775 | -0.8977 | 790.59 | 767.2 | 2.7429 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 384.32 |  | 387.0563 | -0.707 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 104.42 |  | 105.0996 | -0.6467 | 107.28 | 104.215 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 310.42 |  | 314.2679 | -1.2244 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1741.98 |  | 1754.7754 | -0.7292 | 1797.04 | 1768.805 | 0.0781 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 531.35 |  | 536.7885 | -1.0132 | 554.8 | 543 | 1.2873 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 309.38 |  | 312.3405 | -0.9478 | 324.32 | 319.39 | 3.5102 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 210.505 |  | 212.0137 | -0.7116 | 220.28 | 216.62 | 0.9881 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 338.92 |  | 341.3581 | -0.7142 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.955 |  | 282.2994 | -0.8305 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63 |  | 63.4613 | -0.7269 | 64.96 | 63.98 | 0.0794 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 51.48 |  | 51.5795 | -0.193 | 52.74 | 50.72 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 136.975 |  | 137.5908 | -0.4475 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 327.32 |  | 329.5862 | -0.6876 | 338.1 | 328.505 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 511.54 |  | 513.6567 | -0.4121 | 514.7 | 511.78 | 0.0547 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 296.37 |  | 296.5393 | -0.0571 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.94 |  | 27.8701 | 0.2507 | 28.39 | 27.11 | 0.0716 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 40.75 |  | 39.5544 | 3.0226 | 39.16 | 36.335 | 0.0245 | watch_strength | none |
| CORZ | high_beta_ai_infrastructure | 22.31 |  | 22.3466 | -0.1636 | 22.565 | 21.85 | 0.0448 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1432.115 |  | 1424.9555 | 0.5024 | 1449.57 | 1394.24 | 2.0948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 811.54 |  | 815.6221 | -0.5005 | 830.62 | 811.99 | 2.5507 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 250.65 |  | 251.0849 | -0.1732 | 250.22 | 248.12 | 0.016 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.85 |  | 646.1709 | 0.4146 | 646.57 | 638.875 | 0.467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.37 |  | 272.5342 | 0.3067 | 277.4 | 271.455 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 156.71 |  | 157.8396 | -0.7157 | 163.02 | 159.54 | 0.6892 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
