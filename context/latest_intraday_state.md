# Intraday State

- Generated at: `2026-07-29T03:20:44+08:00`
- Market time ET: `2026-07-28T15:20:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 12, 'manual_confirm_candidate': 9, 'below_vwap': 6, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.26 |  | 674.2876 | 0.4408 | 677.3 | 670.84 | 0.0236 | watch_only | none |
| SOXX | semiconductor_index | 495.39 |  | 490.1187 | 1.0755 | 497.64 | 485.42 | 0.0444 | watch_only | none |
| SMH | semiconductor_index | 532.87 |  | 527.5695 | 1.0047 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| SPY | market_regime | 741.62 |  | 739.6941 | 0.2604 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.7 |  | 196.1651 | 0.7825 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.74 |  | 388.1227 | 1.4473 | 390.46 | 382.495 | 0.0813 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.62 |  | 739.6941 | 0.2604 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1594.13 |  | 1577.7593 | 1.0376 | 1586.01 | 1565.95 | 0.1518 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.2 |  | 331.2257 | 0.898 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.81 |  | 138.8793 | 1.3902 | 139.755 | 137.31 | 0.0994 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 121.085 |  | 118.8056 | 1.9186 | 117.17 | 115.25 | 0.0248 | buy_precheck_manual_confirm | none |
| 8 | TER | semiconductor_test_packaging | 319.68 |  | 309.3286 | 3.3464 | 315.21 | 304.11 | 0.3034 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1682 | 4.174 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.62 |  | 739.6941 | 0.2604 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.2 |  | 292.4481 | 0.2571 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 3 | NVDA | ai_accelerator | 197.7 |  | 196.1651 | 0.7825 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 231.05 |  | 230.5421 | 0.2203 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.3 |  | 338.9813 | 0.094 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 6 | QQQ | market_regime | 677.26 |  | 674.2876 | 0.4408 | 677.3 | 670.84 | 0.0236 | watch_only | none |
| 7 | VRT | data_center_power_cooling | 268.335 |  | 266.2084 | 0.7988 | 273.86 | 266.04 | 0.0522 | watch_only | none |
| 8 | JCI | data_center_power_cooling | 140.81 |  | 138.8793 | 1.3902 | 139.755 | 137.31 | 0.0994 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 393.74 |  | 388.1227 | 1.4473 | 390.46 | 382.495 | 0.0813 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1594.13 |  | 1577.7593 | 1.0376 | 1586.01 | 1565.95 | 0.1518 | buy_precheck_manual_confirm | none |
| 11 | GOOGL | cloud_ai_capex | 334.2 |  | 331.2257 | 0.898 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 12 | SMH | semiconductor_index | 532.87 |  | 527.5695 | 1.0047 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| 13 | SOXX | semiconductor_index | 495.39 |  | 490.1187 | 1.0755 | 497.64 | 485.42 | 0.0444 | watch_only | none |
| 14 | ENTG | semiconductor_materials | 119.53 |  | 119.1822 | 0.2918 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1682 | 4.174 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |
| 16 | GEV | data_center_power_cooling | 937.54 |  | 937.4839 | 0.006 | 955.825 | 935.665 | 0.7178 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SKHY | memory_hbm_storage | 131.9 |  | 131.529 | 0.2821 | 136.45 | 131.735 | 0.7051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ARM | ai_accelerator | 245.8 |  | 245.2361 | 0.2299 | 253.38 | 243.72 | 4.7559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | COHU | semiconductor_test_packaging | 42.715 |  | 42.4491 | 0.6265 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CRWV | gpu_cloud_ai_factory | 66.4 |  | 66.2721 | 0.193 | 68.995 | 65.635 | 2.1687 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.7 |  | 196.1651 | 0.7825 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.74 |  | 388.1227 | 1.4473 | 390.46 | 382.495 | 0.0813 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.62 |  | 739.6941 | 0.2604 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1594.13 |  | 1577.7593 | 1.0376 | 1586.01 | 1565.95 | 0.1518 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.2 |  | 331.2257 | 0.898 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.81 |  | 138.8793 | 1.3902 | 139.755 | 137.31 | 0.0994 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 121.085 |  | 118.8056 | 1.9186 | 117.17 | 115.25 | 0.0248 | buy_precheck_manual_confirm | none |
| 8 | TER | semiconductor_test_packaging | 319.68 |  | 309.3286 | 3.3464 | 315.21 | 304.11 | 0.3034 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1682 | 4.174 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 383.715 |  | 378.8289 | 1.2898 | 378.64 | 371.57 | 3.3071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ANET | ai_networking_optical | 168.88 |  | 165.1966 | 2.2297 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 387.66 |  | 381.5482 | 1.6018 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SMH | semiconductor_index | 532.87 |  | 527.5695 | 1.0047 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| 14 | SOXX | semiconductor_index | 495.39 |  | 490.1187 | 1.0755 | 497.64 | 485.42 | 0.0444 | watch_only | none |
| 15 | QQQ | market_regime | 677.26 |  | 674.2876 | 0.4408 | 677.3 | 670.84 | 0.0236 | watch_only | none |
| 16 | VRT | data_center_power_cooling | 268.335 |  | 266.2084 | 0.7988 | 273.86 | 266.04 | 0.0522 | watch_only | none |
| 17 | IWM | market_regime | 293.2 |  | 292.4481 | 0.2571 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 18 | KLAC | semiconductor_equipment | 194.12 |  | 190.9261 | 1.6728 | 194.96 | 189.48 | 0.0515 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 231.05 |  | 230.5421 | 0.2203 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 20 | HPE | ai_server_oem | 45.2 |  | 44.5248 | 1.5165 | 46.19 | 44.33 | 0.0442 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.26 |  | 674.2876 | 0.4408 | 677.3 | 670.84 | 0.0236 | watch_only | none |
| TQQQ | leveraged_tool | 61.94 |  | 61.1504 | 1.2913 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.7 |  | 196.1651 | 0.7825 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.08 |  | 396.3411 | -0.5705 | 400.09 | 392.355 | 0.0355 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.3 |  | 338.9813 | 0.094 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.2 |  | 331.2257 | 0.898 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 460.71 |  | 455.6973 | 1.1 | 472.485 | 453.76 | 0.6338 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.74 |  | 388.1227 | 1.4473 | 390.46 | 382.495 | 0.0813 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.39 |  | 490.1187 | 1.0755 | 497.64 | 485.42 | 0.0444 | watch_only | none |
| SMH | semiconductor_index | 532.87 |  | 527.5695 | 1.0047 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| AVGO | custom_silicon_networking | 383.715 |  | 378.8289 | 1.2898 | 378.64 | 371.57 | 3.3071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 826.7 |  | 816.0051 | 1.3106 | 846.4 | 813.91 | 0.9858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.945 |  | 174.254 | 0.9704 | 181.24 | 172.395 | 1.7846 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 390.48 |  | 375.7703 | 3.9145 | 402 | 374.02 | 2.1486 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.2 |  | 44.5248 | 1.5165 | 46.19 | 44.33 | 0.0442 | watch_only | none |
| SMCI | ai_server_oem | 28.445 |  | 28.0191 | 1.5201 | 28.86 | 27.59 | 0.0703 | watch_only | none |
| SPY | market_regime | 741.62 |  | 739.6941 | 0.2604 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.2 |  | 292.4481 | 0.2571 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 121.085 |  | 118.8056 | 1.9186 | 117.17 | 115.25 | 0.0248 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.4 |  | 66.2721 | 0.193 | 68.995 | 65.635 | 2.1687 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.335 |  | 266.2084 | 0.7988 | 273.86 | 266.04 | 0.0522 | watch_only | none |
| ETN | data_center_power_cooling | 387.66 |  | 381.5482 | 1.6018 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 589.12 |  | 582.8385 | 1.0777 | 603.25 | 584.69 | 4.9277 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 937.54 |  | 937.4839 | 0.006 | 955.825 | 935.665 | 0.7178 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.27 |  | 465.6596 | 0.5606 | 477.73 | 460.77 | 5.0227 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.81 |  | 138.8793 | 1.3902 | 139.755 | 137.31 | 0.0994 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 168.88 |  | 165.1966 | 2.2297 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 242.94 |  | 237.8647 | 2.1337 | 256.145 | 236.73 | 0.0659 | watch_only | none |
| LITE | ai_networking_optical | 649.06 |  | 632.7715 | 2.5742 | 673.65 | 624.91 | 3.864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 344.76 |  | 337.6489 | 2.1061 | 354.09 | 338.14 | 0.8789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.07 |  | 85.9164 | 2.5067 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.605 |  | 259.3031 | 0.8877 | 268.265 | 253.05 | 4.7514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1594.13 |  | 1577.7593 | 1.0376 | 1586.01 | 1565.95 | 0.1518 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 481.52 |  | 476.5733 | 1.038 | 494.87 | 477.03 | 0.9179 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 273.15 |  | 267.044 | 2.2865 | 276.85 | 267.14 | 4.331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 194.12 |  | 190.9261 | 1.6728 | 194.96 | 189.48 | 0.0515 | watch_only | none |
| TER | semiconductor_test_packaging | 319.68 |  | 309.3286 | 3.3464 | 315.21 | 304.11 | 0.3034 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 241.49 |  | 237.1173 | 1.8441 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.28 |  | 46.6659 | -0.827 | 51.64 | 47.435 | 3.6949 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.715 |  | 42.4491 | 0.6265 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.53 |  | 119.1822 | 0.2918 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 286.23 |  | 282.4794 | 1.3277 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 515.42 |  | 517.9907 | -0.4963 | 518.6 | 511.495 | 0.0912 | below_vwap | below_vwap |
| APD | industrial_gases | 295.38 |  | 295.7278 | -0.1176 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.46 |  | 26.5096 | -0.1869 | 27 | 25.42 | 0.1134 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.61 |  | 33.7028 | -0.2754 | 35.08 | 33.52 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1682 | 4.174 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1117.89 |  | 1099.8355 | 1.6416 | 1185.19 | 1114.57 | 0.7335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 458.98 |  | 441.1548 | 4.0406 | 465.04 | 435.22 | 5.0351 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 747.38 |  | 733.3626 | 1.9114 | 774.805 | 719.02 | 0.5299 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.05 |  | 230.5421 | 0.2203 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 593.965 |  | 593.8495 | 0.0194 | 600.765 | 594.21 | 0.4882 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 245.8 |  | 245.2361 | 0.2299 | 253.38 | 243.72 | 4.7559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 131.9 |  | 131.529 | 0.2821 | 136.45 | 131.735 | 0.7051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
