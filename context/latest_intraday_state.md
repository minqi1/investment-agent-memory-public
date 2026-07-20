# Intraday State

- Generated at: `2026-07-21T03:33:42+08:00`
- Market time ET: `2026-07-20T15:33:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 37, 'manual_confirm_candidate': 2, 'below_vwap': 14, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.235 |  | 700.9983 | -0.3942 | 705.51 | 701.82 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.02 |  | 531.135 | -0.963 | 538.59 | 532.55 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 559.62 |  | 565.3483 | -1.0132 | 572.46 | 567.02 | 0.0447 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 743.19 |  | 744.8679 | -0.2253 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.725 |  | 397.5529 | 1.0494 | 392.89 | 389.74 | 0.0523 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 39.78 |  | 39.6906 | 0.2251 | 39.16 | 36.335 | 0.0503 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IREN | high_beta_ai_infrastructure | 39.78 |  | 39.6906 | 0.2251 | 39.16 | 36.335 | 0.0503 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.61 |  | 296.5033 | 0.036 | 296.26 | 293.84 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MSFT | cloud_ai_capex | 401.725 |  | 397.5529 | 1.0494 | 392.89 | 389.74 | 0.0523 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 650.095 |  | 646.4305 | 0.5669 | 646.57 | 638.875 | 0.4845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TT | data_center_power_cooling | 466.615 |  | 466.4926 | 0.0262 | 477.865 | 468.805 | 0.1886 | below_opening_15m_low | below_opening_15m_low |
| 6 | AMZN | cloud_ai_capex | 250.015 |  | 250.3749 | -0.1438 | 250.2 | 248.195 | 0.016 | below_vwap | below_vwap |
| 7 | GOOGL | cloud_ai_capex | 352.99 |  | 355.1609 | -0.6112 | 358.795 | 350.875 | 0.0652 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | CORZ | high_beta_ai_infrastructure | 22.2 |  | 22.3138 | -0.51 | 22.565 | 21.85 | 0.0901 | below_vwap | below_vwap |
| 10 | LITE | ai_networking_optical | 772.74 |  | 786.5379 | -1.7543 | 790.59 | 767.2 | 0.33 | below_vwap | below_vwap |
| 11 | APLD | high_beta_ai_infrastructure | 27.78 |  | 27.8521 | -0.259 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| 12 | COHR | ai_networking_optical | 287.705 |  | 293.071 | -1.8309 | 296.46 | 286.91 | 0.3198 | below_vwap | below_vwap |
| 13 | CIEN | ai_networking_optical | 379.71 |  | 386.1614 | -1.6707 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LIN | industrial_gases | 513.09 |  | 513.1388 | -0.0095 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 51.31 |  | 51.5484 | -0.4625 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 310.74 |  | 313.7282 | -0.9525 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ANET | ai_networking_optical | 170.29 |  | 170.7068 | -0.2442 | 171.39 | 168.79 | 1.151 | below_vwap | below_vwap,spread_too_wide |
| 18 | AVGO | custom_silicon_networking | 379.12 |  | 380.3459 | -0.3223 | 382.67 | 377.47 | 1.2081 | below_vwap | below_vwap,spread_too_wide |
| 19 | AAPL | mega_cap_platform | 329.67 |  | 326.6444 | 0.9263 | 333.63 | 330.03 | 0.0152 | below_opening_15m_low | below_opening_15m_low |
| 20 | MRVL | custom_silicon_networking | 195 |  | 197.2634 | -1.1474 | 196.86 | 192.09 | 2.7385 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.725 |  | 397.5529 | 1.0494 | 392.89 | 389.74 | 0.0523 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 39.78 |  | 39.6906 | 0.2251 | 39.16 | 36.335 | 0.0503 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.61 |  | 296.5033 | 0.036 | 296.26 | 293.84 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | META | cloud_ai_capex | 650.095 |  | 646.4305 | 0.5669 | 646.57 | 638.875 | 0.4845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 170.29 |  | 170.7068 | -0.2442 | 171.39 | 168.79 | 1.151 | below_vwap | below_vwap,spread_too_wide |
| 6 | AVGO | custom_silicon_networking | 379.12 |  | 380.3459 | -0.3223 | 382.67 | 377.47 | 1.2081 | below_vwap | below_vwap,spread_too_wide |
| 7 | AMZN | cloud_ai_capex | 250.015 |  | 250.3749 | -0.1438 | 250.2 | 248.195 | 0.016 | below_vwap | below_vwap |
| 8 | LITE | ai_networking_optical | 772.74 |  | 786.5379 | -1.7543 | 790.59 | 767.2 | 0.33 | below_vwap | below_vwap |
| 9 | CIEN | ai_networking_optical | 379.71 |  | 386.1614 | -1.6707 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | LIN | industrial_gases | 513.09 |  | 513.1388 | -0.0095 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | GOOGL | cloud_ai_capex | 352.99 |  | 355.1609 | -0.6112 | 358.795 | 350.875 | 0.0652 | below_vwap | below_vwap |
| 13 | COHR | ai_networking_optical | 287.705 |  | 293.071 | -1.8309 | 296.46 | 286.91 | 0.3198 | below_vwap | below_vwap |
| 14 | MRVL | custom_silicon_networking | 195 |  | 197.2634 | -1.1474 | 196.86 | 192.09 | 2.7385 | below_vwap | below_vwap,spread_too_wide |
| 15 | COHU | semiconductor_test_packaging | 51.31 |  | 51.5484 | -0.4625 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 310.74 |  | 313.7282 | -0.9525 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CORZ | high_beta_ai_infrastructure | 22.2 |  | 22.3138 | -0.51 | 22.565 | 21.85 | 0.0901 | below_vwap | below_vwap |
| 18 | APLD | high_beta_ai_infrastructure | 27.78 |  | 27.8521 | -0.259 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| 19 | TT | data_center_power_cooling | 466.615 |  | 466.4926 | 0.0262 | 477.865 | 468.805 | 0.1886 | below_opening_15m_low | below_opening_15m_low |
| 20 | AAPL | mega_cap_platform | 329.67 |  | 326.6444 | 0.9263 | 333.63 | 330.03 | 0.0152 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.235 |  | 700.9983 | -0.3942 | 705.51 | 701.82 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 68.305 |  | 69.1177 | -1.1758 | 70.43 | 69.35 | 0.0293 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 203.21 |  | 205.2223 | -0.9806 | 207.71 | 205.095 | 0.0148 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.725 |  | 397.5529 | 1.0494 | 392.89 | 389.74 | 0.0523 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 329.67 |  | 326.6444 | 0.9263 | 333.63 | 330.03 | 0.0152 | below_opening_15m_low | below_opening_15m_low |
| GOOGL | cloud_ai_capex | 352.99 |  | 355.1609 | -0.6112 | 358.795 | 350.875 | 0.0652 | below_vwap | below_vwap |
| AMD | ai_accelerator | 508.36 |  | 513.7815 | -1.0552 | 522.26 | 510.97 | 2.215 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 402.035 |  | 404.0512 | -0.499 | 409.82 | 405.51 | 0.7711 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.02 |  | 531.135 | -0.963 | 538.59 | 532.55 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 559.62 |  | 565.3483 | -1.0132 | 572.46 | 567.02 | 0.0447 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.12 |  | 380.3459 | -0.3223 | 382.67 | 377.47 | 1.2081 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 864.46 |  | 882.73 | -2.0697 | 898.57 | 878.92 | 3.1696 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 195 |  | 197.2634 | -1.1474 | 196.86 | 192.09 | 2.7385 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 383.15 |  | 389.7553 | -1.6947 | 402.76 | 392.82 | 5.079 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 44.91 |  | 45.505 | -1.3075 | 46.21 | 45.305 | 0.0445 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.02 |  | 24.1656 | -0.6027 | 24.51 | 24.22 | 0.0416 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 743.19 |  | 744.8679 | -0.2253 | 748.69 | 746.87 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 293.02 |  | 293.8397 | -0.279 | 295.97 | 294.88 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 122.18 |  | 122.4086 | -0.1868 | 125.41 | 123.57 | 0.1473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.735 |  | 75.9629 | -2.9328 | 79.23 | 75.17 | 4.4619 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 292.47 |  | 295.4926 | -1.0229 | 300.96 | 297.175 | 0.0718 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 400.255 |  | 403.1492 | -0.7179 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 632.54 |  | 636.6008 | -0.6379 | 644.7 | 636.38 | 0.0964 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1076.85 |  | 1077.4378 | -0.0546 | 1103.11 | 1081.14 | 2.5714 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 466.615 |  | 466.4926 | 0.0262 | 477.865 | 468.805 | 0.1886 | below_opening_15m_low | below_opening_15m_low |
| JCI | data_center_power_cooling | 139.01 |  | 140.1511 | -0.8142 | 143.075 | 141.14 | 3.8415 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 170.29 |  | 170.7068 | -0.2442 | 171.39 | 168.79 | 1.151 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 287.705 |  | 293.071 | -1.8309 | 296.46 | 286.91 | 0.3198 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 772.74 |  | 786.5379 | -1.7543 | 790.59 | 767.2 | 0.33 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 379.71 |  | 386.1614 | -1.6707 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 103.05 |  | 104.6885 | -1.5651 | 107.28 | 104.215 | 5.0752 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 310.74 |  | 313.7282 | -0.9525 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1738.52 |  | 1751.01 | -0.7133 | 1797.04 | 1768.805 | 0.0633 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 527.29 |  | 535.2699 | -1.4908 | 554.8 | 543 | 0.3015 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 307.26 |  | 311.5414 | -1.3742 | 324.32 | 319.39 | 4.1268 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 208.785 |  | 211.2765 | -1.1792 | 220.28 | 216.62 | 0.115 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 334.66 |  | 339.6319 | -1.4639 | 349.43 | 335.335 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 277.76 |  | 281.5357 | -1.3411 | 288.94 | 284 | 4.3059 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.255 |  | 63.2454 | -1.566 | 64.96 | 63.98 | 1.2368 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.31 |  | 51.5484 | -0.4625 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.335 |  | 137.1704 | -2.0671 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 324.49 |  | 328.9696 | -1.3617 | 338.1 | 328.505 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 513.09 |  | 513.1388 | -0.0095 | 514.7 | 511.78 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.61 |  | 296.5033 | 0.036 | 296.26 | 293.84 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.78 |  | 27.8521 | -0.259 | 28.39 | 27.11 | 0.072 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 39.78 |  | 39.6906 | 0.2251 | 39.16 | 36.335 | 0.0503 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.2 |  | 22.3138 | -0.51 | 22.565 | 21.85 | 0.0901 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1384.34 |  | 1420.7569 | -2.5632 | 1449.57 | 1394.24 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 489.59 |  | 498.3973 | -1.7671 | 504.53 | 490.68 | 0.3922 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 807.315 |  | 813.8686 | -0.8052 | 830.62 | 811.99 | 4.4431 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 250.015 |  | 250.3749 | -0.1438 | 250.2 | 248.195 | 0.016 | below_vwap | below_vwap |
| META | cloud_ai_capex | 650.095 |  | 646.4305 | 0.5669 | 646.57 | 638.875 | 0.4845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 269.43 |  | 272.154 | -1.0009 | 277.4 | 271.455 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 152.63 |  | 157.2497 | -2.9378 | 163.02 | 159.54 | 1.1204 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
