# Intraday State

- Generated at: `2026-07-21T22:08:05+08:00`
- Market time ET: `2026-07-21T10:08:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 11, 'watch_only': 6, 'spread_too_wide_or_missing': 13, 'below_vwap': 22, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.5 |  | 704.901 | -0.0569 | 707.09 | 704.52 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 543.77 |  | 546.913 | -0.5747 | 550.77 | 545.11 | 0.0791 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.18 |  | 577.2291 | -0.355 | 582.03 | 576.57 | 0.0695 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.7 |  | 745.2314 | 0.0629 | 746.6 | 744.3 | 0.0335 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.45 |  | 23.2868 | 0.701 | 23.32 | 22.79 | 0.1279 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 42.08 |  | 41.3623 | 1.7352 | 41.65 | 40.435 | 0.0475 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 29.965 |  | 29.7133 | 0.8471 | 29.735 | 28.785 | 0.1001 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.7 |  | 745.2314 | 0.0629 | 746.6 | 744.3 | 0.0335 | watch_only | none |
| 2 | IWM | market_regime | 294.15 |  | 293.7099 | 0.1498 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| 3 | GOOGL | cloud_ai_capex | 349.935 |  | 349.5287 | 0.1162 | 350.985 | 347.69 | 0.0286 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 23.45 |  | 23.2868 | 0.701 | 23.32 | 22.79 | 0.1279 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 125.29 |  | 124.9756 | 0.2515 | 126.01 | 122.48 | 0.0958 | watch_only | none |
| 6 | SMCI | ai_server_oem | 24.625 |  | 24.5727 | 0.213 | 24.77 | 24.34 | 0.0406 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 399.59 |  | 399.3789 | 0.0528 | 401.45 | 396.36 | 0.1652 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.965 |  | 29.7133 | 0.8471 | 29.735 | 28.785 | 0.1001 | buy_precheck_manual_confirm | none |
| 9 | CIEN | ai_networking_optical | 401.77 |  | 400.3859 | 0.3457 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | COHR | ai_networking_optical | 305.585 |  | 304.8442 | 0.243 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | APD | industrial_gases | 299.575 |  | 298.6299 | 0.3165 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ANET | ai_networking_optical | 175.62 |  | 174.8557 | 0.4371 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | COHU | semiconductor_test_packaging | 54.45 |  | 54.2304 | 0.405 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | VRT | data_center_power_cooling | 299.77 |  | 299.7651 | 0.0016 | 305.09 | 299.13 | 2.165 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 140.43 |  | 140.4095 | 0.0146 | 142.15 | 140.105 | 4.3367 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | META | cloud_ai_capex | 648.44 |  | 647.3673 | 0.1657 | 655.425 | 643.54 | 1.7735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TER | semiconductor_test_packaging | 365.82 |  | 362.951 | 0.7905 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AAPL | mega_cap_platform | 324.58 |  | 323.8292 | 0.2318 | 325.59 | 322.63 | 0.5392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | IREN | high_beta_ai_infrastructure | 42.08 |  | 41.3623 | 1.7352 | 41.65 | 40.435 | 0.0475 | buy_precheck_manual_confirm | none |
| 20 | TSM | foundry | 415.685 |  | 416.8354 | -0.276 | 418.76 | 415.025 | 0.0674 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.45 |  | 23.2868 | 0.701 | 23.32 | 22.79 | 0.1279 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 42.08 |  | 41.3623 | 1.7352 | 41.65 | 40.435 | 0.0475 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 29.965 |  | 29.7133 | 0.8471 | 29.735 | 28.785 | 0.1001 | buy_precheck_manual_confirm | none |
| 4 | COHU | semiconductor_test_packaging | 54.45 |  | 54.2304 | 0.405 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | SPY | market_regime | 745.7 |  | 745.2314 | 0.0629 | 746.6 | 744.3 | 0.0335 | watch_only | none |
| 6 | AAOI | ai_networking_optical | 111.84 |  | 109.7381 | 1.9154 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | IWM | market_regime | 294.15 |  | 293.7099 | 0.1498 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| 8 | CRWV | gpu_cloud_ai_factory | 76.95 |  | 76.2245 | 0.9519 | 76.615 | 74.55 | 2.5341 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | GOOGL | cloud_ai_capex | 349.935 |  | 349.5287 | 0.1162 | 350.985 | 347.69 | 0.0286 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 399.59 |  | 399.3789 | 0.0528 | 401.45 | 396.36 | 0.1652 | watch_only | none |
| 11 | ORCL | cloud_ai_capex | 125.29 |  | 124.9756 | 0.2515 | 126.01 | 122.48 | 0.0958 | watch_only | none |
| 12 | SMCI | ai_server_oem | 24.625 |  | 24.5727 | 0.213 | 24.77 | 24.34 | 0.0406 | watch_only | none |
| 13 | TSM | foundry | 415.685 |  | 416.8354 | -0.276 | 418.76 | 415.025 | 0.0674 | below_vwap | below_vwap |
| 14 | AMD | ai_accelerator | 525 |  | 529.6497 | -0.8779 | 532.365 | 524.72 | 1.6648 | below_vwap | below_vwap,spread_too_wide |
| 15 | MU | memory_hbm_storage | 925.315 |  | 933.904 | -0.9197 | 944.99 | 923 | 0.4236 | below_vwap | below_vwap,spread_too_wide |
| 16 | ASML | semiconductor_equipment | 1792.41 |  | 1797.6293 | -0.2903 | 1804.54 | 1786.51 | 0.8285 | below_vwap | below_vwap,spread_too_wide |
| 17 | LITE | ai_networking_optical | 804.99 |  | 812.4218 | -0.9148 | 823.31 | 800.37 | 0.2435 | below_vwap | below_vwap |
| 18 | TT | data_center_power_cooling | 469.48 |  | 470.7562 | -0.2711 | 475.98 | 468.07 | 4.6626 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMAT | semiconductor_equipment | 559.59 |  | 559.9255 | -0.0599 | 564.91 | 552.71 | 0.1555 | below_vwap | below_vwap |
| 20 | PWR | data_center_power_cooling | 635.94 |  | 638.7456 | -0.4392 | 645.815 | 635.91 | 0.2359 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.5 |  | 704.901 | -0.0569 | 707.09 | 704.52 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.04 |  | 70.2751 | -0.3345 | 70.84 | 70.09 | 0.0143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 204.835 |  | 206.6293 | -0.8684 | 208.61 | 206.275 | 0.0195 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.59 |  | 399.3789 | 0.0528 | 401.45 | 396.36 | 0.1652 | watch_only | none |
| AAPL | mega_cap_platform | 324.58 |  | 323.8292 | 0.2318 | 325.59 | 322.63 | 0.5392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 349.935 |  | 349.5287 | 0.1162 | 350.985 | 347.69 | 0.0286 | watch_only | none |
| AMD | ai_accelerator | 525 |  | 529.6497 | -0.8779 | 532.365 | 524.72 | 1.6648 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.685 |  | 416.8354 | -0.276 | 418.76 | 415.025 | 0.0674 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 543.77 |  | 546.913 | -0.5747 | 550.77 | 545.11 | 0.0791 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.18 |  | 577.2291 | -0.355 | 582.03 | 576.57 | 0.0695 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 382.06 |  | 384.0332 | -0.5138 | 390.11 | 382.13 | 0.8035 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 925.315 |  | 933.904 | -0.9197 | 944.99 | 923 | 0.4236 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 204.825 |  | 206.3909 | -0.7587 | 208.61 | 205.31 | 1.2303 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.815 |  | 402.6766 | -0.4623 | 405.78 | 397.185 | 5.0821 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.1 |  | 46.2389 | -0.3004 | 46.685 | 45.835 | 0.0868 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.625 |  | 24.5727 | 0.213 | 24.77 | 24.34 | 0.0406 | watch_only | none |
| SPY | market_regime | 745.7 |  | 745.2314 | 0.0629 | 746.6 | 744.3 | 0.0335 | watch_only | none |
| IWM | market_regime | 294.15 |  | 293.7099 | 0.1498 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| ORCL | cloud_ai_capex | 125.29 |  | 124.9756 | 0.2515 | 126.01 | 122.48 | 0.0958 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 76.95 |  | 76.2245 | 0.9519 | 76.615 | 74.55 | 2.5341 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.77 |  | 299.7651 | 0.0016 | 305.09 | 299.13 | 2.165 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 404.69 |  | 405.7663 | -0.2652 | 411.01 | 404.21 | 4.8556 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 635.94 |  | 638.7456 | -0.4392 | 645.815 | 635.91 | 0.2359 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1097.31 |  | 1109.9958 | -1.1429 | 1140.63 | 1103.815 | 5.0596 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 469.48 |  | 470.7562 | -0.2711 | 475.98 | 468.07 | 4.6626 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.43 |  | 140.4095 | 0.0146 | 142.15 | 140.105 | 4.3367 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.62 |  | 174.8557 | 0.4371 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 305.585 |  | 304.8442 | 0.243 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 804.99 |  | 812.4218 | -0.9148 | 823.31 | 800.37 | 0.2435 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 401.77 |  | 400.3859 | 0.3457 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 111.84 |  | 109.7381 | 1.9154 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 323.175 |  | 325.7658 | -0.7953 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1792.41 |  | 1797.6293 | -0.2903 | 1804.54 | 1786.51 | 0.8285 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 559.59 |  | 559.9255 | -0.0599 | 564.91 | 552.71 | 0.1555 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 315.495 |  | 318.8958 | -1.0664 | 328.135 | 317.17 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.945 |  | 216.0853 | -0.0649 | 220.76 | 214.41 | 1.116 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 365.82 |  | 362.951 | 0.7905 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.5 |  | 293.2363 | -0.5921 | 296.68 | 291.43 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.27 |  | 65.3329 | -0.0963 | 66.54 | 65 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.45 |  | 54.2304 | 0.405 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.7 |  | 140.3626 | -0.4721 | 142.09 | 139.44 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 336.06 |  | 337.8785 | -0.5382 | 340.205 | 336.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 509.17 |  | 509.431 | -0.0512 | 512.83 | 507.675 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 299.575 |  | 298.6299 | 0.3165 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.965 |  | 29.7133 | 0.8471 | 29.735 | 28.785 | 0.1001 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.08 |  | 41.3623 | 1.7352 | 41.65 | 40.435 | 0.0475 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.45 |  | 23.2868 | 0.701 | 23.32 | 22.79 | 0.1279 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1512.1 |  | 1521.0885 | -0.5909 | 1540.85 | 1490.29 | 3.6373 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 531.55 |  | 533.536 | -0.3722 | 533.56 | 517.335 | 0.1148 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 861.43 |  | 864.5577 | -0.3618 | 866.73 | 845.78 | 1.696 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 247.46 |  | 247.8124 | -0.1422 | 248.915 | 247.32 | 0.0727 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.44 |  | 647.3673 | 0.1657 | 655.425 | 643.54 | 1.7735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 282.965 |  | 280.1104 | 1.0191 | 286.39 | 275.86 | 3.9581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 163.525 |  | 163.7896 | -0.1616 | 165.88 | 160.77 | 2.3605 | below_vwap | below_vwap,spread_too_wide |
