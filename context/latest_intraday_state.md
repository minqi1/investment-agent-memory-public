# Intraday State

- Generated at: `2026-07-17T23:54:40+08:00`
- Market time ET: `2026-07-17T11:54:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 3, 'watch_only': 5, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1, 'below_vwap': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.47 |  | 693.4648 | 0.5776 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 522.57 |  | 513.2269 | 1.8205 | 511.83 | 498.665 | 0.0593 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.75 |  | 550.137 | 1.5656 | 550 | 536.9 | 0.0877 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.515 |  | 744.494 | 0.1371 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.78 |  | 202.358 | 1.1969 | 203.41 | 197.98 | 0.0244 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.75 |  | 550.137 | 1.5656 | 550 | 536.9 | 0.0877 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 522.57 |  | 513.2269 | 1.8205 | 511.83 | 498.665 | 0.0593 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1046.85 |  | 1034.6376 | 1.1804 | 1001.82 | 982.21 | 0.0516 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.47 |  | 693.4648 | 0.5776 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.685 |  | 45.3096 | 0.8285 | 44.92 | 43.715 | 0.0438 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.515 |  | 744.494 | 0.1371 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.37 |  | 247.8663 | 0.2032 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.685 |  | 71.4811 | 3.0832 | 71.24 | 68.65 | 0.285 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.4146 | 1.3493 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 68.1 |  | 66.7378 | 2.0412 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 248.37 |  | 247.8663 | 0.2032 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 745.515 |  | 744.494 | 0.1371 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 697.47 |  | 693.4648 | 0.5776 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 332.99 |  | 332.5405 | 0.1352 | 334.98 | 331.295 | 0.018 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 24.89 |  | 24.8121 | 0.314 | 25.45 | 24.1 | 0.0402 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.485 |  | 33.426 | 0.1765 | 34 | 32.26 | 0.0299 | watch_only | none |
| 7 | NVDA | ai_accelerator | 204.78 |  | 202.358 | 1.1969 | 203.41 | 197.98 | 0.0244 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 347.33 |  | 345.8472 | 0.4287 | 348.47 | 341.42 | 0.3397 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.4146 | 1.3493 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| 10 | GEV | data_center_power_cooling | 1046.85 |  | 1034.6376 | 1.1804 | 1001.82 | 982.21 | 0.0516 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 45.685 |  | 45.3096 | 0.8285 | 44.92 | 43.715 | 0.0438 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.275 |  | 24.0224 | 1.0517 | 24.3 | 23.46 | 0.0412 | watch_only | none |
| 13 | JCI | data_center_power_cooling | 141.59 |  | 140.5467 | 0.7423 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ALAB | ai_networking_optical | 301.87 |  | 300.1967 | 0.5574 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SMH | semiconductor_index | 558.75 |  | 550.137 | 1.5656 | 550 | 536.9 | 0.0877 | buy_precheck_manual_confirm | none |
| 16 | SOXX | semiconductor_index | 522.57 |  | 513.2269 | 1.8205 | 511.83 | 498.665 | 0.0593 | buy_precheck_manual_confirm | none |
| 17 | TT | data_center_power_cooling | 472.22 |  | 469.1499 | 0.6544 | 469.08 | 460.78 | 3.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CRWV | gpu_cloud_ai_factory | 73.685 |  | 71.4811 | 3.0832 | 71.24 | 68.65 | 0.285 | buy_precheck_manual_confirm | none |
| 19 | IWM | market_regime | 293.83 |  | 294.0003 | -0.0579 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| 20 | AVGO | custom_silicon_networking | 371.245 |  | 368.0877 | 0.8577 | 368.42 | 357.97 | 1.0586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.78 |  | 202.358 | 1.1969 | 203.41 | 197.98 | 0.0244 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.75 |  | 550.137 | 1.5656 | 550 | 536.9 | 0.0877 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 522.57 |  | 513.2269 | 1.8205 | 511.83 | 498.665 | 0.0593 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1046.85 |  | 1034.6376 | 1.1804 | 1001.82 | 982.21 | 0.0516 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.47 |  | 693.4648 | 0.5776 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.685 |  | 45.3096 | 0.8285 | 44.92 | 43.715 | 0.0438 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.515 |  | 744.494 | 0.1371 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.37 |  | 247.8663 | 0.2032 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.685 |  | 71.4811 | 3.0832 | 71.24 | 68.65 | 0.285 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.4146 | 1.3493 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 68.1 |  | 66.7378 | 2.0412 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| 12 | ANET | ai_networking_optical | 165.98 |  | 163.1501 | 1.7346 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 400.055 |  | 395.4424 | 1.1664 | 394.11 | 386.02 | 1.4048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AVGO | custom_silicon_networking | 371.245 |  | 368.0877 | 0.8577 | 368.42 | 357.97 | 1.0586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMAT | semiconductor_equipment | 541.44 |  | 529.2995 | 2.2937 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMD | ai_accelerator | 494.82 |  | 481.0382 | 2.865 | 482.43 | 461.04 | 0.7922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1769.04 |  | 1741.0293 | 1.6089 | 1741.99 | 1704.935 | 1.8066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 472.22 |  | 469.1499 | 0.6544 | 469.08 | 460.78 | 3.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | KLAC | semiconductor_equipment | 214.29 |  | 210.3432 | 1.8763 | 210.82 | 204.71 | 1.344 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MU | memory_hbm_storage | 871.33 |  | 850.1975 | 2.4856 | 835.82 | 804.09 | 2.1783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.47 |  | 693.4648 | 0.5776 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.1 |  | 66.7378 | 2.0412 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.78 |  | 202.358 | 1.1969 | 203.41 | 197.98 | 0.0244 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.485 |  | 393.0466 | -0.1429 | 398.39 | 393.52 | 0.1197 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 332.99 |  | 332.5405 | 0.1352 | 334.98 | 331.295 | 0.018 | watch_only | none |
| GOOGL | cloud_ai_capex | 347.33 |  | 345.8472 | 0.4287 | 348.47 | 341.42 | 0.3397 | watch_only | none |
| AMD | ai_accelerator | 494.82 |  | 481.0382 | 2.865 | 482.43 | 461.04 | 0.7922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.055 |  | 395.4424 | 1.1664 | 394.11 | 386.02 | 1.4048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 522.57 |  | 513.2269 | 1.8205 | 511.83 | 498.665 | 0.0593 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.75 |  | 550.137 | 1.5656 | 550 | 536.9 | 0.0877 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.245 |  | 368.0877 | 0.8577 | 368.42 | 357.97 | 1.0586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 871.33 |  | 850.1975 | 2.4856 | 835.82 | 804.09 | 2.1783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 187.51 |  | 184.5694 | 1.5932 | 185.03 | 178.09 | 1.2639 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 393.61 |  | 387.3368 | 1.6196 | 384 | 368.28 | 4.9465 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.685 |  | 45.3096 | 0.8285 | 44.92 | 43.715 | 0.0438 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.275 |  | 24.0224 | 1.0517 | 24.3 | 23.46 | 0.0412 | watch_only | none |
| SPY | market_regime | 745.515 |  | 744.494 | 0.1371 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.83 |  | 294.0003 | -0.0579 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.46 |  | 125.0406 | 1.1351 | 125.02 | 121.79 | 4.8948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.685 |  | 71.4811 | 3.0832 | 71.24 | 68.65 | 0.285 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 291.42 |  | 283.1204 | 2.9315 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.28 |  | 396.7202 | 1.1494 | 389.4 | 382.38 | 3.9399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 631.52 |  | 624.7385 | 1.0855 | 616.75 | 609.05 | 4.3197 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1046.85 |  | 1034.6376 | 1.1804 | 1001.82 | 982.21 | 0.0516 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 472.22 |  | 469.1499 | 0.6544 | 469.08 | 460.78 | 3.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.59 |  | 140.5467 | 0.7423 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.98 |  | 163.1501 | 1.7346 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 277.98 |  | 269.5554 | 3.1254 | 269.59 | 256.24 | 3.6801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 726.77 |  | 701.6333 | 3.5826 | 694.98 | 653.305 | 3.9201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 379.28 |  | 373.5187 | 1.5424 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.77 |  | 98.3473 | 3.4803 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 301.87 |  | 300.1967 | 0.5574 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1769.04 |  | 1741.0293 | 1.6089 | 1741.99 | 1704.935 | 1.8066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 541.44 |  | 529.2995 | 2.2937 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 317.235 |  | 308.5529 | 2.8138 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.29 |  | 210.3432 | 1.8763 | 210.82 | 204.71 | 1.344 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 317.16 |  | 309.9607 | 2.3227 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 272.86 |  | 267.3108 | 2.0759 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.01 |  | 60.5221 | 2.4585 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.32 |  | 48.8514 | 3.0062 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.51 |  | 133.0342 | 2.6127 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 321.2 |  | 315.105 | 1.9343 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 519.545 |  | 521.7436 | -0.4214 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 299.87 |  | 301.2584 | -0.4609 | 304.36 | 299.62 | 0.3902 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.89 |  | 24.8121 | 0.314 | 25.45 | 24.1 | 0.0402 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.485 |  | 33.426 | 0.1765 | 34 | 32.26 | 0.0299 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.4146 | 1.3493 | 20.445 | 19.92 | 0.0967 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1464.85 |  | 1405.836 | 4.1978 | 1393.96 | 1325.48 | 2.0405 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 470.15 |  | 452.662 | 3.8634 | 453.35 | 431.78 | 4.924 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 761.99 |  | 736.8263 | 3.4151 | 724.57 | 702.24 | 3.7809 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.37 |  | 247.8663 | 0.2032 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 630.17 |  | 635.4112 | -0.8249 | 649.07 | 638.97 | 0.292 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 261.93 |  | 255.4264 | 2.5462 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 162.815 |  | 155.9327 | 4.4137 | 151.99 | 145.6 | 0.6572 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
