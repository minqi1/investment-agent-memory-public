# Intraday State

- Generated at: `2026-07-16T21:59:07+08:00`
- Market time ET: `2026-07-16T09:59:08-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 25, 'below_vwap': 21, 'manual_confirm_candidate': 1, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.11 |  | 709.5739 | -0.2063 | 713.55 | 708.25 | 0.0113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 534.32 |  | 537.2718 | -0.5494 | 543.4 | 535.47 | 0.0861 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 571.63 |  | 574.9082 | -0.5702 | 580.31 | 572.21 | 0.0962 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.46 |  | 751.8428 | -0.0509 | 753.51 | 751.13 | 0.1025 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.08 |  | 328.5292 | 0.472 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.08 |  | 328.5292 | 0.472 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.11 |  | 295.9445 | 0.0559 | 296.28 | 294.65 | 0.0068 | watch_only | none |
| 3 | COHR | ai_networking_optical | 285.42 |  | 284.1298 | 0.4541 | 288.48 | 280.67 | 0.3013 | watch_only | none |
| 4 | JCI | data_center_power_cooling | 140.34 |  | 139.9961 | 0.2456 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ENTG | semiconductor_materials | 134.84 |  | 134.4652 | 0.2787 | 135.04 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | COHU | semiconductor_test_packaging | 52.27 |  | 52.0472 | 0.428 | 52.27 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | AVGO | custom_silicon_networking | 380.955 |  | 380.6389 | 0.083 | 386.58 | 378.53 | 2.9216 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AMAT | semiconductor_equipment | 568.925 |  | 568.4286 | 0.0873 | 572.69 | 562.32 | 4.1042 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TT | data_center_power_cooling | 472.785 |  | 471.0869 | 0.3605 | 474.085 | 467.64 | 0.9307 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | KLAC | semiconductor_equipment | 219.71 |  | 220.3629 | -0.2963 | 222.19 | 218.09 | 0.1047 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 751.46 |  | 751.8428 | -0.0509 | 753.51 | 751.13 | 0.1025 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 254.37 |  | 254.8968 | -0.2067 | 258.07 | 252.62 | 0.0511 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | HPE | ai_server_oem | 46.32 |  | 46.8851 | -1.2054 | 47.65 | 46.165 | 0.3454 | below_vwap | below_vwap |
| 15 | APD | industrial_gases | 291.45 |  | 292.5063 | -0.3611 | 293.89 | 291.35 | 0.2127 | below_vwap | below_vwap |
| 16 | ONTO | semiconductor_test_packaging | 287.42 |  | 288.6302 | -0.4193 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 370.985 |  | 371.7671 | -0.2104 | 375.18 | 369.2 | 0.2156 | below_vwap | below_vwap |
| 18 | ETN | data_center_power_cooling | 401.635 |  | 401.7349 | -0.0249 | 406.24 | 399.495 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | MKSI | semiconductor_materials | 339.28 |  | 340.1256 | -0.2486 | 342.45 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 512.89 |  | 514.0971 | -0.2348 | 515.825 | 512.23 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.08 |  | 328.5292 | 0.472 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |
| 2 | COHU | semiconductor_test_packaging | 52.27 |  | 52.0472 | 0.428 | 52.27 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | IWM | market_regime | 296.11 |  | 295.9445 | 0.0559 | 296.28 | 294.65 | 0.0068 | watch_only | none |
| 4 | COHR | ai_networking_optical | 285.42 |  | 284.1298 | 0.4541 | 288.48 | 280.67 | 0.3013 | watch_only | none |
| 5 | ANET | ai_networking_optical | 165.77 |  | 166.5329 | -0.4581 | 169.91 | 165.6 | 3.8246 | below_vwap | below_vwap,spread_too_wide |
| 6 | TSM | foundry | 408.72 |  | 410.0909 | -0.3343 | 414.385 | 406.61 | 1.7959 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1801.66 |  | 1807.7112 | -0.3347 | 1823.13 | 1796.26 | 0.7243 | below_vwap | below_vwap,spread_too_wide |
| 8 | ONTO | semiconductor_test_packaging | 287.42 |  | 288.6302 | -0.4193 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 401.635 |  | 401.7349 | -0.0249 | 406.24 | 399.495 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | KLAC | semiconductor_equipment | 219.71 |  | 220.3629 | -0.2963 | 222.19 | 218.09 | 0.1047 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 751.46 |  | 751.8428 | -0.0509 | 753.51 | 751.13 | 0.1025 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | MKSI | semiconductor_materials | 339.28 |  | 340.1256 | -0.2486 | 342.45 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LIN | industrial_gases | 512.89 |  | 514.0971 | -0.2348 | 515.825 | 512.23 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | HPE | ai_server_oem | 46.32 |  | 46.8851 | -1.2054 | 47.65 | 46.165 | 0.3454 | below_vwap | below_vwap |
| 16 | APD | industrial_gases | 291.45 |  | 292.5063 | -0.3611 | 293.89 | 291.35 | 0.2127 | below_vwap | below_vwap |
| 17 | ALAB | ai_networking_optical | 327.725 |  | 328.929 | -0.366 | 337.59 | 326.16 | 4.1864 | below_vwap | below_vwap,spread_too_wide |
| 18 | MSFT | cloud_ai_capex | 395.28 |  | 395.5819 | -0.0763 | 398.69 | 392.2 | 1.0271 | below_vwap | below_vwap,spread_too_wide |
| 19 | ARM | ai_accelerator | 258.845 |  | 260.09 | -0.4787 | 265.96 | 258.1 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ORCL | cloud_ai_capex | 127.51 |  | 127.6601 | -0.1175 | 131.36 | 126.665 | 1.5685 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.11 |  | 709.5739 | -0.2063 | 713.55 | 708.25 | 0.0113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.39 |  | 72.01 | -0.861 | 73.09 | 71.45 | 0.042 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.46 |  | 208.5928 | -0.5431 | 211.03 | 207.49 | 0.2699 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 395.28 |  | 395.5819 | -0.0763 | 398.69 | 392.2 | 1.0271 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 330.08 |  | 328.5292 | 0.472 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.985 |  | 371.7671 | -0.2104 | 375.18 | 369.2 | 0.2156 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.48 |  | 511.8355 | -0.851 | 518.33 | 507.62 | 2.54 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 408.72 |  | 410.0909 | -0.3343 | 414.385 | 406.61 | 1.7959 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.32 |  | 537.2718 | -0.5494 | 543.4 | 535.47 | 0.0861 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 571.63 |  | 574.9082 | -0.5702 | 580.31 | 572.21 | 0.0962 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.955 |  | 380.6389 | 0.083 | 386.58 | 378.53 | 2.9216 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 859.16 |  | 865.1795 | -0.6958 | 887.1 | 866.765 | 0.831 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 193.25 |  | 195.3999 | -1.1002 | 201.61 | 194.19 | 2.9082 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 398.495 |  | 402.704 | -1.0452 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.32 |  | 46.8851 | -1.2054 | 47.65 | 46.165 | 0.3454 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.73 |  | 25.9775 | -0.9529 | 26.71 | 25.74 | 0.0777 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.46 |  | 751.8428 | -0.0509 | 753.51 | 751.13 | 0.1025 | below_vwap | below_vwap |
| IWM | market_regime | 296.11 |  | 295.9445 | 0.0559 | 296.28 | 294.65 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 127.51 |  | 127.6601 | -0.1175 | 131.36 | 126.665 | 1.5685 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.18 |  | 74.2164 | -1.3965 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 293.475 |  | 294.5558 | -0.3669 | 300.385 | 293.64 | 4.8624 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 401.635 |  | 401.7349 | -0.0249 | 406.24 | 399.495 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 630.11 |  | 632.265 | -0.3408 | 640.25 | 631.005 | 0.9808 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1020.66 |  | 1024.7565 | -0.3998 | 1035.07 | 1021.09 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 472.785 |  | 471.0869 | 0.3605 | 474.085 | 467.64 | 0.9307 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.34 |  | 139.9961 | 0.2456 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.77 |  | 166.5329 | -0.4581 | 169.91 | 165.6 | 3.8246 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 285.42 |  | 284.1298 | 0.4541 | 288.48 | 280.67 | 0.3013 | watch_only | none |
| LITE | ai_networking_optical | 715.23 |  | 721.5849 | -0.8807 | 737.175 | 720.21 | 5.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 396.11 |  | 401.8091 | -1.4183 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.44 |  | 103.8875 | -2.3559 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.725 |  | 328.929 | -0.366 | 337.59 | 326.16 | 4.1864 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1801.66 |  | 1807.7112 | -0.3347 | 1823.13 | 1796.26 | 0.7243 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 568.925 |  | 568.4286 | 0.0873 | 572.69 | 562.32 | 4.1042 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 323.38 |  | 325.3492 | -0.6053 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.71 |  | 220.3629 | -0.2963 | 222.19 | 218.09 | 0.1047 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 324.715 |  | 326.6697 | -0.5984 | 332.49 | 326.685 | 0.2648 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ONTO | semiconductor_test_packaging | 287.42 |  | 288.6302 | -0.4193 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.12 |  | 64.8879 | -1.1834 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.27 |  | 52.0472 | 0.428 | 52.27 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 134.84 |  | 134.4652 | 0.2787 | 135.04 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 339.28 |  | 340.1256 | -0.2486 | 342.45 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 512.89 |  | 514.0971 | -0.2348 | 515.825 | 512.23 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 291.45 |  | 292.5063 | -0.3611 | 293.89 | 291.35 | 0.2127 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 27.25 |  | 27.557 | -1.1141 | 28.05 | 27.6 | 0.1468 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.91 |  | 36.6143 | -1.9236 | 37.365 | 36.4 | 0.1114 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.48 |  | 21.7862 | -1.4055 | 22.18 | 21.78 | 0.1862 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1477.5 |  | 1498.8093 | -1.4217 | 1549.47 | 1482.06 | 3.1479 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 478.68 |  | 482.6143 | -0.8152 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 765.6 |  | 774.902 | -1.2004 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.37 |  | 254.8968 | -0.2067 | 258.07 | 252.62 | 0.0511 | below_vwap | below_vwap |
| META | cloud_ai_capex | 671.82 |  | 672.6439 | -0.1225 | 680.09 | 667.1 | 0.7591 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.845 |  | 260.09 | -0.4787 | 265.96 | 258.1 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 162.645 |  | 164.9421 | -1.3927 | 168.11 | 162.41 | 2.7053 | below_vwap | below_vwap,spread_too_wide |
