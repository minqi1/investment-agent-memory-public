# Intraday State

- Generated at: `2026-07-22T00:06:22+08:00`
- Market time ET: `2026-07-21T12:06:23-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 19, 'watch_only': 4, 'below_vwap': 6, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 3, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.665 |  | 705.9343 | 0.3868 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 551.78 |  | 547.2447 | 0.8287 | 550.77 | 545.11 | 0.0544 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 582.26 |  | 579.1949 | 0.5292 | 582.03 | 576.57 | 0.0378 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.185 |  | 746.2163 | 0.2638 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 582.26 |  | 579.1949 | 0.5292 | 582.03 | 576.57 | 0.0378 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 551.78 |  | 547.2447 | 0.8287 | 550.77 | 545.11 | 0.0544 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.665 |  | 705.9343 | 0.3868 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.185 |  | 746.2163 | 0.2638 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1814.84 |  | 1805.2334 | 0.5322 | 1804.54 | 1786.51 | 0.0793 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.65 |  | 294.2216 | 0.4855 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | DELL | ai_server_oem | 406.62 |  | 402.5298 | 1.0161 | 405.78 | 397.185 | 0.2976 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.82 |  | 46.3983 | 0.909 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 9 | ARM | ai_accelerator | 291.78 |  | 284.9543 | 2.3954 | 286.39 | 275.86 | 0.2742 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 546.805 |  | 537.3886 | 1.7522 | 533.56 | 517.335 | 0.3456 | buy_precheck_manual_confirm | none |
| 11 | MKSI | semiconductor_materials | 343.16 |  | 338.7914 | 1.2895 | 340.205 | 336.3 | 0.1486 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.15 |  | 23.7858 | 1.531 | 23.32 | 22.79 | 0.0414 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 41.85 |  | 41.6817 | 0.4037 | 41.65 | 40.435 | 0.0239 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 328.7 |  | 325.3867 | 1.0183 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 15 | AAOI | ai_networking_optical | 116.13 |  | 113.9553 | 1.9084 | 109.39 | 107.58 | 0.1292 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.295 |  | 24.7682 | 2.1271 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 78.08 |  | 77.2187 | 1.1155 | 76.615 | 74.55 | 0.0768 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.515 |  | 30.1086 | 1.3497 | 29.735 | 28.785 | 0.0983 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.33 |  | 70.5581 | 1.094 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.185 |  | 746.2163 | 0.2638 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 582.26 |  | 579.1949 | 0.5292 | 582.03 | 576.57 | 0.0378 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.665 |  | 705.9343 | 0.3868 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 206.46 |  | 206.1334 | 0.1585 | 208.61 | 206.275 | 0.0145 | watch_only | none |
| 5 | ASML | semiconductor_equipment | 1814.84 |  | 1805.2334 | 0.5322 | 1804.54 | 1786.51 | 0.0793 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.65 |  | 294.2216 | 0.4855 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 247.76 |  | 247.7588 | 0.0005 | 248.915 | 247.32 | 0.0161 | watch_only | none |
| 8 | IREN | high_beta_ai_infrastructure | 41.85 |  | 41.6817 | 0.4037 | 41.65 | 40.435 | 0.0239 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 125.26 |  | 125.0585 | 0.1611 | 126.01 | 122.48 | 0.0639 | watch_only | none |
| 10 | SOXX | semiconductor_index | 551.78 |  | 547.2447 | 0.8287 | 550.77 | 545.11 | 0.0544 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 46.82 |  | 46.3983 | 0.909 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 12 | AVGO | custom_silicon_networking | 387.04 |  | 384.387 | 0.6902 | 390.11 | 382.13 | 0.2868 | watch_only | none |
| 13 | DELL | ai_server_oem | 406.62 |  | 402.5298 | 1.0161 | 405.78 | 397.185 | 0.2976 | buy_precheck_manual_confirm | none |
| 14 | MKSI | semiconductor_materials | 343.16 |  | 338.7914 | 1.2895 | 340.205 | 336.3 | 0.1486 | buy_precheck_manual_confirm | none |
| 15 | AAPL | mega_cap_platform | 328.7 |  | 325.3867 | 1.0183 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 16 | TT | data_center_power_cooling | 470.02 |  | 469.0258 | 0.212 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 638.925 |  | 636.7873 | 0.3357 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | CRWV | gpu_cloud_ai_factory | 78.08 |  | 77.2187 | 1.1155 | 76.615 | 74.55 | 0.0768 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.515 |  | 30.1086 | 1.3497 | 29.735 | 28.785 | 0.0983 | buy_precheck_manual_confirm | none |
| 20 | LRCX | semiconductor_equipment | 320.44 |  | 319.3214 | 0.3503 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 582.26 |  | 579.1949 | 0.5292 | 582.03 | 576.57 | 0.0378 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 551.78 |  | 547.2447 | 0.8287 | 550.77 | 545.11 | 0.0544 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.665 |  | 705.9343 | 0.3868 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.185 |  | 746.2163 | 0.2638 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1814.84 |  | 1805.2334 | 0.5322 | 1804.54 | 1786.51 | 0.0793 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.65 |  | 294.2216 | 0.4855 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | DELL | ai_server_oem | 406.62 |  | 402.5298 | 1.0161 | 405.78 | 397.185 | 0.2976 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.82 |  | 46.3983 | 0.909 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 9 | ARM | ai_accelerator | 291.78 |  | 284.9543 | 2.3954 | 286.39 | 275.86 | 0.2742 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 546.805 |  | 537.3886 | 1.7522 | 533.56 | 517.335 | 0.3456 | buy_precheck_manual_confirm | none |
| 11 | MKSI | semiconductor_materials | 343.16 |  | 338.7914 | 1.2895 | 340.205 | 336.3 | 0.1486 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.15 |  | 23.7858 | 1.531 | 23.32 | 22.79 | 0.0414 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 41.85 |  | 41.6817 | 0.4037 | 41.65 | 40.435 | 0.0239 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 328.7 |  | 325.3867 | 1.0183 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| 15 | AAOI | ai_networking_optical | 116.13 |  | 113.9553 | 1.9084 | 109.39 | 107.58 | 0.1292 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.295 |  | 24.7682 | 2.1271 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 78.08 |  | 77.2187 | 1.1155 | 76.615 | 74.55 | 0.0768 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.515 |  | 30.1086 | 1.3497 | 29.735 | 28.785 | 0.0983 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.33 |  | 70.5581 | 1.094 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 20 | TSM | foundry | 420.905 |  | 418.0079 | 0.6931 | 418.76 | 415.025 | 0.9575 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.665 |  | 705.9343 | 0.3868 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.33 |  | 70.5581 | 1.094 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.46 |  | 206.1334 | 0.1585 | 208.61 | 206.275 | 0.0145 | watch_only | none |
| MSFT | cloud_ai_capex | 398.3 |  | 399.4312 | -0.2832 | 401.45 | 396.36 | 0.0301 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.7 |  | 325.3867 | 1.0183 | 325.59 | 322.63 | 0.0152 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.08 |  | 349.1324 | -0.015 | 350.985 | 347.69 | 0.0143 | below_vwap | below_vwap |
| AMD | ai_accelerator | 533.63 |  | 530.9285 | 0.5088 | 532.365 | 524.72 | 0.3935 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 420.905 |  | 418.0079 | 0.6931 | 418.76 | 415.025 | 0.9575 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.78 |  | 547.2447 | 0.8287 | 550.77 | 545.11 | 0.0544 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 582.26 |  | 579.1949 | 0.5292 | 582.03 | 576.57 | 0.0378 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 387.04 |  | 384.387 | 0.6902 | 390.11 | 382.13 | 0.2868 | watch_only | none |
| MU | memory_hbm_storage | 965.22 |  | 939.6282 | 2.7236 | 944.99 | 923 | 0.3647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.61 |  | 206.9911 | 1.2652 | 208.61 | 205.31 | 1.1211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 406.62 |  | 402.5298 | 1.0161 | 405.78 | 397.185 | 0.2976 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 46.82 |  | 46.3983 | 0.909 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.295 |  | 24.7682 | 2.1271 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.185 |  | 746.2163 | 0.2638 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.65 |  | 294.2216 | 0.4855 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.26 |  | 125.0585 | 0.1611 | 126.01 | 122.48 | 0.0639 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 78.08 |  | 77.2187 | 1.1155 | 76.615 | 74.55 | 0.0768 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 304.775 |  | 300.6072 | 1.3865 | 305.09 | 299.13 | 2.0441 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.02 |  | 405.7766 | 0.5529 | 411.01 | 404.21 | 4.2351 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 638.925 |  | 636.7873 | 0.3357 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1088.145 |  | 1098.432 | -0.9365 | 1140.63 | 1103.815 | 0.2399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 470.02 |  | 469.0258 | 0.212 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.815 |  | 141.244 | 0.4043 | 142.15 | 140.105 | 5.1193 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| ANET | ai_networking_optical | 175.18 |  | 175.4241 | -0.1391 | 176.06 | 172.32 | 0.3482 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 314.585 |  | 308.7064 | 1.9043 | 309.72 | 302.3 | 2.0567 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 829.93 |  | 819.7631 | 1.2402 | 823.31 | 800.37 | 0.9676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 409.145 |  | 404.6726 | 1.1052 | 401.91 | 397.18 | 4.5461 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 116.13 |  | 113.9553 | 1.9084 | 109.39 | 107.58 | 0.1292 | buy_precheck_manual_confirm | none |
| ALAB | ai_networking_optical | 329.3 |  | 326.055 | 0.9952 | 329.97 | 323.92 | 5.0896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1814.84 |  | 1805.2334 | 0.5322 | 1804.54 | 1786.51 | 0.0793 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 564.02 |  | 563.0172 | 0.1781 | 564.91 | 552.71 | 1.8599 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.44 |  | 319.3214 | 0.3503 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.025 |  | 216.1523 | 0.4038 | 220.76 | 214.41 | 0.7695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373.7 |  | 368.4036 | 1.4377 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 297.42 |  | 294.8287 | 0.8789 | 296.68 | 291.36 | 5.0366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.48 |  | 65.6521 | 1.261 | 66.54 | 65 | 0.5415 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.46 |  | 54.7097 | 1.3713 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 141.93 |  | 140.6404 | 0.917 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 343.16 |  | 338.7914 | 1.2895 | 340.205 | 336.3 | 0.1486 | buy_precheck_manual_confirm | none |
| LIN | industrial_gases | 504.09 |  | 507.4287 | -0.658 | 512.83 | 507.675 | 3.6878 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 297.51 |  | 298.887 | -0.4607 | 301.84 | 296.5 | 4.2755 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.515 |  | 30.1086 | 1.3497 | 29.735 | 28.785 | 0.0983 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.85 |  | 41.6817 | 0.4037 | 41.65 | 40.435 | 0.0239 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.15 |  | 23.7858 | 1.531 | 23.32 | 22.79 | 0.0414 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1552.55 |  | 1530.5854 | 1.435 | 1540.85 | 1490.29 | 0.4631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 546.805 |  | 537.3886 | 1.7522 | 533.56 | 517.335 | 0.3456 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 894.055 |  | 872.3705 | 2.4857 | 866.73 | 845.78 | 0.6756 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.76 |  | 247.7588 | 0.0005 | 248.915 | 247.32 | 0.0161 | watch_only | none |
| META | cloud_ai_capex | 647.35 |  | 647.437 | -0.0134 | 655.425 | 643.54 | 1.1956 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 291.78 |  | 284.9543 | 2.3954 | 286.39 | 275.86 | 0.2742 | buy_precheck_manual_confirm | none |
| SKHY | memory_hbm_storage | 165.625 |  | 165.0434 | 0.3524 | 165.88 | 160.77 | 1.6906 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
