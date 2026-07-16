# Intraday State

- Generated at: `2026-07-17T02:31:43+08:00`
- Market time ET: `2026-07-16T14:31:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 8, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.65 |  | 709.5106 | -0.4032 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.32 |  | 533.9376 | -0.8648 | 543.4 | 535.47 | 0.0529 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.75 |  | 572.0625 | -0.7539 | 580.31 | 572.21 | 0.081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.67 |  | 752.4446 | -0.2358 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.04 |  | 399.1363 | 1.2286 | 398.69 | 392.2 | 0.0594 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.205 |  | 330.6078 | 0.1806 | 328.98 | 326.885 | 0.3351 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.205 |  | 330.6078 | 0.1806 | 328.98 | 326.885 | 0.3351 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 404.04 |  | 399.1363 | 1.2286 | 398.69 | 392.2 | 0.0594 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.52 |  | 140.5164 | 0.0026 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.68 |  | 294.9107 | 0.2608 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 517.425 |  | 515.0919 | 0.4529 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 168.04 |  | 166.5648 | 0.8857 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 220.1 |  | 221.0202 | -0.4163 | 222.19 | 218.09 | 0.1272 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.375 |  | 296.166 | -0.2671 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | AMZN | cloud_ai_capex | 252.84 |  | 255.4173 | -1.0091 | 258.07 | 252.62 | 0.0514 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ARM | ai_accelerator | 257.685 |  | 257.2967 | 0.1509 | 265.96 | 258.1 | 3.0425 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 12 | TT | data_center_power_cooling | 473.68 |  | 474.1751 | -0.1044 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 134.78 |  | 134.9873 | -0.1536 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1023.85 |  | 1027.7001 | -0.3746 | 1035.07 | 1021.09 | 2.6283 | below_vwap | below_vwap,spread_too_wide |
| 15 | META | cloud_ai_capex | 668.255 |  | 671.7385 | -0.5186 | 680.09 | 667.1 | 2.2222 | below_vwap | below_vwap,spread_too_wide |
| 16 | SOXX | semiconductor_index | 529.32 |  | 533.9376 | -0.8648 | 543.4 | 535.47 | 0.0529 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 706.65 |  | 709.5106 | -0.4032 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1795.27 |  | 1818.7289 | -1.2899 | 1823.13 | 1796.26 | 0.1008 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 567.75 |  | 572.0625 | -0.7539 | 580.31 | 572.21 | 0.081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SPY | market_regime | 750.67 |  | 752.4446 | -0.2358 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.04 |  | 399.1363 | 1.2286 | 398.69 | 392.2 | 0.0594 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.205 |  | 330.6078 | 0.1806 | 328.98 | 326.885 | 0.3351 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 517.425 |  | 515.0919 | 0.4529 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.68 |  | 294.9107 | 0.2608 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 473.68 |  | 474.1751 | -0.1044 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1023.85 |  | 1027.7001 | -0.3746 | 1035.07 | 1021.09 | 2.6283 | below_vwap | below_vwap,spread_too_wide |
| 7 | KLAC | semiconductor_equipment | 220.1 |  | 221.0202 | -0.4163 | 222.19 | 218.09 | 0.1272 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.375 |  | 296.166 | -0.2671 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ENTG | semiconductor_materials | 134.78 |  | 134.9873 | -0.1536 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | AMZN | cloud_ai_capex | 252.84 |  | 255.4173 | -1.0091 | 258.07 | 252.62 | 0.0514 | below_vwap | below_vwap |
| 12 | META | cloud_ai_capex | 668.255 |  | 671.7385 | -0.5186 | 680.09 | 667.1 | 2.2222 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 168.04 |  | 166.5648 | 0.8857 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 140.52 |  | 140.5164 | 0.0026 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ARM | ai_accelerator | 257.685 |  | 257.2967 | 0.1509 | 265.96 | 258.1 | 3.0425 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | SOXX | semiconductor_index | 529.32 |  | 533.9376 | -0.8648 | 543.4 | 535.47 | 0.0529 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | TSM | foundry | 405.59 |  | 409.0168 | -0.8378 | 414.385 | 406.61 | 0.6189 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 392.08 |  | 394.9728 | -0.7324 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 19 | QQQ | market_regime | 706.65 |  | 709.5106 | -0.4032 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AVGO | custom_silicon_networking | 376.65 |  | 380.1021 | -0.9082 | 386.58 | 378.53 | 0.6903 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.65 |  | 709.5106 | -0.4032 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.94 |  | 71.8535 | -1.2714 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.72 |  | 207.369 | -0.313 | 211.03 | 207.49 | 0.3773 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 404.04 |  | 399.1363 | 1.2286 | 398.69 | 392.2 | 0.0594 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.205 |  | 330.6078 | 0.1806 | 328.98 | 326.885 | 0.3351 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 360.745 |  | 369.5801 | -2.3906 | 375.18 | 369.2 | 0.1469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 496.99 |  | 504.3357 | -1.4565 | 518.33 | 507.62 | 1.1167 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.59 |  | 409.0168 | -0.8378 | 414.385 | 406.61 | 0.6189 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.32 |  | 533.9376 | -0.8648 | 543.4 | 535.47 | 0.0529 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.75 |  | 572.0625 | -0.7539 | 580.31 | 572.21 | 0.081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.65 |  | 380.1021 | -0.9082 | 386.58 | 378.53 | 0.6903 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 854.15 |  | 857.5966 | -0.4019 | 887.1 | 866.765 | 1.728 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.03 |  | 191.1309 | -1.6224 | 201.61 | 194.19 | 0.0957 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 397.755 |  | 402.3557 | -1.1434 | 411.65 | 400.635 | 3.7309 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.31 |  | 45.839 | -1.1541 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.87 |  | 25.3518 | -1.9005 | 26.71 | 25.74 | 0.0402 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.67 |  | 752.4446 | -0.2358 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.375 |  | 296.166 | -0.2671 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.94 |  | 126.6529 | -0.5629 | 131.36 | 126.665 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.97 |  | 73.3184 | -0.4752 | 75.54 | 73.985 | 0.1096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 289.27 |  | 293.6169 | -1.4805 | 300.385 | 293.64 | 1.4727 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 395.26 |  | 399.3857 | -1.033 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 628.84 |  | 631.4803 | -0.4181 | 640.25 | 631.005 | 4.8009 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1023.85 |  | 1027.7001 | -0.3746 | 1035.07 | 1021.09 | 2.6283 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.68 |  | 474.1751 | -0.1044 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.52 |  | 140.5164 | 0.0026 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.04 |  | 166.5648 | 0.8857 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.66 |  | 280.8417 | -1.489 | 288.48 | 280.67 | 1.0446 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 705.75 |  | 708.5726 | -0.3983 | 737.175 | 720.21 | 0.1573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 392.08 |  | 394.9728 | -0.7324 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.46 |  | 101.4407 | -1.9526 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 321.23 |  | 323.6146 | -0.7369 | 337.59 | 326.16 | 0.3113 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ASML | semiconductor_equipment | 1795.27 |  | 1818.7289 | -1.2899 | 1823.13 | 1796.26 | 0.1008 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.605 |  | 570.281 | -1.5214 | 572.69 | 562.32 | 1.672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.83 |  | 323.0213 | -1.2975 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.1 |  | 221.0202 | -0.4163 | 222.19 | 218.09 | 0.1272 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 323.54 |  | 326.7762 | -0.9904 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.64 |  | 286.8005 | -2.148 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.09 |  | 63.9812 | -1.3929 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.13 |  | 51.9048 | -1.4927 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.78 |  | 134.9873 | -0.1536 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.79 |  | 335.0419 | -1.5675 | 346.26 | 338 | 4.1996 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 517.425 |  | 515.0919 | 0.4529 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.68 |  | 294.9107 | 0.2608 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.07 |  | 26.8096 | -2.7587 | 28.05 | 27.6 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.08 |  | 35.5139 | -1.2216 | 37.365 | 36.4 | 0.057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.91 |  | 21.2273 | -1.4949 | 22.18 | 21.78 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1423.42 |  | 1464.7887 | -2.8242 | 1549.47 | 1482.06 | 2.2565 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 461.425 |  | 474.6652 | -2.7894 | 498.04 | 480.14 | 1.3025 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 748.69 |  | 765.877 | -2.2441 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 252.84 |  | 255.4173 | -1.0091 | 258.07 | 252.62 | 0.0514 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.255 |  | 671.7385 | -0.5186 | 680.09 | 667.1 | 2.2222 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 257.685 |  | 257.2967 | 0.1509 | 265.96 | 258.1 | 3.0425 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| SKHY | memory_hbm_storage | 156.765 |  | 161.8673 | -3.1521 | 168.11 | 162.41 | 1.6394 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
