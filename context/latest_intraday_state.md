# Intraday State

- Generated at: `2026-07-24T01:44:13+08:00`
- Market time ET: `2026-07-23T13:44:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 16, 'watch_only': 4, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 6, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.47 |  | 693.0982 | -0.2349 | 698.65 | 693.24 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.94 |  | 550.9567 | -0.5475 | 557.38 | 545.965 | 0.084 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.95 |  | 581.138 | -0.5486 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| SPY | market_regime | 737.56 |  | 738.7752 | -0.1645 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.09 |  | 31.694 | 1.2493 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | WDC | memory_hbm_storage | 565.33 |  | 564.281 | 0.1859 | 576.24 | 556.3 | 0.1433 | watch_only | none |
| 2 | ARM | ai_accelerator | 280.52 |  | 279.6395 | 0.3149 | 283 | 276.24 | 0.2388 | watch_only | none |
| 3 | NVDA | ai_accelerator | 209.4 |  | 208.5633 | 0.4012 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0656 | 0.3092 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| 5 | SMCI | ai_server_oem | 32.09 |  | 31.694 | 1.2493 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |
| 6 | CIEN | ai_networking_optical | 409.11 |  | 408.2773 | 0.204 | 408.58 | 397.9 | 3.9427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 177.15 |  | 176.7441 | 0.2297 | 177.84 | 173.19 | 0.7846 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | META | cloud_ai_capex | 606.03 |  | 604.0986 | 0.3197 | 614.15 | 605.39 | 1.1551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MU | memory_hbm_storage | 995.99 |  | 991.5948 | 0.4432 | 999.04 | 964.86 | 0.4739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMH | semiconductor_index | 577.95 |  | 581.138 | -0.5486 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 547.94 |  | 550.9567 | -0.5475 | 557.38 | 545.965 | 0.084 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1797.19 |  | 1803.9992 | -0.3774 | 1806.11 | 1780.9 | 0.0495 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 291.155 |  | 291.6698 | -0.1765 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 14 | HPE | ai_server_oem | 48.34 |  | 48.3551 | -0.0313 | 48.88 | 47.635 | 0.0621 | below_vwap | below_vwap |
| 15 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 16 | CRWV | gpu_cloud_ai_factory | 82.32 |  | 82.8458 | -0.6347 | 84.415 | 80.64 | 0.0607 | below_vwap | below_vwap |
| 17 | GEV | data_center_power_cooling | 1027.01 |  | 1013.426 | 1.3404 | 1023.33 | 979.08 | 3.6816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | IREN | high_beta_ai_infrastructure | 40.99 |  | 41.7224 | -1.7554 | 43.21 | 40.51 | 0.0488 | below_vwap | below_vwap |
| 20 | AVGO | custom_silicon_networking | 390.97 |  | 392.5392 | -0.3998 | 397.34 | 390.54 | 0.1893 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.09 |  | 31.694 | 1.2493 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1027.01 |  | 1013.426 | 1.3404 | 1023.33 | 979.08 | 3.6816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | CIEN | ai_networking_optical | 409.11 |  | 408.2773 | 0.204 | 408.58 | 397.9 | 3.9427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1666.53 |  | 1641.2224 | 1.542 | 1651.355 | 1560 | 4.4404 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.4 |  | 208.5633 | 0.4012 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 6 | ARM | ai_accelerator | 280.52 |  | 279.6395 | 0.3149 | 283 | 276.24 | 0.2388 | watch_only | none |
| 7 | WDC | memory_hbm_storage | 565.33 |  | 564.281 | 0.1859 | 576.24 | 556.3 | 0.1433 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0656 | 0.3092 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| 9 | TSM | foundry | 416.605 |  | 416.7204 | -0.0277 | 420.72 | 412.69 | 0.3505 | below_vwap | below_vwap,spread_too_wide |
| 10 | SMH | semiconductor_index | 577.95 |  | 581.138 | -0.5486 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 547.94 |  | 550.9567 | -0.5475 | 557.38 | 545.965 | 0.084 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 390.97 |  | 392.5392 | -0.3998 | 397.34 | 390.54 | 0.1893 | below_vwap | below_vwap |
| 13 | ASML | semiconductor_equipment | 1797.19 |  | 1803.9992 | -0.3774 | 1806.11 | 1780.9 | 0.0495 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 559.12 |  | 566.0085 | -1.217 | 566.18 | 548.47 | 0.3881 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 476.07 |  | 476.805 | -0.1542 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 143.585 |  | 143.9615 | -0.2615 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 649.33 |  | 652.0196 | -0.4125 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 214.05 |  | 215.7022 | -0.766 | 217.88 | 212.99 | 3.2049 | below_vwap | below_vwap,spread_too_wide |
| 19 | ETN | data_center_power_cooling | 412.71 |  | 413.395 | -0.1657 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | IWM | market_regime | 291.155 |  | 291.6698 | -0.1765 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.47 |  | 693.0982 | -0.2349 | 698.65 | 693.24 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.14 |  | 66.5686 | -0.6438 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.4 |  | 208.5633 | 0.4012 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| MSFT | cloud_ai_capex | 380.97 |  | 382.6768 | -0.446 | 391.71 | 387.245 | 0.2809 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.57 |  | 321.1052 | -0.1667 | 323.25 | 320.82 | 0.1591 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.505 |  | 319.5531 | -0.0151 | 324.42 | 320.24 | 0.0751 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 533.24 |  | 540.9162 | -1.4191 | 556.12 | 542.33 | 1.6597 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 416.605 |  | 416.7204 | -0.0277 | 420.72 | 412.69 | 0.3505 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.94 |  | 550.9567 | -0.5475 | 557.38 | 545.965 | 0.084 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.95 |  | 581.138 | -0.5486 | 585.98 | 576.635 | 0.0433 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.97 |  | 392.5392 | -0.3998 | 397.34 | 390.54 | 0.1893 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 995.99 |  | 991.5948 | 0.4432 | 999.04 | 964.86 | 0.4739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.11 |  | 209.7498 | -1.2585 | 213.785 | 207.665 | 0.3235 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 442.495 |  | 444.036 | -0.3471 | 450.07 | 438.55 | 0.4588 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.34 |  | 48.3551 | -0.0313 | 48.88 | 47.635 | 0.0621 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.09 |  | 31.694 | 1.2493 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 737.56 |  | 738.7752 | -0.1645 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.155 |  | 291.6698 | -0.1765 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.14 |  | 121.9759 | -1.5052 | 124.22 | 122.07 | 0.2164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.32 |  | 82.8458 | -0.6347 | 84.415 | 80.64 | 0.0607 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 303.01 |  | 306.2784 | -1.0671 | 311.13 | 303.96 | 1.3036 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.71 |  | 413.395 | -0.1657 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 649.33 |  | 652.0196 | -0.4125 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1027.01 |  | 1013.426 | 1.3404 | 1023.33 | 979.08 | 3.6816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.07 |  | 476.805 | -0.1542 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.585 |  | 143.9615 | -0.2615 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.15 |  | 176.7441 | 0.2297 | 177.84 | 173.19 | 0.7846 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.82 |  | 318.1509 | -1.047 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 844.92 |  | 858.0827 | -1.534 | 880.26 | 833 | 4.3424 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 409.11 |  | 408.2773 | 0.204 | 408.58 | 397.9 | 3.9427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.505 |  | 114.6397 | -0.9898 | 118.01 | 108.505 | 0.2907 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 326.77 |  | 327.7679 | -0.3044 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1797.19 |  | 1803.9992 | -0.3774 | 1806.11 | 1780.9 | 0.0495 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.12 |  | 566.0085 | -1.217 | 566.18 | 548.47 | 0.3881 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.78 |  | 321.1736 | -1.0566 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.05 |  | 215.7022 | -0.766 | 217.88 | 212.99 | 3.2049 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.68 |  | 372.2849 | -0.1625 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 288.63 |  | 294.6739 | -2.051 | 301.305 | 293.685 | 4.1437 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.85 |  | 65.2855 | -0.6671 | 67.455 | 65.81 | 4.7494 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.33 |  | 54.5883 | -0.4732 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.475 |  | 135.3363 | -0.6364 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.575 |  | 507.5122 | -0.3817 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.04 |  | 295.9124 | -0.2948 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.98 |  | 30.0587 | -0.2617 | 31.13 | 29.12 | 0.0667 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.99 |  | 41.7224 | -1.7554 | 43.21 | 40.51 | 0.0488 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0656 | 0.3092 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| SNDK | memory_hbm_storage | 1666.53 |  | 1641.2224 | 1.542 | 1651.355 | 1560 | 4.4404 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 565.33 |  | 564.281 | 0.1859 | 576.24 | 556.3 | 0.1433 | watch_only | none |
| STX | memory_hbm_storage | 922.34 |  | 924.6772 | -0.2528 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.335 |  | 234.3547 | -0.0084 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.03 |  | 604.0986 | 0.3197 | 614.15 | 605.39 | 1.1551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 280.52 |  | 279.6395 | 0.3149 | 283 | 276.24 | 0.2388 | watch_only | none |
| SKHY | memory_hbm_storage | 173.13 |  | 173.6161 | -0.28 | 177.88 | 168.18 | 0.2022 | below_vwap | below_vwap |
