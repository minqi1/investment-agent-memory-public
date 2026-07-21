# Intraday State

- Generated at: `2026-07-21T22:51:04+08:00`
- Market time ET: `2026-07-21T10:51:07-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_opening_15m_low': 3, 'spread_too_wide_or_missing': 28, 'manual_confirm_candidate': 7, 'below_vwap': 7, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.795 |  | 704.9515 | 0.2615 | 707.09 | 704.52 | 0.0241 | watch_only | none |
| SOXX | semiconductor_index | 547.58 |  | 546.2746 | 0.239 | 550.77 | 545.11 | 0.0657 | watch_only | none |
| SMH | semiconductor_index | 578.8 |  | 577.1712 | 0.2822 | 582.03 | 576.57 | 0.0466 | watch_only | none |
| SPY | market_regime | 746.935 |  | 745.6058 | 0.1783 | 746.6 | 744.3 | 0.0361 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.935 |  | 745.6058 | 0.1783 | 746.6 | 744.3 | 0.0361 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.74 |  | 294.0172 | 0.2458 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 23.77 |  | 23.4607 | 1.3182 | 23.32 | 22.79 | 0.0841 | buy_precheck_manual_confirm | none |
| 4 | IREN | high_beta_ai_infrastructure | 41.915 |  | 41.5427 | 0.8962 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 326.925 |  | 324.5309 | 0.7377 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.88 |  | 24.6254 | 1.034 | 24.77 | 24.34 | 0.0402 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.93 |  | 29.7899 | 0.4702 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.935 |  | 745.6058 | 0.1783 | 746.6 | 744.3 | 0.0361 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.74 |  | 294.0172 | 0.2458 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 578.8 |  | 577.1712 | 0.2822 | 582.03 | 576.57 | 0.0466 | watch_only | none |
| 4 | AVGO | custom_silicon_networking | 384.53 |  | 383.872 | 0.1714 | 390.11 | 382.13 | 0.0546 | watch_only | none |
| 5 | SOXX | semiconductor_index | 547.58 |  | 546.2746 | 0.239 | 550.77 | 545.11 | 0.0657 | watch_only | none |
| 6 | QQQ | market_regime | 706.795 |  | 704.9515 | 0.2615 | 707.09 | 704.52 | 0.0241 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 248.425 |  | 247.7183 | 0.2853 | 248.915 | 247.32 | 0.0523 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 326.925 |  | 324.5309 | 0.7377 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 125.33 |  | 125.0244 | 0.2445 | 126.01 | 122.48 | 0.0638 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.93 |  | 29.7899 | 0.4702 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 46.5 |  | 46.2767 | 0.4826 | 46.685 | 45.835 | 0.086 | watch_only | none |
| 12 | TSM | foundry | 418.315 |  | 416.8067 | 0.3619 | 418.76 | 415.025 | 0.2869 | watch_only | none |
| 13 | AMAT | semiconductor_equipment | 564.59 |  | 561.3385 | 0.5792 | 564.91 | 552.71 | 0.2551 | watch_only | none |
| 14 | IREN | high_beta_ai_infrastructure | 41.915 |  | 41.5427 | 0.8962 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 24.88 |  | 24.6254 | 1.034 | 24.77 | 24.34 | 0.0402 | buy_precheck_manual_confirm | none |
| 16 | ANET | ai_networking_optical | 176.335 |  | 175.1359 | 0.6847 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | CORZ | high_beta_ai_infrastructure | 23.77 |  | 23.4607 | 1.3182 | 23.32 | 22.79 | 0.0841 | buy_precheck_manual_confirm | none |
| 18 | ASML | semiconductor_equipment | 1804.19 |  | 1798.181 | 0.3342 | 1804.54 | 1786.51 | 0.8109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 206.32 |  | 206.1237 | 0.0952 | 208.61 | 205.31 | 0.538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | KLAC | semiconductor_equipment | 216.06 |  | 215.8224 | 0.1101 | 220.76 | 214.41 | 1.1525 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.935 |  | 745.6058 | 0.1783 | 746.6 | 744.3 | 0.0361 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.74 |  | 294.0172 | 0.2458 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 23.77 |  | 23.4607 | 1.3182 | 23.32 | 22.79 | 0.0841 | buy_precheck_manual_confirm | none |
| 4 | IREN | high_beta_ai_infrastructure | 41.915 |  | 41.5427 | 0.8962 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 326.925 |  | 324.5309 | 0.7377 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.88 |  | 24.6254 | 1.034 | 24.77 | 24.34 | 0.0402 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.93 |  | 29.7899 | 0.4702 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 176.335 |  | 175.1359 | 0.6847 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | LITE | ai_networking_optical | 825.38 |  | 815.9319 | 1.158 | 823.31 | 800.37 | 1.2576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | CIEN | ai_networking_optical | 405.4 |  | 402.2531 | 0.7823 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | STX | memory_hbm_storage | 873.51 |  | 865.0035 | 0.9834 | 866.73 | 845.78 | 2.5586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | WDC | memory_hbm_storage | 540 |  | 534.3847 | 1.0508 | 533.56 | 517.335 | 0.837 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TER | semiconductor_test_packaging | 371.21 |  | 365.6867 | 1.5104 | 365.97 | 356.39 | 3.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 418.315 |  | 416.8067 | 0.3619 | 418.76 | 415.025 | 0.2869 | watch_only | none |
| 15 | SMH | semiconductor_index | 578.8 |  | 577.1712 | 0.2822 | 582.03 | 576.57 | 0.0466 | watch_only | none |
| 16 | ONTO | semiconductor_test_packaging | 296.88 |  | 293.3669 | 1.1975 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 384.53 |  | 383.872 | 0.1714 | 390.11 | 382.13 | 0.0546 | watch_only | none |
| 18 | COHU | semiconductor_test_packaging | 55.01 |  | 54.6161 | 0.7212 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SOXX | semiconductor_index | 547.58 |  | 546.2746 | 0.239 | 550.77 | 545.11 | 0.0657 | watch_only | none |
| 20 | QQQ | market_regime | 706.795 |  | 704.9515 | 0.2615 | 707.09 | 704.52 | 0.0241 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.795 |  | 704.9515 | 0.2615 | 707.09 | 704.52 | 0.0241 | watch_only | none |
| TQQQ | leveraged_tool | 70.76 |  | 70.3235 | 0.6207 | 70.84 | 70.09 | 0.0141 | watch_only | none |
| NVDA | ai_accelerator | 205.23 |  | 206.1509 | -0.4467 | 208.61 | 206.275 | 0.1218 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.665 |  | 399.6998 | 0.2415 | 401.45 | 396.36 | 0.4493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 326.925 |  | 324.5309 | 0.7377 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.895 |  | 349.3509 | -0.1305 | 350.985 | 347.69 | 0.1433 | below_vwap | below_vwap |
| AMD | ai_accelerator | 529.18 |  | 529.5254 | -0.0652 | 532.365 | 524.72 | 0.2343 | below_vwap | below_vwap |
| TSM | foundry | 418.315 |  | 416.8067 | 0.3619 | 418.76 | 415.025 | 0.2869 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.58 |  | 546.2746 | 0.239 | 550.77 | 545.11 | 0.0657 | watch_only | none |
| SMH | semiconductor_index | 578.8 |  | 577.1712 | 0.2822 | 582.03 | 576.57 | 0.0466 | watch_only | none |
| AVGO | custom_silicon_networking | 384.53 |  | 383.872 | 0.1714 | 390.11 | 382.13 | 0.0546 | watch_only | none |
| MU | memory_hbm_storage | 937.17 |  | 931.3358 | 0.6264 | 944.99 | 923 | 1.3199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 206.32 |  | 206.1237 | 0.0952 | 208.61 | 205.31 | 0.538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.96 |  | 402.3947 | 0.1405 | 405.78 | 397.185 | 1.3897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.5 |  | 46.2767 | 0.4826 | 46.685 | 45.835 | 0.086 | watch_only | none |
| SMCI | ai_server_oem | 24.88 |  | 24.6254 | 1.034 | 24.77 | 24.34 | 0.0402 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.935 |  | 745.6058 | 0.1783 | 746.6 | 744.3 | 0.0361 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.74 |  | 294.0172 | 0.2458 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.33 |  | 125.0244 | 0.2445 | 126.01 | 122.48 | 0.0638 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77 |  | 76.6296 | 0.4834 | 76.615 | 74.55 | 4.5455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 301.04 |  | 299.8341 | 0.4022 | 305.09 | 299.13 | 0.3953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.57 |  | 405.6571 | -0.0215 | 411.01 | 404.21 | 0.2268 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 634.92 |  | 636.7777 | -0.2917 | 645.815 | 635.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1083.01 |  | 1102.2557 | -1.746 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 468.19 |  | 469.1505 | -0.2047 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 141.24 |  | 140.4876 | 0.5356 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.335 |  | 175.1359 | 0.6847 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 309.27 |  | 306.08 | 1.0422 | 309.72 | 302.3 | 4.7434 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 825.38 |  | 815.9319 | 1.158 | 823.31 | 800.37 | 1.2576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 405.4 |  | 402.2531 | 0.7823 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 113.03 |  | 111.4942 | 1.3775 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 326.58 |  | 324.6974 | 0.5798 | 329.97 | 323.92 | 0.395 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1804.19 |  | 1798.181 | 0.3342 | 1804.54 | 1786.51 | 0.8109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 564.59 |  | 561.3385 | 0.5792 | 564.91 | 552.71 | 0.2551 | watch_only | none |
| LRCX | semiconductor_equipment | 320.92 |  | 318.36 | 0.8041 | 328.135 | 317.17 | 3.4401 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.06 |  | 215.8224 | 0.1101 | 220.76 | 214.41 | 1.1525 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.21 |  | 365.6867 | 1.5104 | 365.97 | 356.39 | 3.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.88 |  | 293.3669 | 1.1975 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.27 |  | 65.3959 | 1.3366 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.01 |  | 54.6161 | 0.7212 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 140.69 |  | 140.0934 | 0.4258 | 142.09 | 139.41 | 3.7671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 340.16 |  | 337.7146 | 0.7241 | 340.205 | 336.3 | 3.8599 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 508.74 |  | 509.1831 | -0.087 | 512.83 | 507.675 | 0.914 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 299 |  | 299.4562 | -0.1523 | 301.84 | 296.5 | 0.1204 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 29.93 |  | 29.7899 | 0.4702 | 29.735 | 28.785 | 0.0334 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.915 |  | 41.5427 | 0.8962 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.77 |  | 23.4607 | 1.3182 | 23.32 | 22.79 | 0.0841 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1531.53 |  | 1519.1218 | 0.8168 | 1540.85 | 1490.29 | 2.5981 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 540 |  | 534.3847 | 1.0508 | 533.56 | 517.335 | 0.837 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 873.51 |  | 865.0035 | 0.9834 | 866.73 | 845.78 | 2.5586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.425 |  | 247.7183 | 0.2853 | 248.915 | 247.32 | 0.0523 | watch_only | none |
| META | cloud_ai_capex | 649.225 |  | 647.288 | 0.2992 | 655.425 | 643.54 | 1.8176 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 286.25 |  | 283.5891 | 0.9383 | 286.39 | 275.86 | 1.3205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 164.62 |  | 164.022 | 0.3646 | 165.88 | 160.77 | 1.1481 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
