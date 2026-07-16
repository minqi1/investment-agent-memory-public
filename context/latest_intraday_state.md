# Intraday State

- Generated at: `2026-07-17T01:31:50+08:00`
- Market time ET: `2026-07-16T13:31:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 12, 'below_opening_15m_low': 33, 'spread_too_wide_or_missing': 6, 'manual_confirm_candidate': 1, 'watch_only': 3, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.69 |  | 709.8531 | -0.1638 | 713.55 | 708.25 | 0.0113 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 529.73 |  | 535.1347 | -1.01 | 543.4 | 535.47 | 0.0736 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.015 |  | 573.0896 | -0.8855 | 580.31 | 572.21 | 0.0581 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.7 |  | 752.721 | -0.0028 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.71 |  | 330.2479 | 0.7455 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.65 |  | 140.5453 | 0.0745 | 140.83 | 139.43 | 0.1706 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 371.865 |  | 371.8541 | 0.0029 | 375.18 | 369.2 | 0.2743 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 332.71 |  | 330.2479 | 0.7455 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 256.46 |  | 255.5462 | 0.3576 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 5 | LIN | industrial_gases | 516.055 |  | 514.9339 | 0.2177 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TT | data_center_power_cooling | 475.46 |  | 474.3185 | 0.2407 | 474.085 | 467.64 | 4.7491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 295.185 |  | 294.8687 | 0.1073 | 293.89 | 291.35 | 0.542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ORCL | cloud_ai_capex | 126.8 |  | 126.7417 | 0.046 | 131.36 | 126.665 | 2.5 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 167.61 |  | 166.4542 | 0.6944 | 169.91 | 165.6 | 1.2052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | QQQ | market_regime | 708.69 |  | 709.8531 | -0.1638 | 713.55 | 708.25 | 0.0113 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1801.47 |  | 1821.4171 | -1.0951 | 1823.13 | 1796.26 | 0.1016 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 752.7 |  | 752.721 | -0.0028 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 295.65 |  | 296.3638 | -0.2408 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 669.845 |  | 672.8052 | -0.44 | 680.09 | 667.1 | 0.0597 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | DELL | ai_server_oem | 401.305 |  | 403.213 | -0.4732 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | MSFT | cloud_ai_capex | 403.795 |  | 398.0719 | 1.4377 | 398.69 | 392.2 | 0.4532 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | GEV | data_center_power_cooling | 1022.33 |  | 1028.7683 | -0.6258 | 1035.07 | 1021.09 | 4.5181 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMAT | semiconductor_equipment | 563.71 |  | 572.193 | -1.4825 | 572.69 | 562.32 | 0.6191 | below_vwap | below_vwap,spread_too_wide |
| 20 | KLAC | semiconductor_equipment | 219.205 |  | 221.3664 | -0.9764 | 222.19 | 218.09 | 4.9771 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.71 |  | 330.2479 | 0.7455 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 2 | TT | data_center_power_cooling | 475.46 |  | 474.3185 | 0.2407 | 474.085 | 467.64 | 4.7491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | LIN | industrial_gases | 516.055 |  | 514.9339 | 0.2177 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.185 |  | 294.8687 | 0.1073 | 293.89 | 291.35 | 0.542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | MSFT | cloud_ai_capex | 403.795 |  | 398.0719 | 1.4377 | 398.69 | 392.2 | 0.4532 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | JCI | data_center_power_cooling | 140.65 |  | 140.5453 | 0.0745 | 140.83 | 139.43 | 0.1706 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 371.865 |  | 371.8541 | 0.0029 | 375.18 | 369.2 | 0.2743 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 256.46 |  | 255.5462 | 0.3576 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 9 | QQQ | market_regime | 708.69 |  | 709.8531 | -0.1638 | 713.55 | 708.25 | 0.0113 | below_vwap | below_vwap |
| 10 | GEV | data_center_power_cooling | 1022.33 |  | 1028.7683 | -0.6258 | 1035.07 | 1021.09 | 4.5181 | below_vwap | below_vwap,spread_too_wide |
| 11 | ASML | semiconductor_equipment | 1801.47 |  | 1821.4171 | -1.0951 | 1823.13 | 1796.26 | 0.1016 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 563.71 |  | 572.193 | -1.4825 | 572.69 | 562.32 | 0.6191 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 219.205 |  | 221.3664 | -0.9764 | 222.19 | 218.09 | 4.9771 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 752.7 |  | 752.721 | -0.0028 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.65 |  | 296.3638 | -0.2408 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | DELL | ai_server_oem | 401.305 |  | 403.213 | -0.4732 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 | 1.5546 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 669.845 |  | 672.8052 | -0.44 | 680.09 | 667.1 | 0.0597 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 167.61 |  | 166.4542 | 0.6944 | 169.91 | 165.6 | 1.2052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.69 |  | 709.8531 | -0.1638 | 713.55 | 708.25 | 0.0113 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.63 |  | 71.9949 | -0.5069 | 73.09 | 71.45 | 0.014 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.245 |  | 207.4834 | -0.1149 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.795 |  | 398.0719 | 1.4377 | 398.69 | 392.2 | 0.4532 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 332.71 |  | 330.2479 | 0.7455 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.865 |  | 371.8541 | 0.0029 | 375.18 | 369.2 | 0.2743 | watch_only | none |
| AMD | ai_accelerator | 497.895 |  | 506.4465 | -1.6885 | 518.33 | 507.62 | 0.5162 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.115 |  | 409.9665 | -0.9395 | 414.385 | 406.61 | 0.6304 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.73 |  | 535.1347 | -1.01 | 543.4 | 535.47 | 0.0736 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.015 |  | 573.0896 | -0.8855 | 580.31 | 572.21 | 0.0581 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 378 |  | 380.8374 | -0.7451 | 386.58 | 378.53 | 1.0582 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 852.37 |  | 859.1966 | -0.7945 | 887.1 | 866.765 | 1.5123 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.22 |  | 192.0035 | -1.9706 | 201.61 | 194.19 | 0.5207 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.305 |  | 403.213 | -0.4732 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.49 |  | 45.9791 | -1.0637 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.11 |  | 25.4467 | -1.3233 | 26.71 | 25.74 | 0.0398 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.7 |  | 752.721 | -0.0028 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |
| IWM | market_regime | 295.65 |  | 296.3638 | -0.2408 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.8 |  | 126.7417 | 0.046 | 131.36 | 126.665 | 2.5 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.045 |  | 73.4907 | -0.6064 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 291.24 |  | 294.5303 | -1.1171 | 300.385 | 293.64 | 2.1391 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.84 |  | 399.7035 | -1.2168 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.15 |  | 631.9702 | -0.4463 | 640.25 | 631.005 | 4.8526 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1022.33 |  | 1028.7683 | -0.6258 | 1035.07 | 1021.09 | 4.5181 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.46 |  | 474.3185 | 0.2407 | 474.085 | 467.64 | 4.7491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.65 |  | 140.5453 | 0.0745 | 140.83 | 139.43 | 0.1706 | watch_only | none |
| ANET | ai_networking_optical | 167.61 |  | 166.4542 | 0.6944 | 169.91 | 165.6 | 1.2052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.36 |  | 281.7802 | -1.5687 | 288.48 | 280.67 | 1.6116 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 699.3 |  | 710.4129 | -1.5643 | 737.175 | 720.21 | 0.4419 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 391.22 |  | 396.0708 | -1.2247 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.44 |  | 101.9465 | -2.4587 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.17 |  | 324.0791 | -2.4405 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1801.47 |  | 1821.4171 | -1.0951 | 1823.13 | 1796.26 | 0.1016 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 563.71 |  | 572.193 | -1.4825 | 572.69 | 562.32 | 0.6191 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.28 |  | 324.7326 | -1.6791 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.205 |  | 221.3664 | -0.9764 | 222.19 | 218.09 | 4.9771 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 323.1 |  | 327.3493 | -1.2981 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 282.24 |  | 288.7258 | -2.2464 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.81 |  | 64.2411 | -2.2277 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.16 |  | 52.2255 | -2.0401 | 52.72 | 51.735 | 0.3714 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 | 1.5546 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 332.32 |  | 338.2375 | -1.7495 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 516.055 |  | 514.9339 | 0.2177 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.185 |  | 294.8687 | 0.1073 | 293.89 | 291.35 | 0.542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.25 |  | 26.9828 | -2.7158 | 28.05 | 27.6 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.795 |  | 35.6465 | -2.3888 | 37.365 | 36.4 | 0.0287 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.87 |  | 21.2865 | -1.9568 | 22.18 | 21.78 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1441.025 |  | 1472.575 | -2.1425 | 1549.47 | 1482.06 | 0.5822 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.49 |  | 476.525 | -3.5748 | 498.04 | 480.14 | 2.4114 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 750.52 |  | 768.0973 | -2.2884 | 797.155 | 768.7 | 0.3171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 256.46 |  | 255.5462 | 0.3576 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| META | cloud_ai_capex | 669.845 |  | 672.8052 | -0.44 | 680.09 | 667.1 | 0.0597 | below_vwap | below_vwap |
| ARM | ai_accelerator | 256.19 |  | 257.3965 | -0.4687 | 265.96 | 258.1 | 2.4708 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.93 |  | 162.5812 | -3.4759 | 168.11 | 162.41 | 1.4656 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
