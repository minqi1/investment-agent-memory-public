# Intraday State

- Generated at: `2026-07-18T01:51:04+08:00`
- Market time ET: `2026-07-17T13:51:05-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 1, 'below_opening_15m_low': 3, 'below_vwap': 3, 'spread_too_wide_or_missing': 35, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.99 |  | 695.2802 | 0.6774 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 529.36 |  | 517.7307 | 2.2462 | 511.83 | 498.665 | 0.0963 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 563.125 |  | 554.5567 | 1.5451 | 550 | 536.9 | 0.0799 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.52 |  | 745.0081 | 0.0687 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 205.205 |  | 203.1814 | 0.996 | 203.41 | 197.98 | 0.0097 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 563.125 |  | 554.5567 | 1.5451 | 550 | 536.9 | 0.0799 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 529.36 |  | 517.7307 | 2.2462 | 511.83 | 498.665 | 0.0963 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 214.91 |  | 212.0987 | 1.3255 | 210.82 | 204.71 | 0.121 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.975 |  | 294.2048 | 0.2618 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 699.99 |  | 695.2802 | 0.6774 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.625 |  | 45.5804 | 2.2918 | 44.92 | 43.715 | 0.0214 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.52 |  | 745.0081 | 0.0687 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.07 |  | 24.2611 | 3.334 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.31 |  | 20.6148 | 3.3721 | 20.445 | 19.92 | 0.0939 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.87 |  | 25.0629 | 3.2203 | 25.45 | 24.1 | 0.0773 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.255 |  | 33.7707 | 1.4341 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.9 |  | 67.1468 | 2.611 | 66.9 | 64.92 | 0.029 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.975 |  | 294.2048 | 0.2618 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 745.52 |  | 745.0081 | 0.0687 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 699.99 |  | 695.2802 | 0.6774 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.94 |  | 393.1984 | 0.4429 | 398.39 | 393.52 | 0.0987 | watch_only | none |
| 5 | NVDA | ai_accelerator | 205.205 |  | 203.1814 | 0.996 | 203.41 | 197.98 | 0.0097 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 34.255 |  | 33.7707 | 1.4341 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 141.26 |  | 140.9641 | 0.2099 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | KLAC | semiconductor_equipment | 214.91 |  | 212.0987 | 1.3255 | 210.82 | 204.71 | 0.121 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 471.63 |  | 469.7678 | 0.3964 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SMH | semiconductor_index | 563.125 |  | 554.5567 | 1.5451 | 550 | 536.9 | 0.0799 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 529.36 |  | 517.7307 | 2.2462 | 511.83 | 498.665 | 0.0963 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.625 |  | 45.5804 | 2.2918 | 44.92 | 43.715 | 0.0214 | buy_precheck_manual_confirm | none |
| 13 | SMCI | ai_server_oem | 25.07 |  | 24.2611 | 3.334 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| 14 | CORZ | high_beta_ai_infrastructure | 21.31 |  | 20.6148 | 3.3721 | 20.445 | 19.92 | 0.0939 | buy_precheck_manual_confirm | none |
| 15 | APLD | high_beta_ai_infrastructure | 25.87 |  | 25.0629 | 3.2203 | 25.45 | 24.1 | 0.0773 | buy_precheck_manual_confirm | none |
| 16 | GOOGL | cloud_ai_capex | 344.37 |  | 346.0453 | -0.4841 | 348.47 | 341.42 | 0.0581 | below_vwap | below_vwap |
| 17 | AMZN | cloud_ai_capex | 247.6 |  | 248.0569 | -0.1842 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| 18 | ASML | semiconductor_equipment | 1780.325 |  | 1755.3554 | 1.4225 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 403.13 |  | 399.5573 | 0.8942 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 205.205 |  | 203.1814 | 0.996 | 203.41 | 197.98 | 0.0097 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 563.125 |  | 554.5567 | 1.5451 | 550 | 536.9 | 0.0799 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 529.36 |  | 517.7307 | 2.2462 | 511.83 | 498.665 | 0.0963 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 214.91 |  | 212.0987 | 1.3255 | 210.82 | 204.71 | 0.121 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.975 |  | 294.2048 | 0.2618 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 699.99 |  | 695.2802 | 0.6774 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.625 |  | 45.5804 | 2.2918 | 44.92 | 43.715 | 0.0214 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.52 |  | 745.0081 | 0.0687 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.07 |  | 24.2611 | 3.334 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.31 |  | 20.6148 | 3.3721 | 20.445 | 19.92 | 0.0939 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.87 |  | 25.0629 | 3.2203 | 25.45 | 24.1 | 0.0773 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.255 |  | 33.7707 | 1.4341 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.9 |  | 67.1468 | 2.611 | 66.9 | 64.92 | 0.029 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 170.54 |  | 165.6474 | 2.9536 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 401.42 |  | 398.0639 | 0.8431 | 394.11 | 386.02 | 0.8769 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 375.56 |  | 369.8874 | 1.5336 | 368.42 | 357.97 | 2.5269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 540.455 |  | 535.4073 | 0.9428 | 535.095 | 513.34 | 0.4755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 503.015 |  | 486.0707 | 3.486 | 482.43 | 461.04 | 0.4413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1780.325 |  | 1755.3554 | 1.4225 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TT | data_center_power_cooling | 471.63 |  | 469.7678 | 0.3964 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.99 |  | 695.2802 | 0.6774 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.9 |  | 67.1468 | 2.611 | 66.9 | 64.92 | 0.029 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.205 |  | 203.1814 | 0.996 | 203.41 | 197.98 | 0.0097 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.94 |  | 393.1984 | 0.4429 | 398.39 | 393.52 | 0.0987 | watch_only | none |
| AAPL | mega_cap_platform | 330.795 |  | 332.0057 | -0.3647 | 334.98 | 331.295 | 0.0967 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 344.37 |  | 346.0453 | -0.4841 | 348.47 | 341.42 | 0.0581 | below_vwap | below_vwap |
| AMD | ai_accelerator | 503.015 |  | 486.0707 | 3.486 | 482.43 | 461.04 | 0.4413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 401.42 |  | 398.0639 | 0.8431 | 394.11 | 386.02 | 0.8769 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.36 |  | 517.7307 | 2.2462 | 511.83 | 498.665 | 0.0963 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 563.125 |  | 554.5567 | 1.5451 | 550 | 536.9 | 0.0799 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 375.56 |  | 369.8874 | 1.5336 | 368.42 | 357.97 | 2.5269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 890.94 |  | 862.7741 | 3.2646 | 835.82 | 804.09 | 2.7095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 192.51 |  | 186.8805 | 3.0124 | 185.03 | 178.09 | 1.0285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 404.67 |  | 391.84 | 3.2743 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.625 |  | 45.5804 | 2.2918 | 44.92 | 43.715 | 0.0214 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.07 |  | 24.2611 | 3.334 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.52 |  | 745.0081 | 0.0687 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.975 |  | 294.2048 | 0.2618 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 128.1 |  | 125.863 | 1.7774 | 125.02 | 121.79 | 0.3591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 74.085 |  | 72.1059 | 2.7447 | 71.24 | 68.65 | 2.1867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 295.38 |  | 286.69 | 3.0311 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 403.13 |  | 399.5573 | 0.8942 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 635.245 |  | 629.3315 | 0.9397 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1064.52 |  | 1043.7517 | 1.9898 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 471.63 |  | 469.7678 | 0.3964 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.26 |  | 140.9641 | 0.2099 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 170.54 |  | 165.6474 | 2.9536 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 282.865 |  | 273.6451 | 3.3693 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 741.655 |  | 714.3563 | 3.8214 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 385.04 |  | 377.5078 | 1.9953 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 104.53 |  | 100.3433 | 4.1723 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 309.79 |  | 305.2153 | 1.4988 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1780.325 |  | 1755.3554 | 1.4225 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 540.455 |  | 535.4073 | 0.9428 | 535.095 | 513.34 | 0.4755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 315.46 |  | 312.0064 | 1.1069 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.91 |  | 212.0987 | 1.3255 | 210.82 | 204.71 | 0.121 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 327.61 |  | 318.8636 | 2.743 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 282.26 |  | 277.105 | 1.8603 | 265.71 | 258.355 | 0.496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.93 |  | 61.3672 | 2.5466 | 60.51 | 57.99 | 4.3858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 51.4 |  | 49.802 | 3.2087 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.68 |  | 134.2027 | 3.3362 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 328.41 |  | 318.134 | 3.2301 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 514.67 |  | 520.2941 | -1.0809 | 526.74 | 522.205 | 3.919 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 296.525 |  | 299.6311 | -1.0366 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.87 |  | 25.0629 | 3.2203 | 25.45 | 24.1 | 0.0773 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.255 |  | 33.7707 | 1.4341 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 21.31 |  | 20.6148 | 3.3721 | 20.445 | 19.92 | 0.0939 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1457.535 |  | 1427.5814 | 2.0982 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 489.96 |  | 465.3896 | 5.2795 | 453.35 | 431.78 | 2.7431 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 796.775 |  | 757.4225 | 5.1956 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.6 |  | 248.0569 | -0.1842 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.8 |  | 641.5029 | 0.9816 | 649.07 | 638.97 | 2.6968 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.97 |  | 260.808 | 4.2798 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 160.19 |  | 158.473 | 1.0835 | 151.99 | 145.6 | 3.4771 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
