# Intraday State

- Generated at: `2026-07-16T02:36:43+08:00`
- Market time ET: `2026-07-15T14:36:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 7, 'price_stale_or_missing': 1, 'below_vwap': 2, 'spread_too_wide_or_missing': 1, 'watch_only': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.83 |  | 716.3625 | 0.2049 | 724.31 | 721.08 | 0.0306 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 553.615 |  | 551.4435 | 0.3938 | 575.7 | 565.33 | 0.0434 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.405 |  | 587.3476 | 0.18 | 606.85 | 597.81 | 0.068 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.63 |  | 753.2787 | 0.1794 | 755.54 | 754.215 | 0.0013 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.83 |  | 395.3333 | 0.3786 | 391.33 | 387.05 | 0.0554 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.28 |  | 368.8553 | 0.9285 | 364.41 | 357.885 | 0.3062 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 675.885 |  | 675.5564 | 0.0486 | 664.875 | 657.17 | 0.1391 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.705 |  | 325.643 | 0.6332 | 321.14 | 317.4 | 0.0458 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 133.615 |  | 131.8116 | 1.3682 | 132.925 | 129.92 | 0.0374 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.8903 | 3.8357 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.1 |  | 28.2866 | 2.8756 | 29.055 | 28.28 | 0.2405 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.63 |  | 753.2787 | 0.1794 | 755.54 | 754.215 | 0.0013 | watch_only | none |
| 2 | IWM | market_regime | 295.79 |  | 295.6498 | 0.0474 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 3 | META | cloud_ai_capex | 675.885 |  | 675.5564 | 0.0486 | 664.875 | 657.17 | 0.1391 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 396.83 |  | 395.3333 | 0.3786 | 391.33 | 387.05 | 0.0554 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.705 |  | 325.643 | 0.6332 | 321.14 | 317.4 | 0.0458 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1785.78 |  | 1772.3597 | 0.7572 | 1829.9 | 1759.045 | 0.1624 | watch_only | none |
| 7 | ORCL | cloud_ai_capex | 133.615 |  | 131.8116 | 1.3682 | 132.925 | 129.92 | 0.0374 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 372.28 |  | 368.8553 | 0.9285 | 364.41 | 357.885 | 0.3062 | buy_precheck_manual_confirm | none |
| 9 | APLD | high_beta_ai_infrastructure | 29.1 |  | 28.2866 | 2.8756 | 29.055 | 28.28 | 0.2405 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 394.04 |  | 392.0196 | 0.5154 | 397.94 | 392.62 | 3.8702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 420.18 |  | 419.0015 | 0.2813 | 428.59 | 422.945 | 0.0762 | below_opening_15m_low | below_opening_15m_low |
| 12 | CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.8903 | 3.8357 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 588.405 |  | 587.3476 | 0.18 | 606.85 | 597.81 | 0.068 | below_opening_15m_low | below_opening_15m_low |
| 14 | QQQ | market_regime | 717.83 |  | 716.3625 | 0.2049 | 724.31 | 721.08 | 0.0306 | below_opening_15m_low | below_opening_15m_low |
| 15 | IREN | high_beta_ai_infrastructure | 39.99 |  | 39.2496 | 1.8865 | 40.01 | 38.815 | 0.025 | watch_only | none |
| 16 | HPE | ai_server_oem | 47.01 |  | 46.9292 | 0.1723 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 17 | SKHY | memory_hbm_storage | 179.06 |  | 175.8941 | 1.7999 | 183.63 | 176.08 | 0.2792 | watch_only | none |
| 18 | STX | memory_hbm_storage | 819.79 |  | 817.6875 | 0.2571 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SOXX | semiconductor_index | 553.615 |  | 551.4435 | 0.3938 | 575.7 | 565.33 | 0.0434 | below_opening_15m_low | below_opening_15m_low |
| 20 | SMCI | ai_server_oem | 27.045 |  | 26.8828 | 0.6033 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.83 |  | 395.3333 | 0.3786 | 391.33 | 387.05 | 0.0554 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.28 |  | 368.8553 | 0.9285 | 364.41 | 357.885 | 0.3062 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 675.885 |  | 675.5564 | 0.0486 | 664.875 | 657.17 | 0.1391 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.705 |  | 325.643 | 0.6332 | 321.14 | 317.4 | 0.0458 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 133.615 |  | 131.8116 | 1.3682 | 132.925 | 129.92 | 0.0374 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.8903 | 3.8357 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.1 |  | 28.2866 | 2.8756 | 29.055 | 28.28 | 0.2405 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 254.46 |  | 254.4824 | -0.0088 | 252.89 | 249.98 | 0.0196 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1785.78 |  | 1772.3597 | 0.7572 | 1829.9 | 1759.045 | 0.1624 | watch_only | none |
| 10 | SPY | market_regime | 754.63 |  | 753.2787 | 0.1794 | 755.54 | 754.215 | 0.0013 | watch_only | none |
| 11 | IWM | market_regime | 295.79 |  | 295.6498 | 0.0474 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 12 | SKHY | memory_hbm_storage | 179.06 |  | 175.8941 | 1.7999 | 183.63 | 176.08 | 0.2792 | watch_only | none |
| 13 | IREN | high_beta_ai_infrastructure | 39.99 |  | 39.2496 | 1.8865 | 40.01 | 38.815 | 0.025 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 394.04 |  | 392.0196 | 0.5154 | 397.94 | 392.62 | 3.8702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.555 |  | 209.244 | 0.6266 | 213.775 | 211.225 | 1.7858 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | CIEN | ai_networking_optical | 425.1 |  | 419.4325 | 1.3512 | 438.14 | 427.54 | 3.5333 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SOXX | semiconductor_index | 553.615 |  | 551.4435 | 0.3938 | 575.7 | 565.33 | 0.0434 | below_opening_15m_low | below_opening_15m_low |
| 19 | STX | memory_hbm_storage | 819.79 |  | 817.6875 | 0.2571 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | AMD | ai_accelerator | 530.62 |  | 527.4266 | 0.6055 | 558.62 | 548.745 | 0.2921 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.83 |  | 716.3625 | 0.2049 | 724.31 | 721.08 | 0.0306 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.46 |  | 74.2086 | 0.3388 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.555 |  | 209.244 | 0.6266 | 213.775 | 211.225 | 1.7858 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MSFT | cloud_ai_capex | 396.83 |  | 395.3333 | 0.3786 | 391.33 | 387.05 | 0.0554 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.705 |  | 325.643 | 0.6332 | 321.14 | 317.4 | 0.0458 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.28 |  | 368.8553 | 0.9285 | 364.41 | 357.885 | 0.3062 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 530.62 |  | 527.4266 | 0.6055 | 558.62 | 548.745 | 0.2921 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 420.18 |  | 419.0015 | 0.2813 | 428.59 | 422.945 | 0.0762 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.615 |  | 551.4435 | 0.3938 | 575.7 | 565.33 | 0.0434 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.405 |  | 587.3476 | 0.18 | 606.85 | 597.81 | 0.068 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.04 |  | 392.0196 | 0.5154 | 397.94 | 392.62 | 3.8702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 909.58 |  | 910.2929 | -0.0783 | 977.7 | 953.67 | 0.4068 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 207.57 |  | 208.4074 | -0.4018 | 223.02 | 214.85 | 0.1108 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 406.24 |  | 407.1843 | -0.2319 | 457.935 | 442.67 | 2.3459 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.01 |  | 46.9292 | 0.1723 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.045 |  | 26.8828 | 0.6033 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.63 |  | 753.2787 | 0.1794 | 755.54 | 754.215 | 0.0013 | watch_only | none |
| IWM | market_regime | 295.79 |  | 295.6498 | 0.0474 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 133.615 |  | 131.8116 | 1.3682 | 132.925 | 129.92 | 0.0374 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 77.96 |  | 77.4799 | 0.6196 | 80.585 | 78.73 | 3.7327 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 302.29 |  | 299.268 | 1.0098 | 309.345 | 304.67 | 0.0529 | below_opening_15m_low | below_opening_15m_low |
| ETN | data_center_power_cooling | 411.32 |  | 408.5567 | 0.6763 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.97 |  | 645.7317 | 0.9661 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1058.83 |  | 1033.9809 | 2.4032 | 1073.34 | 1059.27 | 1.989 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 478.505 |  | 478.7308 | -0.0472 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.48 |  | 141.7539 | 0.5122 | 145.99 | 144.625 | 0.1684 | below_opening_15m_low | below_opening_15m_low |
| ANET | ai_networking_optical | 171.63 |  | 171.8704 | -0.1398 | 186.095 | 178.355 | 2.9599 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.97 |  | 294.0457 | 0.3143 | 315.74 | 303.34 | 1.9392 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 753.725 |  | 749.1301 | 0.6134 | 820.15 | 780.365 | 3.0475 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 425.1 |  | 419.4325 | 1.3512 | 438.14 | 427.54 | 3.5333 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 110.46 |  | 112.2702 | -1.6123 | 123.995 | 117.25 | 4.1916 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 349.9 |  | 344.7388 | 1.4971 | 369.23 | 356.615 | 0.6002 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1785.78 |  | 1772.3597 | 0.7572 | 1829.9 | 1759.045 | 0.1624 | watch_only | none |
| AMAT | semiconductor_equipment | 576.2 |  | 577.7382 | -0.2662 | 610.62 | 586.86 | 2.7109 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 331.37 |  | 331.4592 | -0.0269 | 355.245 | 340.745 | 1.2131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 223.42 |  | 222.6719 | 0.336 | 236.49 | 225.11 | 4.4669 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 340.69 |  | 336.0625 | 1.377 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 306.705 |  | 307.445 | -0.2407 | 326.25 | 317.3 | 4.7407 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.79 |  | 66.9516 | 1.2522 | 70.42 | 68.43 | 4.1599 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.6 |  | 54.3593 | 0.4428 | 57.92 | 55.2 | 3.9744 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 138.16 |  | 137.6925 | 0.3395 | 143.15 | 140.4 | 3.6118 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 351.66 |  | 348.7647 | 0.8302 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.92 |  | 516.0907 | -0.0331 | 521.075 | 518.3 | 4.8728 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.48 |  | 294.524 | -0.3545 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.1 |  | 28.2866 | 2.8756 | 29.055 | 28.28 | 0.2405 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 39.99 |  | 39.2496 | 1.8865 | 40.01 | 38.815 | 0.025 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.8903 | 3.8357 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1632.26 |  | 1578.1104 | 3.4313 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 514.115 |  | 516.5689 | -0.475 | 568.16 | 542.4 | 4.0847 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 819.79 |  | 817.6875 | 0.2571 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.46 |  | 254.4824 | -0.0088 | 252.89 | 249.98 | 0.0196 | below_vwap | below_vwap |
| META | cloud_ai_capex | 675.885 |  | 675.5564 | 0.0486 | 664.875 | 657.17 | 0.1391 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 274.67 |  | 275.8069 | -0.4122 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 179.06 |  | 175.8941 | 1.7999 | 183.63 | 176.08 | 0.2792 | watch_only | none |
