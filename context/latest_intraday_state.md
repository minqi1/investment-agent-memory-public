# Intraday State

- Generated at: `2026-07-16T03:56:05+08:00`
- Market time ET: `2026-07-15T15:56:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'watch_only': 5, 'below_vwap': 2, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.14 |  | 716.3669 | 0.1079 | 724.31 | 721.08 | 0.007 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.57 |  | 551.9509 | 0.4745 | 575.7 | 565.33 | 0.0487 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.17 |  | 587.745 | 0.2425 | 606.85 | 597.81 | 0.0255 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.16 |  | 753.3845 | 0.1029 | 755.54 | 754.215 | 0.0053 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.735 |  | 369.19 | 0.4185 | 364.41 | 357.885 | 0.2266 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.205 |  | 254.4832 | 0.2836 | 252.89 | 249.98 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 681.26 |  | 675.8724 | 0.7971 | 664.875 | 657.17 | 0.0484 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.45 |  | 325.9282 | 0.4669 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.705 |  | 22.0207 | 3.1074 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.205 |  | 254.4832 | 0.2836 | 252.89 | 249.98 | 0.0274 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 295.63 |  | 295.6246 | 0.0018 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| 3 | SKHY | memory_hbm_storage | 176.4 |  | 175.8067 | 0.3375 | 183.63 | 176.08 | 0.0794 | watch_only | none |
| 4 | META | cloud_ai_capex | 681.26 |  | 675.8724 | 0.7971 | 664.875 | 657.17 | 0.0484 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.45 |  | 325.9282 | 0.4669 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 370.735 |  | 369.19 | 0.4185 | 364.41 | 357.885 | 0.2266 | buy_precheck_manual_confirm | none |
| 7 | NVDA | ai_accelerator | 211.92 |  | 209.6033 | 1.1053 | 213.775 | 211.225 | 0.0094 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.355 |  | 132.0664 | 0.2185 | 132.925 | 129.92 | 1.3298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1807.45 |  | 1776.21 | 1.7588 | 1829.9 | 1759.045 | 0.0332 | watch_only | none |
| 10 | AVGO | custom_silicon_networking | 394.2 |  | 392.4874 | 0.4363 | 397.94 | 392.62 | 2.3085 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SPY | market_regime | 754.16 |  | 753.3845 | 0.1029 | 755.54 | 754.215 | 0.0053 | below_opening_15m_low | below_opening_15m_low |
| 12 | AMD | ai_accelerator | 529 |  | 527.5782 | 0.2695 | 558.62 | 548.745 | 0.034 | below_opening_15m_low | below_opening_15m_low |
| 13 | TT | data_center_power_cooling | 479.79 |  | 478.697 | 0.2283 | 485.9 | 482.93 | 0.1334 | below_opening_15m_low | below_opening_15m_low |
| 14 | CORZ | high_beta_ai_infrastructure | 22.705 |  | 22.0207 | 3.1074 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 15 | SMH | semiconductor_index | 589.17 |  | 587.745 | 0.2425 | 606.85 | 597.81 | 0.0255 | below_opening_15m_low | below_opening_15m_low |
| 16 | QQQ | market_regime | 717.14 |  | 716.3669 | 0.1079 | 724.31 | 721.08 | 0.007 | below_opening_15m_low | below_opening_15m_low |
| 17 | APLD | high_beta_ai_infrastructure | 28.95 |  | 28.413 | 1.8898 | 29.055 | 28.28 | 0.0345 | watch_only | none |
| 18 | SMCI | ai_server_oem | 26.98 |  | 26.9047 | 0.28 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 19 | TSM | foundry | 420.36 |  | 419.1636 | 0.2854 | 428.59 | 422.945 | 0.1856 | below_opening_15m_low | below_opening_15m_low |
| 20 | ARM | ai_accelerator | 275.84 |  | 275.5909 | 0.0904 | 286.73 | 280.14 | 0.2103 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.735 |  | 369.19 | 0.4185 | 364.41 | 357.885 | 0.2266 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.205 |  | 254.4832 | 0.2836 | 252.89 | 249.98 | 0.0274 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 681.26 |  | 675.8724 | 0.7971 | 664.875 | 657.17 | 0.0484 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.45 |  | 325.9282 | 0.4669 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.705 |  | 22.0207 | 3.1074 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 394.84 |  | 395.3844 | -0.1377 | 391.33 | 387.05 | 0.1646 | below_vwap | below_vwap |
| 7 | NVDA | ai_accelerator | 211.92 |  | 209.6033 | 1.1053 | 213.775 | 211.225 | 0.0094 | watch_only | none |
| 8 | ASML | semiconductor_equipment | 1807.45 |  | 1776.21 | 1.7588 | 1829.9 | 1759.045 | 0.0332 | watch_only | none |
| 9 | IWM | market_regime | 295.63 |  | 295.6246 | 0.0018 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| 10 | SKHY | memory_hbm_storage | 176.4 |  | 175.8067 | 0.3375 | 183.63 | 176.08 | 0.0794 | watch_only | none |
| 11 | APLD | high_beta_ai_infrastructure | 28.95 |  | 28.413 | 1.8898 | 29.055 | 28.28 | 0.0345 | watch_only | none |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 394.2 |  | 392.4874 | 0.4363 | 397.94 | 392.62 | 2.3085 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 304.975 |  | 299.9783 | 1.6657 | 309.345 | 304.67 | 3.8397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | ORCL | cloud_ai_capex | 132.355 |  | 132.0664 | 0.2185 | 132.925 | 129.92 | 1.3298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SOXX | semiconductor_index | 554.57 |  | 551.9509 | 0.4745 | 575.7 | 565.33 | 0.0487 | below_opening_15m_low | below_opening_15m_low |
| 17 | ANET | ai_networking_optical | 172.08 |  | 171.8408 | 0.1392 | 186.095 | 178.355 | 4.0737 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | STX | memory_hbm_storage | 824.745 |  | 818.157 | 0.8052 | 889.1 | 850.01 | 1.0961 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | SPY | market_regime | 754.16 |  | 753.3845 | 0.1029 | 755.54 | 754.215 | 0.0053 | below_opening_15m_low | below_opening_15m_low |
| 20 | AMAT | semiconductor_equipment | 579.75 |  | 577.6047 | 0.3714 | 610.62 | 586.86 | 0.1035 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.14 |  | 716.3669 | 0.1079 | 724.31 | 721.08 | 0.007 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.22 |  | 74.1836 | 0.049 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 211.92 |  | 209.6033 | 1.1053 | 213.775 | 211.225 | 0.0094 | watch_only | none |
| MSFT | cloud_ai_capex | 394.84 |  | 395.3844 | -0.1377 | 391.33 | 387.05 | 0.1646 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.45 |  | 325.9282 | 0.4669 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.735 |  | 369.19 | 0.4185 | 364.41 | 357.885 | 0.2266 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529 |  | 527.5782 | 0.2695 | 558.62 | 548.745 | 0.034 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 420.36 |  | 419.1636 | 0.2854 | 428.59 | 422.945 | 0.1856 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.57 |  | 551.9509 | 0.4745 | 575.7 | 565.33 | 0.0487 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.17 |  | 587.745 | 0.2425 | 606.85 | 597.81 | 0.0255 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.2 |  | 392.4874 | 0.4363 | 397.94 | 392.62 | 2.3085 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 907.3 |  | 909.3267 | -0.2229 | 977.7 | 953.67 | 0.0132 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 205.84 |  | 207.8864 | -0.9844 | 223.02 | 214.85 | 0.1312 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 414.66 |  | 407.5857 | 1.7356 | 457.935 | 442.67 | 1.6158 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 47.63 |  | 47.0839 | 1.1599 | 50.2 | 48.995 | 0.021 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 26.98 |  | 26.9047 | 0.28 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.16 |  | 753.3845 | 0.1029 | 755.54 | 754.215 | 0.0053 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.63 |  | 295.6246 | 0.0018 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| ORCL | cloud_ai_capex | 132.355 |  | 132.0664 | 0.2185 | 132.925 | 129.92 | 1.3298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.055 |  | 77.4696 | -0.5352 | 80.585 | 78.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 304.975 |  | 299.9783 | 1.6657 | 309.345 | 304.67 | 3.8397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 413.17 |  | 409.337 | 0.9364 | 417.84 | 413.82 | 0.0847 | below_opening_15m_low | below_opening_15m_low |
| PWR | data_center_power_cooling | 650.295 |  | 646.7744 | 0.5443 | 663.475 | 653.94 | 0.083 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1053.07 |  | 1038.8249 | 1.3713 | 1073.34 | 1059.27 | 0.1225 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 479.79 |  | 478.697 | 0.2283 | 485.9 | 482.93 | 0.1334 | below_opening_15m_low | below_opening_15m_low |
| JCI | data_center_power_cooling | 143.03 |  | 141.9224 | 0.7804 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 172.08 |  | 171.8408 | 0.1392 | 186.095 | 178.355 | 4.0737 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 298.665 |  | 294.6351 | 1.3678 | 315.74 | 303.34 | 0.3047 | below_opening_15m_low | below_opening_15m_low |
| LITE | ai_networking_optical | 754.11 |  | 749.5362 | 0.6102 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 419.6 |  | 419.9956 | -0.0942 | 438.14 | 427.54 | 4.4566 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.74 |  | 111.5822 | -0.7548 | 123.995 | 117.25 | 1.6886 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 349.42 |  | 345.4559 | 1.1475 | 369.23 | 356.615 | 0.3177 | below_opening_15m_low | below_opening_15m_low |
| ASML | semiconductor_equipment | 1807.45 |  | 1776.21 | 1.7588 | 1829.9 | 1759.045 | 0.0332 | watch_only | none |
| AMAT | semiconductor_equipment | 579.75 |  | 577.6047 | 0.3714 | 610.62 | 586.86 | 0.1035 | below_opening_15m_low | below_opening_15m_low |
| LRCX | semiconductor_equipment | 334.04 |  | 331.6049 | 0.7343 | 355.245 | 340.745 | 4.1193 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 223.44 |  | 222.7705 | 0.3005 | 236.49 | 225.11 | 1.8887 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 341.24 |  | 336.9516 | 1.2727 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 304.87 |  | 306.8558 | -0.6472 | 326.25 | 317.3 | 4.3658 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.38 |  | 67.0925 | 0.4285 | 70.42 | 68.43 | 4.2594 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.045 |  | 54.39 | 1.2042 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 138.365 |  | 137.7133 | 0.4732 | 143.15 | 140.4 | 0.412 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 353.78 |  | 349.5218 | 1.2183 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 514.8 |  | 515.9318 | -0.2194 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 294.015 |  | 294.314 | -0.1016 | 297.8 | 295.655 | 4.8093 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.95 |  | 28.413 | 1.8898 | 29.055 | 28.28 | 0.0345 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.38 |  | 39.1667 | -2.0087 | 40.01 | 38.815 | 0.0521 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.705 |  | 22.0207 | 3.1074 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1615 |  | 1588.3794 | 1.676 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 515.2 |  | 516.0874 | -0.172 | 568.16 | 542.4 | 3.2104 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 824.745 |  | 818.157 | 0.8052 | 889.1 | 850.01 | 1.0961 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMZN | cloud_ai_capex | 255.205 |  | 254.4832 | 0.2836 | 252.89 | 249.98 | 0.0274 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 681.26 |  | 675.8724 | 0.7971 | 664.875 | 657.17 | 0.0484 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 275.84 |  | 275.5909 | 0.0904 | 286.73 | 280.14 | 0.2103 | below_opening_15m_low | below_opening_15m_low |
| SKHY | memory_hbm_storage | 176.4 |  | 175.8067 | 0.3375 | 183.63 | 176.08 | 0.0794 | watch_only | none |
