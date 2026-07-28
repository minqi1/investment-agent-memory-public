# Intraday State

- Generated at: `2026-07-28T22:37:00+08:00`
- Market time ET: `2026-07-28T10:37:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 33, 'below_vwap': 13, 'watch_only': 7, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.75 |  | 671.2 | -0.067 | 677.3 | 670.84 | 0.0552 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 485.05 |  | 488.174 | -0.6399 | 497.64 | 485.42 | 0.099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 523.18 |  | 524.8761 | -0.3231 | 533.01 | 523.325 | 0.0726 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.91 |  | 737.5109 | 0.0541 | 739.42 | 736.57 | 0.0285 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 737.91 |  | 737.5109 | 0.0541 | 739.42 | 736.57 | 0.0285 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 327.745 |  | 327.1095 | 0.1943 | 330.21 | 324.97 | 0.0854 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 395.425 |  | 394.6552 | 0.1951 | 400.09 | 392.355 | 0.0303 | watch_only | none |
| 4 | AVGO | custom_silicon_networking | 375.785 |  | 375.2475 | 0.1432 | 378.64 | 371.57 | 0.1676 | watch_only | none |
| 5 | NVDA | ai_accelerator | 195.17 |  | 194.0511 | 0.5766 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| 6 | SMCI | ai_server_oem | 27.77 |  | 27.6308 | 0.5038 | 28.86 | 27.59 | 0.072 | watch_only | none |
| 7 | LIN | industrial_gases | 519.7 |  | 518.6399 | 0.2044 | 518.6 | 511.495 | 4.162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 163.08 |  | 161.5968 | 0.9178 | 165.975 | 160.51 | 0.2146 | watch_only | none |
| 9 | ASML | semiconductor_equipment | 1576.145 |  | 1570.0981 | 0.3851 | 1586.01 | 1565.95 | 0.5019 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | HPE | ai_server_oem | 44.105 |  | 44.0181 | 0.1974 | 46.19 | 44.33 | 0.0907 | below_opening_15m_low | below_opening_15m_low |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | TT | data_center_power_cooling | 462.74 |  | 464.0839 | -0.2896 | 477.73 | 460.77 | 0.2183 | below_vwap | below_vwap |
| 13 | STX | memory_hbm_storage | 721.44 |  | 721.7033 | -0.0365 | 774.805 | 719.02 | 0.2634 | below_vwap | below_vwap |
| 14 | CORZ | high_beta_ai_infrastructure | 19.89 |  | 19.9464 | -0.2829 | 20.97 | 19.755 | 0.0503 | below_vwap | below_vwap |
| 15 | DELL | ai_server_oem | 372.25 |  | 370.5523 | 0.4581 | 402 | 374.02 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 253.885 |  | 255.3004 | -0.5544 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | AAPL | mega_cap_platform | 338.29 |  | 338.6594 | -0.1091 | 342.87 | 337.78 | 0.2069 | below_vwap | below_vwap |
| 18 | COHU | semiconductor_test_packaging | 42.21 |  | 42.6828 | -1.1077 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | TSM | foundry | 382.945 |  | 384.7288 | -0.4637 | 390.46 | 382.495 | 0.6554 | below_vwap | below_vwap,spread_too_wide |
| 20 | ORCL | cloud_ai_capex | 115.695 |  | 115.7053 | -0.0089 | 117.17 | 115.25 | 3.6994 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 519.7 |  | 518.6399 | 0.2044 | 518.6 | 511.495 | 4.162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | NVDA | ai_accelerator | 195.17 |  | 194.0511 | 0.5766 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 375.785 |  | 375.2475 | 0.1432 | 378.64 | 371.57 | 0.1676 | watch_only | none |
| 4 | SPY | market_regime | 737.91 |  | 737.5109 | 0.0541 | 739.42 | 736.57 | 0.0285 | watch_only | none |
| 5 | ANET | ai_networking_optical | 163.08 |  | 161.5968 | 0.9178 | 165.975 | 160.51 | 0.2146 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 327.745 |  | 327.1095 | 0.1943 | 330.21 | 324.97 | 0.0854 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 395.425 |  | 394.6552 | 0.1951 | 400.09 | 392.355 | 0.0303 | watch_only | none |
| 8 | SMCI | ai_server_oem | 27.77 |  | 27.6308 | 0.5038 | 28.86 | 27.59 | 0.072 | watch_only | none |
| 9 | TSM | foundry | 382.945 |  | 384.7288 | -0.4637 | 390.46 | 382.495 | 0.6554 | below_vwap | below_vwap,spread_too_wide |
| 10 | TT | data_center_power_cooling | 462.74 |  | 464.0839 | -0.2896 | 477.73 | 460.77 | 0.2183 | below_vwap | below_vwap |
| 11 | STX | memory_hbm_storage | 721.44 |  | 721.7033 | -0.0365 | 774.805 | 719.02 | 0.2634 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ALAB | ai_networking_optical | 253.885 |  | 255.3004 | -0.5544 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ORCL | cloud_ai_capex | 115.695 |  | 115.7053 | -0.0089 | 117.17 | 115.25 | 3.6994 | below_vwap | below_vwap,spread_too_wide |
| 15 | APD | industrial_gases | 296.38 |  | 296.4565 | -0.0258 | 297.25 | 293.555 | 4.3458 | below_vwap | below_vwap,spread_too_wide |
| 16 | ENTG | semiconductor_materials | 118.61 |  | 119.1206 | -0.4287 | 121 | 117.72 | 0.6323 | below_vwap | below_vwap,spread_too_wide |
| 17 | COHU | semiconductor_test_packaging | 42.21 |  | 42.6828 | -1.1077 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AAPL | mega_cap_platform | 338.29 |  | 338.6594 | -0.1091 | 342.87 | 337.78 | 0.2069 | below_vwap | below_vwap |
| 19 | CORZ | high_beta_ai_infrastructure | 19.89 |  | 19.9464 | -0.2829 | 20.97 | 19.755 | 0.0503 | below_vwap | below_vwap |
| 20 | APLD | high_beta_ai_infrastructure | 26.29 |  | 26.298 | -0.0304 | 27 | 25.42 | 1.1031 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.75 |  | 671.2 | -0.067 | 677.3 | 670.84 | 0.0552 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 60.23 |  | 60.3799 | -0.2483 | 62.01 | 60.23 | 0.0332 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 195.17 |  | 194.0511 | 0.5766 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| MSFT | cloud_ai_capex | 395.425 |  | 394.6552 | 0.1951 | 400.09 | 392.355 | 0.0303 | watch_only | none |
| AAPL | mega_cap_platform | 338.29 |  | 338.6594 | -0.1091 | 342.87 | 337.78 | 0.2069 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 327.745 |  | 327.1095 | 0.1943 | 330.21 | 324.97 | 0.0854 | watch_only | none |
| AMD | ai_accelerator | 450.47 |  | 453.4425 | -0.6556 | 472.485 | 453.76 | 2.8615 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 382.945 |  | 384.7288 | -0.4637 | 390.46 | 382.495 | 0.6554 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 485.05 |  | 488.174 | -0.6399 | 497.64 | 485.42 | 0.099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 523.18 |  | 524.8761 | -0.3231 | 533.01 | 523.325 | 0.0726 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.785 |  | 375.2475 | 0.1432 | 378.64 | 371.57 | 0.1676 | watch_only | none |
| MU | memory_hbm_storage | 806.85 |  | 811.3001 | -0.5485 | 846.4 | 813.91 | 2.3548 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 169.44 |  | 171.689 | -1.3099 | 181.24 | 172.395 | 1.9417 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 372.25 |  | 370.5523 | 0.4581 | 402 | 374.02 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| HPE | ai_server_oem | 44.105 |  | 44.0181 | 0.1974 | 46.19 | 44.33 | 0.0907 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.77 |  | 27.6308 | 0.5038 | 28.86 | 27.59 | 0.072 | watch_only | none |
| SPY | market_regime | 737.91 |  | 737.5109 | 0.0541 | 739.42 | 736.57 | 0.0285 | watch_only | none |
| IWM | market_regime | 290.83 |  | 291.6659 | -0.2866 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.695 |  | 115.7053 | -0.0089 | 117.17 | 115.25 | 3.6994 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 65.5 |  | 65.9297 | -0.6517 | 68.995 | 65.635 | 4.5802 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 260.69 |  | 266.0856 | -2.0278 | 273.86 | 266.04 | 0.7672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 377.35 |  | 378.5956 | -0.329 | 384.565 | 377.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 571.965 |  | 579.7621 | -1.3449 | 603.25 | 584.69 | 4.4985 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 922.72 |  | 933.8554 | -1.1924 | 955.825 | 935.665 | 0.518 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 462.74 |  | 464.0839 | -0.2896 | 477.73 | 460.77 | 0.2183 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 136.885 |  | 137.8246 | -0.6817 | 139.755 | 137.31 | 4.8289 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 163.08 |  | 161.5968 | 0.9178 | 165.975 | 160.51 | 0.2146 | watch_only | none |
| COHR | ai_networking_optical | 230.8 |  | 236.5201 | -2.4185 | 256.145 | 236.73 | 1.4731 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 614.96 |  | 623.469 | -1.3648 | 673.65 | 624.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 332.03 |  | 335.6639 | -1.0826 | 354.09 | 338.14 | 4.867 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 83.455 |  | 84.7453 | -1.5226 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 253.885 |  | 255.3004 | -0.5544 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1576.145 |  | 1570.0981 | 0.3851 | 1586.01 | 1565.95 | 0.5019 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 472.11 |  | 477.7847 | -1.1877 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 261.93 |  | 265.833 | -1.4682 | 276.85 | 267.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 188.43 |  | 189.945 | -0.7976 | 194.96 | 189.48 | 0.3131 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 304.03 |  | 305.1063 | -0.3528 | 315.21 | 304.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 231.49 |  | 238.04 | -2.7516 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.015 |  | 47.2973 | -2.7111 | 51.64 | 47.435 | 4.216 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.21 |  | 42.6828 | -1.1077 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.61 |  | 119.1206 | -0.4287 | 121 | 117.72 | 0.6323 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 279.14 |  | 282.4294 | -1.1647 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 519.7 |  | 518.6399 | 0.2044 | 518.6 | 511.495 | 4.162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.38 |  | 296.4565 | -0.0258 | 297.25 | 293.555 | 4.3458 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.29 |  | 26.298 | -0.0304 | 27 | 25.42 | 1.1031 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.175 |  | 33.2559 | -0.2431 | 35.08 | 33.52 | 0.0904 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.89 |  | 19.9464 | -0.2829 | 20.97 | 19.755 | 0.0503 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1092.14 |  | 1103.726 | -1.0497 | 1185.19 | 1114.57 | 3.7486 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 430.88 |  | 433.567 | -0.6197 | 465.04 | 435.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 721.44 |  | 721.7033 | -0.0365 | 774.805 | 719.02 | 0.2634 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 228.84 |  | 230.1932 | -0.5879 | 233.05 | 229.7 | 0.0262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 591.87 |  | 594.9261 | -0.5137 | 600.765 | 594.21 | 0.1115 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 243.13 |  | 244.6718 | -0.6301 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.91 |  | 131.2494 | -0.2586 | 136.45 | 131.735 | 4.3847 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
