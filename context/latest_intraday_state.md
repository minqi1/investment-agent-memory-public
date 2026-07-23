# Intraday State

- Generated at: `2026-07-23T23:13:20+08:00`
- Market time ET: `2026-07-23T11:13:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 20, 'watch_only': 1, 'below_vwap': 32, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.325 |  | 694.5139 | -0.7471 | 698.65 | 693.24 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546 |  | 553.3967 | -1.3366 | 557.38 | 545.965 | 0.0769 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.18 |  | 582.2148 | -1.0365 | 585.98 | 576.635 | 0.0764 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.63 |  | 739.7389 | -0.4203 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.67 |  | 321.2532 | 0.1297 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| 2 | LIN | industrial_gases | 508.665 |  | 507.5972 | 0.2104 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | SOXX | semiconductor_index | 546 |  | 553.3967 | -1.3366 | 557.38 | 545.965 | 0.0769 | below_vwap | below_vwap |
| 4 | IWM | market_regime | 290.96 |  | 291.9093 | -0.3252 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 5 | MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 6 | SMCI | ai_server_oem | 30.96 |  | 31.5316 | -1.8127 | 31.52 | 30.23 | 0.0646 | below_vwap | below_vwap |
| 7 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 8 | IREN | high_beta_ai_infrastructure | 40.96 |  | 42.17 | -2.8692 | 43.21 | 40.51 | 0.0977 | below_vwap | below_vwap |
| 9 | CIEN | ai_networking_optical | 402.015 |  | 409.7642 | -1.8911 | 408.58 | 397.9 | 0.2861 | below_vwap | below_vwap |
| 10 | TT | data_center_power_cooling | 475.96 |  | 476.7527 | -0.1663 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 143.45 |  | 144.0604 | -0.4237 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 645.41 |  | 654.6912 | -1.4176 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ETN | data_center_power_cooling | 411.23 |  | 413.6279 | -0.5797 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LRCX | semiconductor_equipment | 318.42 |  | 321.8826 | -1.0757 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | APD | industrial_gases | 296.58 |  | 296.9051 | -0.1095 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHR | ai_networking_optical | 311.49 |  | 319.6294 | -2.5465 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | TER | semiconductor_test_packaging | 368 |  | 373.1066 | -1.3687 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | COHU | semiconductor_test_packaging | 54.22 |  | 55.111 | -1.6168 | 55.76 | 54.22 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | AAOI | ai_networking_optical | 111.38 |  | 115.6361 | -3.6806 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | TSM | foundry | 413.58 |  | 417.6847 | -0.9827 | 420.72 | 412.69 | 1.3613 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.67 |  | 321.2532 | 0.1297 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| 2 | TSM | foundry | 413.58 |  | 417.6847 | -0.9827 | 420.72 | 412.69 | 1.3613 | below_vwap | below_vwap,spread_too_wide |
| 3 | SOXX | semiconductor_index | 546 |  | 553.3967 | -1.3366 | 557.38 | 545.965 | 0.0769 | below_vwap | below_vwap |
| 4 | MU | memory_hbm_storage | 982.71 |  | 989.3619 | -0.6723 | 999.04 | 964.86 | 0.8843 | below_vwap | below_vwap,spread_too_wide |
| 5 | ASML | semiconductor_equipment | 1795.39 |  | 1806.3248 | -0.6054 | 1806.11 | 1780.9 | 0.6032 | below_vwap | below_vwap,spread_too_wide |
| 6 | AMAT | semiconductor_equipment | 561.76 |  | 567.1468 | -0.9498 | 566.18 | 548.47 | 0.4415 | below_vwap | below_vwap,spread_too_wide |
| 7 | TT | data_center_power_cooling | 475.96 |  | 476.7527 | -0.1663 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | ANET | ai_networking_optical | 174.47 |  | 177.0388 | -1.451 | 177.84 | 173.19 | 3.2269 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 143.45 |  | 144.0604 | -0.4237 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 645.41 |  | 654.6912 | -1.4176 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 214.42 |  | 216.1109 | -0.7824 | 217.88 | 212.99 | 2.1873 | below_vwap | below_vwap,spread_too_wide |
| 12 | ETN | data_center_power_cooling | 411.23 |  | 413.6279 | -0.5797 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1001.21 |  | 1011.9696 | -1.0632 | 1023.33 | 979.08 | 2.3162 | below_vwap | below_vwap,spread_too_wide |
| 14 | IWM | market_regime | 290.96 |  | 291.9093 | -0.3252 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 318.42 |  | 321.8826 | -1.0757 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 557.76 |  | 563.1795 | -0.9623 | 576.24 | 556.3 | 3.9372 | below_vwap | below_vwap,spread_too_wide |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | APD | industrial_gases | 296.58 |  | 296.9051 | -0.1095 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | HPE | ai_server_oem | 47.95 |  | 48.5788 | -1.2945 | 48.88 | 47.635 | 4.3796 | below_vwap | below_vwap,spread_too_wide |
| 20 | COHR | ai_networking_optical | 311.49 |  | 319.6294 | -2.5465 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.325 |  | 694.5139 | -0.7471 | 698.65 | 693.24 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.485 |  | 66.9471 | -2.1839 | 68.245 | 66.7 | 0.0153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.86 |  | 208.5793 | -0.8243 | 210.85 | 208.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 377.96 |  | 384.6794 | -1.7468 | 391.71 | 387.245 | 0.0132 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.67 |  | 321.2532 | 0.1297 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| GOOGL | cloud_ai_capex | 315.655 |  | 319.8199 | -1.3023 | 324.42 | 320.24 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 540.145 |  | 549.3496 | -1.6756 | 556.12 | 542.33 | 1.4033 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 413.58 |  | 417.6847 | -0.9827 | 420.72 | 412.69 | 1.3613 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546 |  | 553.3967 | -1.3366 | 557.38 | 545.965 | 0.0769 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.18 |  | 582.2148 | -1.0365 | 585.98 | 576.635 | 0.0764 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 388.73 |  | 393.8239 | -1.2935 | 397.34 | 390.54 | 2.4953 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 982.71 |  | 989.3619 | -0.6723 | 999.04 | 964.86 | 0.8843 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 205.79 |  | 211.1649 | -2.5453 | 213.785 | 207.665 | 0.5783 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 440.69 |  | 444.81 | -0.9262 | 450.07 | 438.55 | 2.4961 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.95 |  | 48.5788 | -1.2945 | 48.88 | 47.635 | 4.3796 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 30.96 |  | 31.5316 | -1.8127 | 31.52 | 30.23 | 0.0646 | below_vwap | below_vwap |
| SPY | market_regime | 736.63 |  | 739.7389 | -0.4203 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.96 |  | 291.9093 | -0.3252 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.87 |  | 123.0305 | -2.5688 | 124.22 | 122.07 | 1.2514 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.175 |  | 83.31 | -2.5628 | 84.415 | 80.64 | 4.903 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.72 |  | 308.9275 | -2.3331 | 311.13 | 303.96 | 2.3366 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 411.23 |  | 413.6279 | -0.5797 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 645.41 |  | 654.6912 | -1.4176 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1001.21 |  | 1011.9696 | -1.0632 | 1023.33 | 979.08 | 2.3162 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.96 |  | 476.7527 | -0.1663 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.45 |  | 144.0604 | -0.4237 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.47 |  | 177.0388 | -1.451 | 177.84 | 173.19 | 3.2269 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.49 |  | 319.6294 | -2.5465 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 825.93 |  | 865.6307 | -4.5863 | 880.26 | 833 | 4.1372 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.015 |  | 409.7642 | -1.8911 | 408.58 | 397.9 | 0.2861 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.38 |  | 115.6361 | -3.6806 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 323.74 |  | 331.4403 | -2.3233 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1795.39 |  | 1806.3248 | -0.6054 | 1806.11 | 1780.9 | 0.6032 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 561.76 |  | 567.1468 | -0.9498 | 566.18 | 548.47 | 0.4415 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.42 |  | 321.8826 | -1.0757 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.42 |  | 216.1109 | -0.7824 | 217.88 | 212.99 | 2.1873 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 368 |  | 373.1066 | -1.3687 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.65 |  | 298.5623 | -2.3152 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.205 |  | 65.9562 | -2.6552 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.22 |  | 55.111 | -1.6168 | 55.76 | 54.22 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.84 |  | 136.1604 | -1.7042 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 508.665 |  | 507.5972 | 0.2104 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.58 |  | 296.9051 | -0.1095 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.3 |  | 30.284 | -3.2493 | 31.13 | 29.12 | 0.1365 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.96 |  | 42.17 | -2.8692 | 43.21 | 40.51 | 0.0977 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.75 |  | 24.1356 | -1.5976 | 24.46 | 23.265 | 0.1263 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1617.99 |  | 1625.0531 | -0.4346 | 1651.355 | 1560 | 0.8035 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 557.76 |  | 563.1795 | -0.9623 | 576.24 | 556.3 | 3.9372 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 916.07 |  | 924.7059 | -0.9339 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.94 |  | 234.8729 | -0.823 | 238.285 | 235.71 | 0.0429 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 600.18 |  | 606.4059 | -1.0267 | 614.15 | 605.39 | 1.5445 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 275.06 |  | 279.7716 | -1.6841 | 283 | 276.24 | 0.189 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SKHY | memory_hbm_storage | 169.73 |  | 174.2617 | -2.6005 | 177.88 | 168.18 | 0.5185 | below_vwap | below_vwap,spread_too_wide |
