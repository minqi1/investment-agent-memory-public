# Intraday State

- Generated at: `2026-07-16T03:24:28+08:00`
- Market time ET: `2026-07-15T15:24:29-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 44, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 1, 'below_vwap': 3, 'spread_too_wide_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.28 |  | 716.3428 | -0.1484 | 724.31 | 721.08 | 0.007 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.68 |  | 551.4826 | -0.3269 | 575.7 | 565.33 | 0.0528 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.46 |  | 587.3024 | -0.3137 | 606.85 | 597.81 | 0.0529 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.41 |  | 753.3149 | 0.0126 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.81 |  | 395.3803 | 0.1087 | 391.33 | 387.05 | 0.0429 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.645 |  | 369.0138 | 0.442 | 364.41 | 357.885 | 0.0135 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.69 |  | 325.8361 | 0.569 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.535 |  | 21.9632 | 2.6036 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.81 |  | 395.3803 | 0.1087 | 391.33 | 387.05 | 0.0429 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.645 |  | 369.0138 | 0.442 | 364.41 | 357.885 | 0.0135 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.69 |  | 325.8361 | 0.569 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1787.75 |  | 1773.2998 | 0.8149 | 1829.9 | 1759.045 | 0.1292 | watch_only | none |
| 5 | ORCL | cloud_ai_capex | 132.01 |  | 131.9327 | 0.0586 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APLD | high_beta_ai_infrastructure | 28.59 |  | 28.3335 | 0.9054 | 29.055 | 28.28 | 0.07 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 22.535 |  | 21.9632 | 2.6036 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 753.41 |  | 753.3149 | 0.0126 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 9 | SMCI | ai_server_oem | 26.945 |  | 26.8917 | 0.1984 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| 10 | META | cloud_ai_capex | 677.65 |  | 675.6521 | 0.2957 | 664.875 | 657.17 | 0.4766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | LIN | industrial_gases | 516.5 |  | 516.1005 | 0.0774 | 521.075 | 518.3 | 0.1723 | below_opening_15m_low | below_opening_15m_low |
| 12 | NVDA | ai_accelerator | 210.665 |  | 209.4464 | 0.5818 | 213.775 | 211.225 | 0.0285 | below_opening_15m_low | below_opening_15m_low |
| 13 | MKSI | semiconductor_materials | 349.935 |  | 348.8595 | 0.3083 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 14 | COHU | semiconductor_test_packaging | 54.46 |  | 54.3628 | 0.1788 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | IWM | market_regime | 295.43 |  | 295.6377 | -0.0702 | 296.08 | 294.86 | 0.0102 | below_vwap | below_vwap |
| 16 | PWR | data_center_power_cooling | 650.51 |  | 646.1298 | 0.6779 | 663.475 | 653.94 | 0.1814 | below_opening_15m_low | below_opening_15m_low |
| 17 | CIEN | ai_networking_optical | 420.125 |  | 419.7439 | 0.0908 | 438.14 | 427.54 | 4.5986 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | AVGO | custom_silicon_networking | 392.235 |  | 392.1946 | 0.0103 | 397.94 | 392.62 | 0.7292 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 411.81 |  | 408.6911 | 0.7631 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.81 |  | 395.3803 | 0.1087 | 391.33 | 387.05 | 0.0429 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.645 |  | 369.0138 | 0.442 | 364.41 | 357.885 | 0.0135 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.69 |  | 325.8361 | 0.569 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.535 |  | 21.9632 | 2.6036 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 254.425 |  | 254.4926 | -0.0266 | 252.89 | 249.98 | 0.3695 | below_vwap | below_vwap,spread_too_wide |
| 6 | META | cloud_ai_capex | 677.65 |  | 675.6521 | 0.2957 | 664.875 | 657.17 | 0.4766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1787.75 |  | 1773.2998 | 0.8149 | 1829.9 | 1759.045 | 0.1292 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 28.59 |  | 28.3335 | 0.9054 | 29.055 | 28.28 | 0.07 | watch_only | none |
| 9 | IWM | market_regime | 295.43 |  | 295.6377 | -0.0702 | 296.08 | 294.86 | 0.0102 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ORCL | cloud_ai_capex | 132.01 |  | 131.9327 | 0.0586 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | NVDA | ai_accelerator | 210.665 |  | 209.4464 | 0.5818 | 213.775 | 211.225 | 0.0285 | below_opening_15m_low | below_opening_15m_low |
| 13 | CIEN | ai_networking_optical | 420.125 |  | 419.7439 | 0.0908 | 438.14 | 427.54 | 4.5986 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 14 | AVGO | custom_silicon_networking | 392.235 |  | 392.1946 | 0.0103 | 397.94 | 392.62 | 0.7292 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | SPY | market_regime | 753.41 |  | 753.3149 | 0.0126 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 16 | VRT | data_center_power_cooling | 302.25 |  | 299.4893 | 0.9218 | 309.345 | 304.67 | 2.6998 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | SNDK | memory_hbm_storage | 1621.155 |  | 1582.9876 | 2.4111 | 1726.34 | 1665.91 | 3.0244 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | JCI | data_center_power_cooling | 142.655 |  | 141.836 | 0.5774 | 145.99 | 144.625 | 5.0612 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | PWR | data_center_power_cooling | 650.51 |  | 646.1298 | 0.6779 | 663.475 | 653.94 | 0.1814 | below_opening_15m_low | below_opening_15m_low |
| 20 | GEV | data_center_power_cooling | 1054.47 |  | 1036.7398 | 1.7102 | 1073.34 | 1059.27 | 2.2751 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.28 |  | 716.3428 | -0.1484 | 724.31 | 721.08 | 0.007 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.59 |  | 74.1917 | -0.811 | 76.46 | 75.39 | 0.0136 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.665 |  | 209.4464 | 0.5818 | 213.775 | 211.225 | 0.0285 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.81 |  | 395.3803 | 0.1087 | 391.33 | 387.05 | 0.0429 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.69 |  | 325.8361 | 0.569 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.645 |  | 369.0138 | 0.442 | 364.41 | 357.885 | 0.0135 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 524.82 |  | 527.4309 | -0.495 | 558.62 | 548.745 | 0.1715 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 417.55 |  | 418.9872 | -0.343 | 428.59 | 422.945 | 0.0934 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.68 |  | 551.4826 | -0.3269 | 575.7 | 565.33 | 0.0528 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.46 |  | 587.3024 | -0.3137 | 606.85 | 597.81 | 0.0529 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 392.235 |  | 392.1946 | 0.0103 | 397.94 | 392.62 | 0.7292 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MU | memory_hbm_storage | 897.36 |  | 909.6769 | -1.354 | 977.7 | 953.67 | 0.5182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 204.6 |  | 208.169 | -1.7145 | 223.02 | 214.85 | 0.1857 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 407.15 |  | 406.9579 | 0.0472 | 457.935 | 442.67 | 2.9203 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 47.45 |  | 46.971 | 1.0198 | 50.2 | 48.995 | 0.0211 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 26.945 |  | 26.8917 | 0.1984 | 28.295 | 27.55 | 0.0371 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.41 |  | 753.3149 | 0.0126 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.43 |  | 295.6377 | -0.0702 | 296.08 | 294.86 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.01 |  | 131.9327 | 0.0586 | 132.925 | 129.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 76.775 |  | 77.4908 | -0.9238 | 80.585 | 78.73 | 0.0521 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 302.25 |  | 299.4893 | 0.9218 | 309.345 | 304.67 | 2.6998 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ETN | data_center_power_cooling | 411.81 |  | 408.6911 | 0.7631 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 650.51 |  | 646.1298 | 0.6779 | 663.475 | 653.94 | 0.1814 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1054.47 |  | 1036.7398 | 1.7102 | 1073.34 | 1059.27 | 2.2751 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 478.58 |  | 478.6757 | -0.02 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.655 |  | 141.836 | 0.5774 | 145.99 | 144.625 | 5.0612 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ANET | ai_networking_optical | 171.545 |  | 171.7911 | -0.1433 | 186.095 | 178.355 | 0.1049 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHR | ai_networking_optical | 293.875 |  | 294.0738 | -0.0676 | 315.74 | 303.34 | 2.3479 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 745.29 |  | 749.1013 | -0.5088 | 820.15 | 780.365 | 0.1342 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 420.125 |  | 419.7439 | 0.0908 | 438.14 | 427.54 | 4.5986 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 108.675 |  | 111.8803 | -2.865 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 344.27 |  | 344.8724 | -0.1747 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1787.75 |  | 1773.2998 | 0.8149 | 1829.9 | 1759.045 | 0.1292 | watch_only | none |
| AMAT | semiconductor_equipment | 572.56 |  | 577.5467 | -0.8634 | 610.62 | 586.86 | 1.5928 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 329.61 |  | 331.3729 | -0.532 | 355.245 | 340.745 | 1.7293 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 221.44 |  | 222.6171 | -0.5287 | 236.49 | 225.11 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 338.04 |  | 336.285 | 0.5219 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 303.22 |  | 307.1047 | -1.2649 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.88 |  | 67.0286 | -0.2216 | 70.42 | 68.43 | 2.1382 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.46 |  | 54.3628 | 0.1788 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 136.4 |  | 137.6029 | -0.8742 | 143.15 | 140.4 | 0.3079 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 349.935 |  | 348.8595 | 0.3083 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.5 |  | 516.1005 | 0.0774 | 521.075 | 518.3 | 0.1723 | below_opening_15m_low | below_opening_15m_low |
| APD | industrial_gases | 294.28 |  | 294.4132 | -0.0452 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.59 |  | 28.3335 | 0.9054 | 29.055 | 28.28 | 0.07 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.44 |  | 39.2438 | -2.0483 | 40.01 | 38.815 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.535 |  | 21.9632 | 2.6036 | 22.36 | 21.94 | 0.0444 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1621.155 |  | 1582.9876 | 2.4111 | 1726.34 | 1665.91 | 3.0244 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 509.135 |  | 516.2046 | -1.3695 | 568.16 | 542.4 | 0.7307 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 816.505 |  | 817.5417 | -0.1268 | 889.1 | 850.01 | 2.6797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 254.425 |  | 254.4926 | -0.0266 | 252.89 | 249.98 | 0.3695 | below_vwap | below_vwap,spread_too_wide |
| META | cloud_ai_capex | 677.65 |  | 675.6521 | 0.2957 | 664.875 | 657.17 | 0.4766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 272.89 |  | 275.5329 | -0.9592 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 174.01 |  | 175.879 | -1.0627 | 183.63 | 176.08 | 0.1034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
