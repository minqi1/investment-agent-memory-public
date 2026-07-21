# Intraday State

- Generated at: `2026-07-22T01:40:18+08:00`
- Market time ET: `2026-07-21T13:40:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 19, 'watch_only': 10, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 3, 'below_vwap': 5, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.67 |  | 706.7483 | 0.4134 | 707.09 | 704.52 | 0.0169 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 554.2 |  | 548.7204 | 0.9986 | 550.77 | 545.11 | 0.0613 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.19 |  | 580.6435 | 0.783 | 582.03 | 576.57 | 0.0256 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.68 |  | 746.9494 | 0.2317 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 423.72 |  | 419.815 | 0.9302 | 418.76 | 415.025 | 0.059 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.19 |  | 580.6435 | 0.783 | 582.03 | 576.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.2 |  | 548.7204 | 0.9986 | 550.77 | 545.11 | 0.0613 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.67 |  | 706.7483 | 0.4134 | 707.09 | 704.52 | 0.0169 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.68 |  | 746.9494 | 0.2317 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1813.945 |  | 1810.1411 | 0.2101 | 1804.54 | 1786.51 | 0.0358 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 567.74 |  | 564.3051 | 0.6087 | 564.91 | 552.71 | 0.1039 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 295.81 |  | 294.5385 | 0.4317 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.74 |  | 46.5227 | 0.467 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 549.495 |  | 539.9391 | 1.7698 | 533.56 | 517.335 | 0.2329 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1566.89 |  | 1540.604 | 1.7062 | 1540.85 | 1490.29 | 0.1302 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.43 |  | 23.9722 | 1.9098 | 23.32 | 22.79 | 0.0409 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.31 |  | 41.8645 | 1.064 | 41.65 | 40.435 | 0.0236 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 326.965 |  | 326.171 | 0.2434 | 325.59 | 322.63 | 0.1621 | buy_precheck_manual_confirm | none |
| 15 | AMKR | semiconductor_test_packaging | 66.815 |  | 66.0149 | 1.212 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.31 |  | 24.8686 | 1.7749 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 79.995 |  | 78.3291 | 2.1268 | 76.615 | 74.55 | 0.05 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.67 |  | 30.2661 | 1.3345 | 29.735 | 28.785 | 0.0652 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.6 |  | 70.7628 | 1.1832 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.68 |  | 746.9494 | 0.2317 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1813.945 |  | 1810.1411 | 0.2101 | 1804.54 | 1786.51 | 0.0358 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 46.74 |  | 46.5227 | 0.467 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.965 |  | 326.171 | 0.2434 | 325.59 | 322.63 | 0.1621 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 585.19 |  | 580.6435 | 0.783 | 582.03 | 576.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.67 |  | 706.7483 | 0.4134 | 707.09 | 704.52 | 0.0169 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 567.74 |  | 564.3051 | 0.6087 | 564.91 | 552.71 | 0.1039 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 295.81 |  | 294.5385 | 0.4317 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | ETN | data_center_power_cooling | 406.09 |  | 406.0664 | 0.0058 | 411.01 | 404.21 | 0.101 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 248.46 |  | 247.7729 | 0.2773 | 248.915 | 247.32 | 0.0201 | watch_only | none |
| 11 | GOOGL | cloud_ai_capex | 349.25 |  | 349.178 | 0.0206 | 350.985 | 347.69 | 0.0172 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 399.33 |  | 399.1655 | 0.0412 | 401.45 | 396.36 | 0.0275 | watch_only | none |
| 13 | ORCL | cloud_ai_capex | 125.85 |  | 125.4846 | 0.2912 | 126.01 | 122.48 | 0.1033 | watch_only | none |
| 14 | TT | data_center_power_cooling | 470.53 |  | 469.7874 | 0.1581 | 475.98 | 467.01 | 0.187 | watch_only | none |
| 15 | APD | industrial_gases | 299.9 |  | 299.2533 | 0.2161 | 301.84 | 296.5 | 0.1901 | watch_only | none |
| 16 | NVDA | ai_accelerator | 206.89 |  | 206.0019 | 0.4311 | 208.61 | 206.275 | 0.0628 | watch_only | none |
| 17 | AVGO | custom_silicon_networking | 386.63 |  | 384.7838 | 0.4798 | 390.11 | 382.13 | 0.0466 | watch_only | none |
| 18 | SOXX | semiconductor_index | 554.2 |  | 548.7204 | 0.9986 | 550.77 | 545.11 | 0.0613 | buy_precheck_manual_confirm | none |
| 19 | KLAC | semiconductor_equipment | 218.16 |  | 216.7214 | 0.6638 | 220.76 | 214.41 | 0.2109 | watch_only | none |
| 20 | TSM | foundry | 423.72 |  | 419.815 | 0.9302 | 418.76 | 415.025 | 0.059 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 423.72 |  | 419.815 | 0.9302 | 418.76 | 415.025 | 0.059 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.19 |  | 580.6435 | 0.783 | 582.03 | 576.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.2 |  | 548.7204 | 0.9986 | 550.77 | 545.11 | 0.0613 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.67 |  | 706.7483 | 0.4134 | 707.09 | 704.52 | 0.0169 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.68 |  | 746.9494 | 0.2317 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1813.945 |  | 1810.1411 | 0.2101 | 1804.54 | 1786.51 | 0.0358 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 567.74 |  | 564.3051 | 0.6087 | 564.91 | 552.71 | 0.1039 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 295.81 |  | 294.5385 | 0.4317 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.74 |  | 46.5227 | 0.467 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 549.495 |  | 539.9391 | 1.7698 | 533.56 | 517.335 | 0.2329 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1566.89 |  | 1540.604 | 1.7062 | 1540.85 | 1490.29 | 0.1302 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.43 |  | 23.9722 | 1.9098 | 23.32 | 22.79 | 0.0409 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.31 |  | 41.8645 | 1.064 | 41.65 | 40.435 | 0.0236 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 326.965 |  | 326.171 | 0.2434 | 325.59 | 322.63 | 0.1621 | buy_precheck_manual_confirm | none |
| 15 | AMKR | semiconductor_test_packaging | 66.815 |  | 66.0149 | 1.212 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.31 |  | 24.8686 | 1.7749 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 79.995 |  | 78.3291 | 2.1268 | 76.615 | 74.55 | 0.05 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.67 |  | 30.2661 | 1.3345 | 29.735 | 28.785 | 0.0652 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.6 |  | 70.7628 | 1.1832 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 20 | AMD | ai_accelerator | 543.8 |  | 533.6938 | 1.8936 | 532.365 | 524.72 | 0.3512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.67 |  | 706.7483 | 0.4134 | 707.09 | 704.52 | 0.0169 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.6 |  | 70.7628 | 1.1832 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.89 |  | 206.0019 | 0.4311 | 208.61 | 206.275 | 0.0628 | watch_only | none |
| MSFT | cloud_ai_capex | 399.33 |  | 399.1655 | 0.0412 | 401.45 | 396.36 | 0.0275 | watch_only | none |
| AAPL | mega_cap_platform | 326.965 |  | 326.171 | 0.2434 | 325.59 | 322.63 | 0.1621 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.25 |  | 349.178 | 0.0206 | 350.985 | 347.69 | 0.0172 | watch_only | none |
| AMD | ai_accelerator | 543.8 |  | 533.6938 | 1.8936 | 532.365 | 524.72 | 0.3512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.72 |  | 419.815 | 0.9302 | 418.76 | 415.025 | 0.059 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.2 |  | 548.7204 | 0.9986 | 550.77 | 545.11 | 0.0613 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.19 |  | 580.6435 | 0.783 | 582.03 | 576.57 | 0.0256 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.63 |  | 384.7838 | 0.4798 | 390.11 | 382.13 | 0.0466 | watch_only | none |
| MU | memory_hbm_storage | 973.04 |  | 949.6354 | 2.4646 | 944.99 | 923 | 0.5087 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.15 |  | 207.6103 | 0.7416 | 208.61 | 205.31 | 3.3469 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.12 |  | 403.5371 | -0.1034 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.74 |  | 46.5227 | 0.467 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.31 |  | 24.8686 | 1.7749 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.68 |  | 746.9494 | 0.2317 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.81 |  | 294.5385 | 0.4317 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.85 |  | 125.4846 | 0.2912 | 126.01 | 122.48 | 0.1033 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 79.995 |  | 78.3291 | 2.1268 | 76.615 | 74.55 | 0.05 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 305.63 |  | 301.4665 | 1.3811 | 305.09 | 299.13 | 2.4409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.09 |  | 406.0664 | 0.0058 | 411.01 | 404.21 | 0.101 | watch_only | none |
| PWR | data_center_power_cooling | 641.79 |  | 638.3543 | 0.5382 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1087.32 |  | 1096.7584 | -0.8606 | 1140.63 | 1103.815 | 1.0733 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.53 |  | 469.7874 | 0.1581 | 475.98 | 467.01 | 0.187 | watch_only | none |
| JCI | data_center_power_cooling | 142.2 |  | 141.8003 | 0.2819 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.69 |  | 175.1816 | -0.2806 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 318.275 |  | 311.7476 | 2.0938 | 309.72 | 302.3 | 2.7209 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 836.18 |  | 823.6063 | 1.5267 | 823.31 | 800.37 | 1.63 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 408.66 |  | 405.4564 | 0.7901 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 119.08 |  | 115.9455 | 2.7034 | 109.39 | 107.58 | 1.6544 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 325.7 |  | 325.9502 | -0.0768 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1813.945 |  | 1810.1411 | 0.2101 | 1804.54 | 1786.51 | 0.0358 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 567.74 |  | 564.3051 | 0.6087 | 564.91 | 552.71 | 0.1039 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.915 |  | 320.4069 | 0.4707 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 218.16 |  | 216.7214 | 0.6638 | 220.76 | 214.41 | 0.2109 | watch_only | none |
| TER | semiconductor_test_packaging | 377.69 |  | 369.8349 | 2.1239 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.48 |  | 296.6786 | 1.6184 | 296.68 | 291.36 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 66.815 |  | 66.0149 | 1.212 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 56.2 |  | 54.9647 | 2.2475 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 142.49 |  | 141.4611 | 0.7273 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 345.94 |  | 339.8277 | 1.7986 | 340.205 | 336.3 | 4.2637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 507.28 |  | 506.3518 | 0.1833 | 512.83 | 507.675 | 4.3073 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 299.9 |  | 299.2533 | 0.2161 | 301.84 | 296.5 | 0.1901 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 30.67 |  | 30.2661 | 1.3345 | 29.735 | 28.785 | 0.0652 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.31 |  | 41.8645 | 1.064 | 41.65 | 40.435 | 0.0236 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.43 |  | 23.9722 | 1.9098 | 23.32 | 22.79 | 0.0409 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1566.89 |  | 1540.604 | 1.7062 | 1540.85 | 1490.29 | 0.1302 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 549.495 |  | 539.9391 | 1.7698 | 533.56 | 517.335 | 0.2329 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 891.865 |  | 876.7314 | 1.7261 | 866.73 | 845.78 | 2.0227 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.46 |  | 247.7729 | 0.2773 | 248.915 | 247.32 | 0.0201 | watch_only | none |
| META | cloud_ai_capex | 646.98 |  | 647.4161 | -0.0674 | 655.425 | 643.54 | 1.8053 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 293.29 |  | 286.3034 | 2.4403 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 168.8 |  | 165.8787 | 1.7611 | 165.88 | 160.77 | 1.013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
