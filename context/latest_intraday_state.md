# Intraday State

- Generated at: `2026-07-22T03:06:27+08:00`
- Market time ET: `2026-07-21T15:06:28-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'spread_too_wide_or_missing': 23, 'below_vwap': 16, 'price_stale_or_missing': 2, 'watch_only': 2, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.06 |  | 707.3604 | 0.2403 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 552.52 |  | 549.5403 | 0.5422 | 550.77 | 545.11 | 0.0398 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.24 |  | 581.419 | 0.4852 | 582.03 | 576.57 | 0.0223 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.32 |  | 747.2225 | 0.1469 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 425.12 |  | 420.8915 | 1.0047 | 418.76 | 415.025 | 0.1129 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.24 |  | 581.419 | 0.4852 | 582.03 | 576.57 | 0.0223 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.52 |  | 549.5403 | 0.5422 | 550.77 | 545.11 | 0.0398 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.06 |  | 707.3604 | 0.2403 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.32 |  | 747.2225 | 0.1469 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.96 |  | 294.6938 | 0.4297 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.105 |  | 125.7966 | 0.2451 | 126.01 | 122.48 | 0.0793 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 25.2 |  | 24.966 | 0.9375 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.435 |  | 70.8272 | 0.8582 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 709.06 |  | 707.3604 | 0.2403 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.32 |  | 747.2225 | 0.1469 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | ORCL | cloud_ai_capex | 126.105 |  | 125.7966 | 0.2451 | 126.01 | 122.48 | 0.0793 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 552.52 |  | 549.5403 | 0.5422 | 550.77 | 545.11 | 0.0398 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 584.24 |  | 581.419 | 0.4852 | 582.03 | 576.57 | 0.0223 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.96 |  | 294.6938 | 0.4297 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 142.09 |  | 141.8737 | 0.1525 | 142.15 | 140.105 | 0.0352 | watch_only | none |
| 8 | AVGO | custom_silicon_networking | 386.095 |  | 384.952 | 0.2969 | 390.11 | 382.13 | 0.1684 | watch_only | none |
| 9 | TT | data_center_power_cooling | 471.26 |  | 470.1228 | 0.2419 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TSM | foundry | 425.12 |  | 420.8915 | 1.0047 | 418.76 | 415.025 | 0.1129 | buy_precheck_manual_confirm | none |
| 11 | AMAT | semiconductor_equipment | 564.94 |  | 564.8036 | 0.0241 | 564.91 | 552.71 | 1.0267 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SMCI | ai_server_oem | 25.2 |  | 24.966 | 0.9375 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 13 | LRCX | semiconductor_equipment | 321.79 |  | 320.5452 | 0.3883 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | MRVL | custom_silicon_networking | 207.81 |  | 207.7619 | 0.0232 | 208.61 | 205.31 | 0.9143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | KLAC | semiconductor_equipment | 217.885 |  | 216.9732 | 0.4202 | 220.76 | 214.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | META | cloud_ai_capex | 647.985 |  | 647.3423 | 0.0993 | 655.425 | 643.54 | 1.2331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ARM | ai_accelerator | 288.58 |  | 286.888 | 0.5898 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | NVDA | ai_accelerator | 206.835 |  | 206.1098 | 0.3519 | 208.61 | 206.275 | 0.3916 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMKR | semiconductor_test_packaging | 66.7 |  | 66.199 | 0.7567 | 66.54 | 65 | 0.9295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | VRT | data_center_power_cooling | 303.71 |  | 302.0793 | 0.5398 | 305.09 | 299.13 | 1.8735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 425.12 |  | 420.8915 | 1.0047 | 418.76 | 415.025 | 0.1129 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.24 |  | 581.419 | 0.4852 | 582.03 | 576.57 | 0.0223 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.52 |  | 549.5403 | 0.5422 | 550.77 | 545.11 | 0.0398 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.06 |  | 707.3604 | 0.2403 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.32 |  | 747.2225 | 0.1469 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.96 |  | 294.6938 | 0.4297 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.105 |  | 125.7966 | 0.2451 | 126.01 | 122.48 | 0.0793 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 25.2 |  | 24.966 | 0.9375 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.435 |  | 70.8272 | 0.8582 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1805.475 |  | 1809.3107 | -0.212 | 1804.54 | 1786.51 | 0.0631 | below_vwap | below_vwap |
| 11 | CIEN | ai_networking_optical | 404.92 |  | 405.6661 | -0.1839 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | CORZ | high_beta_ai_infrastructure | 23.925 |  | 24.0159 | -0.3786 | 23.32 | 22.79 | 0.0418 | below_vwap | below_vwap |
| 13 | CRWV | gpu_cloud_ai_factory | 77.89 |  | 78.5411 | -0.8289 | 76.615 | 74.55 | 3.0042 | below_vwap | below_vwap,spread_too_wide |
| 14 | APLD | high_beta_ai_infrastructure | 30.13 |  | 30.2801 | -0.4958 | 29.735 | 28.785 | 0.0332 | below_vwap | below_vwap |
| 15 | AMD | ai_accelerator | 542.63 |  | 535.6078 | 1.3111 | 532.365 | 524.72 | 1.0707 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 971.175 |  | 953.7799 | 1.8238 | 944.99 | 923 | 0.695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 835.215 |  | 825.6507 | 1.1584 | 823.31 | 800.37 | 1.317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 564.94 |  | 564.8036 | 0.0241 | 564.91 | 552.71 | 1.0267 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 893.9 |  | 879.3498 | 1.6547 | 866.73 | 845.78 | 2.0181 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 288.58 |  | 286.888 | 0.5898 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.06 |  | 707.3604 | 0.2403 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.435 |  | 70.8272 | 0.8582 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.835 |  | 206.1098 | 0.3519 | 208.61 | 206.275 | 0.3916 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 398.51 |  | 399.0811 | -0.1431 | 401.45 | 396.36 | 0.0903 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.15 |  | 326.34 | 0.5546 | 325.59 | 322.63 | 1.3104 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 348.88 |  | 349.1087 | -0.0655 | 350.985 | 347.69 | 0.0086 | below_vwap | below_vwap |
| AMD | ai_accelerator | 542.63 |  | 535.6078 | 1.3111 | 532.365 | 524.72 | 1.0707 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 425.12 |  | 420.8915 | 1.0047 | 418.76 | 415.025 | 0.1129 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.52 |  | 549.5403 | 0.5422 | 550.77 | 545.11 | 0.0398 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.24 |  | 581.419 | 0.4852 | 582.03 | 576.57 | 0.0223 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.095 |  | 384.952 | 0.2969 | 390.11 | 382.13 | 0.1684 | watch_only | none |
| MU | memory_hbm_storage | 971.175 |  | 953.7799 | 1.8238 | 944.99 | 923 | 0.695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.81 |  | 207.7619 | 0.0232 | 208.61 | 205.31 | 0.9143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.395 |  | 403.5918 | -0.0488 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.25 |  | 46.5257 | -0.5926 | 46.685 | 45.835 | 0.0432 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.2 |  | 24.966 | 0.9375 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.32 |  | 747.2225 | 0.1469 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.96 |  | 294.6938 | 0.4297 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.105 |  | 125.7966 | 0.2451 | 126.01 | 122.48 | 0.0793 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 77.89 |  | 78.5411 | -0.8289 | 76.615 | 74.55 | 3.0042 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.71 |  | 302.0793 | 0.5398 | 305.09 | 299.13 | 1.8735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 403.26 |  | 405.6993 | -0.6013 | 411.01 | 404.21 | 4.5157 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 638.355 |  | 638.7479 | -0.0615 | 645.815 | 635.91 | 0.152 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1081.81 |  | 1094.9911 | -1.2038 | 1140.63 | 1103.815 | 2.9081 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 471.26 |  | 470.1228 | 0.2419 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.09 |  | 141.8737 | 0.1525 | 142.15 | 140.105 | 0.0352 | watch_only | none |
| ANET | ai_networking_optical | 174.42 |  | 175.0553 | -0.3629 | 176.06 | 172.32 | 0.1204 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 315.715 |  | 313.1534 | 0.818 | 309.72 | 302.3 | 4.5706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 835.215 |  | 825.6507 | 1.1584 | 823.31 | 800.37 | 1.317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 404.92 |  | 405.6661 | -0.1839 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 118.7 |  | 116.614 | 1.7888 | 109.39 | 107.58 | 2.064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 320.715 |  | 325.2383 | -1.3908 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.475 |  | 1809.3107 | -0.212 | 1804.54 | 1786.51 | 0.0631 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.94 |  | 564.8036 | 0.0241 | 564.91 | 552.71 | 1.0267 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.79 |  | 320.5452 | 0.3883 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.885 |  | 216.9732 | 0.4202 | 220.76 | 214.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TER | semiconductor_test_packaging | 378.22 |  | 372.0295 | 1.664 | 365.97 | 356.39 | 4.2303 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 300.14 |  | 297.3821 | 0.9274 | 296.68 | 291.36 | 0.5198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.7 |  | 66.199 | 0.7567 | 66.54 | 65 | 0.9295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.99 |  | 141.4297 | -1.018 | 142.09 | 139.41 | 4.2717 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 345.24 |  | 340.4317 | 1.4124 | 340.205 | 336.3 | 4.4751 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.43 |  | 506.3901 | 0.0079 | 512.83 | 507.675 | 4.1171 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 298.055 |  | 299.2851 | -0.411 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.13 |  | 30.2801 | -0.4958 | 29.735 | 28.785 | 0.0332 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.73 |  | 41.6984 | -2.3224 | 41.65 | 40.435 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.925 |  | 24.0159 | -0.3786 | 23.32 | 22.79 | 0.0418 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1557 |  | 1544.0064 | 0.8416 | 1540.85 | 1490.29 | 1.5986 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 546.77 |  | 541.1479 | 1.0389 | 533.56 | 517.335 | 1.4631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 893.9 |  | 879.3498 | 1.6547 | 866.73 | 845.78 | 2.0181 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.57 |  | 247.8289 | -0.1045 | 248.915 | 247.32 | 0.0525 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.985 |  | 647.3423 | 0.0993 | 655.425 | 643.54 | 1.2331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 288.58 |  | 286.888 | 0.5898 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 171.08 |  | 167.3675 | 2.2182 | 165.88 | 160.77 | 0.6897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
