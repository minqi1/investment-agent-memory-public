# Intraday State

- Generated at: `2026-07-17T03:07:27+08:00`
- Market time ET: `2026-07-16T15:07:28-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'below_vwap': 8, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.66 |  | 709.2387 | -0.5046 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.63 |  | 533.7271 | -1.1424 | 543.4 | 535.47 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.425 |  | 571.6343 | -0.7364 | 580.31 | 572.21 | 0.0599 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.29 |  | 752.224 | -0.2571 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 405.07 |  | 399.8477 | 1.3061 | 398.69 | 392.2 | 0.0815 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.44 |  | 330.9144 | 1.0654 | 328.98 | 326.885 | 0.0419 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 474.43 |  | 474.1137 | 0.0667 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | MSFT | cloud_ai_capex | 405.07 |  | 399.8477 | 1.3061 | 398.69 | 392.2 | 0.0815 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 334.44 |  | 330.9144 | 1.0654 | 328.98 | 326.885 | 0.0419 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.94 |  | 166.5882 | 0.2112 | 169.91 | 165.6 | 3.2287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 207.35 |  | 207.3496 | 0.0002 | 211.03 | 207.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low |
| 6 | LIN | industrial_gases | 518.4 |  | 515.2613 | 0.6091 | 515.825 | 512.23 | 5.0116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 296.175 |  | 295.0036 | 0.3971 | 293.89 | 291.35 | 3.9031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | IWM | market_regime | 295.015 |  | 296.0925 | -0.3639 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | AMZN | cloud_ai_capex | 252.635 |  | 255.052 | -0.9476 | 258.07 | 252.62 | 0.0198 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 140.43 |  | 140.521 | -0.0648 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ENTG | semiconductor_materials | 134.22 |  | 134.7893 | -0.4224 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | TSM | foundry | 406.73 |  | 408.7127 | -0.4851 | 414.385 | 406.61 | 0.5483 | below_vwap | below_vwap,spread_too_wide |
| 14 | GEV | data_center_power_cooling | 1023.62 |  | 1027.1015 | -0.339 | 1035.07 | 1021.09 | 4.3551 | below_vwap | below_vwap,spread_too_wide |
| 15 | KLAC | semiconductor_equipment | 219.2 |  | 220.9244 | -0.7805 | 222.19 | 218.09 | 5.0365 | below_vwap | below_vwap,spread_too_wide |
| 16 | SOXX | semiconductor_index | 527.63 |  | 533.7271 | -1.1424 | 543.4 | 535.47 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 705.66 |  | 709.2387 | -0.5046 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1794.96 |  | 1817.5176 | -1.2411 | 1823.13 | 1796.26 | 0.0797 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 567.425 |  | 571.6343 | -0.7364 | 580.31 | 572.21 | 0.0599 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SPY | market_regime | 750.29 |  | 752.224 | -0.2571 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 405.07 |  | 399.8477 | 1.3061 | 398.69 | 392.2 | 0.0815 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.44 |  | 330.9144 | 1.0654 | 328.98 | 326.885 | 0.0419 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.43 |  | 474.1137 | 0.0667 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 518.4 |  | 515.2613 | 0.6091 | 515.825 | 512.23 | 5.0116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 296.175 |  | 295.0036 | 0.3971 | 293.89 | 291.35 | 3.9031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | TSM | foundry | 406.73 |  | 408.7127 | -0.4851 | 414.385 | 406.61 | 0.5483 | below_vwap | below_vwap,spread_too_wide |
| 7 | JCI | data_center_power_cooling | 140.43 |  | 140.521 | -0.0648 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 1023.62 |  | 1027.1015 | -0.339 | 1035.07 | 1021.09 | 4.3551 | below_vwap | below_vwap,spread_too_wide |
| 9 | KLAC | semiconductor_equipment | 219.2 |  | 220.9244 | -0.7805 | 222.19 | 218.09 | 5.0365 | below_vwap | below_vwap,spread_too_wide |
| 10 | IWM | market_regime | 295.015 |  | 296.0925 | -0.3639 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ENTG | semiconductor_materials | 134.22 |  | 134.7893 | -0.4224 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AMZN | cloud_ai_capex | 252.635 |  | 255.052 | -0.9476 | 258.07 | 252.62 | 0.0198 | below_vwap | below_vwap |
| 14 | ANET | ai_networking_optical | 166.94 |  | 166.5882 | 0.2112 | 169.91 | 165.6 | 3.2287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | NVDA | ai_accelerator | 207.35 |  | 207.3496 | 0.0002 | 211.03 | 207.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low |
| 16 | SOXX | semiconductor_index | 527.63 |  | 533.7271 | -1.1424 | 543.4 | 535.47 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 388.34 |  | 394.1303 | -1.4691 | 410 | 397.68 | 0.412 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | QQQ | market_regime | 705.66 |  | 709.2387 | -0.5046 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 375.81 |  | 379.7765 | -1.0444 | 386.58 | 378.53 | 0.2661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | MU | memory_hbm_storage | 845.81 |  | 856.5636 | -1.2554 | 887.1 | 866.765 | 0.3488 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.66 |  | 709.2387 | -0.5046 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.63 |  | 71.7742 | -1.5942 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.35 |  | 207.3496 | 0.0002 | 211.03 | 207.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 405.07 |  | 399.8477 | 1.3061 | 398.69 | 392.2 | 0.0815 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 334.44 |  | 330.9144 | 1.0654 | 328.98 | 326.885 | 0.0419 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 356.625 |  | 367.7259 | -3.0188 | 375.18 | 369.2 | 0.1318 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 494.415 |  | 503.585 | -1.8209 | 518.33 | 507.62 | 0.6917 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.73 |  | 408.7127 | -0.4851 | 414.385 | 406.61 | 0.5483 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.63 |  | 533.7271 | -1.1424 | 543.4 | 535.47 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.425 |  | 571.6343 | -0.7364 | 580.31 | 572.21 | 0.0599 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.81 |  | 379.7765 | -1.0444 | 386.58 | 378.53 | 0.2661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 845.81 |  | 856.5636 | -1.2554 | 887.1 | 866.765 | 0.3488 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 186.71 |  | 190.8994 | -2.1946 | 201.61 | 194.19 | 1.8799 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 395.9 |  | 401.9157 | -1.4968 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.255 |  | 45.7657 | -1.116 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.065 |  | 25.3074 | -0.958 | 26.71 | 25.74 | 0.0798 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.29 |  | 752.224 | -0.2571 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.015 |  | 296.0925 | -0.3639 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.685 |  | 126.6006 | -0.7232 | 131.36 | 126.665 | 0.4694 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.29 |  | 73.296 | -0.0082 | 75.54 | 73.985 | 4.3526 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.45 |  | 293.2532 | -1.2969 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.81 |  | 399.218 | -0.8537 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 628.52 |  | 631.1894 | -0.4229 | 640.25 | 631.005 | 4.824 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1023.62 |  | 1027.1015 | -0.339 | 1035.07 | 1021.09 | 4.3551 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.43 |  | 474.1137 | 0.0667 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.43 |  | 140.521 | -0.0648 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.94 |  | 166.5882 | 0.2112 | 169.91 | 165.6 | 3.2287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.07 |  | 280.598 | -1.9701 | 288.48 | 280.67 | 2.5012 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.73 |  | 708.051 | -1.4577 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 388.34 |  | 394.1303 | -1.4691 | 410 | 397.68 | 0.412 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 99.155 |  | 101.2377 | -2.0572 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.88 |  | 323.2864 | -1.6723 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.96 |  | 1817.5176 | -1.2411 | 1823.13 | 1796.26 | 0.0797 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.45 |  | 569.7422 | -1.6309 | 572.69 | 562.32 | 0.546 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.285 |  | 322.8548 | -1.7252 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.2 |  | 220.9244 | -0.7805 | 222.19 | 218.09 | 5.0365 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.61 |  | 326.5762 | -1.2145 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.7 |  | 286.2356 | -1.9339 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.83 |  | 63.8634 | -1.6182 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.05 |  | 51.7568 | -1.3656 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.22 |  | 134.7893 | -0.4224 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.24 |  | 334.1298 | -1.4634 | 346.26 | 338 | 4.2158 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 518.4 |  | 515.2613 | 0.6091 | 515.825 | 512.23 | 5.0116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.175 |  | 295.0036 | 0.3971 | 293.89 | 291.35 | 3.9031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.425 |  | 26.7734 | -1.3014 | 28.05 | 27.6 | 0.0378 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.5 |  | 35.5026 | -0.0073 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.13 |  | 21.2026 | -0.3422 | 22.18 | 21.78 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1401.52 |  | 1459.3393 | -3.962 | 1549.47 | 1482.06 | 1.285 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 457.77 |  | 473.2424 | -3.2694 | 498.04 | 480.14 | 0.7842 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 740.14 |  | 763.7326 | -3.0891 | 797.155 | 768.7 | 4.1627 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 252.635 |  | 255.052 | -0.9476 | 258.07 | 252.62 | 0.0198 | below_vwap | below_vwap |
| META | cloud_ai_capex | 666.81 |  | 671.2257 | -0.6579 | 680.09 | 667.1 | 0.174 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 256.58 |  | 257.2822 | -0.2729 | 265.96 | 258.1 | 2.319 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.7 |  | 161.5695 | -3.6328 | 168.11 | 162.41 | 0.3982 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
