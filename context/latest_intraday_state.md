# Intraday State

- Generated at: `2026-07-29T03:32:14+08:00`
- Market time ET: `2026-07-28T15:32:15-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_vwap': 4, 'watch_only': 10, 'spread_too_wide_or_missing': 29, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.72 |  | 674.3621 | 0.4979 | 677.3 | 670.84 | 0.0339 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 497.58 |  | 490.3025 | 1.4843 | 497.64 | 485.42 | 0.0985 | watch_only | none |
| SMH | semiconductor_index | 534.75 |  | 527.7231 | 1.3316 | 533.01 | 523.325 | 0.0411 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 741.575 |  | 739.7617 | 0.2451 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.88 |  | 196.2078 | 0.8523 | 195.4 | 193.65 | 0.0202 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 534.75 |  | 527.7231 | 1.3316 | 533.01 | 523.325 | 0.0411 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 385.06 |  | 379.0284 | 1.5913 | 378.64 | 371.57 | 0.1013 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.575 |  | 739.7617 | 0.2451 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 677.72 |  | 674.3621 | 0.4979 | 677.3 | 670.84 | 0.0339 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1595.47 |  | 1578.3555 | 1.0843 | 1586.01 | 1565.95 | 0.168 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 334.62 |  | 331.3801 | 0.9777 | 330.21 | 324.97 | 0.251 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 293.375 |  | 292.4771 | 0.307 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 195.48 |  | 191.1172 | 2.2828 | 194.96 | 189.48 | 0.1074 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 62.14 |  | 61.1652 | 1.5938 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.575 |  | 739.7617 | 0.2451 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.375 |  | 292.4771 | 0.307 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 677.72 |  | 674.3621 | 0.4979 | 677.3 | 670.84 | 0.0339 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 230.855 |  | 230.5503 | 0.1322 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.16 |  | 338.988 | 0.0507 | 342.87 | 337.78 | 0.1887 | watch_only | none |
| 6 | SMH | semiconductor_index | 534.75 |  | 527.7231 | 1.3316 | 533.01 | 523.325 | 0.0411 | buy_precheck_manual_confirm | none |
| 7 | NVDA | ai_accelerator | 197.88 |  | 196.2078 | 0.8523 | 195.4 | 193.65 | 0.0202 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1595.47 |  | 1578.3555 | 1.0843 | 1586.01 | 1565.95 | 0.168 | buy_precheck_manual_confirm | none |
| 9 | MU | memory_hbm_storage | 828.02 |  | 816.2521 | 1.4417 | 846.4 | 813.91 | 0.0821 | watch_only | none |
| 10 | SOXX | semiconductor_index | 497.58 |  | 490.3025 | 1.4843 | 497.64 | 485.42 | 0.0985 | watch_only | none |
| 11 | GOOGL | cloud_ai_capex | 334.62 |  | 331.3801 | 0.9777 | 330.21 | 324.97 | 0.251 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 195.48 |  | 191.1172 | 2.2828 | 194.96 | 189.48 | 0.1074 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.165 |  | 33.7128 | 1.3413 | 35.08 | 33.52 | 0.0585 | watch_only | none |
| 14 | APLD | high_beta_ai_infrastructure | 26.915 |  | 26.5287 | 1.4563 | 27 | 25.42 | 0.1486 | watch_only | none |
| 15 | GEV | data_center_power_cooling | 940.47 |  | 937.5593 | 0.3105 | 955.825 | 935.665 | 0.3955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ENTG | semiconductor_materials | 120 |  | 119.2184 | 0.6556 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 385.06 |  | 379.0284 | 1.5913 | 378.64 | 371.57 | 0.1013 | buy_precheck_manual_confirm | none |
| 18 | CIEN | ai_networking_optical | 349.48 |  | 337.8684 | 3.4367 | 354.09 | 338.14 | 0.1087 | watch_only | none |
| 19 | TT | data_center_power_cooling | 468.65 |  | 465.881 | 0.5944 | 477.73 | 460.77 | 5.0187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SMCI | ai_server_oem | 28.625 |  | 28.035 | 2.1046 | 28.86 | 27.59 | 0.0699 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.88 |  | 196.2078 | 0.8523 | 195.4 | 193.65 | 0.0202 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 534.75 |  | 527.7231 | 1.3316 | 533.01 | 523.325 | 0.0411 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 385.06 |  | 379.0284 | 1.5913 | 378.64 | 371.57 | 0.1013 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.575 |  | 739.7617 | 0.2451 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 677.72 |  | 674.3621 | 0.4979 | 677.3 | 670.84 | 0.0339 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1595.47 |  | 1578.3555 | 1.0843 | 1586.01 | 1565.95 | 0.168 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 334.62 |  | 331.3801 | 0.9777 | 330.21 | 324.97 | 0.251 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 293.375 |  | 292.4771 | 0.307 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 195.48 |  | 191.1172 | 2.2828 | 194.96 | 189.48 | 0.1074 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 62.14 |  | 61.1652 | 1.5938 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 394.64 |  | 388.4703 | 1.5882 | 390.46 | 382.495 | 1.5964 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ANET | ai_networking_optical | 169.31 |  | 165.2363 | 2.4654 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 141.125 |  | 138.9759 | 1.5464 | 139.755 | 137.31 | 3.3091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ETN | data_center_power_cooling | 387.43 |  | 381.6121 | 1.5246 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ORCL | cloud_ai_capex | 121.12 |  | 118.873 | 1.8903 | 117.17 | 115.25 | 1.5357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TER | semiconductor_test_packaging | 322.185 |  | 310.0144 | 3.9258 | 315.21 | 304.11 | 0.4159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MU | memory_hbm_storage | 828.02 |  | 816.2521 | 1.4417 | 846.4 | 813.91 | 0.0821 | watch_only | none |
| 18 | SOXX | semiconductor_index | 497.58 |  | 490.3025 | 1.4843 | 497.64 | 485.42 | 0.0985 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 230.855 |  | 230.5503 | 0.1322 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 20 | HPE | ai_server_oem | 45.315 |  | 44.5976 | 1.6087 | 46.19 | 44.33 | 0.3089 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.72 |  | 674.3621 | 0.4979 | 677.3 | 670.84 | 0.0339 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.14 |  | 61.1652 | 1.5938 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.88 |  | 196.2078 | 0.8523 | 195.4 | 193.65 | 0.0202 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.93 |  | 396.2531 | -0.8386 | 400.09 | 392.355 | 0.0153 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.16 |  | 338.988 | 0.0507 | 342.87 | 337.78 | 0.1887 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.62 |  | 331.3801 | 0.9777 | 330.21 | 324.97 | 0.251 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 464.87 |  | 455.9367 | 1.9593 | 472.485 | 453.76 | 4.3388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.64 |  | 388.4703 | 1.5882 | 390.46 | 382.495 | 1.5964 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 497.58 |  | 490.3025 | 1.4843 | 497.64 | 485.42 | 0.0985 | watch_only | none |
| SMH | semiconductor_index | 534.75 |  | 527.7231 | 1.3316 | 533.01 | 523.325 | 0.0411 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.06 |  | 379.0284 | 1.5913 | 378.64 | 371.57 | 0.1013 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 828.02 |  | 816.2521 | 1.4417 | 846.4 | 813.91 | 0.0821 | watch_only | none |
| MRVL | custom_silicon_networking | 177.1 |  | 174.3206 | 1.5944 | 181.24 | 172.395 | 0.4856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 393.29 |  | 376.2674 | 4.5241 | 402 | 374.02 | 1.9604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.315 |  | 44.5976 | 1.6087 | 46.19 | 44.33 | 0.3089 | watch_only | none |
| SMCI | ai_server_oem | 28.625 |  | 28.035 | 2.1046 | 28.86 | 27.59 | 0.0699 | watch_only | none |
| SPY | market_regime | 741.575 |  | 739.7617 | 0.2451 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.375 |  | 292.4771 | 0.307 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 121.12 |  | 118.873 | 1.8903 | 117.17 | 115.25 | 1.5357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67.125 |  | 66.2946 | 1.2526 | 68.995 | 65.635 | 2.8603 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.43 |  | 266.3147 | 1.1698 | 273.86 | 266.04 | 4.6914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 387.43 |  | 381.6121 | 1.5246 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 591.42 |  | 583.1332 | 1.4211 | 603.25 | 584.69 | 2.7798 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 940.47 |  | 937.5593 | 0.3105 | 955.825 | 935.665 | 0.3955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.65 |  | 465.881 | 0.5944 | 477.73 | 460.77 | 5.0187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.125 |  | 138.9759 | 1.5464 | 139.755 | 137.31 | 3.3091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 169.31 |  | 165.2363 | 2.4654 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 245.26 |  | 238.2235 | 2.9537 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 655.88 |  | 633.414 | 3.5468 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 349.48 |  | 337.8684 | 3.4367 | 354.09 | 338.14 | 0.1087 | watch_only | none |
| AAOI | ai_networking_optical | 88.96 |  | 86.0027 | 3.4386 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 266.27 |  | 259.597 | 2.5705 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1595.47 |  | 1578.3555 | 1.0843 | 1586.01 | 1565.95 | 0.168 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 482.475 |  | 476.8306 | 1.1837 | 494.87 | 477.03 | 5.1153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 273.99 |  | 267.1949 | 2.5431 | 276.85 | 267.14 | 4.4637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 195.48 |  | 191.1172 | 2.2828 | 194.96 | 189.48 | 0.1074 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 322.185 |  | 310.0144 | 3.9258 | 315.21 | 304.11 | 0.4159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 242.44 |  | 237.2372 | 2.1931 | 248.8 | 236.42 | 0.528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.635 |  | 46.66 | -0.0537 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.96 |  | 42.4703 | 1.153 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 120 |  | 119.2184 | 0.6556 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 288.31 |  | 282.5805 | 2.0276 | 296.8 | 283.22 | 0.5237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.15 |  | 517.8824 | -0.7207 | 518.6 | 511.495 | 0.1634 | below_vwap | below_vwap |
| APD | industrial_gases | 295.105 |  | 295.7097 | -0.2045 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.915 |  | 26.5287 | 1.4563 | 27 | 25.42 | 0.1486 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.165 |  | 33.7128 | 1.3413 | 35.08 | 33.52 | 0.0585 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.895 |  | 20.1867 | 3.5089 | 20.97 | 19.755 | 0.0957 | watch_only | none |
| SNDK | memory_hbm_storage | 1122.52 |  | 1100.6857 | 1.9837 | 1185.19 | 1114.57 | 3.118 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 462.205 |  | 441.8609 | 4.6042 | 465.04 | 435.22 | 0.7551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 750.26 |  | 733.8764 | 2.2325 | 774.805 | 719.02 | 0.985 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.855 |  | 230.5503 | 0.1322 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.115 |  | 593.8415 | -0.1223 | 600.765 | 594.21 | 0.2259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 247.88 |  | 245.3064 | 1.0491 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.91 |  | 131.5498 | 1.034 | 136.45 | 131.735 | 0.7449 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
