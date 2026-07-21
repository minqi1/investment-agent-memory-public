# Intraday State

- Generated at: `2026-07-22T03:18:08+08:00`
- Market time ET: `2026-07-21T15:18:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'watch_only': 6, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 2, 'below_vwap': 16, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.9 |  | 707.442 | 0.2061 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 551.57 |  | 549.6809 | 0.3437 | 550.77 | 545.11 | 0.0508 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.66 |  | 581.505 | 0.3706 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.43 |  | 747.2652 | 0.1559 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.755 |  | 421.042 | 0.8819 | 418.76 | 415.025 | 0.1271 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.66 |  | 581.505 | 0.3706 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 551.57 |  | 549.6809 | 0.3437 | 550.77 | 545.11 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.9 |  | 707.442 | 0.2061 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.43 |  | 747.2652 | 0.1559 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.96 |  | 294.7106 | 0.4239 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 545.74 |  | 541.2249 | 0.8342 | 533.56 | 517.335 | 0.2657 | buy_precheck_manual_confirm | none |
| 8 | SNDK | memory_hbm_storage | 1553.69 |  | 1544.2976 | 0.6082 | 1540.85 | 1490.29 | 0.1364 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 327.99 |  | 326.3989 | 0.4875 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.15 |  | 24.9698 | 0.7218 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.36 |  | 70.8348 | 0.7414 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 551.57 |  | 549.6809 | 0.3437 | 550.77 | 545.11 | 0.0508 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.9 |  | 707.442 | 0.2061 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 748.43 |  | 747.2652 | 0.1559 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 583.66 |  | 581.505 | 0.3706 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.96 |  | 294.7106 | 0.4239 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 142.05 |  | 141.8753 | 0.1232 | 142.15 | 140.105 | 0.0211 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 349.5 |  | 349.1152 | 0.1102 | 350.985 | 347.69 | 0.0172 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 327.99 |  | 326.3989 | 0.4875 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 9 | MSFT | cloud_ai_capex | 399.27 |  | 399.0791 | 0.0478 | 401.45 | 396.36 | 0.025 | watch_only | none |
| 10 | NVDA | ai_accelerator | 206.83 |  | 206.123 | 0.343 | 208.61 | 206.275 | 0.3481 | watch_only | none |
| 11 | KLAC | semiconductor_equipment | 217.405 |  | 216.983 | 0.1945 | 220.76 | 214.41 | 0.1932 | watch_only | none |
| 12 | SNDK | memory_hbm_storage | 1553.69 |  | 1544.2976 | 0.6082 | 1540.85 | 1490.29 | 0.1364 | buy_precheck_manual_confirm | none |
| 13 | META | cloud_ai_capex | 648.23 |  | 647.3746 | 0.1321 | 655.425 | 643.54 | 0.1959 | watch_only | none |
| 14 | SMCI | ai_server_oem | 25.15 |  | 24.9698 | 0.7218 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 15 | TSM | foundry | 424.755 |  | 421.042 | 0.8819 | 418.76 | 415.025 | 0.1271 | buy_precheck_manual_confirm | none |
| 16 | TT | data_center_power_cooling | 470.2 |  | 470.1268 | 0.0156 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 385.85 |  | 384.9625 | 0.2305 | 390.11 | 382.13 | 0.7542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 322.41 |  | 320.5711 | 0.5736 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ORCL | cloud_ai_capex | 126.17 |  | 125.8103 | 0.2859 | 126.01 | 122.48 | 0.642 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 545.74 |  | 541.2249 | 0.8342 | 533.56 | 517.335 | 0.2657 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.755 |  | 421.042 | 0.8819 | 418.76 | 415.025 | 0.1271 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.66 |  | 581.505 | 0.3706 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 551.57 |  | 549.6809 | 0.3437 | 550.77 | 545.11 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.9 |  | 707.442 | 0.2061 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.43 |  | 747.2652 | 0.1559 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.96 |  | 294.7106 | 0.4239 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 545.74 |  | 541.2249 | 0.8342 | 533.56 | 517.335 | 0.2657 | buy_precheck_manual_confirm | none |
| 8 | SNDK | memory_hbm_storage | 1553.69 |  | 1544.2976 | 0.6082 | 1540.85 | 1490.29 | 0.1364 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 327.99 |  | 326.3989 | 0.4875 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.15 |  | 24.9698 | 0.7218 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.36 |  | 70.8348 | 0.7414 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 12 | ASML | semiconductor_equipment | 1806.11 |  | 1809.19 | -0.1702 | 1804.54 | 1786.51 | 0.0332 | below_vwap | below_vwap |
| 13 | CIEN | ai_networking_optical | 405.55 |  | 405.6477 | -0.0241 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | CORZ | high_beta_ai_infrastructure | 23.88 |  | 24.0101 | -0.5421 | 23.32 | 22.79 | 0.0419 | below_vwap | below_vwap |
| 15 | CRWV | gpu_cloud_ai_factory | 78.15 |  | 78.5259 | -0.4787 | 76.615 | 74.55 | 2.7127 | below_vwap | below_vwap,spread_too_wide |
| 16 | APLD | high_beta_ai_infrastructure | 29.93 |  | 30.266 | -1.1102 | 29.735 | 28.785 | 0.0668 | below_vwap | below_vwap |
| 17 | AMD | ai_accelerator | 541.22 |  | 535.77 | 1.0172 | 532.365 | 524.72 | 2.0934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MU | memory_hbm_storage | 964.8 |  | 954.2522 | 1.1053 | 944.99 | 923 | 0.4343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LITE | ai_networking_optical | 833.315 |  | 825.9 | 0.8978 | 823.31 | 800.37 | 2.106 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 889.64 |  | 879.9013 | 1.1068 | 866.73 | 845.78 | 1.2173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.9 |  | 707.442 | 0.2061 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.36 |  | 70.8348 | 0.7414 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.83 |  | 206.123 | 0.343 | 208.61 | 206.275 | 0.3481 | watch_only | none |
| MSFT | cloud_ai_capex | 399.27 |  | 399.0791 | 0.0478 | 401.45 | 396.36 | 0.025 | watch_only | none |
| AAPL | mega_cap_platform | 327.99 |  | 326.3989 | 0.4875 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.5 |  | 349.1152 | 0.1102 | 350.985 | 347.69 | 0.0172 | watch_only | none |
| AMD | ai_accelerator | 541.22 |  | 535.77 | 1.0172 | 532.365 | 524.72 | 2.0934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 424.755 |  | 421.042 | 0.8819 | 418.76 | 415.025 | 0.1271 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.57 |  | 549.6809 | 0.3437 | 550.77 | 545.11 | 0.0508 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.66 |  | 581.505 | 0.3706 | 582.03 | 576.57 | 0.0377 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.85 |  | 384.9625 | 0.2305 | 390.11 | 382.13 | 0.7542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 964.8 |  | 954.2522 | 1.1053 | 944.99 | 923 | 0.4343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.12 |  | 207.7514 | -0.3039 | 208.61 | 205.31 | 0.2317 | below_vwap | below_vwap |
| DELL | ai_server_oem | 402.59 |  | 403.571 | -0.2431 | 405.78 | 397.185 | 0.1739 | below_vwap | below_vwap |
| HPE | ai_server_oem | 46.09 |  | 46.5097 | -0.9023 | 46.685 | 45.835 | 0.0217 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.15 |  | 24.9698 | 0.7218 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.43 |  | 747.2652 | 0.1559 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.96 |  | 294.7106 | 0.4239 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.17 |  | 125.8103 | 0.2859 | 126.01 | 122.48 | 0.642 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.15 |  | 78.5259 | -0.4787 | 76.615 | 74.55 | 2.7127 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303 |  | 302.0931 | 0.3002 | 305.09 | 299.13 | 3.8977 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.72 |  | 405.5922 | -0.7081 | 411.01 | 404.21 | 0.072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 637.65 |  | 638.7295 | -0.169 | 645.815 | 635.91 | 0.0486 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1074.355 |  | 1094.5954 | -1.8491 | 1140.63 | 1103.815 | 4.693 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.2 |  | 470.1268 | 0.0156 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.05 |  | 141.8753 | 0.1232 | 142.15 | 140.105 | 0.0211 | watch_only | none |
| ANET | ai_networking_optical | 174.36 |  | 175.043 | -0.3902 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 316.06 |  | 313.2166 | 0.9078 | 309.72 | 302.3 | 1.3605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 833.315 |  | 825.9 | 0.8978 | 823.31 | 800.37 | 2.106 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 405.55 |  | 405.6477 | -0.0241 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 118.6 |  | 116.6446 | 1.6764 | 109.39 | 107.58 | 4.2159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 319.16 |  | 324.7318 | -1.7158 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1806.11 |  | 1809.19 | -0.1702 | 1804.54 | 1786.51 | 0.0332 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 563.96 |  | 564.8004 | -0.1488 | 564.91 | 552.71 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 322.41 |  | 320.5711 | 0.5736 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.405 |  | 216.983 | 0.1945 | 220.76 | 214.41 | 0.1932 | watch_only | none |
| TER | semiconductor_test_packaging | 376.8 |  | 372.136 | 1.2533 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 300.15 |  | 297.4893 | 0.8944 | 296.68 | 291.36 | 4.5311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.52 |  | 66.2019 | 0.4805 | 66.54 | 65 | 0.5863 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.79 |  | 141.321 | -1.0834 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 344.86 |  | 340.4983 | 1.281 | 340.205 | 336.3 | 4.2626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.59 |  | 506.393 | 0.0389 | 512.83 | 507.675 | 0.4047 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 298.505 |  | 299.2012 | -0.2327 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.93 |  | 30.266 | -1.1102 | 29.735 | 28.785 | 0.0668 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.59 |  | 41.6629 | -2.5753 | 41.65 | 40.435 | 0.0493 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.88 |  | 24.0101 | -0.5421 | 23.32 | 22.79 | 0.0419 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1553.69 |  | 1544.2976 | 0.6082 | 1540.85 | 1490.29 | 0.1364 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 545.74 |  | 541.2249 | 0.8342 | 533.56 | 517.335 | 0.2657 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 889.64 |  | 879.9013 | 1.1068 | 866.73 | 845.78 | 1.2173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.72 |  | 247.8243 | -0.0421 | 248.915 | 247.32 | 0.0161 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.23 |  | 647.3746 | 0.1321 | 655.425 | 643.54 | 0.1959 | watch_only | none |
| ARM | ai_accelerator | 287.97 |  | 286.9129 | 0.3685 | 286.39 | 275.86 | 2.2155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 169.73 |  | 167.4075 | 1.3873 | 165.88 | 160.77 | 1.6438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
