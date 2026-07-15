# Intraday State

- Generated at: `2026-07-16T02:04:53+08:00`
- Market time ET: `2026-07-15T14:04:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 6, 'price_stale_or_missing': 1, 'below_vwap': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.8 |  | 716.2405 | 0.2177 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.69 |  | 551.191 | 0.6348 | 575.7 | 565.33 | 0.0379 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.08 |  | 587.2383 | 0.3136 | 606.85 | 597.81 | 0.0645 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.49 |  | 753.1712 | 0.1751 | 755.54 | 754.215 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.33 |  | 395.1454 | 0.0467 | 391.33 | 387.05 | 0.0911 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.35 |  | 295.6257 | 0.245 | 296.08 | 294.86 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 372.05 |  | 368.683 | 0.9133 | 364.41 | 357.885 | 0.344 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.6 |  | 254.4575 | 0.056 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.35 |  | 325.5292 | 0.5593 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.7664 | 3.5083 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.35 |  | 295.6257 | 0.245 | 296.08 | 294.86 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.6 |  | 254.4575 | 0.056 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 395.33 |  | 395.1454 | 0.0467 | 391.33 | 387.05 | 0.0911 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 754.49 |  | 753.1712 | 0.1751 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 327.35 |  | 325.5292 | 0.5593 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1793.5 |  | 1771.3655 | 1.2496 | 1829.9 | 1759.045 | 0.0647 | watch_only | none |
| 7 | ORCL | cloud_ai_capex | 132.79 |  | 131.6818 | 0.8416 | 132.925 | 129.92 | 0.0377 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.7664 | 3.5083 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 372.05 |  | 368.683 | 0.9133 | 364.41 | 357.885 | 0.344 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 394.44 |  | 391.7908 | 0.6762 | 397.94 | 392.62 | 2.7888 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | MU | memory_hbm_storage | 911.76 |  | 910.1508 | 0.1768 | 977.7 | 953.67 | 0.1075 | below_opening_15m_low | below_opening_15m_low |
| 12 | SMH | semiconductor_index | 589.08 |  | 587.2383 | 0.3136 | 606.85 | 597.81 | 0.0645 | below_opening_15m_low | below_opening_15m_low |
| 13 | QQQ | market_regime | 717.8 |  | 716.2405 | 0.2177 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| 14 | IREN | high_beta_ai_infrastructure | 39.87 |  | 39.1321 | 1.8857 | 40.01 | 38.815 | 0.0502 | watch_only | none |
| 15 | META | cloud_ai_capex | 675.71 |  | 675.4749 | 0.0348 | 664.875 | 657.17 | 1.5569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | HPE | ai_server_oem | 47.07 |  | 46.9163 | 0.3277 | 50.2 | 48.995 | 0.0425 | below_opening_15m_low | below_opening_15m_low |
| 17 | AMAT | semiconductor_equipment | 578.035 |  | 577.7399 | 0.0511 | 610.62 | 586.86 | 0.3408 | below_opening_15m_low | below_opening_15m_low |
| 18 | JCI | data_center_power_cooling | 141.945 |  | 141.6977 | 0.1745 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | NVDA | ai_accelerator | 210.41 |  | 209.1745 | 0.5907 | 213.775 | 211.225 | 0.0285 | below_opening_15m_low | below_opening_15m_low |
| 20 | LRCX | semiconductor_equipment | 332.2 |  | 331.4097 | 0.2385 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.33 |  | 395.1454 | 0.0467 | 391.33 | 387.05 | 0.0911 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.35 |  | 295.6257 | 0.245 | 296.08 | 294.86 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 372.05 |  | 368.683 | 0.9133 | 364.41 | 357.885 | 0.344 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.6 |  | 254.4575 | 0.056 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.35 |  | 325.5292 | 0.5593 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.7664 | 3.5083 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 7 | META | cloud_ai_capex | 675.71 |  | 675.4749 | 0.0348 | 664.875 | 657.17 | 1.5569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1793.5 |  | 1771.3655 | 1.2496 | 1829.9 | 1759.045 | 0.0647 | watch_only | none |
| 9 | SPY | market_regime | 754.49 |  | 753.1712 | 0.1751 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.1 |  | 28.2021 | 3.1837 | 29.055 | 28.28 | 4.5704 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ORCL | cloud_ai_capex | 132.79 |  | 131.6818 | 0.8416 | 132.925 | 129.92 | 0.0377 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 39.87 |  | 39.1321 | 1.8857 | 40.01 | 38.815 | 0.0502 | watch_only | none |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 394.44 |  | 391.7908 | 0.6762 | 397.94 | 392.62 | 2.7888 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SKHY | memory_hbm_storage | 177.63 |  | 175.6017 | 1.155 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | NVDA | ai_accelerator | 210.41 |  | 209.1745 | 0.5907 | 213.775 | 211.225 | 0.0285 | below_opening_15m_low | below_opening_15m_low |
| 17 | MU | memory_hbm_storage | 911.76 |  | 910.1508 | 0.1768 | 977.7 | 953.67 | 0.1075 | below_opening_15m_low | below_opening_15m_low |
| 18 | CIEN | ai_networking_optical | 422.99 |  | 418.9511 | 0.9641 | 438.14 | 427.54 | 4.5959 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | SOXX | semiconductor_index | 554.69 |  | 551.191 | 0.6348 | 575.7 | 565.33 | 0.0379 | below_opening_15m_low | below_opening_15m_low |
| 20 | ANET | ai_networking_optical | 171.99 |  | 171.8753 | 0.0667 | 186.095 | 178.355 | 2.3199 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.8 |  | 716.2405 | 0.2177 | 724.31 | 721.08 | 0.0056 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.425 |  | 74.1945 | 0.3106 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.41 |  | 209.1745 | 0.5907 | 213.775 | 211.225 | 0.0285 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.33 |  | 395.1454 | 0.0467 | 391.33 | 387.05 | 0.0911 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.35 |  | 325.5292 | 0.5593 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.05 |  | 368.683 | 0.9133 | 364.41 | 357.885 | 0.344 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 531.36 |  | 527.1938 | 0.7903 | 558.62 | 548.745 | 0.3049 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 421.145 |  | 418.8878 | 0.5389 | 428.59 | 422.945 | 0.9498 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.69 |  | 551.191 | 0.6348 | 575.7 | 565.33 | 0.0379 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.08 |  | 587.2383 | 0.3136 | 606.85 | 597.81 | 0.0645 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.44 |  | 391.7908 | 0.6762 | 397.94 | 392.62 | 2.7888 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 911.76 |  | 910.1508 | 0.1768 | 977.7 | 953.67 | 0.1075 | below_opening_15m_low | below_opening_15m_low |
| MRVL | custom_silicon_networking | 208.2 |  | 208.494 | -0.141 | 223.02 | 214.85 | 0.6292 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 406.13 |  | 407.2486 | -0.2747 | 457.935 | 442.67 | 2.6543 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.07 |  | 46.9163 | 0.3277 | 50.2 | 48.995 | 0.0425 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.135 |  | 26.8713 | 0.9813 | 28.295 | 27.55 | 0.0737 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.49 |  | 753.1712 | 0.1751 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| IWM | market_regime | 296.35 |  | 295.6257 | 0.245 | 296.08 | 294.86 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 132.79 |  | 131.6818 | 0.8416 | 132.925 | 129.92 | 0.0377 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 78.1 |  | 77.4037 | 0.8995 | 80.585 | 78.73 | 0.0768 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 301.42 |  | 299.0715 | 0.7853 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.28 |  | 408.4582 | 0.6909 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 652.08 |  | 644.6495 | 1.1526 | 663.475 | 653.94 | 5.1098 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 1051.455 |  | 1032.5192 | 1.8339 | 1073.34 | 1059.27 | 2.6687 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 478.775 |  | 478.7408 | 0.0071 | 485.9 | 482.93 | 0.4762 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| JCI | data_center_power_cooling | 141.945 |  | 141.6977 | 0.1745 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.99 |  | 171.8753 | 0.0667 | 186.095 | 178.355 | 2.3199 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 295.985 |  | 293.9283 | 0.6997 | 315.74 | 303.34 | 0.794 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 757.22 |  | 748.3793 | 1.1813 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 422.99 |  | 418.9511 | 0.9641 | 438.14 | 427.54 | 4.5959 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 112.23 |  | 112.3154 | -0.076 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 349.86 |  | 344.6617 | 1.5082 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1793.5 |  | 1771.3655 | 1.2496 | 1829.9 | 1759.045 | 0.0647 | watch_only | none |
| AMAT | semiconductor_equipment | 578.035 |  | 577.7399 | 0.0511 | 610.62 | 586.86 | 0.3408 | below_opening_15m_low | below_opening_15m_low |
| LRCX | semiconductor_equipment | 332.2 |  | 331.4097 | 0.2385 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.69 |  | 222.6262 | 0.4778 | 236.49 | 225.11 | 4.4705 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 340.54 |  | 335.4861 | 1.5064 | 356.29 | 343.785 | 4.3607 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 305.79 |  | 307.4874 | -0.552 | 326.25 | 317.3 | 4.2317 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.75 |  | 66.8635 | 1.3259 | 70.42 | 68.43 | 3.6162 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.66 |  | 54.3388 | 0.5911 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 137.86 |  | 137.6799 | 0.1308 | 143.15 | 140.4 | 0.5803 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 351.88 |  | 348.5277 | 0.9618 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.51 |  | 516.1055 | -0.1154 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.55 |  | 294.9395 | -0.4711 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.1 |  | 28.2021 | 3.1837 | 29.055 | 28.28 | 4.5704 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 39.87 |  | 39.1321 | 1.8857 | 40.01 | 38.815 | 0.0502 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.7664 | 3.5083 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1627.23 |  | 1572.2973 | 3.4938 | 1726.34 | 1665.91 | 3.584 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 514.33 |  | 516.6244 | -0.4441 | 568.16 | 542.4 | 1.604 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 819.225 |  | 817.2832 | 0.2376 | 889.1 | 850.01 | 2.7099 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMZN | cloud_ai_capex | 254.6 |  | 254.4575 | 0.056 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.71 |  | 675.4749 | 0.0348 | 664.875 | 657.17 | 1.5569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 274.3 |  | 275.928 | -0.59 | 286.73 | 280.14 | 3.5727 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 177.63 |  | 175.6017 | 1.155 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
