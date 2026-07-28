# Intraday State

- Generated at: `2026-07-29T03:13:05+08:00`
- Market time ET: `2026-07-28T15:13:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 13, 'manual_confirm_candidate': 8, 'below_vwap': 7, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.08 |  | 674.2496 | 0.4198 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| SOXX | semiconductor_index | 494.6 |  | 490.0765 | 0.923 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| SMH | semiconductor_index | 532.42 |  | 527.4902 | 0.9346 | 533.01 | 523.325 | 0.0488 | watch_only | none |
| SPY | market_regime | 741.52 |  | 739.6511 | 0.2527 | 739.42 | 736.57 | 0.0108 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.67 |  | 196.1394 | 0.7803 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.13 |  | 387.9391 | 1.3381 | 390.46 | 382.495 | 0.2798 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.52 |  | 739.6511 | 0.2527 | 739.42 | 736.57 | 0.0108 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.28 |  | 331.1508 | 0.945 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 141 |  | 138.8038 | 1.5822 | 139.755 | 137.31 | 0.078 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 121.35 |  | 118.7333 | 2.2038 | 117.17 | 115.25 | 0.0577 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 316.51 |  | 309.0945 | 2.3991 | 315.21 | 304.11 | 0.1295 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 21.1 |  | 20.1542 | 4.693 | 20.97 | 19.755 | 0.0948 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.52 |  | 739.6511 | 0.2527 | 739.42 | 736.57 | 0.0108 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.2 |  | 292.4411 | 0.2595 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 3 | NVDA | ai_accelerator | 197.67 |  | 196.1394 | 0.7803 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 231.25 |  | 230.5331 | 0.311 | 233.05 | 229.7 | 0.0303 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.22 |  | 338.9766 | 0.0718 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 6 | QQQ | market_regime | 677.08 |  | 674.2496 | 0.4198 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| 7 | MRVL | custom_silicon_networking | 175.42 |  | 174.2398 | 0.6773 | 181.24 | 172.395 | 0.2793 | watch_only | none |
| 8 | TSM | foundry | 393.13 |  | 387.9391 | 1.3381 | 390.46 | 382.495 | 0.2798 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 334.28 |  | 331.1508 | 0.945 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 532.42 |  | 527.4902 | 0.9346 | 533.01 | 523.325 | 0.0488 | watch_only | none |
| 11 | SOXX | semiconductor_index | 494.6 |  | 490.0765 | 0.923 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| 12 | HPE | ai_server_oem | 45.11 |  | 44.4745 | 1.429 | 46.19 | 44.33 | 0.0665 | watch_only | none |
| 13 | ASML | semiconductor_equipment | 1590.125 |  | 1577.589 | 0.7946 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 316.51 |  | 309.0945 | 2.3991 | 315.21 | 304.11 | 0.1295 | buy_precheck_manual_confirm | none |
| 15 | VRT | data_center_power_cooling | 268.48 |  | 266.1793 | 0.8643 | 273.86 | 266.04 | 0.2086 | watch_only | none |
| 16 | PWR | data_center_power_cooling | 589.11 |  | 582.7173 | 1.097 | 603.25 | 584.69 | 0.1986 | watch_only | none |
| 17 | KLAC | semiconductor_equipment | 193.435 |  | 190.8579 | 1.3503 | 194.96 | 189.48 | 0.2378 | watch_only | none |
| 18 | CORZ | high_beta_ai_infrastructure | 21.1 |  | 20.1542 | 4.693 | 20.97 | 19.755 | 0.0948 | buy_precheck_manual_confirm | none |
| 19 | JCI | data_center_power_cooling | 141 |  | 138.8038 | 1.5822 | 139.755 | 137.31 | 0.078 | buy_precheck_manual_confirm | none |
| 20 | ARM | ai_accelerator | 246.185 |  | 245.2304 | 0.3893 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.67 |  | 196.1394 | 0.7803 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.13 |  | 387.9391 | 1.3381 | 390.46 | 382.495 | 0.2798 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.52 |  | 739.6511 | 0.2527 | 739.42 | 736.57 | 0.0108 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.28 |  | 331.1508 | 0.945 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 141 |  | 138.8038 | 1.5822 | 139.755 | 137.31 | 0.078 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 121.35 |  | 118.7333 | 2.2038 | 117.17 | 115.25 | 0.0577 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 316.51 |  | 309.0945 | 2.3991 | 315.21 | 304.11 | 0.1295 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 21.1 |  | 20.1542 | 4.693 | 20.97 | 19.755 | 0.0948 | buy_precheck_manual_confirm | none |
| 9 | AVGO | custom_silicon_networking | 383.5 |  | 378.7508 | 1.2539 | 378.64 | 371.57 | 1.8201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ASML | semiconductor_equipment | 1590.125 |  | 1577.589 | 0.7946 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ANET | ai_networking_optical | 169 |  | 165.1676 | 2.3203 | 165.975 | 160.51 | 3.787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ETN | data_center_power_cooling | 387.3 |  | 381.4479 | 1.5342 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SMH | semiconductor_index | 532.42 |  | 527.4902 | 0.9346 | 533.01 | 523.325 | 0.0488 | watch_only | none |
| 14 | SOXX | semiconductor_index | 494.6 |  | 490.0765 | 0.923 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| 15 | QQQ | market_regime | 677.08 |  | 674.2496 | 0.4198 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| 16 | VRT | data_center_power_cooling | 268.48 |  | 266.1793 | 0.8643 | 273.86 | 266.04 | 0.2086 | watch_only | none |
| 17 | PWR | data_center_power_cooling | 589.11 |  | 582.7173 | 1.097 | 603.25 | 584.69 | 0.1986 | watch_only | none |
| 18 | IWM | market_regime | 293.2 |  | 292.4411 | 0.2595 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 19 | KLAC | semiconductor_equipment | 193.435 |  | 190.8579 | 1.3503 | 194.96 | 189.48 | 0.2378 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 231.25 |  | 230.5331 | 0.311 | 233.05 | 229.7 | 0.0303 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.08 |  | 674.2496 | 0.4198 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| TQQQ | leveraged_tool | 61.92 |  | 61.1465 | 1.265 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.67 |  | 196.1394 | 0.7803 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.95 |  | 396.398 | -0.3653 | 400.09 | 392.355 | 0.0329 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.22 |  | 338.9766 | 0.0718 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.28 |  | 331.1508 | 0.945 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 459.37 |  | 455.6293 | 0.821 | 472.485 | 453.76 | 3.1957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.13 |  | 387.9391 | 1.3381 | 390.46 | 382.495 | 0.2798 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 494.6 |  | 490.0765 | 0.923 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| SMH | semiconductor_index | 532.42 |  | 527.4902 | 0.9346 | 533.01 | 523.325 | 0.0488 | watch_only | none |
| AVGO | custom_silicon_networking | 383.5 |  | 378.7508 | 1.2539 | 378.64 | 371.57 | 1.8201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 825.14 |  | 815.8671 | 1.1366 | 846.4 | 813.91 | 1.3331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.42 |  | 174.2398 | 0.6773 | 181.24 | 172.395 | 0.2793 | watch_only | none |
| DELL | ai_server_oem | 390.24 |  | 375.6393 | 3.8869 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.11 |  | 44.4745 | 1.429 | 46.19 | 44.33 | 0.0665 | watch_only | none |
| SMCI | ai_server_oem | 28.45 |  | 28.013 | 1.5599 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 741.52 |  | 739.6511 | 0.2527 | 739.42 | 736.57 | 0.0108 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.2 |  | 292.4411 | 0.2595 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 121.35 |  | 118.7333 | 2.2038 | 117.17 | 115.25 | 0.0577 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.645 |  | 66.2701 | 0.5657 | 68.995 | 65.635 | 2.3558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.48 |  | 266.1793 | 0.8643 | 273.86 | 266.04 | 0.2086 | watch_only | none |
| ETN | data_center_power_cooling | 387.3 |  | 381.4479 | 1.5342 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 589.11 |  | 582.7173 | 1.097 | 603.25 | 584.69 | 0.1986 | watch_only | none |
| GEV | data_center_power_cooling | 936.665 |  | 937.4815 | -0.0871 | 955.825 | 935.665 | 2.7758 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 468.77 |  | 465.4214 | 0.7195 | 477.73 | 460.77 | 0.6528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141 |  | 138.8038 | 1.5822 | 139.755 | 137.31 | 0.078 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169 |  | 165.1676 | 2.3203 | 165.975 | 160.51 | 3.787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 243.65 |  | 237.7669 | 2.4743 | 256.145 | 236.73 | 0.4309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 648.75 |  | 632.5304 | 2.5642 | 673.65 | 624.91 | 4.2975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 344.35 |  | 337.5798 | 2.0055 | 354.09 | 338.14 | 0.8683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.82 |  | 85.887 | 2.2506 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 262.12 |  | 259.2529 | 1.1059 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1590.125 |  | 1577.589 | 0.7946 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 481.3 |  | 476.4791 | 1.0118 | 494.87 | 477.03 | 0.3906 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 273.2 |  | 266.9059 | 2.3582 | 276.85 | 267.14 | 4.1215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.435 |  | 190.8579 | 1.3503 | 194.96 | 189.48 | 0.2378 | watch_only | none |
| TER | semiconductor_test_packaging | 316.51 |  | 309.0945 | 2.3991 | 315.21 | 304.11 | 0.1295 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 240.56 |  | 237.1033 | 1.4579 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.47 |  | 46.6693 | -0.4271 | 51.64 | 47.435 | 3.4861 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.705 |  | 42.4434 | 0.6164 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.6 |  | 119.1752 | 0.3564 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 285.55 |  | 282.4417 | 1.1005 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 515.655 |  | 518.0219 | -0.4569 | 518.6 | 511.495 | 0.1474 | below_vwap | below_vwap |
| APD | industrial_gases | 295.155 |  | 295.7379 | -0.1971 | 297.25 | 293.555 | 4.2791 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.39 |  | 26.5103 | -0.4538 | 27 | 25.42 | 0.1137 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.56 |  | 33.7049 | -0.4299 | 35.08 | 33.52 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.1 |  | 20.1542 | 4.693 | 20.97 | 19.755 | 0.0948 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1116.33 |  | 1099.5063 | 1.5301 | 1185.19 | 1114.57 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 458.74 |  | 440.8673 | 4.054 | 465.04 | 435.22 | 3.2502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 747.2 |  | 733.0849 | 1.9254 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.25 |  | 230.5331 | 0.311 | 233.05 | 229.7 | 0.0303 | watch_only | none |
| META | cloud_ai_capex | 593.84 |  | 593.852 | -0.002 | 600.765 | 594.21 | 0.0269 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 246.185 |  | 245.2304 | 0.3893 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.11 |  | 131.5276 | 0.4428 | 136.45 | 131.735 | 0.5601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
