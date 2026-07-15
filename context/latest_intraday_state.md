# Intraday State

- Generated at: `2026-07-16T02:40:42+08:00`
- Market time ET: `2026-07-15T14:40:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 1, 'below_vwap': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.33 |  | 716.3786 | 0.1328 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 552.62 |  | 551.46 | 0.2104 | 575.7 | 565.33 | 0.0525 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.445 |  | 587.3499 | 0.0162 | 606.85 | 597.81 | 0.0681 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.46 |  | 753.2845 | 0.1561 | 755.54 | 754.215 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.84 |  | 395.3442 | 0.3784 | 391.33 | 387.05 | 0.0378 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.39 |  | 368.8721 | 0.9537 | 364.41 | 357.885 | 0.0081 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.91 |  | 254.4839 | 0.1674 | 252.89 | 249.98 | 0.1765 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.66 |  | 325.6548 | 0.6158 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.695 |  | 21.895 | 3.6539 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.91 |  | 254.4839 | 0.1674 | 252.89 | 249.98 | 0.1765 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.46 |  | 753.2845 | 0.1561 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 3 | IWM | market_regime | 295.76 |  | 295.6501 | 0.0372 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 396.84 |  | 395.3442 | 0.3784 | 391.33 | 387.05 | 0.0378 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1781.1 |  | 1772.4317 | 0.4891 | 1829.9 | 1759.045 | 0.0814 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 327.66 |  | 325.6548 | 0.6158 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 393.22 |  | 392.0321 | 0.303 | 397.94 | 392.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | GOOGL | cloud_ai_capex | 372.39 |  | 368.8721 | 0.9537 | 364.41 | 357.885 | 0.0081 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.695 |  | 21.895 | 3.6539 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 552.62 |  | 551.46 | 0.2104 | 575.7 | 565.33 | 0.0525 | below_opening_15m_low | below_opening_15m_low |
| 11 | SMH | semiconductor_index | 587.445 |  | 587.3499 | 0.0162 | 606.85 | 597.81 | 0.0681 | below_opening_15m_low | below_opening_15m_low |
| 12 | QQQ | market_regime | 717.33 |  | 716.3786 | 0.1328 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| 13 | IREN | high_beta_ai_infrastructure | 39.855 |  | 39.2615 | 1.5117 | 40.01 | 38.815 | 0.0251 | watch_only | none |
| 14 | APLD | high_beta_ai_infrastructure | 28.98 |  | 28.2913 | 2.4341 | 29.055 | 28.28 | 0.1035 | watch_only | none |
| 15 | META | cloud_ai_capex | 676.36 |  | 675.5584 | 0.1187 | 664.875 | 657.17 | 0.8975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 529.13 |  | 527.4461 | 0.3193 | 558.62 | 548.745 | 0.2608 | below_opening_15m_low | below_opening_15m_low |
| 17 | STX | memory_hbm_storage | 818.335 |  | 817.7009 | 0.0775 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | NVDA | ai_accelerator | 210.32 |  | 209.251 | 0.5109 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 19 | LIN | industrial_gases | 516.34 |  | 516.0913 | 0.0482 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 410.81 |  | 408.5639 | 0.5498 | 417.84 | 413.82 | 0.1266 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.84 |  | 395.3442 | 0.3784 | 391.33 | 387.05 | 0.0378 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.39 |  | 368.8721 | 0.9537 | 364.41 | 357.885 | 0.0081 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.91 |  | 254.4839 | 0.1674 | 252.89 | 249.98 | 0.1765 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.66 |  | 325.6548 | 0.6158 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.695 |  | 21.895 | 3.6539 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 676.36 |  | 675.5584 | 0.1187 | 664.875 | 657.17 | 0.8975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1781.1 |  | 1772.4317 | 0.4891 | 1829.9 | 1759.045 | 0.0814 | watch_only | none |
| 8 | SPY | market_regime | 754.46 |  | 753.2845 | 0.1561 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 9 | ORCL | cloud_ai_capex | 133.51 |  | 131.8299 | 1.2745 | 132.925 | 129.92 | 4.157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | IWM | market_regime | 295.76 |  | 295.6501 | 0.0372 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 11 | IREN | high_beta_ai_infrastructure | 39.855 |  | 39.2615 | 1.5117 | 40.01 | 38.815 | 0.0251 | watch_only | none |
| 12 | APLD | high_beta_ai_infrastructure | 28.98 |  | 28.2913 | 2.4341 | 29.055 | 28.28 | 0.1035 | watch_only | none |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 393.22 |  | 392.0321 | 0.303 | 397.94 | 392.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 178.375 |  | 175.9076 | 1.4027 | 183.63 | 176.08 | 1.6762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.32 |  | 209.251 | 0.5109 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 17 | CIEN | ai_networking_optical | 424.63 |  | 419.4732 | 1.2294 | 438.14 | 427.54 | 3.5042 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SOXX | semiconductor_index | 552.62 |  | 551.46 | 0.2104 | 575.7 | 565.33 | 0.0525 | below_opening_15m_low | below_opening_15m_low |
| 19 | STX | memory_hbm_storage | 818.335 |  | 817.7009 | 0.0775 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | AMD | ai_accelerator | 529.13 |  | 527.4461 | 0.3193 | 558.62 | 548.745 | 0.2608 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.33 |  | 716.3786 | 0.1328 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.29 |  | 74.2095 | 0.1085 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.32 |  | 209.251 | 0.5109 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.84 |  | 395.3442 | 0.3784 | 391.33 | 387.05 | 0.0378 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.66 |  | 325.6548 | 0.6158 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.39 |  | 368.8721 | 0.9537 | 364.41 | 357.885 | 0.0081 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.13 |  | 527.4461 | 0.3193 | 558.62 | 548.745 | 0.2608 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 419.39 |  | 419.0061 | 0.0916 | 428.59 | 422.945 | 1.1994 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.62 |  | 551.46 | 0.2104 | 575.7 | 565.33 | 0.0525 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.445 |  | 587.3499 | 0.0162 | 606.85 | 597.81 | 0.0681 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 393.22 |  | 392.0321 | 0.303 | 397.94 | 392.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 907.78 |  | 910.2842 | -0.2751 | 977.7 | 953.67 | 0.369 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.84 |  | 208.3938 | -0.7456 | 223.02 | 214.85 | 0.1305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 404.45 |  | 407.1698 | -0.668 | 457.935 | 442.67 | 4.7596 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.81 |  | 46.9285 | -0.2526 | 50.2 | 48.995 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.02 |  | 26.884 | 0.5057 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.46 |  | 753.2845 | 0.1561 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| IWM | market_regime | 295.76 |  | 295.6501 | 0.0372 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 133.51 |  | 131.8299 | 1.2745 | 132.925 | 129.92 | 4.157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.87 |  | 77.4824 | 0.5002 | 80.585 | 78.73 | 0.2825 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 301.81 |  | 299.2798 | 0.8454 | 309.345 | 304.67 | 0.116 | below_opening_15m_low | below_opening_15m_low |
| ETN | data_center_power_cooling | 410.81 |  | 408.5639 | 0.5498 | 417.84 | 413.82 | 0.1266 | below_opening_15m_low | below_opening_15m_low |
| PWR | data_center_power_cooling | 651.84 |  | 645.7462 | 0.9437 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1056.405 |  | 1034.2892 | 2.1383 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.43 |  | 478.7253 | -0.0617 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.48 |  | 141.7587 | 0.5088 | 145.99 | 144.625 | 5.0674 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ANET | ai_networking_optical | 171.42 |  | 171.8699 | -0.2618 | 186.095 | 178.355 | 2.6485 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.6 |  | 294.0517 | 0.1865 | 315.74 | 303.34 | 3.6897 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 752.48 |  | 749.1493 | 0.4446 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 424.63 |  | 419.4732 | 1.2294 | 438.14 | 427.54 | 3.5042 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 110.04 |  | 112.2573 | -1.9752 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 349 |  | 344.7543 | 1.2315 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1781.1 |  | 1772.4317 | 0.4891 | 1829.9 | 1759.045 | 0.0814 | watch_only | none |
| AMAT | semiconductor_equipment | 575.27 |  | 577.7296 | -0.4257 | 610.62 | 586.86 | 0.7631 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 330.845 |  | 331.4573 | -0.1847 | 355.245 | 340.745 | 1.3874 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 222.8 |  | 222.6743 | 0.0565 | 236.49 | 225.11 | 3.2316 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 339.77 |  | 336.0811 | 1.0976 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 305.54 |  | 307.4386 | -0.6175 | 326.25 | 317.3 | 4.6442 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.61 |  | 66.96 | 0.9707 | 70.42 | 68.43 | 1.2128 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 137.56 |  | 137.6918 | -0.0957 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 350.67 |  | 348.7766 | 0.5429 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.34 |  | 516.0913 | 0.0482 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 293.58 |  | 294.493 | -0.31 | 297.8 | 295.655 | 0.4428 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.98 |  | 28.2913 | 2.4341 | 29.055 | 28.28 | 0.1035 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.855 |  | 39.2615 | 1.5117 | 40.01 | 38.815 | 0.0251 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.695 |  | 21.895 | 3.6539 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1623.3 |  | 1578.818 | 2.8174 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 513.2 |  | 516.536 | -0.6458 | 568.16 | 542.4 | 4.092 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 818.335 |  | 817.7009 | 0.0775 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.91 |  | 254.4839 | 0.1674 | 252.89 | 249.98 | 0.1765 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 676.36 |  | 675.5584 | 0.1187 | 664.875 | 657.17 | 0.8975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.52 |  | 275.7787 | -0.819 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 178.375 |  | 175.9076 | 1.4027 | 183.63 | 176.08 | 1.6762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
