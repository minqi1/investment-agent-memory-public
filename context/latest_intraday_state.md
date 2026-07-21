# Intraday State

- Generated at: `2026-07-22T01:16:37+08:00`
- Market time ET: `2026-07-21T13:16:38-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 16, 'below_opening_15m_low': 3, 'below_vwap': 7, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.475 |  | 706.5902 | 0.4083 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 553.77 |  | 548.4922 | 0.9622 | 550.77 | 545.11 | 0.0343 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.8 |  | 580.3788 | 0.7618 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.44 |  | 746.7405 | 0.2276 | 746.6 | 744.3 | 0.0174 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 584.8 |  | 580.3788 | 0.7618 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 553.77 |  | 548.4922 | 0.9622 | 550.77 | 545.11 | 0.0343 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.475 |  | 706.5902 | 0.4083 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.44 |  | 746.7405 | 0.2276 | 746.6 | 744.3 | 0.0174 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1820.85 |  | 1809.1602 | 0.6461 | 1804.54 | 1786.51 | 0.0379 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.79 |  | 294.4801 | 0.4448 | 294.51 | 292.72 | 0.0101 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.69 |  | 46.5057 | 0.3962 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 8 | ARM | ai_accelerator | 292.67 |  | 285.8568 | 2.3834 | 286.39 | 275.86 | 0.1948 | buy_precheck_manual_confirm | none |
| 9 | SNDK | memory_hbm_storage | 1576.55 |  | 1538.9819 | 2.4411 | 1540.85 | 1490.29 | 0.1897 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.51 |  | 23.9139 | 2.4925 | 23.32 | 22.79 | 0.0408 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 42.32 |  | 41.8148 | 1.2082 | 41.65 | 40.435 | 0.0473 | buy_precheck_manual_confirm | none |
| 12 | AAPL | mega_cap_platform | 328.045 |  | 326.0597 | 0.6089 | 325.59 | 322.63 | 0.0793 | buy_precheck_manual_confirm | none |
| 13 | ORCL | cloud_ai_capex | 126.215 |  | 125.4201 | 0.6338 | 126.01 | 122.48 | 0.0713 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 25.31 |  | 24.8465 | 1.8654 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.665 |  | 30.2064 | 1.5182 | 29.735 | 28.785 | 0.2609 | buy_precheck_manual_confirm | none |
| 16 | TQQQ | leveraged_tool | 71.54 |  | 70.7428 | 1.1268 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.44 |  | 746.7405 | 0.2276 | 746.6 | 744.3 | 0.0174 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.475 |  | 706.5902 | 0.4083 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 46.69 |  | 46.5057 | 0.3962 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 584.8 |  | 580.3788 | 0.7618 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 126.215 |  | 125.4201 | 0.6338 | 126.01 | 122.48 | 0.0713 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.79 |  | 294.4801 | 0.4448 | 294.51 | 292.72 | 0.0101 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 328.045 |  | 326.0597 | 0.6089 | 325.59 | 322.63 | 0.0793 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1820.85 |  | 1809.1602 | 0.6461 | 1804.54 | 1786.51 | 0.0379 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.09 |  | 247.7451 | 0.1392 | 248.915 | 247.32 | 0.2378 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 217.86 |  | 216.599 | 0.5822 | 220.76 | 214.41 | 0.0459 | watch_only | none |
| 11 | SOXX | semiconductor_index | 553.77 |  | 548.4922 | 0.9622 | 550.77 | 545.11 | 0.0343 | buy_precheck_manual_confirm | none |
| 12 | DELL | ai_server_oem | 404.58 |  | 403.5434 | 0.2569 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | IREN | high_beta_ai_infrastructure | 42.32 |  | 41.8148 | 1.2082 | 41.65 | 40.435 | 0.0473 | buy_precheck_manual_confirm | none |
| 14 | JCI | data_center_power_cooling | 142.41 |  | 141.798 | 0.4316 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TT | data_center_power_cooling | 471.475 |  | 469.7027 | 0.3773 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 641.595 |  | 637.661 | 0.6169 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | APD | industrial_gases | 300.14 |  | 298.9599 | 0.3947 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 386.35 |  | 384.6684 | 0.4372 | 390.11 | 382.13 | 0.7014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ENTG | semiconductor_materials | 142.4 |  | 141.3196 | 0.7645 | 142.09 | 139.41 | 4.4452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CORZ | high_beta_ai_infrastructure | 24.51 |  | 23.9139 | 2.4925 | 23.32 | 22.79 | 0.0408 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 584.8 |  | 580.3788 | 0.7618 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 553.77 |  | 548.4922 | 0.9622 | 550.77 | 545.11 | 0.0343 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.475 |  | 706.5902 | 0.4083 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.44 |  | 746.7405 | 0.2276 | 746.6 | 744.3 | 0.0174 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1820.85 |  | 1809.1602 | 0.6461 | 1804.54 | 1786.51 | 0.0379 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.79 |  | 294.4801 | 0.4448 | 294.51 | 292.72 | 0.0101 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.69 |  | 46.5057 | 0.3962 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 8 | ARM | ai_accelerator | 292.67 |  | 285.8568 | 2.3834 | 286.39 | 275.86 | 0.1948 | buy_precheck_manual_confirm | none |
| 9 | SNDK | memory_hbm_storage | 1576.55 |  | 1538.9819 | 2.4411 | 1540.85 | 1490.29 | 0.1897 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.51 |  | 23.9139 | 2.4925 | 23.32 | 22.79 | 0.0408 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 42.32 |  | 41.8148 | 1.2082 | 41.65 | 40.435 | 0.0473 | buy_precheck_manual_confirm | none |
| 12 | AAPL | mega_cap_platform | 328.045 |  | 326.0597 | 0.6089 | 325.59 | 322.63 | 0.0793 | buy_precheck_manual_confirm | none |
| 13 | ORCL | cloud_ai_capex | 126.215 |  | 125.4201 | 0.6338 | 126.01 | 122.48 | 0.0713 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 25.31 |  | 24.8465 | 1.8654 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.665 |  | 30.2064 | 1.5182 | 29.735 | 28.785 | 0.2609 | buy_precheck_manual_confirm | none |
| 16 | TQQQ | leveraged_tool | 71.54 |  | 70.7428 | 1.1268 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 17 | TSM | foundry | 423.77 |  | 419.3746 | 1.0481 | 418.76 | 415.025 | 0.4224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 541.19 |  | 532.8515 | 1.5649 | 532.365 | 524.72 | 0.9738 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MU | memory_hbm_storage | 975.615 |  | 948.207 | 2.8905 | 944.99 | 923 | 0.3915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | LITE | ai_networking_optical | 835.85 |  | 823.014 | 1.5596 | 823.31 | 800.37 | 0.9595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.475 |  | 706.5902 | 0.4083 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.54 |  | 70.7428 | 1.1268 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.24 |  | 205.9742 | 0.129 | 208.61 | 206.275 | 0.1649 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 398.37 |  | 399.17 | -0.2004 | 401.45 | 396.36 | 0.0301 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.045 |  | 326.0597 | 0.6089 | 325.59 | 322.63 | 0.0793 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.09 |  | 349.1782 | -0.0252 | 350.985 | 347.69 | 0.0802 | below_vwap | below_vwap |
| AMD | ai_accelerator | 541.19 |  | 532.8515 | 1.5649 | 532.365 | 524.72 | 0.9738 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.77 |  | 419.3746 | 1.0481 | 418.76 | 415.025 | 0.4224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.77 |  | 548.4922 | 0.9622 | 550.77 | 545.11 | 0.0343 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.8 |  | 580.3788 | 0.7618 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.35 |  | 384.6684 | 0.4372 | 390.11 | 382.13 | 0.7014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 975.615 |  | 948.207 | 2.8905 | 944.99 | 923 | 0.3915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.24 |  | 207.5528 | 0.8129 | 208.61 | 205.31 | 1.5293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 404.58 |  | 403.5434 | 0.2569 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.69 |  | 46.5057 | 0.3962 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.31 |  | 24.8465 | 1.8654 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.44 |  | 746.7405 | 0.2276 | 746.6 | 744.3 | 0.0174 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.79 |  | 294.4801 | 0.4448 | 294.51 | 292.72 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.215 |  | 125.4201 | 0.6338 | 126.01 | 122.48 | 0.0713 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 79.71 |  | 78.1233 | 2.031 | 76.615 | 74.55 | 2.7349 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 305.18 |  | 301.3374 | 1.2752 | 305.09 | 299.13 | 1.8972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.88 |  | 406.09 | -0.0517 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 641.595 |  | 637.661 | 0.6169 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1091.47 |  | 1097.4035 | -0.5407 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 471.475 |  | 469.7027 | 0.3773 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.41 |  | 141.798 | 0.4316 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.885 |  | 175.2265 | -0.1949 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 318.07 |  | 311.3815 | 2.148 | 309.72 | 302.3 | 0.7828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 835.85 |  | 823.014 | 1.5596 | 823.31 | 800.37 | 0.9595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 410.47 |  | 405.3673 | 1.2588 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 118.81 |  | 115.6516 | 2.7309 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 325.41 |  | 325.9788 | -0.1745 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1820.85 |  | 1809.1602 | 0.6461 | 1804.54 | 1786.51 | 0.0379 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 570.96 |  | 564.0166 | 1.2311 | 564.91 | 552.71 | 0.4992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 323.43 |  | 320.2941 | 0.9791 | 328.135 | 317.17 | 4.5821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 217.86 |  | 216.599 | 0.5822 | 220.76 | 214.41 | 0.0459 | watch_only | none |
| TER | semiconductor_test_packaging | 376.935 |  | 369.4953 | 2.0135 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.96 |  | 296.5314 | 1.8307 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.97 |  | 65.9281 | 1.5803 | 66.54 | 65 | 1.4484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.2 |  | 54.9647 | 2.2475 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 142.4 |  | 141.3196 | 0.7645 | 142.09 | 139.41 | 4.4452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 346.37 |  | 339.6961 | 1.9647 | 340.205 | 336.3 | 4.2585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 507.635 |  | 506.3259 | 0.2586 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 300.14 |  | 298.9599 | 0.3947 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.665 |  | 30.2064 | 1.5182 | 29.735 | 28.785 | 0.2609 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.32 |  | 41.8148 | 1.2082 | 41.65 | 40.435 | 0.0473 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.51 |  | 23.9139 | 2.4925 | 23.32 | 22.79 | 0.0408 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1576.55 |  | 1538.9819 | 2.4411 | 1540.85 | 1490.29 | 0.1897 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 550.325 |  | 539.3139 | 2.0417 | 533.56 | 517.335 | 4.8953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 895.33 |  | 876.2144 | 2.1816 | 866.73 | 845.78 | 0.5841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.09 |  | 247.7451 | 0.1392 | 248.915 | 247.32 | 0.2378 | watch_only | none |
| META | cloud_ai_capex | 646.24 |  | 647.5404 | -0.2008 | 655.425 | 643.54 | 0.4797 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 292.67 |  | 285.8568 | 2.3834 | 286.39 | 275.86 | 0.1948 | buy_precheck_manual_confirm | none |
| SKHY | memory_hbm_storage | 168.48 |  | 165.568 | 1.7588 | 165.88 | 160.77 | 1.1218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
