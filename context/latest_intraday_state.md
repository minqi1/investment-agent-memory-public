# Intraday State

- Generated at: `2026-07-16T02:52:43+08:00`
- Market time ET: `2026-07-15T14:52:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'below_vwap': 3, 'spread_too_wide_or_missing': 1, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.54 |  | 716.3841 | -0.1178 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.37 |  | 551.4861 | -0.2024 | 575.7 | 565.33 | 0.0636 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.37 |  | 587.3459 | -0.3364 | 606.85 | 597.81 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.27 |  | 753.3032 | -0.0044 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.135 |  | 395.363 | 0.1953 | 391.33 | 387.05 | 0.1893 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 371.04 |  | 368.9233 | 0.5738 | 364.41 | 357.885 | 0.1186 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.55 |  | 254.4972 | 0.0207 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.2 |  | 325.6954 | 0.462 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.655 |  | 21.9151 | 3.3762 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.55 |  | 254.4972 | 0.0207 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.135 |  | 395.363 | 0.1953 | 391.33 | 387.05 | 0.1893 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1780.31 |  | 1772.5739 | 0.4364 | 1829.9 | 1759.045 | 0.1275 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 371.04 |  | 368.9233 | 0.5738 | 364.41 | 357.885 | 0.1186 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.2 |  | 325.6954 | 0.462 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 39.58 |  | 39.2842 | 0.753 | 40.01 | 38.815 | 0.0505 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.655 |  | 21.9151 | 3.3762 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 28.79 |  | 28.3067 | 1.7072 | 29.055 | 28.28 | 0.1389 | watch_only | none |
| 9 | SMCI | ai_server_oem | 26.93 |  | 26.8861 | 0.1632 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 10 | ORCL | cloud_ai_capex | 132.68 |  | 131.8812 | 0.6057 | 132.925 | 129.92 | 0.5276 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | JCI | data_center_power_cooling | 142.23 |  | 141.7961 | 0.306 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 12 | NVDA | ai_accelerator | 210.07 |  | 209.2764 | 0.3792 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 13 | MKSI | semiconductor_materials | 349.88 |  | 348.7849 | 0.314 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 14 | LITE | ai_networking_optical | 751.27 |  | 749.2204 | 0.2736 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | LIN | industrial_gases | 516.34 |  | 516.0942 | 0.0476 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | IWM | market_regime | 295.28 |  | 295.6457 | -0.1237 | 296.08 | 294.86 | 0.0034 | below_vwap | below_vwap |
| 17 | AVGO | custom_silicon_networking | 392.44 |  | 392.0732 | 0.0936 | 397.94 | 392.62 | 0.7313 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ALAB | ai_networking_optical | 347.5 |  | 344.7628 | 0.7939 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 411.005 |  | 408.6057 | 0.5872 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.135 |  | 395.363 | 0.1953 | 391.33 | 387.05 | 0.1893 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 371.04 |  | 368.9233 | 0.5738 | 364.41 | 357.885 | 0.1186 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 254.55 |  | 254.4972 | 0.0207 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.2 |  | 325.6954 | 0.462 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.655 |  | 21.9151 | 3.3762 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 674.145 |  | 675.5495 | -0.2079 | 664.875 | 657.17 | 0.224 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1780.31 |  | 1772.5739 | 0.4364 | 1829.9 | 1759.045 | 0.1275 | watch_only | none |
| 8 | IREN | high_beta_ai_infrastructure | 39.58 |  | 39.2842 | 0.753 | 40.01 | 38.815 | 0.0505 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.79 |  | 28.3067 | 1.7072 | 29.055 | 28.28 | 0.1389 | watch_only | none |
| 10 | IWM | market_regime | 295.28 |  | 295.6457 | -0.1237 | 296.08 | 294.86 | 0.0034 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ORCL | cloud_ai_capex | 132.68 |  | 131.8812 | 0.6057 | 132.925 | 129.92 | 0.5276 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | NVDA | ai_accelerator | 210.07 |  | 209.2764 | 0.3792 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 14 | CIEN | ai_networking_optical | 423.255 |  | 419.5617 | 0.8803 | 438.14 | 427.54 | 4.4441 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | AVGO | custom_silicon_networking | 392.44 |  | 392.0732 | 0.0936 | 397.94 | 392.62 | 0.7313 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | VRT | data_center_power_cooling | 301.975 |  | 299.3383 | 0.8808 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1597.61 |  | 1580.2492 | 1.0986 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 142.23 |  | 141.7961 | 0.306 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 652.87 |  | 645.9228 | 1.0755 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | GEV | data_center_power_cooling | 1052.55 |  | 1035.1724 | 1.6787 | 1073.34 | 1059.27 | 0.0979 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.54 |  | 716.3841 | -0.1178 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.725 |  | 74.2068 | -0.6493 | 76.46 | 75.39 | 0.0271 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.07 |  | 209.2764 | 0.3792 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.135 |  | 395.363 | 0.1953 | 391.33 | 387.05 | 0.1893 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.2 |  | 325.6954 | 0.462 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.04 |  | 368.9233 | 0.5738 | 364.41 | 357.885 | 0.1186 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 526.04 |  | 527.477 | -0.2724 | 558.62 | 548.745 | 1.4828 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 418.13 |  | 419.0077 | -0.2095 | 428.59 | 422.945 | 0.0287 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.37 |  | 551.4861 | -0.2024 | 575.7 | 565.33 | 0.0636 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.37 |  | 587.3459 | -0.3364 | 606.85 | 597.81 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 392.44 |  | 392.0732 | 0.0936 | 397.94 | 392.62 | 0.7313 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MU | memory_hbm_storage | 900.47 |  | 910.2126 | -1.0704 | 977.7 | 953.67 | 0.0466 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.53 |  | 208.3557 | -0.8763 | 223.02 | 214.85 | 1.3073 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.52 |  | 407.1095 | -1.373 | 457.935 | 442.67 | 1.6288 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.86 |  | 46.9243 | -0.1371 | 50.2 | 48.995 | 0.0427 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.93 |  | 26.8861 | 0.1632 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.27 |  | 753.3032 | -0.0044 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.28 |  | 295.6457 | -0.1237 | 296.08 | 294.86 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.68 |  | 131.8812 | 0.6057 | 132.925 | 129.92 | 0.5276 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.645 |  | 77.508 | 0.1767 | 80.585 | 78.73 | 3.4387 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 301.975 |  | 299.3383 | 0.8808 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.005 |  | 408.6057 | 0.5872 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 652.87 |  | 645.9228 | 1.0755 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1052.55 |  | 1035.1724 | 1.6787 | 1073.34 | 1059.27 | 0.0979 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 477.46 |  | 478.7031 | -0.2597 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.23 |  | 141.7961 | 0.306 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 170.83 |  | 171.848 | -0.5924 | 186.095 | 178.355 | 2.283 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.23 |  | 294.0616 | 0.0573 | 315.74 | 303.34 | 3.5822 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 751.27 |  | 749.2204 | 0.2736 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 423.255 |  | 419.5617 | 0.8803 | 438.14 | 427.54 | 4.4441 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 110 |  | 112.2055 | -1.9656 | 123.995 | 117.25 | 3.9182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 347.5 |  | 344.7628 | 0.7939 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1780.31 |  | 1772.5739 | 0.4364 | 1829.9 | 1759.045 | 0.1275 | watch_only | none |
| AMAT | semiconductor_equipment | 574.19 |  | 577.6891 | -0.6057 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 330.12 |  | 331.437 | -0.3974 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.41 |  | 222.6754 | -0.1192 | 236.49 | 225.11 | 4.4872 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 337.99 |  | 336.1423 | 0.5497 | 356.29 | 343.785 | 5.0357 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 303.75 |  | 307.3697 | -1.1776 | 326.25 | 317.3 | 4.3687 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.37 |  | 66.9972 | 0.5564 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.28 |  | 137.6849 | -0.2941 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 349.88 |  | 348.7849 | 0.314 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.34 |  | 516.0942 | 0.0476 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 293.86 |  | 294.4669 | -0.2061 | 297.8 | 295.655 | 0.507 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.79 |  | 28.3067 | 1.7072 | 29.055 | 28.28 | 0.1389 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.58 |  | 39.2842 | 0.753 | 40.01 | 38.815 | 0.0505 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.655 |  | 21.9151 | 3.3762 | 22.36 | 21.94 | 0.0441 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1597.61 |  | 1580.2492 | 1.0986 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 511.83 |  | 516.4602 | -0.8965 | 568.16 | 542.4 | 1.522 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 814.42 |  | 817.6928 | -0.4003 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.55 |  | 254.4972 | 0.0207 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 674.145 |  | 675.5495 | -0.2079 | 664.875 | 657.17 | 0.224 | below_vwap | below_vwap |
| ARM | ai_accelerator | 272.87 |  | 275.7076 | -1.0292 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 175.75 |  | 175.9264 | -0.1002 | 183.63 | 176.08 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
