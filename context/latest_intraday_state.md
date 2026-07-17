# Intraday State

- Generated at: `2026-07-17T22:13:46+08:00`
- Market time ET: `2026-07-17T10:13:47-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 4, 'spread_too_wide_or_missing': 36, 'price_stale_or_missing': 1, 'below_vwap': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.63 |  | 691.665 | 0.7178 | 693.36 | 686.78 | 0.0947 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 520.57 |  | 510.1476 | 2.043 | 511.83 | 498.665 | 0.1652 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.56 |  | 546.9722 | 1.7529 | 550 | 536.9 | 0.0952 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.25 |  | 743.2186 | 0.4079 | 742.66 | 740.8 | 0.0362 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.38 |  | 200.9082 | 1.7281 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.56 |  | 546.9722 | 1.7529 | 550 | 536.9 | 0.0952 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 520.57 |  | 510.1476 | 2.043 | 511.83 | 498.665 | 0.1652 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1747.575 |  | 1729.0545 | 1.0711 | 1741.99 | 1704.935 | 0.2878 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.8 |  | 293.7376 | 0.7021 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.63 |  | 691.665 | 0.7178 | 693.36 | 686.78 | 0.0947 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.8 |  | 44.6442 | 2.589 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.25 |  | 743.2186 | 0.4079 | 742.66 | 740.8 | 0.0362 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.32 |  | 23.7982 | 2.1924 | 24.3 | 23.46 | 0.1645 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.61 |  | 20.2088 | 1.9853 | 20.445 | 19.92 | 0.1456 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 34.1 |  | 33.1994 | 2.7127 | 34 | 32.26 | 0.176 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.87 |  | 66.0571 | 2.7444 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 295.8 |  | 293.7376 | 0.7021 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 696.63 |  | 691.665 | 0.7178 | 693.36 | 686.78 | 0.0947 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 746.25 |  | 743.2186 | 0.4079 | 742.66 | 740.8 | 0.0362 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1747.575 |  | 1729.0545 | 1.0711 | 1741.99 | 1704.935 | 0.2878 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 204.38 |  | 200.9082 | 1.7281 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 556.56 |  | 546.9722 | 1.7529 | 550 | 536.9 | 0.0952 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.32 |  | 23.7982 | 2.1924 | 24.3 | 23.46 | 0.1645 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 247.55 |  | 246.7513 | 0.3237 | 247.72 | 243.725 | 0.9493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | IREN | high_beta_ai_infrastructure | 34.1 |  | 33.1994 | 2.7127 | 34 | 32.26 | 0.176 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.61 |  | 20.2088 | 1.9853 | 20.445 | 19.92 | 0.1456 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 45.8 |  | 44.6442 | 2.589 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| 12 | SOXX | semiconductor_index | 520.57 |  | 510.1476 | 2.043 | 511.83 | 498.665 | 0.1652 | buy_precheck_manual_confirm | none |
| 13 | GOOGL | cloud_ai_capex | 347.32 |  | 345.2593 | 0.5969 | 348.47 | 341.42 | 0.6939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | APLD | high_beta_ai_infrastructure | 25.13 |  | 24.6885 | 1.7885 | 25.45 | 24.1 | 0.0398 | watch_only | none |
| 15 | TT | data_center_power_cooling | 472.25 |  | 467.5212 | 1.0115 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 141.33 |  | 139.288 | 1.466 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 371.24 |  | 365.7965 | 1.4881 | 368.42 | 357.97 | 2.559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ORCL | cloud_ai_capex | 125.095 |  | 124.0712 | 0.8251 | 125.02 | 121.79 | 3.5573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 399.3 |  | 393.6393 | 1.438 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.38 |  | 200.9082 | 1.7281 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.56 |  | 546.9722 | 1.7529 | 550 | 536.9 | 0.0952 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 520.57 |  | 510.1476 | 2.043 | 511.83 | 498.665 | 0.1652 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1747.575 |  | 1729.0545 | 1.0711 | 1741.99 | 1704.935 | 0.2878 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.8 |  | 293.7376 | 0.7021 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.63 |  | 691.665 | 0.7178 | 693.36 | 686.78 | 0.0947 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.8 |  | 44.6442 | 2.589 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.25 |  | 743.2186 | 0.4079 | 742.66 | 740.8 | 0.0362 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.32 |  | 23.7982 | 2.1924 | 24.3 | 23.46 | 0.1645 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.61 |  | 20.2088 | 1.9853 | 20.445 | 19.92 | 0.1456 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 34.1 |  | 33.1994 | 2.7127 | 34 | 32.26 | 0.176 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.87 |  | 66.0571 | 2.7444 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 13 | ANET | ai_networking_optical | 166.12 |  | 161.3929 | 2.9289 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TSM | foundry | 400.8 |  | 392.2241 | 2.1865 | 394.11 | 386.02 | 2.5175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AVGO | custom_silicon_networking | 371.24 |  | 365.7965 | 1.4881 | 368.42 | 357.97 | 2.559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMAT | semiconductor_equipment | 535.23 |  | 525.4621 | 1.8589 | 535.095 | 513.34 | 1.0295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 488.06 |  | 472.7873 | 3.2304 | 482.43 | 461.04 | 2.5612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 472.25 |  | 467.5212 | 1.0115 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | KLAC | semiconductor_equipment | 212.61 |  | 209.635 | 1.4191 | 210.82 | 204.71 | 0.8984 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MU | memory_hbm_storage | 864.5 |  | 835.5984 | 3.4588 | 835.82 | 804.09 | 1.7941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.63 |  | 691.665 | 0.7178 | 693.36 | 686.78 | 0.0947 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.87 |  | 66.0571 | 2.7444 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.38 |  | 200.9082 | 1.7281 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.23 |  | 394.7851 | -0.6472 | 398.39 | 393.52 | 0.1453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.09 |  | 332.2281 | -0.6436 | 334.98 | 331.295 | 0.2151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.32 |  | 345.2593 | 0.5969 | 348.47 | 341.42 | 0.6939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 488.06 |  | 472.7873 | 3.2304 | 482.43 | 461.04 | 2.5612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.8 |  | 392.2241 | 2.1865 | 394.11 | 386.02 | 2.5175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 520.57 |  | 510.1476 | 2.043 | 511.83 | 498.665 | 0.1652 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.56 |  | 546.9722 | 1.7529 | 550 | 536.9 | 0.0952 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.24 |  | 365.7965 | 1.4881 | 368.42 | 357.97 | 2.559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 864.5 |  | 835.5984 | 3.4588 | 835.82 | 804.09 | 1.7941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 187.79 |  | 182.8881 | 2.6803 | 185.03 | 178.09 | 0.8254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 392.37 |  | 378.7426 | 3.5981 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.8 |  | 44.6442 | 2.589 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.32 |  | 23.7982 | 2.1924 | 24.3 | 23.46 | 0.1645 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.25 |  | 743.2186 | 0.4079 | 742.66 | 740.8 | 0.0362 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.8 |  | 293.7376 | 0.7021 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.095 |  | 124.0712 | 0.8251 | 125.02 | 121.79 | 3.5573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 71.95 |  | 69.9762 | 2.8207 | 71.24 | 68.65 | 2.9882 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 287.49 |  | 280.0916 | 2.6414 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 399.3 |  | 393.6393 | 1.438 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 629.83 |  | 617.9465 | 1.9231 | 616.75 | 609.05 | 0.6637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1049.95 |  | 1018.3184 | 3.1063 | 1001.82 | 982.21 | 5.1069 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 472.25 |  | 467.5212 | 1.0115 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.33 |  | 139.288 | 1.466 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.12 |  | 161.3929 | 2.9289 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 274.895 |  | 266.6917 | 3.0759 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 716.39 |  | 682.5037 | 4.965 | 694.98 | 653.305 | 4.0439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 382.415 |  | 370.9345 | 3.095 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 100.57 |  | 95.7158 | 5.0714 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.63 |  | 299.0057 | 1.881 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1747.575 |  | 1729.0545 | 1.0711 | 1741.99 | 1704.935 | 0.2878 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 535.23 |  | 525.4621 | 1.8589 | 535.095 | 513.34 | 1.0295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 312.44 |  | 304.6031 | 2.5728 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 212.61 |  | 209.635 | 1.4191 | 210.82 | 204.71 | 0.8984 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 316.51 |  | 304.7853 | 3.8469 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 271.75 |  | 264.941 | 2.57 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.355 |  | 59.4355 | 3.2296 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.1 |  | 48.2171 | 3.9051 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.885 |  | 130.9449 | 3.7726 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 319.56 |  | 312.9386 | 2.1159 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 522.18 |  | 522.3586 | -0.0342 | 526.74 | 522.205 | 5.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 301.72 |  | 302.0205 | -0.0995 | 304.36 | 299.62 | 4.7229 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.13 |  | 24.6885 | 1.7885 | 25.45 | 24.1 | 0.0398 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.1 |  | 33.1994 | 2.7127 | 34 | 32.26 | 0.176 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.61 |  | 20.2088 | 1.9853 | 20.445 | 19.92 | 0.1456 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1437.36 |  | 1383.3605 | 3.9035 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 462.78 |  | 446.502 | 3.6457 | 453.35 | 431.78 | 1.4694 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 743.28 |  | 722.6504 | 2.8547 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.55 |  | 246.7513 | 0.3237 | 247.72 | 243.725 | 0.9493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| META | cloud_ai_capex | 636.62 |  | 641.3464 | -0.737 | 649.07 | 638.97 | 1.8598 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 260.7 |  | 251.1557 | 3.8001 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 158.865 |  | 153.1098 | 3.7588 | 151.99 | 145.6 | 1.8758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
