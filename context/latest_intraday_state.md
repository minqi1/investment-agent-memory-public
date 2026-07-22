# Intraday State

- Generated at: `2026-07-23T02:29:51+08:00`
- Market time ET: `2026-07-22T14:29:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'manual_confirm_candidate': 11, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.23 |  | 707.4793 | -0.0352 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.99 |  | 553.4335 | 0.8233 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.78 |  | 586.0128 | 0.6428 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.51 |  | 748.522 | -0.0016 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.76 |  | 211.4593 | 1.088 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 554.23 |  | 551.8028 | 0.4399 | 548.755 | 526.6 | 0.1804 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 556.21 |  | 556.1907 | 0.0035 | 548.14 | 526.22 | 0.0755 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.99 |  | 553.4335 | 0.8233 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.78 |  | 586.0128 | 0.6428 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.52 |  | 211.4263 | 0.5173 | 207.06 | 202.18 | 0.2494 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 372.005 |  | 371.6681 | 0.0907 | 369.53 | 365 | 0.1667 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 396.925 |  | 391.5848 | 1.3637 | 387.635 | 380.205 | 0.0731 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 301.775 |  | 299.3555 | 0.8082 | 297.69 | 293.905 | 0.0663 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 644.385 |  | 641.2597 | 0.4874 | 641.19 | 628.17 | 0.1769 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 70.87 |  | 70.8641 | 0.0083 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | WDC | memory_hbm_storage | 556.21 |  | 556.1907 | 0.0035 | 548.14 | 526.22 | 0.0755 | buy_precheck_manual_confirm | none |
| 2 | TER | semiconductor_test_packaging | 372.005 |  | 371.6681 | 0.0907 | 369.53 | 365 | 0.1667 | buy_precheck_manual_confirm | none |
| 3 | ANET | ai_networking_optical | 175.22 |  | 174.9282 | 0.1668 | 175.265 | 171.06 | 0.0685 | watch_only | none |
| 4 | SMH | semiconductor_index | 589.78 |  | 586.0128 | 0.6428 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 5 | PWR | data_center_power_cooling | 644.385 |  | 641.2597 | 0.4874 | 641.19 | 628.17 | 0.1769 | buy_precheck_manual_confirm | none |
| 6 | AMD | ai_accelerator | 554.23 |  | 551.8028 | 0.4399 | 548.755 | 526.6 | 0.1804 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 212.52 |  | 211.4263 | 0.5173 | 207.06 | 202.18 | 0.2494 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 474.465 |  | 473.82 | 0.1361 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SOXX | semiconductor_index | 557.99 |  | 553.4335 | 0.8233 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 301.775 |  | 299.3555 | 0.8082 | 297.69 | 293.905 | 0.0663 | buy_precheck_manual_confirm | none |
| 11 | NVDA | ai_accelerator | 213.76 |  | 211.4593 | 1.088 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | JCI | data_center_power_cooling | 143.165 |  | 142.9572 | 0.1454 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 138.89 |  | 138.8736 | 0.0118 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 295.41 |  | 295.369 | 0.0139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APD | industrial_gases | 298.47 |  | 297.8376 | 0.2123 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AVGO | custom_silicon_networking | 396.925 |  | 391.5848 | 1.3637 | 387.635 | 380.205 | 0.0731 | buy_precheck_manual_confirm | none |
| 17 | AMAT | semiconductor_equipment | 560.51 |  | 558.7105 | 0.3221 | 559.22 | 544.305 | 2.9955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SKHY | memory_hbm_storage | 166.91 |  | 166.7413 | 0.1012 | 166.63 | 162.08 | 1.4319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MU | memory_hbm_storage | 969.97 |  | 968.5319 | 0.1485 | 963.41 | 936.99 | 1.0856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TSM | foundry | 422.06 |  | 420.8778 | 0.2809 | 419.42 | 414.87 | 0.3507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.76 |  | 211.4593 | 1.088 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 554.23 |  | 551.8028 | 0.4399 | 548.755 | 526.6 | 0.1804 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 556.21 |  | 556.1907 | 0.0035 | 548.14 | 526.22 | 0.0755 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.99 |  | 553.4335 | 0.8233 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.78 |  | 586.0128 | 0.6428 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.52 |  | 211.4263 | 0.5173 | 207.06 | 202.18 | 0.2494 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 372.005 |  | 371.6681 | 0.0907 | 369.53 | 365 | 0.1667 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 396.925 |  | 391.5848 | 1.3637 | 387.635 | 380.205 | 0.0731 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 301.775 |  | 299.3555 | 0.8082 | 297.69 | 293.905 | 0.0663 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 644.385 |  | 641.2597 | 0.4874 | 641.19 | 628.17 | 0.1769 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 70.87 |  | 70.8641 | 0.0083 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 12 | STX | memory_hbm_storage | 906.6 |  | 909.6028 | -0.3301 | 899.59 | 860.605 | 0.1313 | below_vwap | below_vwap |
| 13 | QQQ | market_regime | 707.23 |  | 707.4793 | -0.0352 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 748.51 |  | 748.522 | -0.0016 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 15 | DELL | ai_server_oem | 440.61 |  | 442.4294 | -0.4112 | 435.98 | 415.79 | 2.004 | below_vwap | below_vwap,spread_too_wide |
| 16 | AMKR | semiconductor_test_packaging | 67.3 |  | 67.4736 | -0.2573 | 66.73 | 64.98 | 0.0594 | below_vwap | below_vwap |
| 17 | SMCI | ai_server_oem | 31.04 |  | 31.1636 | -0.3966 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| 18 | MU | memory_hbm_storage | 969.97 |  | 968.5319 | 0.1485 | 963.41 | 936.99 | 1.0856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TSM | foundry | 422.06 |  | 420.8778 | 0.2809 | 419.42 | 414.87 | 0.3507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 474.465 |  | 473.82 | 0.1361 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.23 |  | 707.4793 | -0.0352 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.87 |  | 70.8641 | 0.0083 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.76 |  | 211.4593 | 1.088 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.37 |  | 389.9149 | -0.3962 | 400.89 | 392.26 | 0.0438 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.955 |  | 325.0171 | -0.3268 | 328.865 | 325.74 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.59 |  | 347.8626 | -0.3658 | 348.76 | 346.23 | 0.0317 | below_vwap | below_vwap |
| AMD | ai_accelerator | 554.23 |  | 551.8028 | 0.4399 | 548.755 | 526.6 | 0.1804 | buy_precheck_manual_confirm | none |
| TSM | foundry | 422.06 |  | 420.8778 | 0.2809 | 419.42 | 414.87 | 0.3507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.99 |  | 553.4335 | 0.8233 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.78 |  | 586.0128 | 0.6428 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.925 |  | 391.5848 | 1.3637 | 387.635 | 380.205 | 0.0731 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 969.97 |  | 968.5319 | 0.1485 | 963.41 | 936.99 | 1.0856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.52 |  | 211.4263 | 0.5173 | 207.06 | 202.18 | 0.2494 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 440.61 |  | 442.4294 | -0.4112 | 435.98 | 415.79 | 2.004 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.46 |  | 48.997 | -1.096 | 48.96 | 47.01 | 0.0413 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.04 |  | 31.1636 | -0.3966 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 748.51 |  | 748.522 | -0.0016 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 294.27 |  | 295.0197 | -0.2541 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.995 |  | 126.5747 | -1.248 | 128.79 | 125.83 | 0.776 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.635 |  | 83.4396 | -0.9643 | 83.22 | 79.6 | 2.9043 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.775 |  | 299.3555 | 0.8082 | 297.69 | 293.905 | 0.0663 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.545 |  | 407.8779 | -0.0816 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.385 |  | 641.2597 | 0.4874 | 641.19 | 628.17 | 0.1769 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 994.775 |  | 1005.2525 | -1.0423 | 1036.605 | 998.94 | 3.5184 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.465 |  | 473.82 | 0.1361 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.165 |  | 142.9572 | 0.1454 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.22 |  | 174.9282 | 0.1668 | 175.265 | 171.06 | 0.0685 | watch_only | none |
| COHR | ai_networking_optical | 315.15 |  | 316.058 | -0.2873 | 317.93 | 306.89 | 2.6654 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 825.97 |  | 838.764 | -1.5253 | 840.47 | 814.62 | 0.2361 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 402.475 |  | 405.4117 | -0.7244 | 407.12 | 397.835 | 1.933 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.15 |  | 114.1932 | -2.665 | 117.185 | 113.68 | 3.9586 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 331.205 |  | 329.7819 | 0.4315 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1802.14 |  | 1798.9052 | 0.1798 | 1786.525 | 1767.54 | 2.6441 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.51 |  | 558.7105 | 0.3221 | 559.22 | 544.305 | 2.9955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.42 |  | 319.4209 | 0.6259 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.26 |  | 216.1338 | 0.0584 | 215.465 | 210.975 | 4.3744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.005 |  | 371.6681 | 0.0907 | 369.53 | 365 | 0.1667 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 295.41 |  | 295.369 | 0.0139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.3 |  | 67.4736 | -0.2573 | 66.73 | 64.98 | 0.0594 | below_vwap | below_vwap |
| COHU | semiconductor_test_packaging | 55.425 |  | 55.6716 | -0.4429 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.89 |  | 138.8736 | 0.0118 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 348.16 |  | 344.5936 | 1.035 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.11 |  | 507.3339 | 0.5472 | 507.545 | 505.59 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| APD | industrial_gases | 298.47 |  | 297.8376 | 0.2123 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.11 |  | 30.7211 | -1.9893 | 30.78 | 29.46 | 0.1661 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.57 |  | 42.5486 | -2.3 | 42.29 | 40.305 | 0.0481 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.64 |  | 24.0173 | -1.5708 | 24.255 | 23.58 | 0.0423 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1596.88 |  | 1581.205 | 0.9913 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 556.21 |  | 556.1907 | 0.0035 | 548.14 | 526.22 | 0.0755 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 906.6 |  | 909.6028 | -0.3301 | 899.59 | 860.605 | 0.1313 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 243.08 |  | 244.2334 | -0.4722 | 248.43 | 244.47 | 0.3291 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.75 |  | 630.6589 | -0.6198 | 647.02 | 632.77 | 0.2888 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.98 |  | 285.5987 | -0.2166 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.91 |  | 166.7413 | 0.1012 | 166.63 | 162.08 | 1.4319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
