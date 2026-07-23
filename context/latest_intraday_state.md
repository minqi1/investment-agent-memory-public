# Intraday State

- Generated at: `2026-07-24T03:45:21+08:00`
- Market time ET: `2026-07-23T15:45:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 22, 'watch_only': 2, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.47 |  | 692.6192 | -0.4547 | 698.65 | 693.24 | 0.0044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.16 |  | 550.506 | -0.7895 | 557.38 | 545.965 | 0.0659 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.58 |  | 580.2231 | -0.8002 | 585.98 | 576.635 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.27 |  | 738.3521 | -0.282 | 742.515 | 738.54 | 0.0081 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.115 |  | 320.9091 | 0.0642 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| 2 | CORZ | high_beta_ai_infrastructure | 24.08 |  | 24.0739 | 0.0255 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 3 | TT | data_center_power_cooling | 479.63 |  | 477.0918 | 0.532 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ARM | ai_accelerator | 281.16 |  | 280.0786 | 0.3861 | 283 | 276.24 | 2.3332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SOXX | semiconductor_index | 546.16 |  | 550.506 | -0.7895 | 557.38 | 545.965 | 0.0659 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 981.92 |  | 990.5507 | -0.8713 | 999.04 | 964.86 | 0.0713 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1793.11 |  | 1801.2398 | -0.4513 | 1806.11 | 1780.9 | 0.0563 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 215.32 |  | 215.851 | -0.246 | 217.88 | 212.99 | 0.0604 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 291.61 |  | 291.6118 | -0.0006 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 10 | SKHY | memory_hbm_storage | 168.85 |  | 172.8702 | -2.3255 | 177.88 | 168.18 | 0.0533 | below_vwap | below_vwap |
| 11 | CRWV | gpu_cloud_ai_factory | 80.775 |  | 82.3726 | -1.9394 | 84.415 | 80.64 | 0.0867 | below_vwap | below_vwap |
| 12 | SMCI | ai_server_oem | 31.01 |  | 31.5578 | -1.7359 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 40.7 |  | 41.4924 | -1.9097 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| 15 | ANET | ai_networking_optical | 175.62 |  | 176.5586 | -0.5316 | 177.84 | 173.19 | 0.1765 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.535 |  | 143.7755 | -0.1673 | 145.035 | 141.815 | 0.1811 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 318.75 |  | 319.9856 | -0.3861 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 505.65 |  | 507.0379 | -0.2737 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHR | ai_networking_optical | 311.24 |  | 316.4659 | -1.6513 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CIEN | ai_networking_optical | 402.68 |  | 407.4411 | -1.1685 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036.97 |  | 1019.0349 | 1.76 | 1023.33 | 979.08 | 3.8429 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | AAPL | mega_cap_platform | 321.115 |  | 320.9091 | 0.0642 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| 3 | CORZ | high_beta_ai_infrastructure | 24.08 |  | 24.0739 | 0.0255 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 4 | TSM | foundry | 413.47 |  | 416.1548 | -0.6452 | 420.72 | 412.69 | 0.5079 | below_vwap | below_vwap,spread_too_wide |
| 5 | SOXX | semiconductor_index | 546.16 |  | 550.506 | -0.7895 | 557.38 | 545.965 | 0.0659 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 981.92 |  | 990.5507 | -0.8713 | 999.04 | 964.86 | 0.0713 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1793.11 |  | 1801.2398 | -0.4513 | 1806.11 | 1780.9 | 0.0563 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 558.365 |  | 563.4124 | -0.8959 | 566.18 | 548.47 | 3.3115 | below_vwap | below_vwap,spread_too_wide |
| 9 | ANET | ai_networking_optical | 175.62 |  | 176.5586 | -0.5316 | 177.84 | 173.19 | 0.1765 | below_vwap | below_vwap |
| 10 | JCI | data_center_power_cooling | 143.535 |  | 143.7755 | -0.1673 | 145.035 | 141.815 | 0.1811 | below_vwap | below_vwap |
| 11 | PWR | data_center_power_cooling | 650.31 |  | 650.7303 | -0.0646 | 656.38 | 642.37 | 1.1702 | below_vwap | below_vwap,spread_too_wide |
| 12 | KLAC | semiconductor_equipment | 215.32 |  | 215.851 | -0.246 | 217.88 | 212.99 | 0.0604 | below_vwap | below_vwap |
| 13 | ETN | data_center_power_cooling | 413.31 |  | 413.3953 | -0.0206 | 415.53 | 406.545 | 0.5904 | below_vwap | below_vwap,spread_too_wide |
| 14 | IWM | market_regime | 291.61 |  | 291.6118 | -0.0006 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 318.75 |  | 319.9856 | -0.3861 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 558.35 |  | 563.652 | -0.9406 | 576.24 | 556.3 | 0.3528 | below_vwap | below_vwap,spread_too_wide |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 341.8 |  | 342.4553 | -0.1914 | 347.92 | 341.755 | 4.5553 | below_vwap | below_vwap,spread_too_wide |
| 19 | LIN | industrial_gases | 505.65 |  | 507.0379 | -0.2737 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 311.24 |  | 316.4659 | -1.6513 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.47 |  | 692.6192 | -0.4547 | 698.65 | 693.24 | 0.0044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.5 |  | 66.4651 | -1.452 | 68.245 | 66.7 | 0.0305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.97 |  | 208.4456 | -0.7079 | 210.85 | 208.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.16 |  | 382.3366 | -0.5693 | 391.71 | 387.245 | 0.1368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.115 |  | 320.9091 | 0.0642 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| GOOGL | cloud_ai_capex | 318.04 |  | 319.4096 | -0.4288 | 324.42 | 320.24 | 0.0126 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 536.955 |  | 539.8457 | -0.5355 | 556.12 | 542.33 | 0.3259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 413.47 |  | 416.1548 | -0.6452 | 420.72 | 412.69 | 0.5079 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.16 |  | 550.506 | -0.7895 | 557.38 | 545.965 | 0.0659 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.58 |  | 580.2231 | -0.8002 | 585.98 | 576.635 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.3 |  | 391.8561 | -0.6523 | 397.34 | 390.54 | 1.2022 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 981.92 |  | 990.5507 | -0.8713 | 999.04 | 964.86 | 0.0713 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.17 |  | 209.0983 | -1.4004 | 213.785 | 207.665 | 0.0873 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 436.695 |  | 442.8826 | -1.3971 | 450.07 | 438.55 | 1.6579 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.49 |  | 48.183 | -1.4383 | 48.88 | 47.635 | 0.0632 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.01 |  | 31.5578 | -1.7359 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 736.27 |  | 738.3521 | -0.282 | 742.515 | 738.54 | 0.0081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.61 |  | 291.6118 | -0.0006 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.71 |  | 121.5595 | -1.5215 | 124.22 | 122.07 | 0.0418 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.775 |  | 82.3726 | -1.9394 | 84.415 | 80.64 | 0.0867 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 303 |  | 305.5871 | -0.8466 | 311.13 | 303.96 | 0.736 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.31 |  | 413.3953 | -0.0206 | 415.53 | 406.545 | 0.5904 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 650.31 |  | 650.7303 | -0.0646 | 656.38 | 642.37 | 1.1702 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1036.97 |  | 1019.0349 | 1.76 | 1023.33 | 979.08 | 3.8429 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 479.63 |  | 477.0918 | 0.532 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.535 |  | 143.7755 | -0.1673 | 145.035 | 141.815 | 0.1811 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 175.62 |  | 176.5586 | -0.5316 | 177.84 | 173.19 | 0.1765 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 311.24 |  | 316.4659 | -1.6513 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 828.82 |  | 853.3489 | -2.8744 | 880.26 | 833 | 3.7403 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.68 |  | 407.4411 | -1.1685 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 111.46 |  | 114.2746 | -2.463 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 321.3 |  | 325.9515 | -1.427 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.11 |  | 1801.2398 | -0.4513 | 1806.11 | 1780.9 | 0.0563 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.365 |  | 563.4124 | -0.8959 | 566.18 | 548.47 | 3.3115 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.75 |  | 319.9856 | -0.3861 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.32 |  | 215.851 | -0.246 | 217.88 | 212.99 | 0.0604 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 368.57 |  | 371.6769 | -0.8359 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.77 |  | 293.5402 | -1.2844 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.855 |  | 65.172 | -0.4864 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4331 | -0.3731 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.43 |  | 134.9533 | -0.3877 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.8 |  | 342.4553 | -0.1914 | 347.92 | 341.755 | 4.5553 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 505.65 |  | 507.0379 | -0.2737 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.23 |  | 295.6609 | -0.1457 | 299.26 | 295.795 | 0.1727 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 29.73 |  | 30.0375 | -1.0237 | 31.13 | 29.12 | 0.0673 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.7 |  | 41.4924 | -1.9097 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.08 |  | 24.0739 | 0.0255 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| SNDK | memory_hbm_storage | 1609.79 |  | 1639.4582 | -1.8096 | 1651.355 | 1560 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 558.35 |  | 563.652 | -0.9406 | 576.24 | 556.3 | 0.3528 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 913.02 |  | 922.2177 | -0.9973 | 933.5 | 908.955 | 4.2825 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.155 |  | 234.2553 | -0.4697 | 238.285 | 235.71 | 0.0257 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 604.47 |  | 604.7918 | -0.0532 | 614.15 | 605.39 | 0.0414 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 281.16 |  | 280.0786 | 0.3861 | 283 | 276.24 | 2.3332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.85 |  | 172.8702 | -2.3255 | 177.88 | 168.18 | 0.0533 | below_vwap | below_vwap |
