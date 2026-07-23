# Intraday State

- Generated at: `2026-07-23T23:17:16+08:00`
- Market time ET: `2026-07-23T11:17:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 21, 'watch_only': 1, 'below_vwap': 31, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.61 |  | 694.3348 | -0.6805 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.52 |  | 553.1167 | -1.1926 | 557.38 | 545.965 | 0.1244 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.09 |  | 582.1224 | -1.0363 | 585.98 | 576.635 | 0.0746 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.88 |  | 739.6316 | -0.372 | 742.515 | 738.54 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.93 |  | 321.2678 | 0.2061 | 323.25 | 320.82 | 0.1149 | watch_only | none |
| 2 | LIN | industrial_gases | 508.62 |  | 507.6287 | 0.1953 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | SOXX | semiconductor_index | 546.52 |  | 553.1167 | -1.1926 | 557.38 | 545.965 | 0.1244 | below_vwap | below_vwap |
| 4 | KLAC | semiconductor_equipment | 214.71 |  | 216.0735 | -0.6311 | 217.88 | 212.99 | 0.1258 | below_vwap | below_vwap |
| 5 | IWM | market_regime | 291.1 |  | 291.8836 | -0.2685 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 6 | WDC | memory_hbm_storage | 557.545 |  | 563.0441 | -0.9767 | 576.24 | 556.3 | 0.104 | below_vwap | below_vwap |
| 7 | SMCI | ai_server_oem | 31.12 |  | 31.5117 | -1.243 | 31.52 | 30.23 | 0.0643 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | IREN | high_beta_ai_infrastructure | 41.195 |  | 42.1472 | -2.2592 | 43.21 | 40.51 | 0.0728 | below_vwap | below_vwap |
| 10 | TT | data_center_power_cooling | 475.54 |  | 476.7394 | -0.2516 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 143.55 |  | 144.0409 | -0.3408 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 646.01 |  | 654.425 | -1.2859 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1004.15 |  | 1011.8752 | -0.7635 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LRCX | semiconductor_equipment | 318.89 |  | 321.8234 | -0.9115 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | APD | industrial_gases | 296.83 |  | 296.9037 | -0.0248 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHR | ai_networking_optical | 312.03 |  | 319.5009 | -2.3383 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | TER | semiconductor_test_packaging | 368.805 |  | 372.6765 | -1.0388 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | CRWV | gpu_cloud_ai_factory | 81.28 |  | 83.2829 | -2.405 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | AAOI | ai_networking_optical | 111.78 |  | 115.5229 | -3.2399 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | TSM | foundry | 413.65 |  | 417.4626 | -0.9133 | 420.72 | 412.69 | 1.2595 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.93 |  | 321.2678 | 0.2061 | 323.25 | 320.82 | 0.1149 | watch_only | none |
| 2 | TSM | foundry | 413.65 |  | 417.4626 | -0.9133 | 420.72 | 412.69 | 1.2595 | below_vwap | below_vwap,spread_too_wide |
| 3 | SOXX | semiconductor_index | 546.52 |  | 553.1167 | -1.1926 | 557.38 | 545.965 | 0.1244 | below_vwap | below_vwap |
| 4 | MU | memory_hbm_storage | 984.475 |  | 989.2229 | -0.48 | 999.04 | 964.86 | 0.8126 | below_vwap | below_vwap,spread_too_wide |
| 5 | ASML | semiconductor_equipment | 1796.91 |  | 1806.0894 | -0.5082 | 1806.11 | 1780.9 | 0.5726 | below_vwap | below_vwap,spread_too_wide |
| 6 | AMAT | semiconductor_equipment | 563.615 |  | 567.0577 | -0.6071 | 566.18 | 548.47 | 2.468 | below_vwap | below_vwap,spread_too_wide |
| 7 | TT | data_center_power_cooling | 475.54 |  | 476.7394 | -0.2516 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | ANET | ai_networking_optical | 174.36 |  | 176.9589 | -1.4687 | 177.84 | 173.19 | 4.2957 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 143.55 |  | 144.0409 | -0.3408 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 646.01 |  | 654.425 | -1.2859 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 214.71 |  | 216.0735 | -0.6311 | 217.88 | 212.99 | 0.1258 | below_vwap | below_vwap |
| 12 | ETN | data_center_power_cooling | 411.57 |  | 413.5678 | -0.4831 | 415.53 | 406.545 | 3.3166 | below_vwap | below_vwap,spread_too_wide |
| 13 | GEV | data_center_power_cooling | 1004.15 |  | 1011.8752 | -0.7635 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IWM | market_regime | 291.1 |  | 291.8836 | -0.2685 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 318.89 |  | 321.8234 | -0.9115 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 557.545 |  | 563.0441 | -0.9767 | 576.24 | 556.3 | 0.104 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | APD | industrial_gases | 296.83 |  | 296.9037 | -0.0248 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | HPE | ai_server_oem | 48.12 |  | 48.5357 | -0.8564 | 48.88 | 47.635 | 1.7872 | below_vwap | below_vwap,spread_too_wide |
| 20 | COHR | ai_networking_optical | 312.03 |  | 319.5009 | -2.3383 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.61 |  | 694.3348 | -0.6805 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.63 |  | 66.8873 | -1.8797 | 68.245 | 66.7 | 0.0305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.645 |  | 208.5206 | -0.8995 | 210.85 | 208.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.33 |  | 384.5008 | -1.3448 | 391.71 | 387.245 | 0.9438 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 321.93 |  | 321.2678 | 0.2061 | 323.25 | 320.82 | 0.1149 | watch_only | none |
| GOOGL | cloud_ai_capex | 315.22 |  | 319.7063 | -1.4033 | 324.42 | 320.24 | 0.3553 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 539.96 |  | 548.9576 | -1.639 | 556.12 | 542.33 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 413.65 |  | 417.4626 | -0.9133 | 420.72 | 412.69 | 1.2595 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.52 |  | 553.1167 | -1.1926 | 557.38 | 545.965 | 0.1244 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.09 |  | 582.1224 | -1.0363 | 585.98 | 576.635 | 0.0746 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389 |  | 393.7149 | -1.1975 | 397.34 | 390.54 | 0.455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 984.475 |  | 989.2229 | -0.48 | 999.04 | 964.86 | 0.8126 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.47 |  | 210.8975 | -2.0994 | 213.785 | 207.665 | 1.9373 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 442.67 |  | 444.6984 | -0.4561 | 450.07 | 438.55 | 0.558 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.12 |  | 48.5357 | -0.8564 | 48.88 | 47.635 | 1.7872 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 31.12 |  | 31.5117 | -1.243 | 31.52 | 30.23 | 0.0643 | below_vwap | below_vwap |
| SPY | market_regime | 736.88 |  | 739.6316 | -0.372 | 742.515 | 738.54 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.1 |  | 291.8836 | -0.2685 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.18 |  | 122.9643 | -2.2643 | 124.22 | 122.07 | 1.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.28 |  | 83.2829 | -2.405 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 301.97 |  | 308.1437 | -2.0035 | 311.13 | 303.96 | 0.5464 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 411.57 |  | 413.5678 | -0.4831 | 415.53 | 406.545 | 3.3166 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 646.01 |  | 654.425 | -1.2859 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1004.15 |  | 1011.8752 | -0.7635 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 475.54 |  | 476.7394 | -0.2516 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.55 |  | 144.0409 | -0.3408 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.36 |  | 176.9589 | -1.4687 | 177.84 | 173.19 | 4.2957 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.03 |  | 319.5009 | -2.3383 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 829.27 |  | 864.7926 | -4.1076 | 880.26 | 833 | 0.3003 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 403.215 |  | 409.4744 | -1.5286 | 408.58 | 397.9 | 0.6671 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.78 |  | 115.5229 | -3.2399 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.64 |  | 331.1952 | -1.9793 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.91 |  | 1806.0894 | -0.5082 | 1806.11 | 1780.9 | 0.5726 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 563.615 |  | 567.0577 | -0.6071 | 566.18 | 548.47 | 2.468 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.89 |  | 321.8234 | -0.9115 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.71 |  | 216.0735 | -0.6311 | 217.88 | 212.99 | 0.1258 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 368.805 |  | 372.6765 | -1.0388 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 292.46 |  | 298.252 | -1.942 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.22 |  | 65.804 | -2.4071 | 67.455 | 65.81 | 3.7683 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.22 |  | 55.111 | -1.6168 | 55.76 | 54.22 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.115 |  | 135.9206 | -1.3284 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.59 |  | 344.6636 | -1.472 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 508.62 |  | 507.6287 | 0.1953 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.83 |  | 296.9037 | -0.0248 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.45 |  | 30.266 | -2.6962 | 31.13 | 29.12 | 0.0679 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.195 |  | 42.1472 | -2.2592 | 43.21 | 40.51 | 0.0728 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.85 |  | 24.1271 | -1.1487 | 24.46 | 23.265 | 0.1258 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1621.015 |  | 1624.7609 | -0.2305 | 1651.355 | 1560 | 1.4806 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 557.545 |  | 563.0441 | -0.9767 | 576.24 | 556.3 | 0.104 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 916.42 |  | 924.226 | -0.8446 | 933.5 | 908.955 | 1.5975 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 232.42 |  | 234.8315 | -1.0269 | 238.285 | 235.71 | 0.1678 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.15 |  | 606.2135 | -0.8353 | 614.15 | 605.39 | 0.3161 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 275.665 |  | 279.6873 | -1.4382 | 283 | 276.24 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 170.525 |  | 174.184 | -2.1007 | 177.88 | 168.18 | 1.1728 | below_vwap | below_vwap,spread_too_wide |
