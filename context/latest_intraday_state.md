# Intraday State

- Generated at: `2026-07-16T03:12:34+08:00`
- Market time ET: `2026-07-15T15:12:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'watch_only': 3, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'below_vwap': 3, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.98 |  | 716.3548 | -0.0523 | 724.31 | 721.08 | 0.021 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 551.8 |  | 551.4683 | 0.0601 | 575.7 | 565.33 | 0.0979 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588 |  | 587.3103 | 0.1174 | 606.85 | 597.81 | 0.0748 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.56 |  | 753.3082 | 0.0334 | 755.54 | 754.215 | 0.0252 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.445 |  | 395.3769 | 0.0172 | 391.33 | 387.05 | 0.0354 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.25 |  | 368.9809 | 0.3439 | 364.41 | 357.885 | 0.0486 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.68 |  | 254.4986 | 0.0713 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.925 |  | 325.7974 | 0.653 | 321.14 | 317.4 | 0.0274 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.63 |  | 21.9504 | 3.0959 | 22.36 | 21.94 | 0.0884 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.68 |  | 254.4986 | 0.0713 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 395.445 |  | 395.3769 | 0.0172 | 391.33 | 387.05 | 0.0354 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.25 |  | 368.9809 | 0.3439 | 364.41 | 357.885 | 0.0486 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.925 |  | 325.7974 | 0.653 | 321.14 | 317.4 | 0.0274 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 211.475 |  | 209.3661 | 1.0073 | 213.775 | 211.225 | 0.0142 | watch_only | none |
| 6 | ASML | semiconductor_equipment | 1788.13 |  | 1772.8593 | 0.8614 | 1829.9 | 1759.045 | 0.1247 | watch_only | none |
| 7 | ORCL | cloud_ai_capex | 132.195 |  | 131.9237 | 0.2056 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APLD | high_beta_ai_infrastructure | 28.55 |  | 28.3196 | 0.8136 | 29.055 | 28.28 | 0.035 | watch_only | none |
| 9 | AVGO | custom_silicon_networking | 393.13 |  | 392.1351 | 0.2537 | 397.94 | 392.62 | 0.5316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | CORZ | high_beta_ai_infrastructure | 22.63 |  | 21.9504 | 3.0959 | 22.36 | 21.94 | 0.0884 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 551.8 |  | 551.4683 | 0.0601 | 575.7 | 565.33 | 0.0979 | below_opening_15m_low | below_opening_15m_low |
| 12 | SPY | market_regime | 753.56 |  | 753.3082 | 0.0334 | 755.54 | 754.215 | 0.0252 | below_opening_15m_low | below_opening_15m_low |
| 13 | SMH | semiconductor_index | 588 |  | 587.3103 | 0.1174 | 606.85 | 597.81 | 0.0748 | below_opening_15m_low | below_opening_15m_low |
| 14 | META | cloud_ai_capex | 677.11 |  | 675.6009 | 0.2234 | 664.875 | 657.17 | 0.5627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | KLAC | semiconductor_equipment | 222.815 |  | 222.6712 | 0.0646 | 236.49 | 225.11 | 0.1526 | below_opening_15m_low | below_opening_15m_low |
| 16 | JCI | data_center_power_cooling | 142.305 |  | 141.813 | 0.347 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | SMCI | ai_server_oem | 27.025 |  | 26.8889 | 0.506 | 28.295 | 27.55 | 0.074 | below_opening_15m_low | below_opening_15m_low |
| 18 | IWM | market_regime | 295.525 |  | 295.6396 | -0.0388 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 19 | HPE | ai_server_oem | 47.28 |  | 46.9398 | 0.7247 | 50.2 | 48.995 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| 20 | CIEN | ai_networking_optical | 420.13 |  | 419.707 | 0.1008 | 438.14 | 427.54 | 4.6771 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.445 |  | 395.3769 | 0.0172 | 391.33 | 387.05 | 0.0354 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.25 |  | 368.9809 | 0.3439 | 364.41 | 357.885 | 0.0486 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.68 |  | 254.4986 | 0.0713 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.925 |  | 325.7974 | 0.653 | 321.14 | 317.4 | 0.0274 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.63 |  | 21.9504 | 3.0959 | 22.36 | 21.94 | 0.0884 | buy_precheck_manual_confirm | none |
| 6 | NVDA | ai_accelerator | 211.475 |  | 209.3661 | 1.0073 | 213.775 | 211.225 | 0.0142 | watch_only | none |
| 7 | META | cloud_ai_capex | 677.11 |  | 675.6009 | 0.2234 | 664.875 | 657.17 | 0.5627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1788.13 |  | 1772.8593 | 0.8614 | 1829.9 | 1759.045 | 0.1247 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.55 |  | 28.3196 | 0.8136 | 29.055 | 28.28 | 0.035 | watch_only | none |
| 10 | IWM | market_regime | 295.525 |  | 295.6396 | -0.0388 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 39.07 |  | 39.2638 | -0.4935 | 40.01 | 38.815 | 0.0512 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 393.13 |  | 392.1351 | 0.2537 | 397.94 | 392.62 | 0.5316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 132.195 |  | 131.9237 | 0.2056 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | CIEN | ai_networking_optical | 420.13 |  | 419.707 | 0.1008 | 438.14 | 427.54 | 4.6771 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | SOXX | semiconductor_index | 551.8 |  | 551.4683 | 0.0601 | 575.7 | 565.33 | 0.0979 | below_opening_15m_low | below_opening_15m_low |
| 17 | SPY | market_regime | 753.56 |  | 753.3082 | 0.0334 | 755.54 | 754.215 | 0.0252 | below_opening_15m_low | below_opening_15m_low |
| 18 | VRT | data_center_power_cooling | 302.49 |  | 299.434 | 1.0206 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1617.66 |  | 1581.786 | 2.2679 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 142.305 |  | 141.813 | 0.347 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.98 |  | 716.3548 | -0.0523 | 724.31 | 721.08 | 0.021 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.865 |  | 74.1962 | -0.4464 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.475 |  | 209.3661 | 1.0073 | 213.775 | 211.225 | 0.0142 | watch_only | none |
| MSFT | cloud_ai_capex | 395.445 |  | 395.3769 | 0.0172 | 391.33 | 387.05 | 0.0354 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.925 |  | 325.7974 | 0.653 | 321.14 | 317.4 | 0.0274 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.25 |  | 368.9809 | 0.3439 | 364.41 | 357.885 | 0.0486 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 526.855 |  | 527.4461 | -0.1121 | 558.62 | 548.745 | 0.2505 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 418.94 |  | 418.9858 | -0.0109 | 428.59 | 422.945 | 0.0621 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.8 |  | 551.4683 | 0.0601 | 575.7 | 565.33 | 0.0979 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588 |  | 587.3103 | 0.1174 | 606.85 | 597.81 | 0.0748 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 393.13 |  | 392.1351 | 0.2537 | 397.94 | 392.62 | 0.5316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 901.065 |  | 909.9157 | -0.9727 | 977.7 | 953.67 | 0.6359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 205.495 |  | 208.2483 | -1.3221 | 223.02 | 214.85 | 0.2628 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 404.3 |  | 406.9817 | -0.6589 | 457.935 | 442.67 | 2.3374 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.28 |  | 46.9398 | 0.7247 | 50.2 | 48.995 | 0.0212 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.025 |  | 26.8889 | 0.506 | 28.295 | 27.55 | 0.074 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.56 |  | 753.3082 | 0.0334 | 755.54 | 754.215 | 0.0252 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.525 |  | 295.6396 | -0.0388 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.195 |  | 131.9237 | 0.2056 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 77.15 |  | 77.4995 | -0.4509 | 80.585 | 78.73 | 5.1329 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.49 |  | 299.434 | 1.0206 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.38 |  | 408.6402 | 0.6705 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.61 |  | 646.0751 | 0.8567 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1053.065 |  | 1036.1903 | 1.6285 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 477.785 |  | 478.6782 | -0.1866 | 485.9 | 482.93 | 0.1444 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.305 |  | 141.813 | 0.347 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.255 |  | 171.8098 | -0.3229 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 293.87 |  | 294.055 | -0.0629 | 315.74 | 303.34 | 4.5632 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 745.02 |  | 749.1793 | -0.5552 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 420.13 |  | 419.707 | 0.1008 | 438.14 | 427.54 | 4.6771 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 108.29 |  | 112.0377 | -3.345 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 346.925 |  | 344.8214 | 0.6101 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1788.13 |  | 1772.8593 | 0.8614 | 1829.9 | 1759.045 | 0.1247 | watch_only | none |
| AMAT | semiconductor_equipment | 575.345 |  | 577.6074 | -0.3917 | 610.62 | 586.86 | 1.2184 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 330.97 |  | 331.4007 | -0.13 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.815 |  | 222.6712 | 0.0646 | 236.49 | 225.11 | 0.1526 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 339.71 |  | 336.2072 | 1.0418 | 356.29 | 343.785 | 4.6981 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 303.91 |  | 307.1824 | -1.0653 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.25 |  | 67.0034 | 0.368 | 70.42 | 68.43 | 4.8922 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.535 |  | 137.6642 | -0.0938 | 143.15 | 140.4 | 5.1042 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 350.42 |  | 348.8425 | 0.4522 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.81 |  | 516.0985 | -0.0559 | 521.075 | 518.3 | 0.2695 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 293.8 |  | 294.4189 | -0.2102 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.55 |  | 28.3196 | 0.8136 | 29.055 | 28.28 | 0.035 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.07 |  | 39.2638 | -0.4935 | 40.01 | 38.815 | 0.0512 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.63 |  | 21.9504 | 3.0959 | 22.36 | 21.94 | 0.0884 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1617.66 |  | 1581.786 | 2.2679 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 510.27 |  | 516.3412 | -1.1758 | 568.16 | 542.4 | 1.7638 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 815.63 |  | 817.574 | -0.2378 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.68 |  | 254.4986 | 0.0713 | 252.89 | 249.98 | 0.0118 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 677.11 |  | 675.6009 | 0.2234 | 664.875 | 657.17 | 0.5627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.6 |  | 275.6018 | -0.7263 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 175.18 |  | 175.9261 | -0.4241 | 183.63 | 176.08 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
