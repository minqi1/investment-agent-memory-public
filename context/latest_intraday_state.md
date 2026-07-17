# Intraday State

- Generated at: `2026-07-18T03:00:21+08:00`
- Market time ET: `2026-07-17T15:00:22-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'watch_only': 3, 'spread_too_wide_or_missing': 28, 'below_vwap': 12, 'price_stale_or_missing': 2, 'below_opening_15m_low': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.785 |  | 695.6186 | 0.3114 | 693.36 | 686.78 | 0.0616 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 524.23 |  | 518.58 | 1.0895 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.91 |  | 555.1801 | 0.4917 | 550 | 536.9 | 0.0574 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.44 |  | 744.8731 | -0.0581 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.91 |  | 555.1801 | 0.4917 | 550 | 536.9 | 0.0574 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 524.23 |  | 518.58 | 1.0895 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.34 |  | 212.2297 | 0.5232 | 210.82 | 204.71 | 0.0844 | buy_precheck_manual_confirm | none |
| 4 | ETN | data_center_power_cooling | 399.94 |  | 399.7872 | 0.0382 | 389.4 | 382.38 | 0.2075 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.785 |  | 695.6186 | 0.3114 | 693.36 | 686.78 | 0.0616 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.22 |  | 45.6897 | 1.1607 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.36 |  | 126.0366 | 0.2566 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.575 |  | 24.3171 | 1.0607 | 24.3 | 23.46 | 0.0814 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6676 | 1.6568 | 20.445 | 19.92 | 0.0952 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.32 |  | 67.2311 | 1.6197 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.785 |  | 695.6186 | 0.3114 | 693.36 | 686.78 | 0.0616 | buy_precheck_manual_confirm | none |
| 2 | ORCL | cloud_ai_capex | 126.36 |  | 126.0366 | 0.2566 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 203.345 |  | 203.2422 | 0.0506 | 203.41 | 197.98 | 0.0787 | watch_only | none |
| 4 | SMH | semiconductor_index | 557.91 |  | 555.1801 | 0.4917 | 550 | 536.9 | 0.0574 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 213.34 |  | 212.2297 | 0.5232 | 210.82 | 204.71 | 0.0844 | buy_precheck_manual_confirm | none |
| 6 | ETN | data_center_power_cooling | 399.94 |  | 399.7872 | 0.0382 | 389.4 | 382.38 | 0.2075 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 395.175 |  | 393.4525 | 0.4378 | 398.39 | 393.52 | 0.0658 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 25.235 |  | 25.0938 | 0.5628 | 25.45 | 24.1 | 0.0793 | watch_only | none |
| 9 | CIEN | ai_networking_optical | 377.99 |  | 377.8235 | 0.0441 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SMCI | ai_server_oem | 24.575 |  | 24.3171 | 1.0607 | 24.3 | 23.46 | 0.0814 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 524.23 |  | 518.58 | 1.0895 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.22 |  | 45.6897 | 1.1607 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 13 | LRCX | semiconductor_equipment | 312.635 |  | 312.134 | 0.1605 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ASML | semiconductor_equipment | 1762.33 |  | 1757.1324 | 0.2958 | 1741.99 | 1704.935 | 2.954 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 633.05 |  | 630.2697 | 0.4411 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6676 | 1.6568 | 20.445 | 19.92 | 0.0952 | buy_precheck_manual_confirm | none |
| 17 | META | cloud_ai_capex | 646.08 |  | 642.5337 | 0.5519 | 649.07 | 638.97 | 0.7662 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ONTO | semiconductor_test_packaging | 279.51 |  | 277.7478 | 0.6345 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AAPL | mega_cap_platform | 333.925 |  | 332.1721 | 0.5277 | 334.98 | 331.295 | 0.7966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SKHY | memory_hbm_storage | 159.38 |  | 158.9725 | 0.2563 | 151.99 | 145.6 | 2.0078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.91 |  | 555.1801 | 0.4917 | 550 | 536.9 | 0.0574 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 524.23 |  | 518.58 | 1.0895 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.34 |  | 212.2297 | 0.5232 | 210.82 | 204.71 | 0.0844 | buy_precheck_manual_confirm | none |
| 4 | ETN | data_center_power_cooling | 399.94 |  | 399.7872 | 0.0382 | 389.4 | 382.38 | 0.2075 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.785 |  | 695.6186 | 0.3114 | 693.36 | 686.78 | 0.0616 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.22 |  | 45.6897 | 1.1607 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.36 |  | 126.0366 | 0.2566 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.575 |  | 24.3171 | 1.0607 | 24.3 | 23.46 | 0.0814 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6676 | 1.6568 | 20.445 | 19.92 | 0.0952 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.32 |  | 67.2311 | 1.6197 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 396.995 |  | 398.0402 | -0.2626 | 394.11 | 386.02 | 0.4761 | below_vwap | below_vwap,spread_too_wide |
| 12 | TT | data_center_power_cooling | 469.4 |  | 469.7741 | -0.0796 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | SPY | market_regime | 744.44 |  | 744.8731 | -0.0581 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 14 | AMZN | cloud_ai_capex | 247.755 |  | 247.994 | -0.0964 | 247.72 | 243.725 | 0.1493 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1423.01 |  | 1427.999 | -0.3494 | 1393.96 | 1325.48 | 0.5109 | below_vwap | below_vwap,spread_too_wide |
| 16 | ANET | ai_networking_optical | 168.8 |  | 166.2678 | 1.523 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 373.4 |  | 370.3492 | 0.8238 | 368.42 | 357.97 | 1.8961 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 498.1 |  | 486.935 | 2.2929 | 482.43 | 461.04 | 3.68 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1762.33 |  | 1757.1324 | 0.2958 | 1741.99 | 1704.935 | 2.954 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MU | memory_hbm_storage | 871.28 |  | 864.5795 | 0.775 | 835.82 | 804.09 | 1.7526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.785 |  | 695.6186 | 0.3114 | 693.36 | 686.78 | 0.0616 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.32 |  | 67.2311 | 1.6197 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.345 |  | 203.2422 | 0.0506 | 203.41 | 197.98 | 0.0787 | watch_only | none |
| MSFT | cloud_ai_capex | 395.175 |  | 393.4525 | 0.4378 | 398.39 | 393.52 | 0.0658 | watch_only | none |
| AAPL | mega_cap_platform | 333.925 |  | 332.1721 | 0.5277 | 334.98 | 331.295 | 0.7966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 344.86 |  | 345.8027 | -0.2726 | 348.47 | 341.42 | 0.6756 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 498.1 |  | 486.935 | 2.2929 | 482.43 | 461.04 | 3.68 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.995 |  | 398.0402 | -0.2626 | 394.11 | 386.02 | 0.4761 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524.23 |  | 518.58 | 1.0895 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.91 |  | 555.1801 | 0.4917 | 550 | 536.9 | 0.0574 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.4 |  | 370.3492 | 0.8238 | 368.42 | 357.97 | 1.8961 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 871.28 |  | 864.5795 | 0.775 | 835.82 | 804.09 | 1.7526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.6 |  | 187.2149 | 1.274 | 185.03 | 178.09 | 0.4008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.735 |  | 393.3137 | 2.1411 | 384 | 368.28 | 0.4929 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.22 |  | 45.6897 | 1.1607 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.575 |  | 24.3171 | 1.0607 | 24.3 | 23.46 | 0.0814 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.44 |  | 744.8731 | -0.0581 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.82 |  | 294.1482 | -0.1116 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.36 |  | 126.0366 | 0.2566 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.73 |  | 72.2419 | 2.0599 | 71.24 | 68.65 | 1.7632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 291.57 |  | 287.4335 | 1.4391 | 280.565 | 273.17 | 4.6061 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 399.94 |  | 399.7872 | 0.0382 | 389.4 | 382.38 | 0.2075 | buy_precheck_manual_confirm | none |
| PWR | data_center_power_cooling | 633.05 |  | 630.2697 | 0.4411 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1054.16 |  | 1045.3133 | 0.8463 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.4 |  | 469.7741 | -0.0796 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.75 |  | 140.9532 | -0.1442 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.8 |  | 166.2678 | 1.523 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.48 |  | 274.127 | 1.5879 | 269.59 | 256.24 | 0.5745 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 736.26 |  | 718.5115 | 2.4702 | 694.98 | 653.305 | 3.841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.99 |  | 377.8235 | 0.0441 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 102.2 |  | 100.6028 | 1.5877 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 303 |  | 305.0064 | -0.6578 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1762.33 |  | 1757.1324 | 0.2958 | 1741.99 | 1704.935 | 2.954 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 533.9 |  | 535.1042 | -0.225 | 535.095 | 513.34 | 0.3821 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 312.635 |  | 312.134 | 0.1605 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.34 |  | 212.2297 | 0.5232 | 210.82 | 204.71 | 0.0844 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.06 |  | 320.1818 | 1.2113 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.51 |  | 277.7478 | 0.6345 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.58 |  | 61.528 | 1.7097 | 60.51 | 57.99 | 4.2985 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 51.03 |  | 49.9361 | 2.1905 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.35 |  | 134.9648 | 1.7673 | 129.93 | 126.945 | 4.8562 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.275 |  | 318.9217 | 1.9921 | 315.89 | 307.13 | 4.0919 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.41 |  | 518.9198 | -0.8691 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.97 |  | 298.861 | -0.9673 | 304.36 | 299.62 | 4.7099 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| APLD | high_beta_ai_infrastructure | 25.235 |  | 25.0938 | 0.5628 | 25.45 | 24.1 | 0.0793 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.615 |  | 33.7849 | -0.5028 | 34 | 32.26 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6676 | 1.6568 | 20.445 | 19.92 | 0.0952 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1423.01 |  | 1427.999 | -0.3494 | 1393.96 | 1325.48 | 0.5109 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.31 |  | 467.4188 | 2.758 | 453.35 | 431.78 | 2.6733 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 789.03 |  | 762.0204 | 3.5445 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.755 |  | 247.994 | -0.0964 | 247.72 | 243.725 | 0.1493 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.08 |  | 642.5337 | 0.5519 | 649.07 | 638.97 | 0.7662 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 267.315 |  | 261.2509 | 2.3212 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.38 |  | 158.9725 | 0.2563 | 151.99 | 145.6 | 2.0078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
