# Intraday State

- Generated at: `2026-07-21T02:36:23+08:00`
- Market time ET: `2026-07-20T14:36:23-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 30, 'manual_confirm_candidate': 2, 'below_vwap': 20, 'price_stale_or_missing': 1, 'watch_only': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.94 |  | 701.5302 | -0.3692 | 705.51 | 701.82 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.39 |  | 532.6163 | -0.7935 | 538.59 | 532.55 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 561.95 |  | 566.09 | -0.7313 | 572.46 | 567.02 | 0.0676 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 743.66 |  | 745.4501 | -0.2401 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.81 |  | 396.9092 | 1.2347 | 392.89 | 389.74 | 0.0149 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.675 |  | 39.6244 | 2.6515 | 39.16 | 36.335 | 0.0492 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 24.3 |  | 24.1759 | 0.5131 | 24.51 | 24.22 | 0.0412 | watch_only | none |
| 2 | MSFT | cloud_ai_capex | 401.81 |  | 396.9092 | 1.2347 | 392.89 | 389.74 | 0.0149 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.625 |  | 296.5409 | 0.0284 | 296.26 | 293.84 | 5.0333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | META | cloud_ai_capex | 648.16 |  | 646.2668 | 0.2929 | 646.57 | 638.875 | 1.9625 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | IREN | high_beta_ai_infrastructure | 40.675 |  | 39.6244 | 2.6515 | 39.16 | 36.335 | 0.0492 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 326.455 |  | 326.4164 | 0.0118 | 333.63 | 330.03 | 0.0368 | below_opening_15m_low | below_opening_15m_low |
| 7 | GEV | data_center_power_cooling | 1079.64 |  | 1077.627 | 0.1868 | 1103.11 | 1081.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 8 | AMZN | cloud_ai_capex | 249.91 |  | 250.5391 | -0.2511 | 250.2 | 248.195 | 0.028 | below_vwap | below_vwap |
| 9 | HPE | ai_server_oem | 45.305 |  | 45.6184 | -0.687 | 46.21 | 45.305 | 0.0441 | below_vwap | below_vwap |
| 10 | ANET | ai_networking_optical | 170.47 |  | 170.8515 | -0.2233 | 171.39 | 168.79 | 0.2816 | below_vwap | below_vwap |
| 11 | TT | data_center_power_cooling | 466.82 |  | 466.3855 | 0.0932 | 477.865 | 468.805 | 4.4128 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | CORZ | high_beta_ai_infrastructure | 22.25 |  | 22.3443 | -0.4219 | 22.565 | 21.85 | 0.0899 | below_vwap | below_vwap |
| 14 | APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8727 | -0.2967 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| 15 | GOOGL | cloud_ai_capex | 351.53 |  | 356.1214 | -1.2893 | 358.795 | 350.875 | 0.1707 | below_vwap | below_vwap |
| 16 | CIEN | ai_networking_optical | 382.24 |  | 386.9795 | -1.2247 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LIN | industrial_gases | 512.28 |  | 513.3739 | -0.2131 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | TER | semiconductor_test_packaging | 336.185 |  | 341.1847 | -1.4654 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHU | semiconductor_test_packaging | 51.44 |  | 51.5762 | -0.2641 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 379.99 |  | 380.4929 | -0.1322 | 382.67 | 377.47 | 0.8579 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.81 |  | 396.9092 | 1.2347 | 392.89 | 389.74 | 0.0149 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 40.675 |  | 39.6244 | 2.6515 | 39.16 | 36.335 | 0.0492 | buy_precheck_manual_confirm | none |
| 3 | MRVL | custom_silicon_networking | 196.88 |  | 197.4079 | -0.2674 | 196.86 | 192.09 | 0.7873 | below_vwap | below_vwap,spread_too_wide |
| 4 | APD | industrial_gases | 296.625 |  | 296.5409 | 0.0284 | 296.26 | 293.84 | 5.0333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | META | cloud_ai_capex | 648.16 |  | 646.2668 | 0.2929 | 646.57 | 638.875 | 1.9625 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SMCI | ai_server_oem | 24.3 |  | 24.1759 | 0.5131 | 24.51 | 24.22 | 0.0412 | watch_only | none |
| 7 | ANET | ai_networking_optical | 170.47 |  | 170.8515 | -0.2233 | 171.39 | 168.79 | 0.2816 | below_vwap | below_vwap |
| 8 | AVGO | custom_silicon_networking | 379.99 |  | 380.4929 | -0.1322 | 382.67 | 377.47 | 0.8579 | below_vwap | below_vwap,spread_too_wide |
| 9 | AMD | ai_accelerator | 513.7 |  | 514.3265 | -0.1218 | 522.26 | 510.97 | 2.2367 | below_vwap | below_vwap,spread_too_wide |
| 10 | AMZN | cloud_ai_capex | 249.91 |  | 250.5391 | -0.2511 | 250.2 | 248.195 | 0.028 | below_vwap | below_vwap |
| 11 | WDC | memory_hbm_storage | 491.53 |  | 499.5445 | -1.6044 | 504.53 | 490.68 | 2.5248 | below_vwap | below_vwap,spread_too_wide |
| 12 | LITE | ai_networking_optical | 773.51 |  | 787.5452 | -1.7821 | 790.59 | 767.2 | 3.4686 | below_vwap | below_vwap,spread_too_wide |
| 13 | CIEN | ai_networking_optical | 382.24 |  | 386.9795 | -1.2247 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | HPE | ai_server_oem | 45.305 |  | 45.6184 | -0.687 | 46.21 | 45.305 | 0.0441 | below_vwap | below_vwap |
| 15 | LIN | industrial_gases | 512.28 |  | 513.3739 | -0.2131 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 271.54 |  | 272.5261 | -0.3618 | 277.4 | 271.455 | 1.5283 | below_vwap | below_vwap,spread_too_wide |
| 18 | GOOGL | cloud_ai_capex | 351.53 |  | 356.1214 | -1.2893 | 358.795 | 350.875 | 0.1707 | below_vwap | below_vwap |
| 19 | TER | semiconductor_test_packaging | 336.185 |  | 341.1847 | -1.4654 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 291.095 |  | 293.698 | -0.8863 | 296.46 | 286.91 | 2.6795 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.94 |  | 701.5302 | -0.3692 | 705.51 | 701.82 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 68.44 |  | 69.2623 | -1.1872 | 70.43 | 69.35 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 203.935 |  | 205.5272 | -0.7747 | 207.71 | 205.095 | 0.0147 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.81 |  | 396.9092 | 1.2347 | 392.89 | 389.74 | 0.0149 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 326.455 |  | 326.4164 | 0.0118 | 333.63 | 330.03 | 0.0368 | below_opening_15m_low | below_opening_15m_low |
| GOOGL | cloud_ai_capex | 351.53 |  | 356.1214 | -1.2893 | 358.795 | 350.875 | 0.1707 | below_vwap | below_vwap |
| AMD | ai_accelerator | 513.7 |  | 514.3265 | -0.1218 | 522.26 | 510.97 | 2.2367 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 401.96 |  | 404.5646 | -0.6438 | 409.82 | 405.51 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.39 |  | 532.6163 | -0.7935 | 538.59 | 532.55 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 561.95 |  | 566.09 | -0.7313 | 572.46 | 567.02 | 0.0676 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.99 |  | 380.4929 | -0.1322 | 382.67 | 377.47 | 0.8579 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 873.45 |  | 885.6376 | -1.3761 | 898.57 | 878.92 | 0.4202 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 196.88 |  | 197.4079 | -0.2674 | 196.86 | 192.09 | 0.7873 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 386.69 |  | 390.9594 | -1.092 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.305 |  | 45.6184 | -0.687 | 46.21 | 45.305 | 0.0441 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.3 |  | 24.1759 | 0.5131 | 24.51 | 24.22 | 0.0412 | watch_only | none |
| SPY | market_regime | 743.66 |  | 745.4501 | -0.2401 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 293.29 |  | 294.0543 | -0.2599 | 295.97 | 294.88 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 123.365 |  | 122.3749 | 0.8091 | 125.41 | 123.57 | 0.1135 | below_opening_15m_low | below_opening_15m_low |
| CRWV | gpu_cloud_ai_factory | 74.355 |  | 76.2965 | -2.5447 | 79.23 | 75.17 | 3.4295 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.335 |  | 295.9888 | -0.8966 | 300.96 | 297.175 | 3.9273 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 402.27 |  | 403.7774 | -0.3733 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 634.62 |  | 637.3111 | -0.4223 | 644.7 | 636.38 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1079.64 |  | 1077.627 | 0.1868 | 1103.11 | 1081.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 466.82 |  | 466.3855 | 0.0932 | 477.865 | 468.805 | 4.4128 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 139.82 |  | 140.4548 | -0.4519 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.47 |  | 170.8515 | -0.2233 | 171.39 | 168.79 | 0.2816 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 291.095 |  | 293.698 | -0.8863 | 296.46 | 286.91 | 2.6795 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 773.51 |  | 787.5452 | -1.7821 | 790.59 | 767.2 | 3.4686 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 382.24 |  | 386.9795 | -1.2247 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 103.42 |  | 105.0259 | -1.5291 | 107.28 | 104.215 | 0.4061 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 312.23 |  | 314.1608 | -0.6146 | 322.065 | 308.955 | 4.2917 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1734.59 |  | 1754.0093 | -1.1071 | 1797.04 | 1768.805 | 0.143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 528.18 |  | 536.4612 | -1.5437 | 554.8 | 543 | 0.7914 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 306.86 |  | 312.1806 | -1.7043 | 324.32 | 319.39 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 209.24 |  | 211.8966 | -1.2537 | 220.28 | 216.62 | 0.3584 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 336.185 |  | 341.1847 | -1.4654 | 349.43 | 335.335 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.235 |  | 281.9109 | -0.5945 | 288.94 | 284 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.69 |  | 63.435 | -1.1744 | 64.96 | 63.98 | 3.6529 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.44 |  | 51.5762 | -0.2641 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 136.08 |  | 137.5442 | -1.0645 | 141.89 | 138.545 | 5.1146 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 325.03 |  | 329.4077 | -1.329 | 338.1 | 328.505 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 512.28 |  | 513.3739 | -0.2131 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.625 |  | 296.5409 | 0.0284 | 296.26 | 293.84 | 5.0333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8727 | -0.2967 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.675 |  | 39.6244 | 2.6515 | 39.16 | 36.335 | 0.0492 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.25 |  | 22.3443 | -0.4219 | 22.565 | 21.85 | 0.0899 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1412.2 |  | 1424.9099 | -0.892 | 1449.57 | 1394.24 | 1.4651 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 491.53 |  | 499.5445 | -1.6044 | 504.53 | 490.68 | 2.5248 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 806.89 |  | 815.3461 | -1.0371 | 830.62 | 811.99 | 3.0958 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 249.91 |  | 250.5391 | -0.2511 | 250.2 | 248.195 | 0.028 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.16 |  | 646.2668 | 0.2929 | 646.57 | 638.875 | 1.9625 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.54 |  | 272.5261 | -0.3618 | 277.4 | 271.455 | 1.5283 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.23 |  | 157.7618 | -1.6048 | 163.02 | 159.54 | 1.2304 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
