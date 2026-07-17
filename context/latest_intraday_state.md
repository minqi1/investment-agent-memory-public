# Intraday State

- Generated at: `2026-07-18T01:17:50+08:00`
- Market time ET: `2026-07-17T13:17:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'spread_too_wide_or_missing': 36, 'watch_only': 1, 'below_opening_15m_low': 3, 'price_stale_or_missing': 1, 'below_vwap': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701.875 |  | 694.6764 | 1.0363 | 693.36 | 686.78 | 0.0427 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 532.49 |  | 517.0075 | 2.9946 | 511.83 | 498.665 | 0.0864 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 566.67 |  | 553.9561 | 2.2951 | 550 | 536.9 | 0.0794 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.8 |  | 744.8986 | 0.2553 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 403.515 |  | 397.5917 | 1.4898 | 394.11 | 386.02 | 0.0545 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 566.67 |  | 553.9561 | 2.2951 | 550 | 536.9 | 0.0794 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 532.49 |  | 517.0075 | 2.9946 | 511.83 | 498.665 | 0.0864 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 473.71 |  | 469.5964 | 0.876 | 469.08 | 460.78 | 0.2111 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.26 |  | 294.1092 | 0.3913 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 701.875 |  | 694.6764 | 1.0363 | 693.36 | 686.78 | 0.0427 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.525 |  | 45.4978 | 2.2577 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.8 |  | 744.8986 | 0.2553 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.745 |  | 248.0325 | 0.2873 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.025 |  | 24.2031 | 3.3957 | 24.3 | 23.46 | 0.04 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.5768 | 3.3201 | 20.445 | 19.92 | 0.1411 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.82 |  | 24.9501 | 3.4866 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.535 |  | 33.6463 | 2.6412 | 34 | 32.26 | 0.0579 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 69.44 |  | 67.081 | 3.5167 | 66.9 | 64.92 | 0.0144 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.8 |  | 744.8986 | 0.2553 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.745 |  | 248.0325 | 0.2873 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 295.26 |  | 294.1092 | 0.3913 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.485 |  | 393.0669 | 0.3608 | 398.39 | 393.52 | 0.1217 | watch_only | none |
| 5 | QQQ | market_regime | 701.875 |  | 694.6764 | 1.0363 | 693.36 | 686.78 | 0.0427 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 403.515 |  | 397.5917 | 1.4898 | 394.11 | 386.02 | 0.0545 | buy_precheck_manual_confirm | none |
| 7 | TT | data_center_power_cooling | 473.71 |  | 469.5964 | 0.876 | 469.08 | 460.78 | 0.2111 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 141.585 |  | 140.8117 | 0.5492 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | GOOGL | cloud_ai_capex | 346.4 |  | 346.1827 | 0.0628 | 348.47 | 341.42 | 0.3753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMH | semiconductor_index | 566.67 |  | 553.9561 | 2.2951 | 550 | 536.9 | 0.0794 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 532.49 |  | 517.0075 | 2.9946 | 511.83 | 498.665 | 0.0864 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.82 |  | 24.9501 | 3.4866 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 46.525 |  | 45.4978 | 2.2577 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 25.025 |  | 24.2031 | 3.3957 | 24.3 | 23.46 | 0.04 | buy_precheck_manual_confirm | none |
| 15 | CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.5768 | 3.3201 | 20.445 | 19.92 | 0.1411 | buy_precheck_manual_confirm | none |
| 16 | IREN | high_beta_ai_infrastructure | 34.535 |  | 33.6463 | 2.6412 | 34 | 32.26 | 0.0579 | buy_precheck_manual_confirm | none |
| 17 | META | cloud_ai_capex | 649.515 |  | 640.5559 | 1.3986 | 649.07 | 638.97 | 2.428 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 634.05 |  | 628.5746 | 0.8711 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 403.995 |  | 399.2879 | 1.1789 | 389.4 | 382.38 | 3.6585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 403.515 |  | 397.5917 | 1.4898 | 394.11 | 386.02 | 0.0545 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 566.67 |  | 553.9561 | 2.2951 | 550 | 536.9 | 0.0794 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 532.49 |  | 517.0075 | 2.9946 | 511.83 | 498.665 | 0.0864 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 473.71 |  | 469.5964 | 0.876 | 469.08 | 460.78 | 0.2111 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.26 |  | 294.1092 | 0.3913 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 701.875 |  | 694.6764 | 1.0363 | 693.36 | 686.78 | 0.0427 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.525 |  | 45.4978 | 2.2577 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.8 |  | 744.8986 | 0.2553 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.745 |  | 248.0325 | 0.2873 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.025 |  | 24.2031 | 3.3957 | 24.3 | 23.46 | 0.04 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.5768 | 3.3201 | 20.445 | 19.92 | 0.1411 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.82 |  | 24.9501 | 3.4866 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.535 |  | 33.6463 | 2.6412 | 34 | 32.26 | 0.0579 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 69.44 |  | 67.081 | 3.5167 | 66.9 | 64.92 | 0.0144 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 170.15 |  | 165.0134 | 3.1128 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | NVDA | ai_accelerator | 206.33 |  | 202.9758 | 1.6525 | 203.41 | 197.98 | 0.5671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 376.58 |  | 369.5445 | 1.9038 | 368.42 | 357.97 | 0.9268 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 545.41 |  | 534.5744 | 2.027 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMD | ai_accelerator | 501.59 |  | 485.1109 | 3.397 | 482.43 | 461.04 | 4.3522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1786.56 |  | 1751.5356 | 1.9996 | 1741.99 | 1704.935 | 1.5096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701.875 |  | 694.6764 | 1.0363 | 693.36 | 686.78 | 0.0427 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 69.44 |  | 67.081 | 3.5167 | 66.9 | 64.92 | 0.0144 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.33 |  | 202.9758 | 1.6525 | 203.41 | 197.98 | 0.5671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 394.485 |  | 393.0669 | 0.3608 | 398.39 | 393.52 | 0.1217 | watch_only | none |
| AAPL | mega_cap_platform | 330.12 |  | 332.1306 | -0.6054 | 334.98 | 331.295 | 0.0121 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.4 |  | 346.1827 | 0.0628 | 348.47 | 341.42 | 0.3753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 501.59 |  | 485.1109 | 3.397 | 482.43 | 461.04 | 4.3522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 403.515 |  | 397.5917 | 1.4898 | 394.11 | 386.02 | 0.0545 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 532.49 |  | 517.0075 | 2.9946 | 511.83 | 498.665 | 0.0864 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 566.67 |  | 553.9561 | 2.2951 | 550 | 536.9 | 0.0794 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 376.58 |  | 369.5445 | 1.9038 | 368.42 | 357.97 | 0.9268 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 896.68 |  | 860.2972 | 4.2291 | 835.82 | 804.09 | 1.6505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 193.66 |  | 186.3255 | 3.9364 | 185.03 | 178.09 | 0.7074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 405 |  | 390.1103 | 3.8168 | 384 | 368.28 | 4.1605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.525 |  | 45.4978 | 2.2577 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.025 |  | 24.2031 | 3.3957 | 24.3 | 23.46 | 0.04 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.8 |  | 744.8986 | 0.2553 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.26 |  | 294.1092 | 0.3913 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 128.15 |  | 125.6834 | 1.9626 | 125.02 | 121.79 | 2.6922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.75 |  | 71.885 | 2.5944 | 71.24 | 68.65 | 4.5153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 296.35 |  | 285.623 | 3.7556 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 403.995 |  | 399.2879 | 1.1789 | 389.4 | 382.38 | 3.6585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 634.05 |  | 628.5746 | 0.8711 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1064.39 |  | 1041.6633 | 2.1818 | 1001.82 | 982.21 | 3.3108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 473.71 |  | 469.5964 | 0.876 | 469.08 | 460.78 | 0.2111 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 141.585 |  | 140.8117 | 0.5492 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 170.15 |  | 165.0134 | 3.1128 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 284.01 |  | 273.1378 | 3.9805 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 745.32 |  | 712.1337 | 4.6601 | 694.98 | 653.305 | 1.3712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 383.365 |  | 375.973 | 1.9661 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 104.35 |  | 99.4297 | 4.9486 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 314.305 |  | 303.8735 | 3.4328 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1786.56 |  | 1751.5356 | 1.9996 | 1741.99 | 1704.935 | 1.5096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 545.41 |  | 534.5744 | 2.027 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 317.58 |  | 311.5214 | 1.9448 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.16 |  | 211.8134 | 2.0521 | 210.82 | 204.71 | 1.138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 329.64 |  | 317.2727 | 3.898 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 285.395 |  | 275.3303 | 3.6555 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.48 |  | 61.2162 | 3.698 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.51 |  | 49.6759 | 3.6921 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.83 |  | 133.8189 | 4.4919 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 328.63 |  | 317.3448 | 3.5561 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 516.045 |  | 520.6334 | -0.8813 | 526.74 | 522.205 | 4.2613 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 297.305 |  | 299.9678 | -0.8877 | 304.36 | 299.62 | 3.6663 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.82 |  | 24.9501 | 3.4866 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.535 |  | 33.6463 | 2.6412 | 34 | 32.26 | 0.0579 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.5768 | 3.3201 | 20.445 | 19.92 | 0.1411 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1488.98 |  | 1424.5934 | 4.5196 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 489.575 |  | 461.584 | 6.0641 | 453.35 | 431.78 | 2.7943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 802.225 |  | 752.1882 | 6.6522 | 724.57 | 702.24 | 4.3105 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.745 |  | 248.0325 | 0.2873 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 649.515 |  | 640.5559 | 1.3986 | 649.07 | 638.97 | 2.428 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 272.34 |  | 259.4224 | 4.9794 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 163.49 |  | 158.032 | 3.4537 | 151.99 | 145.6 | 1.0215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
