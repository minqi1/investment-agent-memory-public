# Intraday State

- Generated at: `2026-07-22T02:58:39+08:00`
- Market time ET: `2026-07-21T14:58:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 2, 'below_vwap': 16, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 2, 'below_opening_15m_low': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.01 |  | 707.3218 | 0.2387 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 553.09 |  | 549.4445 | 0.6635 | 550.77 | 545.11 | 0.0579 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.42 |  | 581.3052 | 0.5358 | 582.03 | 576.57 | 0.0428 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.31 |  | 747.2054 | 0.1478 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.66 |  | 420.7139 | 0.938 | 418.76 | 415.025 | 0.1554 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.42 |  | 581.3052 | 0.5358 | 582.03 | 576.57 | 0.0428 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 553.09 |  | 549.4445 | 0.6635 | 550.77 | 545.11 | 0.0579 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.01 |  | 707.3218 | 0.2387 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.31 |  | 747.2054 | 0.1478 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 971.75 |  | 953.3958 | 1.9251 | 944.99 | 923 | 0.317 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.85 |  | 294.6824 | 0.3962 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | STX | memory_hbm_storage | 889.32 |  | 879.0539 | 1.1679 | 866.73 | 845.78 | 0.271 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 546.3 |  | 541.0868 | 0.9635 | 533.56 | 517.335 | 0.1062 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 328.14 |  | 326.3273 | 0.5555 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 126.305 |  | 125.7807 | 0.4168 | 126.01 | 122.48 | 0.0554 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 25.14 |  | 24.9621 | 0.7125 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.415 |  | 70.822 | 0.8374 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 709.01 |  | 707.3218 | 0.2387 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.31 |  | 747.2054 | 0.1478 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 584.42 |  | 581.3052 | 0.5358 | 582.03 | 576.57 | 0.0428 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 553.09 |  | 549.4445 | 0.6635 | 550.77 | 545.11 | 0.0579 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 126.305 |  | 125.7807 | 0.4168 | 126.01 | 122.48 | 0.0554 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.85 |  | 294.6824 | 0.3962 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 328.14 |  | 326.3273 | 0.5555 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 471.22 |  | 470.1089 | 0.2364 | 475.98 | 467.01 | 0.1889 | watch_only | none |
| 9 | NVDA | ai_accelerator | 207.1 |  | 206.0949 | 0.4877 | 208.61 | 206.275 | 0.1449 | watch_only | none |
| 10 | SMCI | ai_server_oem | 25.14 |  | 24.9621 | 0.7125 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 11 | AMAT | semiconductor_equipment | 566.04 |  | 564.7828 | 0.2226 | 564.91 | 552.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 142.16 |  | 141.8683 | 0.2056 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 321.24 |  | 320.5045 | 0.2295 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TSM | foundry | 424.66 |  | 420.7139 | 0.938 | 418.76 | 415.025 | 0.1554 | buy_precheck_manual_confirm | none |
| 15 | PWR | data_center_power_cooling | 638.94 |  | 638.7514 | 0.0295 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 546.3 |  | 541.0868 | 0.9635 | 533.56 | 517.335 | 0.1062 | buy_precheck_manual_confirm | none |
| 17 | STX | memory_hbm_storage | 889.32 |  | 879.0539 | 1.1679 | 866.73 | 845.78 | 0.271 | buy_precheck_manual_confirm | none |
| 18 | KLAC | semiconductor_equipment | 217.62 |  | 216.9591 | 0.3046 | 220.76 | 214.41 | 1.5256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AVGO | custom_silicon_networking | 386.37 |  | 384.9425 | 0.3708 | 390.11 | 382.13 | 0.4348 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | VRT | data_center_power_cooling | 304.14 |  | 302.0471 | 0.6929 | 305.09 | 299.13 | 2.0024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.66 |  | 420.7139 | 0.938 | 418.76 | 415.025 | 0.1554 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.42 |  | 581.3052 | 0.5358 | 582.03 | 576.57 | 0.0428 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 553.09 |  | 549.4445 | 0.6635 | 550.77 | 545.11 | 0.0579 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.01 |  | 707.3218 | 0.2387 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.31 |  | 747.2054 | 0.1478 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 971.75 |  | 953.3958 | 1.9251 | 944.99 | 923 | 0.317 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.85 |  | 294.6824 | 0.3962 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | STX | memory_hbm_storage | 889.32 |  | 879.0539 | 1.1679 | 866.73 | 845.78 | 0.271 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 546.3 |  | 541.0868 | 0.9635 | 533.56 | 517.335 | 0.1062 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 328.14 |  | 326.3273 | 0.5555 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 126.305 |  | 125.7807 | 0.4168 | 126.01 | 122.48 | 0.0554 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 25.14 |  | 24.9621 | 0.7125 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.415 |  | 70.822 | 0.8374 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 14 | ASML | semiconductor_equipment | 1805.315 |  | 1809.3731 | -0.2243 | 1804.54 | 1786.51 | 0.1036 | below_vwap | below_vwap |
| 15 | CIEN | ai_networking_optical | 405.43 |  | 405.6693 | -0.059 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 23.91 |  | 24.0188 | -0.4531 | 23.32 | 22.79 | 0.0836 | below_vwap | below_vwap |
| 17 | CRWV | gpu_cloud_ai_factory | 77.815 |  | 78.5569 | -0.9444 | 76.615 | 74.55 | 0.8096 | below_vwap | below_vwap,spread_too_wide |
| 18 | APLD | high_beta_ai_infrastructure | 30.08 |  | 30.2842 | -0.6742 | 29.735 | 28.785 | 0.0665 | below_vwap | below_vwap |
| 19 | AMD | ai_accelerator | 543.49 |  | 535.5084 | 1.4905 | 532.365 | 524.72 | 1.518 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | LITE | ai_networking_optical | 833.89 |  | 825.534 | 1.0122 | 823.31 | 800.37 | 0.7627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.01 |  | 707.3218 | 0.2387 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.415 |  | 70.822 | 0.8374 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 207.1 |  | 206.0949 | 0.4877 | 208.61 | 206.275 | 0.1449 | watch_only | none |
| MSFT | cloud_ai_capex | 398.13 |  | 399.0925 | -0.2412 | 401.45 | 396.36 | 0.0804 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.14 |  | 326.3273 | 0.5555 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.6 |  | 349.1236 | -0.15 | 350.985 | 347.69 | 0.0057 | below_vwap | below_vwap |
| AMD | ai_accelerator | 543.49 |  | 535.5084 | 1.4905 | 532.365 | 524.72 | 1.518 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 424.66 |  | 420.7139 | 0.938 | 418.76 | 415.025 | 0.1554 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.09 |  | 549.4445 | 0.6635 | 550.77 | 545.11 | 0.0579 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.42 |  | 581.3052 | 0.5358 | 582.03 | 576.57 | 0.0428 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.37 |  | 384.9425 | 0.3708 | 390.11 | 382.13 | 0.4348 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 971.75 |  | 953.3958 | 1.9251 | 944.99 | 923 | 0.317 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 207.725 |  | 207.7607 | -0.0172 | 208.61 | 205.31 | 0.7269 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.47 |  | 403.5892 | -0.0295 | 405.78 | 397.185 | 4.667 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.385 |  | 46.5302 | -0.312 | 46.685 | 45.835 | 0.0431 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.14 |  | 24.9621 | 0.7125 | 24.77 | 24.34 | 0.0398 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.31 |  | 747.2054 | 0.1478 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.85 |  | 294.6824 | 0.3962 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.305 |  | 125.7807 | 0.4168 | 126.01 | 122.48 | 0.0554 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 77.815 |  | 78.5569 | -0.9444 | 76.615 | 74.55 | 0.8096 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.14 |  | 302.0471 | 0.6929 | 305.09 | 299.13 | 2.0024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.605 |  | 405.7402 | -0.7727 | 411.01 | 404.21 | 4.3392 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 638.94 |  | 638.7514 | 0.0295 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1083.55 |  | 1095.2095 | -1.0646 | 1140.63 | 1103.815 | 3.9574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 471.22 |  | 470.1089 | 0.2364 | 475.98 | 467.01 | 0.1889 | watch_only | none |
| JCI | data_center_power_cooling | 142.16 |  | 141.8683 | 0.2056 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.12 |  | 175.0634 | -0.5389 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.71 |  | 313.1175 | 0.828 | 309.72 | 302.3 | 0.9819 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 833.89 |  | 825.534 | 1.0122 | 823.31 | 800.37 | 0.7627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 405.43 |  | 405.6693 | -0.059 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 118.06 |  | 116.583 | 1.2669 | 109.39 | 107.58 | 2.4733 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 321.54 |  | 325.3119 | -1.1595 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.315 |  | 1809.3731 | -0.2243 | 1804.54 | 1786.51 | 0.1036 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.04 |  | 564.7828 | 0.2226 | 564.91 | 552.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 321.24 |  | 320.5045 | 0.2295 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.62 |  | 216.9591 | 0.3046 | 220.76 | 214.41 | 1.5256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 378.27 |  | 371.9007 | 1.7126 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 300.23 |  | 297.3544 | 0.9671 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.75 |  | 66.1799 | 0.8614 | 66.54 | 65 | 5.0637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 140.4 |  | 141.4638 | -0.752 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.125 |  | 340.409 | 1.3854 | 340.205 | 336.3 | 4.3491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.25 |  | 506.39 | -0.0277 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 297.81 |  | 299.2995 | -0.4977 | 301.84 | 296.5 | 4.6842 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.08 |  | 30.2842 | -0.6742 | 29.735 | 28.785 | 0.0665 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.4 |  | 41.7331 | -3.1942 | 41.65 | 40.435 | 0.0495 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.91 |  | 24.0188 | -0.4531 | 23.32 | 22.79 | 0.0836 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1553.19 |  | 1543.7976 | 0.6084 | 1540.85 | 1490.29 | 3.9918 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 546.3 |  | 541.0868 | 0.9635 | 533.56 | 517.335 | 0.1062 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 889.32 |  | 879.0539 | 1.1679 | 866.73 | 845.78 | 0.271 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.555 |  | 247.837 | -0.1138 | 248.915 | 247.32 | 0.5978 | below_vwap | below_vwap,spread_too_wide |
| META | cloud_ai_capex | 647.04 |  | 647.3478 | -0.0475 | 655.425 | 643.54 | 0.8454 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 289.7 |  | 286.8616 | 0.9895 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 169.9 |  | 167.2918 | 1.5591 | 165.88 | 160.77 | 1.4008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
