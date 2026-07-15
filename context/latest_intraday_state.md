# Intraday State

- Generated at: `2026-07-16T03:04:36+08:00`
- Market time ET: `2026-07-15T15:04:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'spread_too_wide_or_missing': 6, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 2, 'below_vwap': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.315 |  | 716.3552 | -0.0056 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 552.21 |  | 551.4241 | 0.1425 | 575.7 | 565.33 | 0.0905 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.5 |  | 587.303 | 0.0335 | 606.85 | 597.81 | 0.0323 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.53 |  | 753.3038 | 0.03 | 755.54 | 754.215 | 0.0013 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.56 |  | 254.4978 | 0.0244 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 328.08 |  | 325.7351 | 0.7199 | 321.14 | 317.4 | 0.0152 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.9398 | 2.9636 | 22.36 | 21.94 | 0.0885 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.56 |  | 254.4978 | 0.0244 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1785.755 |  | 1772.7398 | 0.7342 | 1829.9 | 1759.045 | 0.1221 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 328.08 |  | 325.7351 | 0.7199 | 321.14 | 317.4 | 0.0152 | buy_precheck_manual_confirm | none |
| 4 | APLD | high_beta_ai_infrastructure | 28.48 |  | 28.3157 | 0.5804 | 29.055 | 28.28 | 0.0702 | watch_only | none |
| 5 | SKHY | memory_hbm_storage | 176.505 |  | 175.9246 | 0.3299 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ORCL | cloud_ai_capex | 132.13 |  | 131.907 | 0.1691 | 132.925 | 129.92 | 5.0102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.9398 | 2.9636 | 22.36 | 21.94 | 0.0885 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 395.68 |  | 395.3743 | 0.0773 | 391.33 | 387.05 | 0.4018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | AVGO | custom_silicon_networking | 393.53 |  | 392.0881 | 0.3677 | 397.94 | 392.62 | 3.8752 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SOXX | semiconductor_index | 552.21 |  | 551.4241 | 0.1425 | 575.7 | 565.33 | 0.0905 | below_opening_15m_low | below_opening_15m_low |
| 11 | SPY | market_regime | 753.53 |  | 753.3038 | 0.03 | 755.54 | 754.215 | 0.0013 | below_opening_15m_low | below_opening_15m_low |
| 12 | SMH | semiconductor_index | 587.5 |  | 587.303 | 0.0335 | 606.85 | 597.81 | 0.0323 | below_opening_15m_low | below_opening_15m_low |
| 13 | META | cloud_ai_capex | 677.595 |  | 675.572 | 0.2995 | 664.875 | 657.17 | 2.0661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | JCI | data_center_power_cooling | 142.145 |  | 141.8047 | 0.24 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | MKSI | semiconductor_materials | 349.83 |  | 348.7949 | 0.2968 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | DELL | ai_server_oem | 407.79 |  | 406.9986 | 0.1945 | 457.935 | 442.67 | 0.2722 | below_opening_15m_low | below_opening_15m_low |
| 17 | LIN | industrial_gases | 516.49 |  | 516.1037 | 0.0748 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | VRT | data_center_power_cooling | 301.78 |  | 299.4 | 0.7949 | 309.345 | 304.67 | 0.0994 | below_opening_15m_low | below_opening_15m_low |
| 19 | GOOGL | cloud_ai_capex | 370.595 |  | 368.9617 | 0.4427 | 364.41 | 357.885 | 0.4317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SMCI | ai_server_oem | 27.045 |  | 26.8868 | 0.5883 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.56 |  | 254.4978 | 0.0244 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 328.08 |  | 325.7351 | 0.7199 | 321.14 | 317.4 | 0.0152 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.9398 | 2.9636 | 22.36 | 21.94 | 0.0885 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 395.68 |  | 395.3743 | 0.0773 | 391.33 | 387.05 | 0.4018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GOOGL | cloud_ai_capex | 370.595 |  | 368.9617 | 0.4427 | 364.41 | 357.885 | 0.4317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | META | cloud_ai_capex | 677.595 |  | 675.572 | 0.2995 | 664.875 | 657.17 | 2.0661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1785.755 |  | 1772.7398 | 0.7342 | 1829.9 | 1759.045 | 0.1221 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 28.48 |  | 28.3157 | 0.5804 | 29.055 | 28.28 | 0.0702 | watch_only | none |
| 9 | IWM | market_regime | 295.22 |  | 295.6408 | -0.1423 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | AVGO | custom_silicon_networking | 393.53 |  | 392.0881 | 0.3677 | 397.94 | 392.62 | 3.8752 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SKHY | memory_hbm_storage | 176.505 |  | 175.9246 | 0.3299 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ORCL | cloud_ai_capex | 132.13 |  | 131.907 | 0.1691 | 132.925 | 129.92 | 5.0102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 211.14 |  | 209.3037 | 0.8774 | 213.775 | 211.225 | 0.3884 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | CIEN | ai_networking_optical | 421.445 |  | 419.6892 | 0.4184 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | SOXX | semiconductor_index | 552.21 |  | 551.4241 | 0.1425 | 575.7 | 565.33 | 0.0905 | below_opening_15m_low | below_opening_15m_low |
| 17 | SPY | market_regime | 753.53 |  | 753.3038 | 0.03 | 755.54 | 754.215 | 0.0013 | below_opening_15m_low | below_opening_15m_low |
| 18 | VRT | data_center_power_cooling | 301.78 |  | 299.4 | 0.7949 | 309.345 | 304.67 | 0.0994 | below_opening_15m_low | below_opening_15m_low |
| 19 | SNDK | memory_hbm_storage | 1619.155 |  | 1580.9749 | 2.415 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 142.145 |  | 141.8047 | 0.24 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.315 |  | 716.3552 | -0.0056 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.95 |  | 74.1988 | -0.3353 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.14 |  | 209.3037 | 0.8774 | 213.775 | 211.225 | 0.3884 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MSFT | cloud_ai_capex | 395.68 |  | 395.3743 | 0.0773 | 391.33 | 387.05 | 0.4018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 328.08 |  | 325.7351 | 0.7199 | 321.14 | 317.4 | 0.0152 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.595 |  | 368.9617 | 0.4427 | 364.41 | 357.885 | 0.4317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 527.12 |  | 527.4423 | -0.0611 | 558.62 | 548.745 | 1.9863 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 418.76 |  | 418.986 | -0.0539 | 428.59 | 422.945 | 0.2603 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.21 |  | 551.4241 | 0.1425 | 575.7 | 565.33 | 0.0905 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.5 |  | 587.303 | 0.0335 | 606.85 | 597.81 | 0.0323 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 393.53 |  | 392.0881 | 0.3677 | 397.94 | 392.62 | 3.8752 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 904.37 |  | 909.9982 | -0.6185 | 977.7 | 953.67 | 0.0464 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.66 |  | 208.3044 | -0.7894 | 223.02 | 214.85 | 0.8371 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 407.79 |  | 406.9986 | 0.1945 | 457.935 | 442.67 | 0.2722 | below_opening_15m_low | below_opening_15m_low |
| HPE | ai_server_oem | 47.315 |  | 46.9295 | 0.8215 | 50.2 | 48.995 | 0.0423 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.045 |  | 26.8868 | 0.5883 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.53 |  | 753.3038 | 0.03 | 755.54 | 754.215 | 0.0013 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.22 |  | 295.6408 | -0.1423 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.13 |  | 131.907 | 0.1691 | 132.925 | 129.92 | 5.0102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.08 |  | 77.5023 | -0.5449 | 80.585 | 78.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 301.78 |  | 299.4 | 0.7949 | 309.345 | 304.67 | 0.0994 | below_opening_15m_low | below_opening_15m_low |
| ETN | data_center_power_cooling | 410.49 |  | 408.6208 | 0.4574 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.1 |  | 645.998 | 0.7898 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1051.04 |  | 1035.8983 | 1.4617 | 1073.34 | 1059.27 | 0.1998 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 478.05 |  | 478.6919 | -0.1341 | 485.9 | 482.93 | 0.0858 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.145 |  | 141.8047 | 0.24 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171 |  | 171.8193 | -0.4768 | 186.095 | 178.355 | 4.6784 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 293.945 |  | 294.0509 | -0.036 | 315.74 | 303.34 | 0.3674 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 748.58 |  | 749.2042 | -0.0833 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 421.445 |  | 419.6892 | 0.4184 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 109.525 |  | 112.129 | -2.3223 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 346.06 |  | 344.7826 | 0.3705 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1785.755 |  | 1772.7398 | 0.7342 | 1829.9 | 1759.045 | 0.1221 | watch_only | none |
| AMAT | semiconductor_equipment | 575.18 |  | 577.6236 | -0.423 | 610.62 | 586.86 | 0.1165 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 330.295 |  | 331.4101 | -0.3365 | 355.245 | 340.745 | 1.3019 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 222.8 |  | 222.6687 | 0.0589 | 236.49 | 225.11 | 3.1418 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 338.51 |  | 336.1717 | 0.6956 | 356.29 | 343.785 | 4.9216 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 303.72 |  | 307.238 | -1.145 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.88 |  | 66.9997 | -0.1787 | 70.42 | 68.43 | 2.3176 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 | 3.8137 | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_too_wide,stale_or_missing |
| ENTG | semiconductor_materials | 136.525 |  | 137.663 | -0.8267 | 143.15 | 140.4 | 3.4133 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 349.83 |  | 348.7949 | 0.2968 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.49 |  | 516.1037 | 0.0748 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 293.615 |  | 294.4433 | -0.2813 | 297.8 | 295.655 | 4.8226 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.48 |  | 28.3157 | 0.5804 | 29.055 | 28.28 | 0.0702 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.81 |  | 39.2705 | -1.1727 | 40.01 | 38.815 | 0.0515 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.59 |  | 21.9398 | 2.9636 | 22.36 | 21.94 | 0.0885 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1619.155 |  | 1580.9749 | 2.415 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 512.345 |  | 516.3978 | -0.7848 | 568.16 | 542.4 | 1.3604 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 815.36 |  | 817.6033 | -0.2744 | 889.1 | 850.01 | 2.4161 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 254.56 |  | 254.4978 | 0.0244 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 677.595 |  | 675.572 | 0.2995 | 664.875 | 657.17 | 2.0661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.6 |  | 275.6387 | -0.7396 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 176.505 |  | 175.9246 | 0.3299 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
