# Intraday State

- Generated at: `2026-07-23T23:56:46+08:00`
- Market time ET: `2026-07-23T11:56:47-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 20, 'below_vwap': 29, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.02 |  | 693.2121 | -0.3162 | 698.65 | 693.24 | 0.0174 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.92 |  | 551.2767 | -0.6089 | 557.38 | 545.965 | 0.0858 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.17 |  | 581.3285 | -0.5433 | 585.98 | 576.635 | 0.0778 | below_vwap | below_vwap |
| SPY | market_regime | 737.375 |  | 738.9018 | -0.2066 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IREN | high_beta_ai_infrastructure | 41.95 |  | 41.902 | 0.1145 | 43.21 | 40.51 | 0.0477 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.06 |  | 476.6265 | 0.0909 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | CORZ | high_beta_ai_infrastructure | 24.135 |  | 24.0553 | 0.3313 | 24.46 | 23.265 | 0.1243 | watch_only | none |
| 4 | MU | memory_hbm_storage | 990.62 |  | 988.4539 | 0.2191 | 999.04 | 964.86 | 0.8833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GEV | data_center_power_cooling | 1011.72 |  | 1011.1002 | 0.0613 | 1023.33 | 979.08 | 2.4552 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GOOGL | cloud_ai_capex | 319.93 |  | 319.4427 | 0.1526 | 324.42 | 320.24 | 0.0406 | below_opening_15m_low | below_opening_15m_low |
| 7 | SMH | semiconductor_index | 578.17 |  | 581.3285 | -0.5433 | 585.98 | 576.635 | 0.0778 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 547.92 |  | 551.2767 | -0.6089 | 557.38 | 545.965 | 0.0858 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 291.45 |  | 291.7162 | -0.0913 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 10 | LIN | industrial_gases | 507.06 |  | 507.7293 | -0.1318 | 510.71 | 502.72 | 0.0454 | below_vwap | below_vwap |
| 11 | HPE | ai_server_oem | 47.89 |  | 48.362 | -0.976 | 48.88 | 47.635 | 0.1462 | below_vwap | below_vwap |
| 12 | SMCI | ai_server_oem | 31.175 |  | 31.4411 | -0.8462 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | SNDK | memory_hbm_storage | 1643.94 |  | 1625.6609 | 1.1244 | 1651.355 | 1560 | 2.129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 406.01 |  | 408.4361 | -0.594 | 408.58 | 397.9 | 0.1847 | below_vwap | below_vwap |
| 16 | ANET | ai_networking_optical | 174.85 |  | 176.673 | -1.0319 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 143.63 |  | 143.9547 | -0.2256 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 646.71 |  | 653.207 | -0.9946 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 319.61 |  | 321.4356 | -0.568 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 277.4 |  | 279.0505 | -0.5915 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IREN | high_beta_ai_infrastructure | 41.95 |  | 41.902 | 0.1145 | 43.21 | 40.51 | 0.0477 | watch_only | none |
| 2 | CORZ | high_beta_ai_infrastructure | 24.135 |  | 24.0553 | 0.3313 | 24.46 | 23.265 | 0.1243 | watch_only | none |
| 3 | TSM | foundry | 414.85 |  | 416.6251 | -0.4261 | 420.72 | 412.69 | 1.1088 | below_vwap | below_vwap,spread_too_wide |
| 4 | SMH | semiconductor_index | 578.17 |  | 581.3285 | -0.5433 | 585.98 | 576.635 | 0.0778 | below_vwap | below_vwap |
| 5 | SOXX | semiconductor_index | 547.92 |  | 551.2767 | -0.6089 | 557.38 | 545.965 | 0.0858 | below_vwap | below_vwap |
| 6 | ASML | semiconductor_equipment | 1796.495 |  | 1804.014 | -0.4168 | 1806.11 | 1780.9 | 4.0484 | below_vwap | below_vwap,spread_too_wide |
| 7 | AMAT | semiconductor_equipment | 564.46 |  | 566.3736 | -0.3379 | 566.18 | 548.47 | 0.9159 | below_vwap | below_vwap,spread_too_wide |
| 8 | ANET | ai_networking_optical | 174.85 |  | 176.673 | -1.0319 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 143.63 |  | 143.9547 | -0.2256 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 646.71 |  | 653.207 | -0.9946 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 214.58 |  | 215.7414 | -0.5383 | 217.88 | 212.99 | 2.9313 | below_vwap | below_vwap,spread_too_wide |
| 12 | ETN | data_center_power_cooling | 413 |  | 413.2217 | -0.0536 | 415.53 | 406.545 | 0.8232 | below_vwap | below_vwap,spread_too_wide |
| 13 | IWM | market_regime | 291.45 |  | 291.7162 | -0.0913 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 14 | LRCX | semiconductor_equipment | 319.61 |  | 321.4356 | -0.568 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ARM | ai_accelerator | 277.4 |  | 279.0505 | -0.5915 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 562.83 |  | 562.925 | -0.0169 | 576.24 | 556.3 | 0.5952 | below_vwap | below_vwap,spread_too_wide |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 507.06 |  | 507.7293 | -0.1318 | 510.71 | 502.72 | 0.0454 | below_vwap | below_vwap |
| 19 | HPE | ai_server_oem | 47.89 |  | 48.362 | -0.976 | 48.88 | 47.635 | 0.1462 | below_vwap | below_vwap |
| 20 | COHR | ai_networking_optical | 315.52 |  | 318.6015 | -0.9672 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.02 |  | 693.2121 | -0.3162 | 698.65 | 693.24 | 0.0174 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.98 |  | 66.5771 | -0.8969 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.12 |  | 208.1955 | -0.0362 | 210.85 | 208.49 | 0.3411 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.445 |  | 383.2229 | -0.9858 | 391.71 | 387.245 | 0.0237 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.64 |  | 321.2351 | -0.1853 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.93 |  | 319.4427 | 0.1526 | 324.42 | 320.24 | 0.0406 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 540.09 |  | 546.8646 | -1.2388 | 556.12 | 542.33 | 0.7925 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.85 |  | 416.6251 | -0.4261 | 420.72 | 412.69 | 1.1088 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.92 |  | 551.2767 | -0.6089 | 557.38 | 545.965 | 0.0858 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.17 |  | 581.3285 | -0.5433 | 585.98 | 576.635 | 0.0778 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 388.63 |  | 393.0014 | -1.1123 | 397.34 | 390.54 | 1.3432 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 990.62 |  | 988.4539 | 0.2191 | 999.04 | 964.86 | 0.8833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.04 |  | 210.1828 | -1.4953 | 213.785 | 207.665 | 1.0626 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 442.385 |  | 443.9647 | -0.3558 | 450.07 | 438.55 | 2.0525 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.89 |  | 48.362 | -0.976 | 48.88 | 47.635 | 0.1462 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.175 |  | 31.4411 | -0.8462 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 737.375 |  | 738.9018 | -0.2066 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.45 |  | 291.7162 | -0.0913 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.55 |  | 122.4443 | -1.547 | 124.22 | 122.07 | 3.3181 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.405 |  | 82.9967 | -0.7129 | 84.415 | 80.64 | 2.876 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.35 |  | 306.9119 | -1.4864 | 311.13 | 303.96 | 1.9679 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413 |  | 413.2217 | -0.0536 | 415.53 | 406.545 | 0.8232 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 646.71 |  | 653.207 | -0.9946 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1011.72 |  | 1011.1002 | 0.0613 | 1023.33 | 979.08 | 2.4552 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.06 |  | 476.6265 | 0.0909 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.63 |  | 143.9547 | -0.2256 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.85 |  | 176.673 | -1.0319 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.52 |  | 318.6015 | -0.9672 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 833.52 |  | 860.6042 | -3.1471 | 880.26 | 833 | 4.439 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 406.01 |  | 408.4361 | -0.594 | 408.58 | 397.9 | 0.1847 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 113.41 |  | 114.869 | -1.2701 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.93 |  | 327.7973 | -0.8747 | 341.68 | 327.43 | 4.364 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1796.495 |  | 1804.014 | -0.4168 | 1806.11 | 1780.9 | 4.0484 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 564.46 |  | 566.3736 | -0.3379 | 566.18 | 548.47 | 0.9159 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.61 |  | 321.4356 | -0.568 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.58 |  | 215.7414 | -0.5383 | 217.88 | 212.99 | 2.9313 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.67 |  | 371.6279 | -0.2578 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.585 |  | 295.773 | -1.416 | 301.305 | 293.685 | 4.5819 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.42 |  | 65.3739 | -1.4592 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.03 |  | 54.6522 | -1.1385 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.39 |  | 135.4268 | -0.7656 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.775 |  | 342.9817 | -0.935 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.06 |  | 507.7293 | -0.1318 | 510.71 | 502.72 | 0.0454 | below_vwap | below_vwap |
| APD | industrial_gases | 295.585 |  | 296.6419 | -0.3563 | 299.26 | 295.795 | 0.2233 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.005 |  | 30.0802 | -0.25 | 31.13 | 29.12 | 0.0667 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.95 |  | 41.902 | 0.1145 | 43.21 | 40.51 | 0.0477 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 24.135 |  | 24.0553 | 0.3313 | 24.46 | 23.265 | 0.1243 | watch_only | none |
| SNDK | memory_hbm_storage | 1643.94 |  | 1625.6609 | 1.1244 | 1651.355 | 1560 | 2.129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 562.83 |  | 562.925 | -0.0169 | 576.24 | 556.3 | 0.5952 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 923.06 |  | 923.4771 | -0.0452 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.88 |  | 234.356 | -0.6298 | 238.285 | 235.71 | 0.1632 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 600.88 |  | 604.0135 | -0.5188 | 614.15 | 605.39 | 0.7489 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 277.4 |  | 279.0505 | -0.5915 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.28 |  | 173.5818 | -0.7499 | 177.88 | 168.18 | 0.3773 | below_vwap | below_vwap,spread_too_wide |
