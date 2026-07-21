# Intraday State

- Generated at: `2026-07-21T22:31:24+08:00`
- Market time ET: `2026-07-21T10:31:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'below_opening_15m_low': 3, 'manual_confirm_candidate': 9, 'below_vwap': 11, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.39 |  | 704.6458 | 0.2475 | 707.09 | 704.52 | 0.0142 | watch_only | none |
| SOXX | semiconductor_index | 546.51 |  | 546.0065 | 0.0922 | 550.77 | 545.11 | 0.1043 | watch_only | none |
| SMH | semiconductor_index | 577.835 |  | 576.9028 | 0.1616 | 582.03 | 576.57 | 0.0536 | watch_only | none |
| SPY | market_regime | 746.96 |  | 745.3754 | 0.2126 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.96 |  | 745.3754 | 0.2126 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.9 |  | 293.913 | 0.3358 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 3 | ARM | ai_accelerator | 287.42 |  | 283.2308 | 1.4791 | 286.39 | 275.86 | 0.2783 | buy_precheck_manual_confirm | none |
| 4 | WDC | memory_hbm_storage | 538.12 |  | 533.3003 | 0.9038 | 533.56 | 517.335 | 0.1022 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 23.64 |  | 23.339 | 1.2896 | 23.32 | 22.79 | 0.0846 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 41.83 |  | 41.4612 | 0.8894 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 326.8 |  | 324.278 | 0.7777 | 325.59 | 322.63 | 0.0367 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.795 |  | 24.5771 | 0.8867 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 30.07 |  | 29.7521 | 1.0683 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.96 |  | 745.3754 | 0.2126 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.9 |  | 293.913 | 0.3358 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 577.835 |  | 576.9028 | 0.1616 | 582.03 | 576.57 | 0.0536 | watch_only | none |
| 4 | SOXX | semiconductor_index | 546.51 |  | 546.0065 | 0.0922 | 550.77 | 545.11 | 0.1043 | watch_only | none |
| 5 | QQQ | market_regime | 706.39 |  | 704.6458 | 0.2475 | 707.09 | 704.52 | 0.0142 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 326.8 |  | 324.278 | 0.7777 | 325.59 | 322.63 | 0.0367 | buy_precheck_manual_confirm | none |
| 7 | ONTO | semiconductor_test_packaging | 293.21 |  | 292.9572 | 0.0863 | 296.68 | 291.36 | 0.3104 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 400.83 |  | 399.5556 | 0.319 | 401.45 | 396.36 | 0.2919 | watch_only | none |
| 9 | HPE | ai_server_oem | 46.41 |  | 46.2267 | 0.3966 | 46.685 | 45.835 | 0.1077 | watch_only | none |
| 10 | TSM | foundry | 418.19 |  | 416.4365 | 0.4211 | 418.76 | 415.025 | 0.22 | watch_only | none |
| 11 | SMCI | ai_server_oem | 24.795 |  | 24.5771 | 0.8867 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 41.83 |  | 41.4612 | 0.8894 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| 13 | ARM | ai_accelerator | 287.42 |  | 283.2308 | 1.4791 | 286.39 | 275.86 | 0.2783 | buy_precheck_manual_confirm | none |
| 14 | WDC | memory_hbm_storage | 538.12 |  | 533.3003 | 0.9038 | 533.56 | 517.335 | 0.1022 | buy_precheck_manual_confirm | none |
| 15 | LRCX | semiconductor_equipment | 318.895 |  | 318.2146 | 0.2138 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 23.64 |  | 23.339 | 1.2896 | 23.32 | 22.79 | 0.0846 | buy_precheck_manual_confirm | none |
| 17 | PWR | data_center_power_cooling | 638.17 |  | 636.814 | 0.2129 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 405.91 |  | 405.5209 | 0.096 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 140.62 |  | 140.3094 | 0.2213 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | APLD | high_beta_ai_infrastructure | 30.07 |  | 29.7521 | 1.0683 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.96 |  | 745.3754 | 0.2126 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.9 |  | 293.913 | 0.3358 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 3 | ARM | ai_accelerator | 287.42 |  | 283.2308 | 1.4791 | 286.39 | 275.86 | 0.2783 | buy_precheck_manual_confirm | none |
| 4 | WDC | memory_hbm_storage | 538.12 |  | 533.3003 | 0.9038 | 533.56 | 517.335 | 0.1022 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 23.64 |  | 23.339 | 1.2896 | 23.32 | 22.79 | 0.0846 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 41.83 |  | 41.4612 | 0.8894 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 326.8 |  | 324.278 | 0.7777 | 325.59 | 322.63 | 0.0367 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.795 |  | 24.5771 | 0.8867 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 30.07 |  | 29.7521 | 1.0683 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |
| 10 | ANET | ai_networking_optical | 176.43 |  | 174.9403 | 0.8515 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | LITE | ai_networking_optical | 826.68 |  | 812.9378 | 1.6904 | 823.31 | 800.37 | 1.3343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | CIEN | ai_networking_optical | 407.04 |  | 400.8567 | 1.5425 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AMAT | semiconductor_equipment | 566.4 |  | 560.5903 | 1.0364 | 564.91 | 552.71 | 2.387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | STX | memory_hbm_storage | 867.09 |  | 863.7687 | 0.3845 | 866.73 | 845.78 | 0.7958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 368.905 |  | 363.8109 | 1.4002 | 365.97 | 356.39 | 4.8603 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TSM | foundry | 418.19 |  | 416.4365 | 0.4211 | 418.76 | 415.025 | 0.22 | watch_only | none |
| 17 | SMH | semiconductor_index | 577.835 |  | 576.9028 | 0.1616 | 582.03 | 576.57 | 0.0536 | watch_only | none |
| 18 | COHU | semiconductor_test_packaging | 54.81 |  | 54.3877 | 0.7765 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SOXX | semiconductor_index | 546.51 |  | 546.0065 | 0.0922 | 550.77 | 545.11 | 0.1043 | watch_only | none |
| 20 | QQQ | market_regime | 706.39 |  | 704.6458 | 0.2475 | 707.09 | 704.52 | 0.0142 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.39 |  | 704.6458 | 0.2475 | 707.09 | 704.52 | 0.0142 | watch_only | none |
| TQQQ | leveraged_tool | 70.58 |  | 70.2557 | 0.4616 | 70.84 | 70.09 | 0.0283 | watch_only | none |
| NVDA | ai_accelerator | 205.245 |  | 206.2696 | -0.4967 | 208.61 | 206.275 | 0.0195 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.83 |  | 399.5556 | 0.319 | 401.45 | 396.36 | 0.2919 | watch_only | none |
| AAPL | mega_cap_platform | 326.8 |  | 324.278 | 0.7777 | 325.59 | 322.63 | 0.0367 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.365 |  | 349.5065 | -0.0405 | 350.985 | 347.69 | 0.3435 | below_vwap | below_vwap |
| AMD | ai_accelerator | 531.835 |  | 529.3378 | 0.4718 | 532.365 | 524.72 | 1.7505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 418.19 |  | 416.4365 | 0.4211 | 418.76 | 415.025 | 0.22 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.51 |  | 546.0065 | 0.0922 | 550.77 | 545.11 | 0.1043 | watch_only | none |
| SMH | semiconductor_index | 577.835 |  | 576.9028 | 0.1616 | 582.03 | 576.57 | 0.0536 | watch_only | none |
| AVGO | custom_silicon_networking | 383.69 |  | 383.7903 | -0.0261 | 390.11 | 382.13 | 0.4483 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 929.815 |  | 930.7896 | -0.1047 | 944.99 | 923 | 0.1097 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.33 |  | 206.0881 | 0.1174 | 208.61 | 205.31 | 3.3926 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.5 |  | 402.3391 | -0.2085 | 405.78 | 397.185 | 0.3861 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.41 |  | 46.2267 | 0.3966 | 46.685 | 45.835 | 0.1077 | watch_only | none |
| SMCI | ai_server_oem | 24.795 |  | 24.5771 | 0.8867 | 24.77 | 24.34 | 0.0403 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.96 |  | 745.3754 | 0.2126 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.9 |  | 293.913 | 0.3358 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.745 |  | 124.998 | 0.5976 | 126.01 | 122.48 | 0.835 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 76.77 |  | 76.3268 | 0.5807 | 76.615 | 74.55 | 2.4489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.735 |  | 299.4894 | 0.082 | 305.09 | 299.13 | 0.407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.91 |  | 405.5209 | 0.096 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 638.17 |  | 636.814 | 0.2129 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1092.36 |  | 1102.962 | -0.9612 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 467.695 |  | 469.4936 | -0.3831 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.62 |  | 140.3094 | 0.2213 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.43 |  | 174.9403 | 0.8515 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 309.2 |  | 305.3994 | 1.2445 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 826.68 |  | 812.9378 | 1.6904 | 823.31 | 800.37 | 1.3343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 407.04 |  | 400.8567 | 1.5425 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 112.94 |  | 110.3307 | 2.365 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 327.35 |  | 324.3279 | 0.9318 | 329.97 | 323.92 | 3.5711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1799.17 |  | 1796.4486 | 0.1515 | 1804.54 | 1786.51 | 0.448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 566.4 |  | 560.5903 | 1.0364 | 564.91 | 552.71 | 2.387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 318.895 |  | 318.2146 | 0.2138 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.64 |  | 215.8478 | -0.0963 | 220.76 | 214.41 | 3.6311 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 368.905 |  | 363.8109 | 1.4002 | 365.97 | 356.39 | 4.8603 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.21 |  | 292.9572 | 0.0863 | 296.68 | 291.36 | 0.3104 | watch_only | none |
| AMKR | semiconductor_test_packaging | 65.64 |  | 65.2528 | 0.5933 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.81 |  | 54.3877 | 0.7765 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.125 |  | 140.0863 | -0.6862 | 142.09 | 139.41 | 4.5714 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 337.44 |  | 337.5953 | -0.046 | 340.205 | 336.3 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 509.32 |  | 509.3871 | -0.0132 | 512.83 | 507.675 | 0.9778 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 300.64 |  | 299.2486 | 0.465 | 301.84 | 296.5 | 0.469 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 30.07 |  | 29.7521 | 1.0683 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.83 |  | 41.4612 | 0.8894 | 41.65 | 40.435 | 0.0717 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 23.64 |  | 23.339 | 1.2896 | 23.32 | 22.79 | 0.0846 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1511.02 |  | 1517.202 | -0.4075 | 1540.85 | 1490.29 | 0.3415 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 538.12 |  | 533.3003 | 0.9038 | 533.56 | 517.335 | 0.1022 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 867.09 |  | 863.7687 | 0.3845 | 866.73 | 845.78 | 0.7958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.52 |  | 247.6514 | -0.053 | 248.915 | 247.32 | 0.0364 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.29 |  | 647.2785 | 0.0018 | 655.425 | 643.54 | 1.6237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 287.42 |  | 283.2308 | 1.4791 | 286.39 | 275.86 | 0.2783 | buy_precheck_manual_confirm | none |
| SKHY | memory_hbm_storage | 165.01 |  | 163.789 | 0.7455 | 165.88 | 160.77 | 1.7635 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
