# Intraday State

- Generated at: `2026-07-16T04:00:08+08:00`
- Market time ET: `2026-07-15T16:00:09-04:00`
- Session open: `False`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'closed_market_eod_proxy': 54, 'price_stale_or_missing': 1, 'below_vwap': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.66 |  | 716.3906 | 0.1772 | 724.31 | 721.08 | 0.0223 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| SOXX | semiconductor_index | 555.42 |  | 552.1522 | 0.5918 | 575.7 | 565.33 | 0.0576 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| SMH | semiconductor_index | 590.735 |  | 587.835 | 0.4933 | 606.85 | 597.81 | 0.0372 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| SPY | market_regime | 754.55 |  | 753.4445 | 0.1467 | 755.54 | 754.215 | 0.0292 | closed_market_eod_proxy | closed_market_eod_proxy |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.55 |  | 753.4445 | 0.1467 | 755.54 | 754.215 | 0.0292 | closed_market_eod_proxy | closed_market_eod_proxy |
| 2 | IWM | market_regime | 295.755 |  | 295.6262 | 0.0436 | 296.08 | 294.86 | 0.0068 | closed_market_eod_proxy | closed_market_eod_proxy |
| 3 | ORCL | cloud_ai_capex | 132.325 |  | 132.0867 | 0.1804 | 132.925 | 129.92 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| 4 | AMZN | cloud_ai_capex | 254.845 |  | 254.4987 | 0.1361 | 252.89 | 249.98 | 4.2889 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 5 | QQQ | market_regime | 717.66 |  | 716.3906 | 0.1772 | 724.31 | 721.08 | 0.0223 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| 6 | NVDA | ai_accelerator | 212.41 |  | 209.6961 | 1.2942 | 213.775 | 211.225 | 0.0188 | closed_market_eod_proxy | closed_market_eod_proxy |
| 7 | SMCI | ai_server_oem | 26.915 |  | 26.9064 | 0.032 | 28.295 | 27.55 | 0.0372 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| 8 | AVGO | custom_silicon_networking | 394.105 |  | 392.591 | 0.3857 | 397.94 | 392.62 | 3.5752 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 9 | TT | data_center_power_cooling | 480.28 |  | 478.8508 | 0.2985 | 485.9 | 482.93 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 648.13 |  | 646.9782 | 0.178 | 663.475 | 653.94 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 11 | SOXX | semiconductor_index | 555.42 |  | 552.1522 | 0.5918 | 575.7 | 565.33 | 0.0576 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| 12 | SMH | semiconductor_index | 590.735 |  | 587.835 | 0.4933 | 606.85 | 597.81 | 0.0372 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| 13 | HPE | ai_server_oem | 47.365 |  | 47.0926 | 0.5783 | 50.2 | 48.995 | 0.0211 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| 14 | AMAT | semiconductor_equipment | 579.85 |  | 577.6922 | 0.3735 | 610.62 | 586.86 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 15 | AMD | ai_accelerator | 529.52 |  | 527.6841 | 0.3479 | 558.62 | 548.745 | 2.8686 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
| 16 | TSM | foundry | 419.405 |  | 419.2393 | 0.0395 | 428.59 | 422.945 | 3.2665 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
| 17 | JCI | data_center_power_cooling | 142.7 |  | 141.9551 | 0.5247 | 145.99 | 144.625 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 412.555 |  | 409.4755 | 0.7521 | 417.84 | 413.82 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 370.835 |  | 369.2765 | 0.422 | 364.41 | 357.885 | 1.8067 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 20 | ARM | ai_accelerator | 277.52 |  | 275.6986 | 0.6607 | 286.73 | 280.14 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.835 |  | 369.2765 | 0.422 | 364.41 | 357.885 | 1.8067 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 2 | AMZN | cloud_ai_capex | 254.845 |  | 254.4987 | 0.1361 | 252.89 | 249.98 | 4.2889 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 3 | META | cloud_ai_capex | 681.265 |  | 676.0854 | 0.7661 | 664.875 | 657.17 | 1.233 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 4 | AAPL | mega_cap_platform | 327.29 |  | 326.0012 | 0.3953 | 321.14 | 317.4 | 3.367 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 5 | CORZ | high_beta_ai_infrastructure | 22.775 |  | 22.0454 | 3.3096 | 22.36 | 21.94 | 0.0878 | closed_market_eod_proxy | closed_market_eod_proxy |
| 6 | MSFT | cloud_ai_capex | 395.345 |  | 395.3789 | -0.0086 | 391.33 | 387.05 | 0.9561 | closed_market_eod_proxy | below_vwap,closed_market_eod_proxy,spread_too_wide |
| 7 | NVDA | ai_accelerator | 212.41 |  | 209.6961 | 1.2942 | 213.775 | 211.225 | 0.0188 | closed_market_eod_proxy | closed_market_eod_proxy |
| 8 | AVGO | custom_silicon_networking | 394.105 |  | 392.591 | 0.3857 | 397.94 | 392.62 | 3.5752 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1815.35 |  | 1777.6354 | 2.1216 | 1829.9 | 1759.045 | 1.8905 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| 10 | SPY | market_regime | 754.55 |  | 753.4445 | 0.1467 | 755.54 | 754.215 | 0.0292 | closed_market_eod_proxy | closed_market_eod_proxy |
| 11 | VRT | data_center_power_cooling | 304.89 |  | 300.1965 | 1.5635 | 309.345 | 304.67 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| 12 | IWM | market_regime | 295.755 |  | 295.6262 | 0.0436 | 296.08 | 294.86 | 0.0068 | closed_market_eod_proxy | closed_market_eod_proxy |
| 13 | ORCL | cloud_ai_capex | 132.325 |  | 132.0867 | 0.1804 | 132.925 | 129.92 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| 14 | APLD | high_beta_ai_infrastructure | 29.045 |  | 28.4234 | 2.1871 | 29.055 | 28.28 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | SOXX | semiconductor_index | 555.42 |  | 552.1522 | 0.5918 | 575.7 | 565.33 | 0.0576 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| 17 | STX | memory_hbm_storage | 826.985 |  | 818.6304 | 1.0206 | 889.1 | 850.01 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 18 | AMAT | semiconductor_equipment | 579.85 |  | 577.6922 | 0.3735 | 610.62 | 586.86 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| 19 | AMD | ai_accelerator | 529.52 |  | 527.6841 | 0.3479 | 558.62 | 548.745 | 2.8686 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
| 20 | TT | data_center_power_cooling | 480.28 |  | 478.8508 | 0.2985 | 485.9 | 482.93 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 717.66 |  | 716.3906 | 0.1772 | 724.31 | 721.08 | 0.0223 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| TQQQ | leveraged_tool | 74.39 |  | 74.1863 | 0.2745 | 76.46 | 75.39 | 0.0269 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| NVDA | ai_accelerator | 212.41 |  | 209.6961 | 1.2942 | 213.775 | 211.225 | 0.0188 | closed_market_eod_proxy | closed_market_eod_proxy |
| MSFT | cloud_ai_capex | 395.345 |  | 395.3789 | -0.0086 | 391.33 | 387.05 | 0.9561 | closed_market_eod_proxy | below_vwap,closed_market_eod_proxy,spread_too_wide |
| AAPL | mega_cap_platform | 327.29 |  | 326.0012 | 0.3953 | 321.14 | 317.4 | 3.367 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| GOOGL | cloud_ai_capex | 370.835 |  | 369.2765 | 0.422 | 364.41 | 357.885 | 1.8067 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| AMD | ai_accelerator | 529.52 |  | 527.6841 | 0.3479 | 558.62 | 548.745 | 2.8686 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
| TSM | foundry | 419.405 |  | 419.2393 | 0.0395 | 428.59 | 422.945 | 3.2665 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 555.42 |  | 552.1522 | 0.5918 | 575.7 | 565.33 | 0.0576 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| SMH | semiconductor_index | 590.735 |  | 587.835 | 0.4933 | 606.85 | 597.81 | 0.0372 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| AVGO | custom_silicon_networking | 394.105 |  | 392.591 | 0.3857 | 397.94 | 392.62 | 3.5752 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| MU | memory_hbm_storage | 907.23 |  | 909.1935 | -0.216 | 977.7 | 953.67 | 1.4605 | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_too_wide |
| MRVL | custom_silicon_networking | 206.59 |  | 207.8544 | -0.6083 | 223.02 | 214.85 | 2.4687 | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_too_wide |
| DELL | ai_server_oem | 412.8 |  | 408.0567 | 1.1624 | 457.935 | 442.67 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| HPE | ai_server_oem | 47.365 |  | 47.0926 | 0.5783 | 50.2 | 48.995 | 0.0211 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| SMCI | ai_server_oem | 26.915 |  | 26.9064 | 0.032 | 28.295 | 27.55 | 0.0372 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy |
| SPY | market_regime | 754.55 |  | 753.4445 | 0.1467 | 755.54 | 754.215 | 0.0292 | closed_market_eod_proxy | closed_market_eod_proxy |
| IWM | market_regime | 295.755 |  | 295.6262 | 0.0436 | 296.08 | 294.86 | 0.0068 | closed_market_eod_proxy | closed_market_eod_proxy |
| ORCL | cloud_ai_capex | 132.325 |  | 132.0867 | 0.1804 | 132.925 | 129.92 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 77.095 |  | 77.4523 | -0.4613 | 80.585 | 78.73 | 3.0352 | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_too_wide |
| VRT | data_center_power_cooling | 304.89 |  | 300.1965 | 1.5635 | 309.345 | 304.67 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| ETN | data_center_power_cooling | 412.555 |  | 409.4755 | 0.7521 | 417.84 | 413.82 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| PWR | data_center_power_cooling | 648.13 |  | 646.9782 | 0.178 | 663.475 | 653.94 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| GEV | data_center_power_cooling | 1052.86 |  | 1039.4128 | 1.2937 | 1073.34 | 1059.27 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| TT | data_center_power_cooling | 480.28 |  | 478.8508 | 0.2985 | 485.9 | 482.93 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| JCI | data_center_power_cooling | 142.7 |  | 141.9551 | 0.5247 | 145.99 | 144.625 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| ANET | ai_networking_optical | 171.73 |  | 171.8445 | -0.0666 | 186.095 | 178.355 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| COHR | ai_networking_optical | 299.075 |  | 294.9672 | 1.3926 | 315.74 | 303.34 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| LITE | ai_networking_optical | 752.56 |  | 749.7421 | 0.3758 | 820.15 | 780.365 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| CIEN | ai_networking_optical | 418.24 |  | 419.8788 | -0.3903 | 438.14 | 427.54 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| AAOI | ai_networking_optical | 109.08 |  | 111.5019 | -2.1721 | 123.995 | 117.25 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| ALAB | ai_networking_optical | 350.77 |  | 345.7976 | 1.438 | 369.23 | 356.615 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| ASML | semiconductor_equipment | 1815.35 |  | 1777.6354 | 2.1216 | 1829.9 | 1759.045 | 1.8905 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| AMAT | semiconductor_equipment | 579.85 |  | 577.6922 | 0.3735 | 610.62 | 586.86 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| LRCX | semiconductor_equipment | 335.39 |  | 331.6991 | 1.1127 | 355.245 | 340.745 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| KLAC | semiconductor_equipment | 224.735 |  | 222.878 | 0.8332 | 236.49 | 225.11 | 4.205 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
| TER | semiconductor_test_packaging | 342.22 |  | 337.1603 | 1.5007 | 356.29 | 343.785 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| ONTO | semiconductor_test_packaging | 304.62 |  | 306.6815 | -0.6722 | 326.25 | 317.3 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.54 |  | 67.1192 | 0.6269 | 70.42 | 68.43 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.01 |  | 54.4263 | 1.0725 | 57.92 | 55.2 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| ENTG | semiconductor_materials | 139.115 |  | 137.8771 | 0.8978 | 143.15 | 140.4 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| MKSI | semiconductor_materials | 353.72 |  | 349.8841 | 1.0963 | 368.67 | 358.39 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| LIN | industrial_gases | 513.955 |  | 515.7594 | -0.3499 | 521.075 | 518.3 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| APD | industrial_gases | 293.66 |  | 294.2341 | -0.1951 | 297.8 | 295.655 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.045 |  | 28.4234 | 2.1871 | 29.055 | 28.28 |  | closed_market_eod_proxy | closed_market_eod_proxy,spread_unavailable |
| IREN | high_beta_ai_infrastructure | 38.28 |  | 39.1462 | -2.2128 | 40.01 | 38.815 | 0.0784 | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy |
| CORZ | high_beta_ai_infrastructure | 22.775 |  | 22.0454 | 3.3096 | 22.36 | 21.94 | 0.0878 | closed_market_eod_proxy | closed_market_eod_proxy |
| SNDK | memory_hbm_storage | 1611.5 |  | 1588.8035 | 1.4285 | 1726.34 | 1665.91 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| WDC | memory_hbm_storage | 513.955 |  | 515.9884 | -0.3941 | 568.16 | 542.4 |  | closed_market_eod_proxy | below_opening_15m_low,below_vwap,closed_market_eod_proxy,spread_unavailable |
| STX | memory_hbm_storage | 826.985 |  | 818.6304 | 1.0206 | 889.1 | 850.01 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| AMZN | cloud_ai_capex | 254.845 |  | 254.4987 | 0.1361 | 252.89 | 249.98 | 4.2889 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| META | cloud_ai_capex | 681.265 |  | 676.0854 | 0.7661 | 664.875 | 657.17 | 1.233 | closed_market_eod_proxy | closed_market_eod_proxy,spread_too_wide |
| ARM | ai_accelerator | 277.52 |  | 275.6986 | 0.6607 | 286.73 | 280.14 |  | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_unavailable |
| SKHY | memory_hbm_storage | 175.835 |  | 175.803 | 0.0182 | 183.63 | 176.08 | 2.2294 | closed_market_eod_proxy | below_opening_15m_low,closed_market_eod_proxy,spread_too_wide |
