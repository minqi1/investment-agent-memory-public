# Intraday State

- Generated at: `2026-07-18T01:55:09+08:00`
- Market time ET: `2026-07-17T13:55:10-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'watch_only': 1, 'below_opening_15m_low': 3, 'below_vwap': 4, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.24 |  | 695.332 | 0.562 | 693.36 | 686.78 | 0.0543 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 528.355 |  | 517.7999 | 2.0385 | 511.83 | 498.665 | 0.0719 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 562.3 |  | 554.6401 | 1.3811 | 550 | 536.9 | 0.0658 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.92 |  | 745.0082 | -0.0118 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 205.04 |  | 203.2035 | 0.9038 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 400.76 |  | 398.097 | 0.6689 | 394.11 | 386.02 | 0.1822 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 562.3 |  | 554.6401 | 1.3811 | 550 | 536.9 | 0.0658 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 528.355 |  | 517.7999 | 2.0385 | 511.83 | 498.665 | 0.0719 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.59 |  | 294.2091 | 0.1295 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1062.44 |  | 1043.8513 | 1.7808 | 1001.82 | 982.21 | 0.3097 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 699.24 |  | 695.332 | 0.562 | 693.36 | 686.78 | 0.0543 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.52 |  | 45.5927 | 2.0339 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 192.235 |  | 186.9125 | 2.8476 | 185.03 | 178.09 | 0.1353 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.97 |  | 24.2667 | 2.8982 | 24.3 | 23.46 | 0.0801 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.27 |  | 20.6203 | 3.151 | 20.445 | 19.92 | 0.047 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.815 |  | 25.0649 | 2.9928 | 25.45 | 24.1 | 0.0775 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.19 |  | 33.7781 | 1.2193 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.66 |  | 67.1546 | 2.2416 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.59 |  | 294.2091 | 0.1295 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 699.24 |  | 695.332 | 0.562 | 693.36 | 686.78 | 0.0543 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 394.81 |  | 393.2088 | 0.4072 | 398.39 | 393.52 | 0.076 | watch_only | none |
| 4 | TSM | foundry | 400.76 |  | 398.097 | 0.6689 | 394.11 | 386.02 | 0.1822 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 205.04 |  | 203.2035 | 0.9038 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 470.67 |  | 469.7711 | 0.1914 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | IREN | high_beta_ai_infrastructure | 34.19 |  | 33.7781 | 1.2193 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 141.31 |  | 140.9651 | 0.2447 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 562.3 |  | 554.6401 | 1.3811 | 550 | 536.9 | 0.0658 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 528.355 |  | 517.7999 | 2.0385 | 511.83 | 498.665 | 0.0719 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.815 |  | 25.0649 | 2.9928 | 25.45 | 24.1 | 0.0775 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.52 |  | 45.5927 | 2.0339 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 13 | MRVL | custom_silicon_networking | 192.235 |  | 186.9125 | 2.8476 | 185.03 | 178.09 | 0.1353 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 24.97 |  | 24.2667 | 2.8982 | 24.3 | 23.46 | 0.0801 | buy_precheck_manual_confirm | none |
| 15 | ETN | data_center_power_cooling | 402.455 |  | 399.6167 | 0.7102 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 21.27 |  | 20.6203 | 3.151 | 20.445 | 19.92 | 0.047 | buy_precheck_manual_confirm | none |
| 17 | GEV | data_center_power_cooling | 1062.44 |  | 1043.8513 | 1.7808 | 1001.82 | 982.21 | 0.3097 | buy_precheck_manual_confirm | none |
| 18 | META | cloud_ai_capex | 646.18 |  | 641.5836 | 0.7164 | 649.07 | 638.97 | 2.6912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 539.54 |  | 535.4453 | 0.7647 | 535.095 | 513.34 | 4.5279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SPY | market_regime | 744.92 |  | 745.0082 | -0.0118 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 205.04 |  | 203.2035 | 0.9038 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 400.76 |  | 398.097 | 0.6689 | 394.11 | 386.02 | 0.1822 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 562.3 |  | 554.6401 | 1.3811 | 550 | 536.9 | 0.0658 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 528.355 |  | 517.7999 | 2.0385 | 511.83 | 498.665 | 0.0719 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.59 |  | 294.2091 | 0.1295 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1062.44 |  | 1043.8513 | 1.7808 | 1001.82 | 982.21 | 0.3097 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 699.24 |  | 695.332 | 0.562 | 693.36 | 686.78 | 0.0543 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.52 |  | 45.5927 | 2.0339 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 192.235 |  | 186.9125 | 2.8476 | 185.03 | 178.09 | 0.1353 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.97 |  | 24.2667 | 2.8982 | 24.3 | 23.46 | 0.0801 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.27 |  | 20.6203 | 3.151 | 20.445 | 19.92 | 0.047 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.815 |  | 25.0649 | 2.9928 | 25.45 | 24.1 | 0.0775 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.19 |  | 33.7781 | 1.2193 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.66 |  | 67.1546 | 2.2416 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |
| 15 | SPY | market_regime | 744.92 |  | 745.0082 | -0.0118 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 16 | ANET | ai_networking_optical | 170.31 |  | 165.7352 | 2.7603 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 375.05 |  | 369.9429 | 1.3805 | 368.42 | 357.97 | 1.3438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 539.54 |  | 535.4453 | 0.7647 | 535.095 | 513.34 | 4.5279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 501.9 |  | 486.1379 | 3.2423 | 482.43 | 461.04 | 4.3036 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1775.335 |  | 1755.6363 | 1.122 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.24 |  | 695.332 | 0.562 | 693.36 | 686.78 | 0.0543 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.66 |  | 67.1546 | 2.2416 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.04 |  | 203.2035 | 0.9038 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.81 |  | 393.2088 | 0.4072 | 398.39 | 393.52 | 0.076 | watch_only | none |
| AAPL | mega_cap_platform | 330.71 |  | 331.9968 | -0.3876 | 334.98 | 331.295 | 0.0091 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 343.6 |  | 346.0314 | -0.7027 | 348.47 | 341.42 | 0.096 | below_vwap | below_vwap |
| AMD | ai_accelerator | 501.9 |  | 486.1379 | 3.2423 | 482.43 | 461.04 | 4.3036 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.76 |  | 398.097 | 0.6689 | 394.11 | 386.02 | 0.1822 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.355 |  | 517.7999 | 2.0385 | 511.83 | 498.665 | 0.0719 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 562.3 |  | 554.6401 | 1.3811 | 550 | 536.9 | 0.0658 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 375.05 |  | 369.9429 | 1.3805 | 368.42 | 357.97 | 1.3438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 889.46 |  | 862.9225 | 3.0753 | 835.82 | 804.09 | 1.5279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 192.235 |  | 186.9125 | 2.8476 | 185.03 | 178.09 | 0.1353 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 403.84 |  | 391.9687 | 3.0286 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.52 |  | 45.5927 | 2.0339 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.97 |  | 24.2667 | 2.8982 | 24.3 | 23.46 | 0.0801 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.92 |  | 745.0082 | -0.0118 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.59 |  | 294.2091 | 0.1295 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.785 |  | 125.8833 | 1.5107 | 125.02 | 121.79 | 3.5059 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 74.07 |  | 72.1178 | 2.707 | 71.24 | 68.65 | 0.5805 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 294.97 |  | 286.76 | 2.863 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.455 |  | 399.6167 | 0.7102 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.485 |  | 629.435 | 0.8023 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1062.44 |  | 1043.8513 | 1.7808 | 1001.82 | 982.21 | 0.3097 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 470.67 |  | 469.7711 | 0.1914 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.31 |  | 140.9651 | 0.2447 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 170.31 |  | 165.7352 | 2.7603 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 282.01 |  | 273.6779 | 3.0445 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 740 |  | 714.5933 | 3.5554 | 694.98 | 653.305 | 4.5527 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 383.88 |  | 377.5611 | 1.6736 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 104.555 |  | 100.3499 | 4.1905 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 308.26 |  | 305.2531 | 0.9851 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1775.335 |  | 1755.6363 | 1.122 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 539.54 |  | 535.4453 | 0.7647 | 535.095 | 513.34 | 4.5279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 314.69 |  | 312.0625 | 0.842 | 306.51 | 298.89 | 4.8524 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 214.41 |  | 212.1188 | 1.0802 | 210.82 | 204.71 | 1.9122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 327.24 |  | 318.9639 | 2.5947 | 308.03 | 297.18 | 1.0329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 282.11 |  | 277.2478 | 1.7537 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.82 |  | 61.3759 | 2.3528 | 60.51 | 57.99 | 4.6323 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 51.39 |  | 49.8348 | 3.1208 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.48 |  | 134.23 | 3.1662 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 327.03 |  | 318.2148 | 2.7702 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 514.72 |  | 520.2568 | -1.0642 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.525 |  | 299.6311 | -1.0366 | 304.36 | 299.62 | 4.8192 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.815 |  | 25.0649 | 2.9928 | 25.45 | 24.1 | 0.0775 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.19 |  | 33.7781 | 1.2193 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 21.27 |  | 20.6203 | 3.151 | 20.445 | 19.92 | 0.047 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1450.79 |  | 1427.6984 | 1.6174 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 486.95 |  | 465.603 | 4.5848 | 453.35 | 431.78 | 2.1727 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 790.26 |  | 758.4209 | 4.1981 | 724.57 | 702.24 | 3.433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.08 |  | 248.0424 | -0.388 | 247.72 | 243.725 | 0.0121 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.18 |  | 641.5836 | 0.7164 | 649.07 | 638.97 | 2.6912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.86 |  | 260.8663 | 4.2143 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.195 |  | 158.4838 | 0.4488 | 151.99 | 145.6 | 4.0202 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
