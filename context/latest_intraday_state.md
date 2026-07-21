# Intraday State

- Generated at: `2026-07-21T22:27:30+08:00`
- Market time ET: `2026-07-21T10:27:31-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 9, 'below_opening_15m_low': 3, 'spread_too_wide_or_missing': 19, 'manual_confirm_candidate': 5, 'below_vwap': 19, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.5 |  | 704.5962 | 0.1283 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| SOXX | semiconductor_index | 545.345 |  | 546.0084 | -0.1215 | 550.77 | 545.11 | 0.0642 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.58 |  | 576.8942 | -0.0545 | 582.03 | 576.57 | 0.0382 | below_vwap | below_vwap |
| SPY | market_regime | 746.45 |  | 745.3027 | 0.1539 | 746.6 | 744.3 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 565.74 |  | 560.4143 | 0.9503 | 564.91 | 552.71 | 0.2316 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.75 |  | 293.8598 | 0.3029 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 23.5 |  | 23.3314 | 0.7226 | 23.32 | 22.79 | 0.0851 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.785 |  | 324.2375 | 0.7857 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.77 |  | 29.7453 | 0.0831 | 29.735 | 28.785 | 0.1008 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.75 |  | 293.8598 | 0.3029 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | APLD | high_beta_ai_infrastructure | 29.77 |  | 29.7453 | 0.0831 | 29.735 | 28.785 | 0.1008 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 417.08 |  | 416.3848 | 0.167 | 418.76 | 415.025 | 0.0551 | watch_only | none |
| 4 | QQQ | market_regime | 705.5 |  | 704.5962 | 0.1283 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| 5 | SPY | market_regime | 746.45 |  | 745.3027 | 0.1539 | 746.6 | 744.3 | 0.0027 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 247.77 |  | 247.6599 | 0.0445 | 248.915 | 247.32 | 0.0363 | watch_only | none |
| 7 | HPE | ai_server_oem | 46.25 |  | 46.2208 | 0.0633 | 46.685 | 45.835 | 0.1081 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 23.5 |  | 23.3314 | 0.7226 | 23.32 | 22.79 | 0.0851 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 326.785 |  | 324.2375 | 0.7857 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 41.52 |  | 41.4485 | 0.1725 | 41.65 | 40.435 | 0.0723 | watch_only | none |
| 11 | SMCI | ai_server_oem | 24.635 |  | 24.572 | 0.2563 | 24.77 | 24.34 | 0.0406 | watch_only | none |
| 12 | LITE | ai_networking_optical | 818.695 |  | 812.2556 | 0.7928 | 823.31 | 800.37 | 0.2553 | watch_only | none |
| 13 | AMAT | semiconductor_equipment | 565.74 |  | 560.4143 | 0.9503 | 564.91 | 552.71 | 0.2316 | buy_precheck_manual_confirm | none |
| 14 | JCI | data_center_power_cooling | 140.345 |  | 140.2952 | 0.0355 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ANET | ai_networking_optical | 175.79 |  | 174.8922 | 0.5134 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMD | ai_accelerator | 529.82 |  | 529.2869 | 0.1007 | 532.365 | 524.72 | 0.9097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | COHU | semiconductor_test_packaging | 54.53 |  | 54.3069 | 0.4108 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | META | cloud_ai_capex | 647.305 |  | 647.2882 | 0.0026 | 655.425 | 643.54 | 1.8229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ALAB | ai_networking_optical | 325.5 |  | 324.3109 | 0.3666 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 293 |  | 292.9511 | 0.0167 | 296.68 | 291.36 | 1.1877 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 565.74 |  | 560.4143 | 0.9503 | 564.91 | 552.71 | 0.2316 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.75 |  | 293.8598 | 0.3029 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 23.5 |  | 23.3314 | 0.7226 | 23.32 | 22.79 | 0.0851 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.785 |  | 324.2375 | 0.7857 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.77 |  | 29.7453 | 0.0831 | 29.735 | 28.785 | 0.1008 | buy_precheck_manual_confirm | none |
| 6 | CIEN | ai_networking_optical | 404.69 |  | 400.6416 | 1.0105 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ARM | ai_accelerator | 287.34 |  | 282.7648 | 1.618 | 286.39 | 275.86 | 0.8875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | WDC | memory_hbm_storage | 534.96 |  | 533.03 | 0.3621 | 533.56 | 517.335 | 0.357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TER | semiconductor_test_packaging | 367.01 |  | 363.4062 | 0.9917 | 365.97 | 356.39 | 5.1143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | TSM | foundry | 417.08 |  | 416.3848 | 0.167 | 418.76 | 415.025 | 0.0551 | watch_only | none |
| 11 | COHU | semiconductor_test_packaging | 54.53 |  | 54.3069 | 0.4108 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | QQQ | market_regime | 705.5 |  | 704.5962 | 0.1283 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| 13 | SPY | market_regime | 746.45 |  | 745.3027 | 0.1539 | 746.6 | 744.3 | 0.0027 | watch_only | none |
| 14 | LITE | ai_networking_optical | 818.695 |  | 812.2556 | 0.7928 | 823.31 | 800.37 | 0.2553 | watch_only | none |
| 15 | AAOI | ai_networking_optical | 111.425 |  | 110.1099 | 1.1944 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMZN | cloud_ai_capex | 247.77 |  | 247.6599 | 0.0445 | 248.915 | 247.32 | 0.0363 | watch_only | none |
| 17 | HPE | ai_server_oem | 46.25 |  | 46.2208 | 0.0633 | 46.685 | 45.835 | 0.1081 | watch_only | none |
| 18 | IREN | high_beta_ai_infrastructure | 41.52 |  | 41.4485 | 0.1725 | 41.65 | 40.435 | 0.0723 | watch_only | none |
| 19 | SMCI | ai_server_oem | 24.635 |  | 24.572 | 0.2563 | 24.77 | 24.34 | 0.0406 | watch_only | none |
| 20 | TQQQ | leveraged_tool | 70.46 |  | 70.2317 | 0.3251 | 70.84 | 70.09 | 0.0284 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.5 |  | 704.5962 | 0.1283 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| TQQQ | leveraged_tool | 70.46 |  | 70.2317 | 0.3251 | 70.84 | 70.09 | 0.0284 | watch_only | none |
| NVDA | ai_accelerator | 205.15 |  | 206.2979 | -0.5564 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.295 |  | 399.5009 | 0.1988 | 401.45 | 396.36 | 0.3597 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 326.785 |  | 324.2375 | 0.7857 | 325.59 | 322.63 | 0.0153 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.43 |  | 349.502 | -0.0206 | 350.985 | 347.69 | 0.0429 | below_vwap | below_vwap |
| AMD | ai_accelerator | 529.82 |  | 529.2869 | 0.1007 | 532.365 | 524.72 | 0.9097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 417.08 |  | 416.3848 | 0.167 | 418.76 | 415.025 | 0.0551 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.345 |  | 546.0084 | -0.1215 | 550.77 | 545.11 | 0.0642 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.58 |  | 576.8942 | -0.0545 | 582.03 | 576.57 | 0.0382 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 383.26 |  | 383.794 | -0.1391 | 390.11 | 382.13 | 0.6836 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 925.7 |  | 930.9701 | -0.5661 | 944.99 | 923 | 0.2344 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 205.31 |  | 206.0872 | -0.3771 | 208.61 | 205.31 | 2.0457 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.33 |  | 402.3592 | -0.5043 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.25 |  | 46.2208 | 0.0633 | 46.685 | 45.835 | 0.1081 | watch_only | none |
| SMCI | ai_server_oem | 24.635 |  | 24.572 | 0.2563 | 24.77 | 24.34 | 0.0406 | watch_only | none |
| SPY | market_regime | 746.45 |  | 745.3027 | 0.1539 | 746.6 | 744.3 | 0.0027 | watch_only | none |
| IWM | market_regime | 294.75 |  | 293.8598 | 0.3029 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.15 |  | 124.9857 | 0.1315 | 126.01 | 122.48 | 1.0947 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 75.945 |  | 76.3206 | -0.4922 | 76.615 | 74.55 | 2.4755 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 299.08 |  | 299.5061 | -0.1423 | 305.09 | 299.13 | 1.4411 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 405.5 |  | 405.5099 | -0.0025 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 636 |  | 636.7959 | -0.125 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1089.04 |  | 1103.3721 | -1.2989 | 1140.63 | 1103.815 | 5.0264 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 467.05 |  | 469.5231 | -0.5267 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.345 |  | 140.2952 | 0.0355 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.79 |  | 174.8922 | 0.5134 | 176.06 | 172.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 308.2 |  | 305.1849 | 0.988 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 818.695 |  | 812.2556 | 0.7928 | 823.31 | 800.37 | 0.2553 | watch_only | none |
| CIEN | ai_networking_optical | 404.69 |  | 400.6416 | 1.0105 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 111.425 |  | 110.1099 | 1.1944 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 325.5 |  | 324.3109 | 0.3666 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1795.415 |  | 1796.3762 | -0.0535 | 1804.54 | 1786.51 | 0.093 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.74 |  | 560.4143 | 0.9503 | 564.91 | 552.71 | 0.2316 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 317.535 |  | 318.2082 | -0.2116 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.775 |  | 215.8584 | -0.0387 | 220.76 | 214.41 | 0.19 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 367.01 |  | 363.4062 | 0.9917 | 365.97 | 356.39 | 5.1143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293 |  | 292.9511 | 0.0167 | 296.68 | 291.36 | 1.1877 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 65.42 |  | 65.2386 | 0.278 | 66.54 | 65 | 3.9437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 54.53 |  | 54.3069 | 0.4108 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.41 |  | 140.1212 | -0.5076 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 337.57 |  | 337.6085 | -0.0114 | 340.205 | 336.3 | 4.719 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 509.49 |  | 509.3973 | 0.0182 | 512.83 | 507.675 | 1.0874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 300.165 |  | 299.0877 | 0.3602 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.77 |  | 29.7453 | 0.0831 | 29.735 | 28.785 | 0.1008 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.52 |  | 41.4485 | 0.1725 | 41.65 | 40.435 | 0.0723 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 23.5 |  | 23.3314 | 0.7226 | 23.32 | 22.79 | 0.0851 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1507.07 |  | 1517.4312 | -0.6828 | 1540.85 | 1490.29 | 1.5925 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 534.96 |  | 533.03 | 0.3621 | 533.56 | 517.335 | 0.357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 859.32 |  | 863.7468 | -0.5125 | 866.73 | 845.78 | 1.4232 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 247.77 |  | 247.6599 | 0.0445 | 248.915 | 247.32 | 0.0363 | watch_only | none |
| META | cloud_ai_capex | 647.305 |  | 647.2882 | 0.0026 | 655.425 | 643.54 | 1.8229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 287.34 |  | 282.7648 | 1.618 | 286.39 | 275.86 | 0.8875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 164.33 |  | 163.7267 | 0.3685 | 165.88 | 160.77 | 1.7708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
