# Intraday State

- Generated at: `2026-07-17T02:27:43+08:00`
- Market time ET: `2026-07-16T14:27:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 10, 'watch_only': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.9 |  | 709.5312 | -0.2299 | 713.55 | 708.25 | 0.0254 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.855 |  | 533.9626 | -0.582 | 543.4 | 535.47 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.63 |  | 572.1056 | -0.4327 | 580.31 | 572.21 | 0.0421 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.36 |  | 752.4615 | -0.1464 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.4 |  | 399.0369 | 1.344 | 398.69 | 392.2 | 0.277 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.475 |  | 330.6012 | 0.2643 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.475 |  | 330.6012 | 0.2643 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 140.75 |  | 140.5162 | 0.1664 | 140.83 | 139.43 | 0.2629 | watch_only | none |
| 3 | LIN | industrial_gases | 516.87 |  | 515.0726 | 0.349 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.68 |  | 294.9085 | 0.2616 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 404.4 |  | 399.0369 | 1.344 | 398.69 | 392.2 | 0.277 | buy_precheck_manual_confirm | none |
| 6 | ARM | ai_accelerator | 258.665 |  | 257.2926 | 0.5334 | 265.96 | 258.1 | 3.866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1799.75 |  | 1818.7911 | -1.0469 | 1823.13 | 1796.26 | 0.0845 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 751.36 |  | 752.4615 | -0.1464 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.745 |  | 296.1681 | -0.1429 | 296.28 | 294.65 | 0.0101 | below_vwap | below_vwap |
| 10 | ANET | ai_networking_optical | 168.32 |  | 166.5467 | 1.0648 | 169.91 | 165.6 | 3.7013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TT | data_center_power_cooling | 474.175 |  | 474.1862 | -0.0024 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1027.35 |  | 1027.7075 | -0.0348 | 1035.07 | 1021.09 | 0.2346 | below_vwap | below_vwap |
| 14 | LITE | ai_networking_optical | 709.945 |  | 708.5638 | 0.1949 | 737.175 | 720.21 | 4.406 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | MU | memory_hbm_storage | 861.53 |  | 857.6081 | 0.4573 | 887.1 | 866.765 | 1.1747 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | AMAT | semiconductor_equipment | 564.02 |  | 570.3166 | -1.1041 | 572.69 | 562.32 | 2.0407 | below_vwap | below_vwap,spread_too_wide |
| 17 | KLAC | semiconductor_equipment | 220.95 |  | 221.0231 | -0.0331 | 222.19 | 218.09 | 4.0371 | below_vwap | below_vwap,spread_too_wide |
| 18 | ENTG | semiconductor_materials | 134.85 |  | 134.9908 | -0.1043 | 138.07 | 133.73 | 3.7523 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 667.55 |  | 671.8184 | -0.6354 | 680.09 | 667.1 | 2.3639 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 530.855 |  | 533.9626 | -0.582 | 543.4 | 535.47 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.4 |  | 399.0369 | 1.344 | 398.69 | 392.2 | 0.277 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.475 |  | 330.6012 | 0.2643 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.175 |  | 474.1862 | -0.0024 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 4 | LIN | industrial_gases | 516.87 |  | 515.0726 | 0.349 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.68 |  | 294.9085 | 0.2616 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.75 |  | 140.5162 | 0.1664 | 140.83 | 139.43 | 0.2629 | watch_only | none |
| 7 | GEV | data_center_power_cooling | 1027.35 |  | 1027.7075 | -0.0348 | 1035.07 | 1021.09 | 0.2346 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1799.75 |  | 1818.7911 | -1.0469 | 1823.13 | 1796.26 | 0.0845 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 564.02 |  | 570.3166 | -1.1041 | 572.69 | 562.32 | 2.0407 | below_vwap | below_vwap,spread_too_wide |
| 10 | KLAC | semiconductor_equipment | 220.95 |  | 221.0231 | -0.0331 | 222.19 | 218.09 | 4.0371 | below_vwap | below_vwap,spread_too_wide |
| 11 | SPY | market_regime | 751.36 |  | 752.4615 | -0.1464 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.745 |  | 296.1681 | -0.1429 | 296.28 | 294.65 | 0.0101 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 134.85 |  | 134.9908 | -0.1043 | 138.07 | 133.73 | 3.7523 | below_vwap | below_vwap,spread_too_wide |
| 15 | META | cloud_ai_capex | 667.55 |  | 671.8184 | -0.6354 | 680.09 | 667.1 | 2.3639 | below_vwap | below_vwap,spread_too_wide |
| 16 | ANET | ai_networking_optical | 168.32 |  | 166.5467 | 1.0648 | 169.91 | 165.6 | 3.7013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ARM | ai_accelerator | 258.665 |  | 257.2926 | 0.5334 | 265.96 | 258.1 | 3.866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MU | memory_hbm_storage | 861.53 |  | 857.6081 | 0.4573 | 887.1 | 866.765 | 1.1747 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | LITE | ai_networking_optical | 709.945 |  | 708.5638 | 0.1949 | 737.175 | 720.21 | 4.406 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | SOXX | semiconductor_index | 530.855 |  | 533.9626 | -0.582 | 543.4 | 535.47 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.9 |  | 709.5312 | -0.2299 | 713.55 | 708.25 | 0.0254 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.29 |  | 71.8619 | -0.7958 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.25 |  | 207.3732 | -0.0594 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.4 |  | 399.0369 | 1.344 | 398.69 | 392.2 | 0.277 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.475 |  | 330.6012 | 0.2643 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 360.1 |  | 369.8314 | -2.6313 | 375.18 | 369.2 | 2.08 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 498.04 |  | 504.3825 | -1.2575 | 518.33 | 507.62 | 1.524 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.205 |  | 409.0534 | -0.6963 | 414.385 | 406.61 | 0.8764 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.855 |  | 533.9626 | -0.582 | 543.4 | 535.47 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.63 |  | 572.1056 | -0.4327 | 580.31 | 572.21 | 0.0421 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.67 |  | 380.1338 | -0.6482 | 386.58 | 378.53 | 0.9717 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 861.53 |  | 857.6081 | 0.4573 | 887.1 | 866.765 | 1.1747 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 188.87 |  | 191.1666 | -1.2014 | 201.61 | 194.19 | 0.45 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.05 |  | 402.375 | -0.8263 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.525 |  | 45.8495 | -0.7078 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.005 |  | 25.3555 | -1.3825 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.36 |  | 752.4615 | -0.1464 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.745 |  | 296.1681 | -0.1429 | 296.28 | 294.65 | 0.0101 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.16 |  | 126.6597 | -0.3945 | 131.36 | 126.665 | 3.1706 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.015 |  | 73.3219 | -0.4186 | 75.54 | 73.985 | 1.7942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 290.61 |  | 293.636 | -1.0305 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.85 |  | 399.404 | -0.8898 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.355 |  | 631.4887 | -0.3379 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1027.35 |  | 1027.7075 | -0.0348 | 1035.07 | 1021.09 | 0.2346 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 474.175 |  | 474.1862 | -0.0024 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.75 |  | 140.5162 | 0.1664 | 140.83 | 139.43 | 0.2629 | watch_only | none |
| ANET | ai_networking_optical | 168.32 |  | 166.5467 | 1.0648 | 169.91 | 165.6 | 3.7013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.11 |  | 280.8648 | -0.9808 | 288.48 | 280.67 | 2.1574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 709.945 |  | 708.5638 | 0.1949 | 737.175 | 720.21 | 4.406 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 392.32 |  | 394.9934 | -0.6768 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.26 |  | 101.4561 | -1.1789 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 321.78 |  | 323.6439 | -0.5759 | 337.59 | 326.16 | 4.7797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1799.75 |  | 1818.7911 | -1.0469 | 1823.13 | 1796.26 | 0.0845 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.02 |  | 570.3166 | -1.1041 | 572.69 | 562.32 | 2.0407 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.435 |  | 323.032 | -1.1135 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.95 |  | 221.0231 | -0.0331 | 222.19 | 218.09 | 4.0371 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 324.83 |  | 326.7876 | -0.599 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 281.69 |  | 286.9266 | -1.8251 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.29 |  | 63.9912 | -1.0958 | 66.19 | 63.93 | 4.3293 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.13 |  | 51.9048 | -1.4927 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.85 |  | 134.9908 | -0.1043 | 138.07 | 133.73 | 3.7523 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 330.79 |  | 335.0551 | -1.273 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 516.87 |  | 515.0726 | 0.349 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.68 |  | 294.9085 | 0.2616 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.225 |  | 26.8119 | -2.1888 | 28.05 | 27.6 | 0.1144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.41 |  | 35.5164 | -0.2996 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.015 |  | 21.2306 | -1.0154 | 22.18 | 21.78 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1445.32 |  | 1465.3844 | -1.3692 | 1549.47 | 1482.06 | 3.4594 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 462.89 |  | 474.7192 | -2.4918 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 754.92 |  | 765.9587 | -1.4412 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 252.565 |  | 255.4339 | -1.1231 | 258.07 | 252.62 | 0.0158 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 667.55 |  | 671.8184 | -0.6354 | 680.09 | 667.1 | 2.3639 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.665 |  | 257.2926 | 0.5334 | 265.96 | 258.1 | 3.866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 157.33 |  | 161.893 | -2.8185 | 168.11 | 162.41 | 0.4894 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
