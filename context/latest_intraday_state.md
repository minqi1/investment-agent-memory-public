# Intraday State

- Generated at: `2026-07-17T02:23:44+08:00`
- Market time ET: `2026-07-16T14:23:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 37, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 11, 'spread_too_wide_or_missing': 4, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.77 |  | 709.5519 | -0.2511 | 713.55 | 708.25 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.89 |  | 533.9913 | -0.5808 | 543.4 | 535.47 | 0.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.24 |  | 572.1215 | -0.5036 | 580.31 | 572.21 | 0.0632 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.53 |  | 752.4765 | -0.1258 | 753.51 | 751.13 | 0.016 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.56 |  | 398.9503 | 1.4061 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.85 |  | 330.591 | 0.0783 | 328.98 | 326.885 | 0.3234 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.85 |  | 330.591 | 0.0783 | 328.98 | 326.885 | 0.3234 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 404.56 |  | 398.9503 | 1.4061 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.805 |  | 140.5109 | 0.2093 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ANET | ai_networking_optical | 168.24 |  | 166.5433 | 1.0188 | 169.91 | 165.6 | 0.1605 | watch_only | none |
| 5 | LIN | industrial_gases | 517.03 |  | 515.0611 | 0.3823 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 295.7 |  | 294.9041 | 0.2699 | 293.89 | 291.35 | 4.0785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ARM | ai_accelerator | 258.49 |  | 257.288 | 0.4672 | 265.96 | 258.1 | 3.2999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1802.05 |  | 1818.9947 | -0.9315 | 1823.13 | 1796.26 | 0.1321 | below_vwap | below_vwap |
| 9 | GEV | data_center_power_cooling | 1026.56 |  | 1027.7113 | -0.112 | 1035.07 | 1021.09 | 0.1091 | below_vwap | below_vwap |
| 10 | KLAC | semiconductor_equipment | 220.79 |  | 221.0244 | -0.1061 | 222.19 | 218.09 | 0.077 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 751.53 |  | 752.4765 | -0.1258 | 753.51 | 751.13 | 0.016 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.625 |  | 296.1723 | -0.1848 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 13 | AMZN | cloud_ai_capex | 253.45 |  | 255.4743 | -0.7924 | 258.07 | 252.62 | 0.0118 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | LITE | ai_networking_optical | 709.18 |  | 708.5564 | 0.088 | 737.175 | 720.21 | 4.0794 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | TT | data_center_power_cooling | 473.63 |  | 474.1941 | -0.119 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 134.91 |  | 134.9913 | -0.0602 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AMAT | semiconductor_equipment | 562.99 |  | 570.342 | -1.289 | 572.69 | 562.32 | 1.7993 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 669.515 |  | 671.8997 | -0.3549 | 680.09 | 667.1 | 2.4734 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 530.89 |  | 533.9913 | -0.5808 | 543.4 | 535.47 | 0.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.56 |  | 398.9503 | 1.4061 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.85 |  | 330.591 | 0.0783 | 328.98 | 326.885 | 0.3234 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 517.03 |  | 515.0611 | 0.3823 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.7 |  | 294.9041 | 0.2699 | 293.89 | 291.35 | 4.0785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 168.24 |  | 166.5433 | 1.0188 | 169.91 | 165.6 | 0.1605 | watch_only | none |
| 6 | TT | data_center_power_cooling | 473.63 |  | 474.1941 | -0.119 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | GEV | data_center_power_cooling | 1026.56 |  | 1027.7113 | -0.112 | 1035.07 | 1021.09 | 0.1091 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1802.05 |  | 1818.9947 | -0.9315 | 1823.13 | 1796.26 | 0.1321 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 562.99 |  | 570.342 | -1.289 | 572.69 | 562.32 | 1.7993 | below_vwap | below_vwap,spread_too_wide |
| 10 | KLAC | semiconductor_equipment | 220.79 |  | 221.0244 | -0.1061 | 222.19 | 218.09 | 0.077 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 751.53 |  | 752.4765 | -0.1258 | 753.51 | 751.13 | 0.016 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.625 |  | 296.1723 | -0.1848 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 134.91 |  | 134.9913 | -0.0602 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AMZN | cloud_ai_capex | 253.45 |  | 255.4743 | -0.7924 | 258.07 | 252.62 | 0.0118 | below_vwap | below_vwap |
| 16 | META | cloud_ai_capex | 669.515 |  | 671.8997 | -0.3549 | 680.09 | 667.1 | 2.4734 | below_vwap | below_vwap,spread_too_wide |
| 17 | JCI | data_center_power_cooling | 140.805 |  | 140.5109 | 0.2093 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ARM | ai_accelerator | 258.49 |  | 257.288 | 0.4672 | 265.96 | 258.1 | 3.2999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LITE | ai_networking_optical | 709.18 |  | 708.5564 | 0.088 | 737.175 | 720.21 | 4.0794 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | SOXX | semiconductor_index | 530.89 |  | 533.9913 | -0.5808 | 543.4 | 535.47 | 0.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.77 |  | 709.5519 | -0.2511 | 713.55 | 708.25 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.32 |  | 71.8675 | -0.7618 | 73.09 | 71.45 | 0.028 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.045 |  | 207.3748 | -0.159 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.56 |  | 398.9503 | 1.4061 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.85 |  | 330.591 | 0.0783 | 328.98 | 326.885 | 0.3234 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 363.585 |  | 370.1964 | -1.7859 | 375.18 | 369.2 | 1.3477 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 497.87 |  | 504.4206 | -1.2986 | 518.33 | 507.62 | 1.2774 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.09 |  | 409.0964 | -0.7349 | 414.385 | 406.61 | 0.8176 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.89 |  | 533.9913 | -0.5808 | 543.4 | 535.47 | 0.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.24 |  | 572.1215 | -0.5036 | 580.31 | 572.21 | 0.0632 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.16 |  | 380.1601 | -0.7892 | 386.58 | 378.53 | 0.0769 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 857.32 |  | 857.5505 | -0.0269 | 887.1 | 866.765 | 0.4456 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.33 |  | 191.1942 | -1.4981 | 201.61 | 194.19 | 1.3381 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 398.97 |  | 402.3884 | -0.8495 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.295 |  | 45.8565 | -1.2244 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.995 |  | 25.3602 | -1.4401 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.53 |  | 752.4765 | -0.1258 | 753.51 | 751.13 | 0.016 | below_vwap | below_vwap |
| IWM | market_regime | 295.625 |  | 296.1723 | -0.1848 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.07 |  | 126.664 | -0.469 | 131.36 | 126.665 | 0.9677 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.7 |  | 73.3292 | -0.858 | 75.54 | 73.985 | 0.8803 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 290.2 |  | 293.6703 | -1.1817 | 300.385 | 293.64 | 1.8711 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.37 |  | 399.4167 | -0.7628 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.5 |  | 631.5196 | -0.3198 | 640.25 | 631.005 | 0.1827 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1026.56 |  | 1027.7113 | -0.112 | 1035.07 | 1021.09 | 0.1091 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 473.63 |  | 474.1941 | -0.119 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.805 |  | 140.5109 | 0.2093 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.24 |  | 166.5433 | 1.0188 | 169.91 | 165.6 | 0.1605 | watch_only | none |
| COHR | ai_networking_optical | 277.35 |  | 280.8911 | -1.2607 | 288.48 | 280.67 | 1.2619 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 709.18 |  | 708.5564 | 0.088 | 737.175 | 720.21 | 4.0794 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 392.97 |  | 395.0302 | -0.5215 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.04 |  | 101.4678 | -1.4072 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.08 |  | 323.6715 | -1.1096 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1802.05 |  | 1818.9947 | -0.9315 | 1823.13 | 1796.26 | 0.1321 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 562.99 |  | 570.342 | -1.289 | 572.69 | 562.32 | 1.7993 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.96 |  | 323.0631 | -1.2701 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.79 |  | 221.0244 | -0.1061 | 222.19 | 218.09 | 0.077 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 324.26 |  | 326.8165 | -0.7823 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 281 |  | 287.0187 | -2.097 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.31 |  | 63.9966 | -1.0729 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.91 |  | 51.9099 | -1.9261 | 52.72 | 51.735 | 0.825 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 134.91 |  | 134.9913 | -0.0602 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.13 |  | 335.1656 | -1.5024 | 346.26 | 338 | 0.2454 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LIN | industrial_gases | 517.03 |  | 515.0611 | 0.3823 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.7 |  | 294.9041 | 0.2699 | 293.89 | 291.35 | 4.0785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.255 |  | 26.8214 | -2.1118 | 28.05 | 27.6 | 0.0762 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.295 |  | 35.5189 | -0.6302 | 37.365 | 36.4 | 0.0567 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.035 |  | 21.2323 | -0.9292 | 22.18 | 21.78 | 0.0951 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1440.425 |  | 1465.7452 | -1.7275 | 1549.47 | 1482.06 | 3.4712 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 460.54 |  | 474.8054 | -3.0045 | 498.04 | 480.14 | 1.2377 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 752.115 |  | 766.0823 | -1.8232 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 253.45 |  | 255.4743 | -0.7924 | 258.07 | 252.62 | 0.0118 | below_vwap | below_vwap |
| META | cloud_ai_capex | 669.515 |  | 671.8997 | -0.3549 | 680.09 | 667.1 | 2.4734 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.49 |  | 257.288 | 0.4672 | 265.96 | 258.1 | 3.2999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 157.11 |  | 161.9248 | -2.9735 | 168.11 | 162.41 | 0.4901 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
