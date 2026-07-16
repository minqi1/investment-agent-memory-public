# Intraday State

- Generated at: `2026-07-17T02:03:46+08:00`
- Market time ET: `2026-07-16T14:03:47-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'below_vwap': 9, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.52 |  | 709.6908 | -0.4468 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.235 |  | 534.4284 | -1.5331 | 543.4 | 535.47 | 0.0627 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.94 |  | 572.4016 | -1.3036 | 580.31 | 572.21 | 0.062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.14 |  | 752.6448 | -0.1999 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.01 |  | 398.5578 | 1.1171 | 398.69 | 392.2 | 0.0819 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.28 |  | 330.5683 | 0.2153 | 328.98 | 326.885 | 0.0513 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.28 |  | 330.5683 | 0.2153 | 328.98 | 326.885 | 0.0513 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.51 |  | 515.0166 | 0.29 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MSFT | cloud_ai_capex | 403.01 |  | 398.5578 | 1.1171 | 398.69 | 392.2 | 0.0819 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 167.05 |  | 166.4937 | 0.3341 | 169.91 | 165.6 | 3.3224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 295.26 |  | 294.885 | 0.1272 | 293.89 | 291.35 | 4.2336 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | JCI | data_center_power_cooling | 140.31 |  | 140.5297 | -0.1563 | 140.83 | 139.43 | 0.0713 | below_vwap | below_vwap |
| 7 | KLAC | semiconductor_equipment | 218.66 |  | 221.0782 | -1.0938 | 222.19 | 218.09 | 0.096 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 751.14 |  | 752.6448 | -0.1999 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 294.875 |  | 296.254 | -0.4655 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | GOOGL | cloud_ai_capex | 371.24 |  | 371.8393 | -0.1612 | 375.18 | 369.2 | 0.1158 | below_vwap | below_vwap |
| 11 | AMZN | cloud_ai_capex | 255.01 |  | 255.5429 | -0.2085 | 258.07 | 252.62 | 0.0157 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | TT | data_center_power_cooling | 473.81 |  | 474.4056 | -0.1255 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | META | cloud_ai_capex | 668.92 |  | 672.2377 | -0.4935 | 680.09 | 667.1 | 0.3558 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 526.235 |  | 534.4284 | -1.5331 | 543.4 | 535.47 | 0.0627 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 706.52 |  | 709.6908 | -0.4468 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.68 |  | 207.4076 | -0.3508 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1793.795 |  | 1819.7614 | -1.4269 | 1823.13 | 1796.26 | 0.0714 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AMAT | semiconductor_equipment | 559.68 |  | 570.8009 | -1.9483 | 572.69 | 562.32 | 0.1001 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 564.94 |  | 572.4016 | -1.3036 | 580.31 | 572.21 | 0.062 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.01 |  | 398.5578 | 1.1171 | 398.69 | 392.2 | 0.0819 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.28 |  | 330.5683 | 0.2153 | 328.98 | 326.885 | 0.0513 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 516.51 |  | 515.0166 | 0.29 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.26 |  | 294.885 | 0.1272 | 293.89 | 291.35 | 4.2336 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TT | data_center_power_cooling | 473.81 |  | 474.4056 | -0.1255 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.31 |  | 140.5297 | -0.1563 | 140.83 | 139.43 | 0.0713 | below_vwap | below_vwap |
| 7 | KLAC | semiconductor_equipment | 218.66 |  | 221.0782 | -1.0938 | 222.19 | 218.09 | 0.096 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 751.14 |  | 752.6448 | -0.1999 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 294.875 |  | 296.254 | -0.4655 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GOOGL | cloud_ai_capex | 371.24 |  | 371.8393 | -0.1612 | 375.18 | 369.2 | 0.1158 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 255.01 |  | 255.5429 | -0.2085 | 258.07 | 252.62 | 0.0157 | below_vwap | below_vwap |
| 13 | META | cloud_ai_capex | 668.92 |  | 672.2377 | -0.4935 | 680.09 | 667.1 | 0.3558 | below_vwap | below_vwap,spread_too_wide |
| 14 | ANET | ai_networking_optical | 167.05 |  | 166.4937 | 0.3341 | 169.91 | 165.6 | 3.3224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SOXX | semiconductor_index | 526.235 |  | 534.4284 | -1.5331 | 543.4 | 535.47 | 0.0627 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.07 |  | 409.3083 | -1.2798 | 414.385 | 406.61 | 0.7721 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | CIEN | ai_networking_optical | 388.54 |  | 395.4586 | -1.7495 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 706.52 |  | 709.6908 | -0.4468 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 376.36 |  | 380.4513 | -1.0754 | 386.58 | 378.53 | 1.5942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 843.53 |  | 857.9442 | -1.6801 | 887.1 | 866.765 | 0.3497 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.52 |  | 709.6908 | -0.4468 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.91 |  | 71.9181 | -1.4018 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.68 |  | 207.4076 | -0.3508 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.01 |  | 398.5578 | 1.1171 | 398.69 | 392.2 | 0.0819 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.28 |  | 330.5683 | 0.2153 | 328.98 | 326.885 | 0.0513 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.24 |  | 371.8393 | -0.1612 | 375.18 | 369.2 | 0.1158 | below_vwap | below_vwap |
| AMD | ai_accelerator | 493.47 |  | 505.1303 | -2.3084 | 518.33 | 507.62 | 0.4681 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 404.07 |  | 409.3083 | -1.2798 | 414.385 | 406.61 | 0.7721 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.235 |  | 534.4284 | -1.5331 | 543.4 | 535.47 | 0.0627 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.94 |  | 572.4016 | -1.3036 | 580.31 | 572.21 | 0.062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.36 |  | 380.4513 | -1.0754 | 386.58 | 378.53 | 1.5942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 843.53 |  | 857.9442 | -1.6801 | 887.1 | 866.765 | 0.3497 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 186.59 |  | 191.4175 | -2.522 | 201.61 | 194.19 | 0.4395 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 395.48 |  | 402.6162 | -1.7724 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.82 |  | 45.8882 | -2.3278 | 47.65 | 46.165 | 0.0446 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.935 |  | 25.3932 | -1.8045 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.14 |  | 752.6448 | -0.1999 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.875 |  | 296.254 | -0.4655 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.905 |  | 126.6891 | -0.6189 | 131.36 | 126.665 | 3.32 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.195 |  | 73.3707 | -1.6024 | 75.54 | 73.985 | 0.1108 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 288.21 |  | 293.9706 | -1.9596 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 394.19 |  | 399.5335 | -1.3374 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.2 |  | 631.6868 | -0.8686 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1019.22 |  | 1028.0489 | -0.8588 | 1035.07 | 1021.09 | 4.8282 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.81 |  | 474.4056 | -0.1255 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.31 |  | 140.5297 | -0.1563 | 140.83 | 139.43 | 0.0713 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 167.05 |  | 166.4937 | 0.3341 | 169.91 | 165.6 | 3.3224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.4 |  | 281.2493 | -2.0798 | 288.48 | 280.67 | 2.0879 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 696.15 |  | 709.2756 | -1.8506 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 388.54 |  | 395.4586 | -1.7495 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.4 |  | 101.6021 | -3.1516 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 315.54 |  | 323.9022 | -2.5817 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.795 |  | 1819.7614 | -1.4269 | 1823.13 | 1796.26 | 0.0714 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 559.68 |  | 570.8009 | -1.9483 | 572.69 | 562.32 | 0.1001 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 316.12 |  | 323.3061 | -2.2227 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.66 |  | 221.0782 | -1.0938 | 222.19 | 218.09 | 0.096 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 319.56 |  | 326.9349 | -2.2558 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.48 |  | 287.8594 | -2.5635 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.54 |  | 64.0877 | -2.415 | 66.19 | 63.93 | 1.1193 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.39 |  | 51.982 | -3.0625 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.53 |  | 135.0187 | -1.1026 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.97 |  | 337.4025 | -2.2029 | 346.26 | 338 | 4.6156 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.51 |  | 515.0166 | 0.29 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.26 |  | 294.885 | 0.1272 | 293.89 | 291.35 | 4.2336 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 25.89 |  | 26.8588 | -3.6069 | 28.05 | 27.6 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.69 |  | 35.5471 | -2.4112 | 37.365 | 36.4 | 0.0288 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.795 |  | 21.2465 | -2.125 | 22.18 | 21.78 | 0.0481 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1410.29 |  | 1467.7213 | -3.913 | 1549.47 | 1482.06 | 3.1908 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.415 |  | 475.3785 | -4.4099 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 740.54 |  | 766.8612 | -3.4323 | 797.155 | 768.7 | 4.2672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.01 |  | 255.5429 | -0.2085 | 258.07 | 252.62 | 0.0157 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.92 |  | 672.2377 | -0.4935 | 680.09 | 667.1 | 0.3558 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.25 |  | 257.2918 | -0.7936 | 265.96 | 258.1 | 2.1117 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.08 |  | 162.0946 | -3.7106 | 168.11 | 162.41 | 0.519 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
