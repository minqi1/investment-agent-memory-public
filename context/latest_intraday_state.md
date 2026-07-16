# Intraday State

- Generated at: `2026-07-17T03:23:22+08:00`
- Market time ET: `2026-07-16T15:23:23-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 44, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 3, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.57 |  | 708.9728 | -0.621 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.45 |  | 533.4908 | -1.1323 | 543.4 | 535.47 | 0.0455 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.44 |  | 571.4698 | -0.8802 | 580.31 | 572.21 | 0.0653 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.72 |  | 752.0366 | -0.308 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.64 |  | 400.0246 | 0.6538 | 398.69 | 392.2 | 0.0571 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.135 |  | 331.277 | 0.8627 | 328.98 | 326.885 | 0.0269 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.64 |  | 400.0246 | 0.6538 | 398.69 | 392.2 | 0.0571 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 141.06 |  | 140.5663 | 0.3512 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | AAPL | mega_cap_platform | 334.135 |  | 331.277 | 0.8627 | 328.98 | 326.885 | 0.0269 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1030.12 |  | 1027.1375 | 0.2904 | 1035.07 | 1021.09 | 3.6811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | LIN | industrial_gases | 518.705 |  | 515.4267 | 0.636 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 167.44 |  | 166.5991 | 0.5047 | 169.91 | 165.6 | 4.306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | TT | data_center_power_cooling | 475.86 |  | 474.1964 | 0.3508 | 474.085 | 467.64 | 4.6905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | APD | industrial_gases | 296.74 |  | 295.0713 | 0.5655 | 293.89 | 291.35 | 2.6252 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | KLAC | semiconductor_equipment | 219.44 |  | 220.845 | -0.6362 | 222.19 | 218.09 | 0.0866 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 294.845 |  | 296.0058 | -0.3921 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | SOXX | semiconductor_index | 527.45 |  | 533.4908 | -1.1323 | 543.4 | 535.47 | 0.0455 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 13 | TSM | foundry | 406.24 |  | 408.6382 | -0.5869 | 414.385 | 406.61 | 0.0542 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | QQQ | market_regime | 704.57 |  | 708.9728 | -0.621 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | AVGO | custom_silicon_networking | 376.09 |  | 379.4515 | -0.8859 | 386.58 | 378.53 | 0.0931 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | ASML | semiconductor_equipment | 1790.71 |  | 1815.3236 | -1.3559 | 1823.13 | 1796.26 | 0.0514 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | SMH | semiconductor_index | 566.44 |  | 571.4698 | -0.8802 | 580.31 | 572.21 | 0.0653 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SPY | market_regime | 749.72 |  | 752.0366 | -0.308 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | HPE | ai_server_oem | 45.375 |  | 45.7401 | -0.7983 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | ALAB | ai_networking_optical | 317.115 |  | 323.0566 | -1.8392 | 337.59 | 326.16 | 0.1419 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.64 |  | 400.0246 | 0.6538 | 398.69 | 392.2 | 0.0571 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.135 |  | 331.277 | 0.8627 | 328.98 | 326.885 | 0.0269 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.86 |  | 474.1964 | 0.3508 | 474.085 | 467.64 | 4.6905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | JCI | data_center_power_cooling | 141.06 |  | 140.5663 | 0.3512 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 518.705 |  | 515.4267 | 0.636 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.74 |  | 295.0713 | 0.5655 | 293.89 | 291.35 | 2.6252 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | KLAC | semiconductor_equipment | 219.44 |  | 220.845 | -0.6362 | 222.19 | 218.09 | 0.0866 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 294.845 |  | 296.0058 | -0.3921 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ANET | ai_networking_optical | 167.44 |  | 166.5991 | 0.5047 | 169.91 | 165.6 | 4.306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | GEV | data_center_power_cooling | 1030.12 |  | 1027.1375 | 0.2904 | 1035.07 | 1021.09 | 3.6811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SOXX | semiconductor_index | 527.45 |  | 533.4908 | -1.1323 | 543.4 | 535.47 | 0.0455 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 13 | TSM | foundry | 406.24 |  | 408.6382 | -0.5869 | 414.385 | 406.61 | 0.0542 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | CIEN | ai_networking_optical | 388.87 |  | 393.5797 | -1.1966 | 410 | 397.68 | 0.3189 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 704.57 |  | 708.9728 | -0.621 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | AVGO | custom_silicon_networking | 376.09 |  | 379.4515 | -0.8859 | 386.58 | 378.53 | 0.0931 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | MU | memory_hbm_storage | 845.18 |  | 856.0033 | -1.2644 | 887.1 | 866.765 | 0.3076 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | VRT | data_center_power_cooling | 289.72 |  | 293.0751 | -1.1448 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 19 | NVDA | ai_accelerator | 206.76 |  | 207.3356 | -0.2776 | 211.03 | 207.49 | 0.3869 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | AMD | ai_accelerator | 495.5 |  | 502.9649 | -1.4842 | 518.33 | 507.62 | 0.9929 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.57 |  | 708.9728 | -0.621 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.3 |  | 71.7142 | -1.972 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.76 |  | 207.3356 | -0.2776 | 211.03 | 207.49 | 0.3869 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 402.64 |  | 400.0246 | 0.6538 | 398.69 | 392.2 | 0.0571 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 334.135 |  | 331.277 | 0.8627 | 328.98 | 326.885 | 0.0269 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 353.575 |  | 366.3887 | -3.4973 | 375.18 | 369.2 | 0.1867 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 495.5 |  | 502.9649 | -1.4842 | 518.33 | 507.62 | 0.9929 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.24 |  | 408.6382 | -0.5869 | 414.385 | 406.61 | 0.0542 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.45 |  | 533.4908 | -1.1323 | 543.4 | 535.47 | 0.0455 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.44 |  | 571.4698 | -0.8802 | 580.31 | 572.21 | 0.0653 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.09 |  | 379.4515 | -0.8859 | 386.58 | 378.53 | 0.0931 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 845.18 |  | 856.0033 | -1.2644 | 887.1 | 866.765 | 0.3076 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.26 |  | 190.6326 | -1.7692 | 201.61 | 194.19 | 0.1228 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 394.63 |  | 401.5804 | -1.7308 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.375 |  | 45.7401 | -0.7983 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.95 |  | 25.2909 | -1.3478 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.72 |  | 752.0366 | -0.308 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.845 |  | 296.0058 | -0.3921 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.75 |  | 126.4801 | -1.3679 | 131.36 | 126.665 | 0.2244 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.18 |  | 73.2953 | -0.1574 | 75.54 | 73.985 | 0.1503 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 289.72 |  | 293.0751 | -1.1448 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 397.44 |  | 399.1798 | -0.4358 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.01 |  | 631.1123 | -0.3331 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.12 |  | 1027.1375 | 0.2904 | 1035.07 | 1021.09 | 3.6811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.86 |  | 474.1964 | 0.3508 | 474.085 | 467.64 | 4.6905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.06 |  | 140.5663 | 0.3512 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.44 |  | 166.5991 | 0.5047 | 169.91 | 165.6 | 4.306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.85 |  | 280.4823 | -1.6515 | 288.48 | 280.67 | 0.7903 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 699.735 |  | 707.328 | -1.0735 | 737.175 | 720.21 | 2.9411 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.87 |  | 393.5797 | -1.1966 | 410 | 397.68 | 0.3189 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.5 |  | 101.1355 | -1.6172 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.115 |  | 323.0566 | -1.8392 | 337.59 | 326.16 | 0.1419 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ASML | semiconductor_equipment | 1790.71 |  | 1815.3236 | -1.3559 | 1823.13 | 1796.26 | 0.0514 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.93 |  | 569.3059 | -1.2956 | 572.69 | 562.32 | 0.7866 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.4 |  | 322.5256 | -1.2792 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.44 |  | 220.845 | -0.6362 | 222.19 | 218.09 | 0.0866 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.51 |  | 326.2287 | -1.4464 | 332.49 | 326.685 | 5.1009 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.31 |  | 285.8211 | -1.9282 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.84 |  | 63.8213 | -1.5376 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.85 |  | 51.7429 | -1.7257 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.06 |  | 134.6702 | -1.1957 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.82 |  | 333.8749 | -1.2145 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.705 |  | 515.4267 | 0.636 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.74 |  | 295.0713 | 0.5655 | 293.89 | 291.35 | 2.6252 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.32 |  | 26.7612 | -1.6486 | 28.05 | 27.6 | 0.038 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.37 |  | 35.5011 | -0.3692 | 37.365 | 36.4 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.99 |  | 21.1968 | -0.9758 | 22.18 | 21.78 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1397.82 |  | 1455.9102 | -3.99 | 1549.47 | 1482.06 | 4.2888 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.705 |  | 472.4266 | -2.6928 | 498.04 | 480.14 | 1.2595 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 743.38 |  | 762.3348 | -2.4864 | 797.155 | 768.7 | 0.2408 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 251.72 |  | 254.8578 | -1.2312 | 258.07 | 252.62 | 0.0238 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 664.02 |  | 670.7509 | -1.0035 | 680.09 | 667.1 | 0.3328 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 256.86 |  | 257.2531 | -0.1528 | 265.96 | 258.1 | 2.8498 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.455 |  | 161.3155 | -3.633 | 168.11 | 162.41 | 1.1 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
