# Intraday State

- Generated at: `2026-07-17T02:11:44+08:00`
- Market time ET: `2026-07-16T14:11:45-04:00`
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
| QQQ | market_regime | 706.87 |  | 709.6294 | -0.3888 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.12 |  | 534.3418 | -1.1644 | 543.4 | 535.47 | 0.0701 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.68 |  | 572.3238 | -0.9861 | 580.31 | 572.21 | 0.0688 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.04 |  | 752.5541 | -0.2012 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.74 |  | 398.7213 | 1.2587 | 398.69 | 392.2 | 0.0842 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.3 |  | 330.5952 | 0.2132 | 328.98 | 326.885 | 0.1781 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.3 |  | 330.5952 | 0.2132 | 328.98 | 326.885 | 0.1781 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.71 |  | 515.0358 | 0.3251 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MSFT | cloud_ai_capex | 403.74 |  | 398.7213 | 1.2587 | 398.69 | 392.2 | 0.0842 | buy_precheck_manual_confirm | none |
| 4 | APD | industrial_gases | 295.32 |  | 294.8886 | 0.1463 | 293.89 | 291.35 | 4.253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | META | cloud_ai_capex | 673.2 |  | 672.0687 | 0.1683 | 680.09 | 667.1 | 1.0354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.71 |  | 166.5126 | 0.7191 | 169.91 | 165.6 | 4.0546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | IWM | market_regime | 295.06 |  | 296.2037 | -0.3861 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | AMZN | cloud_ai_capex | 254.53 |  | 255.517 | -0.3863 | 258.07 | 252.62 | 0.0236 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | TT | data_center_power_cooling | 472.8 |  | 474.2638 | -0.3086 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 140.24 |  | 140.514 | -0.195 | 140.83 | 139.43 | 0.5633 | below_vwap | below_vwap,spread_too_wide |
| 12 | KLAC | semiconductor_equipment | 219.83 |  | 221.0368 | -0.546 | 222.19 | 218.09 | 1.1964 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 528.12 |  | 534.3418 | -1.1644 | 543.4 | 535.47 | 0.0701 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | QQQ | market_regime | 706.87 |  | 709.6294 | -0.3888 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | VRT | data_center_power_cooling | 288.55 |  | 293.8082 | -1.7897 | 300.385 | 293.64 | 0.104 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | NVDA | ai_accelerator | 206.8 |  | 207.3873 | -0.2832 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | ASML | semiconductor_equipment | 1795.05 |  | 1819.4176 | -1.3393 | 1823.13 | 1796.26 | 0.1153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SMH | semiconductor_index | 566.68 |  | 572.3238 | -0.9861 | 580.31 | 572.21 | 0.0688 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SPY | market_regime | 751.04 |  | 752.5541 | -0.2012 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | HPE | ai_server_oem | 45.09 |  | 45.8737 | -1.7083 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.74 |  | 398.7213 | 1.2587 | 398.69 | 392.2 | 0.0842 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.3 |  | 330.5952 | 0.2132 | 328.98 | 326.885 | 0.1781 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 516.71 |  | 515.0358 | 0.3251 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.32 |  | 294.8886 | 0.1463 | 293.89 | 291.35 | 4.253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TT | data_center_power_cooling | 472.8 |  | 474.2638 | -0.3086 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.24 |  | 140.514 | -0.195 | 140.83 | 139.43 | 0.5633 | below_vwap | below_vwap,spread_too_wide |
| 7 | KLAC | semiconductor_equipment | 219.83 |  | 221.0368 | -0.546 | 222.19 | 218.09 | 1.1964 | below_vwap | below_vwap,spread_too_wide |
| 8 | IWM | market_regime | 295.06 |  | 296.2037 | -0.3861 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | AMZN | cloud_ai_capex | 254.53 |  | 255.517 | -0.3863 | 258.07 | 252.62 | 0.0236 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 167.71 |  | 166.5126 | 0.7191 | 169.91 | 165.6 | 4.0546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | META | cloud_ai_capex | 673.2 |  | 672.0687 | 0.1683 | 680.09 | 667.1 | 1.0354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SOXX | semiconductor_index | 528.12 |  | 534.3418 | -1.1644 | 543.4 | 535.47 | 0.0701 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 405.03 |  | 409.2109 | -1.0217 | 414.385 | 406.61 | 0.6024 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 15 | CIEN | ai_networking_optical | 389.45 |  | 395.4075 | -1.5067 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 706.87 |  | 709.6294 | -0.3888 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 375.7 |  | 380.2767 | -1.2035 | 386.58 | 378.53 | 0.4844 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | MU | memory_hbm_storage | 849.15 |  | 857.7083 | -0.9978 | 887.1 | 866.765 | 0.6995 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 288.55 |  | 293.8082 | -1.7897 | 300.385 | 293.64 | 0.104 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | NVDA | ai_accelerator | 206.8 |  | 207.3873 | -0.2832 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.87 |  | 709.6294 | -0.3888 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.99 |  | 71.8974 | -1.262 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.8 |  | 207.3873 | -0.2832 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.74 |  | 398.7213 | 1.2587 | 398.69 | 392.2 | 0.0842 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.3 |  | 330.5952 | 0.2132 | 328.98 | 326.885 | 0.1781 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 363.45 |  | 371.2436 | -2.0993 | 375.18 | 369.2 | 0.8749 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 495.52 |  | 504.8145 | -1.8412 | 518.33 | 507.62 | 1.0292 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.03 |  | 409.2109 | -1.0217 | 414.385 | 406.61 | 0.6024 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.12 |  | 534.3418 | -1.1644 | 543.4 | 535.47 | 0.0701 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.68 |  | 572.3238 | -0.9861 | 580.31 | 572.21 | 0.0688 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.7 |  | 380.2767 | -1.2035 | 386.58 | 378.53 | 0.4844 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 849.15 |  | 857.7083 | -0.9978 | 887.1 | 866.765 | 0.6995 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.43 |  | 191.2843 | -2.0149 | 201.61 | 194.19 | 0.1601 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 398.28 |  | 402.4723 | -1.0416 | 411.65 | 400.635 | 4.2508 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.09 |  | 45.8737 | -1.7083 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.04 |  | 25.3803 | -1.3407 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.04 |  | 752.5541 | -0.2012 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.06 |  | 296.2037 | -0.3861 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.16 |  | 126.6766 | -0.4078 | 131.36 | 126.665 | 3.9632 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.57 |  | 73.3555 | -1.0708 | 75.54 | 73.985 | 1.75 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.55 |  | 293.8082 | -1.7897 | 300.385 | 293.64 | 0.104 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 394.5 |  | 399.4883 | -1.2487 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.32 |  | 631.6073 | -0.8371 | 640.25 | 631.005 | 0.1916 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1020.16 |  | 1027.8887 | -0.7519 | 1035.07 | 1021.09 | 4.5797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 472.8 |  | 474.2638 | -0.3086 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.24 |  | 140.514 | -0.195 | 140.83 | 139.43 | 0.5633 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 167.71 |  | 166.5126 | 0.7191 | 169.91 | 165.6 | 4.0546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.07 |  | 281.1159 | -2.1507 | 288.48 | 280.67 | 1.7777 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.92 |  | 708.93 | -1.553 | 737.175 | 720.21 | 2.9574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 389.45 |  | 395.4075 | -1.5067 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.465 |  | 101.5332 | -3.0219 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.43 |  | 323.7843 | -2.2714 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1795.05 |  | 1819.4176 | -1.3393 | 1823.13 | 1796.26 | 0.1153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.855 |  | 570.4779 | -1.6868 | 572.69 | 562.32 | 0.4636 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.03 |  | 323.1367 | -1.5803 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.83 |  | 221.0368 | -0.546 | 222.19 | 218.09 | 1.1964 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 321.87 |  | 326.8457 | -1.5223 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.58 |  | 287.3824 | -2.367 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.82 |  | 64.0258 | -1.8833 | 66.19 | 63.93 | 1.7829 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.61 |  | 51.9298 | -2.5415 | 52.72 | 51.735 | 0.6125 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 133.5 |  | 134.9985 | -1.11 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.25 |  | 337.2125 | -2.0647 | 346.26 | 338 | 4.6117 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.71 |  | 515.0358 | 0.3251 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.32 |  | 294.8886 | 0.1463 | 293.89 | 291.35 | 4.253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.15 |  | 26.8442 | -2.5861 | 28.05 | 27.6 | 0.0382 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.09 |  | 35.5332 | -1.2472 | 37.365 | 36.4 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.9 |  | 21.2379 | -1.5912 | 22.18 | 21.78 | 0.0957 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1424.49 |  | 1466.8093 | -2.8851 | 1549.47 | 1482.06 | 3.51 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.23 |  | 475.0597 | -3.3321 | 498.04 | 480.14 | 1.0039 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 748.88 |  | 766.5251 | -2.302 | 797.155 | 768.7 | 4.7057 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 254.53 |  | 255.517 | -0.3863 | 258.07 | 252.62 | 0.0236 | below_vwap | below_vwap |
| META | cloud_ai_capex | 673.2 |  | 672.0687 | 0.1683 | 680.09 | 667.1 | 1.0354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 256.95 |  | 257.2818 | -0.129 | 265.96 | 258.1 | 3.0356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.63 |  | 162.0247 | -3.3295 | 168.11 | 162.41 | 0.2809 | below_opening_15m_low | below_opening_15m_low,below_vwap |
