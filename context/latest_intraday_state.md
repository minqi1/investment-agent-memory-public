# Intraday State

- Generated at: `2026-07-18T03:28:35+08:00`
- Market time ET: `2026-07-17T15:28:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'manual_confirm_candidate': 8, 'watch_only': 4, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.34 |  | 695.6307 | -0.0418 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 521.08 |  | 518.7195 | 0.4551 | 511.83 | 498.665 | 0.0576 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.37 |  | 555.1711 | 0.0358 | 550 | 536.9 | 0.0774 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.81 |  | 744.739 | -0.259 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 555.37 |  | 555.1711 | 0.0358 | 550 | 536.9 | 0.0774 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 521.08 |  | 518.7195 | 0.4551 | 511.83 | 498.665 | 0.0576 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.26 |  | 212.1905 | 0.0327 | 210.82 | 204.71 | 0.1225 | buy_precheck_manual_confirm | none |
| 4 | VRT | data_center_power_cooling | 290.585 |  | 287.6816 | 1.0092 | 280.565 | 273.17 | 0.0792 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 45.98 |  | 45.7075 | 0.5962 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.385 |  | 24.3225 | 0.257 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.68 |  | 20.6794 | 0.0031 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 67.49 |  | 67.248 | 0.3599 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 212.26 |  | 212.1905 | 0.0327 | 210.82 | 204.71 | 0.1225 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 24.385 |  | 24.3225 | 0.257 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.37 |  | 555.1711 | 0.0358 | 550 | 536.9 | 0.0774 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 20.68 |  | 20.6794 | 0.0031 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.82 |  | 332.325 | 0.149 | 334.98 | 331.295 | 0.015 | watch_only | none |
| 6 | META | cloud_ai_capex | 643.325 |  | 642.58 | 0.1159 | 649.07 | 638.97 | 0.2316 | watch_only | none |
| 7 | SOXX | semiconductor_index | 521.08 |  | 518.7195 | 0.4551 | 511.83 | 498.665 | 0.0576 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.98 |  | 45.7075 | 0.5962 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 9 | MSFT | cloud_ai_capex | 395.33 |  | 393.6179 | 0.435 | 398.39 | 393.52 | 0.0278 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 25.245 |  | 25.1053 | 0.5565 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| 11 | VRT | data_center_power_cooling | 290.585 |  | 287.6816 | 1.0092 | 280.565 | 273.17 | 0.0792 | buy_precheck_manual_confirm | none |
| 12 | AVGO | custom_silicon_networking | 371.22 |  | 370.4044 | 0.2202 | 368.42 | 357.97 | 2.2763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ETN | data_center_power_cooling | 399.74 |  | 399.7344 | 0.0014 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ORCL | cloud_ai_capex | 126.065 |  | 126.0315 | 0.0265 | 125.02 | 121.79 | 1.7451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | GEV | data_center_power_cooling | 1051.175 |  | 1046.0022 | 0.4945 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | QQQ | market_regime | 695.34 |  | 695.6307 | -0.0418 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| 17 | SPY | market_regime | 742.81 |  | 744.739 | -0.259 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 18 | NVDA | ai_accelerator | 202.53 |  | 203.1783 | -0.3191 | 203.41 | 197.98 | 0.0938 | below_vwap | below_vwap |
| 19 | TER | semiconductor_test_packaging | 322.32 |  | 320.3377 | 0.6188 | 308.03 | 297.18 | 4.4335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 187.97 |  | 187.266 | 0.3759 | 185.03 | 178.09 | 2.6706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 555.37 |  | 555.1711 | 0.0358 | 550 | 536.9 | 0.0774 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 521.08 |  | 518.7195 | 0.4551 | 511.83 | 498.665 | 0.0576 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.26 |  | 212.1905 | 0.0327 | 210.82 | 204.71 | 0.1225 | buy_precheck_manual_confirm | none |
| 4 | VRT | data_center_power_cooling | 290.585 |  | 287.6816 | 1.0092 | 280.565 | 273.17 | 0.0792 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 45.98 |  | 45.7075 | 0.5962 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.385 |  | 24.3225 | 0.257 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.68 |  | 20.6794 | 0.0031 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 67.49 |  | 67.248 | 0.3599 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 395.82 |  | 397.8374 | -0.5071 | 394.11 | 386.02 | 0.9878 | below_vwap | below_vwap,spread_too_wide |
| 10 | ASML | semiconductor_equipment | 1750.65 |  | 1756.7942 | -0.3497 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | MU | memory_hbm_storage | 861.19 |  | 864.5814 | -0.3923 | 835.82 | 804.09 | 0.8895 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 140.78 |  | 140.9205 | -0.0997 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 630.225 |  | 630.2934 | -0.0109 | 616.75 | 609.05 | 0.1476 | below_vwap | below_vwap |
| 14 | QQQ | market_regime | 695.34 |  | 695.6307 | -0.0418 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 310.655 |  | 312.0615 | -0.4507 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | SPY | market_regime | 742.81 |  | 744.739 | -0.259 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 17 | ONTO | semiconductor_test_packaging | 276.12 |  | 277.6294 | -0.5437 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | SKHY | memory_hbm_storage | 153.54 |  | 158.8078 | -3.3171 | 151.99 | 145.6 | 0.8011 | below_vwap | below_vwap,spread_too_wide |
| 19 | ANET | ai_networking_optical | 167.9 |  | 166.3602 | 0.9256 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 371.22 |  | 370.4044 | 0.2202 | 368.42 | 357.97 | 2.2763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.34 |  | 695.6307 | -0.0418 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.49 |  | 67.248 | 0.3599 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.53 |  | 203.1783 | -0.3191 | 203.41 | 197.98 | 0.0938 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 395.33 |  | 393.6179 | 0.435 | 398.39 | 393.52 | 0.0278 | watch_only | none |
| AAPL | mega_cap_platform | 332.82 |  | 332.325 | 0.149 | 334.98 | 331.295 | 0.015 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.015 |  | 345.756 | -0.2143 | 348.47 | 341.42 | 0.0985 | below_vwap | below_vwap |
| AMD | ai_accelerator | 494.18 |  | 487.1631 | 1.4404 | 482.43 | 461.04 | 0.4027 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 395.82 |  | 397.8374 | -0.5071 | 394.11 | 386.02 | 0.9878 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 521.08 |  | 518.7195 | 0.4551 | 511.83 | 498.665 | 0.0576 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.37 |  | 555.1711 | 0.0358 | 550 | 536.9 | 0.0774 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.22 |  | 370.4044 | 0.2202 | 368.42 | 357.97 | 2.2763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 861.19 |  | 864.5814 | -0.3923 | 835.82 | 804.09 | 0.8895 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.97 |  | 187.266 | 0.3759 | 185.03 | 178.09 | 2.6706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 397.68 |  | 393.6049 | 1.0353 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.98 |  | 45.7075 | 0.5962 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.385 |  | 24.3225 | 0.257 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.81 |  | 744.739 | -0.259 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.28 |  | 294.0943 | -0.2769 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.065 |  | 126.0315 | 0.0265 | 125.02 | 121.79 | 1.7451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 72.61 |  | 72.2861 | 0.4481 | 71.24 | 68.65 | 2.1347 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.585 |  | 287.6816 | 1.0092 | 280.565 | 273.17 | 0.0792 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 399.74 |  | 399.7344 | 0.0014 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 630.225 |  | 630.2934 | -0.0109 | 616.75 | 609.05 | 0.1476 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1051.175 |  | 1046.0022 | 0.4945 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.04 |  | 469.7213 | -0.145 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.78 |  | 140.9205 | -0.0997 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.9 |  | 166.3602 | 0.9256 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 277.08 |  | 274.2981 | 1.0142 | 269.59 | 256.24 | 4.8542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 733.7 |  | 719.3737 | 1.9915 | 694.98 | 653.305 | 2.1044 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 374.65 |  | 377.6833 | -0.8031 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.28 |  | 100.6923 | 1.5767 | 97.585 | 91.92 | 0.4693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 302.87 |  | 304.632 | -0.5784 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1750.65 |  | 1756.7942 | -0.3497 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 529.19 |  | 534.0039 | -0.9015 | 535.095 | 513.34 | 1.3284 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 310.655 |  | 312.0615 | -0.4507 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.26 |  | 212.1905 | 0.0327 | 210.82 | 204.71 | 0.1225 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 322.32 |  | 320.3377 | 0.6188 | 308.03 | 297.18 | 4.4335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 276.12 |  | 277.6294 | -0.5437 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.26 |  | 61.6268 | 1.0276 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.64 |  | 49.9991 | 1.2818 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.27 |  | 135.1793 | 0.8069 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.37 |  | 319.2209 | 1.613 | 315.89 | 307.13 | 4.2482 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.565 |  | 518.4037 | -0.9334 | 526.74 | 522.205 | 3.6529 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 295.86 |  | 298.6512 | -0.9346 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.245 |  | 25.1053 | 0.5565 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.335 |  | 33.7513 | -1.2335 | 34 | 32.26 | 0.03 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.68 |  | 20.6794 | 0.0031 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1393.78 |  | 1426.9082 | -2.3217 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 478.68 |  | 467.9407 | 2.295 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 789.68 |  | 765.9268 | 3.1012 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.18 |  | 247.9665 | -0.3172 | 247.72 | 243.725 | 0.0121 | below_vwap | below_vwap |
| META | cloud_ai_capex | 643.325 |  | 642.58 | 0.1159 | 649.07 | 638.97 | 0.2316 | watch_only | none |
| ARM | ai_accelerator | 266.42 |  | 261.6075 | 1.8396 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 153.54 |  | 158.8078 | -3.3171 | 151.99 | 145.6 | 0.8011 | below_vwap | below_vwap,spread_too_wide |
