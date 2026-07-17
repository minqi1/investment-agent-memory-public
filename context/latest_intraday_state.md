# Intraday State

- Generated at: `2026-07-17T23:24:49+08:00`
- Market time ET: `2026-07-17T11:24:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'watch_only': 4, 'below_opening_15m_low': 3, 'spread_too_wide_or_missing': 32, 'price_stale_or_missing': 1, 'below_vwap': 9}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.66 |  | 693.2039 | 0.0658 | 693.36 | 686.78 | 0.0317 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 514.8 |  | 512.4277 | 0.4629 | 511.83 | 498.665 | 0.0952 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 551.84 |  | 549.8441 | 0.363 | 550 | 536.9 | 0.0924 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.19 |  | 744.3868 | -0.0264 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 551.84 |  | 549.8441 | 0.363 | 550 | 536.9 | 0.0924 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 514.8 |  | 512.4277 | 0.4629 | 511.83 | 498.665 | 0.0952 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 693.66 |  | 693.2039 | 0.0658 | 693.36 | 686.78 | 0.0317 | buy_precheck_manual_confirm | none |
| 4 | LRCX | semiconductor_equipment | 310.41 |  | 307.3542 | 0.9942 | 306.51 | 298.89 | 0.1772 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 248.34 |  | 247.7303 | 0.2461 | 247.72 | 243.725 | 0.0564 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.3308 | 0.6846 | 20.445 | 19.92 | 0.0489 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 66.99 |  | 66.6541 | 0.5039 | 66.9 | 64.92 | 0.0299 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 693.66 |  | 693.2039 | 0.0658 | 693.36 | 686.78 | 0.0317 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.34 |  | 247.7303 | 0.2461 | 247.72 | 243.725 | 0.0564 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 551.84 |  | 549.8441 | 0.363 | 550 | 536.9 | 0.0924 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 514.8 |  | 512.4277 | 0.4629 | 511.83 | 498.665 | 0.0952 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.3308 | 0.6846 | 20.445 | 19.92 | 0.0489 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.44 |  | 33.4205 | 0.0583 | 34 | 32.26 | 0.0299 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 346.25 |  | 345.5985 | 0.1885 | 348.47 | 341.42 | 0.2022 | watch_only | none |
| 8 | NVDA | ai_accelerator | 203.37 |  | 202.1613 | 0.5979 | 203.41 | 197.98 | 0.0098 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 333.56 |  | 332.2573 | 0.3921 | 334.98 | 331.295 | 0.021 | watch_only | none |
| 10 | TT | data_center_power_cooling | 469.98 |  | 468.8677 | 0.2372 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ORCL | cloud_ai_capex | 125.31 |  | 124.8835 | 0.3415 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ALAB | ai_networking_optical | 300.88 |  | 300.2187 | 0.2203 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 310.41 |  | 307.3542 | 0.9942 | 306.51 | 298.89 | 0.1772 | buy_precheck_manual_confirm | none |
| 14 | TER | semiconductor_test_packaging | 310.4 |  | 309.4968 | 0.2918 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 141.1 |  | 140.384 | 0.51 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMAT | semiconductor_equipment | 531.85 |  | 528.7345 | 0.5892 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | CIEN | ai_networking_optical | 374.6 |  | 373.2204 | 0.3697 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 369.24 |  | 367.9435 | 0.3524 | 368.42 | 357.97 | 3.0468 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1746.79 |  | 1736.5445 | 0.59 | 1741.99 | 1704.935 | 0.7665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | DELL | ai_server_oem | 389.54 |  | 386.799 | 0.7086 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 551.84 |  | 549.8441 | 0.363 | 550 | 536.9 | 0.0924 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 514.8 |  | 512.4277 | 0.4629 | 511.83 | 498.665 | 0.0952 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 693.66 |  | 693.2039 | 0.0658 | 693.36 | 686.78 | 0.0317 | buy_precheck_manual_confirm | none |
| 4 | LRCX | semiconductor_equipment | 310.41 |  | 307.3542 | 0.9942 | 306.51 | 298.89 | 0.1772 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 248.34 |  | 247.7303 | 0.2461 | 247.72 | 243.725 | 0.0564 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.3308 | 0.6846 | 20.445 | 19.92 | 0.0489 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 66.99 |  | 66.6541 | 0.5039 | 66.9 | 64.92 | 0.0299 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.28 |  | 45.2853 | -0.0116 | 44.92 | 43.715 | 0.0221 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 744.19 |  | 744.3868 | -0.0264 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 10 | ANET | ai_networking_optical | 165.08 |  | 162.9182 | 1.3269 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TSM | foundry | 396.46 |  | 394.9866 | 0.373 | 394.11 | 386.02 | 0.5902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | AVGO | custom_silicon_networking | 369.24 |  | 367.9435 | 0.3524 | 368.42 | 357.97 | 3.0468 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | AMD | ai_accelerator | 485.14 |  | 478.5079 | 1.386 | 482.43 | 461.04 | 0.9688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ASML | semiconductor_equipment | 1746.79 |  | 1736.5445 | 0.59 | 1741.99 | 1704.935 | 0.7665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 469.98 |  | 468.8677 | 0.2372 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MU | memory_hbm_storage | 852.795 |  | 848.6904 | 0.4836 | 835.82 | 804.09 | 1.4236 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | VRT | data_center_power_cooling | 286.63 |  | 282.5592 | 1.4407 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 141.1 |  | 140.384 | 0.51 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 397.64 |  | 395.9569 | 0.4251 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | GEV | data_center_power_cooling | 1039.32 |  | 1026.6263 | 1.2364 | 1001.82 | 982.21 | 0.7024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.66 |  | 693.2039 | 0.0658 | 693.36 | 686.78 | 0.0317 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 66.99 |  | 66.6541 | 0.5039 | 66.9 | 64.92 | 0.0299 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.37 |  | 202.1613 | 0.5979 | 203.41 | 197.98 | 0.0098 | watch_only | none |
| MSFT | cloud_ai_capex | 389.9 |  | 393.3226 | -0.8702 | 398.39 | 393.52 | 0.2565 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.56 |  | 332.2573 | 0.3921 | 334.98 | 331.295 | 0.021 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.25 |  | 345.5985 | 0.1885 | 348.47 | 341.42 | 0.2022 | watch_only | none |
| AMD | ai_accelerator | 485.14 |  | 478.5079 | 1.386 | 482.43 | 461.04 | 0.9688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.46 |  | 394.9866 | 0.373 | 394.11 | 386.02 | 0.5902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 514.8 |  | 512.4277 | 0.4629 | 511.83 | 498.665 | 0.0952 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 551.84 |  | 549.8441 | 0.363 | 550 | 536.9 | 0.0924 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 369.24 |  | 367.9435 | 0.3524 | 368.42 | 357.97 | 3.0468 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 852.795 |  | 848.6904 | 0.4836 | 835.82 | 804.09 | 1.4236 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 184.08 |  | 184.4781 | -0.2158 | 185.03 | 178.09 | 2.2273 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 389.54 |  | 386.799 | 0.7086 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.28 |  | 45.2853 | -0.0116 | 44.92 | 43.715 | 0.0221 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 23.98 |  | 24.0124 | -0.1351 | 24.3 | 23.46 | 0.0834 | below_vwap | below_vwap |
| SPY | market_regime | 744.19 |  | 744.3868 | -0.0264 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.58 |  | 294.064 | -0.1646 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.31 |  | 124.8835 | 0.3415 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 72.63 |  | 71.2882 | 1.8822 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 286.63 |  | 282.5592 | 1.4407 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 397.64 |  | 395.9569 | 0.4251 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 626.27 |  | 623.6639 | 0.4179 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1039.32 |  | 1026.6263 | 1.2364 | 1001.82 | 982.21 | 0.7024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.98 |  | 468.8677 | 0.2372 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.1 |  | 140.384 | 0.51 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.08 |  | 162.9182 | 1.3269 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 273.61 |  | 268.8472 | 1.7716 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 716.055 |  | 699.1329 | 2.4204 | 694.98 | 653.305 | 0.8994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 374.6 |  | 373.2204 | 0.3697 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 99.63 |  | 98.1239 | 1.5349 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 300.88 |  | 300.2187 | 0.2203 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1746.79 |  | 1736.5445 | 0.59 | 1741.99 | 1704.935 | 0.7665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.85 |  | 528.7345 | 0.5892 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 310.41 |  | 307.3542 | 0.9942 | 306.51 | 298.89 | 0.1772 | buy_precheck_manual_confirm | none |
| KLAC | semiconductor_equipment | 209.17 |  | 210.2429 | -0.5103 | 210.82 | 204.71 | 3.5665 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 310.4 |  | 309.4968 | 0.2918 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 269.77 |  | 266.9181 | 1.0684 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.02 |  | 60.2473 | 1.2826 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.46 |  | 48.6033 | 1.7626 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135 |  | 132.7767 | 1.6745 | 129.93 | 126.945 | 3.8963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 318.99 |  | 314.9149 | 1.294 | 315.89 | 307.13 | 0.4044 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 520.83 |  | 521.811 | -0.188 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.22 |  | 301.541 | -0.1065 | 304.36 | 299.62 | 2.3206 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.75 |  | 24.8083 | -0.2349 | 25.45 | 24.1 | 0.0404 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.44 |  | 33.4205 | 0.0583 | 34 | 32.26 | 0.0299 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.3308 | 0.6846 | 20.445 | 19.92 | 0.0489 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1411.98 |  | 1401.2731 | 0.7641 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 457.325 |  | 452.0284 | 1.1717 | 453.35 | 431.78 | 4.4542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 748 |  | 735.2515 | 1.7339 | 724.57 | 702.24 | 4.3128 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.34 |  | 247.7303 | 0.2461 | 247.72 | 243.725 | 0.0564 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 628.67 |  | 636.1126 | -1.17 | 649.07 | 638.97 | 0.7762 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 259.505 |  | 254.9582 | 1.7833 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 155.12 |  | 154.9841 | 0.0877 | 151.99 | 145.6 | 1.6117 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
