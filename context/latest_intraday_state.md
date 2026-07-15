# Intraday State

- Generated at: `2026-07-16T03:08:34+08:00`
- Market time ET: `2026-07-15T15:08:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 39, 'watch_only': 5, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 2, 'below_vwap': 4, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.49 |  | 716.3561 | 0.0187 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 553.32 |  | 551.4566 | 0.3379 | 575.7 | 565.33 | 0.0741 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.35 |  | 587.3081 | 0.1774 | 606.85 | 597.81 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.71 |  | 753.3061 | 0.0536 | 755.54 | 754.215 | 0.008 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.59 |  | 395.3752 | 0.0543 | 391.33 | 387.05 | 0.0228 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 369.97 |  | 368.9742 | 0.2699 | 364.41 | 357.885 | 0.0324 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 328.405 |  | 325.7791 | 0.806 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.9443 | 3.0789 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.59 |  | 395.3752 | 0.0543 | 391.33 | 387.05 | 0.0228 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 369.97 |  | 368.9742 | 0.2699 | 364.41 | 357.885 | 0.0324 | buy_precheck_manual_confirm | none |
| 3 | ORCL | cloud_ai_capex | 132.355 |  | 131.9164 | 0.3325 | 132.925 | 129.92 | 0.1058 | watch_only | none |
| 4 | SKHY | memory_hbm_storage | 176.5 |  | 175.9278 | 0.3253 | 183.63 | 176.08 | 0.1926 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 28.52 |  | 28.3173 | 0.7158 | 29.055 | 28.28 | 0.0351 | watch_only | none |
| 6 | NVDA | ai_accelerator | 211.72 |  | 209.3335 | 1.14 | 213.775 | 211.225 | 0.0378 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1790.83 |  | 1772.802 | 1.0169 | 1829.9 | 1759.045 | 0.1335 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 328.405 |  | 325.7791 | 0.806 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.9443 | 3.0789 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 394.105 |  | 392.1114 | 0.5084 | 397.94 | 392.62 | 3.6462 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SOXX | semiconductor_index | 553.32 |  | 551.4566 | 0.3379 | 575.7 | 565.33 | 0.0741 | below_opening_15m_low | below_opening_15m_low |
| 12 | SPY | market_regime | 753.71 |  | 753.3061 | 0.0536 | 755.54 | 754.215 | 0.008 | below_opening_15m_low | below_opening_15m_low |
| 13 | TSM | foundry | 419.14 |  | 418.9877 | 0.0363 | 428.59 | 422.945 | 0.1288 | below_opening_15m_low | below_opening_15m_low |
| 14 | SMH | semiconductor_index | 588.35 |  | 587.3081 | 0.1774 | 606.85 | 597.81 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| 15 | QQQ | market_regime | 716.49 |  | 716.3561 | 0.0187 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| 16 | META | cloud_ai_capex | 676.87 |  | 675.5881 | 0.1897 | 664.875 | 657.17 | 0.4595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | JCI | data_center_power_cooling | 142.18 |  | 141.8065 | 0.2634 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 331.52 |  | 331.4094 | 0.0334 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | COHR | ai_networking_optical | 294.31 |  | 294.0546 | 0.0869 | 315.74 | 303.34 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 137.78 |  | 137.6656 | 0.0831 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.59 |  | 395.3752 | 0.0543 | 391.33 | 387.05 | 0.0228 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 369.97 |  | 368.9742 | 0.2699 | 364.41 | 357.885 | 0.0324 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 328.405 |  | 325.7791 | 0.806 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.9443 | 3.0789 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 254.4 |  | 254.4972 | -0.0382 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 6 | NVDA | ai_accelerator | 211.72 |  | 209.3335 | 1.14 | 213.775 | 211.225 | 0.0378 | watch_only | none |
| 7 | META | cloud_ai_capex | 676.87 |  | 675.5881 | 0.1897 | 664.875 | 657.17 | 0.4595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1790.83 |  | 1772.802 | 1.0169 | 1829.9 | 1759.045 | 0.1335 | watch_only | none |
| 9 | SKHY | memory_hbm_storage | 176.5 |  | 175.9278 | 0.3253 | 183.63 | 176.08 | 0.1926 | watch_only | none |
| 10 | ORCL | cloud_ai_capex | 132.355 |  | 131.9164 | 0.3325 | 132.925 | 129.92 | 0.1058 | watch_only | none |
| 11 | APLD | high_beta_ai_infrastructure | 28.52 |  | 28.3173 | 0.7158 | 29.055 | 28.28 | 0.0351 | watch_only | none |
| 12 | IWM | market_regime | 295.475 |  | 295.6402 | -0.0559 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 39.01 |  | 39.2652 | -0.6498 | 40.01 | 38.815 | 0.0513 | below_vwap | below_vwap |
| 15 | AVGO | custom_silicon_networking | 394.105 |  | 392.1114 | 0.5084 | 397.94 | 392.62 | 3.6462 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | CIEN | ai_networking_optical | 421.91 |  | 419.6999 | 0.5266 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | SOXX | semiconductor_index | 553.32 |  | 551.4566 | 0.3379 | 575.7 | 565.33 | 0.0741 | below_opening_15m_low | below_opening_15m_low |
| 18 | SPY | market_regime | 753.71 |  | 753.3061 | 0.0536 | 755.54 | 754.215 | 0.008 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMD | ai_accelerator | 527.78 |  | 527.4495 | 0.0627 | 558.62 | 548.745 | 1.133 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | VRT | data_center_power_cooling | 302.105 |  | 299.4171 | 0.8977 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.49 |  | 716.3561 | 0.0187 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.01 |  | 74.1975 | -0.2527 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.72 |  | 209.3335 | 1.14 | 213.775 | 211.225 | 0.0378 | watch_only | none |
| MSFT | cloud_ai_capex | 395.59 |  | 395.3752 | 0.0543 | 391.33 | 387.05 | 0.0228 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 328.405 |  | 325.7791 | 0.806 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 369.97 |  | 368.9742 | 0.2699 | 364.41 | 357.885 | 0.0324 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 527.78 |  | 527.4495 | 0.0627 | 558.62 | 548.745 | 1.133 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 419.14 |  | 418.9877 | 0.0363 | 428.59 | 422.945 | 0.1288 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.32 |  | 551.4566 | 0.3379 | 575.7 | 565.33 | 0.0741 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.35 |  | 587.3081 | 0.1774 | 606.85 | 597.81 | 0.0833 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.105 |  | 392.1114 | 0.5084 | 397.94 | 392.62 | 3.6462 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 905.36 |  | 909.9691 | -0.5065 | 977.7 | 953.67 | 0.0784 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.89 |  | 208.2969 | -0.6754 | 223.02 | 214.85 | 0.9087 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 405.985 |  | 406.9958 | -0.2484 | 457.935 | 442.67 | 2.707 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.355 |  | 46.9346 | 0.8958 | 50.2 | 48.995 | 0.0422 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.075 |  | 26.8879 | 0.696 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.71 |  | 753.3061 | 0.0536 | 755.54 | 754.215 | 0.008 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.475 |  | 295.6402 | -0.0559 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.355 |  | 131.9164 | 0.3325 | 132.925 | 129.92 | 0.1058 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.13 |  | 77.501 | -0.4787 | 80.585 | 78.73 | 0.0519 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 302.105 |  | 299.4171 | 0.8977 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411 |  | 408.6283 | 0.5804 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.23 |  | 646.0196 | 0.8065 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1052.43 |  | 1036.0203 | 1.5839 | 1073.34 | 1059.27 | 0.1416 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 477.94 |  | 478.6865 | -0.156 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.18 |  | 141.8065 | 0.2634 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.54 |  | 171.8163 | -0.1608 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 294.31 |  | 294.0546 | 0.0869 | 315.74 | 303.34 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LITE | ai_networking_optical | 748.02 |  | 749.1987 | -0.1573 | 820.15 | 780.365 | 0.3115 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 421.91 |  | 419.6999 | 0.5266 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 109.465 |  | 112.1202 | -2.3682 | 123.995 | 117.25 | 3.8825 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 348.84 |  | 344.8052 | 1.1702 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1790.83 |  | 1772.802 | 1.0169 | 1829.9 | 1759.045 | 0.1335 | watch_only | none |
| AMAT | semiconductor_equipment | 575.43 |  | 577.6175 | -0.3787 | 610.62 | 586.86 | 0.6291 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 331.52 |  | 331.4094 | 0.0334 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 222.66 |  | 222.6718 | -0.0053 | 236.49 | 225.11 | 0.1392 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 339.93 |  | 336.1852 | 1.1139 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 303.91 |  | 307.1824 | -1.0653 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.24 |  | 66.9995 | 0.3589 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.78 |  | 137.6656 | 0.0831 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| MKSI | semiconductor_materials | 350.96 |  | 348.8011 | 0.6189 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.69 |  | 516.099 | -0.0792 | 521.075 | 518.3 | 0.1784 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 293.415 |  | 294.4341 | -0.3461 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.52 |  | 28.3173 | 0.7158 | 29.055 | 28.28 | 0.0351 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.01 |  | 39.2652 | -0.6498 | 40.01 | 38.815 | 0.0513 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.62 |  | 21.9443 | 3.0789 | 22.36 | 21.94 | 0.0442 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1627.135 |  | 1581.4223 | 2.8906 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 512.88 |  | 516.3824 | -0.6783 | 568.16 | 542.4 | 2.9968 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 816.025 |  | 817.5884 | -0.1912 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.4 |  | 254.4972 | -0.0382 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| META | cloud_ai_capex | 676.87 |  | 675.5881 | 0.1897 | 664.875 | 657.17 | 0.4595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.96 |  | 275.6253 | -0.6042 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 176.5 |  | 175.9278 | 0.3253 | 183.63 | 176.08 | 0.1926 | watch_only | none |
