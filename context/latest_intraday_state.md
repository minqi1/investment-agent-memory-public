# Intraday State

- Generated at: `2026-07-23T23:09:24+08:00`
- Market time ET: `2026-07-23T11:09:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 15, 'watch_only': 1, 'below_vwap': 35, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.65 |  | 694.7315 | -0.5875 | 698.65 | 693.24 | 0.0347 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.815 |  | 553.464 | -0.84 | 557.38 | 545.965 | 0.1002 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.32 |  | 582.2848 | -0.6809 | 585.98 | 576.635 | 0.0813 | below_vwap | below_vwap |
| SPY | market_regime | 737.345 |  | 739.8769 | -0.3422 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.495 |  | 321.2426 | 0.0786 | 323.25 | 320.82 | 0.0498 | watch_only | none |
| 2 | MU | memory_hbm_storage | 990.95 |  | 989.4024 | 0.1564 | 999.04 | 964.86 | 1.1272 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | LIN | industrial_gases | 509.75 |  | 507.5473 | 0.434 | 510.71 | 502.72 | 4.1079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1637.025 |  | 1624.973 | 0.7417 | 1651.355 | 1560 | 0.4423 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SMH | semiconductor_index | 578.32 |  | 582.2848 | -0.6809 | 585.98 | 576.635 | 0.0813 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 548.815 |  | 553.464 | -0.84 | 557.38 | 545.965 | 0.1002 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 291.415 |  | 291.9158 | -0.1716 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| 8 | HPE | ai_server_oem | 48.23 |  | 48.6064 | -0.7744 | 48.88 | 47.635 | 0.0622 | below_vwap | below_vwap |
| 9 | MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 10 | SMCI | ai_server_oem | 31.1 |  | 31.5458 | -1.4131 | 31.52 | 30.23 | 0.0643 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.22 |  | 42.2244 | -2.3788 | 43.21 | 40.51 | 0.097 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 565.31 |  | 567.2638 | -0.3444 | 566.18 | 548.47 | 0.2866 | below_vwap | below_vwap |
| 14 | ETN | data_center_power_cooling | 412.42 |  | 413.6878 | -0.3065 | 415.53 | 406.545 | 0.1625 | below_vwap | below_vwap |
| 15 | WDC | memory_hbm_storage | 561.48 |  | 563.3218 | -0.327 | 576.24 | 556.3 | 0.2725 | below_vwap | below_vwap |
| 16 | CIEN | ai_networking_optical | 405.56 |  | 409.9409 | -1.0687 | 408.58 | 397.9 | 0.3304 | below_vwap | below_vwap |
| 17 | TT | data_center_power_cooling | 476.11 |  | 476.7614 | -0.1366 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | SKHY | memory_hbm_storage | 171.47 |  | 174.3745 | -1.6656 | 177.88 | 168.18 | 0.175 | below_vwap | below_vwap |
| 19 | JCI | data_center_power_cooling | 143.87 |  | 144.0743 | -0.1418 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 649.23 |  | 654.8894 | -0.8642 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.495 |  | 321.2426 | 0.0786 | 323.25 | 320.82 | 0.0498 | watch_only | none |
| 2 | TSM | foundry | 415.24 |  | 417.8104 | -0.6152 | 420.72 | 412.69 | 1.2041 | below_vwap | below_vwap,spread_too_wide |
| 3 | SMH | semiconductor_index | 578.32 |  | 582.2848 | -0.6809 | 585.98 | 576.635 | 0.0813 | below_vwap | below_vwap |
| 4 | SOXX | semiconductor_index | 548.815 |  | 553.464 | -0.84 | 557.38 | 545.965 | 0.1002 | below_vwap | below_vwap |
| 5 | ASML | semiconductor_equipment | 1801.31 |  | 1806.6549 | -0.2958 | 1806.11 | 1780.9 | 0.5796 | below_vwap | below_vwap,spread_too_wide |
| 6 | AMAT | semiconductor_equipment | 565.31 |  | 567.2638 | -0.3444 | 566.18 | 548.47 | 0.2866 | below_vwap | below_vwap |
| 7 | TT | data_center_power_cooling | 476.11 |  | 476.7614 | -0.1366 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | ANET | ai_networking_optical | 174.98 |  | 177.1511 | -1.2256 | 177.84 | 173.19 | 2.8918 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 143.87 |  | 144.0743 | -0.1418 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 649.23 |  | 654.8894 | -0.8642 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 215.21 |  | 216.1321 | -0.4267 | 217.88 | 212.99 | 2.6439 | below_vwap | below_vwap,spread_too_wide |
| 12 | AMD | ai_accelerator | 543.565 |  | 549.7094 | -1.1178 | 556.12 | 542.33 | 2.4008 | below_vwap | below_vwap,spread_too_wide |
| 13 | ETN | data_center_power_cooling | 412.42 |  | 413.6878 | -0.3065 | 415.53 | 406.545 | 0.1625 | below_vwap | below_vwap |
| 14 | GEV | data_center_power_cooling | 1000.49 |  | 1012.0312 | -1.1404 | 1023.33 | 979.08 | 3.6352 | below_vwap | below_vwap,spread_too_wide |
| 15 | IWM | market_regime | 291.415 |  | 291.9158 | -0.1716 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 320.145 |  | 321.949 | -0.5603 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 276.54 |  | 279.9291 | -1.2107 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 561.48 |  | 563.3218 | -0.327 | 576.24 | 556.3 | 0.2725 | below_vwap | below_vwap |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 294.225 |  | 299.3667 | -1.7175 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.65 |  | 694.7315 | -0.5875 | 698.65 | 693.24 | 0.0347 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.84 |  | 67.0186 | -1.7586 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.89 |  | 208.6737 | -0.8548 | 210.85 | 208.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 377.615 |  | 385.1159 | -1.9477 | 391.71 | 387.245 | 0.6462 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 321.495 |  | 321.2426 | 0.0786 | 323.25 | 320.82 | 0.0498 | watch_only | none |
| GOOGL | cloud_ai_capex | 316.49 |  | 319.9104 | -1.0692 | 324.42 | 320.24 | 0.2085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 543.565 |  | 549.7094 | -1.1178 | 556.12 | 542.33 | 2.4008 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.24 |  | 417.8104 | -0.6152 | 420.72 | 412.69 | 1.2041 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.815 |  | 553.464 | -0.84 | 557.38 | 545.965 | 0.1002 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.32 |  | 582.2848 | -0.6809 | 585.98 | 576.635 | 0.0813 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.02 |  | 393.9741 | -1.0036 | 397.34 | 390.54 | 2.2307 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 990.95 |  | 989.4024 | 0.1564 | 999.04 | 964.86 | 1.1272 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.64 |  | 211.3361 | -1.7489 | 213.785 | 207.665 | 0.7031 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.46 |  | 444.8446 | -0.3113 | 450.07 | 438.55 | 2.0137 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.23 |  | 48.6064 | -0.7744 | 48.88 | 47.635 | 0.0622 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.1 |  | 31.5458 | -1.4131 | 31.52 | 30.23 | 0.0643 | below_vwap | below_vwap |
| SPY | market_regime | 737.345 |  | 739.8769 | -0.3422 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.415 |  | 291.9158 | -0.1716 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.53 |  | 123.1407 | -2.1201 | 124.22 | 122.07 | 0.3816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.645 |  | 83.3723 | -2.0718 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.745 |  | 309.1789 | -2.081 | 311.13 | 303.96 | 2.6095 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.42 |  | 413.6878 | -0.3065 | 415.53 | 406.545 | 0.1625 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 649.23 |  | 654.8894 | -0.8642 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1000.49 |  | 1012.0312 | -1.1404 | 1023.33 | 979.08 | 3.6352 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.11 |  | 476.7614 | -0.1366 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.87 |  | 144.0743 | -0.1418 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.98 |  | 177.1511 | -1.2256 | 177.84 | 173.19 | 2.8918 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 314.435 |  | 319.724 | -1.6542 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 839.12 |  | 866.3186 | -3.1396 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 405.56 |  | 409.9409 | -1.0687 | 408.58 | 397.9 | 0.3304 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 113.09 |  | 115.8121 | -2.3505 | 118.01 | 108.505 | 4.8634 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 325.68 |  | 332.1122 | -1.9368 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1801.31 |  | 1806.6549 | -0.2958 | 1806.11 | 1780.9 | 0.5796 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 565.31 |  | 567.2638 | -0.3444 | 566.18 | 548.47 | 0.2866 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 320.145 |  | 321.949 | -0.5603 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.21 |  | 216.1321 | -0.4267 | 217.88 | 212.99 | 2.6439 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.795 |  | 373.5233 | -0.7304 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 294.225 |  | 299.3667 | -1.7175 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.7 |  | 66.1389 | -2.1756 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.22 |  | 55.111 | -1.6168 | 55.76 | 54.22 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.98 |  | 136.2025 | -0.8975 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 509.75 |  | 507.5473 | 0.434 | 510.71 | 502.72 | 4.1079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.55 |  | 296.9121 | -0.122 | 299.26 | 295.795 | 4.9031 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.525 |  | 30.3082 | -2.584 | 31.13 | 29.12 |  | below_vwap | below_vwap,spread_unavailable |
| IREN | high_beta_ai_infrastructure | 41.22 |  | 42.2244 | -2.3788 | 43.21 | 40.51 | 0.097 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.9 |  | 24.1455 | -1.0166 | 24.46 | 23.265 | 0.0837 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1637.025 |  | 1624.973 | 0.7417 | 1651.355 | 1560 | 0.4423 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 561.48 |  | 563.3218 | -0.327 | 576.24 | 556.3 | 0.2725 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 918.1 |  | 925.115 | -0.7583 | 933.5 | 908.955 | 1.8386 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 232.915 |  | 234.9586 | -0.8698 | 238.285 | 235.71 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 600.37 |  | 606.7698 | -1.0547 | 614.15 | 605.39 | 1.6656 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 276.54 |  | 279.9291 | -1.2107 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 171.47 |  | 174.3745 | -1.6656 | 177.88 | 168.18 | 0.175 | below_vwap | below_vwap |
