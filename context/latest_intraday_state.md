# Intraday State

- Generated at: `2026-07-16T01:53:02+08:00`
- Market time ET: `2026-07-15T13:53:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 7, 'price_stale_or_missing': 2, 'below_vwap': 2, 'spread_too_wide_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.99 |  | 716.1955 | 0.1109 | 724.31 | 721.08 | 0.0126 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 553.43 |  | 551.1111 | 0.4208 | 575.7 | 565.33 | 0.0705 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.34 |  | 587.2292 | 0.0189 | 606.85 | 597.81 | 0.0579 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.92 |  | 753.1433 | 0.1031 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.4 |  | 395.1274 | 0.069 | 391.33 | 387.05 | 0.0329 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.11 |  | 295.6112 | 0.1687 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 371.635 |  | 368.6182 | 0.8184 | 364.41 | 357.885 | 0.0269 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.835 |  | 254.448 | 0.1521 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.4 |  | 325.4798 | 0.59 | 321.14 | 317.4 | 0.0947 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.52 |  | 21.7221 | 3.6733 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.15 |  | 28.1529 | 3.5419 | 29.055 | 28.28 | 0.2744 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.11 |  | 295.6112 | 0.1687 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.835 |  | 254.448 | 0.1521 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 395.4 |  | 395.1274 | 0.069 | 391.33 | 387.05 | 0.0329 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.4 |  | 325.4798 | 0.59 | 321.14 | 317.4 | 0.0947 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1789.57 |  | 1771.0279 | 1.047 | 1829.9 | 1759.045 | 0.0872 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 371.635 |  | 368.6182 | 0.8184 | 364.41 | 357.885 | 0.0269 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.52 |  | 21.7221 | 3.6733 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.15 |  | 28.1529 | 3.5419 | 29.055 | 28.28 | 0.2744 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 209.59 |  | 209.1563 | 0.2073 | 213.775 | 211.225 | 0.1336 | below_opening_15m_low | below_opening_15m_low |
| 10 | AVGO | custom_silicon_networking | 393.54 |  | 391.7312 | 0.4618 | 397.94 | 392.62 | 1.0672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SPY | market_regime | 753.92 |  | 753.1433 | 0.1031 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| 12 | SMH | semiconductor_index | 587.34 |  | 587.2292 | 0.0189 | 606.85 | 597.81 | 0.0579 | below_opening_15m_low | below_opening_15m_low |
| 13 | QQQ | market_regime | 716.99 |  | 716.1955 | 0.1109 | 724.31 | 721.08 | 0.0126 | below_opening_15m_low | below_opening_15m_low |
| 14 | IREN | high_beta_ai_infrastructure | 39.715 |  | 39.1017 | 1.5683 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| 15 | SMCI | ai_server_oem | 26.93 |  | 26.8667 | 0.2355 | 28.295 | 27.55 | 0.0743 | below_opening_15m_low | below_opening_15m_low |
| 16 | MU | memory_hbm_storage | 911.71 |  | 910.1128 | 0.1755 | 977.7 | 953.67 | 0.3027 | below_opening_15m_low | below_opening_15m_low |
| 17 | TT | data_center_power_cooling | 478.98 |  | 478.7341 | 0.0514 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SOXX | semiconductor_index | 553.43 |  | 551.1111 | 0.4208 | 575.7 | 565.33 | 0.0705 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMD | ai_accelerator | 529.41 |  | 527.1266 | 0.4332 | 558.62 | 548.745 | 0.1171 | below_opening_15m_low | below_opening_15m_low |
| 20 | CRWV | gpu_cloud_ai_factory | 77.765 |  | 77.3904 | 0.484 | 80.585 | 78.73 | 0.1029 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.4 |  | 395.1274 | 0.069 | 391.33 | 387.05 | 0.0329 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.11 |  | 295.6112 | 0.1687 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 371.635 |  | 368.6182 | 0.8184 | 364.41 | 357.885 | 0.0269 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.835 |  | 254.448 | 0.1521 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.4 |  | 325.4798 | 0.59 | 321.14 | 317.4 | 0.0947 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.52 |  | 21.7221 | 3.6733 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.15 |  | 28.1529 | 3.5419 | 29.055 | 28.28 | 0.2744 | buy_precheck_manual_confirm | none |
| 8 | META | cloud_ai_capex | 675.16 |  | 675.4564 | -0.0439 | 664.875 | 657.17 | 0.0592 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1789.57 |  | 1771.0279 | 1.047 | 1829.9 | 1759.045 | 0.0872 | watch_only | none |
| 10 | IREN | high_beta_ai_infrastructure | 39.715 |  | 39.1017 | 1.5683 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 393.54 |  | 391.7312 | 0.4618 | 397.94 | 392.62 | 1.0672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ORCL | cloud_ai_capex | 132.74 |  | 131.6498 | 0.8281 | 132.925 | 129.92 | 4.7763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 209.59 |  | 209.1563 | 0.2073 | 213.775 | 211.225 | 0.1336 | below_opening_15m_low | below_opening_15m_low |
| 15 | MU | memory_hbm_storage | 911.71 |  | 910.1128 | 0.1755 | 977.7 | 953.67 | 0.3027 | below_opening_15m_low | below_opening_15m_low |
| 16 | CIEN | ai_networking_optical | 419.94 |  | 418.8828 | 0.2524 | 438.14 | 427.54 | 1.7574 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | SOXX | semiconductor_index | 553.43 |  | 551.1111 | 0.4208 | 575.7 | 565.33 | 0.0705 | below_opening_15m_low | below_opening_15m_low |
| 18 | SPY | market_regime | 753.92 |  | 753.1433 | 0.1031 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMAT | semiconductor_equipment | 578.08 |  | 577.7375 | 0.0593 | 610.62 | 586.86 | 5.0235 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | AMD | ai_accelerator | 529.41 |  | 527.1266 | 0.4332 | 558.62 | 548.745 | 0.1171 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.99 |  | 716.1955 | 0.1109 | 724.31 | 721.08 | 0.0126 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.16 |  | 74.1924 | -0.0436 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.59 |  | 209.1563 | 0.2073 | 213.775 | 211.225 | 0.1336 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.4 |  | 395.1274 | 0.069 | 391.33 | 387.05 | 0.0329 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.4 |  | 325.4798 | 0.59 | 321.14 | 317.4 | 0.0947 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.635 |  | 368.6182 | 0.8184 | 364.41 | 357.885 | 0.0269 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.41 |  | 527.1266 | 0.4332 | 558.62 | 548.745 | 0.1171 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 419.505 |  | 418.8588 | 0.1543 | 428.59 | 422.945 | 1.0703 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.43 |  | 551.1111 | 0.4208 | 575.7 | 565.33 | 0.0705 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.34 |  | 587.2292 | 0.0189 | 606.85 | 597.81 | 0.0579 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 393.54 |  | 391.7312 | 0.4618 | 397.94 | 392.62 | 1.0672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 911.71 |  | 910.1128 | 0.1755 | 977.7 | 953.67 | 0.3027 | below_opening_15m_low | below_opening_15m_low |
| MRVL | custom_silicon_networking | 207.73 |  | 208.5199 | -0.3788 | 223.02 | 214.85 | 0.0626 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 403.09 |  | 407.3508 | -1.046 | 457.935 | 442.67 | 2.9596 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.78 |  | 46.9169 | -0.2918 | 50.2 | 48.995 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.93 |  | 26.8667 | 0.2355 | 28.295 | 27.55 | 0.0743 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.92 |  | 753.1433 | 0.1031 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 296.11 |  | 295.6112 | 0.1687 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 132.74 |  | 131.6498 | 0.8281 | 132.925 | 129.92 | 4.7763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.765 |  | 77.3904 | 0.484 | 80.585 | 78.73 | 0.1029 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 300.45 |  | 299.009 | 0.4819 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.39 |  | 408.3855 | 0.4908 | 417.84 | 413.82 | 3.1848 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| PWR | data_center_power_cooling | 649.01 |  | 644.3076 | 0.7298 | 663.475 | 653.94 | 3.4946 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 1047.99 |  | 1031.9949 | 1.5499 | 1073.34 | 1059.27 | 3.0449 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 478.98 |  | 478.7341 | 0.0514 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 141.66 |  | 141.6803 | -0.0143 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.41 |  | 171.913 | -0.8743 | 186.095 | 178.355 | 2.271 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 295 |  | 293.8824 | 0.3803 | 315.74 | 303.34 | 1.7424 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 751.78 |  | 748.2263 | 0.475 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 419.94 |  | 418.8828 | 0.2524 | 438.14 | 427.54 | 1.7574 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 111.62 |  | 112.338 | -0.6392 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 348.46 |  | 344.6366 | 1.1094 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1789.57 |  | 1771.0279 | 1.047 | 1829.9 | 1759.045 | 0.0872 | watch_only | none |
| AMAT | semiconductor_equipment | 578.08 |  | 577.7375 | 0.0593 | 610.62 | 586.86 | 5.0235 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LRCX | semiconductor_equipment | 331.185 |  | 331.4057 | -0.0666 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 223.52 |  | 222.6093 | 0.4091 | 236.49 | 225.11 | 2.8006 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 338.95 |  | 335.4315 | 1.0489 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 303.61 |  | 307.5016 | -1.2655 | 326.25 | 317.3 | 3.9656 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| AMKR | semiconductor_test_packaging | 67.485 |  | 66.8059 | 1.0165 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.205 |  | 54.3324 | -0.2344 | 57.92 | 55.2 | 4.3538 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 138.095 |  | 137.6725 | 0.3069 | 143.15 | 140.4 | 4.6272 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 352.95 |  | 348.4311 | 1.2969 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.08 |  | 516.108 | -0.0054 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.76 |  | 295.0631 | -0.4416 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.15 |  | 28.1529 | 3.5419 | 29.055 | 28.28 | 0.2744 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 39.715 |  | 39.1017 | 1.5683 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.52 |  | 21.7221 | 3.6733 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1612.59 |  | 1565.8989 | 2.9817 | 1726.34 | 1665.91 | 2.9766 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 511.9 |  | 516.7157 | -0.932 | 568.16 | 542.4 | 0.1524 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 816.625 |  | 817.228 | -0.0738 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.835 |  | 254.448 | 0.1521 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.16 |  | 675.4564 | -0.0439 | 664.875 | 657.17 | 0.0592 | below_vwap | below_vwap |
| ARM | ai_accelerator | 273.56 |  | 275.971 | -0.8737 | 286.73 | 280.14 | 3.5824 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 175.07 |  | 175.6018 | -0.3028 | 183.63 | 176.08 | 4.5696 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
