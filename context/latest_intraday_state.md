# Intraday State

- Generated at: `2026-07-17T23:50:39+08:00`
- Market time ET: `2026-07-17T11:50:40-04:00`
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
| QQQ | market_regime | 696.46 |  | 693.4085 | 0.4401 | 693.36 | 686.78 | 0.0431 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 521.19 |  | 513.1028 | 1.5761 | 511.83 | 498.665 | 0.117 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.82 |  | 550.0635 | 1.4101 | 550 | 536.9 | 0.0932 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.56 |  | 744.482 | 0.1448 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.86 |  | 202.3328 | 1.2491 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 557.82 |  | 550.0635 | 1.4101 | 550 | 536.9 | 0.0932 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 492.72 |  | 480.8172 | 2.4755 | 482.43 | 461.04 | 0.3024 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 521.19 |  | 513.1028 | 1.5761 | 511.83 | 498.665 | 0.117 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 213.01 |  | 210.3082 | 1.2847 | 210.82 | 204.71 | 0.1972 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.46 |  | 693.4085 | 0.4401 | 693.36 | 686.78 | 0.0431 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.64 |  | 45.3052 | 0.7391 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.56 |  | 744.482 | 0.1448 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.5 |  | 247.8592 | 0.2585 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.64 |  | 20.4104 | 1.1249 | 20.445 | 19.92 | 0.0484 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.91 |  | 66.7283 | 1.7708 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 248.5 |  | 247.8592 | 0.2585 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 745.56 |  | 744.482 | 0.1448 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.46 |  | 693.4085 | 0.4401 | 693.36 | 686.78 | 0.0431 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 333.57 |  | 332.5329 | 0.3119 | 334.98 | 331.295 | 0.1169 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 24.88 |  | 24.8117 | 0.2752 | 25.45 | 24.1 | 0.0402 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.465 |  | 33.4257 | 0.1175 | 34 | 32.26 | 0.0598 | watch_only | none |
| 7 | HPE | ai_server_oem | 45.64 |  | 45.3052 | 0.7391 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 347.8 |  | 345.7841 | 0.583 | 348.47 | 341.42 | 0.0949 | watch_only | none |
| 9 | NVDA | ai_accelerator | 204.86 |  | 202.3328 | 1.2491 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 557.82 |  | 550.0635 | 1.4101 | 550 | 536.9 | 0.0932 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 213.01 |  | 210.3082 | 1.2847 | 210.82 | 204.71 | 0.1972 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.64 |  | 20.4104 | 1.1249 | 20.445 | 19.92 | 0.0484 | buy_precheck_manual_confirm | none |
| 13 | SMCI | ai_server_oem | 24.22 |  | 24.0202 | 0.8316 | 24.3 | 23.46 | 0.0413 | watch_only | none |
| 14 | JCI | data_center_power_cooling | 141.65 |  | 140.5417 | 0.7886 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ALAB | ai_networking_optical | 300.36 |  | 300.1624 | 0.0658 | 305.21 | 289.97 | 0.3829 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SOXX | semiconductor_index | 521.19 |  | 513.1028 | 1.5761 | 511.83 | 498.665 | 0.117 | buy_precheck_manual_confirm | none |
| 17 | AVGO | custom_silicon_networking | 370.675 |  | 368.0636 | 0.7095 | 368.42 | 357.97 | 4.3839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 471.6 |  | 469.1037 | 0.5321 | 469.08 | 460.78 | 3.9737 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 492.72 |  | 480.8172 | 2.4755 | 482.43 | 461.04 | 0.3024 | buy_precheck_manual_confirm | none |
| 20 | ORCL | cloud_ai_capex | 125.91 |  | 125.0033 | 0.7254 | 125.02 | 121.79 | 3.2881 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.86 |  | 202.3328 | 1.2491 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 557.82 |  | 550.0635 | 1.4101 | 550 | 536.9 | 0.0932 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 492.72 |  | 480.8172 | 2.4755 | 482.43 | 461.04 | 0.3024 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 521.19 |  | 513.1028 | 1.5761 | 511.83 | 498.665 | 0.117 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 213.01 |  | 210.3082 | 1.2847 | 210.82 | 204.71 | 0.1972 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.46 |  | 693.4085 | 0.4401 | 693.36 | 686.78 | 0.0431 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.64 |  | 45.3052 | 0.7391 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.56 |  | 744.482 | 0.1448 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.5 |  | 247.8592 | 0.2585 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.64 |  | 20.4104 | 1.1249 | 20.445 | 19.92 | 0.0484 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.91 |  | 66.7283 | 1.7708 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 12 | ANET | ai_networking_optical | 166.02 |  | 163.1292 | 1.7721 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 399.71 |  | 395.3798 | 1.0952 | 394.11 | 386.02 | 0.6705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AVGO | custom_silicon_networking | 370.675 |  | 368.0636 | 0.7095 | 368.42 | 357.97 | 4.3839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMAT | semiconductor_equipment | 538.93 |  | 529.1158 | 1.8548 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ASML | semiconductor_equipment | 1762.78 |  | 1740.3891 | 1.2865 | 1741.99 | 1704.935 | 2.3344 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 471.6 |  | 469.1037 | 0.5321 | 469.08 | 460.78 | 3.9737 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MU | memory_hbm_storage | 865.16 |  | 849.9641 | 1.7878 | 835.82 | 804.09 | 0.5224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 290.12 |  | 282.9542 | 2.5325 | 280.565 | 273.17 | 4.2534 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | JCI | data_center_power_cooling | 141.65 |  | 140.5417 | 0.7886 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.46 |  | 693.4085 | 0.4401 | 693.36 | 686.78 | 0.0431 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.91 |  | 66.7283 | 1.7708 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.86 |  | 202.3328 | 1.2491 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.385 |  | 393.0636 | -0.1726 | 398.39 | 393.52 | 0.1911 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.57 |  | 332.5329 | 0.3119 | 334.98 | 331.295 | 0.1169 | watch_only | none |
| GOOGL | cloud_ai_capex | 347.8 |  | 345.7841 | 0.583 | 348.47 | 341.42 | 0.0949 | watch_only | none |
| AMD | ai_accelerator | 492.72 |  | 480.8172 | 2.4755 | 482.43 | 461.04 | 0.3024 | buy_precheck_manual_confirm | none |
| TSM | foundry | 399.71 |  | 395.3798 | 1.0952 | 394.11 | 386.02 | 0.6705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 521.19 |  | 513.1028 | 1.5761 | 511.83 | 498.665 | 0.117 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.82 |  | 550.0635 | 1.4101 | 550 | 536.9 | 0.0932 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 370.675 |  | 368.0636 | 0.7095 | 368.42 | 357.97 | 4.3839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 865.16 |  | 849.9641 | 1.7878 | 835.82 | 804.09 | 0.5224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 186.475 |  | 184.5456 | 1.0455 | 185.03 | 178.09 | 4.5207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 392.55 |  | 387.1491 | 1.3951 | 384 | 368.28 | 2.0762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.64 |  | 45.3052 | 0.7391 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.22 |  | 24.0202 | 0.8316 | 24.3 | 23.46 | 0.0413 | watch_only | none |
| SPY | market_regime | 745.56 |  | 744.482 | 0.1448 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.67 |  | 294.0062 | -0.1143 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.91 |  | 125.0033 | 0.7254 | 125.02 | 121.79 | 3.2881 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.425 |  | 71.4603 | 2.7493 | 71.24 | 68.65 | 0.4086 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.12 |  | 282.9542 | 2.5325 | 280.565 | 273.17 | 4.2534 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 401.115 |  | 396.4564 | 1.1751 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 631.32 |  | 624.6608 | 1.066 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1047 |  | 1031.8818 | 1.4651 | 1001.82 | 982.21 | 4.5845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 471.6 |  | 469.1037 | 0.5321 | 469.08 | 460.78 | 3.9737 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.65 |  | 140.5417 | 0.7886 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.02 |  | 163.1292 | 1.7721 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.34 |  | 269.4114 | 2.5718 | 269.59 | 256.24 | 4.4945 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 725.75 |  | 700.8309 | 3.5556 | 694.98 | 653.305 | 3.9256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 378.52 |  | 373.4938 | 1.3457 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 100.895 |  | 98.3246 | 2.6142 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 300.36 |  | 300.1624 | 0.0658 | 305.21 | 289.97 | 0.3829 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1762.78 |  | 1740.3891 | 1.2865 | 1741.99 | 1704.935 | 2.3344 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 538.93 |  | 529.1158 | 1.8548 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 315.14 |  | 308.4091 | 2.1825 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.01 |  | 210.3082 | 1.2847 | 210.82 | 204.71 | 0.1972 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 315.94 |  | 309.946 | 1.9339 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 272 |  | 267.2427 | 1.7801 | 265.71 | 258.355 | 4.0478 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 61.79 |  | 60.4829 | 2.1612 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.14 |  | 48.8078 | 2.7295 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.78 |  | 133.009 | 2.0833 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 319.895 |  | 315.0743 | 1.53 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 520.15 |  | 521.7485 | -0.3064 | 526.74 | 522.205 | 4.8774 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 300.015 |  | 301.3004 | -0.4266 | 304.36 | 299.62 | 2.7132 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.88 |  | 24.8117 | 0.2752 | 25.45 | 24.1 | 0.0402 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.465 |  | 33.4257 | 0.1175 | 34 | 32.26 | 0.0598 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.64 |  | 20.4104 | 1.1249 | 20.445 | 19.92 | 0.0484 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1453.79 |  | 1404.9813 | 3.474 | 1393.96 | 1325.48 | 4.7386 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 466.52 |  | 452.4805 | 3.1028 | 453.35 | 431.78 | 3.5111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 760.69 |  | 736.3801 | 3.3013 | 724.57 | 702.24 | 1.4132 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.5 |  | 247.8592 | 0.2585 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 629.905 |  | 635.4661 | -0.8751 | 649.07 | 638.97 | 0.2302 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 261.13 |  | 255.3499 | 2.2636 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 162.71 |  | 155.8469 | 4.4038 | 151.99 | 145.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
