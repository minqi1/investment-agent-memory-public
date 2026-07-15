# Intraday State

- Generated at: `2026-07-16T02:00:56+08:00`
- Market time ET: `2026-07-15T14:00:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 8, 'price_stale_or_missing': 1, 'below_vwap': 1, 'spread_too_wide_or_missing': 1, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.16 |  | 716.2293 | 0.1299 | 724.31 | 721.08 | 0.0084 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 552.68 |  | 551.161 | 0.2756 | 575.7 | 565.33 | 0.0669 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 586.89 |  | 587.235 | -0.0587 | 606.85 | 597.81 | 0.0784 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.13 |  | 753.1631 | 0.1284 | 755.54 | 754.215 | 0.0212 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.13 |  | 395.1405 | 0.2504 | 391.33 | 387.05 | 0.0656 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.29 |  | 295.625 | 0.2249 | 296.08 | 294.86 | 0.0034 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 372.02 |  | 368.662 | 0.9109 | 364.41 | 357.885 | 0.1075 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.03 |  | 254.4539 | 0.2264 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 676.59 |  | 675.4697 | 0.1659 | 664.875 | 657.17 | 0.2616 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.59 |  | 325.5175 | 0.6367 | 321.14 | 317.4 | 0.0214 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.54 |  | 21.7512 | 3.6265 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.215 |  | 28.1899 | 3.6365 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.29 |  | 295.625 | 0.2249 | 296.08 | 294.86 | 0.0034 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.13 |  | 395.1405 | 0.2504 | 391.33 | 387.05 | 0.0656 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.03 |  | 254.4539 | 0.2264 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 676.59 |  | 675.4697 | 0.1659 | 664.875 | 657.17 | 0.2616 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.59 |  | 325.5175 | 0.6367 | 321.14 | 317.4 | 0.0214 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 132.715 |  | 131.6728 | 0.7915 | 132.925 | 129.92 | 0.0301 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1785.66 |  | 1771.2664 | 0.8126 | 1829.9 | 1759.045 | 0.1014 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 372.02 |  | 368.662 | 0.9109 | 364.41 | 357.885 | 0.1075 | buy_precheck_manual_confirm | none |
| 9 | IREN | high_beta_ai_infrastructure | 39.65 |  | 39.1221 | 1.3494 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.215 |  | 28.1899 | 3.6365 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 22.54 |  | 21.7512 | 3.6265 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 12 | NVDA | ai_accelerator | 209.63 |  | 209.1639 | 0.2228 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| 13 | AVGO | custom_silicon_networking | 393.975 |  | 391.7773 | 0.5609 | 397.94 | 392.62 | 1.0356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SOXX | semiconductor_index | 552.68 |  | 551.161 | 0.2756 | 575.7 | 565.33 | 0.0669 | below_opening_15m_low | below_opening_15m_low |
| 15 | SPY | market_regime | 754.13 |  | 753.1631 | 0.1284 | 755.54 | 754.215 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| 16 | TSM | foundry | 419.415 |  | 418.8781 | 0.1282 | 428.59 | 422.945 | 0.031 | below_opening_15m_low | below_opening_15m_low |
| 17 | KLAC | semiconductor_equipment | 222.96 |  | 222.6175 | 0.1539 | 236.49 | 225.11 | 0.0897 | below_opening_15m_low | below_opening_15m_low |
| 18 | QQQ | market_regime | 717.16 |  | 716.2293 | 0.1299 | 724.31 | 721.08 | 0.0084 | below_opening_15m_low | below_opening_15m_low |
| 19 | SKHY | memory_hbm_storage | 175.98 |  | 175.5943 | 0.2196 | 183.63 | 176.08 | 0.125 | below_opening_15m_low | below_opening_15m_low |
| 20 | JCI | data_center_power_cooling | 142 |  | 141.6938 | 0.2161 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.13 |  | 395.1405 | 0.2504 | 391.33 | 387.05 | 0.0656 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.29 |  | 295.625 | 0.2249 | 296.08 | 294.86 | 0.0034 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 372.02 |  | 368.662 | 0.9109 | 364.41 | 357.885 | 0.1075 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.03 |  | 254.4539 | 0.2264 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 676.59 |  | 675.4697 | 0.1659 | 664.875 | 657.17 | 0.2616 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.59 |  | 325.5175 | 0.6367 | 321.14 | 317.4 | 0.0214 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.54 |  | 21.7512 | 3.6265 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.215 |  | 28.1899 | 3.6365 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1785.66 |  | 1771.2664 | 0.8126 | 1829.9 | 1759.045 | 0.1014 | watch_only | none |
| 10 | ORCL | cloud_ai_capex | 132.715 |  | 131.6728 | 0.7915 | 132.925 | 129.92 | 0.0301 | watch_only | none |
| 11 | IREN | high_beta_ai_infrastructure | 39.65 |  | 39.1221 | 1.3494 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 393.975 |  | 391.7773 | 0.5609 | 397.94 | 392.62 | 1.0356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 209.63 |  | 209.1639 | 0.2228 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| 15 | CIEN | ai_networking_optical | 419.955 |  | 418.9155 | 0.2481 | 438.14 | 427.54 | 4.9958 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | SOXX | semiconductor_index | 552.68 |  | 551.161 | 0.2756 | 575.7 | 565.33 | 0.0669 | below_opening_15m_low | below_opening_15m_low |
| 17 | STX | memory_hbm_storage | 817.9 |  | 817.2679 | 0.0773 | 889.1 | 850.01 | 0.9402 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SPY | market_regime | 754.13 |  | 753.1631 | 0.1284 | 755.54 | 754.215 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMD | ai_accelerator | 530.415 |  | 527.1732 | 0.6149 | 558.62 | 548.745 | 0.1471 | below_opening_15m_low | below_opening_15m_low |
| 20 | TT | data_center_power_cooling | 478.925 |  | 478.7407 | 0.0385 | 485.9 | 482.93 | 0.4928 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.16 |  | 716.2293 | 0.1299 | 724.31 | 721.08 | 0.0084 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.23 |  | 74.1942 | 0.0483 | 76.46 | 75.39 | 0.0269 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 209.63 |  | 209.1639 | 0.2228 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.13 |  | 395.1405 | 0.2504 | 391.33 | 387.05 | 0.0656 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.59 |  | 325.5175 | 0.6367 | 321.14 | 317.4 | 0.0214 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.02 |  | 368.662 | 0.9109 | 364.41 | 357.885 | 0.1075 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 530.415 |  | 527.1732 | 0.6149 | 558.62 | 548.745 | 0.1471 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 419.415 |  | 418.8781 | 0.1282 | 428.59 | 422.945 | 0.031 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.68 |  | 551.161 | 0.2756 | 575.7 | 565.33 | 0.0669 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 586.89 |  | 587.235 | -0.0587 | 606.85 | 597.81 | 0.0784 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 393.975 |  | 391.7773 | 0.5609 | 397.94 | 392.62 | 1.0356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 907.85 |  | 910.1513 | -0.2528 | 977.7 | 953.67 | 0.4847 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 207.27 |  | 208.5017 | -0.5907 | 223.02 | 214.85 | 0.1013 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 403.57 |  | 407.2656 | -0.9074 | 457.935 | 442.67 | 2.9041 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.85 |  | 46.9151 | -0.1387 | 50.2 | 48.995 | 0.0427 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.08 |  | 26.8694 | 0.7838 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.13 |  | 753.1631 | 0.1284 | 755.54 | 754.215 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 296.29 |  | 295.625 | 0.2249 | 296.08 | 294.86 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 132.715 |  | 131.6728 | 0.7915 | 132.925 | 129.92 | 0.0301 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.9 |  | 77.3971 | 0.6498 | 80.585 | 78.73 | 0.0642 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 300.655 |  | 299.0375 | 0.5409 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.98 |  | 408.4289 | 0.6246 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.15 |  | 644.4795 | 1.035 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1049 |  | 1032.3543 | 1.6124 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.925 |  | 478.7407 | 0.0385 | 485.9 | 482.93 | 0.4928 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 142 |  | 141.6938 | 0.2161 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 170.82 |  | 171.8757 | -0.6142 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 294.4 |  | 293.9177 | 0.1641 | 315.74 | 303.34 | 2.3777 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 750.395 |  | 748.3083 | 0.2789 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 419.955 |  | 418.9155 | 0.2481 | 438.14 | 427.54 | 4.9958 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 111.43 |  | 112.3179 | -0.7906 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 349.86 |  | 344.6617 | 1.5082 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1785.66 |  | 1771.2664 | 0.8126 | 1829.9 | 1759.045 | 0.1014 | watch_only | none |
| AMAT | semiconductor_equipment | 576.58 |  | 577.7404 | -0.2009 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 330.65 |  | 331.4077 | -0.2286 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.96 |  | 222.6175 | 0.1539 | 236.49 | 225.11 | 0.0897 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 339.19 |  | 335.4675 | 1.1096 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 305.79 |  | 307.4874 | -0.552 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.53 |  | 66.8494 | 1.0181 | 70.42 | 68.43 | 3.628 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.63 |  | 54.3367 | 0.5399 | 57.92 | 55.2 | 0.6773 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 137.86 |  | 137.6799 | 0.1308 | 143.15 | 140.4 | 4.773 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 352.88 |  | 348.512 | 1.2533 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.92 |  | 516.1066 | -0.0362 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.73 |  | 295.0105 | -0.4341 | 297.8 | 295.655 | 0.0851 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 29.215 |  | 28.1899 | 3.6365 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 39.65 |  | 39.1221 | 1.3494 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.54 |  | 21.7512 | 3.6265 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1613 |  | 1570.2881 | 2.72 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 512.06 |  | 516.6479 | -0.888 | 568.16 | 542.4 | 2.2615 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 817.9 |  | 817.2679 | 0.0773 | 889.1 | 850.01 | 0.9402 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMZN | cloud_ai_capex | 255.03 |  | 254.4539 | 0.2264 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 676.59 |  | 675.4697 | 0.1659 | 664.875 | 657.17 | 0.2616 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 273.36 |  | 275.941 | -0.9353 | 286.73 | 280.14 | 3.585 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 175.98 |  | 175.5943 | 0.2196 | 183.63 | 176.08 | 0.125 | below_opening_15m_low | below_opening_15m_low |
