# Intraday State

- Generated at: `2026-07-17T02:43:36+08:00`
- Market time ET: `2026-07-16T14:43:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 6, 'watch_only': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.155 |  | 709.4007 | -0.4575 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.78 |  | 533.8884 | -1.1441 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.8 |  | 571.8617 | -0.8851 | 580.31 | 572.21 | 0.0388 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.44 |  | 752.3726 | -0.2569 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.04 |  | 399.3561 | 1.1729 | 398.69 | 392.2 | 0.1114 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.92 |  | 330.6283 | 0.3907 | 328.98 | 326.885 | 0.0241 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.54 |  | 140.5167 | 0.0166 | 140.83 | 139.43 | 0.064 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 331.92 |  | 330.6283 | 0.3907 | 328.98 | 326.885 | 0.0241 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 404.04 |  | 399.3561 | 1.1729 | 398.69 | 392.2 | 0.1114 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 518.15 |  | 515.1433 | 0.5837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 167.43 |  | 166.5776 | 0.5117 | 169.91 | 165.6 | 4.3003 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.395 |  | 294.9485 | 0.4904 | 293.89 | 291.35 | 0.9109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | IWM | market_regime | 295.215 |  | 296.1586 | -0.3186 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | TT | data_center_power_cooling | 473.24 |  | 474.1557 | -0.1931 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | META | cloud_ai_capex | 668.37 |  | 671.5888 | -0.4793 | 680.09 | 667.1 | 0.3336 | below_vwap | below_vwap |
| 11 | ENTG | semiconductor_materials | 133.82 |  | 134.961 | -0.8454 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 220.04 |  | 220.9915 | -0.4305 | 222.19 | 218.09 | 4.4037 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 527.78 |  | 533.8884 | -1.1441 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | QQQ | market_regime | 706.155 |  | 709.4007 | -0.4575 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | NVDA | ai_accelerator | 206.755 |  | 207.354 | -0.2889 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | ASML | semiconductor_equipment | 1794.16 |  | 1818.3807 | -1.332 | 1823.13 | 1796.26 | 0.1499 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | SMH | semiconductor_index | 566.8 |  | 571.8617 | -0.8851 | 580.31 | 572.21 | 0.0388 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SPY | market_regime | 750.44 |  | 752.3726 | -0.2569 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | HPE | ai_server_oem | 45.415 |  | 45.8035 | -0.8483 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | GOOGL | cloud_ai_capex | 359.92 |  | 368.9177 | -2.4389 | 375.18 | 369.2 | 0.1473 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.04 |  | 399.3561 | 1.1729 | 398.69 | 392.2 | 0.1114 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.92 |  | 330.6283 | 0.3907 | 328.98 | 326.885 | 0.0241 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.15 |  | 515.1433 | 0.5837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.395 |  | 294.9485 | 0.4904 | 293.89 | 291.35 | 0.9109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | JCI | data_center_power_cooling | 140.54 |  | 140.5167 | 0.0166 | 140.83 | 139.43 | 0.064 | watch_only | none |
| 6 | TT | data_center_power_cooling | 473.24 |  | 474.1557 | -0.1931 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 220.04 |  | 220.9915 | -0.4305 | 222.19 | 218.09 | 4.4037 | below_vwap | below_vwap,spread_too_wide |
| 8 | IWM | market_regime | 295.215 |  | 296.1586 | -0.3186 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ENTG | semiconductor_materials | 133.82 |  | 134.961 | -0.8454 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | META | cloud_ai_capex | 668.37 |  | 671.5888 | -0.4793 | 680.09 | 667.1 | 0.3336 | below_vwap | below_vwap |
| 12 | ANET | ai_networking_optical | 167.43 |  | 166.5776 | 0.5117 | 169.91 | 165.6 | 4.3003 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SOXX | semiconductor_index | 527.78 |  | 533.8884 | -1.1441 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 405.13 |  | 408.906 | -0.9234 | 414.385 | 406.61 | 0.4246 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 15 | CIEN | ai_networking_optical | 390.21 |  | 394.8053 | -1.1639 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 706.155 |  | 709.4007 | -0.4575 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 376.115 |  | 379.9836 | -1.0181 | 386.58 | 378.53 | 0.4919 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | MU | memory_hbm_storage | 848.24 |  | 857.3388 | -1.0613 | 887.1 | 866.765 | 1.5668 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 289.51 |  | 293.3967 | -1.3247 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 20 | NVDA | ai_accelerator | 206.755 |  | 207.354 | -0.2889 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.155 |  | 709.4007 | -0.4575 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.79 |  | 71.8222 | -1.4372 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.755 |  | 207.354 | -0.2889 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.04 |  | 399.3561 | 1.1729 | 398.69 | 392.2 | 0.1114 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.92 |  | 330.6283 | 0.3907 | 328.98 | 326.885 | 0.0241 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 359.92 |  | 368.9177 | -2.4389 | 375.18 | 369.2 | 0.1473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 495.105 |  | 504.1 | -1.7844 | 518.33 | 507.62 | 1.3532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.13 |  | 408.906 | -0.9234 | 414.385 | 406.61 | 0.4246 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.78 |  | 533.8884 | -1.1441 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.8 |  | 571.8617 | -0.8851 | 580.31 | 572.21 | 0.0388 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.115 |  | 379.9836 | -1.0181 | 386.58 | 378.53 | 0.4919 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.24 |  | 857.3388 | -1.0613 | 887.1 | 866.765 | 1.5668 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.55 |  | 191.0738 | -1.8442 | 201.61 | 194.19 | 1.0024 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 396.865 |  | 402.313 | -1.3542 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.415 |  | 45.8035 | -0.8483 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.985 |  | 25.3293 | -1.3594 | 26.71 | 25.74 | 0.08 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.44 |  | 752.3726 | -0.2569 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.215 |  | 296.1586 | -0.3186 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.03 |  | 126.639 | -0.4809 | 131.36 | 126.665 | 3.2135 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.84 |  | 73.3054 | -0.6349 | 75.54 | 73.985 | 0.4942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.51 |  | 293.3967 | -1.3247 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.01 |  | 399.3222 | -1.0799 | 406.24 | 399.495 | 1.4 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 626.75 |  | 631.3873 | -0.7345 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1020.655 |  | 1027.4872 | -0.6649 | 1035.07 | 1021.09 | 2.5974 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.24 |  | 474.1557 | -0.1931 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.54 |  | 140.5167 | 0.0166 | 140.83 | 139.43 | 0.064 | watch_only | none |
| ANET | ai_networking_optical | 167.43 |  | 166.5776 | 0.5117 | 169.91 | 165.6 | 4.3003 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.07 |  | 280.7469 | -1.6659 | 288.48 | 280.67 | 0.9273 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 703.1 |  | 708.4701 | -0.758 | 737.175 | 720.21 | 2.57 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.21 |  | 394.8053 | -1.1639 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.05 |  | 101.3777 | -2.296 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.125 |  | 323.4987 | -1.0429 | 337.59 | 326.16 | 0.7872 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1794.16 |  | 1818.3807 | -1.332 | 1823.13 | 1796.26 | 0.1499 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.27 |  | 570.1503 | -1.7329 | 572.69 | 562.32 | 1.5457 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.58 |  | 322.9666 | -1.6679 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.04 |  | 220.9915 | -0.4305 | 222.19 | 218.09 | 4.4037 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.67 |  | 326.7216 | -1.2401 | 332.49 | 326.685 | 4.6797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 279.835 |  | 286.6211 | -2.3676 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.08 |  | 63.9609 | -1.3772 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.64 |  | 51.8298 | -2.2956 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.82 |  | 134.961 | -0.8454 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.72 |  | 334.9354 | -1.8557 | 346.26 | 338 | 4.2133 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 518.15 |  | 515.1433 | 0.5837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.395 |  | 294.9485 | 0.4904 | 293.89 | 291.35 | 0.9109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.07 |  | 26.8016 | -2.7297 | 28.05 | 27.6 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.185 |  | 35.5007 | -0.8893 | 37.365 | 36.4 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.94 |  | 21.2198 | -1.3186 | 22.18 | 21.78 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1419.29 |  | 1463.1295 | -2.9963 | 1549.47 | 1482.06 | 2.5365 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 462.04 |  | 474.125 | -2.5489 | 498.04 | 480.14 | 0.4588 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 747.44 |  | 765.3242 | -2.3368 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 252 |  | 255.2687 | -1.2805 | 258.07 | 252.62 | 0.0278 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 668.37 |  | 671.5888 | -0.4793 | 680.09 | 667.1 | 0.3336 | below_vwap | below_vwap |
| ARM | ai_accelerator | 256.85 |  | 257.2963 | -0.1734 | 265.96 | 258.1 | 3.8933 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.8 |  | 161.7287 | -3.0475 | 168.11 | 162.41 | 0.4592 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
