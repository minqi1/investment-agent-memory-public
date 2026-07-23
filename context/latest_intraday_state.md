# Intraday State

- Generated at: `2026-07-24T03:37:34+08:00`
- Market time ET: `2026-07-23T15:37:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'below_vwap': 28, 'price_stale_or_missing': 1, 'watch_only': 4, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.49 |  | 692.6746 | -0.3154 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.17 |  | 550.5628 | -0.4346 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.925 |  | 580.3038 | -0.4099 | 585.98 | 576.635 | 0.0519 | below_vwap | below_vwap |
| SPY | market_regime | 737.03 |  | 738.4067 | -0.1864 | 742.515 | 738.54 | 0.0176 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 291.715 |  | 291.6102 | 0.0359 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 2 | KLAC | semiconductor_equipment | 216.8 |  | 215.8023 | 0.4623 | 217.88 | 212.99 | 0.0461 | watch_only | none |
| 3 | PWR | data_center_power_cooling | 650.94 |  | 650.7153 | 0.0345 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ETN | data_center_power_cooling | 413.89 |  | 413.3758 | 0.1244 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ARM | ai_accelerator | 282.75 |  | 279.9019 | 1.0176 | 283 | 276.24 | 0.145 | watch_only | none |
| 6 | CORZ | high_beta_ai_infrastructure | 24.2 |  | 24.0689 | 0.5445 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| 7 | TT | data_center_power_cooling | 479.66 |  | 477.032 | 0.5509 | 480 | 472.33 | 5.064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ENTG | semiconductor_materials | 134.98 |  | 134.9554 | 0.0182 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 9 | SMH | semiconductor_index | 577.925 |  | 580.3038 | -0.4099 | 585.98 | 576.635 | 0.0519 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 548.17 |  | 550.5628 | -0.4346 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 390.93 |  | 391.8987 | -0.2472 | 397.34 | 390.54 | 0.1279 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1798.8 |  | 1801.3946 | -0.144 | 1806.11 | 1780.9 | 0.0595 | below_vwap | below_vwap |
| 13 | HPE | ai_server_oem | 47.65 |  | 48.1928 | -1.1262 | 48.88 | 47.635 | 0.1049 | below_vwap | below_vwap |
| 14 | COHR | ai_networking_optical | 312.09 |  | 316.7 | -1.4556 | 320.13 | 307.04 | 0.1057 | below_vwap | below_vwap |
| 15 | SKHY | memory_hbm_storage | 170.005 |  | 172.9667 | -1.7123 | 177.88 | 168.18 | 0.0647 | below_vwap | below_vwap |
| 16 | SNDK | memory_hbm_storage | 1625.185 |  | 1640.1841 | -0.9145 | 1651.355 | 1560 | 0.1077 | below_vwap | below_vwap |
| 17 | SMCI | ai_server_oem | 31.365 |  | 31.5617 | -0.6231 | 31.52 | 30.23 | 0.0319 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | IREN | high_beta_ai_infrastructure | 41.2 |  | 41.5067 | -0.7389 | 43.21 | 40.51 | 0.0485 | below_vwap | below_vwap |
| 20 | MU | memory_hbm_storage | 988.53 |  | 990.7604 | -0.2251 | 999.04 | 964.86 | 0.1912 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1040.99 |  | 1018.2184 | 2.2364 | 1023.33 | 979.08 | 1.6042 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | KLAC | semiconductor_equipment | 216.8 |  | 215.8023 | 0.4623 | 217.88 | 212.99 | 0.0461 | watch_only | none |
| 3 | IWM | market_regime | 291.715 |  | 291.6102 | 0.0359 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 4 | ARM | ai_accelerator | 282.75 |  | 279.9019 | 1.0176 | 283 | 276.24 | 0.145 | watch_only | none |
| 5 | CORZ | high_beta_ai_infrastructure | 24.2 |  | 24.0689 | 0.5445 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| 6 | TSM | foundry | 414.705 |  | 416.2309 | -0.3666 | 420.72 | 412.69 | 0.8102 | below_vwap | below_vwap,spread_too_wide |
| 7 | SMH | semiconductor_index | 577.925 |  | 580.3038 | -0.4099 | 585.98 | 576.635 | 0.0519 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 548.17 |  | 550.5628 | -0.4346 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| 9 | AVGO | custom_silicon_networking | 390.93 |  | 391.8987 | -0.2472 | 397.34 | 390.54 | 0.1279 | below_vwap | below_vwap |
| 10 | MU | memory_hbm_storage | 988.53 |  | 990.7604 | -0.2251 | 999.04 | 964.86 | 0.1912 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1798.8 |  | 1801.3946 | -0.144 | 1806.11 | 1780.9 | 0.0595 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 559.455 |  | 563.6125 | -0.7376 | 566.18 | 548.47 | 0.2127 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 176.19 |  | 176.5716 | -0.2161 | 177.84 | 173.19 | 3.1216 | below_vwap | below_vwap,spread_too_wide |
| 14 | JCI | data_center_power_cooling | 143.54 |  | 143.7835 | -0.1694 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | VRT | data_center_power_cooling | 304.29 |  | 305.6587 | -0.4478 | 311.13 | 303.96 | 1.4789 | below_vwap | below_vwap,spread_too_wide |
| 16 | LRCX | semiconductor_equipment | 319.56 |  | 320.0049 | -0.139 | 322.4 | 317.27 | 4.115 | below_vwap | below_vwap,spread_too_wide |
| 17 | WDC | memory_hbm_storage | 560.16 |  | 563.7337 | -0.6339 | 576.24 | 556.3 | 1.8941 | below_vwap | below_vwap,spread_too_wide |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 505.53 |  | 507.0783 | -0.3053 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | HPE | ai_server_oem | 47.65 |  | 48.1928 | -1.1262 | 48.88 | 47.635 | 0.1049 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.49 |  | 692.6746 | -0.3154 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.89 |  | 66.4732 | -0.8773 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.59 |  | 208.4733 | -0.4237 | 210.85 | 208.49 | 0.0482 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.9 |  | 382.3821 | -0.3876 | 391.71 | 387.245 | 0.0263 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.32 |  | 320.9158 | -0.1856 | 323.25 | 320.82 | 0.0062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 317.845 |  | 319.449 | -0.5021 | 324.42 | 320.24 | 0.4877 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 539.5 |  | 539.8659 | -0.0678 | 556.12 | 542.33 | 1.7609 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.705 |  | 416.2309 | -0.3666 | 420.72 | 412.69 | 0.8102 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.17 |  | 550.5628 | -0.4346 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.925 |  | 580.3038 | -0.4099 | 585.98 | 576.635 | 0.0519 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.93 |  | 391.8987 | -0.2472 | 397.34 | 390.54 | 0.1279 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 988.53 |  | 990.7604 | -0.2251 | 999.04 | 964.86 | 0.1912 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 207.5 |  | 209.1537 | -0.7907 | 213.785 | 207.665 | 0.2458 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.91 |  | 443.0565 | -1.1616 | 450.07 | 438.55 | 1.4044 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.65 |  | 48.1928 | -1.1262 | 48.88 | 47.635 | 0.1049 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.365 |  | 31.5617 | -0.6231 | 31.52 | 30.23 | 0.0319 | below_vwap | below_vwap |
| SPY | market_regime | 737.03 |  | 738.4067 | -0.1864 | 742.515 | 738.54 | 0.0176 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.715 |  | 291.6102 | 0.0359 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 120.145 |  | 121.6277 | -1.219 | 124.22 | 122.07 | 0.025 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.34 |  | 82.4203 | -1.3107 | 84.415 | 80.64 | 3.7251 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.29 |  | 305.6587 | -0.4478 | 311.13 | 303.96 | 1.4789 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.89 |  | 413.3758 | 0.1244 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.94 |  | 650.7153 | 0.0345 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1040.99 |  | 1018.2184 | 2.2364 | 1023.33 | 979.08 | 1.6042 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 479.66 |  | 477.032 | 0.5509 | 480 | 472.33 | 5.064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 143.54 |  | 143.7835 | -0.1694 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.19 |  | 176.5716 | -0.2161 | 177.84 | 173.19 | 3.1216 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.09 |  | 316.7 | -1.4556 | 320.13 | 307.04 | 0.1057 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 833.04 |  | 853.8941 | -2.4422 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 405.145 |  | 407.5996 | -0.6022 | 408.58 | 397.9 | 4.9908 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.92 |  | 114.3033 | -2.0851 | 118.01 | 108.505 | 4.5658 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 323.24 |  | 326.1622 | -0.8959 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1798.8 |  | 1801.3946 | -0.144 | 1806.11 | 1780.9 | 0.0595 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.455 |  | 563.6125 | -0.7376 | 566.18 | 548.47 | 0.2127 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.56 |  | 320.0049 | -0.139 | 322.4 | 317.27 | 4.115 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 216.8 |  | 215.8023 | 0.4623 | 217.88 | 212.99 | 0.0461 | watch_only | none |
| TER | semiconductor_test_packaging | 370.23 |  | 371.7341 | -0.4046 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.43 |  | 293.5854 | -1.0748 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.995 |  | 65.1812 | -0.2856 | 67.455 | 65.81 | 4.1542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4331 | -0.3731 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.98 |  | 134.9554 | 0.0182 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| MKSI | semiconductor_materials | 341.71 |  | 342.4799 | -0.2248 | 347.92 | 341.755 | 0.3746 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 505.53 |  | 507.0783 | -0.3053 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.34 |  | 295.6811 | -0.1153 | 299.26 | 295.795 | 0.0508 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 29.945 |  | 30.0421 | -0.3234 | 31.13 | 29.12 | 0.1002 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.2 |  | 41.5067 | -0.7389 | 43.21 | 40.51 | 0.0485 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.2 |  | 24.0689 | 0.5445 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| SNDK | memory_hbm_storage | 1625.185 |  | 1640.1841 | -0.9145 | 1651.355 | 1560 | 0.1077 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 560.16 |  | 563.7337 | -0.6339 | 576.24 | 556.3 | 1.8941 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 915.945 |  | 922.4633 | -0.7066 | 933.5 | 908.955 | 1.3953 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.31 |  | 234.2704 | -0.4099 | 238.285 | 235.71 | 0.0129 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 604.965 |  | 604.7855 | 0.0297 | 614.15 | 605.39 | 0.7967 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 282.75 |  | 279.9019 | 1.0176 | 283 | 276.24 | 0.145 | watch_only | none |
| SKHY | memory_hbm_storage | 170.005 |  | 172.9667 | -1.7123 | 177.88 | 168.18 | 0.0647 | below_vwap | below_vwap |
