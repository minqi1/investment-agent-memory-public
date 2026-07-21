# Intraday State

- Generated at: `2026-07-22T02:54:45+08:00`
- Market time ET: `2026-07-21T14:54:46-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'spread_too_wide_or_missing': 22, 'below_vwap': 15, 'price_stale_or_missing': 2, 'watch_only': 2, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.23 |  | 707.3055 | 0.2721 | 707.09 | 704.52 | 0.0127 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 553.33 |  | 549.4262 | 0.7105 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.67 |  | 581.2795 | 0.5833 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.32 |  | 747.1925 | 0.1509 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.42 |  | 420.6962 | 0.8852 | 418.76 | 415.025 | 0.0353 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.67 |  | 581.2795 | 0.5833 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 553.33 |  | 549.4262 | 0.7105 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.23 |  | 707.3055 | 0.2721 | 707.09 | 704.52 | 0.0127 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.32 |  | 747.1925 | 0.1509 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.86 |  | 294.6785 | 0.4009 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 142.16 |  | 141.8683 | 0.2056 | 142.15 | 140.105 | 0.0703 | buy_precheck_manual_confirm | none |
| 8 | COHR | ai_networking_optical | 316.62 |  | 313.0834 | 1.1296 | 309.72 | 302.3 | 0.259 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 328.255 |  | 326.3174 | 0.5938 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.26 |  | 24.958 | 1.2101 | 24.77 | 24.34 | 0.0792 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.49 |  | 70.8203 | 0.9456 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 709.23 |  | 707.3055 | 0.2721 | 707.09 | 704.52 | 0.0127 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.32 |  | 747.1925 | 0.1509 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 142.16 |  | 141.8683 | 0.2056 | 142.15 | 140.105 | 0.0703 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 584.67 |  | 581.2795 | 0.5833 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 553.33 |  | 549.4262 | 0.7105 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 386.23 |  | 384.9325 | 0.3371 | 390.11 | 382.13 | 0.0362 | watch_only | none |
| 7 | IWM | market_regime | 295.86 |  | 294.6785 | 0.4009 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 217.71 |  | 216.9519 | 0.3494 | 220.76 | 214.41 | 0.2343 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 328.255 |  | 326.3174 | 0.5938 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 10 | TSM | foundry | 424.42 |  | 420.6962 | 0.8852 | 418.76 | 415.025 | 0.0353 | buy_precheck_manual_confirm | none |
| 11 | LRCX | semiconductor_equipment | 320.97 |  | 320.5023 | 0.1459 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TT | data_center_power_cooling | 471.015 |  | 470.0987 | 0.1949 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AMAT | semiconductor_equipment | 566.375 |  | 564.7778 | 0.2828 | 564.91 | 552.71 | 0.7168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SMCI | ai_server_oem | 25.26 |  | 24.958 | 1.2101 | 24.77 | 24.34 | 0.0792 | buy_precheck_manual_confirm | none |
| 15 | COHR | ai_networking_optical | 316.62 |  | 313.0834 | 1.1296 | 309.72 | 302.3 | 0.259 | buy_precheck_manual_confirm | none |
| 16 | MRVL | custom_silicon_networking | 207.91 |  | 207.7607 | 0.0718 | 208.61 | 205.31 | 0.683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | DELL | ai_server_oem | 404.2 |  | 403.5905 | 0.151 | 405.78 | 397.185 | 4.9258 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 407.57 |  | 405.6577 | 0.4714 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | NVDA | ai_accelerator | 207.17 |  | 206.0839 | 0.527 | 208.61 | 206.275 | 0.7289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | VRT | data_center_power_cooling | 303.87 |  | 302.0371 | 0.6068 | 305.09 | 299.13 | 1.9317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.42 |  | 420.6962 | 0.8852 | 418.76 | 415.025 | 0.0353 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.67 |  | 581.2795 | 0.5833 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 553.33 |  | 549.4262 | 0.7105 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.23 |  | 707.3055 | 0.2721 | 707.09 | 704.52 | 0.0127 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.32 |  | 747.1925 | 0.1509 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.86 |  | 294.6785 | 0.4009 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 142.16 |  | 141.8683 | 0.2056 | 142.15 | 140.105 | 0.0703 | buy_precheck_manual_confirm | none |
| 8 | COHR | ai_networking_optical | 316.62 |  | 313.0834 | 1.1296 | 309.72 | 302.3 | 0.259 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 328.255 |  | 326.3174 | 0.5938 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.26 |  | 24.958 | 1.2101 | 24.77 | 24.34 | 0.0792 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.49 |  | 70.8203 | 0.9456 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | ASML | semiconductor_equipment | 1805.42 |  | 1809.4018 | -0.2201 | 1804.54 | 1786.51 | 0.0227 | below_vwap | below_vwap |
| 13 | CORZ | high_beta_ai_infrastructure | 23.96 |  | 24.021 | -0.2541 | 23.32 | 22.79 | 0.0417 | below_vwap | below_vwap |
| 14 | CRWV | gpu_cloud_ai_factory | 78.21 |  | 78.564 | -0.4505 | 76.615 | 74.55 | 2.8257 | below_vwap | below_vwap,spread_too_wide |
| 15 | APLD | high_beta_ai_infrastructure | 30.17 |  | 30.2873 | -0.3874 | 29.735 | 28.785 | 0.0663 | below_vwap | below_vwap |
| 16 | AMD | ai_accelerator | 544.335 |  | 535.4396 | 1.6613 | 532.365 | 524.72 | 0.6632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MU | memory_hbm_storage | 972.35 |  | 953.3059 | 1.9977 | 944.99 | 923 | 0.4031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LITE | ai_networking_optical | 836.31 |  | 825.4602 | 1.3144 | 823.31 | 800.37 | 0.8358 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | CIEN | ai_networking_optical | 407.57 |  | 405.6577 | 0.4714 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMAT | semiconductor_equipment | 566.375 |  | 564.7778 | 0.2828 | 564.91 | 552.71 | 0.7168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.23 |  | 707.3055 | 0.2721 | 707.09 | 704.52 | 0.0127 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.49 |  | 70.8203 | 0.9456 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 207.17 |  | 206.0839 | 0.527 | 208.61 | 206.275 | 0.7289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 398.36 |  | 399.0997 | -0.1853 | 401.45 | 396.36 | 0.0276 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.255 |  | 326.3174 | 0.5938 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.37 |  | 349.1289 | -0.2174 | 350.985 | 347.69 | 0.0144 | below_vwap | below_vwap |
| AMD | ai_accelerator | 544.335 |  | 535.4396 | 1.6613 | 532.365 | 524.72 | 0.6632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 424.42 |  | 420.6962 | 0.8852 | 418.76 | 415.025 | 0.0353 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.33 |  | 549.4262 | 0.7105 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.67 |  | 581.2795 | 0.5833 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.23 |  | 384.9325 | 0.3371 | 390.11 | 382.13 | 0.0362 | watch_only | none |
| MU | memory_hbm_storage | 972.35 |  | 953.3059 | 1.9977 | 944.99 | 923 | 0.4031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.91 |  | 207.7607 | 0.0718 | 208.61 | 205.31 | 0.683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 404.2 |  | 403.5905 | 0.151 | 405.78 | 397.185 | 4.9258 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.425 |  | 46.5321 | -0.2301 | 46.685 | 45.835 | 0.0431 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.26 |  | 24.958 | 1.2101 | 24.77 | 24.34 | 0.0792 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.32 |  | 747.1925 | 0.1509 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.86 |  | 294.6785 | 0.4009 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.58 |  | 125.7728 | 0.6418 | 126.01 | 122.48 | 0.79 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.21 |  | 78.564 | -0.4505 | 76.615 | 74.55 | 2.8257 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.87 |  | 302.0371 | 0.6068 | 305.09 | 299.13 | 1.9317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.76 |  | 405.8214 | -0.7544 | 411.01 | 404.21 | 4.3127 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 638.725 |  | 638.7514 | -0.0041 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1082.3 |  | 1095.2594 | -1.1832 | 1140.63 | 1103.815 | 2.7146 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 471.015 |  | 470.0987 | 0.1949 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.16 |  | 141.8683 | 0.2056 | 142.15 | 140.105 | 0.0703 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 174.38 |  | 175.0797 | -0.3996 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 316.62 |  | 313.0834 | 1.1296 | 309.72 | 302.3 | 0.259 | buy_precheck_manual_confirm | none |
| LITE | ai_networking_optical | 836.31 |  | 825.4602 | 1.3144 | 823.31 | 800.37 | 0.8358 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 407.57 |  | 405.6577 | 0.4714 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 118.75 |  | 116.5664 | 1.8733 | 109.39 | 107.58 | 1.9368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 321.92 |  | 325.3536 | -1.0553 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.42 |  | 1809.4018 | -0.2201 | 1804.54 | 1786.51 | 0.0227 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.375 |  | 564.7778 | 0.2828 | 564.91 | 552.71 | 0.7168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.97 |  | 320.5023 | 0.1459 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.71 |  | 216.9519 | 0.3494 | 220.76 | 214.41 | 0.2343 | watch_only | none |
| TER | semiconductor_test_packaging | 378.215 |  | 371.8422 | 1.7138 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 299.91 |  | 297.3217 | 0.8705 | 296.68 | 291.36 | 3.421 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.755 |  | 66.1752 | 0.8762 | 66.54 | 65 | 4.1195 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 140.58 |  | 141.4793 | -0.6357 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.125 |  | 340.409 | 1.3854 | 340.205 | 336.3 | 4.3434 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.18 |  | 506.3903 | -0.0415 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 297.975 |  | 299.3026 | -0.4436 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.17 |  | 30.2873 | -0.3874 | 29.735 | 28.785 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.655 |  | 41.7467 | -2.6151 | 41.65 | 40.435 | 0.0492 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.96 |  | 24.021 | -0.2541 | 23.32 | 22.79 | 0.0417 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1555.35 |  | 1543.7494 | 0.7515 | 1540.85 | 1490.29 | 2.6541 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 547.51 |  | 541.0368 | 1.1964 | 533.56 | 517.335 | 0.4219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 891.44 |  | 878.9627 | 1.4195 | 866.73 | 845.78 | 1.0163 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.6 |  | 247.8411 | -0.0973 | 248.915 | 247.32 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.19 |  | 647.3537 | -0.0253 | 655.425 | 643.54 | 1.2346 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 289.905 |  | 286.8475 | 1.0659 | 286.39 | 275.86 | 2.1938 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 170.71 |  | 167.2679 | 2.0578 | 165.88 | 160.77 | 0.8787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
