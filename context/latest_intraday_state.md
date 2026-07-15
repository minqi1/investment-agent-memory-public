# Intraday State

- Generated at: `2026-07-16T03:36:23+08:00`
- Market time ET: `2026-07-15T15:36:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 1, 'below_vwap': 3, 'spread_too_wide_or_missing': 3, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.11 |  | 716.3379 | -0.0318 | 724.31 | 721.08 | 0.0196 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 552.8 |  | 551.5629 | 0.2243 | 575.7 | 565.33 | 0.0796 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588 |  | 587.3055 | 0.1183 | 606.85 | 597.81 | 0.0629 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.55 |  | 753.3223 | 0.0302 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.75 |  | 395.3862 | 0.092 | 391.33 | 387.05 | 0.048 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.7 |  | 369.075 | 0.4403 | 364.41 | 357.885 | 0.0432 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.28 |  | 325.8705 | 0.1257 | 321.14 | 317.4 | 0.0245 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.64 |  | 21.9822 | 2.9923 | 22.36 | 21.94 | 0.0883 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.75 |  | 395.3862 | 0.092 | 391.33 | 387.05 | 0.048 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 326.28 |  | 325.8705 | 0.1257 | 321.14 | 317.4 | 0.0245 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.7 |  | 369.075 | 0.4403 | 364.41 | 357.885 | 0.0432 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1794.72 |  | 1774.3078 | 1.1504 | 1829.9 | 1759.045 | 0.1003 | watch_only | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.64 |  | 21.9822 | 2.9923 | 22.36 | 21.94 | 0.0883 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 393.925 |  | 392.2559 | 0.4255 | 397.94 | 392.62 | 0.4011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SOXX | semiconductor_index | 552.8 |  | 551.5629 | 0.2243 | 575.7 | 565.33 | 0.0796 | below_opening_15m_low | below_opening_15m_low |
| 8 | ORCL | cloud_ai_capex | 132.925 |  | 131.9577 | 0.733 | 132.925 | 129.92 | 1.4595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SPY | market_regime | 753.55 |  | 753.3223 | 0.0302 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |
| 10 | KLAC | semiconductor_equipment | 222.96 |  | 222.6504 | 0.139 | 236.49 | 225.11 | 0.0762 | below_opening_15m_low | below_opening_15m_low |
| 11 | SMH | semiconductor_index | 588 |  | 587.3055 | 0.1183 | 606.85 | 597.81 | 0.0629 | below_opening_15m_low | below_opening_15m_low |
| 12 | APLD | high_beta_ai_infrastructure | 28.85 |  | 28.3469 | 1.7747 | 29.055 | 28.28 | 0.0693 | watch_only | none |
| 13 | SMCI | ai_server_oem | 27.08 |  | 26.8961 | 0.6838 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| 14 | META | cloud_ai_capex | 678.43 |  | 675.6751 | 0.4077 | 664.875 | 657.17 | 0.3832 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | IWM | market_regime | 295.48 |  | 295.6331 | -0.0518 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 16 | AMZN | cloud_ai_capex | 254.04 |  | 254.4816 | -0.1735 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 17 | PWR | data_center_power_cooling | 650.76 |  | 646.3035 | 0.6895 | 663.475 | 653.94 | 0.1721 | below_opening_15m_low | below_opening_15m_low |
| 18 | LRCX | semiconductor_equipment | 332.64 |  | 331.4128 | 0.3703 | 355.245 | 340.745 | 0.1744 | below_opening_15m_low | below_opening_15m_low |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ANET | ai_networking_optical | 171.865 |  | 171.8052 | 0.0348 | 186.095 | 178.355 | 4.6548 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 395.75 |  | 395.3862 | 0.092 | 391.33 | 387.05 | 0.048 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.7 |  | 369.075 | 0.4403 | 364.41 | 357.885 | 0.0432 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.28 |  | 325.8705 | 0.1257 | 321.14 | 317.4 | 0.0245 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.64 |  | 21.9822 | 2.9923 | 22.36 | 21.94 | 0.0883 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 254.04 |  | 254.4816 | -0.1735 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 6 | META | cloud_ai_capex | 678.43 |  | 675.6751 | 0.4077 | 664.875 | 657.17 | 0.3832 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1794.72 |  | 1774.3078 | 1.1504 | 1829.9 | 1759.045 | 0.1003 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.925 |  | 131.9577 | 0.733 | 132.925 | 129.92 | 1.4595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APLD | high_beta_ai_infrastructure | 28.85 |  | 28.3469 | 1.7747 | 29.055 | 28.28 | 0.0693 | watch_only | none |
| 10 | IWM | market_regime | 295.48 |  | 295.6331 | -0.0518 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 393.925 |  | 392.2559 | 0.4255 | 397.94 | 392.62 | 0.4011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | NVDA | ai_accelerator | 211.15 |  | 209.4776 | 0.7983 | 213.775 | 211.225 | 0.5304 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 14 | SOXX | semiconductor_index | 552.8 |  | 551.5629 | 0.2243 | 575.7 | 565.33 | 0.0796 | below_opening_15m_low | below_opening_15m_low |
| 15 | ANET | ai_networking_optical | 171.865 |  | 171.8052 | 0.0348 | 186.095 | 178.355 | 4.6548 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | STX | memory_hbm_storage | 821.36 |  | 817.6589 | 0.4526 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | SPY | market_regime | 753.55 |  | 753.3223 | 0.0302 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |
| 18 | AMD | ai_accelerator | 527.47 |  | 527.4523 | 0.0034 | 558.62 | 548.745 | 1.2342 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 303.675 |  | 299.587 | 1.3645 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | SNDK | memory_hbm_storage | 1646.57 |  | 1585.5513 | 3.8484 | 1726.34 | 1665.91 | 2.5526 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.11 |  | 716.3379 | -0.0318 | 724.31 | 721.08 | 0.0196 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.89 |  | 74.1845 | -0.397 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.15 |  | 209.4776 | 0.7983 | 213.775 | 211.225 | 0.5304 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MSFT | cloud_ai_capex | 395.75 |  | 395.3862 | 0.092 | 391.33 | 387.05 | 0.048 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 326.28 |  | 325.8705 | 0.1257 | 321.14 | 317.4 | 0.0245 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.7 |  | 369.075 | 0.4403 | 364.41 | 357.885 | 0.0432 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 527.47 |  | 527.4523 | 0.0034 | 558.62 | 548.745 | 1.2342 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 419.17 |  | 418.9881 | 0.0434 | 428.59 | 422.945 | 1.8107 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.8 |  | 551.5629 | 0.2243 | 575.7 | 565.33 | 0.0796 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588 |  | 587.3055 | 0.1183 | 606.85 | 597.81 | 0.0629 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 393.925 |  | 392.2559 | 0.4255 | 397.94 | 392.62 | 0.4011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 904.56 |  | 909.4343 | -0.536 | 977.7 | 953.67 | 0.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 205.43 |  | 208.0927 | -1.2796 | 223.02 | 214.85 | 2.1954 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 411.99 |  | 407.0491 | 1.2138 | 457.935 | 442.67 | 0.216 | below_opening_15m_low | below_opening_15m_low |
| HPE | ai_server_oem | 47.625 |  | 47.0033 | 1.3227 | 50.2 | 48.995 | 0.021 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.08 |  | 26.8961 | 0.6838 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.55 |  | 753.3223 | 0.0302 | 755.54 | 754.215 | 0.0265 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.48 |  | 295.6331 | -0.0518 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.925 |  | 131.9577 | 0.733 | 132.925 | 129.92 | 1.4595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.09 |  | 77.4772 | -0.4997 | 80.585 | 78.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.675 |  | 299.587 | 1.3645 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.84 |  | 408.7795 | 0.7487 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 650.76 |  | 646.3035 | 0.6895 | 663.475 | 653.94 | 0.1721 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1056.25 |  | 1037.3104 | 1.8258 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 477.75 |  | 478.6544 | -0.1889 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.49 |  | 141.858 | 0.4455 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.865 |  | 171.8052 | 0.0348 | 186.095 | 178.355 | 4.6548 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 296.39 |  | 294.1292 | 0.7686 | 315.74 | 303.34 | 0.4251 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 748.32 |  | 749.0984 | -0.1039 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 419.56 |  | 419.7712 | -0.0503 | 438.14 | 427.54 | 4.4952 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 108.96 |  | 111.7143 | -2.4655 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 347.64 |  | 345.0192 | 0.7596 | 369.23 | 356.615 | 2.3731 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1794.72 |  | 1774.3078 | 1.1504 | 1829.9 | 1759.045 | 0.1003 | watch_only | none |
| AMAT | semiconductor_equipment | 577.05 |  | 577.5255 | -0.0823 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 332.64 |  | 331.4128 | 0.3703 | 355.245 | 340.745 | 0.1744 | below_opening_15m_low | below_opening_15m_low |
| KLAC | semiconductor_equipment | 222.96 |  | 222.6504 | 0.139 | 236.49 | 225.11 | 0.0762 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 339.75 |  | 336.4868 | 0.9698 | 356.29 | 343.785 | 4.624 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 304.515 |  | 307.0152 | -0.8143 | 326.25 | 317.3 | 4.6993 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.365 |  | 67.0472 | 0.4739 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.62 |  | 54.3723 | 0.4556 | 57.92 | 55.2 | 0.6042 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 137.48 |  | 137.5591 | -0.0575 | 143.15 | 140.4 | 0.3419 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 352.05 |  | 349.0126 | 0.8703 | 368.67 | 358.39 | 0.5283 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LIN | industrial_gases | 515.14 |  | 516.0657 | -0.1794 | 521.075 | 518.3 | 4.6337 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.975 |  | 294.3932 | -0.1421 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.85 |  | 28.3469 | 1.7747 | 29.055 | 28.28 | 0.0693 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.57 |  | 39.2185 | -1.6535 | 40.01 | 38.815 | 0.0259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.64 |  | 21.9822 | 2.9923 | 22.36 | 21.94 | 0.0883 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1646.57 |  | 1585.5513 | 3.8484 | 1726.34 | 1665.91 | 2.5526 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 511.995 |  | 516.1025 | -0.7959 | 568.16 | 542.4 | 1.3574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 821.36 |  | 817.6589 | 0.4526 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.04 |  | 254.4816 | -0.1735 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| META | cloud_ai_capex | 678.43 |  | 675.6751 | 0.4077 | 664.875 | 657.17 | 0.3832 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 274.94 |  | 275.5071 | -0.2058 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 173.87 |  | 175.8412 | -1.121 | 183.63 | 176.08 | 0.0748 | below_opening_15m_low | below_opening_15m_low,below_vwap |
