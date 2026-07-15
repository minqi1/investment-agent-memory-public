# Intraday State

- Generated at: `2026-07-16T02:48:44+08:00`
- Market time ET: `2026-07-15T14:48:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'below_vwap': 3, 'spread_too_wide_or_missing': 3, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.4 |  | 716.3882 | 0.0016 | 724.31 | 721.08 | 0.0112 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 552.24 |  | 551.4824 | 0.1374 | 575.7 | 565.33 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.17 |  | 587.347 | -0.0301 | 606.85 | 597.81 | 0.0647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.78 |  | 753.2993 | 0.0638 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.18 |  | 395.3584 | 0.2078 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 371.16 |  | 368.9101 | 0.6099 | 364.41 | 357.885 | 0.1105 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.5 |  | 254.4971 | 0.0011 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.395 |  | 325.6818 | 0.526 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.9096 | 3.562 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.5 |  | 254.4971 | 0.0011 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.18 |  | 395.3584 | 0.2078 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1781.15 |  | 1772.5313 | 0.4862 | 1829.9 | 1759.045 | 0.0281 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 371.16 |  | 368.9101 | 0.6099 | 364.41 | 357.885 | 0.1105 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.395 |  | 325.6818 | 0.526 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 39.65 |  | 39.2793 | 0.9437 | 40.01 | 38.815 | 0.0252 | watch_only | none |
| 7 | AVGO | custom_silicon_networking | 393.38 |  | 392.0612 | 0.3364 | 397.94 | 392.62 | 0.5364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SKHY | memory_hbm_storage | 177.18 |  | 175.9213 | 0.7155 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.9096 | 3.562 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 552.24 |  | 551.4824 | 0.1374 | 575.7 | 565.33 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| 11 | SPY | market_regime | 753.78 |  | 753.2993 | 0.0638 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |
| 12 | QQQ | market_regime | 716.4 |  | 716.3882 | 0.0016 | 724.31 | 721.08 | 0.0112 | below_opening_15m_low | below_opening_15m_low |
| 13 | APLD | high_beta_ai_infrastructure | 28.87 |  | 28.302 | 2.0069 | 29.055 | 28.28 | 0.1039 | watch_only | none |
| 14 | ORCL | cloud_ai_capex | 132.905 |  | 131.8586 | 0.7936 | 132.925 | 129.92 | 4.7402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 142.25 |  | 141.7814 | 0.3305 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | NVDA | ai_accelerator | 210.48 |  | 209.2691 | 0.5786 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| 17 | MKSI | semiconductor_materials | 349.75 |  | 348.7825 | 0.2774 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SMCI | ai_server_oem | 26.98 |  | 26.8856 | 0.3513 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 19 | IWM | market_regime | 295.45 |  | 295.6478 | -0.0669 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 20 | CIEN | ai_networking_optical | 422.53 |  | 419.5286 | 0.7154 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.18 |  | 395.3584 | 0.2078 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 371.16 |  | 368.9101 | 0.6099 | 364.41 | 357.885 | 0.1105 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.5 |  | 254.4971 | 0.0011 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.395 |  | 325.6818 | 0.526 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.9096 | 3.562 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 674.66 |  | 675.5537 | -0.1323 | 664.875 | 657.17 | 0.0548 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1781.15 |  | 1772.5313 | 0.4862 | 1829.9 | 1759.045 | 0.0281 | watch_only | none |
| 8 | IREN | high_beta_ai_infrastructure | 39.65 |  | 39.2793 | 0.9437 | 40.01 | 38.815 | 0.0252 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.87 |  | 28.302 | 2.0069 | 29.055 | 28.28 | 0.1039 | watch_only | none |
| 10 | IWM | market_regime | 295.45 |  | 295.6478 | -0.0669 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 393.38 |  | 392.0612 | 0.3364 | 397.94 | 392.62 | 0.5364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SKHY | memory_hbm_storage | 177.18 |  | 175.9213 | 0.7155 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ORCL | cloud_ai_capex | 132.905 |  | 131.8586 | 0.7936 | 132.925 | 129.92 | 4.7402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | NVDA | ai_accelerator | 210.48 |  | 209.2691 | 0.5786 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| 16 | CIEN | ai_networking_optical | 422.53 |  | 419.5286 | 0.7154 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | SOXX | semiconductor_index | 552.24 |  | 551.4824 | 0.1374 | 575.7 | 565.33 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| 18 | SPY | market_regime | 753.78 |  | 753.2993 | 0.0638 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMD | ai_accelerator | 528.92 |  | 527.4731 | 0.2743 | 558.62 | 548.745 | 0.4878 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | VRT | data_center_power_cooling | 301.755 |  | 299.3261 | 0.8114 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.4 |  | 716.3882 | 0.0016 | 724.31 | 721.08 | 0.0112 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 73.99 |  | 74.2088 | -0.2948 | 76.46 | 75.39 | 0.027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.48 |  | 209.2691 | 0.5786 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.18 |  | 395.3584 | 0.2078 | 391.33 | 387.05 | 0.0353 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.395 |  | 325.6818 | 0.526 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.16 |  | 368.9101 | 0.6099 | 364.41 | 357.885 | 0.1105 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 528.92 |  | 527.4731 | 0.2743 | 558.62 | 548.745 | 0.4878 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 418.96 |  | 419.0089 | -0.0117 | 428.59 | 422.945 | 1.2722 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.24 |  | 551.4824 | 0.1374 | 575.7 | 565.33 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.17 |  | 587.347 | -0.0301 | 606.85 | 597.81 | 0.0647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 393.38 |  | 392.0612 | 0.3364 | 397.94 | 392.62 | 0.5364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 907.905 |  | 910.2565 | -0.2583 | 977.7 | 953.67 | 0.1245 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.84 |  | 208.3655 | -0.7321 | 223.02 | 214.85 | 1.1506 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.81 |  | 407.1387 | -0.8176 | 457.935 | 442.67 | 0.3417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 46.88 |  | 46.9249 | -0.0956 | 50.2 | 48.995 | 0.0427 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.98 |  | 26.8856 | 0.3513 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.78 |  | 753.2993 | 0.0638 | 755.54 | 754.215 | 0.0199 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.45 |  | 295.6478 | -0.0669 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.905 |  | 131.8586 | 0.7936 | 132.925 | 129.92 | 4.7402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.965 |  | 77.5069 | 0.5911 | 80.585 | 78.73 | 4.2968 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 301.755 |  | 299.3261 | 0.8114 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.77 |  | 408.601 | 0.5308 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.37 |  | 645.8574 | 0.8535 | 663.475 | 653.94 | 4.9772 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 1053.345 |  | 1034.7773 | 1.7944 | 1073.34 | 1059.27 | 0.1443 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 477.795 |  | 478.7176 | -0.1927 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.25 |  | 141.7814 | 0.3305 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 170.76 |  | 171.854 | -0.6366 | 186.095 | 178.355 | 2.3835 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.27 |  | 294.0575 | 0.0723 | 315.74 | 303.34 | 3.6021 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 749.8 |  | 749.1987 | 0.0803 | 820.15 | 780.365 | 3.4503 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 422.53 |  | 419.5286 | 0.7154 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 110.05 |  | 112.2147 | -1.929 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 347.5 |  | 344.7628 | 0.7939 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1781.15 |  | 1772.5313 | 0.4862 | 1829.9 | 1759.045 | 0.0281 | watch_only | none |
| AMAT | semiconductor_equipment | 575.67 |  | 577.6976 | -0.351 | 610.62 | 586.86 | 0.0799 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 330.24 |  | 331.4422 | -0.3627 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.665 |  | 222.6754 | -0.0046 | 236.49 | 225.11 | 0.0584 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 338.74 |  | 336.1347 | 0.7751 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 304.305 |  | 307.3908 | -1.0039 | 326.25 | 317.3 | 4.5086 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.485 |  | 66.9917 | 0.7364 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.47 |  | 137.6885 | -0.1587 | 143.15 | 140.4 | 0.291 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 349.75 |  | 348.7825 | 0.2774 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.4 |  | 516.0933 | 0.0594 | 521.075 | 518.3 | 4.816 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 293.565 |  | 294.4708 | -0.3076 | 297.8 | 295.655 | 0.5076 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.87 |  | 28.302 | 2.0069 | 29.055 | 28.28 | 0.1039 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.65 |  | 39.2793 | 0.9437 | 40.01 | 38.815 | 0.0252 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.69 |  | 21.9096 | 3.562 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1610.62 |  | 1579.7637 | 1.9532 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 512.95 |  | 516.4806 | -0.6836 | 568.16 | 542.4 | 0.3996 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 816.41 |  | 817.6983 | -0.1576 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.5 |  | 254.4971 | 0.0011 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 674.66 |  | 675.5537 | -0.1323 | 664.875 | 657.17 | 0.0548 | below_vwap | below_vwap |
| ARM | ai_accelerator | 273.18 |  | 275.7264 | -0.9235 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 177.18 |  | 175.9213 | 0.7155 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
