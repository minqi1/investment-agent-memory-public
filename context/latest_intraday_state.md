# Intraday State

- Generated at: `2026-07-16T23:14:44+08:00`
- Market time ET: `2026-07-16T11:14:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'below_opening_15m_low': 25, 'spread_too_wide_or_missing': 7, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.22 |  | 710.568 | -0.1897 | 713.55 | 708.25 | 0.0381 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 533.08 |  | 537.9395 | -0.9034 | 543.4 | 535.47 | 0.0675 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 570.66 |  | 575.8718 | -0.905 | 580.31 | 572.21 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.22 |  | 752.7023 | 0.0688 | 753.51 | 751.13 | 0.0146 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.685 |  | 296.5889 | 0.0324 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.57 |  | 329.2828 | 0.3909 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.685 |  | 296.5889 | 0.0324 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.22 |  | 752.7023 | 0.0688 | 753.51 | 751.13 | 0.0146 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 330.57 |  | 329.2828 | 0.3909 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.67 |  | 255.1879 | 0.1889 | 258.07 | 252.62 | 0.0274 | watch_only | none |
| 5 | JCI | data_center_power_cooling | 140.7 |  | 140.6886 | 0.0081 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TT | data_center_power_cooling | 475.34 |  | 474.1366 | 0.2538 | 474.085 | 467.64 | 4.866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 517.115 |  | 513.6458 | 0.6754 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 1037.22 |  | 1032.2322 | 0.4832 | 1035.07 | 1021.09 | 3.2414 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MSFT | cloud_ai_capex | 397.895 |  | 395.5481 | 0.5933 | 398.69 | 392.2 | 0.3845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | META | cloud_ai_capex | 678.855 |  | 674.7513 | 0.6082 | 680.09 | 667.1 | 1.2609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 409.54 |  | 411.4445 | -0.4629 | 414.385 | 406.61 | 0.0464 | below_vwap | below_vwap |
| 12 | APD | industrial_gases | 296.4 |  | 292.9409 | 1.1808 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | QQQ | market_regime | 709.22 |  | 710.568 | -0.1897 | 713.55 | 708.25 | 0.0381 | below_vwap | below_vwap |
| 14 | PWR | data_center_power_cooling | 632.5 |  | 633.6239 | -0.1774 | 640.25 | 631.005 | 0.1423 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 288.37 |  | 290.6202 | -0.7743 | 295.83 | 285.02 | 0.3329 | below_vwap | below_vwap |
| 17 | STX | memory_hbm_storage | 769.06 |  | 778.3423 | -1.1926 | 797.155 | 768.7 | 0.3368 | below_vwap | below_vwap |
| 18 | ORCL | cloud_ai_capex | 126.945 |  | 127.1487 | -0.1602 | 131.36 | 126.665 | 0.2048 | below_vwap | below_vwap |
| 19 | MKSI | semiconductor_materials | 341.29 |  | 341.362 | -0.0211 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 135.665 |  | 135.9818 | -0.233 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.685 |  | 296.5889 | 0.0324 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.57 |  | 329.2828 | 0.3909 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.34 |  | 474.1366 | 0.2538 | 474.085 | 467.64 | 4.866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | GEV | data_center_power_cooling | 1037.22 |  | 1032.2322 | 0.4832 | 1035.07 | 1021.09 | 3.2414 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | LIN | industrial_gases | 517.115 |  | 513.6458 | 0.6754 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.4 |  | 292.9409 | 1.1808 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SPY | market_regime | 753.22 |  | 752.7023 | 0.0688 | 753.51 | 751.13 | 0.0146 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 255.67 |  | 255.1879 | 0.1889 | 258.07 | 252.62 | 0.0274 | watch_only | none |
| 9 | TSM | foundry | 409.54 |  | 411.4445 | -0.4629 | 414.385 | 406.61 | 0.0464 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 709.22 |  | 710.568 | -0.1897 | 713.55 | 708.25 | 0.0381 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 379.64 |  | 382.0187 | -0.6227 | 386.58 | 378.53 | 0.8903 | below_vwap | below_vwap,spread_too_wide |
| 12 | VRT | data_center_power_cooling | 293.705 |  | 296.6698 | -0.9993 | 300.385 | 293.64 | 3.0541 | below_vwap | below_vwap,spread_too_wide |
| 13 | PWR | data_center_power_cooling | 632.5 |  | 633.6239 | -0.1774 | 640.25 | 631.005 | 0.1423 | below_vwap | below_vwap |
| 14 | ASML | semiconductor_equipment | 1815.77 |  | 1826.6732 | -0.5969 | 1823.13 | 1796.26 | 0.6906 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMAT | semiconductor_equipment | 571.385 |  | 575.6091 | -0.7339 | 572.69 | 562.32 | 0.6791 | below_vwap | below_vwap,spread_too_wide |
| 16 | ONTO | semiconductor_test_packaging | 288.37 |  | 290.6202 | -0.7743 | 295.83 | 285.02 | 0.3329 | below_vwap | below_vwap |
| 17 | KLAC | semiconductor_equipment | 220.96 |  | 222.9325 | -0.8848 | 222.19 | 218.09 | 4.055 | below_vwap | below_vwap,spread_too_wide |
| 18 | STX | memory_hbm_storage | 769.06 |  | 778.3423 | -1.1926 | 797.155 | 768.7 | 0.3368 | below_vwap | below_vwap |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | MKSI | semiconductor_materials | 341.29 |  | 341.362 | -0.0211 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.22 |  | 710.568 | -0.1897 | 713.55 | 708.25 | 0.0381 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.725 |  | 72.2063 | -0.6666 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 205.955 |  | 207.8403 | -0.9071 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 397.895 |  | 395.5481 | 0.5933 | 398.69 | 392.2 | 0.3845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 330.57 |  | 329.2828 | 0.3909 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.665 |  | 372.0473 | -0.1028 | 375.18 | 369.2 | 0.4978 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 505.73 |  | 510.7239 | -0.9778 | 518.33 | 507.62 | 0.1681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 409.54 |  | 411.4445 | -0.4629 | 414.385 | 406.61 | 0.0464 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 533.08 |  | 537.9395 | -0.9034 | 543.4 | 535.47 | 0.0675 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 570.66 |  | 575.8718 | -0.905 | 580.31 | 572.21 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.64 |  | 382.0187 | -0.6227 | 386.58 | 378.53 | 0.8903 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 854.63 |  | 866.2306 | -1.3392 | 887.1 | 866.765 | 0.2726 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 189.95 |  | 194.4881 | -2.3333 | 201.61 | 194.19 | 0.7212 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.69 |  | 405.2826 | -1.3799 | 411.65 | 400.635 | 4.4359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.48 |  | 46.4883 | -2.1689 | 47.65 | 46.165 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.355 |  | 25.8219 | -1.8081 | 26.71 | 25.74 | 0.0394 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.22 |  | 752.7023 | 0.0688 | 753.51 | 751.13 | 0.0146 | watch_only | none |
| IWM | market_regime | 296.685 |  | 296.5889 | 0.0324 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.945 |  | 127.1487 | -0.1602 | 131.36 | 126.665 | 0.2048 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.15 |  | 74.0024 | -1.1519 | 75.54 | 73.985 | 0.4101 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.705 |  | 296.6698 | -0.9993 | 300.385 | 293.64 | 3.0541 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.15 |  | 401.8278 | -1.413 | 406.24 | 399.495 | 0.2348 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 632.5 |  | 633.6239 | -0.1774 | 640.25 | 631.005 | 0.1423 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1037.22 |  | 1032.2322 | 0.4832 | 1035.07 | 1021.09 | 3.2414 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.34 |  | 474.1366 | 0.2538 | 474.085 | 467.64 | 4.866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.7 |  | 140.6886 | 0.0081 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164 |  | 166.2887 | -1.3763 | 169.91 | 165.6 | 3.8659 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 277.08 |  | 284.3048 | -2.5412 | 288.48 | 280.67 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 709.44 |  | 720.7441 | -1.5684 | 737.175 | 720.21 | 0.1508 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 392.895 |  | 398.9017 | -1.5058 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.58 |  | 103.4408 | -2.7656 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 322.66 |  | 329.2082 | -1.9891 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1815.77 |  | 1826.6732 | -0.5969 | 1823.13 | 1796.26 | 0.6906 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 571.385 |  | 575.6091 | -0.7339 | 572.69 | 562.32 | 0.6791 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 324.05 |  | 327.5208 | -1.0597 | 328.96 | 324.11 | 4.2031 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 220.96 |  | 222.9325 | -0.8848 | 222.19 | 218.09 | 4.055 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 328.865 |  | 328.9124 | -0.0144 | 332.49 | 326.685 | 0.7906 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 288.37 |  | 290.6202 | -0.7743 | 295.83 | 285.02 | 0.3329 | below_vwap | below_vwap |
| AMKR | semiconductor_test_packaging | 63.97 |  | 64.6789 | -1.096 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.57 |  | 52.6746 | -0.1987 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.665 |  | 135.9818 | -0.233 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.29 |  | 341.362 | -0.0211 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.115 |  | 513.6458 | 0.6754 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.4 |  | 292.9409 | 1.1808 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.88 |  | 27.4404 | -2.0422 | 28.05 | 27.6 | 0.0744 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.235 |  | 36.1277 | -2.471 | 37.365 | 36.4 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.205 |  | 21.5784 | -1.7304 | 22.18 | 21.78 | 0.1415 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1459.02 |  | 1496.9501 | -2.5338 | 1549.47 | 1482.06 | 3.7011 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 475.42 |  | 483.8571 | -1.7437 | 498.04 | 480.14 | 1.8931 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 769.06 |  | 778.3423 | -1.1926 | 797.155 | 768.7 | 0.3368 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 255.67 |  | 255.1879 | 0.1889 | 258.07 | 252.62 | 0.0274 | watch_only | none |
| META | cloud_ai_capex | 678.855 |  | 674.7513 | 0.6082 | 680.09 | 667.1 | 1.2609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 255.12 |  | 259.0347 | -1.5113 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.65 |  | 164.2743 | -2.2063 | 168.11 | 162.41 | 2.4899 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
