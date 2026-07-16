# Intraday State

- Generated at: `2026-07-17T01:23:54+08:00`
- Market time ET: `2026-07-16T13:23:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 2, 'below_vwap': 10, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.62 |  | 709.8755 | -0.3177 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.715 |  | 535.8674 | -1.5213 | 543.4 | 535.47 | 0.055 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.12 |  | 573.3135 | -1.0803 | 580.31 | 572.21 | 0.0423 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.135 |  | 752.7266 | -0.0786 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.945 |  | 397.9205 | 1.2627 | 398.69 | 392.2 | 0.0521 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.56 |  | 330.1437 | 0.7319 | 328.98 | 326.885 | 0.0932 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.56 |  | 330.1437 | 0.7319 | 328.98 | 326.885 | 0.0932 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 256.32 |  | 255.5162 | 0.3146 | 258.07 | 252.62 | 0.2185 | watch_only | none |
| 3 | TT | data_center_power_cooling | 475.27 |  | 474.2727 | 0.2103 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 294.905 |  | 294.8599 | 0.0153 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 402.945 |  | 397.9205 | 1.2627 | 398.69 | 392.2 | 0.0521 | buy_precheck_manual_confirm | none |
| 6 | LIN | industrial_gases | 515.51 |  | 514.9261 | 0.1134 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ANET | ai_networking_optical | 167.225 |  | 166.4459 | 0.4681 | 169.91 | 165.6 | 4.5388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1801.36 |  | 1821.6665 | -1.1147 | 1823.13 | 1796.26 | 0.1182 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 752.135 |  | 752.7266 | -0.0786 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.585 |  | 296.382 | -0.2689 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.44 |  | 371.8581 | -0.1124 | 375.18 | 369.2 | 0.0619 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 140.485 |  | 140.5417 | -0.0403 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | META | cloud_ai_capex | 669.71 |  | 672.9296 | -0.4784 | 680.09 | 667.1 | 0.209 | below_vwap | below_vwap |
| 15 | ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | AMAT | semiconductor_equipment | 564.11 |  | 572.4527 | -1.4574 | 572.69 | 562.32 | 1.9659 | below_vwap | below_vwap,spread_too_wide |
| 17 | KLAC | semiconductor_equipment | 218.43 |  | 221.4744 | -1.3746 | 222.19 | 218.09 | 0.5768 | below_vwap | below_vwap,spread_too_wide |
| 18 | SOXX | semiconductor_index | 527.715 |  | 535.8674 | -1.5213 | 543.4 | 535.47 | 0.055 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | QQQ | market_regime | 707.62 |  | 709.8755 | -0.3177 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | MU | memory_hbm_storage | 842.58 |  | 859.3619 | -1.9528 | 887.1 | 866.765 | 0.0712 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.945 |  | 397.9205 | 1.2627 | 398.69 | 392.2 | 0.0521 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.56 |  | 330.1437 | 0.7319 | 328.98 | 326.885 | 0.0932 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.27 |  | 474.2727 | 0.2103 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 294.905 |  | 294.8599 | 0.0153 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | AMZN | cloud_ai_capex | 256.32 |  | 255.5162 | 0.3146 | 258.07 | 252.62 | 0.2185 | watch_only | none |
| 6 | JCI | data_center_power_cooling | 140.485 |  | 140.5417 | -0.0403 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | ASML | semiconductor_equipment | 1801.36 |  | 1821.6665 | -1.1147 | 1823.13 | 1796.26 | 0.1182 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 564.11 |  | 572.4527 | -1.4574 | 572.69 | 562.32 | 1.9659 | below_vwap | below_vwap,spread_too_wide |
| 9 | KLAC | semiconductor_equipment | 218.43 |  | 221.4744 | -1.3746 | 222.19 | 218.09 | 0.5768 | below_vwap | below_vwap,spread_too_wide |
| 10 | SPY | market_regime | 752.135 |  | 752.7266 | -0.0786 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.585 |  | 296.382 | -0.2689 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 371.44 |  | 371.8581 | -0.1124 | 375.18 | 369.2 | 0.0619 | below_vwap | below_vwap |
| 15 | META | cloud_ai_capex | 669.71 |  | 672.9296 | -0.4784 | 680.09 | 667.1 | 0.209 | below_vwap | below_vwap |
| 16 | ANET | ai_networking_optical | 167.225 |  | 166.4459 | 0.4681 | 169.91 | 165.6 | 4.5388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LIN | industrial_gases | 515.51 |  | 514.9261 | 0.1134 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SOXX | semiconductor_index | 527.715 |  | 535.8674 | -1.5213 | 543.4 | 535.47 | 0.055 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | TSM | foundry | 405.39 |  | 410.0731 | -1.142 | 414.385 | 406.61 | 0.3379 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | CIEN | ai_networking_optical | 389.8 |  | 396.1272 | -1.5973 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.62 |  | 709.8755 | -0.3177 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.22 |  | 72.013 | -1.1012 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.02 |  | 207.4913 | -0.2272 | 211.03 | 207.49 | 0.0338 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.945 |  | 397.9205 | 1.2627 | 398.69 | 392.2 | 0.0521 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.56 |  | 330.1437 | 0.7319 | 328.98 | 326.885 | 0.0932 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.44 |  | 371.8581 | -0.1124 | 375.18 | 369.2 | 0.0619 | below_vwap | below_vwap |
| AMD | ai_accelerator | 496.455 |  | 506.6271 | -2.0078 | 518.33 | 507.62 | 0.4673 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.39 |  | 410.0731 | -1.142 | 414.385 | 406.61 | 0.3379 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.715 |  | 535.8674 | -1.5213 | 543.4 | 535.47 | 0.055 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.12 |  | 573.3135 | -1.0803 | 580.31 | 572.21 | 0.0423 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.34 |  | 380.9388 | -0.9447 | 386.58 | 378.53 | 1.5901 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 842.58 |  | 859.3619 | -1.9528 | 887.1 | 866.765 | 0.0712 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.4 |  | 192.1504 | -2.4722 | 201.61 | 194.19 | 1.4354 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.365 |  | 403.2585 | -0.7175 | 411.65 | 400.635 | 4.5059 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.345 |  | 45.9905 | -1.4035 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.07 |  | 25.4576 | -1.5227 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.135 |  | 752.7266 | -0.0786 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |
| IWM | market_regime | 295.585 |  | 296.382 | -0.2689 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.51 |  | 126.7439 | -0.1845 | 131.36 | 126.665 | 0.4585 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.065 |  | 73.4973 | -0.5881 | 75.54 | 73.985 | 0.0411 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 291.2 |  | 294.6324 | -1.165 | 300.385 | 293.64 | 2.239 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.475 |  | 399.7709 | -1.3247 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.57 |  | 632.0001 | -0.3845 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1019.36 |  | 1029.0588 | -0.9425 | 1035.07 | 1021.09 | 4.8697 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.27 |  | 474.2727 | 0.2103 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.485 |  | 140.5417 | -0.0403 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.225 |  | 166.4459 | 0.4681 | 169.91 | 165.6 | 4.5388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.64 |  | 281.8547 | -1.8501 | 288.48 | 280.67 | 1.0917 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 696.475 |  | 710.6584 | -1.9958 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 389.8 |  | 396.1272 | -1.5973 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.69 |  | 101.9934 | -3.2389 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 314.81 |  | 324.1885 | -2.8929 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1801.36 |  | 1821.6665 | -1.1147 | 1823.13 | 1796.26 | 0.1182 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.11 |  | 572.4527 | -1.4574 | 572.69 | 562.32 | 1.9659 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.24 |  | 324.7943 | -1.7101 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.43 |  | 221.4744 | -1.3746 | 222.19 | 218.09 | 0.5768 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.89 |  | 327.4097 | -1.3804 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 282.16 |  | 289.1333 | -2.4118 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.65 |  | 64.2675 | -2.5168 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.415 |  | 52.2393 | -1.578 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 332.49 |  | 338.4274 | -1.7544 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 515.51 |  | 514.9261 | 0.1134 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 294.905 |  | 294.8599 | 0.0153 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.135 |  | 26.9939 | -3.1819 | 28.05 | 27.6 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.66 |  | 35.6767 | -2.8496 | 37.365 | 36.4 | 0.0289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.805 |  | 21.3028 | -2.3368 | 22.18 | 21.78 | 0.0961 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1424.61 |  | 1473.2302 | -3.3002 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 457.43 |  | 476.8949 | -4.0816 | 498.04 | 480.14 | 3.5765 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 748.59 |  | 768.61 | -2.6047 | 797.155 | 768.7 | 3.0818 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.32 |  | 255.5162 | 0.3146 | 258.07 | 252.62 | 0.2185 | watch_only | none |
| META | cloud_ai_capex | 669.71 |  | 672.9296 | -0.4784 | 680.09 | 667.1 | 0.209 | below_vwap | below_vwap |
| ARM | ai_accelerator | 255.23 |  | 257.4315 | -0.8552 | 265.96 | 258.1 | 3.918 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.42 |  | 162.8723 | -3.9616 | 168.11 | 162.41 | 3.0942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
