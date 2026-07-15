# Intraday State

- Generated at: `2026-07-16T01:56:58+08:00`
- Market time ET: `2026-07-15T13:56:59-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 8, 'price_stale_or_missing': 2, 'below_vwap': 1, 'spread_too_wide_or_missing': 2, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.51 |  | 716.2183 | 0.1803 | 724.31 | 721.08 | 0.0139 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 553.74 |  | 551.1353 | 0.4726 | 575.7 | 565.33 | 0.0795 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.02 |  | 587.2348 | 0.1337 | 606.85 | 597.81 | 0.0697 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.3 |  | 753.1538 | 0.1522 | 755.54 | 754.215 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.675 |  | 395.1321 | 0.1374 | 391.33 | 387.05 | 0.2932 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.26 |  | 295.6205 | 0.2163 | 296.08 | 294.86 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 371.77 |  | 368.6526 | 0.8456 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.77 |  | 254.4516 | 0.1251 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 676.58 |  | 675.4623 | 0.1655 | 664.875 | 657.17 | 0.0798 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.45 |  | 325.4937 | 0.601 | 321.14 | 317.4 | 0.0641 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.51 |  | 21.7387 | 3.5479 | 22.36 | 21.94 | 0.1777 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.13 |  | 28.1628 | 3.4344 | 29.055 | 28.28 | 0.1373 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.26 |  | 295.6205 | 0.2163 | 296.08 | 294.86 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.77 |  | 254.4516 | 0.1251 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 395.675 |  | 395.1321 | 0.1374 | 391.33 | 387.05 | 0.2932 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 754.3 |  | 753.1538 | 0.1522 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 5 | META | cloud_ai_capex | 676.58 |  | 675.4623 | 0.1655 | 664.875 | 657.17 | 0.0798 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.45 |  | 325.4937 | 0.601 | 321.14 | 317.4 | 0.0641 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 371.77 |  | 368.6526 | 0.8456 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1789.39 |  | 1771.1777 | 1.0283 | 1829.9 | 1759.045 | 0.1822 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 29.13 |  | 28.1628 | 3.4344 | 29.055 | 28.28 | 0.1373 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 39.645 |  | 39.1127 | 1.361 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 22.51 |  | 21.7387 | 3.5479 | 22.36 | 21.94 | 0.1777 | buy_precheck_manual_confirm | none |
| 12 | NVDA | ai_accelerator | 209.72 |  | 209.1604 | 0.2676 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| 13 | AVGO | custom_silicon_networking | 394.38 |  | 391.7529 | 0.6706 | 397.94 | 392.62 | 1.0371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | JCI | data_center_power_cooling | 141.99 |  | 141.6826 | 0.217 | 145.99 | 144.625 | 0.1127 | below_opening_15m_low | below_opening_15m_low |
| 15 | SMH | semiconductor_index | 588.02 |  | 587.2348 | 0.1337 | 606.85 | 597.81 | 0.0697 | below_opening_15m_low | below_opening_15m_low |
| 16 | QQQ | market_regime | 717.51 |  | 716.2183 | 0.1803 | 724.31 | 721.08 | 0.0139 | below_opening_15m_low | below_opening_15m_low |
| 17 | SMCI | ai_server_oem | 26.955 |  | 26.8673 | 0.3263 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 18 | ORCL | cloud_ai_capex | 132.46 |  | 131.6626 | 0.6057 | 132.925 | 129.92 | 5.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 818.33 |  | 817.257 | 0.1313 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | TT | data_center_power_cooling | 479 |  | 478.736 | 0.0551 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.675 |  | 395.1321 | 0.1374 | 391.33 | 387.05 | 0.2932 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.26 |  | 295.6205 | 0.2163 | 296.08 | 294.86 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 371.77 |  | 368.6526 | 0.8456 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.77 |  | 254.4516 | 0.1251 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 676.58 |  | 675.4623 | 0.1655 | 664.875 | 657.17 | 0.0798 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.45 |  | 325.4937 | 0.601 | 321.14 | 317.4 | 0.0641 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.51 |  | 21.7387 | 3.5479 | 22.36 | 21.94 | 0.1777 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.13 |  | 28.1628 | 3.4344 | 29.055 | 28.28 | 0.1373 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1789.39 |  | 1771.1777 | 1.0283 | 1829.9 | 1759.045 | 0.1822 | watch_only | none |
| 10 | SPY | market_regime | 754.3 |  | 753.1538 | 0.1522 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| 11 | IREN | high_beta_ai_infrastructure | 39.645 |  | 39.1127 | 1.361 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 394.38 |  | 391.7529 | 0.6706 | 397.94 | 392.62 | 1.0371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 132.46 |  | 131.6626 | 0.6057 | 132.925 | 129.92 | 5.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | NVDA | ai_accelerator | 209.72 |  | 209.1604 | 0.2676 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| 16 | MU | memory_hbm_storage | 913.135 |  | 910.1435 | 0.3287 | 977.7 | 953.67 | 1.5321 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | CIEN | ai_networking_optical | 420.8 |  | 418.8946 | 0.4549 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SOXX | semiconductor_index | 553.74 |  | 551.1353 | 0.4726 | 575.7 | 565.33 | 0.0795 | below_opening_15m_low | below_opening_15m_low |
| 19 | STX | memory_hbm_storage | 818.33 |  | 817.257 | 0.1313 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | AMAT | semiconductor_equipment | 578.27 |  | 577.7406 | 0.0916 | 610.62 | 586.86 | 5.0997 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.51 |  | 716.2183 | 0.1803 | 724.31 | 721.08 | 0.0139 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.33 |  | 74.1934 | 0.1841 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 209.72 |  | 209.1604 | 0.2676 | 213.775 | 211.225 | 0.0095 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.675 |  | 395.1321 | 0.1374 | 391.33 | 387.05 | 0.2932 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.45 |  | 325.4937 | 0.601 | 321.14 | 317.4 | 0.0641 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.77 |  | 368.6526 | 0.8456 | 364.41 | 357.885 | 0.0484 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.91 |  | 527.1468 | 0.5242 | 558.62 | 548.745 | 0.3378 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 420.19 |  | 418.8671 | 0.3158 | 428.59 | 422.945 | 1.1066 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.74 |  | 551.1353 | 0.4726 | 575.7 | 565.33 | 0.0795 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.02 |  | 587.2348 | 0.1337 | 606.85 | 597.81 | 0.0697 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.38 |  | 391.7529 | 0.6706 | 397.94 | 392.62 | 1.0371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 913.135 |  | 910.1435 | 0.3287 | 977.7 | 953.67 | 1.5321 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 208.035 |  | 208.5121 | -0.2288 | 223.02 | 214.85 | 0.9421 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.635 |  | 407.3004 | -0.8999 | 457.935 | 442.67 | 3.248 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.82 |  | 46.9157 | -0.2039 | 50.2 | 48.995 | 0.0427 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.955 |  | 26.8673 | 0.3263 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.3 |  | 753.1538 | 0.1522 | 755.54 | 754.215 | 0.0027 | watch_only | none |
| IWM | market_regime | 296.26 |  | 295.6205 | 0.2163 | 296.08 | 294.86 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 132.46 |  | 131.6626 | 0.6057 | 132.925 | 129.92 | 5.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.69 |  | 77.3934 | 0.3833 | 80.585 | 78.73 | 0.1158 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 301 |  | 299.031 | 0.6585 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.81 |  | 408.4042 | 0.5891 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 649.55 |  | 644.3501 | 0.807 | 663.475 | 653.94 | 3.31 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 1047.93 |  | 1032.1267 | 1.5311 | 1073.34 | 1059.27 | 2.7817 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 479 |  | 478.736 | 0.0551 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 141.99 |  | 141.6826 | 0.217 | 145.99 | 144.625 | 0.1127 | below_opening_15m_low | below_opening_15m_low |
| ANET | ai_networking_optical | 170.69 |  | 171.8966 | -0.7019 | 186.095 | 178.355 | 0.2754 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHR | ai_networking_optical | 294.42 |  | 293.906 | 0.1749 | 315.74 | 303.34 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LITE | ai_networking_optical | 751.73 |  | 748.2612 | 0.4636 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 420.8 |  | 418.8946 | 0.4549 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 111.67 |  | 112.3294 | -0.587 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 349.27 |  | 344.6504 | 1.3404 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1789.39 |  | 1771.1777 | 1.0283 | 1829.9 | 1759.045 | 0.1822 | watch_only | none |
| AMAT | semiconductor_equipment | 578.27 |  | 577.7406 | 0.0916 | 610.62 | 586.86 | 5.0997 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LRCX | semiconductor_equipment | 331.85 |  | 331.407 | 0.1337 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.75 |  | 222.6131 | 0.5107 | 236.49 | 225.11 | 3.0078 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 339.75 |  | 335.4449 | 1.2834 | 356.29 | 343.785 | 4.7859 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 306.97 |  | 307.4967 | -0.1713 | 326.25 | 317.3 | 3.7267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.57 |  | 66.84 | 1.0921 | 70.42 | 68.43 | 0.814 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.205 |  | 54.3324 | -0.2344 | 57.92 | 55.2 | 0.3136 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,stale_or_missing |
| ENTG | semiconductor_materials | 138.11 |  | 137.6748 | 0.3161 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| MKSI | semiconductor_materials | 352.88 |  | 348.512 | 1.2533 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.82 |  | 516.1076 | -0.0557 | 521.075 | 518.3 | 4.7962 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.735 |  | 295.0307 | -0.4392 | 297.8 | 295.655 | 4.8785 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.13 |  | 28.1628 | 3.4344 | 29.055 | 28.28 | 0.1373 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 39.645 |  | 39.1127 | 1.361 | 40.01 | 38.815 | 0.0504 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.51 |  | 21.7387 | 3.5479 | 22.36 | 21.94 | 0.1777 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1610.895 |  | 1567.8425 | 2.746 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 512.37 |  | 516.6849 | -0.8351 | 568.16 | 542.4 | 2.1742 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 818.33 |  | 817.257 | 0.1313 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.77 |  | 254.4516 | 0.1251 | 252.89 | 249.98 | 0.0314 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 676.58 |  | 675.4623 | 0.1655 | 664.875 | 657.17 | 0.0798 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 273.6 |  | 275.9591 | -0.8549 | 286.73 | 280.14 | 3.5819 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 174.735 |  | 175.5959 | -0.4903 | 183.63 | 176.08 | 3.76 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
