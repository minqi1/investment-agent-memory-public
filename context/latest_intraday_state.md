# Intraday State

- Generated at: `2026-07-16T02:28:44+08:00`
- Market time ET: `2026-07-15T14:28:45-04:00`
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
| QQQ | market_regime | 718.41 |  | 716.3413 | 0.2888 | 724.31 | 721.08 | 0.0097 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.9 |  | 551.422 | 0.6307 | 575.7 | 565.33 | 0.0469 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.45 |  | 587.3233 | 0.3621 | 606.85 | 597.81 | 0.0611 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.7 |  | 753.2541 | 0.192 | 755.54 | 754.215 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.715 |  | 395.3028 | 0.3572 | 391.33 | 387.05 | 0.0403 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.43 |  | 368.8191 | 0.9791 | 364.41 | 357.885 | 0.0242 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.03 |  | 254.4821 | 0.2153 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.43 |  | 325.6075 | 0.5597 | 321.14 | 317.4 | 0.0153 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.81 |  | 21.8721 | 4.2882 | 22.36 | 21.94 | 0.0877 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.365 |  | 39.2067 | 2.9544 | 40.01 | 38.815 | 0.0248 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.22 |  | 28.2652 | 3.3779 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.03 |  | 254.4821 | 0.2153 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.7 |  | 753.2541 | 0.192 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 3 | IWM | market_regime | 295.81 |  | 295.6461 | 0.0554 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 396.715 |  | 395.3028 | 0.3572 | 391.33 | 387.05 | 0.0403 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.43 |  | 325.6075 | 0.5597 | 321.14 | 317.4 | 0.0153 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 394.785 |  | 391.9817 | 0.7152 | 397.94 | 392.62 | 0.2001 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1789.84 |  | 1772.2375 | 0.9932 | 1829.9 | 1759.045 | 0.1408 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 372.43 |  | 368.8191 | 0.9791 | 364.41 | 357.885 | 0.0242 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 29.22 |  | 28.2652 | 3.3779 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 40.365 |  | 39.2067 | 2.9544 | 40.01 | 38.815 | 0.0248 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 22.81 |  | 21.8721 | 4.2882 | 22.36 | 21.94 | 0.0877 | buy_precheck_manual_confirm | none |
| 12 | QQQ | market_regime | 718.41 |  | 716.3413 | 0.2888 | 724.31 | 721.08 | 0.0097 | below_opening_15m_low | below_opening_15m_low |
| 13 | META | cloud_ai_capex | 677.555 |  | 675.5433 | 0.2978 | 664.875 | 657.17 | 0.7409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | HPE | ai_server_oem | 47.09 |  | 46.9263 | 0.3488 | 50.2 | 48.995 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| 15 | AMAT | semiconductor_equipment | 578.82 |  | 577.7406 | 0.1868 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | NVDA | ai_accelerator | 210.67 |  | 209.2275 | 0.6894 | 213.775 | 211.225 | 0.0237 | below_opening_15m_low | below_opening_15m_low |
| 17 | LRCX | semiconductor_equipment | 332.59 |  | 331.4457 | 0.3452 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | ONTO | semiconductor_test_packaging | 307.61 |  | 307.4622 | 0.0481 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | MU | memory_hbm_storage | 914.12 |  | 910.2163 | 0.4289 | 977.7 | 953.67 | 0.0613 | below_opening_15m_low | below_opening_15m_low |
| 20 | SOXX | semiconductor_index | 554.9 |  | 551.422 | 0.6307 | 575.7 | 565.33 | 0.0469 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.715 |  | 395.3028 | 0.3572 | 391.33 | 387.05 | 0.0403 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.43 |  | 368.8191 | 0.9791 | 364.41 | 357.885 | 0.0242 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.03 |  | 254.4821 | 0.2153 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.43 |  | 325.6075 | 0.5597 | 321.14 | 317.4 | 0.0153 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.81 |  | 21.8721 | 4.2882 | 22.36 | 21.94 | 0.0877 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.365 |  | 39.2067 | 2.9544 | 40.01 | 38.815 | 0.0248 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.22 |  | 28.2652 | 3.3779 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 394.785 |  | 391.9817 | 0.7152 | 397.94 | 392.62 | 0.2001 | watch_only | none |
| 9 | META | cloud_ai_capex | 677.555 |  | 675.5433 | 0.2978 | 664.875 | 657.17 | 0.7409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ASML | semiconductor_equipment | 1789.84 |  | 1772.2375 | 0.9932 | 1829.9 | 1759.045 | 0.1408 | watch_only | none |
| 11 | SPY | market_regime | 754.7 |  | 753.2541 | 0.192 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 12 | ORCL | cloud_ai_capex | 133.56 |  | 131.7817 | 1.3494 | 132.925 | 129.92 | 4.1255 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | IWM | market_regime | 295.81 |  | 295.6461 | 0.0554 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 180.455 |  | 175.7991 | 2.6484 | 183.63 | 176.08 | 0.3768 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.67 |  | 209.2275 | 0.6894 | 213.775 | 211.225 | 0.0237 | below_opening_15m_low | below_opening_15m_low |
| 17 | MU | memory_hbm_storage | 914.12 |  | 910.2163 | 0.4289 | 977.7 | 953.67 | 0.0613 | below_opening_15m_low | below_opening_15m_low |
| 18 | CIEN | ai_networking_optical | 425.88 |  | 419.3174 | 1.5651 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SOXX | semiconductor_index | 554.9 |  | 551.422 | 0.6307 | 575.7 | 565.33 | 0.0469 | below_opening_15m_low | below_opening_15m_low |
| 20 | ANET | ai_networking_optical | 172.005 |  | 171.8695 | 0.0788 | 186.095 | 178.355 | 2.9185 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.41 |  | 716.3413 | 0.2888 | 724.31 | 721.08 | 0.0097 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.62 |  | 74.2035 | 0.5613 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.67 |  | 209.2275 | 0.6894 | 213.775 | 211.225 | 0.0237 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.715 |  | 395.3028 | 0.3572 | 391.33 | 387.05 | 0.0403 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.43 |  | 325.6075 | 0.5597 | 321.14 | 317.4 | 0.0153 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.43 |  | 368.8191 | 0.9791 | 364.41 | 357.885 | 0.0242 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 532.04 |  | 527.3663 | 0.8862 | 558.62 | 548.745 | 0.1673 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 421.26 |  | 418.9773 | 0.5448 | 428.59 | 422.945 | 0.5341 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.9 |  | 551.422 | 0.6307 | 575.7 | 565.33 | 0.0469 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.45 |  | 587.3233 | 0.3621 | 606.85 | 597.81 | 0.0611 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.785 |  | 391.9817 | 0.7152 | 397.94 | 392.62 | 0.2001 | watch_only | none |
| MU | memory_hbm_storage | 914.12 |  | 910.2163 | 0.4289 | 977.7 | 953.67 | 0.0613 | below_opening_15m_low | below_opening_15m_low |
| MRVL | custom_silicon_networking | 207.72 |  | 208.4315 | -0.3413 | 223.02 | 214.85 | 0.2263 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 408.37 |  | 407.1894 | 0.2899 | 457.935 | 442.67 | 1.9198 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 47.09 |  | 46.9263 | 0.3488 | 50.2 | 48.995 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.08 |  | 26.8793 | 0.7465 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.7 |  | 753.2541 | 0.192 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| IWM | market_regime | 295.81 |  | 295.6461 | 0.0554 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 133.56 |  | 131.7817 | 1.3494 | 132.925 | 129.92 | 4.1255 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.07 |  | 77.4697 | 0.7749 | 80.585 | 78.73 | 4.022 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 302.5 |  | 299.2425 | 1.0886 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.18 |  | 408.5417 | 0.6458 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.47 |  | 644.9649 | 1.0086 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1057.72 |  | 1033.526 | 2.3409 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.39 |  | 478.7406 | -0.0732 | 485.9 | 482.93 | 0.0857 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.57 |  | 141.7434 | 0.5832 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 172.005 |  | 171.8695 | 0.0788 | 186.095 | 178.355 | 2.9185 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 295.69 |  | 294.0192 | 0.5683 | 315.74 | 303.34 | 0.487 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 756.24 |  | 748.9882 | 0.9682 | 820.15 | 780.365 | 2.8245 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 425.88 |  | 419.3174 | 1.5651 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 110.91 |  | 112.2837 | -1.2234 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 350.66 |  | 344.7064 | 1.7272 | 369.23 | 356.615 | 4.5942 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1789.84 |  | 1772.2375 | 0.9932 | 1829.9 | 1759.045 | 0.1408 | watch_only | none |
| AMAT | semiconductor_equipment | 578.82 |  | 577.7406 | 0.1868 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LRCX | semiconductor_equipment | 332.59 |  | 331.4457 | 0.3452 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.835 |  | 222.6571 | 0.529 | 236.49 | 225.11 | 2.7654 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 341.11 |  | 335.6773 | 1.6184 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 307.61 |  | 307.4622 | 0.0481 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.96 |  | 66.9252 | 1.5462 | 70.42 | 68.43 | 4.1495 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3553 | 0.3398 | 57.92 | 55.2 | 4.2538 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 138.08 |  | 137.6856 | 0.2864 | 143.15 | 140.4 | 4.4322 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 352.26 |  | 348.7507 | 1.0062 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.24 |  | 516.0921 | -0.1651 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.005 |  | 294.5617 | -0.5285 | 297.8 | 295.655 | 0.1195 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 29.22 |  | 28.2652 | 3.3779 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 40.365 |  | 39.2067 | 2.9544 | 40.01 | 38.815 | 0.0248 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.81 |  | 21.8721 | 4.2882 | 22.36 | 21.94 | 0.0877 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1647.48 |  | 1575.9703 | 4.5375 | 1726.34 | 1665.91 | 3.0956 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 516.655 |  | 516.5694 | 0.0166 | 568.16 | 542.4 | 0.4607 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| STX | memory_hbm_storage | 824.15 |  | 817.5647 | 0.8055 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 255.03 |  | 254.4821 | 0.2153 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 677.555 |  | 675.5433 | 0.2978 | 664.875 | 657.17 | 0.7409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 274.92 |  | 275.834 | -0.3313 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 180.455 |  | 175.7991 | 2.6484 | 183.63 | 176.08 | 0.3768 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
