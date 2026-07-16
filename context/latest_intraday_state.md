# Intraday State

- Generated at: `2026-07-17T02:55:31+08:00`
- Market time ET: `2026-07-16T14:55:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 2, 'below_vwap': 7, 'spread_too_wide_or_missing': 3, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.89 |  | 709.3379 | -0.4861 | 713.55 | 708.25 | 0.0113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.05 |  | 533.8314 | -1.083 | 543.4 | 535.47 | 0.0492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.94 |  | 571.7363 | -0.8389 | 580.31 | 572.21 | 0.0406 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.25 |  | 752.3079 | -0.2735 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.48 |  | 399.5203 | 1.2414 | 398.69 | 392.2 | 0.0445 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.79 |  | 330.73 | 0.6229 | 328.98 | 326.885 | 0.0361 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 166.885 |  | 166.586 | 0.1795 | 169.91 | 165.6 | 0.1258 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 332.79 |  | 330.73 | 0.6229 | 328.98 | 326.885 | 0.0361 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 404.48 |  | 399.5203 | 1.2414 | 398.69 | 392.2 | 0.0445 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.665 |  | 140.5212 | 0.1024 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 518.66 |  | 515.1739 | 0.6767 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.38 |  | 294.9801 | 0.4746 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | IREN | high_beta_ai_infrastructure | 35.515 |  | 35.5004 | 0.0411 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low |
| 8 | IWM | market_regime | 295.125 |  | 296.1386 | -0.3423 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | META | cloud_ai_capex | 667.94 |  | 671.3675 | -0.5105 | 680.09 | 667.1 | 0.1108 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | TT | data_center_power_cooling | 473.79 |  | 474.1319 | -0.0721 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 219.5 |  | 220.9588 | -0.6602 | 222.19 | 218.09 | 0.8018 | below_vwap | below_vwap,spread_too_wide |
| 13 | ENTG | semiconductor_materials | 133.74 |  | 134.8801 | -0.8453 | 138.07 | 133.73 | 0.4337 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMZN | cloud_ai_capex | 253.075 |  | 255.1331 | -0.8067 | 258.07 | 252.62 | 0.4149 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 528.05 |  | 533.8314 | -1.083 | 543.4 | 535.47 | 0.0492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 405.13 |  | 408.8229 | -0.9033 | 414.385 | 406.61 | 0.0666 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 705.89 |  | 709.3379 | -0.4861 | 713.55 | 708.25 | 0.0113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 207.085 |  | 207.3493 | -0.1275 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1793.065 |  | 1818.0344 | -1.3734 | 1823.13 | 1796.26 | 0.1099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 566.94 |  | 571.7363 | -0.8389 | 580.31 | 572.21 | 0.0406 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.48 |  | 399.5203 | 1.2414 | 398.69 | 392.2 | 0.0445 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.79 |  | 330.73 | 0.6229 | 328.98 | 326.885 | 0.0361 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.66 |  | 515.1739 | 0.6767 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.38 |  | 294.9801 | 0.4746 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 166.885 |  | 166.586 | 0.1795 | 169.91 | 165.6 | 0.1258 | watch_only | none |
| 6 | TT | data_center_power_cooling | 473.79 |  | 474.1319 | -0.0721 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 219.5 |  | 220.9588 | -0.6602 | 222.19 | 218.09 | 0.8018 | below_vwap | below_vwap,spread_too_wide |
| 8 | IWM | market_regime | 295.125 |  | 296.1386 | -0.3423 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ENTG | semiconductor_materials | 133.74 |  | 134.8801 | -0.8453 | 138.07 | 133.73 | 0.4337 | below_vwap | below_vwap,spread_too_wide |
| 11 | AMZN | cloud_ai_capex | 253.075 |  | 255.1331 | -0.8067 | 258.07 | 252.62 | 0.4149 | below_vwap | below_vwap,spread_too_wide |
| 12 | META | cloud_ai_capex | 667.94 |  | 671.3675 | -0.5105 | 680.09 | 667.1 | 0.1108 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 140.665 |  | 140.5212 | 0.1024 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 35.515 |  | 35.5004 | 0.0411 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low |
| 15 | SOXX | semiconductor_index | 528.05 |  | 533.8314 | -1.083 | 543.4 | 535.47 | 0.0492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 405.13 |  | 408.8229 | -0.9033 | 414.385 | 406.61 | 0.0666 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 388.77 |  | 394.6016 | -1.4779 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 705.89 |  | 709.3379 | -0.4861 | 713.55 | 708.25 | 0.0113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 375.81 |  | 379.8893 | -1.0738 | 386.58 | 378.53 | 0.2262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | MU | memory_hbm_storage | 845.975 |  | 857.0037 | -1.2869 | 887.1 | 866.765 | 1.2305 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.89 |  | 709.3379 | -0.4861 | 713.55 | 708.25 | 0.0113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.74 |  | 71.8012 | -1.478 | 73.09 | 71.45 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.085 |  | 207.3493 | -0.1275 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.48 |  | 399.5203 | 1.2414 | 398.69 | 392.2 | 0.0445 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.79 |  | 330.73 | 0.6229 | 328.98 | 326.885 | 0.0361 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 358.06 |  | 368.5505 | -2.8464 | 375.18 | 369.2 | 0.1759 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 495.37 |  | 503.8358 | -1.6803 | 518.33 | 507.62 | 0.8398 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.13 |  | 408.8229 | -0.9033 | 414.385 | 406.61 | 0.0666 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.05 |  | 533.8314 | -1.083 | 543.4 | 535.47 | 0.0492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.94 |  | 571.7363 | -0.8389 | 580.31 | 572.21 | 0.0406 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.81 |  | 379.8893 | -1.0738 | 386.58 | 378.53 | 0.2262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 845.975 |  | 857.0037 | -1.2869 | 887.1 | 866.765 | 1.2305 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.91 |  | 191.0006 | -1.6181 | 201.61 | 194.19 | 0.314 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 394.5 |  | 402.1734 | -1.908 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.095 |  | 45.79 | -1.5179 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.025 |  | 25.3166 | -1.1517 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.25 |  | 752.3079 | -0.2735 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.125 |  | 296.1386 | -0.3423 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.06 |  | 126.6246 | -0.4459 | 131.36 | 126.665 | 0.0555 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.085 |  | 73.3005 | -0.294 | 75.54 | 73.985 | 4.6521 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.11 |  | 293.3441 | -1.4434 | 300.385 | 293.64 | 1.3905 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 395.82 |  | 399.2627 | -0.8623 | 406.24 | 399.495 | 0.2147 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 628.17 |  | 631.2991 | -0.4957 | 640.25 | 631.005 | 0.1528 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1019.89 |  | 1027.286 | -0.72 | 1035.07 | 1021.09 | 0.151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 473.79 |  | 474.1319 | -0.0721 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.665 |  | 140.5212 | 0.1024 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.885 |  | 166.586 | 0.1795 | 169.91 | 165.6 | 0.1258 | watch_only | none |
| COHR | ai_networking_optical | 275.56 |  | 280.6602 | -1.8172 | 288.48 | 280.67 | 0.9617 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 699.44 |  | 708.3339 | -1.2556 | 737.175 | 720.21 | 2.705 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.77 |  | 394.6016 | -1.4779 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.22 |  | 101.2787 | -2.0327 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.55 |  | 323.4399 | -1.2027 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.065 |  | 1818.0344 | -1.3734 | 1823.13 | 1796.26 | 0.1099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 559.26 |  | 569.9668 | -1.8785 | 572.69 | 562.32 | 0.2289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 317.37 |  | 322.9134 | -1.7167 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.5 |  | 220.9588 | -0.6602 | 222.19 | 218.09 | 0.8018 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.29 |  | 326.6601 | -1.3378 | 332.49 | 326.685 | 4.6014 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 279.74 |  | 286.4696 | -2.3491 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.885 |  | 63.9252 | -1.6272 | 66.19 | 63.93 | 1.7651 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.68 |  | 51.7902 | -2.1437 | 52.72 | 51.735 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 133.74 |  | 134.8801 | -0.8453 | 138.07 | 133.73 | 0.4337 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 328 |  | 334.6433 | -1.9852 | 346.26 | 338 | 3.8506 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 518.66 |  | 515.1739 | 0.6767 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.38 |  | 294.9801 | 0.4746 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.325 |  | 26.7904 | -1.737 | 28.05 | 27.6 | 0.076 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.515 |  | 35.5004 | 0.0411 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low |
| CORZ | high_beta_ai_infrastructure | 21.035 |  | 21.2137 | -0.8426 | 22.18 | 21.78 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1410.54 |  | 1462.1313 | -3.5285 | 1549.47 | 1482.06 | 3.5447 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 460.69 |  | 473.7359 | -2.7538 | 498.04 | 480.14 | 0.254 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 745.93 |  | 764.4975 | -2.4287 | 797.155 | 768.7 | 3.373 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 253.075 |  | 255.1331 | -0.8067 | 258.07 | 252.62 | 0.4149 | below_vwap | below_vwap,spread_too_wide |
| META | cloud_ai_capex | 667.94 |  | 671.3675 | -0.5105 | 680.09 | 667.1 | 0.1108 | below_vwap | below_vwap |
| ARM | ai_accelerator | 256.62 |  | 257.2905 | -0.2606 | 265.96 | 258.1 | 3.8968 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.355 |  | 161.6665 | -3.2854 | 168.11 | 162.41 | 1.0425 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
