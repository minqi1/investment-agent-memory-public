# Intraday State

- Generated at: `2026-07-17T02:51:35+08:00`
- Market time ET: `2026-07-16T14:51:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 7, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.67 |  | 709.3685 | -0.3804 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.71 |  | 533.8533 | -0.9634 | 543.4 | 535.47 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.655 |  | 571.7568 | -0.7174 | 580.31 | 572.21 | 0.0652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.88 |  | 752.3281 | -0.1925 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.71 |  | 399.4671 | 1.3125 | 398.69 | 392.2 | 0.0741 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.82 |  | 330.6606 | 0.6531 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.82 |  | 330.6606 | 0.6531 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 140.72 |  | 140.5207 | 0.1418 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MSFT | cloud_ai_capex | 404.71 |  | 399.4671 | 1.3125 | 398.69 | 392.2 | 0.0741 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 518.195 |  | 515.1639 | 0.5884 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 296.56 |  | 294.9749 | 0.5374 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 167.38 |  | 166.5838 | 0.478 | 169.91 | 165.6 | 3.4831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | CRWV | gpu_cloud_ai_factory | 73.47 |  | 73.3025 | 0.2284 | 75.54 | 73.985 | 0.0544 | below_opening_15m_low | below_opening_15m_low |
| 8 | IREN | high_beta_ai_infrastructure | 35.6 |  | 35.4996 | 0.2827 | 37.365 | 36.4 | 0.0562 | below_opening_15m_low | below_opening_15m_low |
| 9 | KLAC | semiconductor_equipment | 220.29 |  | 220.9772 | -0.311 | 222.19 | 218.09 | 0.0499 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.295 |  | 296.1488 | -0.2883 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 11 | AMZN | cloud_ai_capex | 253 |  | 255.1558 | -0.8449 | 258.07 | 252.62 | 0.0198 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1022.37 |  | 1027.3748 | -0.4871 | 1035.07 | 1021.09 | 0.1731 | below_vwap | below_vwap |
| 14 | TT | data_center_power_cooling | 473.86 |  | 474.1352 | -0.0581 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | META | cloud_ai_capex | 668.07 |  | 671.4266 | -0.4999 | 680.09 | 667.1 | 2.1779 | below_vwap | below_vwap,spread_too_wide |
| 16 | SOXX | semiconductor_index | 528.71 |  | 533.8533 | -0.9634 | 543.4 | 535.47 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 706.67 |  | 709.3685 | -0.3804 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 207.34 |  | 207.3498 | -0.0047 | 211.03 | 207.49 | 0.1109 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1795.29 |  | 1818.1673 | -1.2583 | 1823.13 | 1796.26 | 0.1092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | ETN | data_center_power_cooling | 395.55 |  | 399.2848 | -0.9354 | 406.24 | 399.495 | 0.0784 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.71 |  | 399.4671 | 1.3125 | 398.69 | 392.2 | 0.0741 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.82 |  | 330.6606 | 0.6531 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.195 |  | 515.1639 | 0.5884 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.56 |  | 294.9749 | 0.5374 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 473.86 |  | 474.1352 | -0.0581 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1022.37 |  | 1027.3748 | -0.4871 | 1035.07 | 1021.09 | 0.1731 | below_vwap | below_vwap |
| 7 | KLAC | semiconductor_equipment | 220.29 |  | 220.9772 | -0.311 | 222.19 | 218.09 | 0.0499 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.295 |  | 296.1488 | -0.2883 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | AMZN | cloud_ai_capex | 253 |  | 255.1558 | -0.8449 | 258.07 | 252.62 | 0.0198 | below_vwap | below_vwap |
| 11 | META | cloud_ai_capex | 668.07 |  | 671.4266 | -0.4999 | 680.09 | 667.1 | 2.1779 | below_vwap | below_vwap,spread_too_wide |
| 12 | ANET | ai_networking_optical | 167.38 |  | 166.5838 | 0.478 | 169.91 | 165.6 | 3.4831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | JCI | data_center_power_cooling | 140.72 |  | 140.5207 | 0.1418 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | CRWV | gpu_cloud_ai_factory | 73.47 |  | 73.3025 | 0.2284 | 75.54 | 73.985 | 0.0544 | below_opening_15m_low | below_opening_15m_low |
| 15 | IREN | high_beta_ai_infrastructure | 35.6 |  | 35.4996 | 0.2827 | 37.365 | 36.4 | 0.0562 | below_opening_15m_low | below_opening_15m_low |
| 16 | SOXX | semiconductor_index | 528.71 |  | 533.8533 | -0.9634 | 543.4 | 535.47 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | TSM | foundry | 405.52 |  | 408.85 | -0.8145 | 414.385 | 406.61 | 0.6461 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 389.62 |  | 394.6706 | -1.2797 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 19 | QQQ | market_regime | 706.67 |  | 709.3685 | -0.3804 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AVGO | custom_silicon_networking | 376.545 |  | 379.9326 | -0.8916 | 386.58 | 378.53 | 0.4913 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.67 |  | 709.3685 | -0.3804 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.955 |  | 71.8062 | -1.1854 | 73.09 | 71.45 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.34 |  | 207.3498 | -0.0047 | 211.03 | 207.49 | 0.1109 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.71 |  | 399.4671 | 1.3125 | 398.69 | 392.2 | 0.0741 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.82 |  | 330.6606 | 0.6531 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 358.425 |  | 368.6676 | -2.7783 | 375.18 | 369.2 | 0.0949 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 495.365 |  | 503.8933 | -1.6925 | 518.33 | 507.62 | 0.864 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.52 |  | 408.85 | -0.8145 | 414.385 | 406.61 | 0.6461 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.71 |  | 533.8533 | -0.9634 | 543.4 | 535.47 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.655 |  | 571.7568 | -0.7174 | 580.31 | 572.21 | 0.0652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.545 |  | 379.9326 | -0.8916 | 386.58 | 378.53 | 0.4913 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.03 |  | 857.1477 | -1.0637 | 887.1 | 866.765 | 0.8372 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.9 |  | 191.021 | -1.6339 | 201.61 | 194.19 | 0.8728 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 395.13 |  | 402.2255 | -1.7641 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.14 |  | 45.7926 | -1.4251 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.03 |  | 25.3208 | -1.1483 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.88 |  | 752.3281 | -0.1925 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.295 |  | 296.1488 | -0.2883 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.14 |  | 126.6305 | -0.3874 | 131.36 | 126.665 | 3.2107 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.47 |  | 73.3025 | 0.2284 | 75.54 | 73.985 | 0.0544 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 289.64 |  | 293.3669 | -1.2704 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.55 |  | 399.2848 | -0.9354 | 406.24 | 399.495 | 0.0784 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 627.975 |  | 631.3632 | -0.5367 | 640.25 | 631.005 | 4.7374 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1022.37 |  | 1027.3748 | -0.4871 | 1035.07 | 1021.09 | 0.1731 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 473.86 |  | 474.1352 | -0.0581 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.72 |  | 140.5207 | 0.1418 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.38 |  | 166.5838 | 0.478 | 169.91 | 165.6 | 3.4831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.545 |  | 280.7026 | -1.8374 | 288.48 | 280.67 | 0.0871 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LITE | ai_networking_optical | 700.935 |  | 708.3791 | -1.0509 | 737.175 | 720.21 | 3.0174 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 389.62 |  | 394.6706 | -1.2797 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.1 |  | 101.3202 | -2.1912 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.15 |  | 323.4466 | -1.0192 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1795.29 |  | 1818.1673 | -1.2583 | 1823.13 | 1796.26 | 0.1092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.6 |  | 570.0477 | -1.6574 | 572.69 | 562.32 | 0.4816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.2 |  | 322.9329 | -1.4656 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.29 |  | 220.9772 | -0.311 | 222.19 | 218.09 | 0.0499 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 323.02 |  | 326.6838 | -1.1215 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.22 |  | 286.5825 | -2.2201 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.995 |  | 63.9361 | -1.472 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.68 |  | 51.7902 | -2.1437 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.65 |  | 134.9 | -0.9266 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.55 |  | 334.6654 | -1.8273 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.195 |  | 515.1639 | 0.5884 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.56 |  | 294.9749 | 0.5374 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.285 |  | 26.7962 | -1.9077 | 28.05 | 27.6 | 0.038 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.6 |  | 35.4996 | 0.2827 | 37.365 | 36.4 | 0.0562 | below_opening_15m_low | below_opening_15m_low |
| CORZ | high_beta_ai_infrastructure | 21.085 |  | 21.2155 | -0.6152 | 22.18 | 21.78 | 0.0474 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1413.28 |  | 1462.3453 | -3.3553 | 1549.47 | 1482.06 | 2.3159 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 462.225 |  | 473.8515 | -2.4536 | 498.04 | 480.14 | 0.2293 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 746.69 |  | 764.6107 | -2.3438 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 253 |  | 255.1558 | -0.8449 | 258.07 | 252.62 | 0.0198 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.07 |  | 671.4266 | -0.4999 | 680.09 | 667.1 | 2.1779 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 256.97 |  | 257.2931 | -0.1256 | 265.96 | 258.1 | 3.8915 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.36 |  | 161.68 | -3.2904 | 168.11 | 162.41 | 1.4838 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
