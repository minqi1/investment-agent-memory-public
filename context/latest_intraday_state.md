# Intraday State

- Generated at: `2026-07-16T03:32:26+08:00`
- Market time ET: `2026-07-15T15:32:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'watch_only': 4, 'below_vwap': 3, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.66 |  | 716.3397 | 0.0447 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.55 |  | 551.5449 | 0.5449 | 575.7 | 565.33 | 0.0793 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.7 |  | 587.2888 | 0.4106 | 606.85 | 597.81 | 0.078 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.86 |  | 753.3197 | 0.0717 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.01 |  | 369.0524 | 0.2595 | 364.41 | 357.885 | 0.0622 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 676.08 |  | 675.6673 | 0.0611 | 664.875 | 657.17 | 0.0592 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.64 |  | 325.8596 | 0.2395 | 321.14 | 317.4 | 0.0367 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.705 |  | 21.9753 | 3.3205 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 295.83 |  | 295.6377 | 0.065 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 370.01 |  | 369.0524 | 0.2595 | 364.41 | 357.885 | 0.0622 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 676.08 |  | 675.6673 | 0.0611 | 664.875 | 657.17 | 0.0592 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.64 |  | 325.8596 | 0.2395 | 321.14 | 317.4 | 0.0367 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 132.585 |  | 131.9409 | 0.4882 | 132.925 | 129.92 | 0.083 | watch_only | none |
| 6 | NVDA | ai_accelerator | 211.26 |  | 209.4652 | 0.8569 | 213.775 | 211.225 | 0.0142 | watch_only | none |
| 7 | AVGO | custom_silicon_networking | 394.95 |  | 392.2269 | 0.6943 | 397.94 | 392.62 | 2.3699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SPY | market_regime | 753.86 |  | 753.3197 | 0.0717 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |
| 9 | TSM | foundry | 420.125 |  | 418.9843 | 0.2722 | 428.59 | 422.945 | 0.0904 | below_opening_15m_low | below_opening_15m_low |
| 10 | CORZ | high_beta_ai_infrastructure | 22.705 |  | 21.9753 | 3.3205 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 11 | QQQ | market_regime | 716.66 |  | 716.3397 | 0.0447 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low |
| 12 | APLD | high_beta_ai_infrastructure | 28.98 |  | 28.3428 | 2.2483 | 29.055 | 28.28 | 0.069 | watch_only | none |
| 13 | SOXX | semiconductor_index | 554.55 |  | 551.5449 | 0.5449 | 575.7 | 565.33 | 0.0793 | below_opening_15m_low | below_opening_15m_low |
| 14 | SMH | semiconductor_index | 589.7 |  | 587.2888 | 0.4106 | 606.85 | 597.81 | 0.078 | below_opening_15m_low | below_opening_15m_low |
| 15 | KLAC | semiconductor_equipment | 223.845 |  | 222.6356 | 0.5432 | 236.49 | 225.11 | 0.1519 | below_opening_15m_low | below_opening_15m_low |
| 16 | AMZN | cloud_ai_capex | 253.98 |  | 254.4891 | -0.2 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 17 | CIEN | ai_networking_optical | 421.33 |  | 419.7577 | 0.3746 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | STX | memory_hbm_storage | 823.935 |  | 817.6129 | 0.7732 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | AMAT | semiconductor_equipment | 578.88 |  | 577.5275 | 0.2342 | 610.62 | 586.86 | 0.5442 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.01 |  | 369.0524 | 0.2595 | 364.41 | 357.885 | 0.0622 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 676.08 |  | 675.6673 | 0.0611 | 664.875 | 657.17 | 0.0592 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.64 |  | 325.8596 | 0.2395 | 321.14 | 317.4 | 0.0367 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.705 |  | 21.9753 | 3.3205 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 395.37 |  | 395.3854 | -0.0039 | 391.33 | 387.05 | 0.0632 | below_vwap | below_vwap |
| 6 | AMZN | cloud_ai_capex | 253.98 |  | 254.4891 | -0.2 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 7 | NVDA | ai_accelerator | 211.26 |  | 209.4652 | 0.8569 | 213.775 | 211.225 | 0.0142 | watch_only | none |
| 8 | IWM | market_regime | 295.83 |  | 295.6377 | 0.065 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 9 | ORCL | cloud_ai_capex | 132.585 |  | 131.9409 | 0.4882 | 132.925 | 129.92 | 0.083 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 28.98 |  | 28.3428 | 2.2483 | 29.055 | 28.28 | 0.069 | watch_only | none |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 394.95 |  | 392.2269 | 0.6943 | 397.94 | 392.62 | 2.3699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ASML | semiconductor_equipment | 1800.92 |  | 1773.7623 | 1.5311 | 1829.9 | 1759.045 | 2.677 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | CIEN | ai_networking_optical | 421.33 |  | 419.7577 | 0.3746 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | SOXX | semiconductor_index | 554.55 |  | 551.5449 | 0.5449 | 575.7 | 565.33 | 0.0793 | below_opening_15m_low | below_opening_15m_low |
| 16 | ANET | ai_networking_optical | 172.6 |  | 171.7998 | 0.4658 | 186.095 | 178.355 | 3.9745 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | STX | memory_hbm_storage | 823.935 |  | 817.6129 | 0.7732 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SPY | market_regime | 753.86 |  | 753.3197 | 0.0717 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMAT | semiconductor_equipment | 578.88 |  | 577.5275 | 0.2342 | 610.62 | 586.86 | 0.5442 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | AMD | ai_accelerator | 530.13 |  | 527.4434 | 0.5094 | 558.62 | 548.745 | 1.4015 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.66 |  | 716.3397 | 0.0447 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.09 |  | 74.1874 | -0.1313 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.26 |  | 209.4652 | 0.8569 | 213.775 | 211.225 | 0.0142 | watch_only | none |
| MSFT | cloud_ai_capex | 395.37 |  | 395.3854 | -0.0039 | 391.33 | 387.05 | 0.0632 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 326.64 |  | 325.8596 | 0.2395 | 321.14 | 317.4 | 0.0367 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.01 |  | 369.0524 | 0.2595 | 364.41 | 357.885 | 0.0622 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 530.13 |  | 527.4434 | 0.5094 | 558.62 | 548.745 | 1.4015 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 420.125 |  | 418.9843 | 0.2722 | 428.59 | 422.945 | 0.0904 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.55 |  | 551.5449 | 0.5449 | 575.7 | 565.33 | 0.0793 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.7 |  | 587.2888 | 0.4106 | 606.85 | 597.81 | 0.078 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.95 |  | 392.2269 | 0.6943 | 397.94 | 392.62 | 2.3699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 906.675 |  | 909.4846 | -0.3089 | 977.7 | 953.67 | 0.7147 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.79 |  | 208.1242 | -0.641 | 223.02 | 214.85 | 1.238 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 411.33 |  | 406.9912 | 1.0661 | 457.935 | 442.67 | 0.2431 | below_opening_15m_low | below_opening_15m_low |
| HPE | ai_server_oem | 47.745 |  | 46.9927 | 1.6008 | 50.2 | 48.995 | 0.0209 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.12 |  | 26.8936 | 0.8418 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.86 |  | 753.3197 | 0.0717 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.83 |  | 295.6377 | 0.065 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 132.585 |  | 131.9409 | 0.4882 | 132.925 | 129.92 | 0.083 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.29 |  | 77.4799 | -0.2451 | 80.585 | 78.73 | 0.1164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 304.33 |  | 299.5477 | 1.5965 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 412.18 |  | 408.752 | 0.8386 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.12 |  | 646.2512 | 0.7534 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1058.24 |  | 1037.0971 | 2.0387 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.475 |  | 478.6713 | -0.041 | 485.9 | 482.93 | 0.1526 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.79 |  | 141.849 | 0.6634 | 145.99 | 144.625 | 4.9583 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ANET | ai_networking_optical | 172.6 |  | 171.7998 | 0.4658 | 186.095 | 178.355 | 3.9745 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 296.66 |  | 294.0878 | 0.8746 | 315.74 | 303.34 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LITE | ai_networking_optical | 753.02 |  | 749.0863 | 0.5251 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 421.33 |  | 419.7577 | 0.3746 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 109.64 |  | 111.7676 | -1.9036 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 350.97 |  | 344.9553 | 1.7436 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1800.92 |  | 1773.7623 | 1.5311 | 1829.9 | 1759.045 | 2.677 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 578.88 |  | 577.5275 | 0.2342 | 610.62 | 586.86 | 0.5442 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LRCX | semiconductor_equipment | 333.51 |  | 331.3876 | 0.6405 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.845 |  | 222.6356 | 0.5432 | 236.49 | 225.11 | 0.1519 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 341.035 |  | 336.4061 | 1.376 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 306.525 |  | 307.0707 | -0.1777 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.53 |  | 67.04 | 0.7308 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.57 |  | 54.3644 | 0.3782 | 57.92 | 55.2 | 0.2566 | below_opening_15m_low | below_opening_15m_low |
| ENTG | semiconductor_materials | 137.91 |  | 137.5667 | 0.2495 | 143.15 | 140.4 | 3.8866 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 352.88 |  | 348.9777 | 1.1182 | 368.67 | 358.39 | 0.6886 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LIN | industrial_gases | 515.83 |  | 516.0981 | -0.0519 | 521.075 | 518.3 | 4.7516 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.995 |  | 294.4025 | -0.1384 | 297.8 | 295.655 | 0.1531 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 28.98 |  | 28.3428 | 2.2483 | 29.055 | 28.28 | 0.069 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.78 |  | 39.2326 | -1.1535 | 40.01 | 38.815 | 0.0516 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.705 |  | 21.9753 | 3.3205 | 22.36 | 21.94 | 0.044 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1651.65 |  | 1584.6435 | 4.2285 | 1726.34 | 1665.91 | 1.5251 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 513.01 |  | 516.1378 | -0.606 | 568.16 | 542.4 | 0.2612 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 823.935 |  | 817.6129 | 0.7732 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 253.98 |  | 254.4891 | -0.2 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| META | cloud_ai_capex | 676.08 |  | 675.6673 | 0.0611 | 664.875 | 657.17 | 0.0592 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 276.28 |  | 275.5082 | 0.2802 | 286.73 | 280.14 | 4.7054 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| SKHY | memory_hbm_storage | 174.56 |  | 175.8559 | -0.7369 | 183.63 | 176.08 | 3.2596 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
