# Intraday State

- Generated at: `2026-07-18T02:56:18+08:00`
- Market time ET: `2026-07-17T14:56:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'spread_too_wide_or_missing': 25, 'watch_only': 3, 'below_vwap': 12, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698 |  | 695.6066 | 0.3441 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 524.44 |  | 518.5507 | 1.1357 | 511.83 | 498.665 | 0.0648 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.48 |  | 555.1712 | 0.596 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.45 |  | 744.8757 | -0.0572 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 558.48 |  | 555.1712 | 0.596 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 498.22 |  | 486.9104 | 2.3227 | 482.43 | 461.04 | 0.2649 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.44 |  | 518.5507 | 1.1357 | 511.83 | 498.665 | 0.0648 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 873.29 |  | 864.5336 | 1.0128 | 835.82 | 804.09 | 0.1225 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 402.005 |  | 393.2588 | 2.224 | 384 | 368.28 | 0.2662 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 698 |  | 695.6066 | 0.3441 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.38 |  | 45.6847 | 1.5219 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 8 | LITE | ai_networking_optical | 736.73 |  | 718.2887 | 2.5674 | 694.98 | 653.305 | 0.1575 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189.87 |  | 187.1993 | 1.4267 | 185.03 | 178.09 | 0.2686 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 126.47 |  | 126.0347 | 0.3454 | 125.02 | 121.79 | 0.0553 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.655 |  | 24.3159 | 1.3944 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.025 |  | 20.6661 | 1.7366 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.28 |  | 67.2258 | 1.5682 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 698 |  | 695.6066 | 0.3441 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| 2 | ORCL | cloud_ai_capex | 126.47 |  | 126.0347 | 0.3454 | 125.02 | 121.79 | 0.0553 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 558.48 |  | 555.1712 | 0.596 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 646.755 |  | 642.5135 | 0.6601 | 649.07 | 638.97 | 0.0495 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 394.925 |  | 393.4336 | 0.3791 | 398.39 | 393.52 | 0.0582 | watch_only | none |
| 6 | APLD | high_beta_ai_infrastructure | 25.26 |  | 25.0928 | 0.6663 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| 7 | SMCI | ai_server_oem | 24.655 |  | 24.3159 | 1.3944 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 524.44 |  | 518.5507 | 1.1357 | 511.83 | 498.665 | 0.0648 | buy_precheck_manual_confirm | none |
| 9 | MU | memory_hbm_storage | 873.29 |  | 864.5336 | 1.0128 | 835.82 | 804.09 | 0.1225 | buy_precheck_manual_confirm | none |
| 10 | NVDA | ai_accelerator | 203.52 |  | 203.2419 | 0.1368 | 203.41 | 197.98 | 1.4397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | CIEN | ai_networking_optical | 378.165 |  | 377.8246 | 0.0901 | 375.52 | 359.81 | 1.5496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | MRVL | custom_silicon_networking | 189.87 |  | 187.1993 | 1.4267 | 185.03 | 178.09 | 0.2686 | buy_precheck_manual_confirm | none |
| 13 | ETN | data_center_power_cooling | 400.38 |  | 399.7849 | 0.1489 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | LRCX | semiconductor_equipment | 313.19 |  | 312.1287 | 0.34 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ASML | semiconductor_equipment | 1764.49 |  | 1757.1139 | 0.4198 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | HPE | ai_server_oem | 46.38 |  | 45.6847 | 1.5219 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 17 | AMD | ai_accelerator | 498.22 |  | 486.9104 | 2.3227 | 482.43 | 461.04 | 0.2649 | buy_precheck_manual_confirm | none |
| 18 | CORZ | high_beta_ai_infrastructure | 21.025 |  | 20.6661 | 1.7366 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| 19 | DELL | ai_server_oem | 402.005 |  | 393.2588 | 2.224 | 384 | 368.28 | 0.2662 | buy_precheck_manual_confirm | none |
| 20 | LITE | ai_networking_optical | 736.73 |  | 718.2887 | 2.5674 | 694.98 | 653.305 | 0.1575 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 558.48 |  | 555.1712 | 0.596 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 498.22 |  | 486.9104 | 2.3227 | 482.43 | 461.04 | 0.2649 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.44 |  | 518.5507 | 1.1357 | 511.83 | 498.665 | 0.0648 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 873.29 |  | 864.5336 | 1.0128 | 835.82 | 804.09 | 0.1225 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 402.005 |  | 393.2588 | 2.224 | 384 | 368.28 | 0.2662 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 698 |  | 695.6066 | 0.3441 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.38 |  | 45.6847 | 1.5219 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 8 | LITE | ai_networking_optical | 736.73 |  | 718.2887 | 2.5674 | 694.98 | 653.305 | 0.1575 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189.87 |  | 187.1993 | 1.4267 | 185.03 | 178.09 | 0.2686 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 126.47 |  | 126.0347 | 0.3454 | 125.02 | 121.79 | 0.0553 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.655 |  | 24.3159 | 1.3944 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.025 |  | 20.6661 | 1.7366 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.28 |  | 67.2258 | 1.5682 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| 14 | TSM | foundry | 397.11 |  | 398.0491 | -0.2359 | 394.11 | 386.02 | 0.5565 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 469.3 |  | 469.7793 | -0.102 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 140.87 |  | 140.9549 | -0.0602 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | SPY | market_regime | 744.45 |  | 744.8757 | -0.0572 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 18 | SNDK | memory_hbm_storage | 1424 |  | 1428.0281 | -0.2821 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ANET | ai_networking_optical | 168.9 |  | 166.2122 | 1.6171 | 163.275 | 157.34 | 2.5814 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | NVDA | ai_accelerator | 203.52 |  | 203.2419 | 0.1368 | 203.41 | 197.98 | 1.4397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698 |  | 695.6066 | 0.3441 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.28 |  | 67.2258 | 1.5682 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.52 |  | 203.2419 | 0.1368 | 203.41 | 197.98 | 1.4397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 394.925 |  | 393.4336 | 0.3791 | 398.39 | 393.52 | 0.0582 | watch_only | none |
| AAPL | mega_cap_platform | 334.07 |  | 332.1462 | 0.5792 | 334.98 | 331.295 | 0.901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 344.855 |  | 345.8066 | -0.2752 | 348.47 | 341.42 | 0.2204 | below_vwap | below_vwap |
| AMD | ai_accelerator | 498.22 |  | 486.9104 | 2.3227 | 482.43 | 461.04 | 0.2649 | buy_precheck_manual_confirm | none |
| TSM | foundry | 397.11 |  | 398.0491 | -0.2359 | 394.11 | 386.02 | 0.5565 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524.44 |  | 518.5507 | 1.1357 | 511.83 | 498.665 | 0.0648 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.48 |  | 555.1712 | 0.596 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.665 |  | 370.3251 | 0.9019 | 368.42 | 357.97 | 1.7261 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 873.29 |  | 864.5336 | 1.0128 | 835.82 | 804.09 | 0.1225 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 189.87 |  | 187.1993 | 1.4267 | 185.03 | 178.09 | 0.2686 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 402.005 |  | 393.2588 | 2.224 | 384 | 368.28 | 0.2662 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 46.38 |  | 45.6847 | 1.5219 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.655 |  | 24.3159 | 1.3944 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.45 |  | 744.8757 | -0.0572 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.93 |  | 294.1491 | -0.0745 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.47 |  | 126.0347 | 0.3454 | 125.02 | 121.79 | 0.0553 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.83 |  | 72.2354 | 2.2075 | 71.24 | 68.65 | 1.219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.005 |  | 287.4164 | 1.5965 | 280.565 | 273.17 | 4.6951 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 400.38 |  | 399.7849 | 0.1489 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 633.21 |  | 630.246 | 0.4703 | 616.75 | 609.05 | 4.0982 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1054.73 |  | 1045.2897 | 0.9031 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.3 |  | 469.7793 | -0.102 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.87 |  | 140.9549 | -0.0602 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.9 |  | 166.2122 | 1.6171 | 163.275 | 157.34 | 2.5814 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.31 |  | 274.0687 | 1.5475 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 736.73 |  | 718.2887 | 2.5674 | 694.98 | 653.305 | 0.1575 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 378.165 |  | 377.8246 | 0.0901 | 375.52 | 359.81 | 1.5496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 102.48 |  | 100.5929 | 1.8759 | 97.585 | 91.92 | 4.235 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 303 |  | 305.0588 | -0.6749 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1764.49 |  | 1757.1139 | 0.4198 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 533.67 |  | 535.1101 | -0.2691 | 535.095 | 513.34 | 0.2586 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 313.19 |  | 312.1287 | 0.34 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.625 |  | 212.2235 | 0.6604 | 210.82 | 204.71 | 2.481 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 324.39 |  | 320.1388 | 1.3279 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.275 |  | 277.7184 | 0.9206 | 265.71 | 258.355 | 5.0843 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.62 |  | 61.5239 | 1.7815 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.05 |  | 49.928 | 2.2472 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.35 |  | 134.9648 | 1.7673 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.96 |  | 318.8509 | 1.916 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 514.9 |  | 518.9752 | -0.7852 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.97 |  | 298.861 | -0.9673 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.26 |  | 25.0928 | 0.6663 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.765 |  | 33.7855 | -0.0606 | 34 | 32.26 | 0.0592 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.025 |  | 20.6661 | 1.7366 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1424 |  | 1428.0281 | -0.2821 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 481.52 |  | 467.3808 | 3.0252 | 453.35 | 431.78 | 2.6666 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 787.46 |  | 761.3215 | 3.4333 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.64 |  | 247.9954 | -0.1433 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.755 |  | 642.5135 | 0.6601 | 649.07 | 638.97 | 0.0495 | watch_only | none |
| ARM | ai_accelerator | 267.77 |  | 261.2448 | 2.4977 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 160.615 |  | 158.9524 | 1.046 | 151.99 | 145.6 | 0.7098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
