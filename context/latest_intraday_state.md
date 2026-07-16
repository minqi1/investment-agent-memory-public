# Intraday State

- Generated at: `2026-07-17T00:19:38+08:00`
- Market time ET: `2026-07-16T12:19:39-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 34, 'spread_too_wide_or_missing': 5, 'manual_confirm_candidate': 1, 'below_vwap': 14, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.2 |  | 710.3263 | -0.2993 | 713.55 | 708.25 | 0.0268 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.08 |  | 537.0145 | -1.2913 | 543.4 | 535.47 | 0.0755 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.81 |  | 574.8458 | -1.05 | 580.31 | 572.21 | 0.0527 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.51 |  | 752.8374 | -0.0435 | 753.51 | 751.13 | 0.0146 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.21 |  | 329.8521 | 0.4117 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.21 |  | 329.8521 | 0.4117 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 256.31 |  | 255.3732 | 0.3668 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 3 | TT | data_center_power_cooling | 474.72 |  | 474.367 | 0.0744 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 516.52 |  | 514.7485 | 0.3441 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 166.74 |  | 166.3176 | 0.254 | 169.91 | 165.6 | 4.6899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.755 |  | 294.6493 | 0.7146 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TSM | foundry | 406.85 |  | 410.918 | -0.99 | 414.385 | 406.61 | 0.0614 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1810.36 |  | 1824.5377 | -0.7771 | 1823.13 | 1796.26 | 0.1237 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 752.51 |  | 752.8374 | -0.0435 | 753.51 | 751.13 | 0.0146 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 296.005 |  | 296.5394 | -0.1802 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.65 |  | 371.9304 | -0.0754 | 375.18 | 369.2 | 0.1426 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | MSFT | cloud_ai_capex | 400.435 |  | 396.5579 | 0.9777 | 398.69 | 392.2 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | JCI | data_center_power_cooling | 140.34 |  | 140.6447 | -0.2167 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ONTO | semiconductor_test_packaging | 285.25 |  | 290.2743 | -1.7309 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | META | cloud_ai_capex | 670.67 |  | 674.6855 | -0.5952 | 680.09 | 667.1 | 0.2937 | below_vwap | below_vwap |
| 17 | AVGO | custom_silicon_networking | 380.605 |  | 381.7408 | -0.2975 | 386.58 | 378.53 | 0.712 | below_vwap | below_vwap,spread_too_wide |
| 18 | GEV | data_center_power_cooling | 1028.255 |  | 1032.4857 | -0.4098 | 1035.07 | 1021.09 | 4.1604 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMAT | semiconductor_equipment | 566.36 |  | 574.3303 | -1.3878 | 572.69 | 562.32 | 2.456 | below_vwap | below_vwap,spread_too_wide |
| 20 | KLAC | semiconductor_equipment | 219.025 |  | 222.438 | -1.5344 | 222.19 | 218.09 | 5.0999 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.21 |  | 329.8521 | 0.4117 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | TT | data_center_power_cooling | 474.72 |  | 474.367 | 0.0744 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | LIN | industrial_gases | 516.52 |  | 514.7485 | 0.3441 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.755 |  | 294.6493 | 0.7146 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 400.435 |  | 396.5579 | 0.9777 | 398.69 | 392.2 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AMZN | cloud_ai_capex | 256.31 |  | 255.3732 | 0.3668 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 7 | TSM | foundry | 406.85 |  | 410.918 | -0.99 | 414.385 | 406.61 | 0.0614 | below_vwap | below_vwap |
| 8 | AVGO | custom_silicon_networking | 380.605 |  | 381.7408 | -0.2975 | 386.58 | 378.53 | 0.712 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 140.34 |  | 140.6447 | -0.2167 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | GEV | data_center_power_cooling | 1028.255 |  | 1032.4857 | -0.4098 | 1035.07 | 1021.09 | 4.1604 | below_vwap | below_vwap,spread_too_wide |
| 11 | ASML | semiconductor_equipment | 1810.36 |  | 1824.5377 | -0.7771 | 1823.13 | 1796.26 | 0.1237 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 566.36 |  | 574.3303 | -1.3878 | 572.69 | 562.32 | 2.456 | below_vwap | below_vwap,spread_too_wide |
| 13 | ONTO | semiconductor_test_packaging | 285.25 |  | 290.2743 | -1.7309 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 219.025 |  | 222.438 | -1.5344 | 222.19 | 218.09 | 5.0999 | below_vwap | below_vwap,spread_too_wide |
| 15 | SPY | market_regime | 752.51 |  | 752.8374 | -0.0435 | 753.51 | 751.13 | 0.0146 | below_vwap | below_vwap |
| 16 | IWM | market_regime | 296.005 |  | 296.5394 | -0.1802 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 133.78 |  | 135.5394 | -1.2981 | 138.07 | 133.73 | 3.5656 | below_vwap | below_vwap,spread_too_wide |
| 19 | GOOGL | cloud_ai_capex | 371.65 |  | 371.9304 | -0.0754 | 375.18 | 369.2 | 0.1426 | below_vwap | below_vwap |
| 20 | META | cloud_ai_capex | 670.67 |  | 674.6855 | -0.5952 | 680.09 | 667.1 | 0.2937 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.2 |  | 710.3263 | -0.2993 | 713.55 | 708.25 | 0.0268 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.44 |  | 72.1502 | -0.9843 | 73.09 | 71.45 | 0.028 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.07 |  | 207.5899 | -0.2504 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.435 |  | 396.5579 | 0.9777 | 398.69 | 392.2 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 331.21 |  | 329.8521 | 0.4117 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.65 |  | 371.9304 | -0.0754 | 375.18 | 369.2 | 0.1426 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.99 |  | 509.1236 | -1.794 | 518.33 | 507.62 | 1.034 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.85 |  | 410.918 | -0.99 | 414.385 | 406.61 | 0.0614 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.08 |  | 537.0145 | -1.2913 | 543.4 | 535.47 | 0.0755 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.81 |  | 574.8458 | -1.05 | 580.31 | 572.21 | 0.0527 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.605 |  | 381.7408 | -0.2975 | 386.58 | 378.53 | 0.712 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.52 |  | 862.8878 | -1.6651 | 887.1 | 866.765 | 2.1213 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.13 |  | 192.9829 | -2.5147 | 201.61 | 194.19 | 2.0465 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.4 |  | 404.2415 | -1.1977 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.45 |  | 46.1501 | -1.5171 | 47.65 | 46.165 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.045 |  | 25.6165 | -2.2311 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.51 |  | 752.8374 | -0.0435 | 753.51 | 751.13 | 0.0146 | below_vwap | below_vwap |
| IWM | market_regime | 296.005 |  | 296.5394 | -0.1802 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.17 |  | 126.8787 | -0.5586 | 131.36 | 126.665 | 3.9629 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.54 |  | 73.6503 | -1.5075 | 75.54 | 73.985 | 0.0827 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 289.95 |  | 295.6416 | -1.9252 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 392.96 |  | 400.731 | -1.9392 | 406.24 | 399.495 | 3.6467 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 628.17 |  | 632.9519 | -0.7555 | 640.25 | 631.005 | 4.7869 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1028.255 |  | 1032.4857 | -0.4098 | 1035.07 | 1021.09 | 4.1604 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.72 |  | 474.367 | 0.0744 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.34 |  | 140.6447 | -0.2167 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.74 |  | 166.3176 | 0.254 | 169.91 | 165.6 | 4.6899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.55 |  | 283.1122 | -2.3179 | 288.48 | 280.67 | 3.6413 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.93 |  | 713.2001 | -1.7204 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 391.58 |  | 397.4842 | -1.4854 | 410 | 397.68 | 4.561 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 99.02 |  | 102.6178 | -3.506 | 106.975 | 102.85 | 3.4034 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 316.42 |  | 325.7594 | -2.867 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1810.36 |  | 1824.5377 | -0.7771 | 1823.13 | 1796.26 | 0.1237 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.36 |  | 574.3303 | -1.3878 | 572.69 | 562.32 | 2.456 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.3 |  | 326.035 | -1.759 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.025 |  | 222.438 | -1.5344 | 222.19 | 218.09 | 5.0999 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 323.125 |  | 328.4906 | -1.6334 | 332.49 | 326.685 | 4.6607 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 285.25 |  | 290.2743 | -1.7309 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.345 |  | 64.5169 | -1.8164 | 66.19 | 63.93 | 0.1579 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 51.58 |  | 52.4146 | -1.5923 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.78 |  | 135.5394 | -1.2981 | 138.07 | 133.73 | 3.5656 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 334.75 |  | 339.8179 | -1.4914 | 346.26 | 338 | 4.2121 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.52 |  | 514.7485 | 0.3441 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.755 |  | 294.6493 | 0.7146 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.33 |  | 27.192 | -3.17 | 28.05 | 27.6 | 0.038 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.97 |  | 35.8309 | -2.4028 | 37.365 | 36.4 | 0.0286 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.04 |  | 21.4675 | -1.9915 | 22.18 | 21.78 | 0.0951 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1432.11 |  | 1481.1195 | -3.309 | 1549.47 | 1482.06 | 1.5013 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 464.48 |  | 480.4022 | -3.3144 | 498.04 | 480.14 | 1.1841 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 755.69 |  | 771.2491 | -2.0174 | 797.155 | 768.7 | 4.089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.31 |  | 255.3732 | 0.3668 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 670.67 |  | 674.6855 | -0.5952 | 680.09 | 667.1 | 0.2937 | below_vwap | below_vwap |
| ARM | ai_accelerator | 253.44 |  | 258.2298 | -1.8548 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.21 |  | 163.5158 | -1.4102 | 168.11 | 162.41 | 0.6203 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
