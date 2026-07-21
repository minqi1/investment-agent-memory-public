# Intraday State

- Generated at: `2026-07-22T01:04:49+08:00`
- Market time ET: `2026-07-21T13:04:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 19, 'below_opening_15m_low': 3, 'below_vwap': 5, 'watch_only': 3, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.65 |  | 706.4942 | 0.4467 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 554.25 |  | 548.3789 | 1.0706 | 550.77 | 545.11 | 0.0559 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.57 |  | 580.124 | 0.7664 | 582.03 | 576.57 | 0.0137 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.62 |  | 746.6508 | 0.2637 | 746.6 | 744.3 | 0.0187 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 423.18 |  | 418.9611 | 1.007 | 418.76 | 415.025 | 0.1087 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.57 |  | 580.124 | 0.7664 | 582.03 | 576.57 | 0.0137 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.25 |  | 548.3789 | 1.0706 | 550.77 | 545.11 | 0.0559 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.65 |  | 706.4942 | 0.4467 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.62 |  | 746.6508 | 0.2637 | 746.6 | 744.3 | 0.0187 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1819.335 |  | 1808.5342 | 0.5972 | 1804.54 | 1786.51 | 0.0297 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 569.84 |  | 563.6996 | 1.0893 | 564.91 | 552.71 | 0.1369 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 209.675 |  | 207.5078 | 1.0444 | 208.61 | 205.31 | 0.0382 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 296.15 |  | 294.4085 | 0.5915 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.855 |  | 46.4902 | 0.7846 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 551.76 |  | 538.9033 | 2.3857 | 533.56 | 517.335 | 0.1559 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.41 |  | 23.867 | 2.275 | 23.32 | 22.79 | 0.041 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.485 |  | 41.7742 | 1.7015 | 41.65 | 40.435 | 0.0235 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 327.88 |  | 325.9467 | 0.5931 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 15 | ORCL | cloud_ai_capex | 126.25 |  | 125.2971 | 0.7605 | 126.01 | 122.48 | 0.1426 | buy_precheck_manual_confirm | none |
| 16 | AAOI | ai_networking_optical | 119.43 |  | 115.4337 | 3.462 | 109.39 | 107.58 | 0.1926 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 25.33 |  | 24.8371 | 1.9845 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.59 |  | 30.1734 | 1.3806 | 29.735 | 28.785 | 0.0327 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.6 |  | 70.716 | 1.2501 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.62 |  | 746.6508 | 0.2637 | 746.6 | 744.3 | 0.0187 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.57 |  | 580.124 | 0.7664 | 582.03 | 576.57 | 0.0137 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.65 |  | 706.4942 | 0.4467 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 126.25 |  | 125.2971 | 0.7605 | 126.01 | 122.48 | 0.1426 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 296.15 |  | 294.4085 | 0.5915 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.855 |  | 46.4902 | 0.7846 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 349.535 |  | 349.179 | 0.1019 | 350.985 | 347.69 | 0.0429 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 327.88 |  | 325.9467 | 0.5931 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1819.335 |  | 1808.5342 | 0.5972 | 1804.54 | 1786.51 | 0.0297 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.025 |  | 247.735 | 0.1171 | 248.915 | 247.32 | 0.3266 | watch_only | none |
| 11 | AVGO | custom_silicon_networking | 386.575 |  | 384.6175 | 0.509 | 390.11 | 382.13 | 0.3363 | watch_only | none |
| 12 | SOXX | semiconductor_index | 554.25 |  | 548.3789 | 1.0706 | 550.77 | 545.11 | 0.0559 | buy_precheck_manual_confirm | none |
| 13 | MRVL | custom_silicon_networking | 209.675 |  | 207.5078 | 1.0444 | 208.61 | 205.31 | 0.0382 | buy_precheck_manual_confirm | none |
| 14 | TSM | foundry | 423.18 |  | 418.9611 | 1.007 | 418.76 | 415.025 | 0.1087 | buy_precheck_manual_confirm | none |
| 15 | AMAT | semiconductor_equipment | 569.84 |  | 563.6996 | 1.0893 | 564.91 | 552.71 | 0.1369 | buy_precheck_manual_confirm | none |
| 16 | JCI | data_center_power_cooling | 142.61 |  | 141.7897 | 0.5785 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | DELL | ai_server_oem | 405.94 |  | 403.4921 | 0.6067 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | APLD | high_beta_ai_infrastructure | 30.59 |  | 30.1734 | 1.3806 | 29.735 | 28.785 | 0.0327 | buy_precheck_manual_confirm | none |
| 19 | TT | data_center_power_cooling | 471.42 |  | 469.6795 | 0.3706 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 640.98 |  | 637.4959 | 0.5465 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 423.18 |  | 418.9611 | 1.007 | 418.76 | 415.025 | 0.1087 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 584.57 |  | 580.124 | 0.7664 | 582.03 | 576.57 | 0.0137 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.25 |  | 548.3789 | 1.0706 | 550.77 | 545.11 | 0.0559 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.65 |  | 706.4942 | 0.4467 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.62 |  | 746.6508 | 0.2637 | 746.6 | 744.3 | 0.0187 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1819.335 |  | 1808.5342 | 0.5972 | 1804.54 | 1786.51 | 0.0297 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 569.84 |  | 563.6996 | 1.0893 | 564.91 | 552.71 | 0.1369 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 209.675 |  | 207.5078 | 1.0444 | 208.61 | 205.31 | 0.0382 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 296.15 |  | 294.4085 | 0.5915 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.855 |  | 46.4902 | 0.7846 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 551.76 |  | 538.9033 | 2.3857 | 533.56 | 517.335 | 0.1559 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.41 |  | 23.867 | 2.275 | 23.32 | 22.79 | 0.041 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.485 |  | 41.7742 | 1.7015 | 41.65 | 40.435 | 0.0235 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 327.88 |  | 325.9467 | 0.5931 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 15 | ORCL | cloud_ai_capex | 126.25 |  | 125.2971 | 0.7605 | 126.01 | 122.48 | 0.1426 | buy_precheck_manual_confirm | none |
| 16 | AAOI | ai_networking_optical | 119.43 |  | 115.4337 | 3.462 | 109.39 | 107.58 | 0.1926 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 25.33 |  | 24.8371 | 1.9845 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.59 |  | 30.1734 | 1.3806 | 29.735 | 28.785 | 0.0327 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.6 |  | 70.716 | 1.2501 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 20 | AMD | ai_accelerator | 542.27 |  | 532.3957 | 1.8547 | 532.365 | 524.72 | 0.6122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.65 |  | 706.4942 | 0.4467 | 707.09 | 704.52 | 0.0028 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.6 |  | 70.716 | 1.2501 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.3 |  | 205.9815 | -0.3309 | 208.61 | 206.275 | 1.0229 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 398.495 |  | 399.1925 | -0.1747 | 401.45 | 396.36 | 0.0527 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.88 |  | 325.9467 | 0.5931 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.535 |  | 349.179 | 0.1019 | 350.985 | 347.69 | 0.0429 | watch_only | none |
| AMD | ai_accelerator | 542.27 |  | 532.3957 | 1.8547 | 532.365 | 524.72 | 0.6122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.18 |  | 418.9611 | 1.007 | 418.76 | 415.025 | 0.1087 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.25 |  | 548.3789 | 1.0706 | 550.77 | 545.11 | 0.0559 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.57 |  | 580.124 | 0.7664 | 582.03 | 576.57 | 0.0137 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.575 |  | 384.6175 | 0.509 | 390.11 | 382.13 | 0.3363 | watch_only | none |
| MU | memory_hbm_storage | 981.5 |  | 947.0094 | 3.6421 | 944.99 | 923 | 0.8864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.675 |  | 207.5078 | 1.0444 | 208.61 | 205.31 | 0.0382 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 405.94 |  | 403.4921 | 0.6067 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.855 |  | 46.4902 | 0.7846 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.33 |  | 24.8371 | 1.9845 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.62 |  | 746.6508 | 0.2637 | 746.6 | 744.3 | 0.0187 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.15 |  | 294.4085 | 0.5915 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.25 |  | 125.2971 | 0.7605 | 126.01 | 122.48 | 0.1426 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 80.185 |  | 77.9695 | 2.8415 | 76.615 | 74.55 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 304.92 |  | 301.0897 | 1.2722 | 305.09 | 299.13 | 3.6173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.045 |  | 406.0871 | -0.0104 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 640.98 |  | 637.4959 | 0.5465 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1092.62 |  | 1097.5582 | -0.4499 | 1140.63 | 1103.815 | 0.4704 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 471.42 |  | 469.6795 | 0.3706 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.61 |  | 141.7897 | 0.5785 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.1 |  | 175.2355 | -0.0773 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 319.37 |  | 310.9879 | 2.6953 | 309.72 | 302.3 | 3.2689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 835.1 |  | 822.5144 | 1.5301 | 823.31 | 800.37 | 1.5124 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 410.395 |  | 405.3237 | 1.2512 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 119.43 |  | 115.4337 | 3.462 | 109.39 | 107.58 | 0.1926 | buy_precheck_manual_confirm | none |
| ALAB | ai_networking_optical | 325.88 |  | 325.9744 | -0.029 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1819.335 |  | 1808.5342 | 0.5972 | 1804.54 | 1786.51 | 0.0297 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 569.84 |  | 563.6996 | 1.0893 | 564.91 | 552.71 | 0.1369 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 322.93 |  | 320.2003 | 0.8525 | 328.135 | 317.17 | 4.6419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 217.73 |  | 216.5099 | 0.5636 | 220.76 | 214.41 | 1.4284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 375.9 |  | 369.2054 | 1.8133 | 365.97 | 356.39 | 4.6182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 301.9 |  | 296.1215 | 1.9514 | 296.68 | 291.36 | 3.5939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.845 |  | 65.8673 | 1.4843 | 66.54 | 65 | 1.3165 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.2 |  | 54.9647 | 2.2475 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 142.7 |  | 141.1449 | 1.1018 | 142.09 | 139.41 | 4.2537 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 346 |  | 339.5223 | 1.9079 | 340.205 | 336.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.9 |  | 506.3002 | 0.1185 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 299.6 |  | 298.8759 | 0.2423 | 301.84 | 296.5 | 5.0868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 30.59 |  | 30.1734 | 1.3806 | 29.735 | 28.785 | 0.0327 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.485 |  | 41.7742 | 1.7015 | 41.65 | 40.435 | 0.0235 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.41 |  | 23.867 | 2.275 | 23.32 | 22.79 | 0.041 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1580.61 |  | 1537.5842 | 2.7983 | 1540.85 | 1490.29 | 3.0937 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 551.76 |  | 538.9033 | 2.3857 | 533.56 | 517.335 | 0.1559 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 897.835 |  | 875.4536 | 2.5566 | 866.73 | 845.78 | 2.1396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.025 |  | 247.735 | 0.1171 | 248.915 | 247.32 | 0.3266 | watch_only | none |
| META | cloud_ai_capex | 647.73 |  | 647.602 | 0.0198 | 655.425 | 643.54 | 1.6504 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 290.95 |  | 285.6682 | 1.8489 | 286.39 | 275.86 | 2.9765 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.56 |  | 165.449 | 1.8803 | 165.88 | 160.77 | 1.0026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
