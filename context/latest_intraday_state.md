# Intraday State

- Generated at: `2026-07-22T03:33:48+08:00`
- Market time ET: `2026-07-21T15:33:49-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'spread_too_wide_or_missing': 19, 'watch_only': 3, 'price_stale_or_missing': 1, 'below_vwap': 19, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.71 |  | 707.5033 | 0.1706 | 707.09 | 704.52 | 0.0183 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 550.97 |  | 549.8101 | 0.211 | 550.77 | 545.11 | 0.0581 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 582.9 |  | 581.568 | 0.229 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.255 |  | 747.3286 | 0.124 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 582.9 |  | 581.568 | 0.229 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 550.97 |  | 549.8101 | 0.211 | 550.77 | 545.11 | 0.0581 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.71 |  | 707.5033 | 0.1706 | 707.09 | 704.52 | 0.0183 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.255 |  | 747.3286 | 0.124 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 5 | LITE | ai_networking_optical | 835.51 |  | 826.0805 | 1.1415 | 823.31 | 800.37 | 0.2609 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 296.16 |  | 294.7378 | 0.4825 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 327.785 |  | 326.4611 | 0.4055 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 126.59 |  | 125.8307 | 0.6034 | 126.01 | 122.48 | 0.0316 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.23 |  | 24.9762 | 1.0164 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.34 |  | 70.8497 | 0.6921 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 582.9 |  | 581.568 | 0.229 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 550.97 |  | 549.8101 | 0.211 | 550.77 | 545.11 | 0.0581 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.71 |  | 707.5033 | 0.1706 | 707.09 | 704.52 | 0.0183 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.255 |  | 747.3286 | 0.124 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 296.16 |  | 294.7378 | 0.4825 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 349.59 |  | 349.1318 | 0.1312 | 350.985 | 347.69 | 0.0257 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 327.785 |  | 326.4611 | 0.4055 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 126.59 |  | 125.8307 | 0.6034 | 126.01 | 122.48 | 0.0316 | buy_precheck_manual_confirm | none |
| 9 | MSFT | cloud_ai_capex | 399.285 |  | 399.0865 | 0.0497 | 401.45 | 396.36 | 0.0225 | watch_only | none |
| 10 | AVGO | custom_silicon_networking | 385.56 |  | 385.0195 | 0.1404 | 390.11 | 382.13 | 0.1971 | watch_only | none |
| 11 | ARM | ai_accelerator | 287.16 |  | 286.9214 | 0.0832 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | LITE | ai_networking_optical | 835.51 |  | 826.0805 | 1.1415 | 823.31 | 800.37 | 0.2609 | buy_precheck_manual_confirm | none |
| 13 | CIEN | ai_networking_optical | 406.215 |  | 405.6487 | 0.1396 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMCI | ai_server_oem | 25.23 |  | 24.9762 | 1.0164 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 15 | VRT | data_center_power_cooling | 302.82 |  | 302.1104 | 0.2349 | 305.09 | 299.13 | 4.2269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMKR | semiconductor_test_packaging | 66.405 |  | 66.2146 | 0.2876 | 66.54 | 65 | 4.7436 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | NVDA | ai_accelerator | 206.96 |  | 206.1568 | 0.3896 | 208.61 | 206.275 | 0.6571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 322.07 |  | 320.6274 | 0.4499 | 328.135 | 317.17 | 5.0331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ONTO | semiconductor_test_packaging | 298.955 |  | 297.6356 | 0.4433 | 296.68 | 291.36 | 4.5726 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TSM | foundry | 423.71 |  | 421.1411 | 0.61 | 418.76 | 415.025 | 0.5711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 582.9 |  | 581.568 | 0.229 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 550.97 |  | 549.8101 | 0.211 | 550.77 | 545.11 | 0.0581 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.71 |  | 707.5033 | 0.1706 | 707.09 | 704.52 | 0.0183 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.255 |  | 747.3286 | 0.124 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 5 | LITE | ai_networking_optical | 835.51 |  | 826.0805 | 1.1415 | 823.31 | 800.37 | 0.2609 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 296.16 |  | 294.7378 | 0.4825 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 327.785 |  | 326.4611 | 0.4055 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 126.59 |  | 125.8307 | 0.6034 | 126.01 | 122.48 | 0.0316 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 25.23 |  | 24.9762 | 1.0164 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.34 |  | 70.8497 | 0.6921 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 23.98 |  | 24.0024 | -0.0934 | 23.32 | 22.79 | 0.0417 | below_vwap | below_vwap |
| 12 | TSM | foundry | 423.71 |  | 421.1411 | 0.61 | 418.76 | 415.025 | 0.5711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | CRWV | gpu_cloud_ai_factory | 78.31 |  | 78.5169 | -0.2635 | 76.615 | 74.55 | 2.6433 | below_vwap | below_vwap,spread_too_wide |
| 14 | APLD | high_beta_ai_infrastructure | 29.93 |  | 30.2494 | -1.0559 | 29.735 | 28.785 | 0.0668 | below_vwap | below_vwap |
| 15 | AMD | ai_accelerator | 540.735 |  | 535.9986 | 0.8837 | 532.365 | 524.72 | 1.2612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 966.03 |  | 954.8471 | 1.1712 | 944.99 | 923 | 1.4378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | CIEN | ai_networking_optical | 406.215 |  | 405.6487 | 0.1396 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 893.25 |  | 880.5443 | 1.4429 | 866.73 | 845.78 | 0.8217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ARM | ai_accelerator | 287.16 |  | 286.9214 | 0.0832 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 543.97 |  | 541.3125 | 0.4909 | 533.56 | 517.335 | 1.6196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.71 |  | 707.5033 | 0.1706 | 707.09 | 704.52 | 0.0183 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.34 |  | 70.8497 | 0.6921 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.96 |  | 206.1568 | 0.3896 | 208.61 | 206.275 | 0.6571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 399.285 |  | 399.0865 | 0.0497 | 401.45 | 396.36 | 0.0225 | watch_only | none |
| AAPL | mega_cap_platform | 327.785 |  | 326.4611 | 0.4055 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.59 |  | 349.1318 | 0.1312 | 350.985 | 347.69 | 0.0257 | watch_only | none |
| AMD | ai_accelerator | 540.735 |  | 535.9986 | 0.8837 | 532.365 | 524.72 | 1.2612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.71 |  | 421.1411 | 0.61 | 418.76 | 415.025 | 0.5711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.97 |  | 549.8101 | 0.211 | 550.77 | 545.11 | 0.0581 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 582.9 |  | 581.568 | 0.229 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.56 |  | 385.0195 | 0.1404 | 390.11 | 382.13 | 0.1971 | watch_only | none |
| MU | memory_hbm_storage | 966.03 |  | 954.8471 | 1.1712 | 944.99 | 923 | 1.4378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 206.51 |  | 207.7197 | -0.5824 | 208.61 | 205.31 | 0.1307 | below_vwap | below_vwap |
| DELL | ai_server_oem | 402.63 |  | 403.523 | -0.2213 | 405.78 | 397.185 | 4.873 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.295 |  | 46.4887 | -0.4166 | 46.685 | 45.835 | 0.0216 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.23 |  | 24.9762 | 1.0164 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.255 |  | 747.3286 | 0.124 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.16 |  | 294.7378 | 0.4825 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.59 |  | 125.8307 | 0.6034 | 126.01 | 122.48 | 0.0316 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 78.31 |  | 78.5169 | -0.2635 | 76.615 | 74.55 | 2.6433 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.82 |  | 302.1104 | 0.2349 | 305.09 | 299.13 | 4.2269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.86 |  | 405.4314 | -0.6342 | 411.01 | 404.21 | 0.0621 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 638.4 |  | 638.6646 | -0.0414 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1073.43 |  | 1093.6484 | -1.8487 | 1140.63 | 1103.815 | 4.2853 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 469.365 |  | 470.1171 | -0.16 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 141.675 |  | 141.8793 | -0.144 | 142.15 | 140.105 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 173.95 |  | 174.9959 | -0.5976 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 316.75 |  | 313.4044 | 1.0675 | 309.72 | 302.3 | 2.5699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 835.51 |  | 826.0805 | 1.1415 | 823.31 | 800.37 | 0.2609 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 406.215 |  | 405.6487 | 0.1396 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 118.16 |  | 116.6997 | 1.2513 | 109.39 | 107.58 | 4.2316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 315.64 |  | 323.8219 | -2.5267 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1802.395 |  | 1808.9708 | -0.3635 | 1804.54 | 1786.51 | 0.0505 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 563.08 |  | 564.7677 | -0.2988 | 564.91 | 552.71 | 0.5719 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 322.07 |  | 320.6274 | 0.4499 | 328.135 | 317.17 | 5.0331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.945 |  | 216.9846 | -0.0182 | 220.76 | 214.41 | 0.0369 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 373.05 |  | 372.2888 | 0.2045 | 365.97 | 356.39 | 4.7071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 298.955 |  | 297.6356 | 0.4433 | 296.68 | 291.36 | 4.5726 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.405 |  | 66.2146 | 0.2876 | 66.54 | 65 | 4.7436 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.87 |  | 55.2551 | 1.1128 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.74 |  | 141.2512 | -1.0698 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 344.68 |  | 340.6628 | 1.1792 | 340.205 | 336.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.07 |  | 506.3954 | -0.0643 | 512.83 | 507.675 | 4.037 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 297.785 |  | 299.0951 | -0.438 | 301.84 | 296.5 | 0.0907 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 29.93 |  | 30.2494 | -1.0559 | 29.735 | 28.785 | 0.0668 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.805 |  | 41.6108 | -1.9365 | 41.65 | 40.435 | 0.049 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.98 |  | 24.0024 | -0.0934 | 23.32 | 22.79 | 0.0417 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1566.87 |  | 1544.7953 | 1.429 | 1540.85 | 1490.29 | 1.1456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 543.97 |  | 541.3125 | 0.4909 | 533.56 | 517.335 | 1.6196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 893.25 |  | 880.5443 | 1.4429 | 866.73 | 845.78 | 0.8217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.58 |  | 247.8161 | -0.0953 | 248.915 | 247.32 | 0.1131 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.41 |  | 647.4275 | -0.0027 | 655.425 | 643.54 | 1.384 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 287.16 |  | 286.9214 | 0.0832 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 170.58 |  | 167.4736 | 1.8548 | 165.88 | 160.77 | 0.4221 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
