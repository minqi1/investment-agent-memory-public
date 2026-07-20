# Intraday State

- Generated at: `2026-07-21T00:07:35+08:00`
- Market time ET: `2026-07-20T12:07:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `56`
- stale_count: `0`
- coverage_price: `50`
- coverage_vwap: `50`
- caution_counts: `{'spread_too_wide_or_missing': 12, 'watch_only': 7, 'below_vwap': 15, 'manual_confirm_candidate': 3, 'below_opening_15m_low': 19}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 702.54 |  | 701.7212 | 0.1167 | 705.51 | 701.82 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SOXX | semiconductor_index | 534.3 |  | 533.2049 | 0.2054 | 538.59 | 532.55 | 0.0524 | watch_only | none |
| SMH | semiconductor_index | 567.01 |  | 567.0259 | -0.0028 | 572.46 | 567.02 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 746.19 |  | 745.8395 | 0.047 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.12 |  | 394.0479 | 1.2872 | 392.89 | 389.74 | 0.0401 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 647.59 |  | 643.7917 | 0.59 | 646.57 | 638.875 | 0.3351 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 39.93 |  | 38.9645 | 2.4779 | 39.16 | 36.335 | 0.0751 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 170.91 |  | 170.9018 | 0.0048 | 171.39 | 168.79 | 0.1229 | watch_only | none |
| 2 | SOXX | semiconductor_index | 534.3 |  | 533.2049 | 0.2054 | 538.59 | 532.55 | 0.0524 | watch_only | none |
| 3 | HPE | ai_server_oem | 45.845 |  | 45.6885 | 0.3424 | 46.21 | 45.305 | 0.0873 | watch_only | none |
| 4 | META | cloud_ai_capex | 647.59 |  | 643.7917 | 0.59 | 646.57 | 638.875 | 0.3351 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.41 |  | 22.3759 | 0.1525 | 22.565 | 21.85 | 0.0446 | watch_only | none |
| 6 | APLD | high_beta_ai_infrastructure | 27.95 |  | 27.8673 | 0.2968 | 28.39 | 27.11 | 0.0716 | watch_only | none |
| 7 | AMD | ai_accelerator | 514.93 |  | 514.8607 | 0.0135 | 522.26 | 510.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | QQQ | market_regime | 702.54 |  | 701.7212 | 0.1167 | 705.51 | 701.82 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | MSFT | cloud_ai_capex | 399.12 |  | 394.0479 | 1.2872 | 392.89 | 389.74 | 0.0401 | buy_precheck_manual_confirm | none |
| 10 | AAOI | ai_networking_optical | 105.4 |  | 105.2486 | 0.1439 | 107.28 | 104.215 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MU | memory_hbm_storage | 892.725 |  | 883.3527 | 1.061 | 898.57 | 878.92 | 0.2005 | watch_only | none |
| 12 | AMZN | cloud_ai_capex | 251.99 |  | 250.0307 | 0.7836 | 250.2 | 248.195 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | WDC | memory_hbm_storage | 500.585 |  | 500.1312 | 0.0907 | 504.53 | 490.68 | 0.3915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | LITE | ai_networking_optical | 790.36 |  | 788.7354 | 0.206 | 790.59 | 767.2 | 1.4753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 387.995 |  | 387.1076 | 0.2292 | 393.855 | 377.005 | 4.8171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 381.96 |  | 379.8072 | 0.5668 | 382.67 | 377.47 | 0.6467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SPY | market_regime | 746.19 |  | 745.8395 | 0.047 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 18 | IREN | high_beta_ai_infrastructure | 39.93 |  | 38.9645 | 2.4779 | 39.16 | 36.335 | 0.0751 | buy_precheck_manual_confirm | none |
| 19 | COHR | ai_networking_optical | 295.785 |  | 293.8185 | 0.6693 | 296.46 | 286.91 | 1.2239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ORCL | cloud_ai_capex | 122.185 |  | 122.1641 | 0.0171 | 125.41 | 123.57 | 0.0491 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.12 |  | 394.0479 | 1.2872 | 392.89 | 389.74 | 0.0401 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 647.59 |  | 643.7917 | 0.59 | 646.57 | 638.875 | 0.3351 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 39.93 |  | 38.9645 | 2.4779 | 39.16 | 36.335 | 0.0751 | buy_precheck_manual_confirm | none |
| 4 | APD | industrial_gases | 296.49 |  | 296.7249 | -0.0792 | 296.26 | 293.84 | 0.1315 | below_vwap | below_vwap |
| 5 | AMZN | cloud_ai_capex | 251.99 |  | 250.0307 | 0.7836 | 250.2 | 248.195 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 170.91 |  | 170.9018 | 0.0048 | 171.39 | 168.79 | 0.1229 | watch_only | none |
| 7 | MRVL | custom_silicon_networking | 200.7 |  | 196.6991 | 2.034 | 196.86 | 192.09 | 0.4833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | MU | memory_hbm_storage | 892.725 |  | 883.3527 | 1.061 | 898.57 | 878.92 | 0.2005 | watch_only | none |
| 9 | SOXX | semiconductor_index | 534.3 |  | 533.2049 | 0.2054 | 538.59 | 532.55 | 0.0524 | watch_only | none |
| 10 | HPE | ai_server_oem | 45.845 |  | 45.6885 | 0.3424 | 46.21 | 45.305 | 0.0873 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 22.41 |  | 22.3759 | 0.1525 | 22.565 | 21.85 | 0.0446 | watch_only | none |
| 12 | APLD | high_beta_ai_infrastructure | 27.95 |  | 27.8673 | 0.2968 | 28.39 | 27.11 | 0.0716 | watch_only | none |
| 13 | TQQQ | leveraged_tool | 69.5 |  | 69.3176 | 0.2632 | 70.43 | 69.35 | 0.0144 | watch_only | none |
| 14 | NVDA | ai_accelerator | 205.95 |  | 205.9858 | -0.0174 | 207.71 | 205.095 | 0.0194 | below_vwap | below_vwap |
| 15 | KLAC | semiconductor_equipment |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | IWM | market_regime |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | STX | memory_hbm_storage | 812.15 |  | 818.7888 | -0.8108 | 830.62 | 811.99 | 1.7669 | below_vwap | below_vwap,spread_too_wide |
| 18 | LIN | industrial_gases | 514.04 |  | 514.7341 | -0.1348 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 702.54 |  | 701.7212 | 0.1167 | 705.51 | 701.82 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TQQQ | leveraged_tool | 69.5 |  | 69.3176 | 0.2632 | 70.43 | 69.35 | 0.0144 | watch_only | none |
| NVDA | ai_accelerator | 205.95 |  | 205.9858 | -0.0174 | 207.71 | 205.095 | 0.0194 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 399.12 |  | 394.0479 | 1.2872 | 392.89 | 389.74 | 0.0401 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 325.49 |  | 327.4309 | -0.5928 | 333.63 | 330.03 | 0.0369 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 355.975 |  | 357.3647 | -0.3889 | 358.795 | 350.875 | 0.2697 | below_vwap | below_vwap |
| AMD | ai_accelerator | 514.93 |  | 514.8607 | 0.0135 | 522.26 | 510.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TSM | foundry | 404.515 |  | 404.6558 | -0.0348 | 409.82 | 405.51 | 0.0939 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.3 |  | 533.2049 | 0.2054 | 538.59 | 532.55 | 0.0524 | watch_only | none |
| SMH | semiconductor_index | 567.01 |  | 567.0259 | -0.0028 | 572.46 | 567.02 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.96 |  | 379.8072 | 0.5668 | 382.67 | 377.47 | 0.6467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 892.725 |  | 883.3527 | 1.061 | 898.57 | 878.92 | 0.2005 | watch_only | none |
| MRVL | custom_silicon_networking | 200.7 |  | 196.6991 | 2.034 | 196.86 | 192.09 | 0.4833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 388.96 |  | 392.0476 | -0.7876 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.845 |  | 45.6885 | 0.3424 | 46.21 | 45.305 | 0.0873 | watch_only | none |
| SMCI | ai_server_oem |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SPY | market_regime | 746.19 |  | 745.8395 | 0.047 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| ORCL | cloud_ai_capex | 122.185 |  | 122.1641 | 0.0171 | 125.41 | 123.57 | 0.0491 | below_opening_15m_low | below_opening_15m_low |
| CRWV | gpu_cloud_ai_factory |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 295.26 |  | 296.4969 | -0.4172 | 300.96 | 297.175 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 402.31 |  | 404.5346 | -0.5499 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 634.82 |  | 638.0897 | -0.5124 | 644.7 | 636.38 | 0.1906 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1062.56 |  | 1079.9981 | -1.6146 | 1103.11 | 1081.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 465.03 |  | 466.1664 | -0.2438 | 477.865 | 468.805 | 4.8126 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 139.77 |  | 140.856 | -0.771 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.91 |  | 170.9018 | 0.0048 | 171.39 | 168.79 | 0.1229 | watch_only | none |
| COHR | ai_networking_optical | 295.785 |  | 293.8185 | 0.6693 | 296.46 | 286.91 | 1.2239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 790.36 |  | 788.7354 | 0.206 | 790.59 | 767.2 | 1.4753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 387.995 |  | 387.1076 | 0.2292 | 393.855 | 377.005 | 4.8171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 105.4 |  | 105.2486 | 0.1439 | 107.28 | 104.215 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 318.67 |  | 314.9924 | 1.1675 | 322.065 | 308.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1743.99 |  | 1758.2689 | -0.8121 | 1797.04 | 1768.805 | 0.0935 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 534.77 |  | 539.3223 | -0.8441 | 554.8 | 543 | 0.2225 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 312.3 |  | 313.1201 | -0.2619 | 324.32 | 319.39 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 340.24 |  | 342.6293 | -0.6974 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.42 |  | 283.4994 | -1.4389 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.14 |  | 63.5861 | -0.7015 | 64.96 | 63.98 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.395 |  | 51.3968 | -0.0036 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 137.365 |  | 137.7142 | -0.2536 | 141.89 | 138.545 | 4.0986 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 329.95 |  | 330.6855 | -0.2224 | 338.1 | 328.505 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 514.04 |  | 514.7341 | -0.1348 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.49 |  | 296.7249 | -0.0792 | 296.26 | 293.84 | 0.1315 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 27.95 |  | 27.8673 | 0.2968 | 28.39 | 27.11 | 0.0716 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.93 |  | 38.9645 | 2.4779 | 39.16 | 36.335 | 0.0751 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.41 |  | 22.3759 | 0.1525 | 22.565 | 21.85 | 0.0446 | watch_only | none |
| SNDK | memory_hbm_storage | 1431.76 |  | 1420.0469 | 0.8248 | 1449.57 | 1394.24 | 0.9632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 500.585 |  | 500.1312 | 0.0907 | 504.53 | 490.68 | 0.3915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 812.15 |  | 818.7888 | -0.8108 | 830.62 | 811.99 | 1.7669 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 251.99 |  | 250.0307 | 0.7836 | 250.2 | 248.195 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| META | cloud_ai_capex | 647.59 |  | 643.7917 | 0.59 | 646.57 | 638.875 | 0.3351 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 272.1 |  | 272.4444 | -0.1264 | 277.4 | 271.455 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 158.535 |  | 158.1203 | 0.2623 | 163.02 | 159.54 | 1.4634 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
