# Intraday State

- Generated at: `2026-07-16T02:12:49+08:00`
- Market time ET: `2026-07-15T14:12:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 7, 'price_stale_or_missing': 3, 'below_vwap': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.16 |  | 716.2839 | 0.2619 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 555.14 |  | 551.3965 | 0.6789 | 575.7 | 565.33 | 0.0648 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.58 |  | 587.2564 | 0.3957 | 606.85 | 597.81 | 0.0746 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.71 |  | 753.1914 | 0.2016 | 755.54 | 754.215 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.15 |  | 395.1596 | 0.2506 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 371.9 |  | 368.7247 | 0.8612 | 364.41 | 357.885 | 0.2877 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.87 |  | 254.4597 | 0.1613 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.53 |  | 325.5546 | 0.6068 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.8003 | 3.6225 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.1 |  | 39.1562 | 2.4104 | 40.01 | 38.815 | 0.0748 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.085 |  | 28.2298 | 3.0294 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.87 |  | 254.4597 | 0.1613 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.15 |  | 395.1596 | 0.2506 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 754.71 |  | 753.1914 | 0.2016 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 4 | IWM | market_regime | 296.055 |  | 295.6377 | 0.1411 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 327.53 |  | 325.5546 | 0.6068 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1791.75 |  | 1771.6974 | 1.1318 | 1829.9 | 1759.045 | 0.0776 | watch_only | none |
| 7 | IREN | high_beta_ai_infrastructure | 40.1 |  | 39.1562 | 2.4104 | 40.01 | 38.815 | 0.0748 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.085 |  | 28.2298 | 3.0294 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 371.9 |  | 368.7247 | 0.8612 | 364.41 | 357.885 | 0.2877 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.8003 | 3.6225 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 11 | MU | memory_hbm_storage | 912.67 |  | 910.2436 | 0.2666 | 977.7 | 953.67 | 0.0625 | below_opening_15m_low | below_opening_15m_low |
| 12 | QQQ | market_regime | 718.16 |  | 716.2839 | 0.2619 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| 13 | META | cloud_ai_capex | 675.8 |  | 675.4726 | 0.0485 | 664.875 | 657.17 | 0.583 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | JCI | data_center_power_cooling | 142.07 |  | 141.7024 | 0.2594 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | NVDA | ai_accelerator | 210.385 |  | 209.1973 | 0.5677 | 213.775 | 211.225 | 0.019 | below_opening_15m_low | below_opening_15m_low |
| 16 | LRCX | semiconductor_equipment | 332.56 |  | 331.4367 | 0.3389 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | SOXX | semiconductor_index | 555.14 |  | 551.3965 | 0.6789 | 575.7 | 565.33 | 0.0648 | below_opening_15m_low | below_opening_15m_low |
| 18 | SMH | semiconductor_index | 589.58 |  | 587.2564 | 0.3957 | 606.85 | 597.81 | 0.0746 | below_opening_15m_low | below_opening_15m_low |
| 19 | HPE | ai_server_oem | 47.12 |  | 46.921 | 0.4241 | 50.2 | 48.995 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| 20 | AVGO | custom_silicon_networking | 395.575 |  | 391.8525 | 0.95 | 397.94 | 392.62 | 0.6472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.15 |  | 395.1596 | 0.2506 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 371.9 |  | 368.7247 | 0.8612 | 364.41 | 357.885 | 0.2877 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.87 |  | 254.4597 | 0.1613 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.53 |  | 325.5546 | 0.6068 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.8003 | 3.6225 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.1 |  | 39.1562 | 2.4104 | 40.01 | 38.815 | 0.0748 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.085 |  | 28.2298 | 3.0294 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |
| 8 | META | cloud_ai_capex | 675.8 |  | 675.4726 | 0.0485 | 664.875 | 657.17 | 0.583 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1791.75 |  | 1771.6974 | 1.1318 | 1829.9 | 1759.045 | 0.0776 | watch_only | none |
| 10 | SPY | market_regime | 754.71 |  | 753.1914 | 0.2016 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 11 | ORCL | cloud_ai_capex | 132.99 |  | 131.7133 | 0.9693 | 132.925 | 129.92 | 0.7895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | IWM | market_regime | 296.055 |  | 295.6377 | 0.1411 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 395.575 |  | 391.8525 | 0.95 | 397.94 | 392.62 | 0.6472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SKHY | memory_hbm_storage | 179.41 |  | 175.7061 | 2.108 | 183.63 | 176.08 | 0.4459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.385 |  | 209.1973 | 0.5677 | 213.775 | 211.225 | 0.019 | below_opening_15m_low | below_opening_15m_low |
| 17 | MU | memory_hbm_storage | 912.67 |  | 910.2436 | 0.2666 | 977.7 | 953.67 | 0.0625 | below_opening_15m_low | below_opening_15m_low |
| 18 | CIEN | ai_networking_optical | 425.07 |  | 419.1196 | 1.4197 | 438.14 | 427.54 | 4.0911 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | SOXX | semiconductor_index | 555.14 |  | 551.3965 | 0.6789 | 575.7 | 565.33 | 0.0648 | below_opening_15m_low | below_opening_15m_low |
| 20 | STX | memory_hbm_storage | 823.39 |  | 817.3513 | 0.7388 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.16 |  | 716.2839 | 0.2619 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.56 |  | 74.1964 | 0.49 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.385 |  | 209.1973 | 0.5677 | 213.775 | 211.225 | 0.019 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.15 |  | 395.1596 | 0.2506 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.53 |  | 325.5546 | 0.6068 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.9 |  | 368.7247 | 0.8612 | 364.41 | 357.885 | 0.2877 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 532.03 |  | 527.2475 | 0.9071 | 558.62 | 548.745 | 0.2688 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 421.325 |  | 418.9214 | 0.5738 | 428.59 | 422.945 | 0.8972 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 555.14 |  | 551.3965 | 0.6789 | 575.7 | 565.33 | 0.0648 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.58 |  | 587.2564 | 0.3957 | 606.85 | 597.81 | 0.0746 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 395.575 |  | 391.8525 | 0.95 | 397.94 | 392.62 | 0.6472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 912.67 |  | 910.2436 | 0.2666 | 977.7 | 953.67 | 0.0625 | below_opening_15m_low | below_opening_15m_low |
| MRVL | custom_silicon_networking | 208.07 |  | 208.4883 | -0.2006 | 223.02 | 214.85 | 0.1057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 405.8 |  | 407.2306 | -0.3513 | 457.935 | 442.67 | 2.967 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.12 |  | 46.921 | 0.4241 | 50.2 | 48.995 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.135 |  | 26.8744 | 0.9696 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.71 |  | 753.1914 | 0.2016 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| IWM | market_regime | 296.055 |  | 295.6377 | 0.1411 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 132.99 |  | 131.7133 | 0.9693 | 132.925 | 129.92 | 0.7895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.26 |  | 77.4526 | 1.0424 | 80.585 | 78.73 | 0.0894 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 302.58 |  | 299.1548 | 1.1449 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 412 |  | 408.4987 | 0.8571 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 652 |  | 644.8393 | 1.1105 | 663.475 | 653.94 | 0.3466 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1055.895 |  | 1033.0388 | 2.2125 | 1073.34 | 1059.27 | 0.3267 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 478.73 |  | 478.7436 | -0.0028 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.07 |  | 141.7024 | 0.2594 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.655 |  | 171.8735 | -0.1271 | 186.095 | 178.355 | 4.0779 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 296.28 |  | 293.9664 | 0.787 | 315.74 | 303.34 | 4.7759 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 757.09 |  | 748.6998 | 1.1206 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 425.07 |  | 419.1196 | 1.4197 | 438.14 | 427.54 | 4.0911 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 111.51 |  | 112.3076 | -0.7102 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 349.86 |  | 344.6617 | 1.5082 | 369.23 | 356.615 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ASML | semiconductor_equipment | 1791.75 |  | 1771.6974 | 1.1318 | 1829.9 | 1759.045 | 0.0776 | watch_only | none |
| AMAT | semiconductor_equipment | 579.12 |  | 577.7478 | 0.2375 | 610.62 | 586.86 | 5.0456 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LRCX | semiconductor_equipment | 332.56 |  | 331.4367 | 0.3389 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.79 |  | 222.6463 | 0.5137 | 236.49 | 225.11 | 2.842 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 341.23 |  | 335.5399 | 1.6958 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 306.94 |  | 307.4856 | -0.1774 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.845 |  | 66.8826 | 1.4389 | 70.42 | 68.43 | 3.6112 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.725 |  | 54.3463 | 0.6969 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 137.86 |  | 137.6799 | 0.1308 | 143.15 | 140.4 | 4.5191 | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_too_wide,stale_or_missing |
| MKSI | semiconductor_materials | 352.79 |  | 348.5999 | 1.202 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.665 |  | 516.0999 | -0.0843 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.095 |  | 294.8317 | -0.5891 | 297.8 | 295.655 | 4.7288 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.085 |  | 28.2298 | 3.0294 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 40.1 |  | 39.1562 | 2.4104 | 40.01 | 38.815 | 0.0748 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.8003 | 3.6225 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1628.91 |  | 1573.553 | 3.518 | 1726.34 | 1665.91 | 1.2241 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 515.815 |  | 516.599 | -0.1518 | 568.16 | 542.4 | 0.252 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 823.39 |  | 817.3513 | 0.7388 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.87 |  | 254.4597 | 0.1613 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.8 |  | 675.4726 | 0.0485 | 664.875 | 657.17 | 0.583 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 275.38 |  | 275.8887 | -0.1844 | 286.73 | 280.14 | 3.704 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 179.41 |  | 175.7061 | 2.108 | 183.63 | 176.08 | 0.4459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
