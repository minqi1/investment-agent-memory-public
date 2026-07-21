# Intraday State

- Generated at: `2026-07-22T01:48:11+08:00`
- Market time ET: `2026-07-21T13:48:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 20, 'watch_only': 4, 'below_vwap': 7, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 22, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.6 |  | 706.7828 | 0.3986 | 707.09 | 704.52 | 0.0113 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 554.23 |  | 548.7798 | 0.9931 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.3 |  | 580.6934 | 0.7933 | 582.03 | 576.57 | 0.0188 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.68 |  | 746.978 | 0.2278 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.405 |  | 419.9267 | 1.0665 | 418.76 | 415.025 | 0.2757 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.3 |  | 580.6934 | 0.7933 | 582.03 | 576.57 | 0.0188 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.23 |  | 548.7798 | 0.9931 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.6 |  | 706.7828 | 0.3986 | 707.09 | 704.52 | 0.0113 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 543.61 |  | 533.8874 | 1.8211 | 532.365 | 524.72 | 0.3072 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 748.68 |  | 746.978 | 0.2278 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1812.755 |  | 1810.2209 | 0.14 | 1804.54 | 1786.51 | 0.0182 | buy_precheck_manual_confirm | none |
| 8 | CIEN | ai_networking_optical | 410.87 |  | 405.5032 | 1.3235 | 401.91 | 397.18 | 0.1996 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 568.465 |  | 564.399 | 0.7204 | 564.91 | 552.71 | 0.3026 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 306.23 |  | 301.5565 | 1.5498 | 305.09 | 299.13 | 0.16 | buy_precheck_manual_confirm | none |
| 11 | IWM | market_regime | 296.1 |  | 294.5489 | 0.5266 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 12 | JCI | data_center_power_cooling | 142.34 |  | 141.8095 | 0.3741 | 142.15 | 140.105 | 0.0422 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 46.7 |  | 46.5274 | 0.371 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.9848 | 1.4185 | 23.32 | 22.79 | 0.0822 | buy_precheck_manual_confirm | none |
| 15 | IREN | high_beta_ai_infrastructure | 42 |  | 41.8726 | 0.3044 | 41.65 | 40.435 | 0.0714 | buy_precheck_manual_confirm | none |
| 16 | AAPL | mega_cap_platform | 326.93 |  | 326.188 | 0.2275 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| 17 | ORCL | cloud_ai_capex | 126.4 |  | 125.5018 | 0.7157 | 126.01 | 122.48 | 0.1028 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 25.28 |  | 24.8771 | 1.6196 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.61 |  | 30.2706 | 1.1211 | 29.735 | 28.785 | 0.098 | buy_precheck_manual_confirm | none |
| 20 | TQQQ | leveraged_tool | 71.58 |  | 70.7657 | 1.1507 | 70.84 | 70.09 | 0.0279 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.68 |  | 746.978 | 0.2278 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1812.755 |  | 1810.2209 | 0.14 | 1804.54 | 1786.51 | 0.0182 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.93 |  | 326.188 | 0.2275 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 142.34 |  | 141.8095 | 0.3741 | 142.15 | 140.105 | 0.0422 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.7 |  | 46.5274 | 0.371 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 42 |  | 41.8726 | 0.3044 | 41.65 | 40.435 | 0.0714 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 585.3 |  | 580.6934 | 0.7933 | 582.03 | 576.57 | 0.0188 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 709.6 |  | 706.7828 | 0.3986 | 707.09 | 704.52 | 0.0113 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 126.4 |  | 125.5018 | 0.7157 | 126.01 | 122.48 | 0.1028 | buy_precheck_manual_confirm | none |
| 10 | IWM | market_regime | 296.1 |  | 294.5489 | 0.5266 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.52 |  | 247.7856 | 0.2964 | 248.915 | 247.32 | 0.0523 | watch_only | none |
| 12 | AMAT | semiconductor_equipment | 568.465 |  | 564.399 | 0.7204 | 564.91 | 552.71 | 0.3026 | buy_precheck_manual_confirm | none |
| 13 | NVDA | ai_accelerator | 206.83 |  | 206.016 | 0.3951 | 208.61 | 206.275 | 0.0774 | watch_only | none |
| 14 | AVGO | custom_silicon_networking | 386.575 |  | 384.8038 | 0.4603 | 390.11 | 382.13 | 0.0491 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 218.18 |  | 216.7615 | 0.6544 | 220.76 | 214.41 | 0.1192 | watch_only | none |
| 16 | SOXX | semiconductor_index | 554.23 |  | 548.7798 | 0.9931 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| 17 | TSM | foundry | 424.405 |  | 419.9267 | 1.0665 | 418.76 | 415.025 | 0.2757 | buy_precheck_manual_confirm | none |
| 18 | APD | industrial_gases | 299.9 |  | 299.2533 | 0.2161 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.9848 | 1.4185 | 23.32 | 22.79 | 0.0822 | buy_precheck_manual_confirm | none |
| 20 | CIEN | ai_networking_optical | 410.87 |  | 405.5032 | 1.3235 | 401.91 | 397.18 | 0.1996 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.405 |  | 419.9267 | 1.0665 | 418.76 | 415.025 | 0.2757 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.3 |  | 580.6934 | 0.7933 | 582.03 | 576.57 | 0.0188 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.23 |  | 548.7798 | 0.9931 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.6 |  | 706.7828 | 0.3986 | 707.09 | 704.52 | 0.0113 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 543.61 |  | 533.8874 | 1.8211 | 532.365 | 524.72 | 0.3072 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 748.68 |  | 746.978 | 0.2278 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1812.755 |  | 1810.2209 | 0.14 | 1804.54 | 1786.51 | 0.0182 | buy_precheck_manual_confirm | none |
| 8 | CIEN | ai_networking_optical | 410.87 |  | 405.5032 | 1.3235 | 401.91 | 397.18 | 0.1996 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 568.465 |  | 564.399 | 0.7204 | 564.91 | 552.71 | 0.3026 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 306.23 |  | 301.5565 | 1.5498 | 305.09 | 299.13 | 0.16 | buy_precheck_manual_confirm | none |
| 11 | IWM | market_regime | 296.1 |  | 294.5489 | 0.5266 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 12 | JCI | data_center_power_cooling | 142.34 |  | 141.8095 | 0.3741 | 142.15 | 140.105 | 0.0422 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 46.7 |  | 46.5274 | 0.371 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.9848 | 1.4185 | 23.32 | 22.79 | 0.0822 | buy_precheck_manual_confirm | none |
| 15 | IREN | high_beta_ai_infrastructure | 42 |  | 41.8726 | 0.3044 | 41.65 | 40.435 | 0.0714 | buy_precheck_manual_confirm | none |
| 16 | AAPL | mega_cap_platform | 326.93 |  | 326.188 | 0.2275 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| 17 | ORCL | cloud_ai_capex | 126.4 |  | 125.5018 | 0.7157 | 126.01 | 122.48 | 0.1028 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 25.28 |  | 24.8771 | 1.6196 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.61 |  | 30.2706 | 1.1211 | 29.735 | 28.785 | 0.098 | buy_precheck_manual_confirm | none |
| 20 | TQQQ | leveraged_tool | 71.58 |  | 70.7657 | 1.1507 | 70.84 | 70.09 | 0.0279 | buy_precheck_manual_confirm | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.6 |  | 706.7828 | 0.3986 | 707.09 | 704.52 | 0.0113 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.58 |  | 70.7657 | 1.1507 | 70.84 | 70.09 | 0.0279 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.83 |  | 206.016 | 0.3951 | 208.61 | 206.275 | 0.0774 | watch_only | none |
| MSFT | cloud_ai_capex | 398.65 |  | 399.1639 | -0.1287 | 401.45 | 396.36 | 0.1706 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 326.93 |  | 326.188 | 0.2275 | 325.59 | 322.63 | 0.0184 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349 |  | 349.1776 | -0.0509 | 350.985 | 347.69 | 0.0229 | below_vwap | below_vwap |
| AMD | ai_accelerator | 543.61 |  | 533.8874 | 1.8211 | 532.365 | 524.72 | 0.3072 | buy_precheck_manual_confirm | none |
| TSM | foundry | 424.405 |  | 419.9267 | 1.0665 | 418.76 | 415.025 | 0.2757 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.23 |  | 548.7798 | 0.9931 | 550.77 | 545.11 | 0.0361 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.3 |  | 580.6934 | 0.7933 | 582.03 | 576.57 | 0.0188 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.575 |  | 384.8038 | 0.4603 | 390.11 | 382.13 | 0.0491 | watch_only | none |
| MU | memory_hbm_storage | 974.485 |  | 950.0974 | 2.5668 | 944.99 | 923 | 0.6332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.16 |  | 207.6288 | 0.7375 | 208.61 | 205.31 | 1.2909 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403 |  | 403.5327 | -0.132 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.7 |  | 46.5274 | 0.371 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.28 |  | 24.8771 | 1.6196 | 24.77 | 24.34 | 0.0396 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.68 |  | 746.978 | 0.2278 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.1 |  | 294.5489 | 0.5266 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.4 |  | 125.5018 | 0.7157 | 126.01 | 122.48 | 0.1028 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 79.76 |  | 78.4152 | 1.7149 | 76.615 | 74.55 | 0.7272 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 306.23 |  | 301.5565 | 1.5498 | 305.09 | 299.13 | 0.16 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.35 |  | 406.0617 | 0.071 | 411.01 | 404.21 | 4.6807 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 642.45 |  | 638.4534 | 0.626 | 645.815 | 635.91 | 2.671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1086.15 |  | 1096.6008 | -0.953 | 1140.63 | 1103.815 | 0.6574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.86 |  | 469.7946 | 0.2268 | 475.98 | 467.01 | 4.9972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 142.34 |  | 141.8095 | 0.3741 | 142.15 | 140.105 | 0.0422 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 174.71 |  | 175.1719 | -0.2637 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 319.075 |  | 311.8584 | 2.3141 | 309.72 | 302.3 | 1.0499 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 839.235 |  | 823.8798 | 1.8638 | 823.31 | 800.37 | 1.0533 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 410.87 |  | 405.5032 | 1.3235 | 401.91 | 397.18 | 0.1996 | buy_precheck_manual_confirm | none |
| AAOI | ai_networking_optical | 119.88 |  | 116.0439 | 3.3057 | 109.39 | 107.58 | 1.0928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 325.08 |  | 325.9308 | -0.261 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1812.755 |  | 1810.2209 | 0.14 | 1804.54 | 1786.51 | 0.0182 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 568.465 |  | 564.399 | 0.7204 | 564.91 | 552.71 | 0.3026 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.93 |  | 320.4312 | 0.4677 | 328.135 | 317.17 | 5.057 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 218.18 |  | 216.7615 | 0.6544 | 220.76 | 214.41 | 0.1192 | watch_only | none |
| TER | semiconductor_test_packaging | 378.44 |  | 369.9596 | 2.2922 | 365.97 | 356.39 | 4.1063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 301.82 |  | 296.9653 | 1.6348 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.845 |  | 66.0555 | 1.1952 | 66.54 | 65 | 3.9943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.25 |  | 55.0076 | 2.2586 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 142.48 |  | 141.5299 | 0.6713 | 142.09 | 139.41 | 4.3024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 345.7 |  | 339.838 | 1.7249 | 340.205 | 336.3 | 4.1886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 507.57 |  | 506.3607 | 0.2388 | 512.83 | 507.675 | 4.3521 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 299.9 |  | 299.2533 | 0.2161 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.61 |  | 30.2706 | 1.1211 | 29.735 | 28.785 | 0.098 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42 |  | 41.8726 | 0.3044 | 41.65 | 40.435 | 0.0714 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.325 |  | 23.9848 | 1.4185 | 23.32 | 22.79 | 0.0822 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1566.36 |  | 1540.9129 | 1.6514 | 1540.85 | 1490.29 | 1.8712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 549.51 |  | 540.0344 | 1.7546 | 533.56 | 517.335 | 0.6569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 895.125 |  | 876.95 | 2.0725 | 866.73 | 845.78 | 0.9652 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.52 |  | 247.7856 | 0.2964 | 248.915 | 247.32 | 0.0523 | watch_only | none |
| META | cloud_ai_capex | 647.01 |  | 647.4203 | -0.0634 | 655.425 | 643.54 | 1.8207 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 292.77 |  | 286.3653 | 2.2365 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 169.985 |  | 166.1748 | 2.2929 | 165.88 | 160.77 | 1.5237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
