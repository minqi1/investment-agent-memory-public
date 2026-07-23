# Intraday State

- Generated at: `2026-07-24T03:41:25+08:00`
- Market time ET: `2026-07-23T15:41:26-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'watch_only': 4, 'below_vwap': 27, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.28 |  | 692.6443 | -0.3413 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.775 |  | 550.5367 | -0.5016 | 557.38 | 545.965 | 0.0402 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.23 |  | 580.2486 | -0.5202 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| SPY | market_regime | 736.84 |  | 738.3899 | -0.2099 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 216.29 |  | 215.8417 | 0.2077 | 217.88 | 212.99 | 0.0416 | watch_only | none |
| 2 | IWM | market_regime | 291.68 |  | 291.6113 | 0.0236 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 321.055 |  | 320.9063 | 0.0463 | 323.25 | 320.82 | 0.0966 | watch_only | none |
| 4 | ETN | data_center_power_cooling | 414.15 |  | 413.393 | 0.1831 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 479.98 |  | 477.0641 | 0.6112 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | PWR | data_center_power_cooling | 651.73 |  | 650.7413 | 0.1519 | 656.38 | 642.37 | 4.8701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | CORZ | high_beta_ai_infrastructure | 24.26 |  | 24.0706 | 0.7869 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| 8 | ARM | ai_accelerator | 282.05 |  | 280.015 | 0.7267 | 283 | 276.24 | 0.3581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | META | cloud_ai_capex | 604.88 |  | 604.7884 | 0.0151 | 614.15 | 605.39 | 0.1984 | below_opening_15m_low | below_opening_15m_low |
| 10 | SMH | semiconductor_index | 577.23 |  | 580.2486 | -0.5202 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 547.775 |  | 550.5367 | -0.5016 | 557.38 | 545.965 | 0.0402 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1796.63 |  | 1801.3547 | -0.2623 | 1806.11 | 1780.9 | 0.0262 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 559.165 |  | 563.5065 | -0.7704 | 566.18 | 548.47 | 0.059 | below_vwap | below_vwap |
| 14 | WDC | memory_hbm_storage | 560.27 |  | 563.6935 | -0.6073 | 576.24 | 556.3 | 0.0589 | below_vwap | below_vwap |
| 15 | SMCI | ai_server_oem | 31.22 |  | 31.5605 | -1.079 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 41.04 |  | 41.5015 | -1.1119 | 43.21 | 40.51 | 0.0487 | below_vwap | below_vwap |
| 18 | MU | memory_hbm_storage | 985.04 |  | 990.6745 | -0.5688 | 999.04 | 964.86 | 0.3188 | below_vwap | below_vwap |
| 19 | SKHY | memory_hbm_storage | 169.83 |  | 172.9369 | -1.7965 | 177.88 | 168.18 | 0.2709 | below_vwap | below_vwap |
| 20 | JCI | data_center_power_cooling | 143.58 |  | 143.7789 | -0.1383 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1039.895 |  | 1018.7131 | 2.0793 | 1023.33 | 979.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | KLAC | semiconductor_equipment | 216.29 |  | 215.8417 | 0.2077 | 217.88 | 212.99 | 0.0416 | watch_only | none |
| 3 | IWM | market_regime | 291.68 |  | 291.6113 | 0.0236 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 321.055 |  | 320.9063 | 0.0463 | 323.25 | 320.82 | 0.0966 | watch_only | none |
| 5 | CORZ | high_beta_ai_infrastructure | 24.26 |  | 24.0706 | 0.7869 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| 6 | TSM | foundry | 414.39 |  | 416.2063 | -0.4364 | 420.72 | 412.69 | 0.7047 | below_vwap | below_vwap,spread_too_wide |
| 7 | SMH | semiconductor_index | 577.23 |  | 580.2486 | -0.5202 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 547.775 |  | 550.5367 | -0.5016 | 557.38 | 545.965 | 0.0402 | below_vwap | below_vwap |
| 9 | AVGO | custom_silicon_networking | 390.57 |  | 391.8869 | -0.3361 | 397.34 | 390.54 | 1.4953 | below_vwap | below_vwap,spread_too_wide |
| 10 | MU | memory_hbm_storage | 985.04 |  | 990.6745 | -0.5688 | 999.04 | 964.86 | 0.3188 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1796.63 |  | 1801.3547 | -0.2623 | 1806.11 | 1780.9 | 0.0262 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 559.165 |  | 563.5065 | -0.7704 | 566.18 | 548.47 | 0.059 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 176.055 |  | 176.5678 | -0.2904 | 177.84 | 173.19 | 0.977 | below_vwap | below_vwap,spread_too_wide |
| 14 | JCI | data_center_power_cooling | 143.58 |  | 143.7789 | -0.1383 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | LRCX | semiconductor_equipment | 319.42 |  | 319.9966 | -0.1802 | 322.4 | 317.27 | 4.2201 | below_vwap | below_vwap,spread_too_wide |
| 16 | WDC | memory_hbm_storage | 560.27 |  | 563.6935 | -0.6073 | 576.24 | 556.3 | 0.0589 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 341.8 |  | 342.4553 | -0.1914 | 347.92 | 341.755 | 4.8128 | below_vwap | below_vwap,spread_too_wide |
| 19 | LIN | industrial_gases | 505.89 |  | 507.0517 | -0.2291 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 312.67 |  | 316.5341 | -1.2208 | 320.13 | 307.04 | 4.743 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.28 |  | 692.6443 | -0.3413 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.75 |  | 66.4713 | -1.0851 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.41 |  | 208.4645 | -0.5058 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.49 |  | 382.3658 | -0.4906 | 391.71 | 387.245 | 0.1262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.055 |  | 320.9063 | 0.0463 | 323.25 | 320.82 | 0.0966 | watch_only | none |
| GOOGL | cloud_ai_capex | 317.8 |  | 319.4333 | -0.5113 | 324.42 | 320.24 | 0.0031 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.755 |  | 539.863 | -0.2052 | 556.12 | 542.33 | 0.4548 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.39 |  | 416.2063 | -0.4364 | 420.72 | 412.69 | 0.7047 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.775 |  | 550.5367 | -0.5016 | 557.38 | 545.965 | 0.0402 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.23 |  | 580.2486 | -0.5202 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.57 |  | 391.8869 | -0.3361 | 397.34 | 390.54 | 1.4953 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 985.04 |  | 990.6745 | -0.5688 | 999.04 | 964.86 | 0.3188 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 207.3 |  | 209.1323 | -0.8761 | 213.785 | 207.665 | 0.1206 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.82 |  | 442.9919 | -1.1675 | 450.07 | 438.55 | 0.201 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 47.62 |  | 48.1895 | -1.1817 | 48.88 | 47.635 | 0.084 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.22 |  | 31.5605 | -1.079 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| SPY | market_regime | 736.84 |  | 738.3899 | -0.2099 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.68 |  | 291.6113 | 0.0236 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| ORCL | cloud_ai_capex | 119.81 |  | 121.6159 | -1.4849 | 124.22 | 122.07 | 0.5175 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.255 |  | 82.4062 | -1.3969 | 84.415 | 80.64 | 3.4459 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.93 |  | 305.6387 | -0.5591 | 311.13 | 303.96 | 1.2931 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.15 |  | 413.393 | 0.1831 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 651.73 |  | 650.7413 | 0.1519 | 656.38 | 642.37 | 4.8701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1039.895 |  | 1018.7131 | 2.0793 | 1023.33 | 979.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 479.98 |  | 477.0641 | 0.6112 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.58 |  | 143.7789 | -0.1383 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.055 |  | 176.5678 | -0.2904 | 177.84 | 173.19 | 0.977 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.67 |  | 316.5341 | -1.2208 | 320.13 | 307.04 | 4.743 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 833.53 |  | 853.6747 | -2.3598 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 404.32 |  | 407.5666 | -0.7966 | 408.58 | 397.9 | 4.1329 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.28 |  | 114.2989 | -1.7663 | 118.01 | 108.505 | 0.8461 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 322.93 |  | 326.0674 | -0.9622 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.63 |  | 1801.3547 | -0.2623 | 1806.11 | 1780.9 | 0.0262 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.165 |  | 563.5065 | -0.7704 | 566.18 | 548.47 | 0.059 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.42 |  | 319.9966 | -0.1802 | 322.4 | 317.27 | 4.2201 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 216.29 |  | 215.8417 | 0.2077 | 217.88 | 212.99 | 0.0416 | watch_only | none |
| TER | semiconductor_test_packaging | 369.83 |  | 371.7141 | -0.5069 | 376.78 | 363.37 | 0.4434 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 290.9 |  | 293.5675 | -0.9086 | 301.305 | 293.685 | 0.5122 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.07 |  | 65.1794 | -0.1678 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4331 | -0.3731 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.89 |  | 134.9559 | -0.0489 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.8 |  | 342.4553 | -0.1914 | 347.92 | 341.755 | 4.8128 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 505.89 |  | 507.0517 | -0.2291 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.29 |  | 295.6706 | -0.1287 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.94 |  | 30.0417 | -0.3387 | 31.13 | 29.12 | 0.8684 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.04 |  | 41.5015 | -1.1119 | 43.21 | 40.51 | 0.0487 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.26 |  | 24.0706 | 0.7869 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| SNDK | memory_hbm_storage | 1625.8 |  | 1640.0011 | -0.8659 | 1651.355 | 1560 | 4.1912 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 560.27 |  | 563.6935 | -0.6073 | 576.24 | 556.3 | 0.0589 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 917.66 |  | 922.3162 | -0.5048 | 933.5 | 908.955 | 0.146 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 233.245 |  | 234.2628 | -0.4345 | 238.285 | 235.71 | 0.0086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 604.88 |  | 604.7884 | 0.0151 | 614.15 | 605.39 | 0.1984 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 282.05 |  | 280.015 | 0.7267 | 283 | 276.24 | 0.3581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 169.83 |  | 172.9369 | -1.7965 | 177.88 | 168.18 | 0.2709 | below_vwap | below_vwap |
