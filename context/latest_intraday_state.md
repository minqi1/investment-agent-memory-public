# Intraday State

- Generated at: `2026-07-28T21:47:35+08:00`
- Market time ET: `2026-07-28T09:47:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 30, 'below_vwap': 22, 'price_stale_or_missing': 1, 'watch_only': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 669.95 |  | 673.465 | -0.5219 | 677.3 | 670.84 | 0.0134 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 485.16 |  | 490.4279 | -1.0741 | 497.64 | 485.42 | 0.0515 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 522.53 |  | 527.3749 | -0.9187 | 533.01 | 523.325 | 0.0823 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.485 |  | 738.0244 | -0.2086 | 739.42 | 736.57 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.41 |  | 516.0772 | 0.452 | 518.6 | 511.495 | 0.1427 | watch_only | none |
| 2 | TSM | foundry | 384.21 |  | 385.6813 | -0.3815 | 390.46 | 382.495 | 0.0547 | below_vwap | below_vwap |
| 3 | MSFT | cloud_ai_capex | 394.8 |  | 395.5982 | -0.2018 | 400.09 | 392.355 | 0.0456 | below_vwap | below_vwap |
| 4 | AMZN | cloud_ai_capex | 229.84 |  | 230.927 | -0.4707 | 233.05 | 229.7 | 0.0174 | below_vwap | below_vwap |
| 5 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 6 | AVGO | custom_silicon_networking | 372.68 |  | 374.1134 | -0.3831 | 378.64 | 371.57 | 0.2012 | below_vwap | below_vwap |
| 7 | APD | industrial_gases | 296.99 |  | 294.487 | 0.8499 | 297.25 | 293.555 | 1.5859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AAPL | mega_cap_platform | 338.34 |  | 339.6493 | -0.3855 | 342.87 | 337.78 | 0.0502 | below_vwap | below_vwap |
| 9 | TT | data_center_power_cooling | 465.065 |  | 465.4516 | -0.0831 | 477.73 | 460.77 | 0.2817 | below_vwap | below_vwap |
| 10 | CORZ | high_beta_ai_infrastructure | 20.015 |  | 20.0929 | -0.3878 | 20.97 | 19.755 | 0.1499 | below_vwap | below_vwap |
| 11 | VRT | data_center_power_cooling | 266.75 |  | 270.2297 | -1.2877 | 273.86 | 266.04 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 584.69 |  | 590.1764 | -0.9296 | 603.25 | 584.69 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 137.81 |  | 138.0663 | -0.1856 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ETN | data_center_power_cooling | 378.95 |  | 379.6485 | -0.184 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | APLD | high_beta_ai_infrastructure | 26.565 |  | 26.3047 | 0.9897 | 27 | 25.42 | 1.8822 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ORCL | cloud_ai_capex | 115.415 |  | 115.9767 | -0.4843 | 117.17 | 115.25 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CIEN | ai_networking_optical | 338.49 |  | 344.4659 | -1.7348 | 354.09 | 338.14 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 283.22 |  | 289.0049 | -2.0017 | 296.8 | 283.22 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ENTG | semiconductor_materials | 118.01 |  | 118.709 | -0.5888 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 237.535 |  | 241.404 | -1.6027 | 248.8 | 236.92 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.41 |  | 516.0772 | 0.452 | 518.6 | 511.495 | 0.1427 | watch_only | none |
| 2 | TSM | foundry | 384.21 |  | 385.6813 | -0.3815 | 390.46 | 382.495 | 0.0547 | below_vwap | below_vwap |
| 3 | AVGO | custom_silicon_networking | 372.68 |  | 374.1134 | -0.3831 | 378.64 | 371.57 | 0.2012 | below_vwap | below_vwap |
| 4 | ASML | semiconductor_equipment | 1567.775 |  | 1575.7281 | -0.5047 | 1586.01 | 1565.95 | 0.6621 | below_vwap | below_vwap,spread_too_wide |
| 5 | TT | data_center_power_cooling | 465.065 |  | 465.4516 | -0.0831 | 477.73 | 460.77 | 0.2817 | below_vwap | below_vwap |
| 6 | VRT | data_center_power_cooling | 266.75 |  | 270.2297 | -1.2877 | 273.86 | 266.04 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | PWR | data_center_power_cooling | 584.69 |  | 590.1764 | -0.9296 | 603.25 | 584.69 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 938.48 |  | 944.6945 | -0.6578 | 955.825 | 935.665 | 4.8067 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 137.81 |  | 138.0663 | -0.1856 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 378.95 |  | 379.6485 | -0.184 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ALAB | ai_networking_optical | 253.07 |  | 256.0819 | -1.1761 | 268.265 | 253.05 | 0.6243 | below_vwap | below_vwap,spread_too_wide |
| 13 | ORCL | cloud_ai_capex | 115.415 |  | 115.9767 | -0.4843 | 117.17 | 115.25 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | MSFT | cloud_ai_capex | 394.8 |  | 395.5982 | -0.2018 | 400.09 | 392.355 | 0.0456 | below_vwap | below_vwap |
| 15 | AMZN | cloud_ai_capex | 229.84 |  | 230.927 | -0.4707 | 233.05 | 229.7 | 0.0174 | below_vwap | below_vwap |
| 16 | CIEN | ai_networking_optical | 338.49 |  | 344.4659 | -1.7348 | 354.09 | 338.14 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | MKSI | semiconductor_materials | 283.22 |  | 289.0049 | -2.0017 | 296.8 | 283.22 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 118.01 |  | 118.709 | -0.5888 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1117.52 |  | 1140.5636 | -2.0204 | 1185.19 | 1114.57 | 4.4044 | below_vwap | below_vwap,spread_too_wide |
| 20 | ONTO | semiconductor_test_packaging | 237.535 |  | 241.404 | -1.6027 | 248.8 | 236.92 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 669.95 |  | 673.465 | -0.5219 | 677.3 | 670.84 | 0.0134 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 59.96 |  | 60.8962 | -1.5374 | 62.01 | 60.23 | 0.0167 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 193.305 |  | 194.3694 | -0.5476 | 195.4 | 193.65 | 0.0466 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 394.8 |  | 395.5982 | -0.2018 | 400.09 | 392.355 | 0.0456 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 338.34 |  | 339.6493 | -0.3855 | 342.87 | 337.78 | 0.0502 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 324.86 |  | 327.5069 | -0.8082 | 330.21 | 324.97 | 0.1631 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 453.19 |  | 460.0253 | -1.4858 | 472.485 | 453.76 | 0.7282 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 384.21 |  | 385.6813 | -0.3815 | 390.46 | 382.495 | 0.0547 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 485.16 |  | 490.4279 | -1.0741 | 497.64 | 485.42 | 0.0515 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 522.53 |  | 527.3749 | -0.9187 | 533.01 | 523.325 | 0.0823 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 372.68 |  | 374.1134 | -0.3831 | 378.64 | 371.57 | 0.2012 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 810.285 |  | 827.3678 | -2.0647 | 846.4 | 813.91 | 0.8269 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 171.63 |  | 175.3328 | -2.1119 | 181.24 | 172.395 | 0.6817 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 369.705 |  | 378.2559 | -2.2606 | 402 | 374.02 | 3.3189 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 44.1 |  | 44.5821 | -1.0814 | 46.19 | 44.33 | 0.1361 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.42 |  | 27.9597 | -1.9304 | 28.86 | 27.59 | 2.2247 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SPY | market_regime | 736.485 |  | 738.0244 | -0.2086 | 739.42 | 736.57 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.36 |  | 292.5207 | -0.3968 | 293.26 | 291.55 | 0.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.415 |  | 115.9767 | -0.4843 | 117.17 | 115.25 |  | below_vwap | below_vwap,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 65.44 |  | 66.6258 | -1.7798 | 68.995 | 65.635 | 4.0801 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 266.75 |  | 270.2297 | -1.2877 | 273.86 | 266.04 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 378.95 |  | 379.6485 | -0.184 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 584.69 |  | 590.1764 | -0.9296 | 603.25 | 584.69 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 938.48 |  | 944.6945 | -0.6578 | 955.825 | 935.665 | 4.8067 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 465.065 |  | 465.4516 | -0.0831 | 477.73 | 460.77 | 0.2817 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 137.81 |  | 138.0663 | -0.1856 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 160.48 |  | 162.2085 | -1.0656 | 165.975 | 160.51 | 4.3806 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 235.54 |  | 242.9901 | -3.066 | 256.145 | 236.73 | 3.4177 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 624.26 |  | 636.876 | -1.9809 | 673.65 | 624.91 | 4.0608 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 338.49 |  | 344.4659 | -1.7348 | 354.09 | 338.14 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 84.14 |  | 87.0341 | -3.3252 | 92.95 | 84.63 | 3.9458 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 253.07 |  | 256.0819 | -1.1761 | 268.265 | 253.05 | 0.6243 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1567.775 |  | 1575.7281 | -0.5047 | 1586.01 | 1565.95 | 0.6621 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 474.775 |  | 483.0655 | -1.7162 | 494.87 | 477.03 | 0.5708 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 265.225 |  | 269.7162 | -1.6651 | 276.85 | 267.14 | 3.974 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 188.66 |  | 192.0669 | -1.7738 | 194.96 | 189.48 | 0.3233 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 302.25 |  | 307.2844 | -1.6384 | 315.21 | 304.11 | 4.6617 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 237.535 |  | 241.404 | -1.6027 | 248.8 | 236.92 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 47.01 |  | 48.5421 | -3.1562 | 51.64 | 47.435 | 3.9991 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 43.11 |  | 43.7735 | -1.5159 | 44.155 | 43.11 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.01 |  | 118.709 | -0.5888 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 283.22 |  | 289.0049 | -2.0017 | 296.8 | 283.22 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.41 |  | 516.0772 | 0.452 | 518.6 | 511.495 | 0.1427 | watch_only | none |
| APD | industrial_gases | 296.99 |  | 294.487 | 0.8499 | 297.25 | 293.555 | 1.5859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.565 |  | 26.3047 | 0.9897 | 27 | 25.42 | 1.8822 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.39 |  | 33.9289 | -1.5884 | 35.08 | 33.52 | 0.0898 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.015 |  | 20.0929 | -0.3878 | 20.97 | 19.755 | 0.1499 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1117.52 |  | 1140.5636 | -2.0204 | 1185.19 | 1114.57 | 4.4044 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 431.75 |  | 442.3088 | -2.3872 | 465.04 | 435.22 | 0.2432 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 709.93 |  | 733.9051 | -3.2668 | 774.805 | 719.02 | 0.1155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 229.84 |  | 230.927 | -0.4707 | 233.05 | 229.7 | 0.0174 | below_vwap | below_vwap |
| META | cloud_ai_capex | 593.65 |  | 597.7286 | -0.6824 | 600.765 | 594.21 | 0.0859 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 243 |  | 247.622 | -1.8666 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.9 |  | 133.3483 | -1.836 | 136.45 | 131.735 | 1.6883 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
