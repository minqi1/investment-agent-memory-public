# Intraday State

- Generated at: `2026-07-16T03:48:12+08:00`
- Market time ET: `2026-07-15T15:48:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 39, 'spread_too_wide_or_missing': 5, 'below_vwap': 3, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.68 |  | 716.3545 | 0.0454 | 724.31 | 721.08 | 0.0181 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.785 |  | 551.7083 | 0.5577 | 575.7 | 565.33 | 0.0595 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.81 |  | 587.4316 | 0.4049 | 606.85 | 597.81 | 0.0593 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.73 |  | 753.3369 | 0.0522 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.055 |  | 369.1415 | 0.2475 | 364.41 | 357.885 | 0.3054 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.49 |  | 254.4739 | 0.0063 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 679.87 |  | 675.7795 | 0.6053 | 664.875 | 657.17 | 0.2427 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.195 |  | 325.8875 | 0.0944 | 321.14 | 317.4 | 0.0123 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.755 |  | 22.0077 | 3.3958 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.49 |  | 254.4739 | 0.0063 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 326.195 |  | 325.8875 | 0.0944 | 321.14 | 317.4 | 0.0123 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.055 |  | 369.1415 | 0.2475 | 364.41 | 357.885 | 0.3054 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 679.87 |  | 675.7795 | 0.6053 | 664.875 | 657.17 | 0.2427 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1806.86 |  | 1775.1551 | 1.786 | 1829.9 | 1759.045 | 0.0415 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 394.95 |  | 392.3605 | 0.66 | 397.94 | 392.62 | 0.7647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ORCL | cloud_ai_capex | 133.065 |  | 132.044 | 0.7732 | 132.925 | 129.92 | 1.5782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SPY | market_regime | 753.73 |  | 753.3369 | 0.0522 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 9 | WDC | memory_hbm_storage | 516.365 |  | 516.0723 | 0.0567 | 568.16 | 542.4 | 0.1278 | below_opening_15m_low | below_opening_15m_low |
| 10 | CORZ | high_beta_ai_infrastructure | 22.755 |  | 22.0077 | 3.3958 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |
| 11 | QQQ | market_regime | 716.68 |  | 716.3545 | 0.0454 | 724.31 | 721.08 | 0.0181 | below_opening_15m_low | below_opening_15m_low |
| 12 | APLD | high_beta_ai_infrastructure | 28.99 |  | 28.3673 | 2.1953 | 29.055 | 28.28 | 0.069 | watch_only | none |
| 13 | AMAT | semiconductor_equipment | 579.005 |  | 577.5554 | 0.251 | 610.62 | 586.86 | 0.1606 | below_opening_15m_low | below_opening_15m_low |
| 14 | KLAC | semiconductor_equipment | 223.32 |  | 222.7026 | 0.2772 | 236.49 | 225.11 | 0.1791 | below_opening_15m_low | below_opening_15m_low |
| 15 | SOXX | semiconductor_index | 554.785 |  | 551.7083 | 0.5577 | 575.7 | 565.33 | 0.0595 | below_opening_15m_low | below_opening_15m_low |
| 16 | SMH | semiconductor_index | 589.81 |  | 587.4316 | 0.4049 | 606.85 | 597.81 | 0.0593 | below_opening_15m_low | below_opening_15m_low |
| 17 | SMCI | ai_server_oem | 27.05 |  | 26.9014 | 0.5525 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| 18 | NVDA | ai_accelerator | 211.43 |  | 209.5317 | 0.906 | 213.775 | 211.225 | 2.3459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | IWM | market_regime | 295.565 |  | 295.6327 | -0.0229 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 20 | AMD | ai_accelerator | 529.37 |  | 527.4996 | 0.3546 | 558.62 | 548.745 | 0.1549 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.055 |  | 369.1415 | 0.2475 | 364.41 | 357.885 | 0.3054 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.49 |  | 254.4739 | 0.0063 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 679.87 |  | 675.7795 | 0.6053 | 664.875 | 657.17 | 0.2427 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 326.195 |  | 325.8875 | 0.0944 | 321.14 | 317.4 | 0.0123 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.755 |  | 22.0077 | 3.3958 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 395.185 |  | 395.397 | -0.0536 | 391.33 | 387.05 | 0.0557 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1806.86 |  | 1775.1551 | 1.786 | 1829.9 | 1759.045 | 0.0415 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 133.065 |  | 132.044 | 0.7732 | 132.925 | 129.92 | 1.5782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APLD | high_beta_ai_infrastructure | 28.99 |  | 28.3673 | 2.1953 | 29.055 | 28.28 | 0.069 | watch_only | none |
| 10 | IWM | market_regime | 295.565 |  | 295.6327 | -0.0229 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | NVDA | ai_accelerator | 211.43 |  | 209.5317 | 0.906 | 213.775 | 211.225 | 2.3459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | AVGO | custom_silicon_networking | 394.95 |  | 392.3605 | 0.66 | 397.94 | 392.62 | 0.7647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 305.25 |  | 299.7989 | 1.8183 | 309.345 | 304.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | GEV | data_center_power_cooling | 1060.6 |  | 1038.096 | 2.1678 | 1073.34 | 1059.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CIEN | ai_networking_optical | 421.44 |  | 419.8167 | 0.3867 | 438.14 | 427.54 | 5.047 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | SOXX | semiconductor_index | 554.785 |  | 551.7083 | 0.5577 | 575.7 | 565.33 | 0.0595 | below_opening_15m_low | below_opening_15m_low |
| 18 | ANET | ai_networking_optical | 172.175 |  | 171.8272 | 0.2024 | 186.095 | 178.355 | 4.0366 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | STX | memory_hbm_storage | 825.675 |  | 817.8368 | 0.9584 | 889.1 | 850.01 | 0.2095 | below_opening_15m_low | below_opening_15m_low |
| 20 | SPY | market_regime | 753.73 |  | 753.3369 | 0.0522 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.68 |  | 716.3545 | 0.0454 | 724.31 | 721.08 | 0.0181 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.06 |  | 74.1837 | -0.1667 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.43 |  | 209.5317 | 0.906 | 213.775 | 211.225 | 2.3459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 395.185 |  | 395.397 | -0.0536 | 391.33 | 387.05 | 0.0557 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 326.195 |  | 325.8875 | 0.0944 | 321.14 | 317.4 | 0.0123 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.055 |  | 369.1415 | 0.2475 | 364.41 | 357.885 | 0.3054 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.37 |  | 527.4996 | 0.3546 | 558.62 | 548.745 | 0.1549 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 420.99 |  | 419.108 | 0.449 | 428.59 | 422.945 | 0.9501 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.785 |  | 551.7083 | 0.5577 | 575.7 | 565.33 | 0.0595 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.81 |  | 587.4316 | 0.4049 | 606.85 | 597.81 | 0.0593 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.95 |  | 392.3605 | 0.66 | 397.94 | 392.62 | 0.7647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 907.81 |  | 909.4327 | -0.1784 | 977.7 | 953.67 | 0.9264 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 205.685 |  | 207.9693 | -1.0984 | 223.02 | 214.85 | 0.1215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 411.98 |  | 407.3768 | 1.13 | 457.935 | 442.67 | 0.1384 | below_opening_15m_low | below_opening_15m_low |
| HPE | ai_server_oem | 47.86 |  | 47.0598 | 1.7004 | 50.2 | 48.995 | 0.0209 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.05 |  | 26.9014 | 0.5525 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.73 |  | 753.3369 | 0.0522 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.565 |  | 295.6327 | -0.0229 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 133.065 |  | 132.044 | 0.7732 | 132.925 | 129.92 | 1.5782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.4 |  | 77.4737 | -0.0952 | 80.585 | 78.73 | 3.1525 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 305.25 |  | 299.7989 | 1.8183 | 309.345 | 304.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 412.46 |  | 408.8574 | 0.8811 | 417.84 | 413.82 | 4.7253 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| PWR | data_center_power_cooling | 651.43 |  | 646.526 | 0.7585 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1060.6 |  | 1038.096 | 2.1678 | 1073.34 | 1059.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 478.5 |  | 478.5906 | -0.0189 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.86 |  | 141.8884 | 0.6848 | 145.99 | 144.625 | 4.7599 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ANET | ai_networking_optical | 172.175 |  | 171.8272 | 0.2024 | 186.095 | 178.355 | 4.0366 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 298.295 |  | 294.2783 | 1.3649 | 315.74 | 303.34 | 0.6336 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 752.98 |  | 749.3094 | 0.4899 | 820.15 | 780.365 | 0.3347 | below_opening_15m_low | below_opening_15m_low |
| CIEN | ai_networking_optical | 421.44 |  | 419.8167 | 0.3867 | 438.14 | 427.54 | 5.047 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 110.845 |  | 111.6166 | -0.6913 | 123.995 | 117.25 | 0.2616 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ALAB | ai_networking_optical | 349.615 |  | 345.235 | 1.2687 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1806.86 |  | 1775.1551 | 1.786 | 1829.9 | 1759.045 | 0.0415 | watch_only | none |
| AMAT | semiconductor_equipment | 579.005 |  | 577.5554 | 0.251 | 610.62 | 586.86 | 0.1606 | below_opening_15m_low | below_opening_15m_low |
| LRCX | semiconductor_equipment | 334.45 |  | 331.4594 | 0.9022 | 355.245 | 340.745 | 4.2607 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 223.32 |  | 222.7026 | 0.2772 | 236.49 | 225.11 | 0.1791 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 341.51 |  | 336.7127 | 1.4247 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 305.735 |  | 306.9491 | -0.3955 | 326.25 | 317.3 | 0.3794 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.66 |  | 67.0745 | 0.8729 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.62 |  | 54.3723 | 0.4556 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.37 |  | 137.6045 | 0.5563 | 143.15 | 140.4 | 0.1807 | below_opening_15m_low | below_opening_15m_low |
| MKSI | semiconductor_materials | 353 |  | 349.2434 | 1.0756 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 514.58 |  | 515.9996 | -0.2751 | 521.075 | 518.3 | 0.0428 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 293.825 |  | 294.3404 | -0.1751 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.99 |  | 28.3673 | 2.1953 | 29.055 | 28.28 | 0.069 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.64 |  | 39.1791 | -1.3759 | 40.01 | 38.815 | 0.0518 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.755 |  | 22.0077 | 3.3958 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1642.34 |  | 1587.474 | 3.4562 | 1726.34 | 1665.91 | 4.848 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 516.365 |  | 516.0723 | 0.0567 | 568.16 | 542.4 | 0.1278 | below_opening_15m_low | below_opening_15m_low |
| STX | memory_hbm_storage | 825.675 |  | 817.8368 | 0.9584 | 889.1 | 850.01 | 0.2095 | below_opening_15m_low | below_opening_15m_low |
| AMZN | cloud_ai_capex | 254.49 |  | 254.4739 | 0.0063 | 252.89 | 249.98 | 0.0157 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 679.87 |  | 675.7795 | 0.6053 | 664.875 | 657.17 | 0.2427 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 276.67 |  | 275.5446 | 0.4084 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| SKHY | memory_hbm_storage | 174.42 |  | 175.8062 | -0.7885 | 183.63 | 176.08 | 3.6808 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
