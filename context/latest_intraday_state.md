# Intraday State

- Generated at: `2026-07-22T00:53:10+08:00`
- Market time ET: `2026-07-21T12:53:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 20, 'below_opening_15m_low': 3, 'below_vwap': 4, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 2, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.56 |  | 706.3984 | 0.4476 | 707.09 | 704.52 | 0.0352 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 554.37 |  | 548.1842 | 1.1284 | 550.77 | 545.11 | 0.0487 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.46 |  | 579.9124 | 0.7842 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.875 |  | 746.5868 | 0.3065 | 746.6 | 744.3 | 0.0214 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.55 |  | 418.8022 | 0.8949 | 418.76 | 415.025 | 0.1041 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.46 |  | 579.9124 | 0.7842 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.37 |  | 548.1842 | 1.1284 | 550.77 | 545.11 | 0.0487 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.56 |  | 706.3984 | 0.4476 | 707.09 | 704.52 | 0.0352 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.875 |  | 746.5868 | 0.3065 | 746.6 | 744.3 | 0.0214 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 978.895 |  | 945.4431 | 3.5382 | 944.99 | 923 | 0.1481 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1817.41 |  | 1808.2537 | 0.5064 | 1804.54 | 1786.51 | 0.044 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 305.64 |  | 300.9863 | 1.5462 | 305.09 | 299.13 | 0.1178 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 209.96 |  | 207.4506 | 1.2096 | 208.61 | 205.31 | 0.1572 | buy_precheck_manual_confirm | none |
| 10 | IWM | market_regime | 296.16 |  | 294.3525 | 0.6141 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 11 | DELL | ai_server_oem | 406.835 |  | 403.3851 | 0.8552 | 405.78 | 397.185 | 0.1843 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.96 |  | 46.4775 | 1.0382 | 46.685 | 45.835 | 0.0426 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.8527 | 1.9802 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 41.98 |  | 41.7361 | 0.5843 | 41.65 | 40.435 | 0.0238 | buy_precheck_manual_confirm | none |
| 15 | AAPL | mega_cap_platform | 327.48 |  | 325.8396 | 0.5034 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 16 | ORCL | cloud_ai_capex | 126.65 |  | 125.2169 | 1.1445 | 126.01 | 122.48 | 0.3237 | buy_precheck_manual_confirm | none |
| 17 | AMKR | semiconductor_test_packaging | 66.895 |  | 65.8481 | 1.5899 | 66.54 | 65 | 0.1046 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 25.385 |  | 24.8272 | 2.2467 | 24.77 | 24.34 | 0.0394 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.37 |  | 30.1687 | 0.6673 | 29.735 | 28.785 | 0.0659 | buy_precheck_manual_confirm | none |
| 20 | TQQQ | leveraged_tool | 71.58 |  | 70.6959 | 1.2506 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.875 |  | 746.5868 | 0.3065 | 746.6 | 744.3 | 0.0214 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.56 |  | 706.3984 | 0.4476 | 707.09 | 704.52 | 0.0352 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 584.46 |  | 579.9124 | 0.7842 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1817.41 |  | 1808.2537 | 0.5064 | 1804.54 | 1786.51 | 0.044 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 296.16 |  | 294.3525 | 0.6141 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 247.945 |  | 247.7205 | 0.0906 | 248.915 | 247.32 | 0.0161 | watch_only | none |
| 7 | IREN | high_beta_ai_infrastructure | 41.98 |  | 41.7361 | 0.5843 | 41.65 | 40.435 | 0.0238 | buy_precheck_manual_confirm | none |
| 8 | AAPL | mega_cap_platform | 327.48 |  | 325.8396 | 0.5034 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 217.92 |  | 216.4649 | 0.6722 | 220.76 | 214.41 | 0.1101 | watch_only | none |
| 10 | AVGO | custom_silicon_networking | 387 |  | 384.5863 | 0.6276 | 390.11 | 382.13 | 0.2972 | watch_only | none |
| 11 | SOXX | semiconductor_index | 554.37 |  | 548.1842 | 1.1284 | 550.77 | 545.11 | 0.0487 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 30.37 |  | 30.1687 | 0.6673 | 29.735 | 28.785 | 0.0659 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 46.96 |  | 46.4775 | 1.0382 | 46.685 | 45.835 | 0.0426 | buy_precheck_manual_confirm | none |
| 14 | DELL | ai_server_oem | 406.835 |  | 403.3851 | 0.8552 | 405.78 | 397.185 | 0.1843 | buy_precheck_manual_confirm | none |
| 15 | TSM | foundry | 422.55 |  | 418.8022 | 0.8949 | 418.76 | 415.025 | 0.1041 | buy_precheck_manual_confirm | none |
| 16 | MRVL | custom_silicon_networking | 209.96 |  | 207.4506 | 1.2096 | 208.61 | 205.31 | 0.1572 | buy_precheck_manual_confirm | none |
| 17 | ANET | ai_networking_optical | 175.37 |  | 175.237 | 0.0759 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ORCL | cloud_ai_capex | 126.65 |  | 125.2169 | 1.1445 | 126.01 | 122.48 | 0.3237 | buy_precheck_manual_confirm | none |
| 19 | ETN | data_center_power_cooling | 407.09 |  | 406.0523 | 0.2556 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | VRT | data_center_power_cooling | 305.64 |  | 300.9863 | 1.5462 | 305.09 | 299.13 | 0.1178 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.55 |  | 418.8022 | 0.8949 | 418.76 | 415.025 | 0.1041 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.46 |  | 579.9124 | 0.7842 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.37 |  | 548.1842 | 1.1284 | 550.77 | 545.11 | 0.0487 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.56 |  | 706.3984 | 0.4476 | 707.09 | 704.52 | 0.0352 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.875 |  | 746.5868 | 0.3065 | 746.6 | 744.3 | 0.0214 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 978.895 |  | 945.4431 | 3.5382 | 944.99 | 923 | 0.1481 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1817.41 |  | 1808.2537 | 0.5064 | 1804.54 | 1786.51 | 0.044 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 305.64 |  | 300.9863 | 1.5462 | 305.09 | 299.13 | 0.1178 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 209.96 |  | 207.4506 | 1.2096 | 208.61 | 205.31 | 0.1572 | buy_precheck_manual_confirm | none |
| 10 | IWM | market_regime | 296.16 |  | 294.3525 | 0.6141 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 11 | DELL | ai_server_oem | 406.835 |  | 403.3851 | 0.8552 | 405.78 | 397.185 | 0.1843 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.96 |  | 46.4775 | 1.0382 | 46.685 | 45.835 | 0.0426 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.8527 | 1.9802 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 41.98 |  | 41.7361 | 0.5843 | 41.65 | 40.435 | 0.0238 | buy_precheck_manual_confirm | none |
| 15 | AAPL | mega_cap_platform | 327.48 |  | 325.8396 | 0.5034 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 16 | ORCL | cloud_ai_capex | 126.65 |  | 125.2169 | 1.1445 | 126.01 | 122.48 | 0.3237 | buy_precheck_manual_confirm | none |
| 17 | AMKR | semiconductor_test_packaging | 66.895 |  | 65.8481 | 1.5899 | 66.54 | 65 | 0.1046 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 25.385 |  | 24.8272 | 2.2467 | 24.77 | 24.34 | 0.0394 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.37 |  | 30.1687 | 0.6673 | 29.735 | 28.785 | 0.0659 | buy_precheck_manual_confirm | none |
| 20 | TQQQ | leveraged_tool | 71.58 |  | 70.6959 | 1.2506 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.56 |  | 706.3984 | 0.4476 | 707.09 | 704.52 | 0.0352 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.58 |  | 70.6959 | 1.2506 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.325 |  | 206.009 | -0.332 | 208.61 | 206.275 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.815 |  | 399.2029 | -0.0972 | 401.45 | 396.36 | 0.3561 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 327.48 |  | 325.8396 | 0.5034 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.11 |  | 349.1705 | -0.0173 | 350.985 | 347.69 | 0.0115 | below_vwap | below_vwap |
| AMD | ai_accelerator | 542.325 |  | 532.0772 | 1.926 | 532.365 | 524.72 | 1.0105 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.55 |  | 418.8022 | 0.8949 | 418.76 | 415.025 | 0.1041 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.37 |  | 548.1842 | 1.1284 | 550.77 | 545.11 | 0.0487 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.46 |  | 579.9124 | 0.7842 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 387 |  | 384.5863 | 0.6276 | 390.11 | 382.13 | 0.2972 | watch_only | none |
| MU | memory_hbm_storage | 978.895 |  | 945.4431 | 3.5382 | 944.99 | 923 | 0.1481 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 209.96 |  | 207.4506 | 1.2096 | 208.61 | 205.31 | 0.1572 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 406.835 |  | 403.3851 | 0.8552 | 405.78 | 397.185 | 0.1843 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 46.96 |  | 46.4775 | 1.0382 | 46.685 | 45.835 | 0.0426 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.385 |  | 24.8272 | 2.2467 | 24.77 | 24.34 | 0.0394 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.875 |  | 746.5868 | 0.3065 | 746.6 | 744.3 | 0.0214 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.16 |  | 294.3525 | 0.6141 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.65 |  | 125.2169 | 1.1445 | 126.01 | 122.48 | 0.3237 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 79.47 |  | 77.8246 | 2.1143 | 76.615 | 74.55 | 1.0193 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 305.64 |  | 300.9863 | 1.5462 | 305.09 | 299.13 | 0.1178 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.09 |  | 406.0523 | 0.2556 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 641.32 |  | 637.3847 | 0.6174 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1092.79 |  | 1097.6443 | -0.4422 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 472.27 |  | 469.5995 | 0.5687 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.45 |  | 141.5556 | 0.6318 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.37 |  | 175.237 | 0.0759 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 319.23 |  | 310.631 | 2.7682 | 309.72 | 302.3 | 3.3549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 835.75 |  | 822.1102 | 1.6591 | 823.31 | 800.37 | 1.7948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 411.08 |  | 405.2612 | 1.4358 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 119.19 |  | 115.1207 | 3.5348 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 325.94 |  | 325.9808 | -0.0125 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1817.41 |  | 1808.2537 | 0.5064 | 1804.54 | 1786.51 | 0.044 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 571.85 |  | 563.5622 | 1.4706 | 564.91 | 552.71 | 1.4409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 323.345 |  | 320.0294 | 1.036 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.92 |  | 216.4649 | 0.6722 | 220.76 | 214.41 | 0.1101 | watch_only | none |
| TER | semiconductor_test_packaging | 377.3 |  | 369.0635 | 2.2317 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.82 |  | 295.7504 | 2.0523 | 296.68 | 291.36 | 3.8102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.895 |  | 65.8481 | 1.5899 | 66.54 | 65 | 0.1046 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 55.82 |  | 54.8344 | 1.7973 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 142.85 |  | 140.9974 | 1.314 | 142.09 | 139.41 | 4.1092 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 347.06 |  | 339.2562 | 2.3003 | 340.205 | 336.3 | 4.0541 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 505.775 |  | 506.2841 | -0.1006 | 512.83 | 507.675 | 0.087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 299.26 |  | 298.7763 | 0.1619 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.37 |  | 30.1687 | 0.6673 | 29.735 | 28.785 | 0.0659 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.98 |  | 41.7361 | 0.5843 | 41.65 | 40.435 | 0.0238 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.8527 | 1.9802 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1575.84 |  | 1535.9172 | 2.5993 | 1540.85 | 1490.29 | 2.221 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 550.82 |  | 538.6268 | 2.2638 | 533.56 | 517.335 | 2.155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 895.64 |  | 874.9956 | 2.3594 | 866.73 | 845.78 | 0.6811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.945 |  | 247.7205 | 0.0906 | 248.915 | 247.32 | 0.0161 | watch_only | none |
| META | cloud_ai_capex | 648.18 |  | 647.4954 | 0.1057 | 655.425 | 643.54 | 1.3083 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 291.72 |  | 285.6083 | 2.1399 | 286.39 | 275.86 | 2.9617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 167.675 |  | 165.3065 | 1.4328 | 165.88 | 160.77 | 0.8588 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
