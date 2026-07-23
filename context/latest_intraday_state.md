# Intraday State

- Generated at: `2026-07-23T23:36:55+08:00`
- Market time ET: `2026-07-23T11:36:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 17, 'below_vwap': 32, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.805 |  | 693.6036 | -0.5477 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.58 |  | 551.9924 | -0.7994 | 557.38 | 545.965 | 0.095 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.51 |  | 581.5246 | -0.6904 | 585.98 | 576.635 | 0.09 | below_vwap | below_vwap |
| SPY | market_regime | 736.59 |  | 739.1123 | -0.3413 | 742.515 | 738.54 | 0.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1634.74 |  | 1624.8675 | 0.6076 | 1651.355 | 1560 | 0.1915 | watch_only | none |
| 2 | STX | memory_hbm_storage | 923.84 |  | 923.5431 | 0.0322 | 933.5 | 908.955 | 0.2555 | watch_only | none |
| 3 | LIN | industrial_gases | 508.42 |  | 507.7181 | 0.1383 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | MU | memory_hbm_storage | 988.85 |  | 988.4825 | 0.0372 | 999.04 | 964.86 | 0.9607 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | WDC | memory_hbm_storage | 566.1 |  | 562.8272 | 0.5815 | 576.24 | 556.3 | 0.7896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SMH | semiconductor_index | 577.51 |  | 581.5246 | -0.6904 | 585.98 | 576.635 | 0.09 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.58 |  | 551.9924 | -0.7994 | 557.38 | 545.965 | 0.095 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 290.84 |  | 291.7542 | -0.3134 | 293.01 | 290.365 | 0.0138 | below_vwap | below_vwap |
| 9 | HPE | ai_server_oem | 48.115 |  | 48.4459 | -0.6831 | 48.88 | 47.635 | 0.0831 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 31.24 |  | 31.4693 | -0.7286 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.35 |  | 42.0442 | -1.6512 | 43.21 | 40.51 | 0.0484 | below_vwap | below_vwap |
| 13 | AAPL | mega_cap_platform | 320.9 |  | 321.2847 | -0.1197 | 323.25 | 320.82 | 0.0623 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 563.78 |  | 566.7013 | -0.5155 | 566.18 | 548.47 | 0.2111 | below_vwap | below_vwap |
| 15 | ARM | ai_accelerator | 276.665 |  | 279.3329 | -0.9551 | 283 | 276.24 | 0.2602 | below_vwap | below_vwap |
| 16 | TT | data_center_power_cooling | 476.43 |  | 476.6129 | -0.0384 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 143.28 |  | 143.9748 | -0.4826 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 646.06 |  | 653.6125 | -1.1555 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 412.88 |  | 413.278 | -0.0963 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | GEV | data_center_power_cooling | 1008.645 |  | 1011.1497 | -0.2477 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1634.74 |  | 1624.8675 | 0.6076 | 1651.355 | 1560 | 0.1915 | watch_only | none |
| 2 | STX | memory_hbm_storage | 923.84 |  | 923.5431 | 0.0322 | 933.5 | 908.955 | 0.2555 | watch_only | none |
| 3 | TSM | foundry | 414.11 |  | 417.1116 | -0.7196 | 420.72 | 412.69 | 2.1733 | below_vwap | below_vwap,spread_too_wide |
| 4 | SMH | semiconductor_index | 577.51 |  | 581.5246 | -0.6904 | 585.98 | 576.635 | 0.09 | below_vwap | below_vwap |
| 5 | SOXX | semiconductor_index | 547.58 |  | 551.9924 | -0.7994 | 557.38 | 545.965 | 0.095 | below_vwap | below_vwap |
| 6 | ASML | semiconductor_equipment | 1796.56 |  | 1805.3924 | -0.4892 | 1806.11 | 1780.9 | 3.0553 | below_vwap | below_vwap,spread_too_wide |
| 7 | AMAT | semiconductor_equipment | 563.78 |  | 566.7013 | -0.5155 | 566.18 | 548.47 | 0.2111 | below_vwap | below_vwap |
| 8 | TT | data_center_power_cooling | 476.43 |  | 476.6129 | -0.0384 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 174.98 |  | 176.8035 | -1.0314 | 177.84 | 173.19 | 3.1261 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 143.28 |  | 143.9748 | -0.4826 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 646.06 |  | 653.6125 | -1.1555 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 214.83 |  | 215.9528 | -0.5199 | 217.88 | 212.99 | 2.225 | below_vwap | below_vwap,spread_too_wide |
| 13 | ETN | data_center_power_cooling | 412.88 |  | 413.278 | -0.0963 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1008.645 |  | 1011.1497 | -0.2477 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | IWM | market_regime | 290.84 |  | 291.7542 | -0.3134 | 293.01 | 290.365 | 0.0138 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 319.27 |  | 321.591 | -0.7217 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 276.665 |  | 279.3329 | -0.9551 | 283 | 276.24 | 0.2602 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | APD | industrial_gases | 296.38 |  | 296.8488 | -0.1579 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | HPE | ai_server_oem | 48.115 |  | 48.4459 | -0.6831 | 48.88 | 47.635 | 0.0831 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.805 |  | 693.6036 | -0.5477 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.575 |  | 66.6717 | -1.645 | 68.245 | 66.7 | 0.0305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.845 |  | 208.2829 | -0.6903 | 210.85 | 208.49 | 1.0249 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 378.39 |  | 383.8703 | -1.4276 | 391.71 | 387.245 | 0.3488 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.9 |  | 321.2847 | -0.1197 | 323.25 | 320.82 | 0.0623 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 317.61 |  | 319.5325 | -0.6016 | 324.42 | 320.24 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.925 |  | 547.5129 | -1.5685 | 556.12 | 542.33 | 0.6494 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.11 |  | 417.1116 | -0.7196 | 420.72 | 412.69 | 2.1733 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.58 |  | 551.9924 | -0.7994 | 557.38 | 545.965 | 0.095 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.51 |  | 581.5246 | -0.6904 | 585.98 | 576.635 | 0.09 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 388.395 |  | 393.2557 | -1.236 | 397.34 | 390.54 | 0.1056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 988.85 |  | 988.4825 | 0.0372 | 999.04 | 964.86 | 0.9607 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.505 |  | 210.3757 | -1.3645 | 213.785 | 207.665 | 0.2313 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 439.13 |  | 444.2547 | -1.1535 | 450.07 | 438.55 | 0.7674 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.115 |  | 48.4459 | -0.6831 | 48.88 | 47.635 | 0.0831 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.24 |  | 31.4693 | -0.7286 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| SPY | market_regime | 736.59 |  | 739.1123 | -0.3413 | 742.515 | 738.54 | 0.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.84 |  | 291.7542 | -0.3134 | 293.01 | 290.365 | 0.0138 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.08 |  | 122.7137 | -2.1462 | 124.22 | 122.07 | 0.075 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.78 |  | 83.0947 | -1.5822 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.13 |  | 307.5501 | -1.4372 | 311.13 | 303.96 | 2.3092 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.88 |  | 413.278 | -0.0963 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 646.06 |  | 653.6125 | -1.1555 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1008.645 |  | 1011.1497 | -0.2477 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 476.43 |  | 476.6129 | -0.0384 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.28 |  | 143.9748 | -0.4826 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.98 |  | 176.8035 | -1.0314 | 177.84 | 173.19 | 3.1261 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 314.87 |  | 318.9653 | -1.2839 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.12 |  | 862.2572 | -3.1472 | 880.26 | 833 | 1.7961 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 406.87 |  | 409.0696 | -0.5377 | 408.58 | 397.9 | 4.5862 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 113.095 |  | 115.0308 | -1.6828 | 118.01 | 108.505 | 0.4067 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 324.26 |  | 328.2668 | -1.2206 | 341.68 | 327.43 | 0.5027 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1796.56 |  | 1805.3924 | -0.4892 | 1806.11 | 1780.9 | 3.0553 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 563.78 |  | 566.7013 | -0.5155 | 566.18 | 548.47 | 0.2111 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.27 |  | 321.591 | -0.7217 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.83 |  | 215.9528 | -0.5199 | 217.88 | 212.99 | 2.225 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 369.69 |  | 371.9975 | -0.6203 | 376.78 | 363.37 | 0.5735 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 291.08 |  | 295.9832 | -1.6566 | 301.305 | 293.685 | 4.7169 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.32 |  | 65.4264 | -1.6911 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.78 |  | 54.9332 | -2.0993 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.55 |  | 135.6527 | -1.5501 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.325 |  | 344.4459 | -1.4867 | 347.92 | 341.755 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 508.42 |  | 507.7181 | 0.1383 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.38 |  | 296.8488 | -0.1579 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.79 |  | 30.0977 | -1.0225 | 31.13 | 29.12 | 0.1343 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.35 |  | 42.0442 | -1.6512 | 43.21 | 40.51 | 0.0484 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.93 |  | 24.0663 | -0.5664 | 24.46 | 23.265 | 0.1254 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1634.74 |  | 1624.8675 | 0.6076 | 1651.355 | 1560 | 0.1915 | watch_only | none |
| WDC | memory_hbm_storage | 566.1 |  | 562.8272 | 0.5815 | 576.24 | 556.3 | 0.7896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 923.84 |  | 923.5431 | 0.0322 | 933.5 | 908.955 | 0.2555 | watch_only | none |
| AMZN | cloud_ai_capex | 232.53 |  | 234.5402 | -0.8571 | 238.285 | 235.71 | 0.0215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 598.26 |  | 605.0157 | -1.1166 | 614.15 | 605.39 | 0.0802 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 276.665 |  | 279.3329 | -0.9551 | 283 | 276.24 | 0.2602 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 170.52 |  | 173.7616 | -1.8655 | 177.88 | 168.18 | 0.5337 | below_vwap | below_vwap,spread_too_wide |
