# Intraday State

- Generated at: `2026-07-17T02:59:28+08:00`
- Market time ET: `2026-07-16T14:59:29-04:00`
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
| QQQ | market_regime | 705.75 |  | 709.3125 | -0.5023 | 713.55 | 708.25 | 0.0468 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.62 |  | 533.8087 | -1.1593 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.43 |  | 571.6961 | -0.9211 | 580.31 | 572.21 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.38 |  | 752.281 | -0.2527 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 405.75 |  | 399.6047 | 1.5378 | 398.69 | 392.2 | 0.0271 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.495 |  | 330.7889 | 0.8181 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.57 |  | 140.5215 | 0.0345 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | AAPL | mega_cap_platform | 333.495 |  | 330.7889 | 0.8181 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | ANET | ai_networking_optical | 166.69 |  | 166.5863 | 0.0623 | 169.91 | 165.6 | 3.1016 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 518.385 |  | 515.1864 | 0.6209 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 296.23 |  | 294.9909 | 0.42 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MSFT | cloud_ai_capex | 405.75 |  | 399.6047 | 1.5378 | 398.69 | 392.2 | 0.0271 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 219.38 |  | 220.9447 | -0.7082 | 222.19 | 218.09 | 0.0684 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.1 |  | 296.1265 | -0.3466 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | AMZN | cloud_ai_capex | 253.37 |  | 255.1218 | -0.6867 | 258.07 | 252.62 | 0.0355 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | TT | data_center_power_cooling | 473.58 |  | 474.1256 | -0.1151 | 474.085 | 467.64 | 0.1837 | below_vwap | below_vwap |
| 12 | META | cloud_ai_capex | 668.59 |  | 671.3195 | -0.4066 | 680.09 | 667.1 | 2.4619 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 527.62 |  | 533.8087 | -1.1593 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 405.44 |  | 408.7522 | -0.8103 | 414.385 | 406.61 | 0.0592 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 705.75 |  | 709.3125 | -0.5023 | 713.55 | 708.25 | 0.0468 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | NVDA | ai_accelerator | 207 |  | 207.3473 | -0.1675 | 211.03 | 207.49 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AMD | ai_accelerator | 494.89 |  | 503.7486 | -1.7585 | 518.33 | 507.62 | 0.1394 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1793.335 |  | 1817.809 | -1.3463 | 1823.13 | 1796.26 | 0.0786 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | GEV | data_center_power_cooling | 1019.79 |  | 1027.2312 | -0.7244 | 1035.07 | 1021.09 | 0.05 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 566.43 |  | 571.6961 | -0.9211 | 580.31 | 572.21 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 405.75 |  | 399.6047 | 1.5378 | 398.69 | 392.2 | 0.0271 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.495 |  | 330.7889 | 0.8181 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.385 |  | 515.1864 | 0.6209 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.23 |  | 294.9909 | 0.42 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 473.58 |  | 474.1256 | -0.1151 | 474.085 | 467.64 | 0.1837 | below_vwap | below_vwap |
| 6 | KLAC | semiconductor_equipment | 219.38 |  | 220.9447 | -0.7082 | 222.19 | 218.09 | 0.0684 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 295.1 |  | 296.1265 | -0.3466 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | AMZN | cloud_ai_capex | 253.37 |  | 255.1218 | -0.6867 | 258.07 | 252.62 | 0.0355 | below_vwap | below_vwap |
| 10 | META | cloud_ai_capex | 668.59 |  | 671.3195 | -0.4066 | 680.09 | 667.1 | 2.4619 | below_vwap | below_vwap,spread_too_wide |
| 11 | ANET | ai_networking_optical | 166.69 |  | 166.5863 | 0.0623 | 169.91 | 165.6 | 3.1016 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | JCI | data_center_power_cooling | 140.57 |  | 140.5215 | 0.0345 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SOXX | semiconductor_index | 527.62 |  | 533.8087 | -1.1593 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 405.44 |  | 408.7522 | -0.8103 | 414.385 | 406.61 | 0.0592 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | CIEN | ai_networking_optical | 387.61 |  | 394.4348 | -1.7303 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 705.75 |  | 709.3125 | -0.5023 | 713.55 | 708.25 | 0.0468 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 375.72 |  | 379.8624 | -1.0905 | 386.58 | 378.53 | 0.5057 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | MU | memory_hbm_storage | 845.45 |  | 856.8482 | -1.3303 | 887.1 | 866.765 | 1.1899 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 288.8 |  | 293.3103 | -1.5377 | 300.385 | 293.64 | 1.3158 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | NVDA | ai_accelerator | 207 |  | 207.3473 | -0.1675 | 211.03 | 207.49 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.75 |  | 709.3125 | -0.5023 | 713.55 | 708.25 | 0.0468 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.72 |  | 71.7935 | -1.4953 | 73.09 | 71.45 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207 |  | 207.3473 | -0.1675 | 211.03 | 207.49 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 405.75 |  | 399.6047 | 1.5378 | 398.69 | 392.2 | 0.0271 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.495 |  | 330.7889 | 0.8181 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 356.705 |  | 368.3611 | -3.1643 | 375.18 | 369.2 | 0.0925 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 494.89 |  | 503.7486 | -1.7585 | 518.33 | 507.62 | 0.1394 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 405.44 |  | 408.7522 | -0.8103 | 414.385 | 406.61 | 0.0592 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.62 |  | 533.8087 | -1.1593 | 543.4 | 535.47 | 0.0512 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.43 |  | 571.6961 | -0.9211 | 580.31 | 572.21 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.72 |  | 379.8624 | -1.0905 | 386.58 | 378.53 | 0.5057 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 845.45 |  | 856.8482 | -1.3303 | 887.1 | 866.765 | 1.1899 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.51 |  | 190.9758 | -1.8148 | 201.61 | 194.19 | 0.0693 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 394.56 |  | 402.071 | -1.8681 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.96 |  | 45.7878 | -1.808 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.015 |  | 25.3126 | -1.1756 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.38 |  | 752.281 | -0.2527 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.1 |  | 296.1265 | -0.3466 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.97 |  | 126.618 | -0.5117 | 131.36 | 126.665 | 3.2151 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.06 |  | 73.298 | -0.3247 | 75.54 | 73.985 | 0.0684 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 288.8 |  | 293.3103 | -1.5377 | 300.385 | 293.64 | 1.3158 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 395.33 |  | 399.2526 | -0.9825 | 406.24 | 399.495 | 0.3845 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 627.83 |  | 631.278 | -0.5462 | 640.25 | 631.005 | 4.7051 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1019.79 |  | 1027.2312 | -0.7244 | 1035.07 | 1021.09 | 0.05 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 473.58 |  | 474.1256 | -0.1151 | 474.085 | 467.64 | 0.1837 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 140.57 |  | 140.5215 | 0.0345 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.69 |  | 166.5863 | 0.0623 | 169.91 | 165.6 | 3.1016 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 274.945 |  | 280.6372 | -2.0283 | 288.48 | 280.67 | 2.5023 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.07 |  | 708.2627 | -1.5803 | 737.175 | 720.21 | 2.5521 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 387.61 |  | 394.4348 | -1.7303 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.93 |  | 101.2686 | -2.3093 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.24 |  | 323.3583 | -1.8921 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.335 |  | 1817.809 | -1.3463 | 1823.13 | 1796.26 | 0.0786 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 559.18 |  | 569.867 | -1.8753 | 572.69 | 562.32 | 0.3559 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 316.885 |  | 322.8924 | -1.8605 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.38 |  | 220.9447 | -0.7082 | 222.19 | 218.09 | 0.0684 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.54 |  | 326.6375 | -1.5606 | 332.49 | 326.685 | 4.6775 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 279.55 |  | 286.3768 | -2.3839 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.71 |  | 63.8923 | -1.8505 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.73 |  | 51.787 | -2.0411 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.62 |  | 134.8493 | -0.9116 | 138.07 | 133.73 | 0.3143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 328.22 |  | 334.1814 | -1.7839 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.385 |  | 515.1864 | 0.6209 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.23 |  | 294.9909 | 0.42 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.265 |  | 26.7841 | -1.9379 | 28.05 | 27.6 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.455 |  | 35.5002 | -0.1273 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.025 |  | 21.2051 | -0.8495 | 22.18 | 21.78 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1406.79 |  | 1461.668 | -3.7545 | 1549.47 | 1482.06 | 0.7108 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.095 |  | 473.5481 | -3.0521 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 741.83 |  | 764.2949 | -2.9393 | 797.155 | 768.7 | 4.4215 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 253.37 |  | 255.1218 | -0.6867 | 258.07 | 252.62 | 0.0355 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.59 |  | 671.3195 | -0.4066 | 680.09 | 667.1 | 2.4619 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 256.54 |  | 257.2874 | -0.2905 | 265.96 | 258.1 | 2.6234 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.26 |  | 161.652 | -3.3355 | 168.11 | 162.41 | 0.8511 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
