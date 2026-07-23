# Intraday State

- Generated at: `2026-07-23T23:52:39+08:00`
- Market time ET: `2026-07-23T11:52:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 20, 'below_vwap': 32, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.93 |  | 693.2413 | -0.4777 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.67 |  | 551.4882 | -0.8737 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.46 |  | 581.3466 | -0.8406 | 585.98 | 576.635 | 0.0815 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.74 |  | 738.9215 | -0.2952 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1635.93 |  | 1625.4229 | 0.6464 | 1651.355 | 1560 | 0.2133 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.08 |  | 476.6242 | 0.0956 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | GEV | data_center_power_cooling | 1011.52 |  | 1011.0979 | 0.0417 | 1023.33 | 979.08 | 2.2817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | GOOGL | cloud_ai_capex | 319.55 |  | 319.4389 | 0.0348 | 324.42 | 320.24 | 0.169 | below_opening_15m_low | below_opening_15m_low |
| 5 | TSM | foundry | 413.62 |  | 416.6589 | -0.7293 | 420.72 | 412.69 | 0.0967 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 546.67 |  | 551.4882 | -0.8737 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1794.46 |  | 1804.056 | -0.5319 | 1806.11 | 1780.9 | 0.1025 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.13 |  | 291.7173 | -0.2013 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 9 | HPE | ai_server_oem | 47.8 |  | 48.3757 | -1.19 | 48.88 | 47.635 | 0.1255 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 31.145 |  | 31.4459 | -0.9568 | 31.52 | 30.23 | 0.0642 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.465 |  | 41.9085 | -1.0582 | 43.21 | 40.51 | 0.0724 | below_vwap | below_vwap |
| 13 | LIN | industrial_gases | 507.72 |  | 507.7353 | -0.003 | 510.71 | 502.72 | 0.2324 | below_vwap | below_vwap |
| 14 | ANET | ai_networking_optical | 174.05 |  | 176.7382 | -1.521 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 171.15 |  | 173.6167 | -1.4208 | 177.88 | 168.18 | 0.2454 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.45 |  | 143.9605 | -0.3546 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 645.555 |  | 653.3084 | -1.1868 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 412.5 |  | 413.2352 | -0.1779 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 318.12 |  | 321.4575 | -1.0382 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 276.97 |  | 279.0699 | -0.7525 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1635.93 |  | 1625.4229 | 0.6464 | 1651.355 | 1560 | 0.2133 | watch_only | none |
| 2 | TSM | foundry | 413.62 |  | 416.6589 | -0.7293 | 420.72 | 412.69 | 0.0967 | below_vwap | below_vwap |
| 3 | SOXX | semiconductor_index | 546.67 |  | 551.4882 | -0.8737 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| 4 | MU | memory_hbm_storage | 985.94 |  | 988.4379 | -0.2527 | 999.04 | 964.86 | 0.6015 | below_vwap | below_vwap,spread_too_wide |
| 5 | ASML | semiconductor_equipment | 1794.46 |  | 1804.056 | -0.5319 | 1806.11 | 1780.9 | 0.1025 | below_vwap | below_vwap |
| 6 | AMAT | semiconductor_equipment | 562.7 |  | 566.4023 | -0.6537 | 566.18 | 548.47 | 1.0823 | below_vwap | below_vwap,spread_too_wide |
| 7 | ANET | ai_networking_optical | 174.05 |  | 176.7382 | -1.521 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 143.45 |  | 143.9605 | -0.3546 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | PWR | data_center_power_cooling | 645.555 |  | 653.3084 | -1.1868 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | KLAC | semiconductor_equipment | 213.74 |  | 215.768 | -0.9399 | 217.88 | 212.99 | 0.7111 | below_vwap | below_vwap,spread_too_wide |
| 11 | ETN | data_center_power_cooling | 412.5 |  | 413.2352 | -0.1779 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IWM | market_regime | 291.13 |  | 291.7173 | -0.2013 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 318.12 |  | 321.4575 | -1.0382 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ARM | ai_accelerator | 276.97 |  | 279.0699 | -0.7525 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 561.29 |  | 562.9271 | -0.2908 | 576.24 | 556.3 | 0.4044 | below_vwap | below_vwap,spread_too_wide |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LIN | industrial_gases | 507.72 |  | 507.7353 | -0.003 | 510.71 | 502.72 | 0.2324 | below_vwap | below_vwap |
| 18 | APD | industrial_gases | 295.81 |  | 296.7258 | -0.3086 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | HPE | ai_server_oem | 47.8 |  | 48.3757 | -1.19 | 48.88 | 47.635 | 0.1255 | below_vwap | below_vwap |
| 20 | COHR | ai_networking_optical | 314.08 |  | 318.6271 | -1.4271 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.93 |  | 693.2413 | -0.4777 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.65 |  | 66.5906 | -1.4126 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.7 |  | 208.1984 | -0.2394 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 378.435 |  | 383.2856 | -1.2655 | 391.71 | 387.245 | 0.2352 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.6 |  | 321.2454 | -0.2009 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.55 |  | 319.4389 | 0.0348 | 324.42 | 320.24 | 0.169 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 538.975 |  | 546.9415 | -1.4566 | 556.12 | 542.33 | 1.0798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 413.62 |  | 416.6589 | -0.7293 | 420.72 | 412.69 | 0.0967 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.67 |  | 551.4882 | -0.8737 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.46 |  | 581.3466 | -0.8406 | 585.98 | 576.635 | 0.0815 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 388.28 |  | 393.0232 | -1.2069 | 397.34 | 390.54 | 1.3444 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 985.94 |  | 988.4379 | -0.2527 | 999.04 | 964.86 | 0.6015 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.53 |  | 210.2067 | -1.7491 | 213.785 | 207.665 | 0.3535 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 440.3 |  | 444.0212 | -0.8381 | 450.07 | 438.55 | 2.5823 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.8 |  | 48.3757 | -1.19 | 48.88 | 47.635 | 0.1255 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.145 |  | 31.4459 | -0.9568 | 31.52 | 30.23 | 0.0642 | below_vwap | below_vwap |
| SPY | market_regime | 736.74 |  | 738.9215 | -0.2952 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.13 |  | 291.7173 | -0.2013 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.3 |  | 122.4779 | -1.7782 | 124.22 | 122.07 | 0.0748 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.96 |  | 83.0093 | -1.2641 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.055 |  | 306.969 | -1.6008 | 311.13 | 303.96 | 0.7416 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.5 |  | 413.2352 | -0.1779 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 645.555 |  | 653.3084 | -1.1868 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1011.52 |  | 1011.0979 | 0.0417 | 1023.33 | 979.08 | 2.2817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.08 |  | 476.6242 | 0.0956 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.45 |  | 143.9605 | -0.3546 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.05 |  | 176.7382 | -1.521 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 314.08 |  | 318.6271 | -1.4271 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 833 |  | 860.7298 | -3.2217 | 880.26 | 833 | 4.4418 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 403.52 |  | 408.6163 | -1.2472 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 112.555 |  | 114.8886 | -2.0312 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.14 |  | 327.816 | -1.1214 | 341.68 | 327.43 | 4.9361 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1794.46 |  | 1804.056 | -0.5319 | 1806.11 | 1780.9 | 0.1025 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 562.7 |  | 566.4023 | -0.6537 | 566.18 | 548.47 | 1.0823 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.12 |  | 321.4575 | -1.0382 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 213.74 |  | 215.768 | -0.9399 | 217.88 | 212.99 | 0.7111 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 369.045 |  | 371.6723 | -0.7069 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.79 |  | 295.7863 | -2.0272 | 301.305 | 293.685 | 5.0174 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.22 |  | 65.3945 | -1.796 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.005 |  | 54.694 | -1.2597 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.15 |  | 135.4358 | -0.9494 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.3 |  | 343.1553 | -1.1235 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.72 |  | 507.7353 | -0.003 | 510.71 | 502.72 | 0.2324 | below_vwap | below_vwap |
| APD | industrial_gases | 295.81 |  | 296.7258 | -0.3086 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.855 |  | 30.0812 | -0.7521 | 31.13 | 29.12 | 0.134 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.465 |  | 41.9085 | -1.0582 | 43.21 | 40.51 | 0.0724 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.98 |  | 24.0551 | -0.3123 | 24.46 | 23.265 | 0.1251 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1635.93 |  | 1625.4229 | 0.6464 | 1651.355 | 1560 | 0.2133 | watch_only | none |
| WDC | memory_hbm_storage | 561.29 |  | 562.9271 | -0.2908 | 576.24 | 556.3 | 0.4044 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 921.8 |  | 923.4841 | -0.1824 | 933.5 | 908.955 | 0.4752 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 232.73 |  | 234.3761 | -0.7023 | 238.285 | 235.71 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 599.9 |  | 604.2256 | -0.7159 | 614.15 | 605.39 | 0.5034 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 276.97 |  | 279.0699 | -0.7525 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 171.15 |  | 173.6167 | -1.4208 | 177.88 | 168.18 | 0.2454 | below_vwap | below_vwap |
