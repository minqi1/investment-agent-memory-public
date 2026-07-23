# Intraday State

- Generated at: `2026-07-24T00:01:56+08:00`
- Market time ET: `2026-07-23T12:01:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 18, 'below_vwap': 31, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.505 |  | 693.1539 | -0.2379 | 698.65 | 693.24 | 0.0275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549 |  | 551.1436 | -0.3889 | 557.38 | 545.965 | 0.071 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.75 |  | 581.2836 | -0.4359 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| SPY | market_regime | 737.885 |  | 738.8582 | -0.1317 | 742.515 | 738.54 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1012.97 |  | 1011.1865 | 0.1764 | 1023.33 | 979.08 | 0.0977 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.6 |  | 476.643 | 0.2008 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | WDC | memory_hbm_storage | 562.97 |  | 562.9179 | 0.0093 | 576.24 | 556.3 | 1.4068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | DELL | ai_server_oem | 443.99 |  | 443.9546 | 0.008 | 450.07 | 438.55 | 1.6104 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | MU | memory_hbm_storage | 992.595 |  | 988.5015 | 0.4141 | 999.04 | 964.86 | 1.2049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GOOGL | cloud_ai_capex | 319.995 |  | 319.4501 | 0.1706 | 324.42 | 320.24 | 0.0875 | below_opening_15m_low | below_opening_15m_low |
| 7 | SMH | semiconductor_index | 578.75 |  | 581.2836 | -0.4359 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 549 |  | 551.1436 | -0.3889 | 557.38 | 545.965 | 0.071 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 291.425 |  | 291.7105 | -0.0979 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 10 | NVDA | ai_accelerator | 208.23 |  | 208.1929 | 0.0178 | 210.85 | 208.49 | 0.5331 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 11 | SMCI | ai_server_oem | 31.29 |  | 31.4356 | -0.4631 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | IREN | high_beta_ai_infrastructure | 41.42 |  | 41.8992 | -1.1437 | 43.21 | 40.51 | 0.0724 | below_vwap | below_vwap |
| 14 | AAPL | mega_cap_platform | 320.96 |  | 321.2298 | -0.084 | 323.25 | 320.82 | 0.0249 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1650 |  | 1626.0264 | 1.4744 | 1651.355 | 1560 | 3.8788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ARM | ai_accelerator | 278.04 |  | 278.9962 | -0.3427 | 283 | 276.24 | 0.1906 | below_vwap | below_vwap |
| 17 | CIEN | ai_networking_optical | 404.03 |  | 408.1403 | -1.0071 | 408.58 | 397.9 | 0.2054 | below_vwap | below_vwap |
| 18 | ANET | ai_networking_optical | 174.88 |  | 176.6667 | -1.0114 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 143.865 |  | 143.949 | -0.0583 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 646.785 |  | 653.069 | -0.9622 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1012.97 |  | 1011.1865 | 0.1764 | 1023.33 | 979.08 | 0.0977 | watch_only | none |
| 2 | TSM | foundry | 415.13 |  | 416.5598 | -0.3432 | 420.72 | 412.69 | 2.168 | below_vwap | below_vwap,spread_too_wide |
| 3 | SMH | semiconductor_index | 578.75 |  | 581.2836 | -0.4359 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| 4 | SOXX | semiconductor_index | 549 |  | 551.1436 | -0.3889 | 557.38 | 545.965 | 0.071 | below_vwap | below_vwap |
| 5 | ASML | semiconductor_equipment | 1799.585 |  | 1803.9439 | -0.2416 | 1806.11 | 1780.9 | 3.8959 | below_vwap | below_vwap,spread_too_wide |
| 6 | AMAT | semiconductor_equipment | 565 |  | 566.3489 | -0.2382 | 566.18 | 548.47 | 1.2619 | below_vwap | below_vwap,spread_too_wide |
| 7 | ANET | ai_networking_optical | 174.88 |  | 176.6667 | -1.0114 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 143.865 |  | 143.949 | -0.0583 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | PWR | data_center_power_cooling | 646.785 |  | 653.069 | -0.9622 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | KLAC | semiconductor_equipment | 215 |  | 215.73 | -0.3384 | 217.88 | 212.99 | 2.2047 | below_vwap | below_vwap,spread_too_wide |
| 11 | ETN | data_center_power_cooling | 413.01 |  | 413.2179 | -0.0503 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IWM | market_regime | 291.425 |  | 291.7105 | -0.0979 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 319.45 |  | 321.4018 | -0.6073 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ARM | ai_accelerator | 278.04 |  | 278.9962 | -0.3427 | 283 | 276.24 | 0.1906 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LIN | industrial_gases | 507.06 |  | 507.7293 | -0.1318 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | HPE | ai_server_oem | 48.05 |  | 48.3459 | -0.612 | 48.88 | 47.635 | 4.3913 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 315.495 |  | 318.5313 | -0.9532 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | CIEN | ai_networking_optical | 404.03 |  | 408.1403 | -1.0071 | 408.58 | 397.9 | 0.2054 | below_vwap | below_vwap |
| 20 | MRVL | custom_silicon_networking | 207.97 |  | 210.0841 | -1.0063 | 213.785 | 207.665 | 1.0146 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.505 |  | 693.1539 | -0.2379 | 698.65 | 693.24 | 0.0275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.21 |  | 66.5694 | -0.54 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.23 |  | 208.1929 | 0.0178 | 210.85 | 208.49 | 0.5331 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MSFT | cloud_ai_capex | 379.845 |  | 383.1746 | -0.869 | 391.71 | 387.245 | 2.2325 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.96 |  | 321.2298 | -0.084 | 323.25 | 320.82 | 0.0249 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 319.995 |  | 319.4501 | 0.1706 | 324.42 | 320.24 | 0.0875 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 541.875 |  | 546.7603 | -0.8935 | 556.12 | 542.33 | 1.0131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.13 |  | 416.5598 | -0.3432 | 420.72 | 412.69 | 2.168 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549 |  | 551.1436 | -0.3889 | 557.38 | 545.965 | 0.071 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.75 |  | 581.2836 | -0.4359 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 389.14 |  | 392.921 | -0.9623 | 397.34 | 390.54 | 1.087 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.595 |  | 988.5015 | 0.4141 | 999.04 | 964.86 | 1.2049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.97 |  | 210.0841 | -1.0063 | 213.785 | 207.665 | 1.0146 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.99 |  | 443.9546 | 0.008 | 450.07 | 438.55 | 1.6104 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.05 |  | 48.3459 | -0.612 | 48.88 | 47.635 | 4.3913 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 31.29 |  | 31.4356 | -0.4631 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| SPY | market_regime | 737.885 |  | 738.8582 | -0.1317 | 742.515 | 738.54 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.425 |  | 291.7105 | -0.0979 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.66 |  | 122.3885 | -1.4123 | 124.22 | 122.07 | 0.1492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.08 |  | 82.9768 | -1.0807 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.645 |  | 306.8778 | -1.3793 | 311.13 | 303.96 | 1.5431 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.01 |  | 413.2179 | -0.0503 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 646.785 |  | 653.069 | -0.9622 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1012.97 |  | 1011.1865 | 0.1764 | 1023.33 | 979.08 | 0.0977 | watch_only | none |
| TT | data_center_power_cooling | 477.6 |  | 476.643 | 0.2008 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.865 |  | 143.949 | -0.0583 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.88 |  | 176.6667 | -1.0114 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.495 |  | 318.5313 | -0.9532 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.43 |  | 860.1386 | -2.8726 | 880.26 | 833 | 4.4289 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.03 |  | 408.1403 | -1.0071 | 408.58 | 397.9 | 0.2054 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 113.06 |  | 114.8418 | -1.5516 | 118.01 | 108.505 | 4.8204 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 326.065 |  | 327.7743 | -0.5215 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1799.585 |  | 1803.9439 | -0.2416 | 1806.11 | 1780.9 | 3.8959 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 565 |  | 566.3489 | -0.2382 | 566.18 | 548.47 | 1.2619 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.45 |  | 321.4018 | -0.6073 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215 |  | 215.73 | -0.3384 | 217.88 | 212.99 | 2.2047 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.46 |  | 371.6168 | -0.0422 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.67 |  | 295.7599 | -1.3828 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.675 |  | 65.3451 | -1.0254 | 67.455 | 65.81 | 4.6386 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.1 |  | 54.6181 | -0.9486 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.39 |  | 135.4268 | -0.7656 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.535 |  | 342.9146 | -0.6939 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.06 |  | 507.7293 | -0.1318 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.36 |  | 296.552 | -0.402 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.82 |  | 30.0776 | -0.8564 | 31.13 | 29.12 | 0.7378 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.42 |  | 41.8992 | -1.1437 | 43.21 | 40.51 | 0.0724 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.04 |  | 24.0565 | -0.0688 | 24.46 | 23.265 | 0.1248 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1650 |  | 1626.0264 | 1.4744 | 1651.355 | 1560 | 3.8788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 562.97 |  | 562.9179 | 0.0093 | 576.24 | 556.3 | 1.4068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 922.58 |  | 923.4405 | -0.0932 | 933.5 | 908.955 | 0.8769 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.71 |  | 234.3406 | -0.2691 | 238.285 | 235.71 | 0.0342 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.37 |  | 603.936 | -0.4249 | 614.15 | 605.39 | 0.8314 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 278.04 |  | 278.9962 | -0.3427 | 283 | 276.24 | 0.1906 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 172.86 |  | 173.5697 | -0.4089 | 177.88 | 168.18 | 1.4058 | below_vwap | below_vwap,spread_too_wide |
