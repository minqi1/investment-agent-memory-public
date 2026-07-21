# Intraday State

- Generated at: `2026-07-22T03:02:32+08:00`
- Market time ET: `2026-07-21T15:02:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'watch_only': 3, 'below_vwap': 15, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 2, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.91 |  | 707.333 | 0.223 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 552.92 |  | 549.4815 | 0.6258 | 550.77 | 545.11 | 0.0253 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.25 |  | 581.3658 | 0.4961 | 582.03 | 576.57 | 0.0531 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.235 |  | 747.2154 | 0.1365 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.625 |  | 420.7308 | 0.9256 | 418.76 | 415.025 | 0.0942 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.25 |  | 581.3658 | 0.4961 | 582.03 | 576.57 | 0.0531 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.92 |  | 549.4815 | 0.6258 | 550.77 | 545.11 | 0.0253 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.91 |  | 707.333 | 0.223 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.235 |  | 747.2154 | 0.1365 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 972.37 |  | 953.5635 | 1.9722 | 944.99 | 923 | 0.1964 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.8 |  | 294.6889 | 0.377 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | AAPL | mega_cap_platform | 328.025 |  | 326.3348 | 0.5179 | 325.59 | 322.63 | 0.0183 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.195 |  | 24.9637 | 0.9266 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.4 |  | 70.8251 | 0.8116 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 708.91 |  | 707.333 | 0.223 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.235 |  | 747.2154 | 0.1365 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 584.25 |  | 581.3658 | 0.4961 | 582.03 | 576.57 | 0.0531 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 552.92 |  | 549.4815 | 0.6258 | 550.77 | 545.11 | 0.0253 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.8 |  | 294.6889 | 0.377 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 142.11 |  | 141.8725 | 0.1674 | 142.15 | 140.105 | 0.0422 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 328.025 |  | 326.3348 | 0.5179 | 325.59 | 322.63 | 0.0183 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 207.98 |  | 207.7617 | 0.1051 | 208.61 | 205.31 | 0.2068 | watch_only | none |
| 9 | NVDA | ai_accelerator | 206.98 |  | 206.1019 | 0.4261 | 208.61 | 206.275 | 0.0097 | watch_only | none |
| 10 | TSM | foundry | 424.625 |  | 420.7308 | 0.9256 | 418.76 | 415.025 | 0.0942 | buy_precheck_manual_confirm | none |
| 11 | TT | data_center_power_cooling | 471.26 |  | 470.1228 | 0.2419 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | AMAT | semiconductor_equipment | 564.99 |  | 564.804 | 0.0329 | 564.91 | 552.71 | 1.1239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SMCI | ai_server_oem | 25.195 |  | 24.9637 | 0.9266 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 14 | AVGO | custom_silicon_networking | 386.28 |  | 384.948 | 0.346 | 390.11 | 382.13 | 0.4841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | LRCX | semiconductor_equipment | 321.665 |  | 320.5287 | 0.3545 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ORCL | cloud_ai_capex | 126.06 |  | 125.7911 | 0.2138 | 126.01 | 122.48 | 1.5152 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | KLAC | semiconductor_equipment | 217.52 |  | 216.9653 | 0.2557 | 220.76 | 214.41 | 3.3974 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | DELL | ai_server_oem | 403.695 |  | 403.5913 | 0.0257 | 405.78 | 397.185 | 4.6471 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | META | cloud_ai_capex | 647.4 |  | 647.3418 | 0.009 | 655.425 | 643.54 | 1.2573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 289.17 |  | 286.8777 | 0.799 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.625 |  | 420.7308 | 0.9256 | 418.76 | 415.025 | 0.0942 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.25 |  | 581.3658 | 0.4961 | 582.03 | 576.57 | 0.0531 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.92 |  | 549.4815 | 0.6258 | 550.77 | 545.11 | 0.0253 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.91 |  | 707.333 | 0.223 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.235 |  | 747.2154 | 0.1365 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 972.37 |  | 953.5635 | 1.9722 | 944.99 | 923 | 0.1964 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.8 |  | 294.6889 | 0.377 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | AAPL | mega_cap_platform | 328.025 |  | 326.3348 | 0.5179 | 325.59 | 322.63 | 0.0183 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.195 |  | 24.9637 | 0.9266 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.4 |  | 70.8251 | 0.8116 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | ASML | semiconductor_equipment | 1806.715 |  | 1809.3368 | -0.1449 | 1804.54 | 1786.51 | 0.16 | below_vwap | below_vwap |
| 12 | CIEN | ai_networking_optical | 405.43 |  | 405.6692 | -0.059 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | CORZ | high_beta_ai_infrastructure | 23.925 |  | 24.0174 | -0.3849 | 23.32 | 22.79 | 0.0418 | below_vwap | below_vwap |
| 14 | CRWV | gpu_cloud_ai_factory | 77.83 |  | 78.5475 | -0.9135 | 76.615 | 74.55 | 3.2764 | below_vwap | below_vwap,spread_too_wide |
| 15 | APLD | high_beta_ai_infrastructure | 30.165 |  | 30.2817 | -0.3852 | 29.735 | 28.785 | 0.0663 | below_vwap | below_vwap |
| 16 | AMD | ai_accelerator | 542.65 |  | 535.558 | 1.3242 | 532.365 | 524.72 | 1.758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 835.65 |  | 825.5931 | 1.2181 | 823.31 | 800.37 | 0.9274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 564.99 |  | 564.804 | 0.0329 | 564.91 | 552.71 | 1.1239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 890.35 |  | 879.1905 | 1.2693 | 866.73 | 845.78 | 2.0262 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 289.17 |  | 286.8777 | 0.799 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.91 |  | 707.333 | 0.223 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.4 |  | 70.8251 | 0.8116 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.98 |  | 206.1019 | 0.4261 | 208.61 | 206.275 | 0.0097 | watch_only | none |
| MSFT | cloud_ai_capex | 398.3 |  | 399.0844 | -0.1965 | 401.45 | 396.36 | 0.0201 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.025 |  | 326.3348 | 0.5179 | 325.59 | 322.63 | 0.0183 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.52 |  | 349.1172 | -0.1711 | 350.985 | 347.69 | 0.0488 | below_vwap | below_vwap |
| AMD | ai_accelerator | 542.65 |  | 535.558 | 1.3242 | 532.365 | 524.72 | 1.758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 424.625 |  | 420.7308 | 0.9256 | 418.76 | 415.025 | 0.0942 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.92 |  | 549.4815 | 0.6258 | 550.77 | 545.11 | 0.0253 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.25 |  | 581.3658 | 0.4961 | 582.03 | 576.57 | 0.0531 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.28 |  | 384.948 | 0.346 | 390.11 | 382.13 | 0.4841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 972.37 |  | 953.5635 | 1.9722 | 944.99 | 923 | 0.1964 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 207.98 |  | 207.7617 | 0.1051 | 208.61 | 205.31 | 0.2068 | watch_only | none |
| DELL | ai_server_oem | 403.695 |  | 403.5913 | 0.0257 | 405.78 | 397.185 | 4.6471 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.345 |  | 46.5286 | -0.3946 | 46.685 | 45.835 | 0.0647 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.195 |  | 24.9637 | 0.9266 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.235 |  | 747.2154 | 0.1365 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.8 |  | 294.6889 | 0.377 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.06 |  | 125.7911 | 0.2138 | 126.01 | 122.48 | 1.5152 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.83 |  | 78.5475 | -0.9135 | 76.615 | 74.55 | 3.2764 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.92 |  | 302.0678 | 0.6132 | 305.09 | 299.13 | 1.8459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 403.1 |  | 405.7185 | -0.6454 | 411.01 | 404.21 | 0.1141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 638.67 |  | 638.7509 | -0.0127 | 645.815 | 635.91 | 0.1801 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1082.835 |  | 1095.0913 | -1.1192 | 1140.63 | 1103.815 | 2.6551 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 471.26 |  | 470.1228 | 0.2419 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.11 |  | 141.8725 | 0.1674 | 142.15 | 140.105 | 0.0422 | watch_only | none |
| ANET | ai_networking_optical | 174.41 |  | 175.0574 | -0.3698 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 316.05 |  | 313.1305 | 0.9324 | 309.72 | 302.3 | 0.9809 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 835.65 |  | 825.5931 | 1.2181 | 823.31 | 800.37 | 0.9274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 405.43 |  | 405.6692 | -0.059 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 118.575 |  | 116.5971 | 1.6963 | 109.39 | 107.58 | 2.1674 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 321.73 |  | 325.2903 | -1.0945 | 329.97 | 323.92 | 0.1305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ASML | semiconductor_equipment | 1806.715 |  | 1809.3368 | -0.1449 | 1804.54 | 1786.51 | 0.16 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.99 |  | 564.804 | 0.0329 | 564.91 | 552.71 | 1.1239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.665 |  | 320.5287 | 0.3545 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.52 |  | 216.9653 | 0.2557 | 220.76 | 214.41 | 3.3974 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 378.145 |  | 371.9501 | 1.6655 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 300.61 |  | 297.3666 | 1.0907 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.785 |  | 66.1918 | 0.8962 | 66.54 | 65 | 0.9433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 140.08 |  | 141.4476 | -0.9668 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.125 |  | 340.409 | 1.3854 | 340.205 | 336.3 | 4.3434 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.295 |  | 506.39 | -0.0188 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 298.05 |  | 299.2876 | -0.4135 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.165 |  | 30.2817 | -0.3852 | 29.735 | 28.785 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.59 |  | 41.7115 | -2.6887 | 41.65 | 40.435 | 0.0493 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.925 |  | 24.0174 | -0.3849 | 23.32 | 22.79 | 0.0418 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1558.25 |  | 1543.9184 | 0.9283 | 1540.85 | 1490.29 | 3.9788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 546.61 |  | 541.1257 | 1.0135 | 533.56 | 517.335 | 0.4226 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 890.35 |  | 879.1905 | 1.2693 | 866.73 | 845.78 | 2.0262 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.46 |  | 247.8333 | -0.1506 | 248.915 | 247.32 | 0.0242 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.4 |  | 647.3418 | 0.009 | 655.425 | 643.54 | 1.2573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 289.17 |  | 286.8777 | 0.799 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 170.625 |  | 167.3309 | 1.9686 | 165.88 | 160.77 | 1.1722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
