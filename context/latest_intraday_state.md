# Intraday State

- Generated at: `2026-07-24T01:39:51+08:00`
- Market time ET: `2026-07-23T13:39:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 16, 'watch_only': 5, 'spread_too_wide_or_missing': 9, 'price_stale_or_missing': 1, 'below_vwap': 24, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.71 |  | 693.1026 | -0.2009 | 698.65 | 693.24 | 0.026 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.59 |  | 550.9707 | -0.4321 | 557.38 | 545.965 | 0.0565 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.33 |  | 581.1417 | -0.4838 | 585.98 | 576.635 | 0.0674 | below_vwap | below_vwap |
| SPY | market_regime | 737.625 |  | 738.7859 | -0.1571 | 742.515 | 738.54 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.225 |  | 31.6871 | 1.6975 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 209.21 |  | 208.5587 | 0.3123 | 210.85 | 208.49 | 0.2438 | watch_only | none |
| 2 | WDC | memory_hbm_storage | 565.36 |  | 564.2783 | 0.1917 | 576.24 | 556.3 | 0.168 | watch_only | none |
| 3 | MU | memory_hbm_storage | 996.43 |  | 991.5589 | 0.4913 | 999.04 | 964.86 | 0.1275 | watch_only | none |
| 4 | APLD | high_beta_ai_infrastructure | 30.13 |  | 30.0589 | 0.2366 | 31.13 | 29.12 | 0.0996 | watch_only | none |
| 5 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TSM | foundry | 417.39 |  | 416.7179 | 0.1613 | 420.72 | 412.69 | 1.3177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | CIEN | ai_networking_optical | 410.14 |  | 408.258 | 0.461 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | META | cloud_ai_capex | 605.82 |  | 604.0632 | 0.2908 | 614.15 | 605.39 | 1.8108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TER | semiconductor_test_packaging | 372.295 |  | 372.2887 | 0.0017 | 376.78 | 363.37 | 4.9396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | CORZ | high_beta_ai_infrastructure | 24.19 |  | 24.0649 | 0.5198 | 24.46 | 23.265 | 0.0827 | watch_only | none |
| 11 | ANET | ai_networking_optical | 177.395 |  | 176.7346 | 0.3737 | 177.84 | 173.19 | 1.6009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SMCI | ai_server_oem | 32.225 |  | 31.6871 | 1.6975 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |
| 13 | ARM | ai_accelerator | 281.16 |  | 279.6279 | 0.5479 | 283 | 276.24 | 0.3592 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SMH | semiconductor_index | 578.33 |  | 581.1417 | -0.4838 | 585.98 | 576.635 | 0.0674 | below_vwap | below_vwap |
| 15 | SOXX | semiconductor_index | 548.59 |  | 550.9707 | -0.4321 | 557.38 | 545.965 | 0.0565 | below_vwap | below_vwap |
| 16 | ASML | semiconductor_equipment | 1798.4 |  | 1804.013 | -0.3111 | 1806.11 | 1780.9 | 0.1023 | below_vwap | below_vwap |
| 17 | IWM | market_regime | 291.18 |  | 291.6775 | -0.1706 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 18 | HPE | ai_server_oem | 48.35 |  | 48.3553 | -0.0109 | 48.88 | 47.635 | 0.0414 | below_vwap | below_vwap |
| 19 | CRWV | gpu_cloud_ai_factory | 82.435 |  | 82.8503 | -0.5013 | 84.415 | 80.64 | 0.0607 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.225 |  | 31.6871 | 1.6975 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1028.56 |  | 1013.3053 | 1.5054 | 1023.33 | 979.08 | 0.8556 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | CIEN | ai_networking_optical | 410.14 |  | 408.258 | 0.461 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | SNDK | memory_hbm_storage | 1666.305 |  | 1640.7842 | 1.5554 | 1651.355 | 1560 | 4.441 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.21 |  | 208.5587 | 0.3123 | 210.85 | 208.49 | 0.2438 | watch_only | none |
| 6 | MU | memory_hbm_storage | 996.43 |  | 991.5589 | 0.4913 | 999.04 | 964.86 | 0.1275 | watch_only | none |
| 7 | WDC | memory_hbm_storage | 565.36 |  | 564.2783 | 0.1917 | 576.24 | 556.3 | 0.168 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.19 |  | 24.0649 | 0.5198 | 24.46 | 23.265 | 0.0827 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 30.13 |  | 30.0589 | 0.2366 | 31.13 | 29.12 | 0.0996 | watch_only | none |
| 10 | SMH | semiconductor_index | 578.33 |  | 581.1417 | -0.4838 | 585.98 | 576.635 | 0.0674 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 548.59 |  | 550.9707 | -0.4321 | 557.38 | 545.965 | 0.0565 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 390.99 |  | 392.5527 | -0.3981 | 397.34 | 390.54 | 2.8696 | below_vwap | below_vwap,spread_too_wide |
| 13 | ASML | semiconductor_equipment | 1798.4 |  | 1804.013 | -0.3111 | 1806.11 | 1780.9 | 0.1023 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 559.39 |  | 566.0583 | -1.178 | 566.18 | 548.47 | 2.5885 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 476.07 |  | 476.805 | -0.1542 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 143.7 |  | 143.9644 | -0.1837 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 649.025 |  | 652.0375 | -0.462 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 214.11 |  | 215.714 | -0.7436 | 217.88 | 212.99 | 2.0597 | below_vwap | below_vwap,spread_too_wide |
| 19 | ETN | data_center_power_cooling | 412.89 |  | 413.3991 | -0.1231 | 415.53 | 406.545 | 0.6612 | below_vwap | below_vwap,spread_too_wide |
| 20 | IWM | market_regime | 291.18 |  | 291.6775 | -0.1706 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.71 |  | 693.1026 | -0.2009 | 698.65 | 693.24 | 0.026 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.13 |  | 66.5703 | -0.6614 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.21 |  | 208.5587 | 0.3123 | 210.85 | 208.49 | 0.2438 | watch_only | none |
| MSFT | cloud_ai_capex | 381.095 |  | 382.6903 | -0.4169 | 391.71 | 387.245 | 0.0315 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.49 |  | 321.1091 | -0.1928 | 323.25 | 320.82 | 0.1997 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.39 |  | 319.5536 | -0.0512 | 324.42 | 320.24 | 0.2129 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 532.28 |  | 540.9982 | -1.6115 | 556.12 | 542.33 | 1.7735 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.39 |  | 416.7179 | 0.1613 | 420.72 | 412.69 | 1.3177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.59 |  | 550.9707 | -0.4321 | 557.38 | 545.965 | 0.0565 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.33 |  | 581.1417 | -0.4838 | 585.98 | 576.635 | 0.0674 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.99 |  | 392.5527 | -0.3981 | 397.34 | 390.54 | 2.8696 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 996.43 |  | 991.5589 | 0.4913 | 999.04 | 964.86 | 0.1275 | watch_only | none |
| MRVL | custom_silicon_networking | 207 |  | 209.7617 | -1.3166 | 213.785 | 207.665 | 0.3285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 443.4 |  | 444.0444 | -0.1451 | 450.07 | 438.55 | 0.2932 | below_vwap | below_vwap |
| HPE | ai_server_oem | 48.35 |  | 48.3553 | -0.0109 | 48.88 | 47.635 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.225 |  | 31.6871 | 1.6975 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 737.625 |  | 738.7859 | -0.1571 | 742.515 | 738.54 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.18 |  | 291.6775 | -0.1706 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.31 |  | 122.0253 | -1.4057 | 124.22 | 122.07 | 0.3574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.435 |  | 82.8503 | -0.5013 | 84.415 | 80.64 | 0.0607 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 303.26 |  | 306.2914 | -0.9897 | 311.13 | 303.96 | 1.0024 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.89 |  | 413.3991 | -0.1231 | 415.53 | 406.545 | 0.6612 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 649.025 |  | 652.0375 | -0.462 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.56 |  | 1013.3053 | 1.5054 | 1023.33 | 979.08 | 0.8556 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.07 |  | 476.805 | -0.1542 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.7 |  | 143.9644 | -0.1837 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.395 |  | 176.7346 | 0.3737 | 177.84 | 173.19 | 1.6009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.16 |  | 318.1726 | -0.9468 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 843.42 |  | 858.1172 | -1.7127 | 880.26 | 833 | 0.1909 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 410.14 |  | 408.258 | 0.461 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 113.64 |  | 114.6636 | -0.8927 | 118.01 | 108.505 | 0.2376 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 326.77 |  | 327.7679 | -0.3044 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1798.4 |  | 1804.013 | -0.3111 | 1806.11 | 1780.9 | 0.1023 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.39 |  | 566.0583 | -1.178 | 566.18 | 548.47 | 2.5885 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.68 |  | 321.2369 | -0.796 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.11 |  | 215.714 | -0.7436 | 217.88 | 212.99 | 2.0597 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.295 |  | 372.2887 | 0.0017 | 376.78 | 363.37 | 4.9396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 289.3 |  | 294.7256 | -1.8409 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.81 |  | 65.2908 | -0.7363 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.33 |  | 54.5883 | -0.4732 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.475 |  | 135.3363 | -0.6364 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 505.69 |  | 507.5246 | -0.3615 | 510.71 | 502.72 | 4.9141 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.84 |  | 295.9438 | -0.373 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.13 |  | 30.0589 | 0.2366 | 31.13 | 29.12 | 0.0996 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.04 |  | 41.7247 | -1.6411 | 43.21 | 40.51 | 0.0487 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.19 |  | 24.0649 | 0.5198 | 24.46 | 23.265 | 0.0827 | watch_only | none |
| SNDK | memory_hbm_storage | 1666.305 |  | 1640.7842 | 1.5554 | 1651.355 | 1560 | 4.441 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 565.36 |  | 564.2783 | 0.1917 | 576.24 | 556.3 | 0.168 | watch_only | none |
| STX | memory_hbm_storage | 923.24 |  | 924.6811 | -0.1559 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.14 |  | 234.3549 | -0.0917 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.82 |  | 604.0632 | 0.2908 | 614.15 | 605.39 | 1.8108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.16 |  | 279.6279 | 0.5479 | 283 | 276.24 | 0.3592 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.125 |  | 173.6197 | -0.2849 | 177.88 | 168.18 | 0.4794 | below_vwap | below_vwap,spread_too_wide |
