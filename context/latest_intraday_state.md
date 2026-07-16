# Intraday State

- Generated at: `2026-07-17T01:04:00+08:00`
- Market time ET: `2026-07-16T13:04:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 36, 'manual_confirm_candidate': 3, 'below_vwap': 11, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.72 |  | 709.9705 | -0.317 | 713.55 | 708.25 | 0.0268 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.37 |  | 536.0908 | -1.2537 | 543.4 | 535.47 | 0.0793 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.825 |  | 573.8443 | -0.8747 | 580.31 | 572.21 | 0.0879 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.26 |  | 752.7454 | -0.0645 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.26 |  | 294.8197 | 0.4885 | 293.89 | 291.35 | 0.3105 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.59 |  | 397.6286 | 1.2477 | 398.69 | 392.2 | 0.1764 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.96 |  | 330.038 | 0.5823 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.81 |  | 255.4478 | 0.1418 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 331.96 |  | 330.038 | 0.5823 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.26 |  | 294.8197 | 0.4885 | 293.89 | 291.35 | 0.3105 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.75 |  | 140.528 | 0.158 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 402.59 |  | 397.6286 | 1.2477 | 398.69 | 392.2 | 0.1764 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 475.39 |  | 474.0127 | 0.2906 | 474.085 | 467.64 | 4.9812 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 516.46 |  | 514.8944 | 0.3041 | 515.825 | 512.23 | 0.5576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 167.14 |  | 166.386 | 0.4532 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SPY | market_regime | 752.26 |  | 752.7454 | -0.0645 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.85 |  | 296.4073 | -0.188 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.61 |  | 371.8799 | -0.0726 | 375.18 | 369.2 | 0.0727 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | META | cloud_ai_capex | 669.22 |  | 673.3854 | -0.6186 | 680.09 | 667.1 | 0.2002 | below_vwap | below_vwap |
| 14 | ENTG | semiconductor_materials | 134.96 |  | 135.1543 | -0.1438 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ASML | semiconductor_equipment | 1807.22 |  | 1822.3819 | -0.832 | 1823.13 | 1796.26 | 0.5102 | below_vwap | below_vwap,spread_too_wide |
| 16 | GEV | data_center_power_cooling | 1025.4 |  | 1029.294 | -0.3783 | 1035.07 | 1021.09 | 4.1486 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMAT | semiconductor_equipment | 565.99 |  | 572.8601 | -1.1993 | 572.69 | 562.32 | 2.5548 | below_vwap | below_vwap,spread_too_wide |
| 18 | KLAC | semiconductor_equipment | 218.925 |  | 221.6535 | -1.231 | 222.19 | 218.09 | 5.0017 | below_vwap | below_vwap,spread_too_wide |
| 19 | ORCL | cloud_ai_capex | 126.67 |  | 126.762 | -0.0726 | 131.36 | 126.665 | 0.4816 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 529.37 |  | 536.0908 | -1.2537 | 543.4 | 535.47 | 0.0793 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.26 |  | 294.8197 | 0.4885 | 293.89 | 291.35 | 0.3105 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.59 |  | 397.6286 | 1.2477 | 398.69 | 392.2 | 0.1764 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.96 |  | 330.038 | 0.5823 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.39 |  | 474.0127 | 0.2906 | 474.085 | 467.64 | 4.9812 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | LIN | industrial_gases | 516.46 |  | 514.8944 | 0.3041 | 515.825 | 512.23 | 0.5576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AMZN | cloud_ai_capex | 255.81 |  | 255.4478 | 0.1418 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| 7 | GEV | data_center_power_cooling | 1025.4 |  | 1029.294 | -0.3783 | 1035.07 | 1021.09 | 4.1486 | below_vwap | below_vwap,spread_too_wide |
| 8 | ASML | semiconductor_equipment | 1807.22 |  | 1822.3819 | -0.832 | 1823.13 | 1796.26 | 0.5102 | below_vwap | below_vwap,spread_too_wide |
| 9 | AMAT | semiconductor_equipment | 565.99 |  | 572.8601 | -1.1993 | 572.69 | 562.32 | 2.5548 | below_vwap | below_vwap,spread_too_wide |
| 10 | KLAC | semiconductor_equipment | 218.925 |  | 221.6535 | -1.231 | 222.19 | 218.09 | 5.0017 | below_vwap | below_vwap,spread_too_wide |
| 11 | SPY | market_regime | 752.26 |  | 752.7454 | -0.0645 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.85 |  | 296.4073 | -0.188 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 134.96 |  | 135.1543 | -0.1438 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ORCL | cloud_ai_capex | 126.67 |  | 126.762 | -0.0726 | 131.36 | 126.665 | 0.4816 | below_vwap | below_vwap,spread_too_wide |
| 16 | GOOGL | cloud_ai_capex | 371.61 |  | 371.8799 | -0.0726 | 375.18 | 369.2 | 0.0727 | below_vwap | below_vwap |
| 17 | META | cloud_ai_capex | 669.22 |  | 673.3854 | -0.6186 | 680.09 | 667.1 | 0.2002 | below_vwap | below_vwap |
| 18 | ANET | ai_networking_optical | 167.14 |  | 166.386 | 0.4532 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 140.75 |  | 140.528 | 0.158 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SOXX | semiconductor_index | 529.37 |  | 536.0908 | -1.2537 | 543.4 | 535.47 | 0.0793 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.72 |  | 709.9705 | -0.317 | 713.55 | 708.25 | 0.0268 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.295 |  | 72.0397 | -1.0337 | 73.09 | 71.45 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.69 |  | 207.5183 | -0.3991 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.59 |  | 397.6286 | 1.2477 | 398.69 | 392.2 | 0.1764 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.96 |  | 330.038 | 0.5823 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.61 |  | 371.8799 | -0.0726 | 375.18 | 369.2 | 0.0727 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.65 |  | 507.2713 | -1.5024 | 518.33 | 507.62 | 0.6585 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.03 |  | 410.3136 | -1.044 | 414.385 | 406.61 | 0.8768 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.37 |  | 536.0908 | -1.2537 | 543.4 | 535.47 | 0.0793 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.825 |  | 573.8443 | -0.8747 | 580.31 | 572.21 | 0.0879 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.42 |  | 381.2972 | -1.0168 | 386.58 | 378.53 | 0.7525 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 847.895 |  | 860.2804 | -1.4397 | 887.1 | 866.765 | 0.8126 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.09 |  | 192.3069 | -2.1928 | 201.61 | 194.19 | 0.7177 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.5 |  | 403.3715 | -0.7119 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.27 |  | 46.0426 | -1.678 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.995 |  | 25.4963 | -1.9662 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.26 |  | 752.7454 | -0.0645 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |
| IWM | market_regime | 295.85 |  | 296.4073 | -0.188 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.67 |  | 126.762 | -0.0726 | 131.36 | 126.665 | 0.4816 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.215 |  | 73.5193 | -0.414 | 75.54 | 73.985 | 4.4117 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 291.14 |  | 294.8298 | -1.2515 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.75 |  | 400.0841 | -1.0833 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.97 |  | 632.225 | -0.673 | 640.25 | 631.005 | 4.8267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1025.4 |  | 1029.294 | -0.3783 | 1035.07 | 1021.09 | 4.1486 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.39 |  | 474.0127 | 0.2906 | 474.085 | 467.64 | 4.9812 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.75 |  | 140.528 | 0.158 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.14 |  | 166.386 | 0.4532 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.22 |  | 281.9988 | -1.34 | 288.48 | 280.67 | 3.3031 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.43 |  | 711.1952 | -1.7949 | 737.175 | 720.21 | 2.8364 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.94 |  | 396.4504 | -1.3899 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.03 |  | 102.146 | -3.0506 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.52 |  | 324.7302 | -1.9124 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1807.22 |  | 1822.3819 | -0.832 | 1823.13 | 1796.26 | 0.5102 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 565.99 |  | 572.8601 | -1.1993 | 572.69 | 562.32 | 2.5548 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.16 |  | 325.0469 | -1.5034 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.925 |  | 221.6535 | -1.231 | 222.19 | 218.09 | 5.0017 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 324.69 |  | 327.566 | -0.878 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.31 |  | 289.3043 | -1.7263 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.12 |  | 64.3637 | -1.9323 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.62 |  | 52.2972 | -1.2949 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.96 |  | 135.1543 | -0.1438 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.645 |  | 338.7585 | -0.9191 | 346.26 | 338 | 3.7361 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.46 |  | 514.8944 | 0.3041 | 515.825 | 512.23 | 0.5576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.26 |  | 294.8197 | 0.4885 | 293.89 | 291.35 | 0.3105 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.21 |  | 27.034 | -3.048 | 28.05 | 27.6 | 0.0763 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.89 |  | 35.7207 | -2.3255 | 37.365 | 36.4 | 0.086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.875 |  | 21.3466 | -2.2094 | 22.18 | 21.78 | 0.0958 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1441.14 |  | 1475.2098 | -2.3095 | 1549.47 | 1482.06 | 4.996 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 460.375 |  | 477.3287 | -3.5518 | 498.04 | 480.14 | 2.4111 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 753.85 |  | 769.2405 | -2.0007 | 797.155 | 768.7 | 3.7992 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.81 |  | 255.4478 | 0.1418 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| META | cloud_ai_capex | 669.22 |  | 673.3854 | -0.6186 | 680.09 | 667.1 | 0.2002 | below_vwap | below_vwap |
| ARM | ai_accelerator | 253.395 |  | 257.5627 | -1.6181 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 159.41 |  | 163.2304 | -2.3405 | 168.11 | 162.41 | 2.7915 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
