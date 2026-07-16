# Intraday State

- Generated at: `2026-07-17T00:04:56+08:00`
- Market time ET: `2026-07-16T12:04:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 17, 'watch_only': 3, 'manual_confirm_candidate': 2, 'below_opening_15m_low': 29, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.56 |  | 710.4807 | -0.1296 | 713.55 | 708.25 | 0.0056 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 532.38 |  | 537.2655 | -0.9093 | 543.4 | 535.47 | 0.0826 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 571.2 |  | 575.1678 | -0.6899 | 580.31 | 572.21 | 0.0525 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.3 |  | 752.8751 | 0.0564 | 753.51 | 751.13 | 0.0265 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.42 |  | 396.3588 | 1.0246 | 398.69 | 392.2 | 0.1324 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.575 |  | 329.7149 | 0.5642 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 207.88 |  | 207.6342 | 0.1184 | 211.03 | 207.49 | 0.1395 | watch_only | none |
| 2 | SPY | market_regime | 753.3 |  | 752.8751 | 0.0564 | 753.51 | 751.13 | 0.0265 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 331.575 |  | 329.7149 | 0.5642 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 256.39 |  | 255.3127 | 0.4219 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 400.42 |  | 396.3588 | 1.0246 | 398.69 | 392.2 | 0.1324 | buy_precheck_manual_confirm | none |
| 6 | LIN | industrial_gases | 517.095 |  | 514.6376 | 0.4775 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ANET | ai_networking_optical | 166.99 |  | 166.3052 | 0.4118 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 296.595 |  | 294.5735 | 0.6862 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | IWM | market_regime | 296.53 |  | 296.6118 | -0.0276 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 709.56 |  | 710.4807 | -0.1296 | 713.55 | 708.25 | 0.0056 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1815.995 |  | 1825.3491 | -0.5125 | 1823.13 | 1796.26 | 0.0809 | below_vwap | below_vwap |
| 12 | TT | data_center_power_cooling | 474.27 |  | 474.4239 | -0.0324 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | SKHY | memory_hbm_storage | 163.02 |  | 163.5847 | -0.3452 | 168.11 | 162.41 | 0.0061 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 673.19 |  | 674.9995 | -0.2681 | 680.09 | 667.1 | 0.0966 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | TSM | foundry | 408.695 |  | 411.1434 | -0.5955 | 414.385 | 406.61 | 0.1541 | below_vwap | below_vwap |
| 17 | KLAC | semiconductor_equipment | 220.54 |  | 222.7004 | -0.9701 | 222.19 | 218.09 | 0.1904 | below_vwap | below_vwap |
| 18 | JCI | data_center_power_cooling | 140.4 |  | 140.6762 | -0.1964 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ONTO | semiconductor_test_packaging | 289.445 |  | 290.6257 | -0.4062 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 134.92 |  | 135.9508 | -0.7582 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.42 |  | 396.3588 | 1.0246 | 398.69 | 392.2 | 0.1324 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.575 |  | 329.7149 | 0.5642 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.27 |  | 474.4239 | -0.0324 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 4 | IWM | market_regime | 296.53 |  | 296.6118 | -0.0276 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 5 | LIN | industrial_gases | 517.095 |  | 514.6376 | 0.4775 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.595 |  | 294.5735 | 0.6862 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | NVDA | ai_accelerator | 207.88 |  | 207.6342 | 0.1184 | 211.03 | 207.49 | 0.1395 | watch_only | none |
| 8 | SPY | market_regime | 753.3 |  | 752.8751 | 0.0564 | 753.51 | 751.13 | 0.0265 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 256.39 |  | 255.3127 | 0.4219 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| 10 | TSM | foundry | 408.695 |  | 411.1434 | -0.5955 | 414.385 | 406.61 | 0.1541 | below_vwap | below_vwap |
| 11 | QQQ | market_regime | 709.56 |  | 710.4807 | -0.1296 | 713.55 | 708.25 | 0.0056 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 380.66 |  | 381.8436 | -0.31 | 386.58 | 378.53 | 1.2478 | below_vwap | below_vwap,spread_too_wide |
| 13 | JCI | data_center_power_cooling | 140.4 |  | 140.6762 | -0.1964 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1032.05 |  | 1032.57 | -0.0504 | 1035.07 | 1021.09 | 3.6539 | below_vwap | below_vwap,spread_too_wide |
| 15 | ASML | semiconductor_equipment | 1815.995 |  | 1825.3491 | -0.5125 | 1823.13 | 1796.26 | 0.0809 | below_vwap | below_vwap |
| 16 | AMAT | semiconductor_equipment | 570.03 |  | 574.6467 | -0.8034 | 572.69 | 562.32 | 1.1385 | below_vwap | below_vwap,spread_too_wide |
| 17 | ONTO | semiconductor_test_packaging | 289.445 |  | 290.6257 | -0.4062 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 220.54 |  | 222.7004 | -0.9701 | 222.19 | 218.09 | 0.1904 | below_vwap | below_vwap |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 134.92 |  | 135.9508 | -0.7582 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.56 |  | 710.4807 | -0.1296 | 713.55 | 708.25 | 0.0056 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.83 |  | 72.1917 | -0.501 | 73.09 | 71.45 | 0.0278 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.88 |  | 207.6342 | 0.1184 | 211.03 | 207.49 | 0.1395 | watch_only | none |
| MSFT | cloud_ai_capex | 400.42 |  | 396.3588 | 1.0246 | 398.69 | 392.2 | 0.1324 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.575 |  | 329.7149 | 0.5642 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.16 |  | 371.9705 | -0.2179 | 375.18 | 369.2 | 0.4176 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 504.975 |  | 510.0447 | -0.994 | 518.33 | 507.62 | 0.3267 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 408.695 |  | 411.1434 | -0.5955 | 414.385 | 406.61 | 0.1541 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 532.38 |  | 537.2655 | -0.9093 | 543.4 | 535.47 | 0.0826 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 571.2 |  | 575.1678 | -0.6899 | 580.31 | 572.21 | 0.0525 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.66 |  | 381.8436 | -0.31 | 386.58 | 378.53 | 1.2478 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 852.52 |  | 863.4545 | -1.2664 | 887.1 | 866.765 | 1.3994 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 189.32 |  | 193.4406 | -2.1301 | 201.61 | 194.19 | 0.2113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 400.01 |  | 404.524 | -1.1159 | 411.65 | 400.635 | 4.5699 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.58 |  | 46.1973 | -1.3363 | 47.65 | 46.165 | 0.0219 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.18 |  | 25.6619 | -1.878 | 26.71 | 25.74 | 0.0397 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.3 |  | 752.8751 | 0.0564 | 753.51 | 751.13 | 0.0265 | watch_only | none |
| IWM | market_regime | 296.53 |  | 296.6118 | -0.0276 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.005 |  | 127.0127 | -0.7934 | 131.36 | 126.665 | 3.9681 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.695 |  | 73.7164 | -1.3856 | 75.54 | 73.985 | 1.8708 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 292.82 |  | 296.0944 | -1.1059 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.41 |  | 401.0915 | -1.4165 | 406.24 | 399.495 | 4.4182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 630.395 |  | 633.0978 | -0.4269 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1032.05 |  | 1032.57 | -0.0504 | 1035.07 | 1021.09 | 3.6539 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.27 |  | 474.4239 | -0.0324 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.4 |  | 140.6762 | -0.1964 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.99 |  | 166.3052 | 0.4118 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 279.14 |  | 283.5494 | -1.5551 | 288.48 | 280.67 | 1.6658 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 704.55 |  | 714.4887 | -1.391 | 737.175 | 720.21 | 3.625 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.04 |  | 397.7396 | -0.6787 | 410 | 397.68 | 4.6907 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 100.66 |  | 102.9597 | -2.2336 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.51 |  | 326.8072 | -2.5389 | 337.59 | 326.16 | 3.5697 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1815.995 |  | 1825.3491 | -0.5125 | 1823.13 | 1796.26 | 0.0809 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 570.03 |  | 574.6467 | -0.8034 | 572.69 | 562.32 | 1.1385 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 322.42 |  | 326.7068 | -1.3121 | 328.96 | 324.11 | 0.2109 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 220.54 |  | 222.7004 | -0.9701 | 222.19 | 218.09 | 0.1904 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 325.885 |  | 328.8752 | -0.9092 | 332.49 | 326.685 | 0.491 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 289.445 |  | 290.6257 | -0.4062 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.85 |  | 64.5615 | -1.1021 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.25 |  | 52.6601 | -0.7788 | 52.72 | 51.735 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.92 |  | 135.9508 | -0.7582 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 337 |  | 340.5565 | -1.0443 | 346.26 | 338 | 4.2789 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 517.095 |  | 514.6376 | 0.4775 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.595 |  | 294.5735 | 0.6862 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.4 |  | 27.2693 | -3.1878 | 28.05 | 27.6 | 0.0758 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.97 |  | 35.9196 | -2.6436 | 37.365 | 36.4 | 0.0572 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.05 |  | 21.4929 | -2.0607 | 22.18 | 21.78 | 0.095 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1438.8 |  | 1484.9191 | -3.1058 | 1549.47 | 1482.06 | 4.1701 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 467.9 |  | 481.2675 | -2.7776 | 498.04 | 480.14 | 0.2672 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 756.6 |  | 772.6118 | -2.0724 | 797.155 | 768.7 | 4.2096 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.39 |  | 255.3127 | 0.4219 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| META | cloud_ai_capex | 673.19 |  | 674.9995 | -0.2681 | 680.09 | 667.1 | 0.0966 | below_vwap | below_vwap |
| ARM | ai_accelerator | 255.635 |  | 258.4066 | -1.0726 | 265.96 | 258.1 | 3.9118 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 163.02 |  | 163.5847 | -0.3452 | 168.11 | 162.41 | 0.0061 | below_vwap | below_vwap |
