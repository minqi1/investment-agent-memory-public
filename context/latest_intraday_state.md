# Intraday State

- Generated at: `2026-07-22T00:37:43+08:00`
- Market time ET: `2026-07-21T12:37:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 19, 'below_opening_15m_low': 3, 'below_vwap': 5, 'watch_only': 2, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.01 |  | 706.289 | 0.3853 | 707.09 | 704.52 | 0.0324 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 552.89 |  | 547.7598 | 0.9366 | 550.77 | 545.11 | 0.0543 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.295 |  | 579.448 | 0.6639 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.61 |  | 746.4815 | 0.2851 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.365 |  | 418.5505 | 0.9114 | 418.76 | 415.025 | 0.1918 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.295 |  | 579.448 | 0.6639 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.89 |  | 547.7598 | 0.9366 | 550.77 | 545.11 | 0.0543 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.01 |  | 706.289 | 0.3853 | 707.09 | 704.52 | 0.0324 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.61 |  | 746.4815 | 0.2851 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 973.15 |  | 943.5448 | 3.1377 | 944.99 | 923 | 0.0997 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.91 |  | 294.3118 | 0.543 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | DELL | ai_server_oem | 407.08 |  | 403.0256 | 1.006 | 405.78 | 397.185 | 0.2383 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.9 |  | 46.4505 | 0.9676 | 46.685 | 45.835 | 0.064 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 548.9 |  | 538.2353 | 1.9814 | 533.56 | 517.335 | 0.2733 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1567.35 |  | 1534.2954 | 2.1544 | 1540.85 | 1490.29 | 0.0861 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.315 |  | 23.8271 | 2.0479 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 13 | SKHY | memory_hbm_storage | 166.78 |  | 165.1493 | 0.9874 | 165.88 | 160.77 | 0.2278 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 41.89 |  | 41.714 | 0.4219 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 15 | AAPL | mega_cap_platform | 328.565 |  | 325.6902 | 0.8827 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 16 | AAOI | ai_networking_optical | 117.52 |  | 114.5369 | 2.6045 | 109.39 | 107.58 | 0.3489 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 25.335 |  | 24.8084 | 2.1227 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.49 |  | 30.1579 | 1.1012 | 29.735 | 28.785 | 0.0656 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.41 |  | 70.6745 | 1.0407 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.61 |  | 746.4815 | 0.2851 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.295 |  | 579.448 | 0.6639 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.01 |  | 706.289 | 0.3853 | 707.09 | 704.52 | 0.0324 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 295.91 |  | 294.3118 | 0.543 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 349.885 |  | 349.1494 | 0.2107 | 350.985 | 347.69 | 0.02 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 41.89 |  | 41.714 | 0.4219 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 218.045 |  | 216.3241 | 0.7955 | 220.76 | 214.41 | 0.133 | watch_only | none |
| 8 | SOXX | semiconductor_index | 552.89 |  | 547.7598 | 0.9366 | 550.77 | 545.11 | 0.0543 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.9 |  | 46.4505 | 0.9676 | 46.685 | 45.835 | 0.064 | buy_precheck_manual_confirm | none |
| 10 | DELL | ai_server_oem | 407.08 |  | 403.0256 | 1.006 | 405.78 | 397.185 | 0.2383 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 422.365 |  | 418.5505 | 0.9114 | 418.76 | 415.025 | 0.1918 | buy_precheck_manual_confirm | none |
| 12 | SKHY | memory_hbm_storage | 166.78 |  | 165.1493 | 0.9874 | 165.88 | 160.77 | 0.2278 | buy_precheck_manual_confirm | none |
| 13 | AAPL | mega_cap_platform | 328.565 |  | 325.6902 | 0.8827 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 14 | ETN | data_center_power_cooling | 407.01 |  | 405.9888 | 0.2515 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APD | industrial_gases | 298.88 |  | 298.7679 | 0.0375 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 142.57 |  | 141.4681 | 0.7789 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | APLD | high_beta_ai_infrastructure | 30.49 |  | 30.1579 | 1.1012 | 29.735 | 28.785 | 0.0656 | buy_precheck_manual_confirm | none |
| 18 | AVGO | custom_silicon_networking | 385.44 |  | 384.5482 | 0.2319 | 390.11 | 382.13 | 2.1378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LRCX | semiconductor_equipment | 321.97 |  | 319.7359 | 0.6987 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TT | data_center_power_cooling | 471.84 |  | 469.3319 | 0.5344 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.365 |  | 418.5505 | 0.9114 | 418.76 | 415.025 | 0.1918 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.295 |  | 579.448 | 0.6639 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.89 |  | 547.7598 | 0.9366 | 550.77 | 545.11 | 0.0543 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.01 |  | 706.289 | 0.3853 | 707.09 | 704.52 | 0.0324 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.61 |  | 746.4815 | 0.2851 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 973.15 |  | 943.5448 | 3.1377 | 944.99 | 923 | 0.0997 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.91 |  | 294.3118 | 0.543 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | DELL | ai_server_oem | 407.08 |  | 403.0256 | 1.006 | 405.78 | 397.185 | 0.2383 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.9 |  | 46.4505 | 0.9676 | 46.685 | 45.835 | 0.064 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 548.9 |  | 538.2353 | 1.9814 | 533.56 | 517.335 | 0.2733 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1567.35 |  | 1534.2954 | 2.1544 | 1540.85 | 1490.29 | 0.0861 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.315 |  | 23.8271 | 2.0479 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 13 | SKHY | memory_hbm_storage | 166.78 |  | 165.1493 | 0.9874 | 165.88 | 160.77 | 0.2278 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 41.89 |  | 41.714 | 0.4219 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| 15 | AAPL | mega_cap_platform | 328.565 |  | 325.6902 | 0.8827 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 16 | AAOI | ai_networking_optical | 117.52 |  | 114.5369 | 2.6045 | 109.39 | 107.58 | 0.3489 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 25.335 |  | 24.8084 | 2.1227 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.49 |  | 30.1579 | 1.1012 | 29.735 | 28.785 | 0.0656 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.41 |  | 70.6745 | 1.0407 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 20 | AMD | ai_accelerator | 537.61 |  | 531.5667 | 1.1369 | 532.365 | 524.72 | 0.7124 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.01 |  | 706.289 | 0.3853 | 707.09 | 704.52 | 0.0324 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.41 |  | 70.6745 | 1.0407 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205 |  | 206.0556 | -0.5123 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.48 |  | 399.2275 | -0.1872 | 401.45 | 396.36 | 0.0301 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.565 |  | 325.6902 | 0.8827 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.885 |  | 349.1494 | 0.2107 | 350.985 | 347.69 | 0.02 | watch_only | none |
| AMD | ai_accelerator | 537.61 |  | 531.5667 | 1.1369 | 532.365 | 524.72 | 0.7124 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.365 |  | 418.5505 | 0.9114 | 418.76 | 415.025 | 0.1918 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.89 |  | 547.7598 | 0.9366 | 550.77 | 545.11 | 0.0543 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.295 |  | 579.448 | 0.6639 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.44 |  | 384.5482 | 0.2319 | 390.11 | 382.13 | 2.1378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 973.15 |  | 943.5448 | 3.1377 | 944.99 | 923 | 0.0997 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 209.62 |  | 207.3906 | 1.075 | 208.61 | 205.31 | 0.7013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 407.08 |  | 403.0256 | 1.006 | 405.78 | 397.185 | 0.2383 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 46.9 |  | 46.4505 | 0.9676 | 46.685 | 45.835 | 0.064 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.335 |  | 24.8084 | 2.1227 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.61 |  | 746.4815 | 0.2851 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.91 |  | 294.3118 | 0.543 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.09 |  | 125.0932 | 0.7968 | 126.01 | 122.48 | 0.4362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 79.49 |  | 77.5749 | 2.4687 | 76.615 | 74.55 | 3.8747 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 304.71 |  | 300.8887 | 1.27 | 305.09 | 299.13 | 2.0938 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.01 |  | 405.9888 | 0.2515 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 640.17 |  | 637.3121 | 0.4484 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1090.55 |  | 1097.8588 | -0.6657 | 1140.63 | 1103.815 | 0.6941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 471.84 |  | 469.3319 | 0.5344 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.57 |  | 141.4681 | 0.7789 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.66 |  | 175.2713 | -0.3488 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 317.55 |  | 310.0006 | 2.4353 | 309.72 | 302.3 | 3.9899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 833.72 |  | 821.6858 | 1.4646 | 823.31 | 800.37 | 2.7587 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 410.03 |  | 405.2252 | 1.1857 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 117.52 |  | 114.5369 | 2.6045 | 109.39 | 107.58 | 0.3489 | buy_precheck_manual_confirm | none |
| ALAB | ai_networking_optical | 325.42 |  | 325.9987 | -0.1775 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1817.47 |  | 1807.57 | 0.5477 | 1804.54 | 1786.51 | 0.9403 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 570.44 |  | 563.3282 | 1.2625 | 564.91 | 552.71 | 0.6521 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.97 |  | 319.7359 | 0.6987 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 218.045 |  | 216.3241 | 0.7955 | 220.76 | 214.41 | 0.133 | watch_only | none |
| TER | semiconductor_test_packaging | 375.73 |  | 368.9101 | 1.8487 | 365.97 | 356.39 | 1.3866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 299.685 |  | 295.5981 | 1.3826 | 296.68 | 291.36 | 4.0976 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.545 |  | 65.7986 | 1.1343 | 66.54 | 65 | 0.3907 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.82 |  | 54.8344 | 1.7973 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 141.96 |  | 140.9393 | 0.7242 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 344.67 |  | 339.1917 | 1.6151 | 340.205 | 336.3 | 4.3868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 504.49 |  | 506.5893 | -0.4144 | 512.83 | 507.675 | 3.7543 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 298.88 |  | 298.7679 | 0.0375 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.49 |  | 30.1579 | 1.1012 | 29.735 | 28.785 | 0.0656 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.89 |  | 41.714 | 0.4219 | 41.65 | 40.435 | 0.0716 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.315 |  | 23.8271 | 2.0479 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1567.35 |  | 1534.2954 | 2.1544 | 1540.85 | 1490.29 | 0.0861 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 548.9 |  | 538.2353 | 1.9814 | 533.56 | 517.335 | 0.2733 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 892.65 |  | 874.3618 | 2.0916 | 866.73 | 845.78 | 1.0206 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.55 |  | 247.7249 | -0.0706 | 248.915 | 247.32 | 0.0081 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.61 |  | 647.4087 | 0.0311 | 655.425 | 643.54 | 1.118 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 290.595 |  | 285.4825 | 1.7908 | 286.39 | 275.86 | 3.1934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.78 |  | 165.1493 | 0.9874 | 165.88 | 160.77 | 0.2278 | buy_precheck_manual_confirm | none |
