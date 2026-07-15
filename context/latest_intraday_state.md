# Intraday State

- Generated at: `2026-07-16T02:20:48+08:00`
- Market time ET: `2026-07-15T14:20:49-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'spread_too_wide_or_missing': 3, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 1, 'below_vwap': 1, 'watch_only': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.71 |  | 716.312 | 0.1952 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 551.49 |  | 551.4097 | 0.0146 | 575.7 | 565.33 | 0.0653 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.56 |  | 587.2654 | 0.0502 | 606.85 | 597.81 | 0.0664 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.325 |  | 753.2221 | 0.1464 | 755.54 | 754.215 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 372.715 |  | 368.7688 | 1.0701 | 364.41 | 357.885 | 0.212 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.19 |  | 254.4733 | 0.2816 | 252.89 | 249.98 | 0.0588 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.35 |  | 325.5875 | 0.5413 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 133.24 |  | 131.7378 | 1.1403 | 132.925 | 129.92 | 0.0525 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.545 |  | 21.8181 | 3.3316 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.19 |  | 254.4733 | 0.2816 | 252.89 | 249.98 | 0.0588 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.325 |  | 753.2221 | 0.1464 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 3 | IWM | market_regime | 295.74 |  | 295.6392 | 0.0341 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 327.35 |  | 325.5875 | 0.5413 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 394.2 |  | 391.9157 | 0.5829 | 397.94 | 392.62 | 0.2207 | watch_only | none |
| 6 | ORCL | cloud_ai_capex | 133.24 |  | 131.7378 | 1.1403 | 132.925 | 129.92 | 0.0525 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1788.86 |  | 1771.9022 | 0.957 | 1829.9 | 1759.045 | 0.1375 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 372.715 |  | 368.7688 | 1.0701 | 364.41 | 357.885 | 0.212 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.545 |  | 21.8181 | 3.3316 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 551.49 |  | 551.4097 | 0.0146 | 575.7 | 565.33 | 0.0653 | below_opening_15m_low | below_opening_15m_low |
| 11 | SMH | semiconductor_index | 587.56 |  | 587.2654 | 0.0502 | 606.85 | 597.81 | 0.0664 | below_opening_15m_low | below_opening_15m_low |
| 12 | QQQ | market_regime | 717.71 |  | 716.312 | 0.1952 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| 13 | IREN | high_beta_ai_infrastructure | 39.95 |  | 39.1835 | 1.9562 | 40.01 | 38.815 | 0.0501 | watch_only | none |
| 14 | APLD | high_beta_ai_infrastructure | 28.89 |  | 28.2438 | 2.288 | 29.055 | 28.28 | 0.1385 | watch_only | none |
| 15 | SMCI | ai_server_oem | 26.935 |  | 26.8776 | 0.2135 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 16 | META | cloud_ai_capex | 676.86 |  | 675.5078 | 0.2002 | 664.875 | 657.17 | 0.4373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MSFT | cloud_ai_capex | 396.595 |  | 395.1976 | 0.3536 | 391.33 | 387.05 | 0.6657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 819.57 |  | 817.3912 | 0.2666 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | TT | data_center_power_cooling | 478.85 |  | 478.7438 | 0.0222 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | COHR | ai_networking_optical | 294.49 |  | 293.9914 | 0.1696 | 315.74 | 303.34 | 0.2003 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 372.715 |  | 368.7688 | 1.0701 | 364.41 | 357.885 | 0.212 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.19 |  | 254.4733 | 0.2816 | 252.89 | 249.98 | 0.0588 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.35 |  | 325.5875 | 0.5413 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 133.24 |  | 131.7378 | 1.1403 | 132.925 | 129.92 | 0.0525 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.545 |  | 21.8181 | 3.3316 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 396.595 |  | 395.1976 | 0.3536 | 391.33 | 387.05 | 0.6657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AVGO | custom_silicon_networking | 394.2 |  | 391.9157 | 0.5829 | 397.94 | 392.62 | 0.2207 | watch_only | none |
| 8 | META | cloud_ai_capex | 676.86 |  | 675.5078 | 0.2002 | 664.875 | 657.17 | 0.4373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1788.86 |  | 1771.9022 | 0.957 | 1829.9 | 1759.045 | 0.1375 | watch_only | none |
| 10 | SPY | market_regime | 754.325 |  | 753.2221 | 0.1464 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 11 | IWM | market_regime | 295.74 |  | 295.6392 | 0.0341 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 39.95 |  | 39.1835 | 1.9562 | 40.01 | 38.815 | 0.0501 | watch_only | none |
| 13 | APLD | high_beta_ai_infrastructure | 28.89 |  | 28.2438 | 2.288 | 29.055 | 28.28 | 0.1385 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 179.215 |  | 175.7424 | 1.976 | 183.63 | 176.08 | 0.6528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.15 |  | 209.2129 | 0.4479 | 213.775 | 211.225 | 0.3426 | below_opening_15m_low | below_opening_15m_low |
| 17 | CIEN | ai_networking_optical | 423.925 |  | 419.2294 | 1.1201 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SOXX | semiconductor_index | 551.49 |  | 551.4097 | 0.0146 | 575.7 | 565.33 | 0.0653 | below_opening_15m_low | below_opening_15m_low |
| 19 | STX | memory_hbm_storage | 819.57 |  | 817.3912 | 0.2666 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | AMD | ai_accelerator | 530.45 |  | 527.3035 | 0.5967 | 558.62 | 548.745 | 0.4147 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.71 |  | 716.312 | 0.1952 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.42 |  | 74.2008 | 0.2955 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.15 |  | 209.2129 | 0.4479 | 213.775 | 211.225 | 0.3426 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.595 |  | 395.1976 | 0.3536 | 391.33 | 387.05 | 0.6657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 327.35 |  | 325.5875 | 0.5413 | 321.14 | 317.4 | 0.0061 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.715 |  | 368.7688 | 1.0701 | 364.41 | 357.885 | 0.212 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 530.45 |  | 527.3035 | 0.5967 | 558.62 | 548.745 | 0.4147 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 420.58 |  | 418.9422 | 0.3909 | 428.59 | 422.945 | 1.7 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.49 |  | 551.4097 | 0.0146 | 575.7 | 565.33 | 0.0653 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 587.56 |  | 587.2654 | 0.0502 | 606.85 | 597.81 | 0.0664 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.2 |  | 391.9157 | 0.5829 | 397.94 | 392.62 | 0.2207 | watch_only | none |
| MU | memory_hbm_storage | 908.91 |  | 910.182 | -0.1398 | 977.7 | 953.67 | 0.5149 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.82 |  | 208.4558 | -0.7847 | 223.02 | 214.85 | 0.0677 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 402.87 |  | 407.2014 | -1.0637 | 457.935 | 442.67 | 4.7782 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.9 |  | 46.9227 | -0.0484 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.935 |  | 26.8776 | 0.2135 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.325 |  | 753.2221 | 0.1464 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| IWM | market_regime | 295.74 |  | 295.6392 | 0.0341 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 133.24 |  | 131.7378 | 1.1403 | 132.925 | 129.92 | 0.0525 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 77.97 |  | 77.4631 | 0.6544 | 80.585 | 78.73 | 0.1154 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 301.49 |  | 299.1882 | 0.7693 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.28 |  | 408.5353 | 0.4271 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 649.15 |  | 644.9222 | 0.6556 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1051.49 |  | 1033.1384 | 1.7763 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.85 |  | 478.7438 | 0.0222 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 142.3 |  | 141.7293 | 0.4027 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.46 |  | 171.8681 | -0.2375 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 294.49 |  | 293.9914 | 0.1696 | 315.74 | 303.34 | 0.2003 | below_opening_15m_low | below_opening_15m_low |
| LITE | ai_networking_optical | 752.8 |  | 748.8144 | 0.5322 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 423.925 |  | 419.2294 | 1.1201 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 110.51 |  | 112.2977 | -1.5919 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 347.28 |  | 344.6937 | 0.7503 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1788.86 |  | 1771.9022 | 0.957 | 1829.9 | 1759.045 | 0.1375 | watch_only | none |
| AMAT | semiconductor_equipment | 576.86 |  | 577.7372 | -0.1518 | 610.62 | 586.86 | 0.2271 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 331.04 |  | 331.4326 | -0.1185 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.76 |  | 222.6487 | 0.05 | 236.49 | 225.11 | 3.1334 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 339.33 |  | 335.63 | 1.1024 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 306.58 |  | 307.4648 | -0.2878 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.65 |  | 66.8998 | 1.1214 | 70.42 | 68.43 | 3.6216 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.67 |  | 54.354 | 0.5814 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 137.66 |  | 137.6846 | -0.0179 | 143.15 | 140.4 | 3.5377 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 350.14 |  | 348.6657 | 0.4228 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.76 |  | 516.1003 | -0.0659 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.04 |  | 294.5934 | -0.5273 | 297.8 | 295.655 | 4.6205 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.89 |  | 28.2438 | 2.288 | 29.055 | 28.28 | 0.1385 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.95 |  | 39.1835 | 1.9562 | 40.01 | 38.815 | 0.0501 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.545 |  | 21.8181 | 3.3316 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1623.11 |  | 1574.5638 | 3.0832 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 515.64 |  | 516.574 | -0.1808 | 568.16 | 542.4 | 0.6982 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 819.57 |  | 817.3912 | 0.2666 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 255.19 |  | 254.4733 | 0.2816 | 252.89 | 249.98 | 0.0588 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 676.86 |  | 675.5078 | 0.2002 | 664.875 | 657.17 | 0.4373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.87 |  | 275.8392 | -0.7139 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 179.215 |  | 175.7424 | 1.976 | 183.63 | 176.08 | 0.6528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
