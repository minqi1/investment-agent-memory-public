# Intraday State

- Generated at: `2026-07-16T23:32:32+08:00`
- Market time ET: `2026-07-16T11:32:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 6, 'below_opening_15m_low': 20, 'manual_confirm_candidate': 5, 'below_vwap': 20, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.94 |  | 710.4772 | 0.0651 | 713.55 | 708.25 | 0.0675 | watch_only | none |
| SOXX | semiconductor_index | 535.68 |  | 537.6995 | -0.3756 | 543.4 | 535.47 | 0.056 | below_vwap | below_vwap |
| SMH | semiconductor_index | 573.81 |  | 575.6615 | -0.3216 | 580.31 | 572.21 | 0.0558 | below_vwap | below_vwap |
| SPY | market_regime | 754 |  | 752.7892 | 0.1608 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754 |  | 752.7892 | 0.1608 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.955 |  | 296.6094 | 0.1165 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.94 |  | 293.8277 | 1.0592 | 293.89 | 291.35 | 0.1515 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 398.83 |  | 395.8137 | 0.7621 | 398.69 | 392.2 | 0.1429 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 330.675 |  | 329.4372 | 0.3757 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754 |  | 752.7892 | 0.1608 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.955 |  | 296.6094 | 0.1165 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 398.83 |  | 395.8137 | 0.7621 | 398.69 | 392.2 | 0.1429 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 710.94 |  | 710.4772 | 0.0651 | 713.55 | 708.25 | 0.0675 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 330.675 |  | 329.4372 | 0.3757 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 255.52 |  | 255.2186 | 0.1181 | 258.07 | 252.62 | 0.0235 | watch_only | none |
| 7 | META | cloud_ai_capex | 676.59 |  | 674.907 | 0.2494 | 680.09 | 667.1 | 0.133 | watch_only | none |
| 8 | GEV | data_center_power_cooling | 1034.9 |  | 1032.8852 | 0.1951 | 1035.07 | 1021.09 | 0.1933 | watch_only | none |
| 9 | TER | semiconductor_test_packaging | 329.785 |  | 328.9925 | 0.2409 | 332.49 | 326.685 | 0.3426 | watch_only | none |
| 10 | TT | data_center_power_cooling | 475.05 |  | 474.3359 | 0.1505 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 140.74 |  | 140.7047 | 0.0251 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ENTG | semiconductor_materials | 136.13 |  | 135.9842 | 0.1072 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 296.94 |  | 293.8277 | 1.0592 | 293.89 | 291.35 | 0.1515 | buy_precheck_manual_confirm | none |
| 14 | LIN | industrial_gases | 517.26 |  | 514.0844 | 0.6177 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ASML | semiconductor_equipment | 1825.425 |  | 1825.7127 | -0.0158 | 1823.13 | 1796.26 | 0.0953 | below_vwap | below_vwap |
| 16 | SOXX | semiconductor_index | 535.68 |  | 537.6995 | -0.3756 | 543.4 | 535.47 | 0.056 | below_vwap | below_vwap |
| 17 | TSM | foundry | 411.21 |  | 411.3909 | -0.044 | 414.385 | 406.61 | 0.0486 | below_vwap | below_vwap |
| 18 | SMH | semiconductor_index | 573.81 |  | 575.6615 | -0.3216 | 580.31 | 572.21 | 0.0558 | below_vwap | below_vwap |
| 19 | AMAT | semiconductor_equipment | 573.37 |  | 575.3523 | -0.3445 | 572.69 | 562.32 | 0.2424 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754 |  | 752.7892 | 0.1608 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.955 |  | 296.6094 | 0.1165 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.94 |  | 293.8277 | 1.0592 | 293.89 | 291.35 | 0.1515 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 398.83 |  | 395.8137 | 0.7621 | 398.69 | 392.2 | 0.1429 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 330.675 |  | 329.4372 | 0.3757 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1825.425 |  | 1825.7127 | -0.0158 | 1823.13 | 1796.26 | 0.0953 | below_vwap | below_vwap |
| 7 | AMAT | semiconductor_equipment | 573.37 |  | 575.3523 | -0.3445 | 572.69 | 562.32 | 0.2424 | below_vwap | below_vwap |
| 8 | TT | data_center_power_cooling | 475.05 |  | 474.3359 | 0.1505 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | LIN | industrial_gases | 517.26 |  | 514.0844 | 0.6177 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | QQQ | market_regime | 710.94 |  | 710.4772 | 0.0651 | 713.55 | 708.25 | 0.0675 | watch_only | none |
| 11 | GEV | data_center_power_cooling | 1034.9 |  | 1032.8852 | 0.1951 | 1035.07 | 1021.09 | 0.1933 | watch_only | none |
| 12 | TER | semiconductor_test_packaging | 329.785 |  | 328.9925 | 0.2409 | 332.49 | 326.685 | 0.3426 | watch_only | none |
| 13 | AMZN | cloud_ai_capex | 255.52 |  | 255.2186 | 0.1181 | 258.07 | 252.62 | 0.0235 | watch_only | none |
| 14 | META | cloud_ai_capex | 676.59 |  | 674.907 | 0.2494 | 680.09 | 667.1 | 0.133 | watch_only | none |
| 15 | TQQQ | leveraged_tool | 72.29 |  | 72.1983 | 0.127 | 73.09 | 71.45 | 0.0277 | watch_only | none |
| 16 | ANET | ai_networking_optical | 165.71 |  | 166.2674 | -0.3352 | 169.91 | 165.6 | 3.826 | below_vwap | below_vwap,spread_too_wide |
| 17 | SOXX | semiconductor_index | 535.68 |  | 537.6995 | -0.3756 | 543.4 | 535.47 | 0.056 | below_vwap | below_vwap |
| 18 | TSM | foundry | 411.21 |  | 411.3909 | -0.044 | 414.385 | 406.61 | 0.0486 | below_vwap | below_vwap |
| 19 | AVGO | custom_silicon_networking | 381.395 |  | 381.8609 | -0.122 | 386.58 | 378.53 | 0.3382 | below_vwap | below_vwap |
| 20 | VRT | data_center_power_cooling | 294.21 |  | 296.4597 | -0.7589 | 300.385 | 293.64 | 3.3989 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.94 |  | 710.4772 | 0.0651 | 713.55 | 708.25 | 0.0675 | watch_only | none |
| TQQQ | leveraged_tool | 72.29 |  | 72.1983 | 0.127 | 73.09 | 71.45 | 0.0277 | watch_only | none |
| NVDA | ai_accelerator | 207.295 |  | 207.6499 | -0.1709 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.83 |  | 395.8137 | 0.7621 | 398.69 | 392.2 | 0.1429 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.675 |  | 329.4372 | 0.3757 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.54 |  | 372.0196 | -0.1289 | 375.18 | 369.2 | 0.2934 | below_vwap | below_vwap |
| AMD | ai_accelerator | 508.535 |  | 510.4685 | -0.3788 | 518.33 | 507.62 | 0.5644 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 411.21 |  | 411.3909 | -0.044 | 414.385 | 406.61 | 0.0486 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 535.68 |  | 537.6995 | -0.3756 | 543.4 | 535.47 | 0.056 | below_vwap | below_vwap |
| SMH | semiconductor_index | 573.81 |  | 575.6615 | -0.3216 | 580.31 | 572.21 | 0.0558 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.395 |  | 381.8609 | -0.122 | 386.58 | 378.53 | 0.3382 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 858.805 |  | 864.7949 | -0.6926 | 887.1 | 866.765 | 0.6544 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 191.79 |  | 193.9786 | -1.1283 | 201.61 | 194.19 | 0.2294 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 404.105 |  | 404.9924 | -0.2191 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.07 |  | 46.4034 | -0.7184 | 47.65 | 46.165 | 0.0217 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.39 |  | 25.7497 | -1.3969 | 26.71 | 25.74 | 0.0394 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754 |  | 752.7892 | 0.1608 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.955 |  | 296.6094 | 0.1165 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.99 |  | 127.1284 | -0.1089 | 131.36 | 126.665 | 3.268 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.425 |  | 73.9342 | -0.6887 | 75.54 | 73.985 | 0.0817 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 294.21 |  | 296.4597 | -0.7589 | 300.385 | 293.64 | 3.3989 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.445 |  | 401.6302 | -1.291 | 406.24 | 399.495 | 0.9434 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 631.99 |  | 633.2389 | -0.1972 | 640.25 | 631.005 | 2.2864 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1034.9 |  | 1032.8852 | 0.1951 | 1035.07 | 1021.09 | 0.1933 | watch_only | none |
| TT | data_center_power_cooling | 475.05 |  | 474.3359 | 0.1505 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.74 |  | 140.7047 | 0.0251 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.71 |  | 166.2674 | -0.3352 | 169.91 | 165.6 | 3.826 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 277.445 |  | 283.9758 | -2.2998 | 288.48 | 280.67 | 4.4117 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 706.645 |  | 717.24 | -1.4772 | 737.175 | 720.21 | 4.8242 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.97 |  | 398.5955 | -0.6587 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101 |  | 103.2323 | -2.1624 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.66 |  | 328.7103 | -1.2322 | 337.59 | 326.16 | 0.4435 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1825.425 |  | 1825.7127 | -0.0158 | 1823.13 | 1796.26 | 0.0953 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 573.37 |  | 575.3523 | -0.3445 | 572.69 | 562.32 | 0.2424 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 325.765 |  | 327.3193 | -0.4748 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.14 |  | 222.8319 | -0.3105 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 329.785 |  | 328.9925 | 0.2409 | 332.49 | 326.685 | 0.3426 | watch_only | none |
| ONTO | semiconductor_test_packaging | 290.375 |  | 290.5564 | -0.0624 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.465 |  | 64.6163 | -0.2341 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.59 |  | 52.6697 | -0.1514 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 136.13 |  | 135.9842 | 0.1072 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 340.79 |  | 341.2598 | -0.1377 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.26 |  | 514.0844 | 0.6177 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.94 |  | 293.8277 | 1.0592 | 293.89 | 291.35 | 0.1515 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.915 |  | 27.3848 | -1.7156 | 28.05 | 27.6 | 0.0743 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.74 |  | 36.0772 | -0.9347 | 37.365 | 36.4 | 0.056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.235 |  | 21.5601 | -1.5077 | 22.18 | 21.78 | 0.1413 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1463.165 |  | 1490.2728 | -1.819 | 1549.47 | 1482.06 | 3.7583 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 474.045 |  | 482.8324 | -1.82 | 498.04 | 480.14 | 3.0314 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 767.01 |  | 777.3435 | -1.3293 | 797.155 | 768.7 | 0.2568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 255.52 |  | 255.2186 | 0.1181 | 258.07 | 252.62 | 0.0235 | watch_only | none |
| META | cloud_ai_capex | 676.59 |  | 674.907 | 0.2494 | 680.09 | 667.1 | 0.133 | watch_only | none |
| ARM | ai_accelerator | 256.8 |  | 258.7353 | -0.748 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 162.36 |  | 163.8644 | -0.918 | 168.11 | 162.41 | 0.8869 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
