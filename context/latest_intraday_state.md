# Intraday State

- Generated at: `2026-07-16T03:28:26+08:00`
- Market time ET: `2026-07-15T15:28:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 6, 'price_stale_or_missing': 2, 'below_vwap': 2, 'watch_only': 3, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.06 |  | 716.3385 | -0.0389 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 552.19 |  | 551.467 | 0.1311 | 575.7 | 565.33 | 0.0978 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.15 |  | 587.265 | -0.0196 | 606.85 | 597.81 | 0.0664 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.61 |  | 753.3155 | 0.0391 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.65 |  | 395.3829 | 0.0676 | 391.33 | 387.05 | 0.0834 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.28 |  | 369.0317 | 0.3383 | 364.41 | 357.885 | 0.0756 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.58 |  | 254.4923 | 0.0344 | 252.89 | 249.98 | 0.0943 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 676.97 |  | 675.6595 | 0.194 | 664.875 | 657.17 | 0.1684 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.385 |  | 325.8516 | 0.4706 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.9656 | 2.6606 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.58 |  | 254.4923 | 0.0344 | 252.89 | 249.98 | 0.0943 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 395.65 |  | 395.3829 | 0.0676 | 391.33 | 387.05 | 0.0834 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 393.29 |  | 392.2025 | 0.2773 | 397.94 | 392.62 | 0.0585 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 370.28 |  | 369.0317 | 0.3383 | 364.41 | 357.885 | 0.0756 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 676.97 |  | 675.6595 | 0.194 | 664.875 | 657.17 | 0.1684 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.385 |  | 325.8516 | 0.4706 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1793.59 |  | 1773.4051 | 1.1382 | 1829.9 | 1759.045 | 0.1082 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.08 |  | 131.9349 | 0.11 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | APLD | high_beta_ai_infrastructure | 28.64 |  | 28.3384 | 1.0642 | 29.055 | 28.28 | 0.0698 | watch_only | none |
| 10 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.9656 | 2.6606 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 552.19 |  | 551.467 | 0.1311 | 575.7 | 565.33 | 0.0978 | below_opening_15m_low | below_opening_15m_low |
| 12 | SPY | market_regime | 753.61 |  | 753.3155 | 0.0391 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 13 | SMCI | ai_server_oem | 26.975 |  | 26.892 | 0.3085 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 14 | CIEN | ai_networking_optical | 421.04 |  | 419.7554 | 0.306 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | ANET | ai_networking_optical | 171.905 |  | 171.79 | 0.0669 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | STX | memory_hbm_storage | 818.37 |  | 817.5392 | 0.1016 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | NVDA | ai_accelerator | 210.84 |  | 209.4534 | 0.662 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 18 | JCI | data_center_power_cooling | 142.77 |  | 141.8396 | 0.656 | 145.99 | 144.625 | 0.1471 | below_opening_15m_low | below_opening_15m_low |
| 19 | IWM | market_regime | 295.6 |  | 295.6375 | -0.0127 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 20 | ALAB | ai_networking_optical | 347.27 |  | 344.8642 | 0.6976 | 369.23 | 356.615 | 0.3254 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.65 |  | 395.3829 | 0.0676 | 391.33 | 387.05 | 0.0834 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.28 |  | 369.0317 | 0.3383 | 364.41 | 357.885 | 0.0756 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.58 |  | 254.4923 | 0.0344 | 252.89 | 249.98 | 0.0943 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 676.97 |  | 675.6595 | 0.194 | 664.875 | 657.17 | 0.1684 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.385 |  | 325.8516 | 0.4706 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.9656 | 2.6606 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 393.29 |  | 392.2025 | 0.2773 | 397.94 | 392.62 | 0.0585 | watch_only | none |
| 8 | ASML | semiconductor_equipment | 1793.59 |  | 1773.4051 | 1.1382 | 1829.9 | 1759.045 | 0.1082 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.64 |  | 28.3384 | 1.0642 | 29.055 | 28.28 | 0.0698 | watch_only | none |
| 10 | IWM | market_regime | 295.6 |  | 295.6375 | -0.0127 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ORCL | cloud_ai_capex | 132.08 |  | 131.9349 | 0.11 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | NVDA | ai_accelerator | 210.84 |  | 209.4534 | 0.662 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 14 | CIEN | ai_networking_optical | 421.04 |  | 419.7554 | 0.306 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | SOXX | semiconductor_index | 552.19 |  | 551.467 | 0.1311 | 575.7 | 565.33 | 0.0978 | below_opening_15m_low | below_opening_15m_low |
| 16 | ANET | ai_networking_optical | 171.905 |  | 171.79 | 0.0669 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | STX | memory_hbm_storage | 818.37 |  | 817.5392 | 0.1016 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SPY | market_regime | 753.61 |  | 753.3155 | 0.0391 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 19 | TT | data_center_power_cooling | 478.735 |  | 478.6747 | 0.0126 | 485.9 | 482.93 | 0.4512 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | VRT | data_center_power_cooling | 303.47 |  | 299.5066 | 1.3233 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.06 |  | 716.3385 | -0.0389 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.87 |  | 74.1896 | -0.4307 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.84 |  | 209.4534 | 0.662 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.65 |  | 395.3829 | 0.0676 | 391.33 | 387.05 | 0.0834 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.385 |  | 325.8516 | 0.4706 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.28 |  | 369.0317 | 0.3383 | 364.41 | 357.885 | 0.0756 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 527.1 |  | 527.4203 | -0.0607 | 558.62 | 548.745 | 0.184 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 418.59 |  | 418.9744 | -0.0918 | 428.59 | 422.945 | 1.8132 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.19 |  | 551.467 | 0.1311 | 575.7 | 565.33 | 0.0978 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.15 |  | 587.265 | -0.0196 | 606.85 | 597.81 | 0.0664 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 393.29 |  | 392.2025 | 0.2773 | 397.94 | 392.62 | 0.0585 | watch_only | none |
| MU | memory_hbm_storage | 900.78 |  | 909.5632 | -0.9657 | 977.7 | 953.67 | 0.4174 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 205.76 |  | 208.1422 | -1.1445 | 223.02 | 214.85 | 0.4471 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 408.33 |  | 406.9597 | 0.3367 | 457.935 | 442.67 | 3.4433 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 47.6 |  | 46.9803 | 1.319 | 50.2 | 48.995 | 0.042 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 26.975 |  | 26.892 | 0.3085 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.61 |  | 753.3155 | 0.0391 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.6 |  | 295.6375 | -0.0127 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.08 |  | 131.9349 | 0.11 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 76.79 |  | 77.4858 | -0.898 | 80.585 | 78.73 | 0.0521 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 303.47 |  | 299.5066 | 1.3233 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 412.14 |  | 408.7248 | 0.8356 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 650.62 |  | 646.2007 | 0.6839 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1056.57 |  | 1036.9276 | 1.8943 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.735 |  | 478.6747 | 0.0126 | 485.9 | 482.93 | 0.4512 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 142.77 |  | 141.8396 | 0.656 | 145.99 | 144.625 | 0.1471 | below_opening_15m_low | below_opening_15m_low |
| ANET | ai_networking_optical | 171.905 |  | 171.79 | 0.0669 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHR | ai_networking_optical | 295.48 |  | 294.0774 | 0.477 | 315.74 | 303.34 | 0.7141 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 748.4 |  | 749.0548 | -0.0874 | 820.15 | 780.365 | 3.6585 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 421.04 |  | 419.7554 | 0.306 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 108.94 |  | 111.8172 | -2.5732 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 347.27 |  | 344.8642 | 0.6976 | 369.23 | 356.615 | 0.3254 | below_opening_15m_low | below_opening_15m_low |
| ASML | semiconductor_equipment | 1793.59 |  | 1773.4051 | 1.1382 | 1829.9 | 1759.045 | 0.1082 | watch_only | none |
| AMAT | semiconductor_equipment | 575.835 |  | 577.5251 | -0.2927 | 610.62 | 586.86 | 1.0993 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 330.7 |  | 331.3655 | -0.2008 | 355.245 | 340.745 | 1.2579 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 222.565 |  | 222.6064 | -0.0186 | 236.49 | 225.11 | 3.2889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 338.87 |  | 336.3185 | 0.7586 | 356.29 | 343.785 | 0.3364 | below_opening_15m_low | below_opening_15m_low |
| ONTO | semiconductor_test_packaging | 303.61 |  | 307.0918 | -1.1338 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.09 |  | 67.0274 | 0.0934 | 70.42 | 68.43 | 2.519 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.46 |  | 54.3628 | 0.1788 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.16 |  | 137.5724 | -0.2998 | 143.15 | 140.4 | 0.5978 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 351.42 |  | 348.8717 | 0.7304 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.44 |  | 516.1019 | 0.0655 | 521.075 | 518.3 | 4.8602 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 294.28 |  | 294.4123 | -0.045 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.64 |  | 28.3384 | 1.0642 | 29.055 | 28.28 | 0.0698 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.45 |  | 39.2382 | -2.0088 | 40.01 | 38.815 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.9656 | 2.6606 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1637.45 |  | 1583.4521 | 3.4101 | 1726.34 | 1665.91 | 2.1118 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 511.01 |  | 516.1688 | -0.9994 | 568.16 | 542.4 | 1.5205 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 818.37 |  | 817.5392 | 0.1016 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.58 |  | 254.4923 | 0.0344 | 252.89 | 249.98 | 0.0943 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 676.97 |  | 675.6595 | 0.194 | 664.875 | 657.17 | 0.1684 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 273.6 |  | 275.5129 | -0.6943 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 175.4 |  | 175.8602 | -0.2617 | 183.63 | 176.08 | 2.6226 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
