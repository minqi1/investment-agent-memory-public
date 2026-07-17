# Intraday State

- Generated at: `2026-07-18T03:24:33+08:00`
- Market time ET: `2026-07-17T15:24:34-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 24, 'manual_confirm_candidate': 6, 'watch_only': 4, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.02 |  | 695.6367 | -0.0887 | 693.36 | 686.78 | 0.0072 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 519.91 |  | 518.7036 | 0.2326 | 511.83 | 498.665 | 0.0577 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 554.04 |  | 555.1954 | -0.2081 | 550 | 536.9 | 0.0578 | below_vwap | below_vwap |
| SPY | market_regime | 742.56 |  | 744.7706 | -0.2968 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 519.91 |  | 518.7036 | 0.2326 | 511.83 | 498.665 | 0.0577 | buy_precheck_manual_confirm | none |
| 2 | VRT | data_center_power_cooling | 290.235 |  | 287.6592 | 0.8954 | 280.565 | 273.17 | 0.0689 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 45.95 |  | 45.7058 | 0.5344 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.345 |  | 24.3224 | 0.0929 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.71 |  | 20.6794 | 0.1481 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 67.375 |  | 67.2477 | 0.1894 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 24.345 |  | 24.3224 | 0.0929 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 20.71 |  | 20.6794 | 0.1481 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 519.91 |  | 518.7036 | 0.2326 | 511.83 | 498.665 | 0.0577 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 333.05 |  | 332.3166 | 0.2207 | 334.98 | 331.295 | 0.1081 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 25.175 |  | 25.1045 | 0.2809 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| 6 | META | cloud_ai_capex | 643.5 |  | 642.5773 | 0.1436 | 649.07 | 638.97 | 0.2704 | watch_only | none |
| 7 | HPE | ai_server_oem | 45.95 |  | 45.7058 | 0.5344 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 395.12 |  | 393.5935 | 0.3878 | 398.39 | 393.52 | 0.0253 | watch_only | none |
| 9 | VRT | data_center_power_cooling | 290.235 |  | 287.6592 | 0.8954 | 280.565 | 273.17 | 0.0689 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 370.475 |  | 370.4026 | 0.0196 | 368.42 | 357.97 | 2.5454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ETN | data_center_power_cooling | 399.83 |  | 399.735 | 0.0238 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | MRVL | custom_silicon_networking | 187.38 |  | 187.2652 | 0.0613 | 185.03 | 178.09 | 2.8979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | GEV | data_center_power_cooling | 1051.01 |  | 1045.9493 | 0.4838 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 321.47 |  | 320.3306 | 0.3557 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AMKR | semiconductor_test_packaging | 62.03 |  | 61.6188 | 0.6673 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | QQQ | market_regime | 695.02 |  | 695.6367 | -0.0887 | 693.36 | 686.78 | 0.0072 | below_vwap | below_vwap |
| 17 | TQQQ | leveraged_tool | 67.375 |  | 67.2477 | 0.1894 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |
| 18 | NVDA | ai_accelerator | 202.23 |  | 203.1857 | -0.4704 | 203.41 | 197.98 | 0.0247 | below_vwap | below_vwap |
| 19 | SMH | semiconductor_index | 554.04 |  | 555.1954 | -0.2081 | 550 | 536.9 | 0.0578 | below_vwap | below_vwap |
| 20 | AMAT | semiconductor_equipment | 527.05 |  | 534.2538 | -1.3484 | 535.095 | 513.34 | 0.1063 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 519.91 |  | 518.7036 | 0.2326 | 511.83 | 498.665 | 0.0577 | buy_precheck_manual_confirm | none |
| 2 | VRT | data_center_power_cooling | 290.235 |  | 287.6592 | 0.8954 | 280.565 | 273.17 | 0.0689 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 45.95 |  | 45.7058 | 0.5344 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.345 |  | 24.3224 | 0.0929 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.71 |  | 20.6794 | 0.1481 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 67.375 |  | 67.2477 | 0.1894 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 394.94 |  | 397.8813 | -0.7392 | 394.11 | 386.02 | 0.2051 | below_vwap | below_vwap |
| 8 | SMH | semiconductor_index | 554.04 |  | 555.1954 | -0.2081 | 550 | 536.9 | 0.0578 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1750.14 |  | 1756.8229 | -0.3804 | 1741.99 | 1704.935 | 0.1303 | below_vwap | below_vwap |
| 10 | TT | data_center_power_cooling | 469.33 |  | 469.7243 | -0.0839 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 211.49 |  | 212.2007 | -0.3349 | 210.82 | 204.71 | 4.7094 | below_vwap | below_vwap,spread_too_wide |
| 12 | MU | memory_hbm_storage | 859.26 |  | 864.6457 | -0.6229 | 835.82 | 804.09 | 1.0625 | below_vwap | below_vwap,spread_too_wide |
| 13 | PWR | data_center_power_cooling | 630.17 |  | 630.3003 | -0.0207 | 616.75 | 609.05 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | QQQ | market_regime | 695.02 |  | 695.6367 | -0.0887 | 693.36 | 686.78 | 0.0072 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 310.16 |  | 312.0817 | -0.6158 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 276.62 |  | 277.6914 | -0.3858 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1396.685 |  | 1427.2627 | -2.1424 | 1393.96 | 1325.48 | 3.3759 | below_vwap | below_vwap,spread_too_wide |
| 18 | SKHY | memory_hbm_storage | 154.225 |  | 158.8593 | -2.9172 | 151.99 | 145.6 | 4.8047 | below_vwap | below_vwap,spread_too_wide |
| 19 | ORCL | cloud_ai_capex | 125.865 |  | 126.0326 | -0.133 | 125.02 | 121.79 | 0.2622 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 167.73 |  | 166.3484 | 0.8306 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.02 |  | 695.6367 | -0.0887 | 693.36 | 686.78 | 0.0072 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.375 |  | 67.2477 | 0.1894 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.23 |  | 203.1857 | -0.4704 | 203.41 | 197.98 | 0.0247 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 395.12 |  | 393.5935 | 0.3878 | 398.39 | 393.52 | 0.0253 | watch_only | none |
| AAPL | mega_cap_platform | 333.05 |  | 332.3166 | 0.2207 | 334.98 | 331.295 | 0.1081 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.04 |  | 345.7656 | -0.2099 | 348.47 | 341.42 | 0.029 | below_vwap | below_vwap |
| AMD | ai_accelerator | 493.535 |  | 487.1412 | 1.3125 | 482.43 | 461.04 | 2.8103 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.94 |  | 397.8813 | -0.7392 | 394.11 | 386.02 | 0.2051 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 519.91 |  | 518.7036 | 0.2326 | 511.83 | 498.665 | 0.0577 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 554.04 |  | 555.1954 | -0.2081 | 550 | 536.9 | 0.0578 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 370.475 |  | 370.4026 | 0.0196 | 368.42 | 357.97 | 2.5454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 859.26 |  | 864.6457 | -0.6229 | 835.82 | 804.09 | 1.0625 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.38 |  | 187.2652 | 0.0613 | 185.03 | 178.09 | 2.8979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 397.345 |  | 393.5635 | 0.9608 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.95 |  | 45.7058 | 0.5344 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.345 |  | 24.3224 | 0.0929 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.56 |  | 744.7706 | -0.2968 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.205 |  | 294.1057 | -0.3063 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.865 |  | 126.0326 | -0.133 | 125.02 | 121.79 | 0.2622 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.56 |  | 72.2842 | 0.3815 | 71.24 | 68.65 | 4.548 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.235 |  | 287.6592 | 0.8954 | 280.565 | 273.17 | 0.0689 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 399.83 |  | 399.735 | 0.0238 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 630.17 |  | 630.3003 | -0.0207 | 616.75 | 609.05 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1051.01 |  | 1045.9493 | 0.4838 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.33 |  | 469.7243 | -0.0839 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.73 |  | 140.923 | -0.137 | 140.765 | 137.165 | 0.0782 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 167.73 |  | 166.3484 | 0.8306 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 277.235 |  | 274.2761 | 1.0788 | 269.59 | 256.24 | 3.2536 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 734.01 |  | 719.2478 | 2.0524 | 694.98 | 653.305 | 1.7166 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.425 |  | 377.705 | -0.6037 | 375.52 | 359.81 | 4.0701 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.22 |  | 100.6783 | 1.5313 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 300.71 |  | 304.6794 | -1.3028 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1750.14 |  | 1756.8229 | -0.3804 | 1741.99 | 1704.935 | 0.1303 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 527.05 |  | 534.2538 | -1.3484 | 535.095 | 513.34 | 0.1063 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 310.16 |  | 312.0817 | -0.6158 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 211.49 |  | 212.2007 | -0.3349 | 210.82 | 204.71 | 4.7094 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 321.47 |  | 320.3306 | 0.3557 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 276.62 |  | 277.6914 | -0.3858 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.03 |  | 61.6188 | 0.6673 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.76 |  | 49.9891 | 1.5422 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.46 |  | 135.1594 | 0.9623 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 323.99 |  | 319.1849 | 1.5054 | 315.89 | 307.13 | 3.994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.595 |  | 518.4515 | -0.9367 | 526.74 | 522.205 | 0.3057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.87 |  | 298.7104 | -0.9509 | 304.36 | 299.62 | 4.1099 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.175 |  | 25.1045 | 0.2809 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.325 |  | 33.7573 | -1.2805 | 34 | 32.26 | 0.03 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.71 |  | 20.6794 | 0.1481 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1396.685 |  | 1427.2627 | -2.1424 | 1393.96 | 1325.48 | 3.3759 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 478.08 |  | 467.8848 | 2.179 | 453.35 | 431.78 | 4.7963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 787.24 |  | 765.1199 | 2.8911 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.45 |  | 247.9744 | -0.2115 | 247.72 | 243.725 | 0.1293 | below_vwap | below_vwap |
| META | cloud_ai_capex | 643.5 |  | 642.5773 | 0.1436 | 649.07 | 638.97 | 0.2704 | watch_only | none |
| ARM | ai_accelerator | 266.28 |  | 261.5776 | 1.7977 | 252.95 | 243.21 | 2.1819 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 154.225 |  | 158.8593 | -2.9172 | 151.99 | 145.6 | 4.8047 | below_vwap | below_vwap,spread_too_wide |
