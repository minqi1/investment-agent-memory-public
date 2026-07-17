# Intraday State

- Generated at: `2026-07-18T03:04:23+08:00`
- Market time ET: `2026-07-17T15:04:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_vwap': 16, 'watch_only': 3, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 2, 'below_opening_15m_low': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.3 |  | 695.6272 | 0.2405 | 693.36 | 686.78 | 0.0316 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.26 |  | 518.6152 | 0.8956 | 511.83 | 498.665 | 0.0784 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.15 |  | 555.2054 | 0.3502 | 550 | 536.9 | 0.0736 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.92 |  | 744.8668 | -0.1271 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.15 |  | 555.2054 | 0.3502 | 550 | 536.9 | 0.0736 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.26 |  | 518.6152 | 0.8956 | 511.83 | 498.665 | 0.0784 | buy_precheck_manual_confirm | none |
| 3 | PWR | data_center_power_cooling | 632.12 |  | 630.296 | 0.2894 | 616.75 | 609.05 | 0.242 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.3 |  | 695.6272 | 0.2405 | 693.36 | 686.78 | 0.0316 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.225 |  | 45.6944 | 1.1611 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | AMKR | semiconductor_test_packaging | 62.595 |  | 61.5851 | 1.6399 | 60.51 | 57.99 | 0.3195 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.145 |  | 126.0387 | 0.0843 | 125.02 | 121.79 | 0.3171 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.575 |  | 24.3184 | 1.0554 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6684 | 1.6528 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.02 |  | 67.238 | 1.163 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.3 |  | 695.6272 | 0.2405 | 693.36 | 686.78 | 0.0316 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 557.15 |  | 555.2054 | 0.3502 | 550 | 536.9 | 0.0736 | buy_precheck_manual_confirm | none |
| 3 | ORCL | cloud_ai_capex | 126.145 |  | 126.0387 | 0.0843 | 125.02 | 121.79 | 0.3171 | buy_precheck_manual_confirm | none |
| 4 | PWR | data_center_power_cooling | 632.12 |  | 630.296 | 0.2894 | 616.75 | 609.05 | 0.242 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 644.44 |  | 642.5631 | 0.2921 | 649.07 | 638.97 | 0.2141 | watch_only | none |
| 6 | MSFT | cloud_ai_capex | 394.93 |  | 393.4759 | 0.3695 | 398.39 | 393.52 | 0.0532 | watch_only | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.205 |  | 25.0944 | 0.4406 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.575 |  | 24.3184 | 1.0554 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 9 | SOXX | semiconductor_index | 523.26 |  | 518.6152 | 0.8956 | 511.83 | 498.665 | 0.0784 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1759.69 |  | 1757.1486 | 0.1446 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | HPE | ai_server_oem | 46.225 |  | 45.6944 | 1.1611 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 213.02 |  | 212.2374 | 0.3688 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1052.27 |  | 1045.4191 | 0.6553 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6684 | 1.6528 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| 15 | ONTO | semiconductor_test_packaging | 278.805 |  | 277.7559 | 0.3777 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AVGO | custom_silicon_networking | 372.75 |  | 370.3633 | 0.6444 | 368.42 | 357.97 | 1.9531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AAPL | mega_cap_platform | 334.07 |  | 332.1986 | 0.5633 | 334.98 | 331.295 | 0.8322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SKHY | memory_hbm_storage | 159.5 |  | 158.9781 | 0.3283 | 151.99 | 145.6 | 1.5298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMKR | semiconductor_test_packaging | 62.595 |  | 61.5851 | 1.6399 | 60.51 | 57.99 | 0.3195 | buy_precheck_manual_confirm | none |
| 20 | MU | memory_hbm_storage | 870.09 |  | 864.6376 | 0.6306 | 835.82 | 804.09 | 1.755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.15 |  | 555.2054 | 0.3502 | 550 | 536.9 | 0.0736 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.26 |  | 518.6152 | 0.8956 | 511.83 | 498.665 | 0.0784 | buy_precheck_manual_confirm | none |
| 3 | PWR | data_center_power_cooling | 632.12 |  | 630.296 | 0.2894 | 616.75 | 609.05 | 0.242 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.3 |  | 695.6272 | 0.2405 | 693.36 | 686.78 | 0.0316 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.225 |  | 45.6944 | 1.1611 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | AMKR | semiconductor_test_packaging | 62.595 |  | 61.5851 | 1.6399 | 60.51 | 57.99 | 0.3195 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.145 |  | 126.0387 | 0.0843 | 125.02 | 121.79 | 0.3171 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.575 |  | 24.3184 | 1.0554 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6684 | 1.6528 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.02 |  | 67.238 | 1.163 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 396.16 |  | 398.0202 | -0.4674 | 394.11 | 386.02 | 0.4998 | below_vwap | below_vwap,spread_too_wide |
| 12 | CIEN | ai_networking_optical | 377.34 |  | 377.8214 | -0.1274 | 375.52 | 359.81 | 1.341 | below_vwap | below_vwap,spread_too_wide |
| 13 | ETN | data_center_power_cooling | 399.365 |  | 399.7835 | -0.1047 | 389.4 | 382.38 | 0.1578 | below_vwap | below_vwap |
| 14 | LRCX | semiconductor_equipment | 311.855 |  | 312.1349 | -0.0897 | 306.51 | 298.89 | 0.4425 | below_vwap | below_vwap,spread_too_wide |
| 15 | SPY | market_regime | 743.92 |  | 744.8668 | -0.1271 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 16 | AMZN | cloud_ai_capex | 247.93 |  | 247.9916 | -0.0248 | 247.72 | 243.725 | 0.2138 | below_vwap | below_vwap |
| 17 | SNDK | memory_hbm_storage | 1421.72 |  | 1427.9207 | -0.4342 | 1393.96 | 1325.48 | 0.645 | below_vwap | below_vwap,spread_too_wide |
| 18 | ANET | ai_networking_optical | 168.6 |  | 166.2862 | 1.3914 | 163.275 | 157.34 | 4.7153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AVGO | custom_silicon_networking | 372.75 |  | 370.3633 | 0.6444 | 368.42 | 357.97 | 1.9531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 496.76 |  | 486.969 | 2.0106 | 482.43 | 461.04 | 3.6899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.3 |  | 695.6272 | 0.2405 | 693.36 | 686.78 | 0.0316 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.02 |  | 67.238 | 1.163 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.17 |  | 203.2417 | -0.0353 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.93 |  | 393.4759 | 0.3695 | 398.39 | 393.52 | 0.0532 | watch_only | none |
| AAPL | mega_cap_platform | 334.07 |  | 332.1986 | 0.5633 | 334.98 | 331.295 | 0.8322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 345.12 |  | 345.7917 | -0.1942 | 348.47 | 341.42 | 0.3622 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496.76 |  | 486.969 | 2.0106 | 482.43 | 461.04 | 3.6899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.16 |  | 398.0202 | -0.4674 | 394.11 | 386.02 | 0.4998 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.26 |  | 518.6152 | 0.8956 | 511.83 | 498.665 | 0.0784 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.15 |  | 555.2054 | 0.3502 | 550 | 536.9 | 0.0736 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.75 |  | 370.3633 | 0.6444 | 368.42 | 357.97 | 1.9531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 870.09 |  | 864.6376 | 0.6306 | 835.82 | 804.09 | 1.755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.225 |  | 187.2309 | 1.065 | 185.03 | 178.09 | 0.3699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.17 |  | 393.3459 | 1.9891 | 384 | 368.28 | 1.1217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.225 |  | 45.6944 | 1.1611 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.575 |  | 24.3184 | 1.0554 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.92 |  | 744.8668 | -0.1271 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.69 |  | 294.1466 | -0.1552 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.145 |  | 126.0387 | 0.0843 | 125.02 | 121.79 | 0.3171 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.67 |  | 72.2501 | 1.9652 | 71.24 | 68.65 | 2.4162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 291.08 |  | 287.4963 | 1.2465 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 399.365 |  | 399.7835 | -0.1047 | 389.4 | 382.38 | 0.1578 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 632.12 |  | 630.296 | 0.2894 | 616.75 | 609.05 | 0.242 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 1052.27 |  | 1045.4191 | 0.6553 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.95 |  | 469.7683 | -0.1742 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.705 |  | 140.9318 | -0.1609 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.6 |  | 166.2862 | 1.3914 | 163.275 | 157.34 | 4.7153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.58 |  | 274.1382 | 1.2555 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 735.5 |  | 718.6597 | 2.3433 | 694.98 | 653.305 | 4.412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.34 |  | 377.8214 | -0.1274 | 375.52 | 359.81 | 1.341 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.36 |  | 100.6074 | 1.742 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 302.22 |  | 304.9259 | -0.8874 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1759.69 |  | 1757.1486 | 0.1446 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 532.78 |  | 535.0461 | -0.4235 | 535.095 | 513.34 | 4.0786 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 311.855 |  | 312.1349 | -0.0897 | 306.51 | 298.89 | 0.4425 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 213.02 |  | 212.2374 | 0.3688 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TER | semiconductor_test_packaging | 323.515 |  | 320.2491 | 1.0198 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.805 |  | 277.7559 | 0.3777 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.595 |  | 61.5851 | 1.6399 | 60.51 | 57.99 | 0.3195 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 51.03 |  | 49.9361 | 2.1905 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.1 |  | 134.974 | 1.5752 | 129.93 | 126.945 | 4.8505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 324.445 |  | 318.9907 | 1.7099 | 315.89 | 307.13 | 4.2966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.1 |  | 518.7827 | -0.9026 | 526.74 | 522.205 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.97 |  | 298.861 | -0.9673 | 304.36 | 299.62 | 0.7602 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| APLD | high_beta_ai_infrastructure | 25.205 |  | 25.0944 | 0.4406 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.655 |  | 33.7835 | -0.3805 | 34 | 32.26 | 0.0594 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.6684 | 1.6528 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1421.72 |  | 1427.9207 | -0.4342 | 1393.96 | 1325.48 | 0.645 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.75 |  | 467.5247 | 2.8288 | 453.35 | 431.78 | 2.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 789.84 |  | 762.1415 | 3.6343 | 724.57 | 702.24 | 4.3072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.93 |  | 247.9916 | -0.0248 | 247.72 | 243.725 | 0.2138 | below_vwap | below_vwap |
| META | cloud_ai_capex | 644.44 |  | 642.5631 | 0.2921 | 649.07 | 638.97 | 0.2141 | watch_only | none |
| ARM | ai_accelerator | 266.915 |  | 261.2766 | 2.158 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.5 |  | 158.9781 | 0.3283 | 151.99 | 145.6 | 1.5298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
