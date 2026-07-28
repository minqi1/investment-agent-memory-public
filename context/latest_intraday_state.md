# Intraday State

- Generated at: `2026-07-28T21:55:20+08:00`
- Market time ET: `2026-07-28T09:55:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 27, 'below_vwap': 22, 'watch_only': 2, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.19 |  | 672.4759 | -0.3399 | 677.3 | 670.84 | 0.0925 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 486.81 |  | 489.6356 | -0.5771 | 497.64 | 485.42 | 0.0965 | below_vwap | below_vwap |
| SMH | semiconductor_index | 524.03 |  | 526.4972 | -0.4686 | 533.01 | 523.325 | 0.0725 | below_vwap | below_vwap |
| SPY | market_regime | 737.01 |  | 737.759 | -0.1015 | 739.42 | 736.57 | 0.0366 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 327.13 |  | 327.1228 | 0.0022 | 330.21 | 324.97 | 0.0397 | watch_only | none |
| 2 | JCI | data_center_power_cooling | 138.6 |  | 138.0606 | 0.3907 | 139.755 | 137.31 | 0.1299 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 375.7 |  | 374.6282 | 0.2861 | 378.64 | 371.57 | 1.1073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 520.12 |  | 517.5827 | 0.4902 | 518.6 | 511.495 | 3.9068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 297.13 |  | 295.2758 | 0.628 | 297.25 | 293.555 | 1.427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ENTG | semiconductor_materials | 119.6 |  | 119.146 | 0.3811 | 121 | 117.72 | 0.51 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SMH | semiconductor_index | 524.03 |  | 526.4972 | -0.4686 | 533.01 | 523.325 | 0.0725 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 486.81 |  | 489.6356 | -0.5771 | 497.64 | 485.42 | 0.0965 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 737.01 |  | 737.759 | -0.1015 | 739.42 | 736.57 | 0.0366 | below_vwap | below_vwap |
| 10 | AMZN | cloud_ai_capex | 229.9 |  | 230.674 | -0.3356 | 233.05 | 229.7 | 0.0217 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ASML | semiconductor_equipment | 1570.4 |  | 1574.9911 | -0.2915 | 1586.01 | 1565.95 | 0.3197 | below_vwap | below_vwap |
| 13 | AAPL | mega_cap_platform | 338.29 |  | 339.3897 | -0.324 | 342.87 | 337.78 | 0.1478 | below_vwap | below_vwap |
| 14 | CORZ | high_beta_ai_infrastructure | 20.01 |  | 20.075 | -0.3239 | 20.97 | 19.755 | 0.05 | below_vwap | below_vwap |
| 15 | TT | data_center_power_cooling | 464.27 |  | 464.5738 | -0.0654 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 585.32 |  | 588.8261 | -0.5954 | 603.25 | 584.69 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GEV | data_center_power_cooling | 937.835 |  | 943.2474 | -0.5738 | 955.825 | 935.665 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ALAB | ai_networking_optical | 254.13 |  | 255.4713 | -0.525 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | APLD | high_beta_ai_infrastructure | 26.125 |  | 26.3711 | -0.9332 | 27 | 25.42 | 0.1531 | below_vwap | below_vwap |
| 20 | ONTO | semiconductor_test_packaging | 237.92 |  | 240.3972 | -1.0305 | 248.8 | 236.42 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 520.12 |  | 517.5827 | 0.4902 | 518.6 | 511.495 | 3.9068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | GOOGL | cloud_ai_capex | 327.13 |  | 327.1228 | 0.0022 | 330.21 | 324.97 | 0.0397 | watch_only | none |
| 3 | JCI | data_center_power_cooling | 138.6 |  | 138.0606 | 0.3907 | 139.755 | 137.31 | 0.1299 | watch_only | none |
| 4 | TSM | foundry | 385.14 |  | 385.7989 | -0.1708 | 390.46 | 382.495 | 1.5215 | below_vwap | below_vwap,spread_too_wide |
| 5 | MU | memory_hbm_storage | 814.94 |  | 824.2384 | -1.1281 | 846.4 | 813.91 | 0.373 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 524.03 |  | 526.4972 | -0.4686 | 533.01 | 523.325 | 0.0725 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 486.81 |  | 489.6356 | -0.5771 | 497.64 | 485.42 | 0.0965 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 737.01 |  | 737.759 | -0.1015 | 739.42 | 736.57 | 0.0366 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1570.4 |  | 1574.9911 | -0.2915 | 1586.01 | 1565.95 | 0.3197 | below_vwap | below_vwap |
| 10 | TT | data_center_power_cooling | 464.27 |  | 464.5738 | -0.0654 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 585.32 |  | 588.8261 | -0.5954 | 603.25 | 584.69 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | GEV | data_center_power_cooling | 937.835 |  | 943.2474 | -0.5738 | 955.825 | 935.665 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ETN | data_center_power_cooling | 379.33 |  | 379.4315 | -0.0267 | 384.565 | 377.43 | 4.2021 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMAT | semiconductor_equipment | 478.22 |  | 481.5111 | -0.6835 | 494.87 | 477.03 | 1.2693 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMD | ai_accelerator | 454.03 |  | 459.0087 | -1.0847 | 472.485 | 453.76 | 0.7753 | below_vwap | below_vwap,spread_too_wide |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ALAB | ai_networking_optical | 254.13 |  | 255.4713 | -0.525 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 190.38 |  | 191.6172 | -0.6457 | 194.96 | 189.48 | 1.4602 | below_vwap | below_vwap,spread_too_wide |
| 19 | ORCL | cloud_ai_capex | 115.36 |  | 115.9457 | -0.5052 | 117.17 | 115.25 | 4.2476 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMZN | cloud_ai_capex | 229.9 |  | 230.674 | -0.3356 | 233.05 | 229.7 | 0.0217 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.19 |  | 672.4759 | -0.3399 | 677.3 | 670.84 | 0.0925 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 60.02 |  | 60.737 | -1.1805 | 62.01 | 60.23 | 0.0167 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 193.41 |  | 194.1894 | -0.4014 | 195.4 | 193.65 | 0.0259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 391.885 |  | 394.7871 | -0.7351 | 400.09 | 392.355 | 0.0408 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 338.29 |  | 339.3897 | -0.324 | 342.87 | 337.78 | 0.1478 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 327.13 |  | 327.1228 | 0.0022 | 330.21 | 324.97 | 0.0397 | watch_only | none |
| AMD | ai_accelerator | 454.03 |  | 459.0087 | -1.0847 | 472.485 | 453.76 | 0.7753 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 385.14 |  | 385.7989 | -0.1708 | 390.46 | 382.495 | 1.5215 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 486.81 |  | 489.6356 | -0.5771 | 497.64 | 485.42 | 0.0965 | below_vwap | below_vwap |
| SMH | semiconductor_index | 524.03 |  | 526.4972 | -0.4686 | 533.01 | 523.325 | 0.0725 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 375.7 |  | 374.6282 | 0.2861 | 378.64 | 371.57 | 1.1073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 814.94 |  | 824.2384 | -1.1281 | 846.4 | 813.91 | 0.373 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 171.26 |  | 174.3897 | -1.7947 | 181.24 | 172.395 | 0.6773 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 365.69 |  | 374.5834 | -2.3742 | 402 | 374.02 | 1.8595 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.99 |  | 44.4466 | -1.0272 | 46.19 | 44.33 | 0.1364 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.36 |  | 27.849 | -1.7559 | 28.86 | 27.59 | 0.1096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.01 |  | 737.759 | -0.1015 | 739.42 | 736.57 | 0.0366 | below_vwap | below_vwap |
| IWM | market_regime | 291.09 |  | 292.1631 | -0.3673 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.36 |  | 115.9457 | -0.5052 | 117.17 | 115.25 | 4.2476 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 65.42 |  | 66.3381 | -1.3839 | 68.995 | 65.635 | 4.3412 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 265.725 |  | 269.2002 | -1.2909 | 273.86 | 266.04 | 4.8471 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 379.33 |  | 379.4315 | -0.0267 | 384.565 | 377.43 | 4.2021 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 585.32 |  | 588.8261 | -0.5954 | 603.25 | 584.69 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 937.835 |  | 943.2474 | -0.5738 | 955.825 | 935.665 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 464.27 |  | 464.5738 | -0.0654 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 138.6 |  | 138.0606 | 0.3907 | 139.755 | 137.31 | 0.1299 | watch_only | none |
| ANET | ai_networking_optical | 160.04 |  | 161.7263 | -1.0427 | 165.975 | 160.51 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 235.73 |  | 240.0676 | -1.8068 | 256.145 | 236.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 619.315 |  | 633.3143 | -2.2105 | 673.65 | 624.91 | 3.646 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 336.72 |  | 341.4385 | -1.382 | 354.09 | 338.14 | 0.5227 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 83.27 |  | 85.859 | -3.0154 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 254.13 |  | 255.4713 | -0.525 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1570.4 |  | 1574.9911 | -0.2915 | 1586.01 | 1565.95 | 0.3197 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 478.22 |  | 481.5111 | -0.6835 | 494.87 | 477.03 | 1.2693 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 266.99 |  | 268.7043 | -0.638 | 276.85 | 267.14 | 4.7455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 190.38 |  | 191.6172 | -0.6457 | 194.96 | 189.48 | 1.4602 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 303.64 |  | 305.4561 | -0.5945 | 315.21 | 304.11 | 0.3557 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 237.92 |  | 240.3972 | -1.0305 | 248.8 | 236.42 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.605 |  | 48.1589 | -3.2266 | 51.64 | 47.435 | 1.3089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.75 |  | 43.3423 | -1.3666 | 44.155 | 42.75 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.6 |  | 119.146 | 0.3811 | 121 | 117.72 | 0.51 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 282.13 |  | 285.9512 | -1.3363 | 296.8 | 283.22 | 2.07 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 520.12 |  | 517.5827 | 0.4902 | 518.6 | 511.495 | 3.9068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.13 |  | 295.2758 | 0.628 | 297.25 | 293.555 | 1.427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.125 |  | 26.3711 | -0.9332 | 27 | 25.42 | 0.1531 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 32.855 |  | 33.5594 | -2.0989 | 35.08 | 33.52 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.01 |  | 20.075 | -0.3239 | 20.97 | 19.755 | 0.05 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1109.03 |  | 1129.7859 | -1.8372 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 430.845 |  | 439.7597 | -2.0272 | 465.04 | 435.22 | 0.5106 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 713.46 |  | 728.4465 | -2.0573 | 774.805 | 719.02 | 1.1437 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 229.9 |  | 230.674 | -0.3356 | 233.05 | 229.7 | 0.0217 | below_vwap | below_vwap |
| META | cloud_ai_capex | 594.01 |  | 596.4485 | -0.4088 | 600.765 | 594.21 | 0.1279 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 242.83 |  | 246.4913 | -1.4853 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.23 |  | 132.4509 | -2.4318 | 136.45 | 131.735 | 4.4726 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
