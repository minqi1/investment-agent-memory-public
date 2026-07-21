# Intraday State

- Generated at: `2026-07-22T03:14:17+08:00`
- Market time ET: `2026-07-21T15:14:18-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'watch_only': 5, 'below_vwap': 16, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 2, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.82 |  | 707.422 | 0.1976 | 707.09 | 704.52 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 551.62 |  | 549.6554 | 0.3574 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.35 |  | 581.4848 | 0.3208 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.2 |  | 747.2565 | 0.1263 | 746.6 | 744.3 | 0.0147 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.62 |  | 421.0277 | 0.8532 | 418.76 | 415.025 | 0.1389 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.35 |  | 581.4848 | 0.3208 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 551.62 |  | 549.6554 | 0.3574 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.82 |  | 707.422 | 0.1976 | 707.09 | 704.52 | 0.0085 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.2 |  | 747.2565 | 0.1263 | 746.6 | 744.3 | 0.0147 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.905 |  | 294.7037 | 0.4076 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 545.59 |  | 541.2079 | 0.8097 | 533.56 | 517.335 | 0.2786 | buy_precheck_manual_confirm | none |
| 8 | AAPL | mega_cap_platform | 327.88 |  | 326.3832 | 0.4586 | 325.59 | 322.63 | 0.0366 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.11 |  | 24.9681 | 0.5681 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.35 |  | 70.8304 | 0.7336 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 583.35 |  | 581.4848 | 0.3208 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.82 |  | 707.422 | 0.1976 | 707.09 | 704.52 | 0.0085 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 748.2 |  | 747.2565 | 0.1263 | 746.6 | 744.3 | 0.0147 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 551.62 |  | 549.6554 | 0.3574 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 206.785 |  | 206.1191 | 0.3231 | 208.61 | 206.275 | 0.0339 | watch_only | none |
| 6 | IWM | market_regime | 295.905 |  | 294.7037 | 0.4076 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 217.185 |  | 216.9808 | 0.0941 | 220.76 | 214.41 | 0.0691 | watch_only | none |
| 8 | JCI | data_center_power_cooling | 142.03 |  | 141.8746 | 0.1095 | 142.15 | 140.105 | 0.0422 | watch_only | none |
| 9 | GOOGL | cloud_ai_capex | 349.34 |  | 349.1099 | 0.0659 | 350.985 | 347.69 | 0.0143 | watch_only | none |
| 10 | AAPL | mega_cap_platform | 327.88 |  | 326.3832 | 0.4586 | 325.59 | 322.63 | 0.0366 | buy_precheck_manual_confirm | none |
| 11 | META | cloud_ai_capex | 648.03 |  | 647.3645 | 0.1028 | 655.425 | 643.54 | 0.3086 | watch_only | none |
| 12 | SMCI | ai_server_oem | 25.11 |  | 24.9681 | 0.5681 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 13 | TSM | foundry | 424.62 |  | 421.0277 | 0.8532 | 418.76 | 415.025 | 0.1389 | buy_precheck_manual_confirm | none |
| 14 | TT | data_center_power_cooling | 470.4 |  | 470.124 | 0.0587 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 385.62 |  | 384.9599 | 0.1715 | 390.11 | 382.13 | 1.014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ORCL | cloud_ai_capex | 126.15 |  | 125.8079 | 0.2719 | 126.01 | 122.48 | 0.6659 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | WDC | memory_hbm_storage | 545.59 |  | 541.2079 | 0.8097 | 533.56 | 517.335 | 0.2786 | buy_precheck_manual_confirm | none |
| 18 | AMAT | semiconductor_equipment | 564.83 |  | 564.8015 | 0.005 | 564.91 | 552.71 | 1.1419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 303.08 |  | 302.0885 | 0.3282 | 305.09 | 299.13 | 1.6233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 288.085 |  | 286.9038 | 0.4117 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.62 |  | 421.0277 | 0.8532 | 418.76 | 415.025 | 0.1389 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.35 |  | 581.4848 | 0.3208 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 551.62 |  | 549.6554 | 0.3574 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.82 |  | 707.422 | 0.1976 | 707.09 | 704.52 | 0.0085 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.2 |  | 747.2565 | 0.1263 | 746.6 | 744.3 | 0.0147 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.905 |  | 294.7037 | 0.4076 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 545.59 |  | 541.2079 | 0.8097 | 533.56 | 517.335 | 0.2786 | buy_precheck_manual_confirm | none |
| 8 | AAPL | mega_cap_platform | 327.88 |  | 326.3832 | 0.4586 | 325.59 | 322.63 | 0.0366 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.11 |  | 24.9681 | 0.5681 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.35 |  | 70.8304 | 0.7336 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 11 | ASML | semiconductor_equipment | 1805.94 |  | 1809.2433 | -0.1826 | 1804.54 | 1786.51 | 0.0343 | below_vwap | below_vwap |
| 12 | CIEN | ai_networking_optical | 405.155 |  | 405.6479 | -0.1215 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | CORZ | high_beta_ai_infrastructure | 23.885 |  | 24.0123 | -0.5302 | 23.32 | 22.79 | 0.0419 | below_vwap | below_vwap |
| 14 | CRWV | gpu_cloud_ai_factory | 78.155 |  | 78.5292 | -0.4765 | 76.615 | 74.55 | 4.2864 | below_vwap | below_vwap,spread_too_wide |
| 15 | APLD | high_beta_ai_infrastructure | 29.885 |  | 30.2687 | -1.2675 | 29.735 | 28.785 | 0.0669 | below_vwap | below_vwap |
| 16 | AMD | ai_accelerator | 541.54 |  | 535.7189 | 1.0866 | 532.365 | 524.72 | 2.7902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MU | memory_hbm_storage | 966.475 |  | 954.1259 | 1.2943 | 944.99 | 923 | 1.2944 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LITE | ai_networking_optical | 832.525 |  | 825.7624 | 0.8189 | 823.31 | 800.37 | 1.5675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 890.04 |  | 879.7877 | 1.1653 | 866.73 | 845.78 | 1.2483 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 288.085 |  | 286.9038 | 0.4117 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.82 |  | 707.422 | 0.1976 | 707.09 | 704.52 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.35 |  | 70.8304 | 0.7336 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.785 |  | 206.1191 | 0.3231 | 208.61 | 206.275 | 0.0339 | watch_only | none |
| MSFT | cloud_ai_capex | 398.885 |  | 399.0784 | -0.0485 | 401.45 | 396.36 | 0.0125 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.88 |  | 326.3832 | 0.4586 | 325.59 | 322.63 | 0.0366 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.34 |  | 349.1099 | 0.0659 | 350.985 | 347.69 | 0.0143 | watch_only | none |
| AMD | ai_accelerator | 541.54 |  | 535.7189 | 1.0866 | 532.365 | 524.72 | 2.7902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 424.62 |  | 421.0277 | 0.8532 | 418.76 | 415.025 | 0.1389 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.62 |  | 549.6554 | 0.3574 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.35 |  | 581.4848 | 0.3208 | 582.03 | 576.57 | 0.0274 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.62 |  | 384.9599 | 0.1715 | 390.11 | 382.13 | 1.014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 966.475 |  | 954.1259 | 1.2943 | 944.99 | 923 | 1.2944 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.09 |  | 207.7554 | -0.3203 | 208.61 | 205.31 | 0.3573 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 402.63 |  | 403.5766 | -0.2346 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.105 |  | 46.5169 | -0.8856 | 46.685 | 45.835 | 0.0434 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.11 |  | 24.9681 | 0.5681 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.2 |  | 747.2565 | 0.1263 | 746.6 | 744.3 | 0.0147 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.905 |  | 294.7037 | 0.4076 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.15 |  | 125.8079 | 0.2719 | 126.01 | 122.48 | 0.6659 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.155 |  | 78.5292 | -0.4765 | 76.615 | 74.55 | 4.2864 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.08 |  | 302.0885 | 0.3282 | 305.09 | 299.13 | 1.6233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.62 |  | 405.6368 | -0.7437 | 411.01 | 404.21 | 0.0944 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 638.21 |  | 638.7366 | -0.0824 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1075.46 |  | 1094.7129 | -1.7587 | 1140.63 | 1103.815 | 4.5692 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.4 |  | 470.124 | 0.0587 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.03 |  | 141.8746 | 0.1095 | 142.15 | 140.105 | 0.0422 | watch_only | none |
| ANET | ai_networking_optical | 174.43 |  | 175.0455 | -0.3516 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.67 |  | 313.1944 | 0.7904 | 309.72 | 302.3 | 1.0676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 832.525 |  | 825.7624 | 0.8189 | 823.31 | 800.37 | 1.5675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 405.155 |  | 405.6479 | -0.1215 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 118.595 |  | 116.6336 | 1.6817 | 109.39 | 107.58 | 2.5465 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 318.9 |  | 324.8157 | -1.8212 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.94 |  | 1809.2433 | -0.1826 | 1804.54 | 1786.51 | 0.0343 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.83 |  | 564.8015 | 0.005 | 564.91 | 552.71 | 1.1419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 322.63 |  | 320.5689 | 0.6429 | 328.135 | 317.17 | 4.9592 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 217.185 |  | 216.9808 | 0.0941 | 220.76 | 214.41 | 0.0691 | watch_only | none |
| TER | semiconductor_test_packaging | 376.5 |  | 372.1118 | 1.1793 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 299.81 |  | 297.4641 | 0.7886 | 296.68 | 291.36 | 4.5529 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.51 |  | 66.2004 | 0.4677 | 66.54 | 65 | 4.5557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.44 |  | 141.3355 | -1.3412 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 344.86 |  | 340.4983 | 1.281 | 340.205 | 336.3 | 4.4801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.635 |  | 506.3909 | 0.0482 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 298.4 |  | 299.2039 | -0.2687 | 301.84 | 296.5 | 4.5643 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.885 |  | 30.2687 | -1.2675 | 29.735 | 28.785 | 0.0669 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.645 |  | 41.6718 | -2.4641 | 41.65 | 40.435 | 0.0246 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.885 |  | 24.0123 | -0.5302 | 23.32 | 22.79 | 0.0419 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1552.5 |  | 1544.209 | 0.5369 | 1540.85 | 1490.29 | 3.9936 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 545.59 |  | 541.2079 | 0.8097 | 533.56 | 517.335 | 0.2786 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 890.04 |  | 879.7877 | 1.1653 | 866.73 | 845.78 | 1.2483 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.685 |  | 247.8248 | -0.0564 | 248.915 | 247.32 | 0.0161 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.03 |  | 647.3645 | 0.1028 | 655.425 | 643.54 | 0.3086 | watch_only | none |
| ARM | ai_accelerator | 288.085 |  | 286.9038 | 0.4117 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 170.25 |  | 167.3998 | 1.7026 | 165.88 | 160.77 | 1.1689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
