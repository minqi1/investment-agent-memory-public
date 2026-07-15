# Intraday State

- Generated at: `2026-07-16T02:44:43+08:00`
- Market time ET: `2026-07-15T14:44:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 7, 'price_stale_or_missing': 1, 'below_vwap': 1, 'spread_too_wide_or_missing': 1, 'watch_only': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.1 |  | 716.3864 | 0.0996 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 552.82 |  | 551.472 | 0.2444 | 575.7 | 565.33 | 0.0597 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.11 |  | 587.3503 | -0.0409 | 606.85 | 597.81 | 0.0647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.3 |  | 753.2898 | 0.1341 | 755.54 | 754.215 | 0.0146 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.6 |  | 395.3515 | 0.3158 | 391.33 | 387.05 | 0.0252 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.28 |  | 368.8931 | 0.9181 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.02 |  | 254.4923 | 0.2073 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 675.68 |  | 675.5603 | 0.0177 | 664.875 | 657.17 | 0.0607 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.6 |  | 325.665 | 0.5942 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 133.27 |  | 131.8489 | 1.0779 | 132.925 | 129.92 | 0.0375 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.9022 | 3.7795 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.6 |  | 395.3515 | 0.3158 | 391.33 | 387.05 | 0.0252 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.02 |  | 254.4923 | 0.2073 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 754.3 |  | 753.2898 | 0.1341 | 755.54 | 754.215 | 0.0146 | watch_only | none |
| 4 | IWM | market_regime | 295.73 |  | 295.6503 | 0.027 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| 5 | META | cloud_ai_capex | 675.68 |  | 675.5603 | 0.0177 | 664.875 | 657.17 | 0.0607 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1782.39 |  | 1772.4856 | 0.5588 | 1829.9 | 1759.045 | 0.0713 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 327.6 |  | 325.665 | 0.5942 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 133.27 |  | 131.8489 | 1.0779 | 132.925 | 129.92 | 0.0375 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 372.28 |  | 368.8931 | 0.9181 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 39.845 |  | 39.2702 | 1.4638 | 40.01 | 38.815 | 0.0502 | watch_only | none |
| 11 | AVGO | custom_silicon_networking | 393.39 |  | 392.0438 | 0.3434 | 397.94 | 392.62 | 3.3783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SKHY | memory_hbm_storage | 177.9 |  | 175.9162 | 1.1277 | 183.63 | 176.08 | 0.2698 | watch_only | none |
| 13 | SOXX | semiconductor_index | 552.82 |  | 551.472 | 0.2444 | 575.7 | 565.33 | 0.0597 | below_opening_15m_low | below_opening_15m_low |
| 14 | CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.9022 | 3.7795 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 15 | QQQ | market_regime | 717.1 |  | 716.3864 | 0.0996 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| 16 | APLD | high_beta_ai_infrastructure | 28.99 |  | 28.2947 | 2.4573 | 29.055 | 28.28 | 0.1035 | watch_only | none |
| 17 | AMD | ai_accelerator | 529.28 |  | 527.4595 | 0.3451 | 558.62 | 548.745 | 0.153 | below_opening_15m_low | below_opening_15m_low |
| 18 | NVDA | ai_accelerator | 210.36 |  | 209.2618 | 0.5248 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 19 | LIN | industrial_gases | 516.5 |  | 516.0929 | 0.0789 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | SMCI | ai_server_oem | 26.995 |  | 26.8847 | 0.4104 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.6 |  | 395.3515 | 0.3158 | 391.33 | 387.05 | 0.0252 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.28 |  | 368.8931 | 0.9181 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.02 |  | 254.4923 | 0.2073 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 675.68 |  | 675.5603 | 0.0177 | 664.875 | 657.17 | 0.0607 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.6 |  | 325.665 | 0.5942 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 133.27 |  | 131.8489 | 1.0779 | 132.925 | 129.92 | 0.0375 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.9022 | 3.7795 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1782.39 |  | 1772.4856 | 0.5588 | 1829.9 | 1759.045 | 0.0713 | watch_only | none |
| 9 | SPY | market_regime | 754.3 |  | 753.2898 | 0.1341 | 755.54 | 754.215 | 0.0146 | watch_only | none |
| 10 | IWM | market_regime | 295.73 |  | 295.6503 | 0.027 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| 11 | SKHY | memory_hbm_storage | 177.9 |  | 175.9162 | 1.1277 | 183.63 | 176.08 | 0.2698 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 39.845 |  | 39.2702 | 1.4638 | 40.01 | 38.815 | 0.0502 | watch_only | none |
| 13 | APLD | high_beta_ai_infrastructure | 28.99 |  | 28.2947 | 2.4573 | 29.055 | 28.28 | 0.1035 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 393.39 |  | 392.0438 | 0.3434 | 397.94 | 392.62 | 3.3783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.36 |  | 209.2618 | 0.5248 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 17 | CIEN | ai_networking_optical | 422.25 |  | 419.5181 | 0.6512 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SOXX | semiconductor_index | 552.82 |  | 551.472 | 0.2444 | 575.7 | 565.33 | 0.0597 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMD | ai_accelerator | 529.28 |  | 527.4595 | 0.3451 | 558.62 | 548.745 | 0.153 | below_opening_15m_low | below_opening_15m_low |
| 20 | VRT | data_center_power_cooling | 301.65 |  | 299.3081 | 0.7824 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.1 |  | 716.3864 | 0.0996 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.215 |  | 74.2106 | 0.0059 | 76.46 | 75.39 | 0.0269 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.36 |  | 209.2618 | 0.5248 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.6 |  | 395.3515 | 0.3158 | 391.33 | 387.05 | 0.0252 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.6 |  | 325.665 | 0.5942 | 321.14 | 317.4 | 0.0244 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.28 |  | 368.8931 | 0.9181 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.28 |  | 527.4595 | 0.3451 | 558.62 | 548.745 | 0.153 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 419.37 |  | 419.0089 | 0.0862 | 428.59 | 422.945 | 1.7049 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.82 |  | 551.472 | 0.2444 | 575.7 | 565.33 | 0.0597 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.11 |  | 587.3503 | -0.0409 | 606.85 | 597.81 | 0.0647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 393.39 |  | 392.0438 | 0.3434 | 397.94 | 392.62 | 3.3783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 908.19 |  | 910.2769 | -0.2293 | 977.7 | 953.67 | 0.1398 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.9 |  | 208.3835 | -0.7119 | 223.02 | 214.85 | 0.3045 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 404.29 |  | 407.1595 | -0.7048 | 457.935 | 442.67 | 2.9533 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.71 |  | 46.9269 | -0.4622 | 50.2 | 48.995 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.995 |  | 26.8847 | 0.4104 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.3 |  | 753.2898 | 0.1341 | 755.54 | 754.215 | 0.0146 | watch_only | none |
| IWM | market_regime | 295.73 |  | 295.6503 | 0.027 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| ORCL | cloud_ai_capex | 133.27 |  | 131.8489 | 1.0779 | 132.925 | 129.92 | 0.0375 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 78.09 |  | 77.5017 | 0.7591 | 80.585 | 78.73 | 0.0512 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 301.65 |  | 299.3081 | 0.7824 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.705 |  | 408.5785 | 0.5205 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 650.75 |  | 645.7582 | 0.773 | 663.475 | 653.94 | 0.2858 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1055.83 |  | 1034.4914 | 2.0627 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.335 |  | 478.7234 | -0.0811 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.41 |  | 141.7637 | 0.4559 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.2 |  | 171.8675 | -0.3884 | 186.095 | 178.355 | 2.5409 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.63 |  | 294.0571 | 0.1948 | 315.74 | 303.34 | 2.0636 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 751.81 |  | 749.1834 | 0.3506 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 422.25 |  | 419.5181 | 0.6512 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 110.1 |  | 112.2306 | -1.8984 | 123.995 | 117.25 | 4.2234 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 349 |  | 344.7543 | 1.2315 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1782.39 |  | 1772.4856 | 0.5588 | 1829.9 | 1759.045 | 0.0713 | watch_only | none |
| AMAT | semiconductor_equipment | 575.08 |  | 577.7129 | -0.4557 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 331.19 |  | 331.4533 | -0.0794 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.955 |  | 222.6757 | 0.1254 | 236.49 | 225.11 | 1.1886 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 339.39 |  | 336.1203 | 0.9728 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 305.25 |  | 307.4307 | -0.7093 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.655 |  | 66.9706 | 1.0219 | 70.42 | 68.43 | 4.1682 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 | 0.4767 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 137.56 |  | 137.6918 | -0.0957 | 143.15 | 140.4 | 3.4385 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 350.67 |  | 348.7766 | 0.5429 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.5 |  | 516.0929 | 0.0789 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 293.79 |  | 294.4914 | -0.2382 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.99 |  | 28.2947 | 2.4573 | 29.055 | 28.28 | 0.1035 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.845 |  | 39.2702 | 1.4638 | 40.01 | 38.815 | 0.0502 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.73 |  | 21.9022 | 3.7795 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1610.77 |  | 1579.4866 | 1.9806 | 1726.34 | 1665.91 | 4.4699 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 513.03 |  | 516.5064 | -0.6731 | 568.16 | 542.4 | 4.0933 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 817.33 |  | 817.7049 | -0.0458 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.02 |  | 254.4923 | 0.2073 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.68 |  | 675.5603 | 0.0177 | 664.875 | 657.17 | 0.0607 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 273.69 |  | 275.7566 | -0.7494 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 177.9 |  | 175.9162 | 1.1277 | 183.63 | 176.08 | 0.2698 | watch_only | none |
