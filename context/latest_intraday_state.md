# Intraday State

- Generated at: `2026-07-16T01:49:05+08:00`
- Market time ET: `2026-07-15T13:49:07-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 8, 'price_stale_or_missing': 2, 'below_vwap': 2, 'spread_too_wide_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.79 |  | 716.1762 | 0.0857 | 724.31 | 721.08 | 0.0084 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 552.83 |  | 551.0943 | 0.315 | 575.7 | 565.33 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 586.95 |  | 587.2272 | -0.0472 | 606.85 | 597.81 | 0.0716 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.92 |  | 753.133 | 0.1045 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.925 |  | 395.1189 | 0.204 | 391.33 | 387.05 | 0.0682 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.255 |  | 295.6064 | 0.2194 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.82 |  | 368.5987 | 0.6026 | 364.41 | 357.885 | 0.2265 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.885 |  | 254.4443 | 0.1732 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.49 |  | 325.4563 | 0.6249 | 321.14 | 317.4 | 0.1924 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 132.975 |  | 131.6415 | 1.013 | 132.925 | 129.92 | 0.0376 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.4 |  | 21.7055 | 3.1995 | 22.36 | 21.94 | 0.0893 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.06 |  | 28.1458 | 3.248 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.255 |  | 295.6064 | 0.2194 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.885 |  | 254.4443 | 0.1732 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 395.925 |  | 395.1189 | 0.204 | 391.33 | 387.05 | 0.0682 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1784.78 |  | 1770.9126 | 0.7831 | 1829.9 | 1759.045 | 0.0885 | watch_only | none |
| 5 | ORCL | cloud_ai_capex | 132.975 |  | 131.6415 | 1.013 | 132.925 | 129.92 | 0.0376 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 370.82 |  | 368.5987 | 0.6026 | 364.41 | 357.885 | 0.2265 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 327.49 |  | 325.4563 | 0.6249 | 321.14 | 317.4 | 0.1924 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 22.4 |  | 21.7055 | 3.1995 | 22.36 | 21.94 | 0.0893 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 29.06 |  | 28.1458 | 3.248 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 393.055 |  | 391.6927 | 0.3478 | 397.94 | 392.62 | 1.3102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | NVDA | ai_accelerator | 209.28 |  | 209.1527 | 0.0609 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 12 | SOXX | semiconductor_index | 552.83 |  | 551.0943 | 0.315 | 575.7 | 565.33 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| 13 | SPY | market_regime | 753.92 |  | 753.133 | 0.1045 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 14 | TSM | foundry | 419 |  | 418.8531 | 0.0351 | 428.59 | 422.945 | 0.0668 | below_opening_15m_low | below_opening_15m_low |
| 15 | KLAC | semiconductor_equipment | 222.775 |  | 222.6036 | 0.077 | 236.49 | 225.11 | 0.0718 | below_opening_15m_low | below_opening_15m_low |
| 16 | QQQ | market_regime | 716.79 |  | 716.1762 | 0.0857 | 724.31 | 721.08 | 0.0084 | below_opening_15m_low | below_opening_15m_low |
| 17 | IREN | high_beta_ai_infrastructure | 39.77 |  | 39.0918 | 1.735 | 40.01 | 38.815 | 0.0251 | watch_only | none |
| 18 | TT | data_center_power_cooling | 478.81 |  | 478.7332 | 0.0161 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 410.36 |  | 408.3718 | 0.4869 | 417.84 | 413.82 | 0.1633 | below_opening_15m_low | below_opening_15m_low |
| 20 | MU | memory_hbm_storage | 910.94 |  | 910.1032 | 0.0919 | 977.7 | 953.67 | 0.7399 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.925 |  | 395.1189 | 0.204 | 391.33 | 387.05 | 0.0682 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.255 |  | 295.6064 | 0.2194 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.82 |  | 368.5987 | 0.6026 | 364.41 | 357.885 | 0.2265 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.885 |  | 254.4443 | 0.1732 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.49 |  | 325.4563 | 0.6249 | 321.14 | 317.4 | 0.1924 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 132.975 |  | 131.6415 | 1.013 | 132.925 | 129.92 | 0.0376 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.4 |  | 21.7055 | 3.1995 | 22.36 | 21.94 | 0.0893 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.06 |  | 28.1458 | 3.248 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |
| 9 | META | cloud_ai_capex | 675.38 |  | 675.4569 | -0.0114 | 664.875 | 657.17 | 0.804 | below_vwap | below_vwap,spread_too_wide |
| 10 | ASML | semiconductor_equipment | 1784.78 |  | 1770.9126 | 0.7831 | 1829.9 | 1759.045 | 0.0885 | watch_only | none |
| 11 | IREN | high_beta_ai_infrastructure | 39.77 |  | 39.0918 | 1.735 | 40.01 | 38.815 | 0.0251 | watch_only | none |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 393.055 |  | 391.6927 | 0.3478 | 397.94 | 392.62 | 1.3102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 209.28 |  | 209.1527 | 0.0609 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 15 | MU | memory_hbm_storage | 910.94 |  | 910.1032 | 0.0919 | 977.7 | 953.67 | 0.7399 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | SOXX | semiconductor_index | 552.83 |  | 551.0943 | 0.315 | 575.7 | 565.33 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| 17 | SPY | market_regime | 753.92 |  | 753.133 | 0.1045 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 18 | AMD | ai_accelerator | 529.49 |  | 527.1032 | 0.4528 | 558.62 | 548.745 | 0.9122 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | TT | data_center_power_cooling | 478.81 |  | 478.7332 | 0.0161 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | VRT | data_center_power_cooling | 300.02 |  | 299.0044 | 0.3397 | 309.345 | 304.67 | 4.8097 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.79 |  | 716.1762 | 0.0857 | 724.31 | 721.08 | 0.0084 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.1 |  | 74.1929 | -0.1252 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.28 |  | 209.1527 | 0.0609 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.925 |  | 395.1189 | 0.204 | 391.33 | 387.05 | 0.0682 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.49 |  | 325.4563 | 0.6249 | 321.14 | 317.4 | 0.1924 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.82 |  | 368.5987 | 0.6026 | 364.41 | 357.885 | 0.2265 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.49 |  | 527.1032 | 0.4528 | 558.62 | 548.745 | 0.9122 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 419 |  | 418.8531 | 0.0351 | 428.59 | 422.945 | 0.0668 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.83 |  | 551.0943 | 0.315 | 575.7 | 565.33 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 586.95 |  | 587.2272 | -0.0472 | 606.85 | 597.81 | 0.0716 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 393.055 |  | 391.6927 | 0.3478 | 397.94 | 392.62 | 1.3102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 910.94 |  | 910.1032 | 0.0919 | 977.7 | 953.67 | 0.7399 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 207.5 |  | 208.5269 | -0.4924 | 223.02 | 214.85 | 0.1446 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 400.085 |  | 407.4384 | -1.8048 | 457.935 | 442.67 | 4.0216 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.655 |  | 46.922 | -0.569 | 50.2 | 48.995 | 0.0429 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.845 |  | 26.8665 | -0.0799 | 28.295 | 27.55 | 0.0373 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.92 |  | 753.133 | 0.1045 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 296.255 |  | 295.6064 | 0.2194 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 132.975 |  | 131.6415 | 1.013 | 132.925 | 129.92 | 0.0376 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 77.375 |  | 77.3866 | -0.0149 | 80.585 | 78.73 | 4.8078 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 300.02 |  | 299.0044 | 0.3397 | 309.345 | 304.67 | 4.8097 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ETN | data_center_power_cooling | 410.36 |  | 408.3718 | 0.4869 | 417.84 | 413.82 | 0.1633 | below_opening_15m_low | below_opening_15m_low |
| PWR | data_center_power_cooling | 648.58 |  | 644.2787 | 0.6676 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1046.45 |  | 1031.7562 | 1.4242 | 1073.34 | 1059.27 | 3.0866 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 478.81 |  | 478.7332 | 0.0161 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 141.54 |  | 141.6801 | -0.0989 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.315 |  | 171.9262 | -0.9371 | 186.095 | 178.355 | 5.073 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.215 |  | 293.8521 | 0.1235 | 315.74 | 303.34 | 3.3989 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 753.61 |  | 748.1518 | 0.7296 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 418.53 |  | 418.8675 | -0.0806 | 438.14 | 427.54 | 2.4514 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.38 |  | 112.348 | -0.8616 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 346.9 |  | 344.6164 | 0.6626 | 369.23 | 356.615 | 4.1741 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1784.78 |  | 1770.9126 | 0.7831 | 1829.9 | 1759.045 | 0.0885 | watch_only | none |
| AMAT | semiconductor_equipment | 576.715 |  | 577.7372 | -0.1769 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 330.25 |  | 331.4088 | -0.3497 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.775 |  | 222.6036 | 0.077 | 236.49 | 225.11 | 0.0718 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 337.71 |  | 335.413 | 0.6848 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 303.61 |  | 307.5016 | -1.2655 | 326.25 | 317.3 | 4.3016 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| AMKR | semiconductor_test_packaging | 67.395 |  | 66.7912 | 0.904 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.205 |  | 54.3324 | -0.2344 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 137.18 |  | 137.6681 | -0.3545 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 350.1 |  | 348.4173 | 0.483 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.25 |  | 516.108 | 0.0275 | 521.075 | 518.3 | 4.8213 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 293.9 |  | 295.0888 | -0.4029 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.06 |  | 28.1458 | 3.248 | 29.055 | 28.28 | 0.0688 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 39.77 |  | 39.0918 | 1.735 | 40.01 | 38.815 | 0.0251 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.4 |  | 21.7055 | 3.1995 | 22.36 | 21.94 | 0.0893 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1608.9 |  | 1563.9338 | 2.8752 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 509.8 |  | 516.7896 | -1.3525 | 568.16 | 542.4 | 0.3609 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 814.75 |  | 817.2576 | -0.3068 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.885 |  | 254.4443 | 0.1732 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.38 |  | 675.4569 | -0.0114 | 664.875 | 657.17 | 0.804 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 273.1 |  | 275.9864 | -1.0458 | 286.73 | 280.14 | 3.5884 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 175.26 |  | 175.6038 | -0.1958 | 183.63 | 176.08 | 0.1826 | below_opening_15m_low | below_opening_15m_low,below_vwap |
