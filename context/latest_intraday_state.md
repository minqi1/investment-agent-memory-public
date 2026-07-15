# Intraday State

- Generated at: `2026-07-16T03:44:18+08:00`
- Market time ET: `2026-07-15T15:44:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 39, 'watch_only': 5, 'below_vwap': 3, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.47 |  | 716.3478 | 0.1567 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 555.84 |  | 551.6229 | 0.7645 | 575.7 | 565.33 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 591.08 |  | 587.3854 | 0.629 | 606.85 | 597.81 | 0.0406 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.1 |  | 753.3322 | 0.1019 | 755.54 | 754.215 | 0.0106 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.84 |  | 369.1212 | 0.4656 | 364.41 | 357.885 | 0.1133 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 679.21 |  | 675.7275 | 0.5154 | 664.875 | 657.17 | 0.0824 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 325.935 |  | 325.8866 | 0.0149 | 321.14 | 317.4 | 0.0399 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.755 |  | 21.9948 | 3.4562 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 325.935 |  | 325.8866 | 0.0149 | 321.14 | 317.4 | 0.0399 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 295.77 |  | 295.6323 | 0.0466 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| 3 | GOOGL | cloud_ai_capex | 370.84 |  | 369.1212 | 0.4656 | 364.41 | 357.885 | 0.1133 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 679.21 |  | 675.7275 | 0.5154 | 664.875 | 657.17 | 0.0824 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 211.78 |  | 209.5146 | 1.0812 | 213.775 | 211.225 | 0.0944 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 394.91 |  | 392.309 | 0.663 | 397.94 | 392.62 | 0.7698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 172.365 |  | 171.8159 | 0.3196 | 186.095 | 178.355 | 0.0986 | below_opening_15m_low | below_opening_15m_low |
| 8 | SPY | market_regime | 754.1 |  | 753.3322 | 0.1019 | 755.54 | 754.215 | 0.0106 | below_opening_15m_low | below_opening_15m_low |
| 9 | CORZ | high_beta_ai_infrastructure | 22.755 |  | 21.9948 | 3.4562 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1803.95 |  | 1774.8001 | 1.6424 | 1829.9 | 1759.045 | 0.1613 | watch_only | none |
| 11 | QQQ | market_regime | 717.47 |  | 716.3478 | 0.1567 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| 12 | VRT | data_center_power_cooling | 305.91 |  | 299.7309 | 2.0616 | 309.345 | 304.67 | 0.3105 | watch_only | none |
| 13 | SKHY | memory_hbm_storage | 176.04 |  | 175.8035 | 0.1345 | 183.63 | 176.08 | 0.0625 | below_opening_15m_low | below_opening_15m_low |
| 14 | APLD | high_beta_ai_infrastructure | 28.99 |  | 28.3559 | 2.2362 | 29.055 | 28.28 | 0.207 | watch_only | none |
| 15 | MU | memory_hbm_storage | 912.745 |  | 909.4182 | 0.3658 | 977.7 | 953.67 | 0.126 | below_opening_15m_low | below_opening_15m_low |
| 16 | SOXX | semiconductor_index | 555.84 |  | 551.6229 | 0.7645 | 575.7 | 565.33 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| 17 | TSM | foundry | 421.61 |  | 419.0384 | 0.6137 | 428.59 | 422.945 | 0.0451 | below_opening_15m_low | below_opening_15m_low |
| 18 | KLAC | semiconductor_equipment | 223.585 |  | 222.6838 | 0.4047 | 236.49 | 225.11 | 0.0716 | below_opening_15m_low | below_opening_15m_low |
| 19 | SMH | semiconductor_index | 591.08 |  | 587.3854 | 0.629 | 606.85 | 597.81 | 0.0406 | below_opening_15m_low | below_opening_15m_low |
| 20 | AMAT | semiconductor_equipment | 579.77 |  | 577.5411 | 0.3859 | 610.62 | 586.86 | 0.1639 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.84 |  | 369.1212 | 0.4656 | 364.41 | 357.885 | 0.1133 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 679.21 |  | 675.7275 | 0.5154 | 664.875 | 657.17 | 0.0824 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 325.935 |  | 325.8866 | 0.0149 | 321.14 | 317.4 | 0.0399 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.755 |  | 21.9948 | 3.4562 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 395.12 |  | 395.3982 | -0.0704 | 391.33 | 387.05 | 0.1822 | below_vwap | below_vwap |
| 6 | AMZN | cloud_ai_capex | 254.08 |  | 254.4752 | -0.1553 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 7 | NVDA | ai_accelerator | 211.78 |  | 209.5146 | 1.0812 | 213.775 | 211.225 | 0.0944 | watch_only | none |
| 8 | ASML | semiconductor_equipment | 1803.95 |  | 1774.8001 | 1.6424 | 1829.9 | 1759.045 | 0.1613 | watch_only | none |
| 9 | ORCL | cloud_ai_capex | 133.23 |  | 132.0069 | 0.9266 | 132.925 | 129.92 | 1.4561 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | VRT | data_center_power_cooling | 305.91 |  | 299.7309 | 2.0616 | 309.345 | 304.67 | 0.3105 | watch_only | none |
| 11 | IWM | market_regime | 295.77 |  | 295.6323 | 0.0466 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| 12 | APLD | high_beta_ai_infrastructure | 28.99 |  | 28.3559 | 2.2362 | 29.055 | 28.28 | 0.207 | watch_only | none |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 394.91 |  | 392.309 | 0.663 | 397.94 | 392.62 | 0.7698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | GEV | data_center_power_cooling | 1062.85 |  | 1037.7825 | 2.4155 | 1073.34 | 1059.27 | 1.4903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 912.745 |  | 909.4182 | 0.3658 | 977.7 | 953.67 | 0.126 | below_opening_15m_low | below_opening_15m_low |
| 17 | CIEN | ai_networking_optical | 422.29 |  | 419.8005 | 0.593 | 438.14 | 427.54 | 4.5798 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SOXX | semiconductor_index | 555.84 |  | 551.6229 | 0.7645 | 575.7 | 565.33 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| 19 | ANET | ai_networking_optical | 172.365 |  | 171.8159 | 0.3196 | 186.095 | 178.355 | 0.0986 | below_opening_15m_low | below_opening_15m_low |
| 20 | STX | memory_hbm_storage | 826.67 |  | 817.7834 | 1.0867 | 889.1 | 850.01 | 0.2492 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.47 |  | 716.3478 | 0.1567 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.26 |  | 74.1836 | 0.103 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 211.78 |  | 209.5146 | 1.0812 | 213.775 | 211.225 | 0.0944 | watch_only | none |
| MSFT | cloud_ai_capex | 395.12 |  | 395.3982 | -0.0704 | 391.33 | 387.05 | 0.1822 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 325.935 |  | 325.8866 | 0.0149 | 321.14 | 317.4 | 0.0399 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.84 |  | 369.1212 | 0.4656 | 364.41 | 357.885 | 0.1133 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 530.19 |  | 527.4787 | 0.514 | 558.62 | 548.745 | 0.2546 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 421.61 |  | 419.0384 | 0.6137 | 428.59 | 422.945 | 0.0451 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 555.84 |  | 551.6229 | 0.7645 | 575.7 | 565.33 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 591.08 |  | 587.3854 | 0.629 | 606.85 | 597.81 | 0.0406 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.91 |  | 392.309 | 0.663 | 397.94 | 392.62 | 0.7698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 912.745 |  | 909.4182 | 0.3658 | 977.7 | 953.67 | 0.126 | below_opening_15m_low | below_opening_15m_low |
| MRVL | custom_silicon_networking | 206.52 |  | 208.004 | -0.7135 | 223.02 | 214.85 | 0.1598 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 413.7 |  | 407.1965 | 1.5971 | 457.935 | 442.67 | 1.9676 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 47.9 |  | 47.0459 | 1.8155 | 50.2 | 48.995 | 0.0209 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.17 |  | 26.8991 | 1.0072 | 28.295 | 27.55 | 0.0368 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.1 |  | 753.3322 | 0.1019 | 755.54 | 754.215 | 0.0106 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.77 |  | 295.6323 | 0.0466 | 296.08 | 294.86 | 0.0034 | watch_only | none |
| ORCL | cloud_ai_capex | 133.23 |  | 132.0069 | 0.9266 | 132.925 | 129.92 | 1.4561 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.54 |  | 77.4735 | 0.0858 | 80.585 | 78.73 | 4.6944 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 305.91 |  | 299.7309 | 2.0616 | 309.345 | 304.67 | 0.3105 | watch_only | none |
| ETN | data_center_power_cooling | 412.39 |  | 408.832 | 0.8703 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 652.09 |  | 646.4615 | 0.8707 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1062.85 |  | 1037.7825 | 2.4155 | 1073.34 | 1059.27 | 1.4903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.73 |  | 478.6082 | -0.1835 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.86 |  | 141.8707 | 0.6973 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 172.365 |  | 171.8159 | 0.3196 | 186.095 | 178.355 | 0.0986 | below_opening_15m_low | below_opening_15m_low |
| COHR | ai_networking_optical | 298.535 |  | 294.1992 | 1.4738 | 315.74 | 303.34 | 0.5192 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 754.34 |  | 749.2293 | 0.6821 | 820.15 | 780.365 | 2.8581 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 422.29 |  | 419.8005 | 0.593 | 438.14 | 427.54 | 4.5798 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 110.89 |  | 111.6331 | -0.6656 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 350.91 |  | 345.1654 | 1.6643 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1803.95 |  | 1774.8001 | 1.6424 | 1829.9 | 1759.045 | 0.1613 | watch_only | none |
| AMAT | semiconductor_equipment | 579.77 |  | 577.5411 | 0.3859 | 610.62 | 586.86 | 0.1639 | below_opening_15m_low | below_opening_15m_low |
| LRCX | semiconductor_equipment | 334.69 |  | 331.4359 | 0.9818 | 355.245 | 340.745 | 4.2308 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 223.585 |  | 222.6838 | 0.4047 | 236.49 | 225.11 | 0.0716 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 342.55 |  | 336.6219 | 1.7611 | 356.29 | 343.785 | 0.4875 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 305.755 |  | 306.9575 | -0.3917 | 326.25 | 317.3 | 3.9836 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.985 |  | 67.0613 | 1.3775 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.62 |  | 54.3723 | 0.4556 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.635 |  | 137.5814 | 0.7658 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| MKSI | semiconductor_materials | 353.83 |  | 349.1391 | 1.3436 | 368.67 | 358.39 | 1.3283 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LIN | industrial_gases | 514.67 |  | 516.0247 | -0.2625 | 521.075 | 518.3 | 4.5175 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.61 |  | 294.3566 | -0.2536 | 297.8 | 295.655 | 4.8432 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 28.99 |  | 28.3559 | 2.2362 | 29.055 | 28.28 | 0.207 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.71 |  | 39.1916 | -1.2289 | 40.01 | 38.815 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.755 |  | 21.9948 | 3.4562 | 22.36 | 21.94 | 0.0439 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1650.46 |  | 1586.8879 | 4.0061 | 1726.34 | 1665.91 | 2.3866 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 516.62 |  | 516.0739 | 0.1058 | 568.16 | 542.4 | 0.4859 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| STX | memory_hbm_storage | 826.67 |  | 817.7834 | 1.0867 | 889.1 | 850.01 | 0.2492 | below_opening_15m_low | below_opening_15m_low |
| AMZN | cloud_ai_capex | 254.08 |  | 254.4752 | -0.1553 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| META | cloud_ai_capex | 679.21 |  | 675.7275 | 0.5154 | 664.875 | 657.17 | 0.0824 | buy_precheck_manual_confirm | none |
| ARM | ai_accelerator | 277.12 |  | 275.5286 | 0.5776 | 286.73 | 280.14 | 0.3067 | below_opening_15m_low | below_opening_15m_low |
| SKHY | memory_hbm_storage | 176.04 |  | 175.8035 | 0.1345 | 183.63 | 176.08 | 0.0625 | below_opening_15m_low | below_opening_15m_low |
