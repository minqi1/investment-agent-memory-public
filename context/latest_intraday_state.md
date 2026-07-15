# Intraday State

- Generated at: `2026-07-16T02:24:46+08:00`
- Market time ET: `2026-07-15T14:24:47-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 7, 'price_stale_or_missing': 1, 'below_vwap': 1, 'watch_only': 4, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.43 |  | 716.3276 | 0.2935 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 553.95 |  | 551.4181 | 0.4592 | 575.7 | 565.33 | 0.0939 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.18 |  | 587.2805 | 0.3234 | 606.85 | 597.81 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.76 |  | 753.2403 | 0.2018 | 755.54 | 754.215 | 0.0026 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.895 |  | 395.2935 | 0.4051 | 391.33 | 387.05 | 0.189 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 373.03 |  | 368.7962 | 1.148 | 364.41 | 357.885 | 0.0268 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.155 |  | 254.4789 | 0.2657 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.39 |  | 325.5968 | 0.5508 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.862 | 3.7874 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.165 |  | 39.1938 | 2.4781 | 40.01 | 38.815 | 0.0498 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.12 |  | 28.2555 | 3.0594 | 29.055 | 28.28 | 0.0687 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.155 |  | 254.4789 | 0.2657 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.76 |  | 753.2403 | 0.2018 | 755.54 | 754.215 | 0.0026 | watch_only | none |
| 3 | IWM | market_regime | 295.81 |  | 295.6453 | 0.0557 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 396.895 |  | 395.2935 | 0.4051 | 391.33 | 387.05 | 0.189 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.39 |  | 325.5968 | 0.5508 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 394.8 |  | 391.9519 | 0.7266 | 397.94 | 392.62 | 0.157 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1789.04 |  | 1772.11 | 0.9554 | 1829.9 | 1759.045 | 0.1476 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 373.03 |  | 368.7962 | 1.148 | 364.41 | 357.885 | 0.0268 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 29.12 |  | 28.2555 | 3.0594 | 29.055 | 28.28 | 0.0687 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 40.165 |  | 39.1938 | 2.4781 | 40.01 | 38.815 | 0.0498 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.862 | 3.7874 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 12 | SMH | semiconductor_index | 589.18 |  | 587.2805 | 0.3234 | 606.85 | 597.81 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| 13 | QQQ | market_regime | 718.43 |  | 716.3276 | 0.2935 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| 14 | META | cloud_ai_capex | 677.63 |  | 675.5248 | 0.3116 | 664.875 | 657.17 | 1.1201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | HPE | ai_server_oem | 47.01 |  | 46.9231 | 0.1851 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 16 | LRCX | semiconductor_equipment | 332.13 |  | 331.4348 | 0.2098 | 355.245 | 340.745 | 0.1596 | below_opening_15m_low | below_opening_15m_low |
| 17 | AMAT | semiconductor_equipment | 578.105 |  | 577.7354 | 0.064 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | NVDA | ai_accelerator | 210.61 |  | 209.2196 | 0.6645 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 19 | SOXX | semiconductor_index | 553.95 |  | 551.4181 | 0.4592 | 575.7 | 565.33 | 0.0939 | below_opening_15m_low | below_opening_15m_low |
| 20 | AMD | ai_accelerator | 531.1 |  | 527.3287 | 0.7152 | 558.62 | 548.745 | 0.1205 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.895 |  | 395.2935 | 0.4051 | 391.33 | 387.05 | 0.189 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 373.03 |  | 368.7962 | 1.148 | 364.41 | 357.885 | 0.0268 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.155 |  | 254.4789 | 0.2657 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.39 |  | 325.5968 | 0.5508 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.862 | 3.7874 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.165 |  | 39.1938 | 2.4781 | 40.01 | 38.815 | 0.0498 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.12 |  | 28.2555 | 3.0594 | 29.055 | 28.28 | 0.0687 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 394.8 |  | 391.9519 | 0.7266 | 397.94 | 392.62 | 0.157 | watch_only | none |
| 9 | META | cloud_ai_capex | 677.63 |  | 675.5248 | 0.3116 | 664.875 | 657.17 | 1.1201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ASML | semiconductor_equipment | 1789.04 |  | 1772.11 | 0.9554 | 1829.9 | 1759.045 | 0.1476 | watch_only | none |
| 11 | SPY | market_regime | 754.76 |  | 753.2403 | 0.2018 | 755.54 | 754.215 | 0.0026 | watch_only | none |
| 12 | ORCL | cloud_ai_capex | 133.855 |  | 131.7537 | 1.5948 | 132.925 | 129.92 | 4.1911 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | IWM | market_regime | 295.81 |  | 295.6453 | 0.0557 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 180.31 |  | 175.775 | 2.58 | 183.63 | 176.08 | 1.9411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.61 |  | 209.2196 | 0.6645 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 17 | MU | memory_hbm_storage | 914.24 |  | 910.1941 | 0.4445 | 977.7 | 953.67 | 1.0052 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 425.59 |  | 419.2775 | 1.5056 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SOXX | semiconductor_index | 553.95 |  | 551.4181 | 0.4592 | 575.7 | 565.33 | 0.0939 | below_opening_15m_low | below_opening_15m_low |
| 20 | ANET | ai_networking_optical | 171.99 |  | 171.8679 | 0.071 | 186.095 | 178.355 | 2.9595 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.43 |  | 716.3276 | 0.2935 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.665 |  | 74.2024 | 0.6234 | 76.46 | 75.39 | 0.0268 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.61 |  | 209.2196 | 0.6645 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.895 |  | 395.2935 | 0.4051 | 391.33 | 387.05 | 0.189 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.39 |  | 325.5968 | 0.5508 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 373.03 |  | 368.7962 | 1.148 | 364.41 | 357.885 | 0.0268 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 531.1 |  | 527.3287 | 0.7152 | 558.62 | 548.745 | 0.1205 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 421.02 |  | 418.9596 | 0.4918 | 428.59 | 422.945 | 0.0546 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.95 |  | 551.4181 | 0.4592 | 575.7 | 565.33 | 0.0939 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.18 |  | 587.2805 | 0.3234 | 606.85 | 597.81 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.8 |  | 391.9519 | 0.7266 | 397.94 | 392.62 | 0.157 | watch_only | none |
| MU | memory_hbm_storage | 914.24 |  | 910.1941 | 0.4445 | 977.7 | 953.67 | 1.0052 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 207.57 |  | 208.4428 | -0.4187 | 223.02 | 214.85 | 0.1349 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 405.48 |  | 407.1849 | -0.4187 | 457.935 | 442.67 | 4.7475 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.01 |  | 46.9231 | 0.1851 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.06 |  | 26.8785 | 0.6751 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.76 |  | 753.2403 | 0.2018 | 755.54 | 754.215 | 0.0026 | watch_only | none |
| IWM | market_regime | 295.81 |  | 295.6453 | 0.0557 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 133.855 |  | 131.7537 | 1.5948 | 132.925 | 129.92 | 4.1911 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.86 |  | 77.4663 | 0.5082 | 80.585 | 78.73 | 0.3082 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 302.22 |  | 299.2027 | 1.0084 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.85 |  | 408.5403 | 0.5653 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 649.68 |  | 644.9469 | 0.7339 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1056.8 |  | 1033.3492 | 2.2694 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.075 |  | 478.7429 | -0.1395 | 485.9 | 482.93 | 0.2405 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.48 |  | 141.7358 | 0.525 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.99 |  | 171.8679 | 0.071 | 186.095 | 178.355 | 2.9595 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 295.435 |  | 293.9988 | 0.4885 | 315.74 | 303.34 | 1.4589 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 757.63 |  | 748.9161 | 1.1635 | 820.15 | 780.365 | 2.4207 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 425.59 |  | 419.2775 | 1.5056 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 110.955 |  | 112.2913 | -1.1901 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 347.28 |  | 344.6937 | 0.7503 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1789.04 |  | 1772.11 | 0.9554 | 1829.9 | 1759.045 | 0.1476 | watch_only | none |
| AMAT | semiconductor_equipment | 578.105 |  | 577.7354 | 0.064 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LRCX | semiconductor_equipment | 332.13 |  | 331.4348 | 0.2098 | 355.245 | 340.745 | 0.1596 | below_opening_15m_low | below_opening_15m_low |
| KLAC | semiconductor_equipment | 223.75 |  | 222.6519 | 0.4932 | 236.49 | 225.11 | 2.8022 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 340.57 |  | 335.6434 | 1.4678 | 356.29 | 343.785 | 4.1783 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 306.685 |  | 307.4612 | -0.2525 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.84 |  | 66.9077 | 1.3934 | 70.42 | 68.43 | 3.6114 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3553 | 0.3398 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 137.68 |  | 137.684 | -0.0029 | 143.15 | 140.4 | 4.0238 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 351.21 |  | 348.6959 | 0.721 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.76 |  | 516.1003 | -0.0659 | 521.075 | 518.3 | 4.6068 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 292.79 |  | 294.5718 | -0.6049 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.12 |  | 28.2555 | 3.0594 | 29.055 | 28.28 | 0.0687 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 40.165 |  | 39.1938 | 2.4781 | 40.01 | 38.815 | 0.0498 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.862 | 3.7874 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1642.19 |  | 1575.0657 | 4.2617 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 515.8 |  | 516.5665 | -0.1484 | 568.16 | 542.4 | 0.2656 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 822.13 |  | 817.4193 | 0.5763 | 889.1 | 850.01 | 1.5192 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMZN | cloud_ai_capex | 255.155 |  | 254.4789 | 0.2657 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 677.63 |  | 675.5248 | 0.3116 | 664.875 | 657.17 | 1.1201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.9 |  | 275.8352 | -0.7016 | 286.73 | 280.14 | 3.3005 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 180.31 |  | 175.775 | 2.58 | 183.63 | 176.08 | 1.9411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
