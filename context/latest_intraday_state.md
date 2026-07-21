# Intraday State

- Generated at: `2026-07-21T22:00:17+08:00`
- Market time ET: `2026-07-21T10:00:18-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'below_opening_15m_low': 7, 'watch_only': 10, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 14, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.81 |  | 705.0049 | -0.0277 | 707.09 | 704.52 | 0.0525 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 544.72 |  | 547.5476 | -0.5164 | 550.77 | 545.11 | 0.0973 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.4 |  | 577.3 | -0.1559 | 582.03 | 576.57 | 0.0625 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.325 |  | 745.192 | 0.0178 | 746.6 | 744.3 | 0.0698 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.385 |  | 23.2088 | 0.7591 | 23.32 | 22.79 | 0.171 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 42.08 |  | 41.278 | 1.943 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6071 | 1.6309 | 29.735 | 28.785 | 0.2991 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.325 |  | 745.192 | 0.0178 | 746.6 | 744.3 | 0.0698 | watch_only | none |
| 2 | META | cloud_ai_capex | 648.37 |  | 647.3036 | 0.1647 | 655.425 | 643.54 | 0.0509 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 400.01 |  | 399.2979 | 0.1783 | 401.45 | 396.36 | 0.0675 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 23.385 |  | 23.2088 | 0.7591 | 23.32 | 22.79 | 0.171 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 324.035 |  | 323.7556 | 0.0863 | 325.59 | 322.63 | 0.0864 | watch_only | none |
| 6 | AMAT | semiconductor_equipment | 560.32 |  | 559.9985 | 0.0574 | 564.91 | 552.71 | 0.1642 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 349.83 |  | 349.5035 | 0.0934 | 350.985 | 347.69 | 0.2201 | watch_only | none |
| 8 | LIN | industrial_gases | 509.57 |  | 509.53 | 0.0079 | 512.83 | 507.675 | 0.21 | watch_only | none |
| 9 | SMCI | ai_server_oem | 24.68 |  | 24.5715 | 0.4414 | 24.77 | 24.34 | 0.081 | watch_only | none |
| 10 | SNDK | memory_hbm_storage | 1527.655 |  | 1521.3588 | 0.4139 | 1540.85 | 1490.29 | 0.1826 | watch_only | none |
| 11 | ORCL | cloud_ai_capex | 125.74 |  | 124.8937 | 0.6776 | 126.01 | 122.48 | 0.1511 | watch_only | none |
| 12 | DELL | ai_server_oem | 403.67 |  | 402.7047 | 0.2397 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | COHR | ai_networking_optical | 305.635 |  | 304.9108 | 0.2375 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | APD | industrial_gases | 298.56 |  | 298.5353 | 0.0083 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ASML | semiconductor_equipment | 1800.61 |  | 1797.1354 | 0.1933 | 1804.54 | 1786.51 | 0.8664 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TER | semiconductor_test_packaging | 365.255 |  | 362.5147 | 0.7559 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SKHY | memory_hbm_storage | 163.96 |  | 163.8458 | 0.0697 | 165.88 | 160.77 | 1.7077 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | IREN | high_beta_ai_infrastructure | 42.08 |  | 41.278 | 1.943 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| 19 | LITE | ai_networking_optical | 816.93 |  | 812.6027 | 0.5325 | 823.31 | 800.37 | 0.7981 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6071 | 1.6309 | 29.735 | 28.785 | 0.2991 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.385 |  | 23.2088 | 0.7591 | 23.32 | 22.79 | 0.171 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 42.08 |  | 41.278 | 1.943 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| 3 | APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6071 | 1.6309 | 29.735 | 28.785 | 0.2991 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 176.5 |  | 174.6347 | 1.0681 | 176.06 | 172.32 | 4.7989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | CIEN | ai_networking_optical | 404.045 |  | 400.0847 | 0.9899 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | STX | memory_hbm_storage | 873.57 |  | 863.6922 | 1.1437 | 866.73 | 845.78 | 2.8218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | WDC | memory_hbm_storage | 538.35 |  | 532.8256 | 1.0368 | 533.56 | 517.335 | 0.3919 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SPY | market_regime | 745.325 |  | 745.192 | 0.0178 | 746.6 | 744.3 | 0.0698 | watch_only | none |
| 9 | AMAT | semiconductor_equipment | 560.32 |  | 559.9985 | 0.0574 | 564.91 | 552.71 | 0.1642 | watch_only | none |
| 10 | AAOI | ai_networking_optical | 111.395 |  | 109.4716 | 1.757 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | CRWV | gpu_cloud_ai_factory | 76.69 |  | 76.0845 | 0.7958 | 76.615 | 74.55 | 4.4334 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | META | cloud_ai_capex | 648.37 |  | 647.3036 | 0.1647 | 655.425 | 643.54 | 0.0509 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 349.83 |  | 349.5035 | 0.0934 | 350.985 | 347.69 | 0.2201 | watch_only | none |
| 14 | SNDK | memory_hbm_storage | 1527.655 |  | 1521.3588 | 0.4139 | 1540.85 | 1490.29 | 0.1826 | watch_only | none |
| 15 | LIN | industrial_gases | 509.57 |  | 509.53 | 0.0079 | 512.83 | 507.675 | 0.21 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 400.01 |  | 399.2979 | 0.1783 | 401.45 | 396.36 | 0.0675 | watch_only | none |
| 17 | AAPL | mega_cap_platform | 324.035 |  | 323.7556 | 0.0863 | 325.59 | 322.63 | 0.0864 | watch_only | none |
| 18 | ORCL | cloud_ai_capex | 125.74 |  | 124.8937 | 0.6776 | 126.01 | 122.48 | 0.1511 | watch_only | none |
| 19 | SMCI | ai_server_oem | 24.68 |  | 24.5715 | 0.4414 | 24.77 | 24.34 | 0.081 | watch_only | none |
| 20 | TSM | foundry | 416.12 |  | 417.1879 | -0.256 | 418.76 | 415.025 | 0.1033 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.81 |  | 705.0049 | -0.0277 | 707.09 | 704.52 | 0.0525 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.04 |  | 70.3119 | -0.3867 | 70.84 | 70.09 | 0.0143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 205.44 |  | 206.7611 | -0.6389 | 208.61 | 206.275 | 1.7864 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 400.01 |  | 399.2979 | 0.1783 | 401.45 | 396.36 | 0.0675 | watch_only | none |
| AAPL | mega_cap_platform | 324.035 |  | 323.7556 | 0.0863 | 325.59 | 322.63 | 0.0864 | watch_only | none |
| GOOGL | cloud_ai_capex | 349.83 |  | 349.5035 | 0.0934 | 350.985 | 347.69 | 0.2201 | watch_only | none |
| AMD | ai_accelerator | 526.37 |  | 529.8886 | -0.664 | 532.365 | 524.72 | 1.8903 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 416.12 |  | 417.1879 | -0.256 | 418.76 | 415.025 | 0.1033 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 544.72 |  | 547.5476 | -0.5164 | 550.77 | 545.11 | 0.0973 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.4 |  | 577.3 | -0.1559 | 582.03 | 576.57 | 0.0625 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.25 |  | 384.168 | -0.7596 | 390.11 | 382.13 | 0.8052 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 932.35 |  | 934.5596 | -0.2364 | 944.99 | 923 | 0.9063 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 205.66 |  | 206.4875 | -0.4007 | 208.61 | 205.31 | 0.6516 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.67 |  | 402.7047 | 0.2397 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.195 |  | 46.2972 | -0.2208 | 46.685 | 45.835 | 0.1082 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.68 |  | 24.5715 | 0.4414 | 24.77 | 24.34 | 0.081 | watch_only | none |
| SPY | market_regime | 745.325 |  | 745.192 | 0.0178 | 746.6 | 744.3 | 0.0698 | watch_only | none |
| IWM | market_regime | 293.495 |  | 293.6799 | -0.063 | 294.51 | 292.72 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.74 |  | 124.8937 | 0.6776 | 126.01 | 122.48 | 0.1511 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 76.69 |  | 76.0845 | 0.7958 | 76.615 | 74.55 | 4.4334 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.1 |  | 299.9986 | -0.2995 | 305.09 | 299.13 | 0.3778 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 404.795 |  | 405.9532 | -0.2853 | 411.01 | 404.21 | 5.0075 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 639.18 |  | 639.4393 | -0.0406 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1097.62 |  | 1112.6182 | -1.348 | 1140.63 | 1103.815 | 4.6154 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 469.875 |  | 471.2009 | -0.2814 | 475.98 | 468.07 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.28 |  | 140.4455 | -0.1178 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.5 |  | 174.6347 | 1.0681 | 176.06 | 172.32 | 4.7989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 305.635 |  | 304.9108 | 0.2375 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 816.93 |  | 812.6027 | 0.5325 | 823.31 | 800.37 | 0.7981 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 404.045 |  | 400.0847 | 0.9899 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 111.395 |  | 109.4716 | 1.757 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 324.89 |  | 326.5372 | -0.5044 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1800.61 |  | 1797.1354 | 0.1933 | 1804.54 | 1786.51 | 0.8664 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.32 |  | 559.9985 | 0.0574 | 564.91 | 552.71 | 0.1642 | watch_only | none |
| LRCX | semiconductor_equipment | 317.525 |  | 319.8479 | -0.7262 | 328.135 | 317.17 | 4.7681 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 215.94 |  | 216.1423 | -0.0936 | 220.76 | 214.41 | 0.0787 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 365.255 |  | 362.5147 | 0.7559 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.89 |  | 293.3024 | -0.4816 | 296.68 | 291.43 | 1.319 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.2 |  | 65.3191 | -0.1824 | 66.54 | 65 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.145 |  | 54.2068 | -0.114 | 54.41 | 54.03 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 140.38 |  | 140.3891 | -0.0065 | 142.09 | 139.44 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 336.35 |  | 338.0132 | -0.492 | 340.205 | 336.3 | 0.5827 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 509.57 |  | 509.53 | 0.0079 | 512.83 | 507.675 | 0.21 | watch_only | none |
| APD | industrial_gases | 298.56 |  | 298.5353 | 0.0083 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.09 |  | 29.6071 | 1.6309 | 29.735 | 28.785 | 0.2991 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.08 |  | 41.278 | 1.943 | 41.65 | 40.435 | 0.0713 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.385 |  | 23.2088 | 0.7591 | 23.32 | 22.79 | 0.171 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1527.655 |  | 1521.3588 | 0.4139 | 1540.85 | 1490.29 | 0.1826 | watch_only | none |
| WDC | memory_hbm_storage | 538.35 |  | 532.8256 | 1.0368 | 533.56 | 517.335 | 0.3919 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 873.57 |  | 863.6922 | 1.1437 | 866.73 | 845.78 | 2.8218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.65 |  | 247.8932 | -0.0981 | 248.915 | 247.32 | 0.6784 | below_vwap | below_vwap,spread_too_wide |
| META | cloud_ai_capex | 648.37 |  | 647.3036 | 0.1647 | 655.425 | 643.54 | 0.0509 | watch_only | none |
| ARM | ai_accelerator | 281.77 |  | 279.4889 | 0.8162 | 286.39 | 275.86 | 4.6882 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 163.96 |  | 163.8458 | 0.0697 | 165.88 | 160.77 | 1.7077 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
