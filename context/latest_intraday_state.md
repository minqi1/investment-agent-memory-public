# Intraday State

- Generated at: `2026-07-17T02:07:48+08:00`
- Market time ET: `2026-07-16T14:07:49-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 4, 'below_vwap': 8, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.535 |  | 709.6781 | -0.4429 | 713.55 | 708.25 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 525.99 |  | 534.3869 | -1.5713 | 543.4 | 535.47 | 0.0646 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.21 |  | 572.377 | -1.2521 | 580.31 | 572.21 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.83 |  | 752.6104 | -0.2366 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.55 |  | 515.0255 | 0.296 | 515.825 | 512.23 | 0.2594 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.195 |  | 294.8871 | 0.1044 | 293.89 | 291.35 | 0.2507 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 402.78 |  | 398.61 | 1.0461 | 398.69 | 392.2 | 0.211 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.4 |  | 330.5761 | 0.2492 | 328.98 | 326.885 | 0.1811 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.55 |  | 515.0255 | 0.296 | 515.825 | 512.23 | 0.2594 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.195 |  | 294.8871 | 0.1044 | 293.89 | 291.35 | 0.2507 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.4 |  | 330.5761 | 0.2492 | 328.98 | 326.885 | 0.1811 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.845 |  | 166.4963 | 0.2095 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 402.78 |  | 398.61 | 1.0461 | 398.69 | 392.2 | 0.211 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 218.91 |  | 221.0672 | -0.9758 | 222.19 | 218.09 | 0.0822 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 294.85 |  | 296.2318 | -0.4665 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | TT | data_center_power_cooling | 472.45 |  | 474.3392 | -0.3983 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 140.16 |  | 140.5212 | -0.2571 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GOOGL | cloud_ai_capex | 370.42 |  | 371.8326 | -0.3799 | 375.18 | 369.2 | 0.6506 | below_vwap | below_vwap,spread_too_wide |
| 12 | AMZN | cloud_ai_capex | 254.84 |  | 255.5379 | -0.2731 | 258.07 | 252.62 | 1.0242 | below_vwap | below_vwap,spread_too_wide |
| 13 | META | cloud_ai_capex | 669 |  | 672.1892 | -0.4744 | 680.09 | 667.1 | 0.4245 | below_vwap | below_vwap,spread_too_wide |
| 14 | SOXX | semiconductor_index | 525.99 |  | 534.3869 | -1.5713 | 543.4 | 535.47 | 0.0646 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 706.535 |  | 709.6781 | -0.4429 | 713.55 | 708.25 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | MU | memory_hbm_storage | 844.01 |  | 857.8186 | -1.6097 | 887.1 | 866.765 | 0.09 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.37 |  | 207.3989 | -0.4961 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1790.48 |  | 1819.5919 | -1.5999 | 1823.13 | 1796.26 | 0.1011 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 565.21 |  | 572.377 | -1.2521 | 580.31 | 572.21 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SPY | market_regime | 750.83 |  | 752.6104 | -0.2366 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.55 |  | 515.0255 | 0.296 | 515.825 | 512.23 | 0.2594 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.195 |  | 294.8871 | 0.1044 | 293.89 | 291.35 | 0.2507 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 402.78 |  | 398.61 | 1.0461 | 398.69 | 392.2 | 0.211 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.4 |  | 330.5761 | 0.2492 | 328.98 | 326.885 | 0.1811 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 472.45 |  | 474.3392 | -0.3983 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.16 |  | 140.5212 | -0.2571 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 218.91 |  | 221.0672 | -0.9758 | 222.19 | 218.09 | 0.0822 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 294.85 |  | 296.2318 | -0.4665 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | GOOGL | cloud_ai_capex | 370.42 |  | 371.8326 | -0.3799 | 375.18 | 369.2 | 0.6506 | below_vwap | below_vwap,spread_too_wide |
| 11 | AMZN | cloud_ai_capex | 254.84 |  | 255.5379 | -0.2731 | 258.07 | 252.62 | 1.0242 | below_vwap | below_vwap,spread_too_wide |
| 12 | META | cloud_ai_capex | 669 |  | 672.1892 | -0.4744 | 680.09 | 667.1 | 0.4245 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 166.845 |  | 166.4963 | 0.2095 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SOXX | semiconductor_index | 525.99 |  | 534.3869 | -1.5713 | 543.4 | 535.47 | 0.0646 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | TSM | foundry | 404.26 |  | 409.2436 | -1.2178 | 414.385 | 406.61 | 0.4082 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 16 | CIEN | ai_networking_optical | 388.86 |  | 395.422 | -1.6595 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 17 | QQQ | market_regime | 706.535 |  | 709.6781 | -0.4429 | 713.55 | 708.25 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AVGO | custom_silicon_networking | 376.43 |  | 380.4223 | -1.0494 | 386.58 | 378.53 | 1.5939 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | MU | memory_hbm_storage | 844.01 |  | 857.8186 | -1.6097 | 887.1 | 866.765 | 0.09 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | VRT | data_center_power_cooling | 288.11 |  | 293.9426 | -1.9843 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.535 |  | 709.6781 | -0.4429 | 713.55 | 708.25 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.9 |  | 71.9149 | -1.4113 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.37 |  | 207.3989 | -0.4961 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.78 |  | 398.61 | 1.0461 | 398.69 | 392.2 | 0.211 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.4 |  | 330.5761 | 0.2492 | 328.98 | 326.885 | 0.1811 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.42 |  | 371.8326 | -0.3799 | 375.18 | 369.2 | 0.6506 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 493.78 |  | 505.0142 | -2.2245 | 518.33 | 507.62 | 0.6602 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 404.26 |  | 409.2436 | -1.2178 | 414.385 | 406.61 | 0.4082 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.99 |  | 534.3869 | -1.5713 | 543.4 | 535.47 | 0.0646 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.21 |  | 572.377 | -1.2521 | 580.31 | 572.21 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.43 |  | 380.4223 | -1.0494 | 386.58 | 378.53 | 1.5939 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 844.01 |  | 857.8186 | -1.6097 | 887.1 | 866.765 | 0.09 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.16 |  | 191.372 | -2.2009 | 201.61 | 194.19 | 0.8121 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 396 |  | 402.5561 | -1.6286 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.83 |  | 45.8839 | -2.297 | 47.65 | 46.165 | 0.0223 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.91 |  | 25.3869 | -1.8785 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.83 |  | 752.6104 | -0.2366 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.85 |  | 296.2318 | -0.4665 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.775 |  | 126.6828 | -0.7166 | 131.36 | 126.665 | 0.7235 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.24 |  | 73.3627 | -1.5303 | 75.54 | 73.985 | 2.727 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.11 |  | 293.9426 | -1.9843 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 393.95 |  | 399.5145 | -1.3928 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 625.37 |  | 631.6252 | -0.9903 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1017.82 |  | 1027.9743 | -0.9878 | 1035.07 | 1021.09 | 1.4187 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 472.45 |  | 474.3392 | -0.3983 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.16 |  | 140.5212 | -0.2571 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.845 |  | 166.4963 | 0.2095 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 274.73 |  | 281.1881 | -2.2967 | 288.48 | 280.67 | 0.1492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LITE | ai_networking_optical | 697.96 |  | 709.0787 | -1.568 | 737.175 | 720.21 | 2.8956 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.86 |  | 395.422 | -1.6595 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.25 |  | 101.5624 | -3.2614 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 315.84 |  | 323.8594 | -2.4762 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1790.48 |  | 1819.5919 | -1.5999 | 1823.13 | 1796.26 | 0.1011 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 559.27 |  | 570.7089 | -2.0043 | 572.69 | 562.32 | 1.2892 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 316.4 |  | 323.2265 | -2.112 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.91 |  | 221.0672 | -0.9758 | 222.19 | 218.09 | 0.0822 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 320.19 |  | 326.8916 | -2.0501 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.01 |  | 287.8195 | -2.7133 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.555 |  | 64.0571 | -2.345 | 66.19 | 63.93 | 1.4068 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.4 |  | 51.9564 | -2.9957 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.42 |  | 135.0109 | -1.1784 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.54 |  | 337.344 | -2.3134 | 346.26 | 338 | 0.6433 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.55 |  | 515.0255 | 0.296 | 515.825 | 512.23 | 0.2594 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 295.195 |  | 294.8871 | 0.1044 | 293.89 | 291.35 | 0.2507 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 25.97 |  | 26.8524 | -3.2861 | 28.05 | 27.6 | 0.077 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.045 |  | 35.5378 | -1.3867 | 37.365 | 36.4 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.815 |  | 21.2412 | -2.0065 | 22.18 | 21.78 | 0.048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1413.64 |  | 1467.2742 | -3.6554 | 1549.47 | 1482.06 | 3.1819 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 455.44 |  | 475.2102 | -4.1603 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 741.82 |  | 766.7592 | -3.2525 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 254.84 |  | 255.5379 | -0.2731 | 258.07 | 252.62 | 1.0242 | below_vwap | below_vwap,spread_too_wide |
| META | cloud_ai_capex | 669 |  | 672.1892 | -0.4744 | 680.09 | 667.1 | 0.4245 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.87 |  | 257.2892 | -0.5516 | 265.96 | 258.1 | 2.4466 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.97 |  | 162.0636 | -3.76 | 168.11 | 162.41 | 1.09 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
