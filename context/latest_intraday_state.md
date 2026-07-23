# Intraday State

- Generated at: `2026-07-24T01:26:57+08:00`
- Market time ET: `2026-07-23T13:26:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_opening_15m_low': 8, 'below_vwap': 16, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 2, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.5 |  | 693.1236 | 0.0543 | 698.65 | 693.24 | 0.0072 | watch_only | none |
| SOXX | semiconductor_index | 551.24 |  | 550.9804 | 0.0471 | 557.38 | 545.965 | 0.0907 | watch_only | none |
| SMH | semiconductor_index | 580.93 |  | 581.1586 | -0.0393 | 585.98 | 576.635 | 0.074 | below_vwap | below_vwap |
| SPY | market_regime | 739.08 |  | 738.7968 | 0.0383 | 742.515 | 738.54 | 0.0189 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 999.69 |  | 991.3413 | 0.8422 | 999.04 | 964.86 | 0.2831 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1806.11 |  | 1804.0574 | 0.1138 | 1806.11 | 1780.9 | 0.0797 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.3 |  | 31.6665 | 2.0006 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1806.11 |  | 1804.0574 | 0.1138 | 1806.11 | 1780.9 | 0.0797 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 551.24 |  | 550.9804 | 0.0471 | 557.38 | 545.965 | 0.0907 | watch_only | none |
| 3 | IWM | market_regime | 291.7 |  | 291.6857 | 0.0049 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 4 | QQQ | market_regime | 693.5 |  | 693.1236 | 0.0543 | 698.65 | 693.24 | 0.0072 | watch_only | none |
| 5 | SPY | market_regime | 739.08 |  | 738.7968 | 0.0383 | 742.515 | 738.54 | 0.0189 | watch_only | none |
| 6 | HPE | ai_server_oem | 48.36 |  | 48.3544 | 0.0116 | 48.88 | 47.635 | 0.1034 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 320.72 |  | 319.5409 | 0.369 | 324.42 | 320.24 | 0.0998 | watch_only | none |
| 8 | MU | memory_hbm_storage | 999.69 |  | 991.3413 | 0.8422 | 999.04 | 964.86 | 0.2831 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 477.58 |  | 476.8113 | 0.1612 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 144.17 |  | 143.9666 | 0.1413 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 414.18 |  | 413.3931 | 0.1903 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | MKSI | semiconductor_materials | 343.45 |  | 342.8978 | 0.161 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | NVDA | ai_accelerator | 210.26 |  | 208.5286 | 0.8303 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 14 | ALAB | ai_networking_optical | 328.695 |  | 327.7889 | 0.2764 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 417.88 |  | 416.6977 | 0.2837 | 420.72 | 412.69 | 0.4762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | CIEN | ai_networking_optical | 409.52 |  | 408.2064 | 0.3218 | 408.58 | 397.9 | 3.8997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ANET | ai_networking_optical | 177.2 |  | 176.723 | 0.2699 | 177.84 | 173.19 | 2.2573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | KLAC | semiconductor_equipment | 216.03 |  | 215.732 | 0.1381 | 217.88 | 212.99 | 2.3886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 374.945 |  | 372.2558 | 0.7224 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SMCI | ai_server_oem | 32.3 |  | 31.6665 | 2.0006 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 999.69 |  | 991.3413 | 0.8422 | 999.04 | 964.86 | 0.2831 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1806.11 |  | 1804.0574 | 0.1138 | 1806.11 | 1780.9 | 0.0797 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.3 |  | 31.6665 | 2.0006 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1033.27 |  | 1012.8796 | 2.0131 | 1023.33 | 979.08 | 0.392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | CIEN | ai_networking_optical | 409.52 |  | 408.2064 | 0.3218 | 408.58 | 397.9 | 3.8997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SNDK | memory_hbm_storage | 1677.105 |  | 1640.1319 | 2.2543 | 1651.355 | 1560 | 0.8044 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SOXX | semiconductor_index | 551.24 |  | 550.9804 | 0.0471 | 557.38 | 545.965 | 0.0907 | watch_only | none |
| 8 | NVDA | ai_accelerator | 210.26 |  | 208.5286 | 0.8303 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 9 | IWM | market_regime | 291.7 |  | 291.6857 | 0.0049 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 10 | QQQ | market_regime | 693.5 |  | 693.1236 | 0.0543 | 698.65 | 693.24 | 0.0072 | watch_only | none |
| 11 | SPY | market_regime | 739.08 |  | 738.7968 | 0.0383 | 742.515 | 738.54 | 0.0189 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 320.72 |  | 319.5409 | 0.369 | 324.42 | 320.24 | 0.0998 | watch_only | none |
| 13 | HPE | ai_server_oem | 48.36 |  | 48.3544 | 0.0116 | 48.88 | 47.635 | 0.1034 | watch_only | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.27 |  | 24.0585 | 0.879 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.33 |  | 30.0542 | 0.9177 | 31.13 | 29.12 | 0.1319 | watch_only | none |
| 16 | TQQQ | leveraged_tool | 66.71 |  | 66.5738 | 0.2046 | 68.245 | 66.7 | 0.015 | watch_only | none |
| 17 | SMH | semiconductor_index | 580.93 |  | 581.1586 | -0.0393 | 585.98 | 576.635 | 0.074 | below_vwap | below_vwap |
| 18 | AVGO | custom_silicon_networking | 392.39 |  | 392.5745 | -0.047 | 397.34 | 390.54 | 0.2268 | below_vwap | below_vwap |
| 19 | AMAT | semiconductor_equipment | 564.13 |  | 566.1254 | -0.3525 | 566.18 | 548.47 | 0.8207 | below_vwap | below_vwap,spread_too_wide |
| 20 | PWR | data_center_power_cooling | 650.745 |  | 652.1038 | -0.2084 | 656.38 | 642.37 | 0.2474 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.5 |  | 693.1236 | 0.0543 | 698.65 | 693.24 | 0.0072 | watch_only | none |
| TQQQ | leveraged_tool | 66.71 |  | 66.5738 | 0.2046 | 68.245 | 66.7 | 0.015 | watch_only | none |
| NVDA | ai_accelerator | 210.26 |  | 208.5286 | 0.8303 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.41 |  | 382.7453 | -0.3489 | 391.71 | 387.245 | 0.3566 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.85 |  | 321.1156 | -0.0827 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 320.72 |  | 319.5409 | 0.369 | 324.42 | 320.24 | 0.0998 | watch_only | none |
| AMD | ai_accelerator | 535.165 |  | 541.3417 | -1.141 | 556.12 | 542.33 | 3.3634 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.88 |  | 416.6977 | 0.2837 | 420.72 | 412.69 | 0.4762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.24 |  | 550.9804 | 0.0471 | 557.38 | 545.965 | 0.0907 | watch_only | none |
| SMH | semiconductor_index | 580.93 |  | 581.1586 | -0.0393 | 585.98 | 576.635 | 0.074 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 392.39 |  | 392.5745 | -0.047 | 397.34 | 390.54 | 0.2268 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 999.69 |  | 991.3413 | 0.8422 | 999.04 | 964.86 | 0.2831 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 208.455 |  | 209.8317 | -0.6561 | 213.785 | 207.665 | 0.1247 | below_vwap | below_vwap |
| DELL | ai_server_oem | 443.46 |  | 444.0577 | -0.1346 | 450.07 | 438.55 | 0.4036 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.36 |  | 48.3544 | 0.0116 | 48.88 | 47.635 | 0.1034 | watch_only | none |
| SMCI | ai_server_oem | 32.3 |  | 31.6665 | 2.0006 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.08 |  | 738.7968 | 0.0383 | 742.515 | 738.54 | 0.0189 | watch_only | none |
| IWM | market_regime | 291.7 |  | 291.6857 | 0.0049 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 121.02 |  | 122.0631 | -0.8546 | 124.22 | 122.07 | 0.0909 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.835 |  | 82.8591 | -0.029 | 84.415 | 80.64 | 5.01 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.55 |  | 306.3245 | -0.5793 | 311.13 | 303.96 | 1.228 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.18 |  | 413.3931 | 0.1903 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.745 |  | 652.1038 | -0.2084 | 656.38 | 642.37 | 0.2474 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1033.27 |  | 1012.8796 | 2.0131 | 1023.33 | 979.08 | 0.392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.58 |  | 476.8113 | 0.1612 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.17 |  | 143.9666 | 0.1413 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.2 |  | 176.723 | 0.2699 | 177.84 | 173.19 | 2.2573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.97 |  | 318.2239 | -0.7083 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.19 |  | 858.2474 | -1.2884 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 409.52 |  | 408.2064 | 0.3218 | 408.58 | 397.9 | 3.8997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.87 |  | 114.6799 | -0.7062 | 118.01 | 108.505 | 4.9706 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 328.695 |  | 327.7889 | 0.2764 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.11 |  | 1804.0574 | 0.1138 | 1806.11 | 1780.9 | 0.0797 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 564.13 |  | 566.1254 | -0.3525 | 566.18 | 548.47 | 0.8207 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.56 |  | 321.3054 | -0.232 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.03 |  | 215.732 | 0.1381 | 217.88 | 212.99 | 2.3886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 374.945 |  | 372.2558 | 0.7224 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.73 |  | 294.8587 | -1.0611 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.21 |  | 65.306 | -0.147 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.35 |  | 135.3658 | -0.0117 | 137.81 | 135.66 | 4.9871 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 343.45 |  | 342.8978 | 0.161 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.09 |  | 507.564 | -0.2904 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.31 |  | 296.0321 | -0.5817 | 299.26 | 295.795 | 0.1937 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.33 |  | 30.0542 | 0.9177 | 31.13 | 29.12 | 0.1319 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.24 |  | 41.7374 | -1.1917 | 43.21 | 40.51 | 0.0485 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.27 |  | 24.0585 | 0.879 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| SNDK | memory_hbm_storage | 1677.105 |  | 1640.1319 | 2.2543 | 1651.355 | 1560 | 0.8044 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 567.7 |  | 564.2438 | 0.6125 | 576.24 | 556.3 | 1.4708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 926.01 |  | 924.6577 | 0.1462 | 933.5 | 908.955 | 4.8347 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.62 |  | 234.3558 | 0.1127 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.77 |  | 603.9646 | 0.4645 | 614.15 | 605.39 | 1.3185 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 282.64 |  | 279.5516 | 1.1048 | 283 | 276.24 | 3.8706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 174.4 |  | 173.6167 | 0.4512 | 177.88 | 168.18 | 0.3612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
