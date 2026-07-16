# Intraday State

- Generated at: `2026-07-17T02:47:34+08:00`
- Market time ET: `2026-07-16T14:47:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 6, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.37 |  | 709.3821 | -0.4246 | 713.55 | 708.25 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.32 |  | 533.8766 | -1.0408 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.075 |  | 571.8305 | -0.8316 | 580.31 | 572.21 | 0.0635 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.61 |  | 752.3417 | -0.2302 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.24 |  | 399.4113 | 1.209 | 398.69 | 392.2 | 0.0544 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.14 |  | 330.6451 | 0.4521 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.14 |  | 330.6451 | 0.4521 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 404.24 |  | 399.4113 | 1.209 | 398.69 | 392.2 | 0.0544 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.695 |  | 140.5177 | 0.1262 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 518.3 |  | 515.1506 | 0.6113 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 167.28 |  | 166.581 | 0.4196 | 169.91 | 165.6 | 4.5074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.51 |  | 294.9603 | 0.5254 | 293.89 | 291.35 | 4.6676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | KLAC | semiconductor_equipment | 219.84 |  | 220.9843 | -0.5178 | 222.19 | 218.09 | 0.0955 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.26 |  | 296.153 | -0.3015 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | AMZN | cloud_ai_capex | 252.73 |  | 255.1802 | -0.9602 | 258.07 | 252.62 | 0.0237 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | TT | data_center_power_cooling | 473.63 |  | 474.1404 | -0.1077 | 474.085 | 467.64 | 5.1095 | below_vwap | below_vwap,spread_too_wide |
| 12 | META | cloud_ai_capex | 668.24 |  | 671.5225 | -0.4888 | 680.09 | 667.1 | 2.4497 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 528.32 |  | 533.8766 | -1.0408 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | QQQ | market_regime | 706.37 |  | 709.3821 | -0.4246 | 713.55 | 708.25 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | NVDA | ai_accelerator | 207.05 |  | 207.351 | -0.1452 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | ASML | semiconductor_equipment | 1794.64 |  | 1818.3118 | -1.3019 | 1823.13 | 1796.26 | 0.1259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | GEV | data_center_power_cooling | 1020.24 |  | 1027.4198 | -0.6988 | 1035.07 | 1021.09 | 0.1411 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AMAT | semiconductor_equipment | 560.32 |  | 570.1095 | -1.7171 | 572.69 | 562.32 | 0.1196 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 567.075 |  | 571.8305 | -0.8316 | 580.31 | 572.21 | 0.0635 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SPY | market_regime | 750.61 |  | 752.3417 | -0.2302 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.24 |  | 399.4113 | 1.209 | 398.69 | 392.2 | 0.0544 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.14 |  | 330.6451 | 0.4521 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.3 |  | 515.1506 | 0.6113 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.51 |  | 294.9603 | 0.5254 | 293.89 | 291.35 | 4.6676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TT | data_center_power_cooling | 473.63 |  | 474.1404 | -0.1077 | 474.085 | 467.64 | 5.1095 | below_vwap | below_vwap,spread_too_wide |
| 6 | KLAC | semiconductor_equipment | 219.84 |  | 220.9843 | -0.5178 | 222.19 | 218.09 | 0.0955 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 295.26 |  | 296.153 | -0.3015 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | AMZN | cloud_ai_capex | 252.73 |  | 255.1802 | -0.9602 | 258.07 | 252.62 | 0.0237 | below_vwap | below_vwap |
| 10 | META | cloud_ai_capex | 668.24 |  | 671.5225 | -0.4888 | 680.09 | 667.1 | 2.4497 | below_vwap | below_vwap,spread_too_wide |
| 11 | ANET | ai_networking_optical | 167.28 |  | 166.581 | 0.4196 | 169.91 | 165.6 | 4.5074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | JCI | data_center_power_cooling | 140.695 |  | 140.5177 | 0.1262 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SOXX | semiconductor_index | 528.32 |  | 533.8766 | -1.0408 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 405.09 |  | 408.8839 | -0.9279 | 414.385 | 406.61 | 0.5406 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 15 | CIEN | ai_networking_optical | 389.955 |  | 394.7393 | -1.212 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 706.37 |  | 709.3821 | -0.4246 | 713.55 | 708.25 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 376.26 |  | 379.9597 | -0.9737 | 386.58 | 378.53 | 0.2551 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | MU | memory_hbm_storage | 847.01 |  | 857.2412 | -1.1935 | 887.1 | 866.765 | 0.4722 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 289.455 |  | 293.3784 | -1.3373 | 300.385 | 293.64 | 0.9259 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | NVDA | ai_accelerator | 207.05 |  | 207.351 | -0.1452 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.37 |  | 709.3821 | -0.4246 | 713.55 | 708.25 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.86 |  | 71.8112 | -1.3246 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.05 |  | 207.351 | -0.1452 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.24 |  | 399.4113 | 1.209 | 398.69 | 392.2 | 0.0544 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.14 |  | 330.6451 | 0.4521 | 328.98 | 326.885 | 0.006 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 359.78 |  | 368.7932 | -2.444 | 375.18 | 369.2 | 0.5031 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 494.55 |  | 503.9584 | -1.8669 | 518.33 | 507.62 | 1.3548 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.09 |  | 408.8839 | -0.9279 | 414.385 | 406.61 | 0.5406 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.32 |  | 533.8766 | -1.0408 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.075 |  | 571.8305 | -0.8316 | 580.31 | 572.21 | 0.0635 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.26 |  | 379.9597 | -0.9737 | 386.58 | 378.53 | 0.2551 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 847.01 |  | 857.2412 | -1.1935 | 887.1 | 866.765 | 0.4722 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.67 |  | 191.0444 | -1.7663 | 201.61 | 194.19 | 1.0018 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 397.07 |  | 402.2821 | -1.2956 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.23 |  | 45.7967 | -1.2374 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.01 |  | 25.3251 | -1.2443 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.61 |  | 752.3417 | -0.2302 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.26 |  | 296.153 | -0.3015 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.1 |  | 126.634 | -0.4217 | 131.36 | 126.665 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.18 |  | 73.3023 | -0.1669 | 75.54 | 73.985 | 0.0957 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 289.455 |  | 293.3784 | -1.3373 | 300.385 | 293.64 | 0.9259 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 395.17 |  | 399.3075 | -1.0362 | 406.24 | 399.495 | 0.5542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 627.54 |  | 631.3803 | -0.6082 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1020.24 |  | 1027.4198 | -0.6988 | 1035.07 | 1021.09 | 0.1411 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 473.63 |  | 474.1404 | -0.1077 | 474.085 | 467.64 | 5.1095 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.695 |  | 140.5177 | 0.1262 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.28 |  | 166.581 | 0.4196 | 169.91 | 165.6 | 4.5074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.52 |  | 280.7199 | -1.8523 | 288.48 | 280.67 | 1.2485 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.71 |  | 708.4205 | -1.0884 | 737.175 | 720.21 | 2.5731 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 389.955 |  | 394.7393 | -1.212 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.16 |  | 101.3473 | -2.1582 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.425 |  | 323.4744 | -0.9427 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.64 |  | 1818.3118 | -1.3019 | 1823.13 | 1796.26 | 0.1259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.32 |  | 570.1095 | -1.7171 | 572.69 | 562.32 | 0.1196 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 318.02 |  | 322.9626 | -1.5304 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.84 |  | 220.9843 | -0.5178 | 222.19 | 218.09 | 0.0955 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.76 |  | 326.6987 | -1.2056 | 332.49 | 326.685 | 4.3624 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.22 |  | 286.5825 | -2.2201 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.09 |  | 63.9523 | -1.3484 | 66.19 | 63.93 | 4.7868 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.68 |  | 51.7902 | -2.1437 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.6 |  | 134.9386 | -0.992 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.57 |  | 334.8117 | -1.8642 | 346.26 | 338 | 4.2152 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 518.3 |  | 515.1506 | 0.6113 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.51 |  | 294.9603 | 0.5254 | 293.89 | 291.35 | 4.6676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.16 |  | 26.7991 | -2.3848 | 28.05 | 27.6 | 0.0382 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.44 |  | 35.4994 | -0.1675 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.995 |  | 21.2173 | -1.0478 | 22.18 | 21.78 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1413.69 |  | 1462.5906 | -3.3434 | 1549.47 | 1482.06 | 2.9356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 462 |  | 473.9605 | -2.5235 | 498.04 | 480.14 | 0.3074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 748.295 |  | 764.8473 | -2.1641 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 252.73 |  | 255.1802 | -0.9602 | 258.07 | 252.62 | 0.0237 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.24 |  | 671.5225 | -0.4888 | 680.09 | 667.1 | 2.4497 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 257.01 |  | 257.294 | -0.1104 | 265.96 | 258.1 | 3.8909 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 157.01 |  | 161.6981 | -2.8993 | 168.11 | 162.41 | 1.4776 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
