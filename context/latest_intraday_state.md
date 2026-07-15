# Intraday State

- Generated at: `2026-07-16T03:20:31+08:00`
- Market time ET: `2026-07-15T15:20:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'spread_too_wide_or_missing': 3, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 1, 'below_vwap': 3, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.69 |  | 716.3503 | -0.0922 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 551.52 |  | 551.4929 | 0.0049 | 575.7 | 565.33 | 0.0834 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 586.965 |  | 587.3128 | -0.0592 | 606.85 | 597.81 | 0.0716 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.67 |  | 753.3147 | 0.0472 | 755.54 | 754.215 | 0.0146 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 676.66 |  | 675.6329 | 0.152 | 664.875 | 657.17 | 0.1877 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 327.765 |  | 325.8177 | 0.5977 | 321.14 | 317.4 | 0.0366 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.961 | 2.6822 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ORCL | cloud_ai_capex | 132.07 |  | 131.9307 | 0.1056 | 132.925 | 129.92 | 0.0303 | watch_only | none |
| 2 | META | cloud_ai_capex | 676.66 |  | 675.6329 | 0.152 | 664.875 | 657.17 | 0.1877 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.765 |  | 325.8177 | 0.5977 | 321.14 | 317.4 | 0.0366 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1792.15 |  | 1773.2147 | 1.0679 | 1829.9 | 1759.045 | 0.111 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 28.61 |  | 28.3299 | 0.9888 | 29.055 | 28.28 | 0.1049 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 392.76 |  | 392.1945 | 0.1442 | 397.94 | 392.62 | 3.2463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.961 | 2.6822 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 395.54 |  | 395.3772 | 0.0412 | 391.33 | 387.05 | 0.4778 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SOXX | semiconductor_index | 551.52 |  | 551.4929 | 0.0049 | 575.7 | 565.33 | 0.0834 | below_opening_15m_low | below_opening_15m_low |
| 10 | SPY | market_regime | 753.67 |  | 753.3147 | 0.0472 | 755.54 | 754.215 | 0.0146 | below_opening_15m_low | below_opening_15m_low |
| 11 | TT | data_center_power_cooling | 479.32 |  | 478.6759 | 0.1346 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 12 | NVDA | ai_accelerator | 210.97 |  | 209.4377 | 0.7316 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 13 | LIN | industrial_gases | 516.55 |  | 516.0994 | 0.0873 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 370.43 |  | 369.002 | 0.387 | 364.41 | 357.885 | 0.4535 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SMCI | ai_server_oem | 27 |  | 26.891 | 0.4052 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| 16 | IWM | market_regime | 295.61 |  | 295.6389 | -0.0098 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 17 | AMZN | cloud_ai_capex | 254.46 |  | 254.4933 | -0.0131 | 252.89 | 249.98 | 0.0393 | below_vwap | below_vwap |
| 18 | ALAB | ai_networking_optical | 347.11 |  | 344.8715 | 0.6491 | 369.23 | 356.615 | 0.265 | below_opening_15m_low | below_opening_15m_low |
| 19 | CIEN | ai_networking_optical | 420.97 |  | 419.7408 | 0.2928 | 438.14 | 427.54 | 4.6773 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 676.66 |  | 675.6329 | 0.152 | 664.875 | 657.17 | 0.1877 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 327.765 |  | 325.8177 | 0.5977 | 321.14 | 317.4 | 0.0366 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.961 | 2.6822 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.46 |  | 254.4933 | -0.0131 | 252.89 | 249.98 | 0.0393 | below_vwap | below_vwap |
| 5 | MSFT | cloud_ai_capex | 395.54 |  | 395.3772 | 0.0412 | 391.33 | 387.05 | 0.4778 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GOOGL | cloud_ai_capex | 370.43 |  | 369.002 | 0.387 | 364.41 | 357.885 | 0.4535 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1792.15 |  | 1773.2147 | 1.0679 | 1829.9 | 1759.045 | 0.111 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.07 |  | 131.9307 | 0.1056 | 132.925 | 129.92 | 0.0303 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.61 |  | 28.3299 | 0.9888 | 29.055 | 28.28 | 0.1049 | watch_only | none |
| 10 | IWM | market_regime | 295.61 |  | 295.6389 | -0.0098 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 392.76 |  | 392.1945 | 0.1442 | 397.94 | 392.62 | 3.2463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | NVDA | ai_accelerator | 210.97 |  | 209.4377 | 0.7316 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 14 | CIEN | ai_networking_optical | 420.97 |  | 419.7408 | 0.2928 | 438.14 | 427.54 | 4.6773 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | SOXX | semiconductor_index | 551.52 |  | 551.4929 | 0.0049 | 575.7 | 565.33 | 0.0834 | below_opening_15m_low | below_opening_15m_low |
| 16 | SPY | market_regime | 753.67 |  | 753.3147 | 0.0472 | 755.54 | 754.215 | 0.0146 | below_opening_15m_low | below_opening_15m_low |
| 17 | TT | data_center_power_cooling | 479.32 |  | 478.6759 | 0.1346 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | VRT | data_center_power_cooling | 303.145 |  | 299.4769 | 1.2248 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1617.41 |  | 1582.684 | 2.1941 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 142.93 |  | 141.8299 | 0.7756 | 145.99 | 144.625 | 4.8835 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.69 |  | 716.3503 | -0.0922 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.74 |  | 74.194 | -0.6119 | 76.46 | 75.39 | 0.0271 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.97 |  | 209.4377 | 0.7316 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.54 |  | 395.3772 | 0.0412 | 391.33 | 387.05 | 0.4778 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 327.765 |  | 325.8177 | 0.5977 | 321.14 | 317.4 | 0.0366 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.43 |  | 369.002 | 0.387 | 364.41 | 357.885 | 0.4535 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 526.83 |  | 527.4452 | -0.1166 | 558.62 | 548.745 | 0.6055 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 418.58 |  | 418.9952 | -0.0991 | 428.59 | 422.945 | 0.1672 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.52 |  | 551.4929 | 0.0049 | 575.7 | 565.33 | 0.0834 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 586.965 |  | 587.3128 | -0.0592 | 606.85 | 597.81 | 0.0716 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 392.76 |  | 392.1945 | 0.1442 | 397.94 | 392.62 | 3.2463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 899.12 |  | 909.7688 | -1.1705 | 977.7 | 953.67 | 0.0367 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 205.505 |  | 208.1971 | -1.2931 | 223.02 | 214.85 | 0.3552 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 406.58 |  | 406.9677 | -0.0953 | 457.935 | 442.67 | 2.9613 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.47 |  | 46.9621 | 1.0815 | 50.2 | 48.995 | 0.0211 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27 |  | 26.891 | 0.4052 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.67 |  | 753.3147 | 0.0472 | 755.54 | 754.215 | 0.0146 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.61 |  | 295.6389 | -0.0098 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.07 |  | 131.9307 | 0.1056 | 132.925 | 129.92 | 0.0303 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 76.99 |  | 77.4953 | -0.6521 | 80.585 | 78.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.145 |  | 299.4769 | 1.2248 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 412.68 |  | 408.6646 | 0.9826 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 652.015 |  | 646.1084 | 0.9142 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1054.515 |  | 1036.6088 | 1.7274 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 479.32 |  | 478.6759 | 0.1346 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 142.93 |  | 141.8299 | 0.7756 | 145.99 | 144.625 | 4.8835 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ANET | ai_networking_optical | 171.14 |  | 171.7984 | -0.3832 | 186.095 | 178.355 | 2.571 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 294.82 |  | 294.0735 | 0.2538 | 315.74 | 303.34 | 3.7786 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 746.805 |  | 749.1296 | -0.3103 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 420.97 |  | 419.7408 | 0.2928 | 438.14 | 427.54 | 4.6773 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 108.855 |  | 111.978 | -2.789 | 123.995 | 117.25 | 0.1654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ALAB | ai_networking_optical | 347.11 |  | 344.8715 | 0.6491 | 369.23 | 356.615 | 0.265 | below_opening_15m_low | below_opening_15m_low |
| ASML | semiconductor_equipment | 1792.15 |  | 1773.2147 | 1.0679 | 1829.9 | 1759.045 | 0.111 | watch_only | none |
| AMAT | semiconductor_equipment | 574.6 |  | 577.5836 | -0.5166 | 610.62 | 586.86 | 0.1044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 330.94 |  | 331.3991 | -0.1385 | 355.245 | 340.745 | 0.281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 221.725 |  | 222.6699 | -0.4244 | 236.49 | 225.11 | 0.0496 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 339.03 |  | 336.2664 | 0.8218 | 356.29 | 343.785 | 4.9258 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 304.28 |  | 307.1368 | -0.9301 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.17 |  | 67.0299 | 0.209 | 70.42 | 68.43 | 2.2927 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.46 |  | 54.3628 | 0.1788 | 57.92 | 55.2 | 3.5439 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 136.855 |  | 137.6404 | -0.5706 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 350.93 |  | 348.8494 | 0.5964 | 368.67 | 358.39 | 1.0144 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LIN | industrial_gases | 516.55 |  | 516.0994 | 0.0873 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 294.275 |  | 294.4154 | -0.0477 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.61 |  | 28.3299 | 0.9888 | 29.055 | 28.28 | 0.1049 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.595 |  | 39.2547 | -1.6804 | 40.01 | 38.815 | 0.0518 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.961 | 2.6822 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1617.41 |  | 1582.684 | 2.1941 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 508.615 |  | 516.2528 | -1.4795 | 568.16 | 542.4 | 2.7526 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 815.895 |  | 817.5571 | -0.2033 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.46 |  | 254.4933 | -0.0131 | 252.89 | 249.98 | 0.0393 | below_vwap | below_vwap |
| META | cloud_ai_capex | 676.66 |  | 675.6329 | 0.152 | 664.875 | 657.17 | 0.1877 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 274.25 |  | 275.5606 | -0.4756 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 173.94 |  | 175.8922 | -1.1099 | 183.63 | 176.08 | 0.092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
