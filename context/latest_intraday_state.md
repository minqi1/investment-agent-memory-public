# Intraday State

- Generated at: `2026-07-21T21:35:15+08:00`
- Market time ET: `2026-07-21T09:35:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 42, 'spread_too_wide_or_missing': 9, 'watch_only': 3, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.71 |  | 705.5981 | -0.1259 | 707.09 | 704.52 | 0.0539 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 545.21 |  | 549.0224 | -0.6944 | 550.77 | 545.21 | 0.1431 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.05 |  | 580.0812 | -0.5226 | 582.03 | 577 | 0.0832 | below_vwap | below_vwap |
| SPY | market_regime | 745.56 |  | 745.6809 | -0.0162 | 746.6 | 745.12 | 0.008 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.39 |  | 294.0921 | 0.1013 | 294.39 | 293.25 | 0.0102 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.39 |  | 294.0921 | 0.1013 | 294.39 | 293.25 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.54 |  | 248.0554 | 0.1953 | 248.915 | 247.32 | 0.0443 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 324.97 |  | 323.9483 | 0.3154 | 325.48 | 322.63 | 0.0431 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 23.13 |  | 23.113 | 0.0733 | 23.32 | 22.79 | 0.2594 | watch_only | none |
| 5 | JCI | data_center_power_cooling | 142.15 |  | 142.15 | 0 | 142.15 | 142.15 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MKSI | semiconductor_materials | 338.62 |  | 338.62 | 0 | 338.62 | 338.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | COHU | semiconductor_test_packaging | 54.125 |  | 54.125 | 0 | 54.125 | 54.125 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | HPE | ai_server_oem | 46.33 |  | 46.261 | 0.1493 | 46.64 | 45.835 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ENTG | semiconductor_materials | 142.09 |  | 142.09 | 0 | 142.09 | 142.09 | 4.7787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | LIN | industrial_gases | 512.12 |  | 511.5449 | 0.1124 | 512.83 | 511.12 | 1.3903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SKHY | memory_hbm_storage | 162.29 |  | 162.0573 | 0.1436 | 163.11 | 160.77 | 1.1584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ORCL | cloud_ai_capex | 123.73 |  | 123.4327 | 0.2409 | 124.195 | 122.48 | 3.9198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | MSFT | cloud_ai_capex | 399.42 |  | 397.9804 | 0.3617 | 399.555 | 396.36 | 0.5508 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 206.46 |  | 207.5574 | -0.5287 | 208.61 | 206.32 | 0.0242 | below_vwap | below_vwap |
| 15 | SMH | semiconductor_index | 577.05 |  | 580.0812 | -0.5226 | 582.03 | 577 | 0.0832 | below_vwap | below_vwap |
| 16 | SOXX | semiconductor_index | 545.21 |  | 549.0224 | -0.6944 | 550.77 | 545.21 | 0.1431 | below_vwap | below_vwap |
| 17 | QQQ | market_regime | 704.71 |  | 705.5981 | -0.1259 | 707.09 | 704.52 | 0.0539 | below_vwap | below_vwap |
| 18 | SPY | market_regime | 745.56 |  | 745.6809 | -0.0162 | 746.6 | 745.12 | 0.008 | below_vwap | below_vwap |
| 19 | MU | memory_hbm_storage | 930.87 |  | 931.0635 | -0.0208 | 936.51 | 923 | 0.0902 | below_vwap | below_vwap |
| 20 | TSM | foundry | 415.775 |  | 416.4801 | -0.1693 | 418.76 | 415.025 | 0.178 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.39 |  | 294.0921 | 0.1013 | 294.39 | 293.25 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 142.15 |  | 142.15 | 0 | 142.15 | 142.15 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | ENTG | semiconductor_materials | 142.09 |  | 142.09 | 0 | 142.09 | 142.09 | 4.7787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | MKSI | semiconductor_materials | 338.62 |  | 338.62 | 0 | 338.62 | 338.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | COHU | semiconductor_test_packaging | 54.125 |  | 54.125 | 0 | 54.125 | 54.125 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | AMZN | cloud_ai_capex | 248.54 |  | 248.0554 | 0.1953 | 248.915 | 247.32 | 0.0443 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 23.13 |  | 23.113 | 0.0733 | 23.32 | 22.79 | 0.2594 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 324.97 |  | 323.9483 | 0.3154 | 325.48 | 322.63 | 0.0431 | watch_only | none |
| 9 | ANET | ai_networking_optical | 172.33 |  | 173.2617 | -0.5377 | 174.43 | 172.33 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | TSM | foundry | 415.775 |  | 416.4801 | -0.1693 | 418.76 | 415.025 | 0.178 | below_vwap | below_vwap |
| 11 | NVDA | ai_accelerator | 206.46 |  | 207.5574 | -0.5287 | 208.61 | 206.32 | 0.0242 | below_vwap | below_vwap |
| 12 | SMH | semiconductor_index | 577.05 |  | 580.0812 | -0.5226 | 582.03 | 577 | 0.0832 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 386.55 |  | 387.8889 | -0.3452 | 390.11 | 386.41 | 3.0009 | below_vwap | below_vwap,spread_too_wide |
| 14 | SOXX | semiconductor_index | 545.21 |  | 549.0224 | -0.6944 | 550.77 | 545.21 | 0.1431 | below_vwap | below_vwap |
| 15 | QQQ | market_regime | 704.71 |  | 705.5981 | -0.1259 | 707.09 | 704.52 | 0.0539 | below_vwap | below_vwap |
| 16 | AMD | ai_accelerator | 526.97 |  | 528.4255 | -0.2754 | 532.365 | 524.72 | 1.7003 | below_vwap | below_vwap,spread_too_wide |
| 17 | SPY | market_regime | 745.56 |  | 745.6809 | -0.0162 | 746.6 | 745.12 | 0.008 | below_vwap | below_vwap |
| 18 | MU | memory_hbm_storage | 930.87 |  | 931.0635 | -0.0208 | 936.51 | 923 | 0.0902 | below_vwap | below_vwap |
| 19 | ASML | semiconductor_equipment | 1790.56 |  | 1792.875 | -0.1291 | 1801.43 | 1789.875 | 0.8277 | below_vwap | below_vwap,spread_too_wide |
| 20 | LRCX | semiconductor_equipment | 318.01 |  | 323.9249 | -1.826 | 328.135 | 318.01 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.71 |  | 705.5981 | -0.1259 | 707.09 | 704.52 | 0.0539 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.23 |  | 70.4934 | -0.3737 | 70.84 | 70.1 | 0.0142 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 206.46 |  | 207.5574 | -0.5287 | 208.61 | 206.32 | 0.0242 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 399.42 |  | 397.9804 | 0.3617 | 399.555 | 396.36 | 0.5508 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 324.97 |  | 323.9483 | 0.3154 | 325.48 | 322.63 | 0.0431 | watch_only | none |
| GOOGL | cloud_ai_capex | 349.51 |  | 349.7343 | -0.0641 | 350.985 | 347.69 | 0.9213 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 526.97 |  | 528.4255 | -0.2754 | 532.365 | 524.72 | 1.7003 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.775 |  | 416.4801 | -0.1693 | 418.76 | 415.025 | 0.178 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.21 |  | 549.0224 | -0.6944 | 550.77 | 545.21 | 0.1431 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.05 |  | 580.0812 | -0.5226 | 582.03 | 577 | 0.0832 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 386.55 |  | 387.8889 | -0.3452 | 390.11 | 386.41 | 3.0009 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 930.87 |  | 931.0635 | -0.0208 | 936.51 | 923 | 0.0902 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.11 |  | 206.64 | -0.2565 | 208.37 | 205.31 | 0.6647 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.435 |  | 400.524 | -0.2719 | 403.81 | 397.185 | 4.8343 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.33 |  | 46.261 | 0.1493 | 46.64 | 45.835 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SMCI | ai_server_oem | 24.4 |  | 24.6755 | -1.1164 | 24.77 | 24.385 | 0.123 | below_vwap | below_vwap |
| SPY | market_regime | 745.56 |  | 745.6809 | -0.0162 | 746.6 | 745.12 | 0.008 | below_vwap | below_vwap |
| IWM | market_regime | 294.39 |  | 294.0921 | 0.1013 | 294.39 | 293.25 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 123.73 |  | 123.4327 | 0.2409 | 124.195 | 122.48 | 3.9198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 75.4 |  | 75.6263 | -0.2992 | 76.23 | 74.55 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 301.35 |  | 304.1731 | -0.9281 | 305.09 | 301.35 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 406.78 |  | 408.92 | -0.5233 | 411.01 | 406.78 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.36 |  | 643.8065 | -0.0693 | 645.815 | 641.99 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1120.785 |  | 1130.274 | -0.8395 | 1140.63 | 1117.32 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 473.6 |  | 474.668 | -0.225 | 475.98 | 473.6 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.15 |  | 142.15 | 0 | 142.15 | 142.15 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 172.33 |  | 173.2617 | -0.5377 | 174.43 | 172.33 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 303.89 |  | 306.5903 | -0.8808 | 309.72 | 303 | 1.9843 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 808.16 |  | 816.4362 | -1.0137 | 823.31 | 806.62 | 3.0947 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 397.92 |  | 399.1035 | -0.2965 | 400.77 | 397.245 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 107.95 |  | 108.4796 | -0.4882 | 109.39 | 107.69 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.8 |  | 327.0303 | -0.682 | 329.97 | 324.8 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1790.56 |  | 1792.875 | -0.1291 | 1801.43 | 1789.875 | 0.8277 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 554.25 |  | 559.8344 | -0.9975 | 564.91 | 554.25 | 2.4989 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.01 |  | 323.9249 | -1.826 | 328.135 | 318.01 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.61 |  | 217.2643 | -1.2217 | 220.76 | 214.54 | 2.8843 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 356.825 |  | 361.8523 | -1.3893 | 365.97 | 356.825 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 294.69 |  | 295.6607 | -0.3283 | 296.68 | 294.59 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.375 |  | 65.7222 | -0.5282 | 66.54 | 65.335 | 0.6883 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.125 |  | 54.125 | 0 | 54.125 | 54.125 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 142.09 |  | 142.09 | 0 | 142.09 | 142.09 | 4.7787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 338.62 |  | 338.62 | 0 | 338.62 | 338.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.12 |  | 511.5449 | 0.1124 | 512.83 | 511.12 | 1.3903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 300.585 |  | 301.0238 | -0.1458 | 301.84 | 300.585 | 5.11 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.3 |  | 29.3804 | -0.2737 | 29.735 | 28.785 | 0.2048 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.655 |  | 41.014 | -0.8753 | 41.65 | 40.435 | 0.123 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.13 |  | 23.113 | 0.0733 | 23.32 | 22.79 | 0.2594 | watch_only | none |
| SNDK | memory_hbm_storage | 1495.995 |  | 1501.5246 | -0.3683 | 1517.545 | 1490.29 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 518.94 |  | 526.0989 | -1.3608 | 533.56 | 517.335 | 1.8519 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 848.095 |  | 856.379 | -0.9673 | 866.73 | 846.22 | 0.7145 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 248.54 |  | 248.0554 | 0.1953 | 248.915 | 247.32 | 0.0443 | watch_only | none |
| META | cloud_ai_capex | 645.81 |  | 648.1801 | -0.3657 | 655.425 | 643.68 | 0.7309 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 281.61 |  | 283.5124 | -0.671 | 286.39 | 280.82 | 0.4155 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 162.29 |  | 162.0573 | 0.1436 | 163.11 | 160.77 | 1.1584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
