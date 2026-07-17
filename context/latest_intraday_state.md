# Intraday State

- Generated at: `2026-07-17T22:43:36+08:00`
- Market time ET: `2026-07-17T10:43:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 3, 'watch_only': 5, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_vwap': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.53 |  | 692.9252 | 0.6645 | 693.36 | 686.78 | 0.0502 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 519.67 |  | 512.0113 | 1.4958 | 511.83 | 498.665 | 0.1251 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.565 |  | 549.3946 | 1.1231 | 550 | 536.9 | 0.045 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.23 |  | 744.205 | 0.2721 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.5 |  | 201.8699 | 0.8075 | 203.41 | 197.98 | 0.0197 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 400.69 |  | 394.0954 | 1.6734 | 394.11 | 386.02 | 0.1772 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.565 |  | 549.3946 | 1.1231 | 550 | 536.9 | 0.045 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 371.71 |  | 367.7544 | 1.0756 | 368.42 | 357.97 | 0.1614 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 519.67 |  | 512.0113 | 1.4958 | 511.83 | 498.665 | 0.1251 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 871.93 |  | 846.1783 | 3.0433 | 835.82 | 804.09 | 0.258 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.33 |  | 294.0043 | 0.4509 | 294.205 | 291.675 | 0.0169 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 697.53 |  | 692.9252 | 0.6645 | 693.36 | 686.78 | 0.0502 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 45.59 |  | 45.188 | 0.8897 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 10 | SPY | market_regime | 746.23 |  | 744.205 | 0.2721 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 466.09 |  | 450.0305 | 3.5685 | 453.35 | 431.78 | 0.2939 | buy_precheck_manual_confirm | none |
| 12 | AMZN | cloud_ai_capex | 249.61 |  | 247.3061 | 0.9316 | 247.72 | 243.725 | 0.02 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.575 |  | 20.2845 | 1.4323 | 20.445 | 19.92 | 0.1944 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 67.99 |  | 66.524 | 2.2037 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.23 |  | 744.205 | 0.2721 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 295.33 |  | 294.0043 | 0.4509 | 294.205 | 291.675 | 0.0169 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 697.53 |  | 692.9252 | 0.6645 | 693.36 | 686.78 | 0.0502 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 346.53 |  | 345.3965 | 0.3282 | 348.47 | 341.42 | 0.1154 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 332.85 |  | 332 | 0.256 | 334.98 | 331.295 | 0.1923 | watch_only | none |
| 6 | NVDA | ai_accelerator | 203.5 |  | 201.8699 | 0.8075 | 203.41 | 197.98 | 0.0197 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.14 |  | 24.0221 | 0.4908 | 24.3 | 23.46 | 0.0829 | watch_only | none |
| 8 | IREN | high_beta_ai_infrastructure | 33.6 |  | 33.4094 | 0.5704 | 34 | 32.26 | 0.0595 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 249.61 |  | 247.3061 | 0.9316 | 247.72 | 243.725 | 0.02 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 555.565 |  | 549.3946 | 1.1231 | 550 | 536.9 | 0.045 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 45.59 |  | 45.188 | 0.8897 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 12 | AVGO | custom_silicon_networking | 371.71 |  | 367.7544 | 1.0756 | 368.42 | 357.97 | 0.1614 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.575 |  | 20.2845 | 1.4323 | 20.445 | 19.92 | 0.1944 | buy_precheck_manual_confirm | none |
| 14 | SOXX | semiconductor_index | 519.67 |  | 512.0113 | 1.4958 | 511.83 | 498.665 | 0.1251 | buy_precheck_manual_confirm | none |
| 15 | TT | data_center_power_cooling | 469.7 |  | 468.2468 | 0.3104 | 469.08 | 460.78 | 4.1857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | APLD | high_beta_ai_infrastructure | 25.08 |  | 24.8003 | 1.1278 | 25.45 | 24.1 | 0.1196 | watch_only | none |
| 17 | KLAC | semiconductor_equipment | 211.92 |  | 210.3258 | 0.758 | 210.82 | 204.71 | 1.7412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TSM | foundry | 400.69 |  | 394.0954 | 1.6734 | 394.11 | 386.02 | 0.1772 | buy_precheck_manual_confirm | none |
| 19 | MU | memory_hbm_storage | 871.93 |  | 846.1783 | 3.0433 | 835.82 | 804.09 | 0.258 | buy_precheck_manual_confirm | none |
| 20 | JCI | data_center_power_cooling | 140.99 |  | 139.6575 | 0.9541 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.5 |  | 201.8699 | 0.8075 | 203.41 | 197.98 | 0.0197 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 400.69 |  | 394.0954 | 1.6734 | 394.11 | 386.02 | 0.1772 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.565 |  | 549.3946 | 1.1231 | 550 | 536.9 | 0.045 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 371.71 |  | 367.7544 | 1.0756 | 368.42 | 357.97 | 0.1614 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 519.67 |  | 512.0113 | 1.4958 | 511.83 | 498.665 | 0.1251 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 871.93 |  | 846.1783 | 3.0433 | 835.82 | 804.09 | 0.258 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.33 |  | 294.0043 | 0.4509 | 294.205 | 291.675 | 0.0169 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 697.53 |  | 692.9252 | 0.6645 | 693.36 | 686.78 | 0.0502 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 45.59 |  | 45.188 | 0.8897 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 10 | SPY | market_regime | 746.23 |  | 744.205 | 0.2721 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 466.09 |  | 450.0305 | 3.5685 | 453.35 | 431.78 | 0.2939 | buy_precheck_manual_confirm | none |
| 12 | AMZN | cloud_ai_capex | 249.61 |  | 247.3061 | 0.9316 | 247.72 | 243.725 | 0.02 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.575 |  | 20.2845 | 1.4323 | 20.445 | 19.92 | 0.1944 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 67.99 |  | 66.524 | 2.2037 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 165.74 |  | 162.562 | 1.9549 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMD | ai_accelerator | 490.485 |  | 477.064 | 2.8133 | 482.43 | 461.04 | 1.7371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1749.175 |  | 1733.7995 | 0.8868 | 1741.99 | 1704.935 | 0.7038 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 469.7 |  | 468.2468 | 0.3104 | 469.08 | 460.78 | 4.1857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | KLAC | semiconductor_equipment | 211.92 |  | 210.3258 | 0.758 | 210.82 | 204.71 | 1.7412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | VRT | data_center_power_cooling | 286.86 |  | 281.7038 | 1.8303 | 280.565 | 273.17 | 3.5941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.53 |  | 692.9252 | 0.6645 | 693.36 | 686.78 | 0.0502 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.99 |  | 66.524 | 2.2037 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.5 |  | 201.8699 | 0.8075 | 203.41 | 197.98 | 0.0197 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 391.71 |  | 394.1994 | -0.6315 | 398.39 | 393.52 | 0.097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 332.85 |  | 332 | 0.256 | 334.98 | 331.295 | 0.1923 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.53 |  | 345.3965 | 0.3282 | 348.47 | 341.42 | 0.1154 | watch_only | none |
| AMD | ai_accelerator | 490.485 |  | 477.064 | 2.8133 | 482.43 | 461.04 | 1.7371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.69 |  | 394.0954 | 1.6734 | 394.11 | 386.02 | 0.1772 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 519.67 |  | 512.0113 | 1.4958 | 511.83 | 498.665 | 0.1251 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.565 |  | 549.3946 | 1.1231 | 550 | 536.9 | 0.045 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.71 |  | 367.7544 | 1.0756 | 368.42 | 357.97 | 0.1614 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 871.93 |  | 846.1783 | 3.0433 | 835.82 | 804.09 | 0.258 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 186.74 |  | 184.378 | 1.2811 | 185.03 | 178.09 | 0.7069 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 395.65 |  | 385.1256 | 2.7327 | 384 | 368.28 | 4.7593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.59 |  | 45.188 | 0.8897 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.14 |  | 24.0221 | 0.4908 | 24.3 | 23.46 | 0.0829 | watch_only | none |
| SPY | market_regime | 746.23 |  | 744.205 | 0.2721 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.33 |  | 294.0043 | 0.4509 | 294.205 | 291.675 | 0.0169 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.86 |  | 124.7625 | 0.8797 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 73.78 |  | 70.9735 | 3.9542 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 286.86 |  | 281.7038 | 1.8303 | 280.565 | 273.17 | 3.5941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 398.08 |  | 395.617 | 0.6226 | 389.4 | 382.38 | 2.2257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 628.37 |  | 622.5026 | 0.9425 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1044.44 |  | 1023.806 | 2.0154 | 1001.82 | 982.21 | 1.2121 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.7 |  | 468.2468 | 0.3104 | 469.08 | 460.78 | 4.1857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.99 |  | 139.6575 | 0.9541 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.74 |  | 162.562 | 1.9549 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.205 |  | 267.8081 | 3.1354 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 723.58 |  | 695.5219 | 4.0341 | 694.98 | 653.305 | 4.8661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 381.42 |  | 372.4075 | 2.4201 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.43 |  | 97.5725 | 3.9535 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.125 |  | 300.4006 | 1.2398 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1749.175 |  | 1733.7995 | 0.8868 | 1741.99 | 1704.935 | 0.7038 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 534.765 |  | 527.7215 | 1.3347 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 313.465 |  | 305.8746 | 2.4816 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 211.92 |  | 210.3258 | 0.758 | 210.82 | 204.71 | 1.7412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 315.905 |  | 308.7891 | 2.3044 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 271.03 |  | 266.2782 | 1.7845 | 265.71 | 258.355 | 4.6895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 61.285 |  | 60.0126 | 2.1202 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.83 |  | 48.4222 | 2.9074 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.37 |  | 132.2747 | 2.34 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 319.64 |  | 314.4166 | 1.6613 | 315.89 | 307.13 | 4.6208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 521.09 |  | 521.8278 | -0.1414 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.2 |  | 301.6519 | -0.1498 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.08 |  | 24.8003 | 1.1278 | 25.45 | 24.1 | 0.1196 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.6 |  | 33.4094 | 0.5704 | 34 | 32.26 | 0.0595 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.575 |  | 20.2845 | 1.4323 | 20.445 | 19.92 | 0.1944 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1438.95 |  | 1399.3173 | 2.8323 | 1393.96 | 1325.48 | 1.4955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 466.09 |  | 450.0305 | 3.5685 | 453.35 | 431.78 | 0.2939 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 757.68 |  | 731.1377 | 3.6303 | 724.57 | 702.24 | 4.5653 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 249.61 |  | 247.3061 | 0.9316 | 247.72 | 243.725 | 0.02 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 635.135 |  | 638.8757 | -0.5855 | 649.07 | 638.97 | 0.9085 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 263.39 |  | 253.9795 | 3.7052 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 157.37 |  | 154.9074 | 1.5897 | 151.99 | 145.6 | 2.618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
