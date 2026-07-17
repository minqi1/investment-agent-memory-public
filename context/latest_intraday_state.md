# Intraday State

- Generated at: `2026-07-18T00:39:07+08:00`
- Market time ET: `2026-07-17T12:39:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 3, 'below_vwap': 2, 'watch_only': 3, 'spread_too_wide_or_missing': 34, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.08 |  | 694.039 | 0.7263 | 693.36 | 686.78 | 0.0343 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 526.67 |  | 515.6016 | 2.1467 | 511.83 | 498.665 | 0.093 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.36 |  | 552.2091 | 1.6571 | 550 | 536.9 | 0.0659 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.8 |  | 744.7336 | 0.1432 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.85 |  | 202.6803 | 1.0705 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 561.36 |  | 552.2091 | 1.6571 | 550 | 536.9 | 0.0659 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 526.67 |  | 515.6016 | 2.1467 | 511.83 | 498.665 | 0.093 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 214.22 |  | 211.3034 | 1.3803 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.08 |  | 694.039 | 0.7263 | 693.36 | 686.78 | 0.0343 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.915 |  | 45.4066 | 1.1197 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.8 |  | 744.7336 | 0.1432 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.255 |  | 247.9038 | 0.1417 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189.89 |  | 185.3385 | 2.4558 | 185.03 | 178.09 | 0.2106 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.61 |  | 24.1095 | 2.0759 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.845 |  | 20.5256 | 1.5562 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.035 |  | 33.5478 | 1.4522 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.63 |  | 66.9022 | 2.5826 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 248.255 |  | 247.9038 | 0.1417 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 745.8 |  | 744.7336 | 0.1432 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 294.11 |  | 294.0442 | 0.0224 | 294.205 | 291.675 | 0.0136 | watch_only | none |
| 4 | QQQ | market_regime | 699.08 |  | 694.039 | 0.7263 | 693.36 | 686.78 | 0.0343 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 346.61 |  | 346.1195 | 0.1417 | 348.47 | 341.42 | 0.225 | watch_only | none |
| 6 | NVDA | ai_accelerator | 204.85 |  | 202.6803 | 1.0705 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 7 | IREN | high_beta_ai_infrastructure | 34.035 |  | 33.5478 | 1.4522 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.915 |  | 45.4066 | 1.1197 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 214.22 |  | 211.3034 | 1.3803 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 25.215 |  | 24.8983 | 1.2718 | 25.45 | 24.1 | 0.0793 | watch_only | none |
| 11 | JCI | data_center_power_cooling | 141.3 |  | 140.7225 | 0.4104 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SMCI | ai_server_oem | 24.61 |  | 24.1095 | 2.0759 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 561.36 |  | 552.2091 | 1.6571 | 550 | 536.9 | 0.0659 | buy_precheck_manual_confirm | none |
| 14 | SOXX | semiconductor_index | 526.67 |  | 515.6016 | 2.1467 | 511.83 | 498.665 | 0.093 | buy_precheck_manual_confirm | none |
| 15 | TT | data_center_power_cooling | 472.32 |  | 469.3794 | 0.6265 | 469.08 | 460.78 | 3.7348 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ETN | data_center_power_cooling | 402.16 |  | 399.0143 | 0.7884 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | CORZ | high_beta_ai_infrastructure | 20.845 |  | 20.5256 | 1.5562 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| 18 | META | cloud_ai_capex | 643.11 |  | 638.1022 | 0.7848 | 649.07 | 638.97 | 0.6111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MSFT | cloud_ai_capex | 393.39 |  | 392.9407 | 0.1143 | 398.39 | 393.52 | 0.0356 | below_opening_15m_low | below_opening_15m_low |
| 20 | MRVL | custom_silicon_networking | 189.89 |  | 185.3385 | 2.4558 | 185.03 | 178.09 | 0.2106 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.85 |  | 202.6803 | 1.0705 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 561.36 |  | 552.2091 | 1.6571 | 550 | 536.9 | 0.0659 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 526.67 |  | 515.6016 | 2.1467 | 511.83 | 498.665 | 0.093 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 214.22 |  | 211.3034 | 1.3803 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.08 |  | 694.039 | 0.7263 | 693.36 | 686.78 | 0.0343 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.915 |  | 45.4066 | 1.1197 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.8 |  | 744.7336 | 0.1432 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.255 |  | 247.9038 | 0.1417 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189.89 |  | 185.3385 | 2.4558 | 185.03 | 178.09 | 0.2106 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.61 |  | 24.1095 | 2.0759 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.845 |  | 20.5256 | 1.5562 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.035 |  | 33.5478 | 1.4522 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.63 |  | 66.9022 | 2.5826 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 167.935 |  | 164.1623 | 2.2982 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 400.99 |  | 396.7336 | 1.0729 | 394.11 | 386.02 | 1.4414 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 373.11 |  | 368.5376 | 1.2407 | 368.42 | 357.97 | 1.2034 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 545.27 |  | 532.1184 | 2.4716 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 498.6 |  | 483.4208 | 3.1399 | 482.43 | 461.04 | 0.9246 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1772.36 |  | 1746.6733 | 1.4706 | 1741.99 | 1704.935 | 1.6362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 472.32 |  | 469.3794 | 0.6265 | 469.08 | 460.78 | 3.7348 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.08 |  | 694.039 | 0.7263 | 693.36 | 686.78 | 0.0343 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.63 |  | 66.9022 | 2.5826 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.85 |  | 202.6803 | 1.0705 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.39 |  | 392.9407 | 0.1143 | 398.39 | 393.52 | 0.0356 | below_opening_15m_low | below_opening_15m_low |
| AAPL | mega_cap_platform | 331.865 |  | 332.273 | -0.1228 | 334.98 | 331.295 | 0.0151 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 346.61 |  | 346.1195 | 0.1417 | 348.47 | 341.42 | 0.225 | watch_only | none |
| AMD | ai_accelerator | 498.6 |  | 483.4208 | 3.1399 | 482.43 | 461.04 | 0.9246 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.99 |  | 396.7336 | 1.0729 | 394.11 | 386.02 | 1.4414 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.67 |  | 515.6016 | 2.1467 | 511.83 | 498.665 | 0.093 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.36 |  | 552.2091 | 1.6571 | 550 | 536.9 | 0.0659 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.11 |  | 368.5376 | 1.2407 | 368.42 | 357.97 | 1.2034 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 885.67 |  | 855.4496 | 3.5327 | 835.82 | 804.09 | 1.1291 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.89 |  | 185.3385 | 2.4558 | 185.03 | 178.09 | 0.2106 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 395.185 |  | 388.6471 | 1.6822 | 384 | 368.28 | 2.8493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.915 |  | 45.4066 | 1.1197 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.61 |  | 24.1095 | 2.0759 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.8 |  | 744.7336 | 0.1432 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.11 |  | 294.0442 | 0.0224 | 294.205 | 291.675 | 0.0136 | watch_only | none |
| ORCL | cloud_ai_capex | 127.215 |  | 125.3704 | 1.4713 | 125.02 | 121.79 | 2.0202 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 72.74 |  | 71.7775 | 1.341 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 294.255 |  | 284.27 | 3.5125 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.16 |  | 399.0143 | 0.7884 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 632.94 |  | 627.5472 | 0.8593 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1051.67 |  | 1039.933 | 1.1286 | 1001.82 | 982.21 | 1.1981 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 472.32 |  | 469.3794 | 0.6265 | 469.08 | 460.78 | 3.7348 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.3 |  | 140.7225 | 0.4104 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.935 |  | 164.1623 | 2.2982 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 280.34 |  | 272.0954 | 3.03 | 269.59 | 256.24 | 1.6551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 728.11 |  | 706.0739 | 3.1209 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 378.85 |  | 374.9705 | 1.0346 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.815 |  | 98.9819 | 2.8622 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 308.78 |  | 302.0567 | 2.2258 | 305.21 | 289.97 | 0.5667 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1772.36 |  | 1746.6733 | 1.4706 | 1741.99 | 1704.935 | 1.6362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 545.27 |  | 532.1184 | 2.4716 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 318.31 |  | 310.53 | 2.5054 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.22 |  | 211.3034 | 1.3803 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 322.785 |  | 312.2296 | 3.3807 | 308.03 | 297.18 | 4.393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 281.84 |  | 271.8688 | 3.6676 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.73 |  | 60.9418 | 2.9343 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.79 |  | 49.473 | 2.6621 | 49.35 | 46.44 | 1.1026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ENTG | semiconductor_materials | 138.08 |  | 133.4938 | 3.4355 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.16 |  | 316.709 | 2.6684 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 516.28 |  | 521.1241 | -0.9295 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 297.525 |  | 300.7493 | -1.0721 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.215 |  | 24.8983 | 1.2718 | 25.45 | 24.1 | 0.0793 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.035 |  | 33.5478 | 1.4522 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.845 |  | 20.5256 | 1.5562 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1468.68 |  | 1417.8796 | 3.5828 | 1393.96 | 1325.48 | 3.4044 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 479.12 |  | 457.3142 | 4.7682 | 453.35 | 431.78 | 0.4571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 782.56 |  | 746.8033 | 4.788 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.255 |  | 247.9038 | 0.1417 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 643.11 |  | 638.1022 | 0.7848 | 649.07 | 638.97 | 0.6111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.46 |  | 257.5713 | 3.451 | 252.95 | 243.21 | 4.1995 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 162.79 |  | 157.1209 | 3.6081 | 151.99 | 145.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
