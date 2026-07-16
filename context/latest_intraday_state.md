# Intraday State

- Generated at: `2026-07-17T03:43:20+08:00`
- Market time ET: `2026-07-16T15:43:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 3, 'below_vwap': 5, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.53 |  | 708.518 | -0.5629 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.62 |  | 532.8947 | -0.9898 | 543.4 | 535.47 | 0.0663 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.64 |  | 571.2239 | -0.8025 | 580.31 | 572.21 | 0.0459 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.05 |  | 751.7058 | -0.3533 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.42 |  | 515.6162 | 0.5438 | 515.825 | 512.23 | 0.0791 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 400.485 |  | 400.099 | 0.0965 | 398.69 | 392.2 | 0.2572 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332.555 |  | 331.453 | 0.3325 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.485 |  | 400.099 | 0.0965 | 398.69 | 392.2 | 0.2572 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.555 |  | 331.453 | 0.3325 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.42 |  | 515.6162 | 0.5438 | 515.825 | 512.23 | 0.0791 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.99 |  | 140.5837 | 0.289 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 475.4 |  | 474.2709 | 0.2381 | 474.085 | 467.64 | 4.9706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.095 |  | 166.6076 | 0.2926 | 169.91 | 165.6 | 3.2975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 296.1 |  | 295.1554 | 0.32 | 293.89 | 291.35 | 4.0122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | GEV | data_center_power_cooling | 1033.49 |  | 1027.2912 | 0.6034 | 1035.07 | 1021.09 | 3.4485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ARM | ai_accelerator | 259.02 |  | 257.2431 | 0.6908 | 265.96 | 258.1 | 1.3512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | TSM | foundry | 407.45 |  | 408.4009 | -0.2328 | 414.385 | 406.61 | 0.0295 | below_vwap | below_vwap |
| 11 | KLAC | semiconductor_equipment | 218.535 |  | 220.4102 | -0.8508 | 222.19 | 218.09 | 0.0824 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 294.73 |  | 295.9092 | -0.3985 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | VRT | data_center_power_cooling | 293.45 |  | 292.9845 | 0.1589 | 300.385 | 293.64 | 5.0298 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | AMAT | semiconductor_equipment | 563.98 |  | 568.6903 | -0.8283 | 572.69 | 562.32 | 2.9292 | below_vwap | below_vwap,spread_too_wide |
| 16 | SOXX | semiconductor_index | 527.62 |  | 532.8947 | -0.9898 | 543.4 | 535.47 | 0.0663 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 704.53 |  | 708.518 | -0.5629 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | MU | memory_hbm_storage | 849.925 |  | 855.4602 | -0.647 | 887.1 | 866.765 | 0.0718 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1796.005 |  | 1812.609 | -0.916 | 1823.13 | 1796.26 | 0.0501 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 566.64 |  | 571.2239 | -0.8025 | 580.31 | 572.21 | 0.0459 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.42 |  | 515.6162 | 0.5438 | 515.825 | 512.23 | 0.0791 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 400.485 |  | 400.099 | 0.0965 | 398.69 | 392.2 | 0.2572 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332.555 |  | 331.453 | 0.3325 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.4 |  | 474.2709 | 0.2381 | 474.085 | 467.64 | 4.9706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | JCI | data_center_power_cooling | 140.99 |  | 140.5837 | 0.289 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.1 |  | 295.1554 | 0.32 | 293.89 | 291.35 | 4.0122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | TSM | foundry | 407.45 |  | 408.4009 | -0.2328 | 414.385 | 406.61 | 0.0295 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 563.98 |  | 568.6903 | -0.8283 | 572.69 | 562.32 | 2.9292 | below_vwap | below_vwap,spread_too_wide |
| 9 | KLAC | semiconductor_equipment | 218.535 |  | 220.4102 | -0.8508 | 222.19 | 218.09 | 0.0824 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 294.73 |  | 295.9092 | -0.3985 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ANET | ai_networking_optical | 167.095 |  | 166.6076 | 0.2926 | 169.91 | 165.6 | 3.2975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | GEV | data_center_power_cooling | 1033.49 |  | 1027.2912 | 0.6034 | 1035.07 | 1021.09 | 3.4485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ARM | ai_accelerator | 259.02 |  | 257.2431 | 0.6908 | 265.96 | 258.1 | 1.3512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | VRT | data_center_power_cooling | 293.45 |  | 292.9845 | 0.1589 | 300.385 | 293.64 | 5.0298 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | SOXX | semiconductor_index | 527.62 |  | 532.8947 | -0.9898 | 543.4 | 535.47 | 0.0663 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 390.22 |  | 393.0224 | -0.713 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 704.53 |  | 708.518 | -0.5629 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 375.97 |  | 379.2232 | -0.8579 | 386.58 | 378.53 | 1.3565 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 849.925 |  | 855.4602 | -0.647 | 887.1 | 866.765 | 0.0718 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.53 |  | 708.518 | -0.5629 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.27 |  | 71.6103 | -1.8717 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.125 |  | 207.2904 | -0.5622 | 211.03 | 207.49 | 0.359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 400.485 |  | 400.099 | 0.0965 | 398.69 | 392.2 | 0.2572 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.555 |  | 331.453 | 0.3325 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 354.45 |  | 365.4573 | -3.0119 | 375.18 | 369.2 | 0.0395 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 497.18 |  | 502.3821 | -1.0355 | 518.33 | 507.62 | 1.2712 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 407.45 |  | 408.4009 | -0.2328 | 414.385 | 406.61 | 0.0295 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.62 |  | 532.8947 | -0.9898 | 543.4 | 535.47 | 0.0663 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.64 |  | 571.2239 | -0.8025 | 580.31 | 572.21 | 0.0459 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.97 |  | 379.2232 | -0.8579 | 386.58 | 378.53 | 1.3565 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 849.925 |  | 855.4602 | -0.647 | 887.1 | 866.765 | 0.0718 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.29 |  | 190.4729 | -1.146 | 201.61 | 194.19 | 1.2481 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 394.65 |  | 401.0819 | -1.6036 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.285 |  | 45.7183 | -0.9478 | 47.65 | 46.165 | 0.0442 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.925 |  | 25.2597 | -1.325 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.05 |  | 751.7058 | -0.3533 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.73 |  | 295.9092 | -0.3985 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 123.78 |  | 126.2382 | -1.9473 | 131.36 | 126.665 | 3.6032 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.625 |  | 73.279 | -0.8925 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 293.45 |  | 292.9845 | 0.1589 | 300.385 | 293.64 | 5.0298 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ETN | data_center_power_cooling | 396.87 |  | 399.1156 | -0.5627 | 406.24 | 399.495 | 0.2646 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 630.28 |  | 630.9956 | -0.1134 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1033.49 |  | 1027.2912 | 0.6034 | 1035.07 | 1021.09 | 3.4485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.4 |  | 474.2709 | 0.2381 | 474.085 | 467.64 | 4.9706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.99 |  | 140.5837 | 0.289 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.095 |  | 166.6076 | 0.2926 | 169.91 | 165.6 | 3.2975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.9 |  | 280.2264 | -1.5439 | 288.48 | 280.67 | 1.033 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.31 |  | 706.9819 | -0.8023 | 737.175 | 720.21 | 0.5119 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.22 |  | 393.0224 | -0.713 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.04 |  | 100.9422 | -0.8938 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.32 |  | 322.5194 | -1.3021 | 337.59 | 326.16 | 2.8336 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1796.005 |  | 1812.609 | -0.916 | 1823.13 | 1796.26 | 0.0501 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 563.98 |  | 568.6903 | -0.8283 | 572.69 | 562.32 | 2.9292 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.96 |  | 321.7864 | -1.1891 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.535 |  | 220.4102 | -0.8508 | 222.19 | 218.09 | 0.0824 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 319.855 |  | 325.3063 | -1.6757 | 332.49 | 326.685 | 0.4471 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 281.01 |  | 285.0886 | -1.4306 | 295.83 | 285.02 | 5.103 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 63.06 |  | 63.753 | -1.0871 | 66.19 | 63.93 | 0.8088 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.065 |  | 51.6995 | -1.2273 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.505 |  | 134.3432 | -0.6239 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.35 |  | 333.5142 | -1.2486 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.42 |  | 515.6162 | 0.5438 | 515.825 | 512.23 | 0.0791 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.1 |  | 295.1554 | 0.32 | 293.89 | 291.35 | 4.0122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.13 |  | 26.737 | -2.2704 | 28.05 | 27.6 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.955 |  | 35.4875 | -1.5005 | 37.365 | 36.4 | 0.0286 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.93 |  | 21.1847 | -1.2023 | 22.18 | 21.78 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1416.815 |  | 1450.378 | -2.3141 | 1549.47 | 1482.06 | 3.035 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 463.19 |  | 471.87 | -1.8395 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 745.23 |  | 760.7243 | -2.0368 | 797.155 | 768.7 | 0.9125 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 252.02 |  | 254.6555 | -1.0349 | 258.07 | 252.62 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 662.97 |  | 670.228 | -1.0829 | 680.09 | 667.1 | 0.4631 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 259.02 |  | 257.2431 | 0.6908 | 265.96 | 258.1 | 1.3512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 156.585 |  | 161.1207 | -2.8151 | 168.11 | 162.41 | 0.1277 | below_opening_15m_low | below_opening_15m_low,below_vwap |
