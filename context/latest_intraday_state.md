# Intraday State

- Generated at: `2026-07-16T02:56:40+08:00`
- Market time ET: `2026-07-15T14:56:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'below_vwap': 3, 'watch_only': 4, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.85 |  | 716.3741 | -0.0732 | 724.31 | 721.08 | 0.0112 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 551.27 |  | 551.4822 | -0.0385 | 575.7 | 565.33 | 0.049 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 586.04 |  | 587.3426 | -0.2218 | 606.85 | 597.81 | 0.0665 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.37 |  | 753.3035 | 0.0088 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.84 |  | 395.3683 | 0.1193 | 391.33 | 387.05 | 0.0202 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.515 |  | 368.9357 | 0.4281 | 364.41 | 357.885 | 0.0297 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.66 |  | 254.4977 | 0.0638 | 252.89 | 249.98 | 0.0079 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.26 |  | 325.7068 | 0.4769 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.92 | 3.1933 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.66 |  | 254.4977 | 0.0638 | 252.89 | 249.98 | 0.0079 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 395.84 |  | 395.3683 | 0.1193 | 391.33 | 387.05 | 0.0202 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1782.395 |  | 1772.6348 | 0.5506 | 1829.9 | 1759.045 | 0.1145 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 370.515 |  | 368.9357 | 0.4281 | 364.41 | 357.885 | 0.0297 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.26 |  | 325.7068 | 0.4769 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 39.53 |  | 39.2866 | 0.6196 | 40.01 | 38.815 | 0.0506 | watch_only | none |
| 7 | ORCL | cloud_ai_capex | 132.42 |  | 131.8952 | 0.3979 | 132.925 | 129.92 | 0.3096 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 28.72 |  | 28.3104 | 1.4469 | 29.055 | 28.28 | 0.1045 | watch_only | none |
| 9 | SKHY | memory_hbm_storage | 176.5 |  | 175.9273 | 0.3255 | 183.63 | 176.08 | 4.6459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.92 | 3.1933 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |
| 11 | SPY | market_regime | 753.37 |  | 753.3035 | 0.0088 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |
| 12 | JCI | data_center_power_cooling | 142.25 |  | 141.7975 | 0.3191 | 145.99 | 144.625 | 0.1476 | below_opening_15m_low | below_opening_15m_low |
| 13 | SMCI | ai_server_oem | 26.935 |  | 26.8867 | 0.1796 | 28.295 | 27.55 | 0.0743 | below_opening_15m_low | below_opening_15m_low |
| 14 | HPE | ai_server_oem | 47 |  | 46.9248 | 0.1602 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 15 | NVDA | ai_accelerator | 210.22 |  | 209.2818 | 0.4483 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 16 | MKSI | semiconductor_materials | 349.57 |  | 348.7883 | 0.2241 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | LITE | ai_networking_optical | 750.515 |  | 749.2239 | 0.1723 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | LIN | industrial_gases | 516.55 |  | 516.0962 | 0.0879 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | IWM | market_regime | 295.43 |  | 295.6443 | -0.0725 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 20 | AVGO | custom_silicon_networking | 392.33 |  | 392.0746 | 0.0652 | 397.94 | 392.62 | 3.887 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.84 |  | 395.3683 | 0.1193 | 391.33 | 387.05 | 0.0202 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.515 |  | 368.9357 | 0.4281 | 364.41 | 357.885 | 0.0297 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.66 |  | 254.4977 | 0.0638 | 252.89 | 249.98 | 0.0079 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.26 |  | 325.7068 | 0.4769 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.92 | 3.1933 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 675.09 |  | 675.5452 | -0.0674 | 664.875 | 657.17 | 0.6607 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1782.395 |  | 1772.6348 | 0.5506 | 1829.9 | 1759.045 | 0.1145 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.42 |  | 131.8952 | 0.3979 | 132.925 | 129.92 | 0.3096 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 39.53 |  | 39.2866 | 0.6196 | 40.01 | 38.815 | 0.0506 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 28.72 |  | 28.3104 | 1.4469 | 29.055 | 28.28 | 0.1045 | watch_only | none |
| 11 | IWM | market_regime | 295.43 |  | 295.6443 | -0.0725 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | SKHY | memory_hbm_storage | 176.5 |  | 175.9273 | 0.3255 | 183.63 | 176.08 | 4.6459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 210.22 |  | 209.2818 | 0.4483 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 15 | CIEN | ai_networking_optical | 423.4 |  | 419.6042 | 0.9046 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | AVGO | custom_silicon_networking | 392.33 |  | 392.0746 | 0.0652 | 397.94 | 392.62 | 3.887 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | SPY | market_regime | 753.37 |  | 753.3035 | 0.0088 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |
| 18 | VRT | data_center_power_cooling | 301.94 |  | 299.3504 | 0.8651 | 309.345 | 304.67 | 0.2716 | below_opening_15m_low | below_opening_15m_low |
| 19 | SNDK | memory_hbm_storage | 1608.2 |  | 1580.3946 | 1.7594 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 142.25 |  | 141.7975 | 0.3191 | 145.99 | 144.625 | 0.1476 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.85 |  | 716.3741 | -0.0732 | 724.31 | 721.08 | 0.0112 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.815 |  | 74.2034 | -0.5234 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.22 |  | 209.2818 | 0.4483 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.84 |  | 395.3683 | 0.1193 | 391.33 | 387.05 | 0.0202 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.26 |  | 325.7068 | 0.4769 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.515 |  | 368.9357 | 0.4281 | 364.41 | 357.885 | 0.0297 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 526.68 |  | 527.4672 | -0.1492 | 558.62 | 548.745 | 0.0759 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 418.34 |  | 419.0005 | -0.1576 | 428.59 | 422.945 | 1.6589 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.27 |  | 551.4822 | -0.0385 | 575.7 | 565.33 | 0.049 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 586.04 |  | 587.3426 | -0.2218 | 606.85 | 597.81 | 0.0665 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 392.33 |  | 392.0746 | 0.0652 | 397.94 | 392.62 | 3.887 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MU | memory_hbm_storage | 904.02 |  | 910.1239 | -0.6707 | 977.7 | 953.67 | 1.7555 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.77 |  | 208.3488 | -0.7578 | 223.02 | 214.85 | 0.1403 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 402.01 |  | 407.0657 | -1.242 | 457.935 | 442.67 | 1.5646 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47 |  | 46.9248 | 0.1602 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 26.935 |  | 26.8867 | 0.1796 | 28.295 | 27.55 | 0.0743 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.37 |  | 753.3035 | 0.0088 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.43 |  | 295.6443 | -0.0725 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.42 |  | 131.8952 | 0.3979 | 132.925 | 129.92 | 0.3096 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.47 |  | 77.5082 | -0.0493 | 80.585 | 78.73 | 0.1162 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 301.94 |  | 299.3504 | 0.8651 | 309.345 | 304.67 | 0.2716 | below_opening_15m_low | below_opening_15m_low |
| ETN | data_center_power_cooling | 411.005 |  | 408.6057 | 0.5872 | 417.84 | 413.82 | 5.1046 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| PWR | data_center_power_cooling | 652.81 |  | 645.9363 | 1.0641 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1055.07 |  | 1035.3592 | 1.9038 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 477.65 |  | 478.6952 | -0.2183 | 485.9 | 482.93 | 0.1403 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.25 |  | 141.7975 | 0.3191 | 145.99 | 144.625 | 0.1476 | below_opening_15m_low | below_opening_15m_low |
| ANET | ai_networking_optical | 170.93 |  | 171.8427 | -0.5312 | 186.095 | 178.355 | 2.4337 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.59 |  | 294.0652 | 0.1785 | 315.74 | 303.34 | 3.6118 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 750.515 |  | 749.2239 | 0.1723 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 423.4 |  | 419.6042 | 0.9046 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 109.89 |  | 112.1878 | -2.0482 | 123.995 | 117.25 | 3.8402 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 347.05 |  | 344.7652 | 0.6627 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1782.395 |  | 1772.6348 | 0.5506 | 1829.9 | 1759.045 | 0.1145 | watch_only | none |
| AMAT | semiconductor_equipment | 575.205 |  | 577.6757 | -0.4277 | 610.62 | 586.86 | 0.1026 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 329.83 |  | 331.4269 | -0.4818 | 355.245 | 340.745 | 0.2092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 222.41 |  | 222.6737 | -0.1184 | 236.49 | 225.11 | 0.0764 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 338.14 |  | 336.1456 | 0.5933 | 356.29 | 343.785 | 5.1162 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 303.75 |  | 307.3697 | -1.1776 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.455 |  | 67.0034 | 0.6739 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.02 |  | 137.6811 | -0.4802 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 349.57 |  | 348.7883 | 0.2241 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.55 |  | 516.0962 | 0.0879 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 293.865 |  | 294.4615 | -0.2026 | 297.8 | 295.655 | 1.3578 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.72 |  | 28.3104 | 1.4469 | 29.055 | 28.28 | 0.1045 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.53 |  | 39.2866 | 0.6196 | 40.01 | 38.815 | 0.0506 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.92 | 3.1933 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1608.2 |  | 1580.3946 | 1.7594 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 512.74 |  | 516.4455 | -0.7175 | 568.16 | 542.4 | 1.4588 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 816.99 |  | 817.6695 | -0.0831 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.66 |  | 254.4977 | 0.0638 | 252.89 | 249.98 | 0.0079 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.09 |  | 675.5452 | -0.0674 | 664.875 | 657.17 | 0.6607 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 273.35 |  | 275.6952 | -0.8507 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 176.5 |  | 175.9273 | 0.3255 | 183.63 | 176.08 | 4.6459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
