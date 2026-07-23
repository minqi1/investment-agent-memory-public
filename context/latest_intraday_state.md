# Intraday State

- Generated at: `2026-07-23T23:48:43+08:00`
- Market time ET: `2026-07-23T11:48:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 23, 'below_vwap': 30, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.39 |  | 693.3643 | -0.5732 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545.39 |  | 551.6371 | -1.1325 | 557.38 | 545.965 | 0.0898 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.99 |  | 581.3687 | -0.9252 | 585.98 | 576.635 | 0.0747 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.5 |  | 738.9594 | -0.3328 | 742.515 | 738.54 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 508.43 |  | 507.7353 | 0.1368 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | SNDK | memory_hbm_storage | 1632.88 |  | 1625.3381 | 0.464 | 1651.355 | 1560 | 0.7961 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | IWM | market_regime | 290.9 |  | 291.7205 | -0.2813 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 4 | HPE | ai_server_oem | 47.77 |  | 48.3916 | -1.2846 | 48.88 | 47.635 | 0.0628 | below_vwap | below_vwap |
| 5 | SMCI | ai_server_oem | 31.04 |  | 31.4548 | -1.3188 | 31.52 | 30.23 | 0.0644 | below_vwap | below_vwap |
| 6 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 7 | IREN | high_beta_ai_infrastructure | 41.45 |  | 41.923 | -1.1283 | 43.21 | 40.51 | 0.0483 | below_vwap | below_vwap |
| 8 | TT | data_center_power_cooling | 476.57 |  | 476.6195 | -0.0104 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 143.385 |  | 143.9632 | -0.4016 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 644.23 |  | 653.4123 | -1.4053 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 411.845 |  | 413.256 | -0.3414 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | LRCX | semiconductor_equipment | 318.09 |  | 321.4728 | -1.0523 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | APD | industrial_gases | 296.26 |  | 296.7541 | -0.1665 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | COHR | ai_networking_optical | 312.94 |  | 318.6601 | -1.795 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 367.94 |  | 371.7203 | -1.017 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 53.835 |  | 54.753 | -1.6766 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | TSM | foundry | 413.03 |  | 416.7413 | -0.8906 | 420.72 | 412.69 | 1.3704 | below_vwap | below_vwap,spread_too_wide |
| 18 | MU | memory_hbm_storage | 983.34 |  | 988.4856 | -0.5206 | 999.04 | 964.86 | 0.4749 | below_vwap | below_vwap,spread_too_wide |
| 19 | ASML | semiconductor_equipment | 1793.88 |  | 1804.7868 | -0.6043 | 1806.11 | 1780.9 | 3.1318 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 561.325 |  | 566.4637 | -0.9072 | 566.18 | 548.47 | 1.5695 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 413.03 |  | 416.7413 | -0.8906 | 420.72 | 412.69 | 1.3704 | below_vwap | below_vwap,spread_too_wide |
| 2 | MU | memory_hbm_storage | 983.34 |  | 988.4856 | -0.5206 | 999.04 | 964.86 | 0.4749 | below_vwap | below_vwap,spread_too_wide |
| 3 | ASML | semiconductor_equipment | 1793.88 |  | 1804.7868 | -0.6043 | 1806.11 | 1780.9 | 3.1318 | below_vwap | below_vwap,spread_too_wide |
| 4 | AMAT | semiconductor_equipment | 561.325 |  | 566.4637 | -0.9072 | 566.18 | 548.47 | 1.5695 | below_vwap | below_vwap,spread_too_wide |
| 5 | TT | data_center_power_cooling | 476.57 |  | 476.6195 | -0.0104 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | ANET | ai_networking_optical | 174.26 |  | 176.7462 | -1.4067 | 177.84 | 173.19 | 4.1145 | below_vwap | below_vwap,spread_too_wide |
| 7 | JCI | data_center_power_cooling | 143.385 |  | 143.9632 | -0.4016 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | PWR | data_center_power_cooling | 644.23 |  | 653.4123 | -1.4053 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 213.5 |  | 215.834 | -1.0814 | 217.88 | 212.99 | 1.6956 | below_vwap | below_vwap,spread_too_wide |
| 10 | ETN | data_center_power_cooling | 411.845 |  | 413.256 | -0.3414 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GEV | data_center_power_cooling | 1009.115 |  | 1011.0988 | -0.1962 | 1023.33 | 979.08 | 3.406 | below_vwap | below_vwap,spread_too_wide |
| 12 | IWM | market_regime | 290.9 |  | 291.7205 | -0.2813 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 318.09 |  | 321.4728 | -1.0523 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | WDC | memory_hbm_storage | 560.63 |  | 562.9428 | -0.4108 | 576.24 | 556.3 | 0.7866 | below_vwap | below_vwap,spread_too_wide |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | APD | industrial_gases | 296.26 |  | 296.7541 | -0.1665 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | HPE | ai_server_oem | 47.77 |  | 48.3916 | -1.2846 | 48.88 | 47.635 | 0.0628 | below_vwap | below_vwap |
| 18 | COHR | ai_networking_optical | 312.94 |  | 318.6601 | -1.795 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | CIEN | ai_networking_optical | 404.28 |  | 408.8409 | -1.1156 | 408.58 | 397.9 | 4.2001 | below_vwap | below_vwap,spread_too_wide |
| 20 | TER | semiconductor_test_packaging | 367.94 |  | 371.7203 | -1.017 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.39 |  | 693.3643 | -0.5732 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.56 |  | 66.6116 | -1.5788 | 68.245 | 66.7 | 0.0305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.42 |  | 208.2117 | -0.3802 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 378.265 |  | 383.4008 | -1.3395 | 391.71 | 387.245 | 0.1613 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.78 |  | 321.2582 | -0.1489 | 323.25 | 320.82 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.6 |  | 319.4449 | -0.2645 | 324.42 | 320.24 | 0.0345 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.16 |  | 547.0732 | -1.6293 | 556.12 | 542.33 | 0.8362 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 413.03 |  | 416.7413 | -0.8906 | 420.72 | 412.69 | 1.3704 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.39 |  | 551.6371 | -1.1325 | 557.38 | 545.965 | 0.0898 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.99 |  | 581.3687 | -0.9252 | 585.98 | 576.635 | 0.0747 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 387.77 |  | 393.0588 | -1.3455 | 397.34 | 390.54 | 1.3462 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 983.34 |  | 988.4856 | -0.5206 | 999.04 | 964.86 | 0.4749 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.27 |  | 210.2274 | -1.8824 | 213.785 | 207.665 | 0.6157 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 439.61 |  | 444.0621 | -1.0026 | 450.07 | 438.55 | 2.7547 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.77 |  | 48.3916 | -1.2846 | 48.88 | 47.635 | 0.0628 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.04 |  | 31.4548 | -1.3188 | 31.52 | 30.23 | 0.0644 | below_vwap | below_vwap |
| SPY | market_regime | 736.5 |  | 738.9594 | -0.3328 | 742.515 | 738.54 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.9 |  | 291.7205 | -0.2813 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.035 |  | 122.5496 | -2.0519 | 124.22 | 122.07 | 0.1 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.62 |  | 83.0326 | -1.7013 | 84.415 | 80.64 | 3.6878 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.26 |  | 307.0455 | -1.8843 | 311.13 | 303.96 | 1.9319 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 411.845 |  | 413.256 | -0.3414 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.23 |  | 653.4123 | -1.4053 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1009.115 |  | 1011.0988 | -0.1962 | 1023.33 | 979.08 | 3.406 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.57 |  | 476.6195 | -0.0104 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.385 |  | 143.9632 | -0.4016 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.26 |  | 176.7462 | -1.4067 | 177.84 | 173.19 | 4.1145 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.94 |  | 318.6601 | -1.795 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 824.58 |  | 860.7964 | -4.2073 | 880.26 | 833 | 4.4871 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.28 |  | 408.8409 | -1.1156 | 408.58 | 397.9 | 4.2001 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.79 |  | 114.9403 | -2.7408 | 118.01 | 108.505 | 4.5621 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 323.19 |  | 327.8465 | -1.4203 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.88 |  | 1804.7868 | -0.6043 | 1806.11 | 1780.9 | 3.1318 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 561.325 |  | 566.4637 | -0.9072 | 566.18 | 548.47 | 1.5695 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.09 |  | 321.4728 | -1.0523 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 213.5 |  | 215.834 | -1.0814 | 217.88 | 212.99 | 1.6956 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 367.94 |  | 371.7203 | -1.017 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.79 |  | 295.7863 | -2.0272 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.22 |  | 65.3945 | -1.796 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.835 |  | 54.753 | -1.6766 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.605 |  | 135.4732 | -1.379 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 337.64 |  | 344.1402 | -1.8888 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 508.43 |  | 507.7353 | 0.1368 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.26 |  | 296.7541 | -0.1665 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.81 |  | 30.0838 | -0.9102 | 31.13 | 29.12 | 0.3019 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.45 |  | 41.923 | -1.1283 | 43.21 | 40.51 | 0.0483 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.98 |  | 24.0551 | -0.3123 | 24.46 | 23.265 | 0.1668 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1632.88 |  | 1625.3381 | 0.464 | 1651.355 | 1560 | 0.7961 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 560.63 |  | 562.9428 | -0.4108 | 576.24 | 556.3 | 0.7866 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.03 |  | 923.5053 | -0.4846 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.64 |  | 234.4153 | -0.7573 | 238.285 | 235.71 | 0.0387 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 597.92 |  | 604.4382 | -1.0784 | 614.15 | 605.39 | 1.3831 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 275.75 |  | 279.1308 | -1.2112 | 283 | 276.24 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 169.825 |  | 173.6358 | -2.1947 | 177.88 | 168.18 | 1.0952 | below_vwap | below_vwap,spread_too_wide |
