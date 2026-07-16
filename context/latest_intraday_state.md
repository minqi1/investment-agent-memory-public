# Intraday State

- Generated at: `2026-07-16T22:03:25+08:00`
- Market time ET: `2026-07-16T10:03:26-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 7, 'below_vwap': 19, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 20, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.23 |  | 709.5526 | 0.0955 | 713.55 | 708.25 | 0.0929 | watch_only | none |
| SOXX | semiconductor_index | 538.68 |  | 537.2883 | 0.259 | 543.4 | 535.47 | 0.1114 | watch_only | none |
| SMH | semiconductor_index | 575.57 |  | 574.8973 | 0.117 | 580.31 | 572.21 | 0.1129 | watch_only | none |
| SPY | market_regime | 752.545 |  | 751.8807 | 0.0883 | 753.51 | 751.13 | 0.0545 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 223.175 |  | 220.4783 | 1.2231 | 222.19 | 218.09 | 0.1031 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.845 |  | 296.0836 | 0.2572 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.005 |  | 328.8163 | 0.3615 | 328.98 | 326.885 | 0.1061 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.845 |  | 296.0836 | 0.2572 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 538.68 |  | 537.2883 | 0.259 | 543.4 | 535.47 | 0.1114 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 330.005 |  | 328.8163 | 0.3615 | 328.98 | 326.885 | 0.1061 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 710.23 |  | 709.5526 | 0.0955 | 713.55 | 708.25 | 0.0929 | watch_only | none |
| 5 | SMH | semiconductor_index | 575.57 |  | 574.8973 | 0.117 | 580.31 | 572.21 | 0.1129 | watch_only | none |
| 6 | SPY | market_regime | 752.545 |  | 751.8807 | 0.0883 | 753.51 | 751.13 | 0.0545 | watch_only | none |
| 7 | TT | data_center_power_cooling | 472.55 |  | 471.2135 | 0.2836 | 474.085 | 467.64 | 0.3471 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 223.175 |  | 220.4783 | 1.2231 | 222.19 | 218.09 | 0.1031 | buy_precheck_manual_confirm | none |
| 9 | COHR | ai_networking_optical | 285.77 |  | 284.3159 | 0.5114 | 288.48 | 280.67 | 0.2904 | watch_only | none |
| 10 | VRT | data_center_power_cooling | 295.33 |  | 294.6534 | 0.2296 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 632.94 |  | 632.3456 | 0.094 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 402.41 |  | 401.8129 | 0.1486 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AAOI | ai_networking_optical | 104 |  | 103.7953 | 0.1972 | 106.975 | 102.85 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 135.32 |  | 134.4958 | 0.6128 | 135.32 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 140.71 |  | 140.0084 | 0.5011 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ASML | semiconductor_equipment | 1813.9 |  | 1808.3071 | 0.3093 | 1823.13 | 1796.26 | 0.6384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 725.12 |  | 721.4096 | 0.5143 | 737.175 | 720.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | DELL | ai_server_oem | 405.4 |  | 402.8442 | 0.6344 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ALAB | ai_networking_optical | 329.92 |  | 329.2192 | 0.2129 | 337.59 | 326.16 | 4.883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 483.74 |  | 482.6313 | 0.2297 | 498.04 | 480.14 | 0.4114 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 223.175 |  | 220.4783 | 1.2231 | 222.19 | 218.09 | 0.1031 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.845 |  | 296.0836 | 0.2572 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.005 |  | 328.8163 | 0.3615 | 328.98 | 326.885 | 0.1061 | buy_precheck_manual_confirm | none |
| 4 | AMAT | semiconductor_equipment | 578.95 |  | 569.1323 | 1.725 | 572.69 | 562.32 | 0.8671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ENTG | semiconductor_materials | 135.32 |  | 134.4958 | 0.6128 | 135.32 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | COHU | semiconductor_test_packaging | 52.695 |  | 52.1079 | 1.1267 | 52.695 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SOXX | semiconductor_index | 538.68 |  | 537.2883 | 0.259 | 543.4 | 535.47 | 0.1114 | watch_only | none |
| 8 | QQQ | market_regime | 710.23 |  | 709.5526 | 0.0955 | 713.55 | 708.25 | 0.0929 | watch_only | none |
| 9 | TT | data_center_power_cooling | 472.55 |  | 471.2135 | 0.2836 | 474.085 | 467.64 | 0.3471 | watch_only | none |
| 10 | SMH | semiconductor_index | 575.57 |  | 574.8973 | 0.117 | 580.31 | 572.21 | 0.1129 | watch_only | none |
| 11 | SPY | market_regime | 752.545 |  | 751.8807 | 0.0883 | 753.51 | 751.13 | 0.0545 | watch_only | none |
| 12 | COHR | ai_networking_optical | 285.77 |  | 284.3159 | 0.5114 | 288.48 | 280.67 | 0.2904 | watch_only | none |
| 13 | TQQQ | leveraged_tool | 72.04 |  | 71.9999 | 0.0558 | 73.09 | 71.45 | 0.0278 | watch_only | none |
| 14 | ANET | ai_networking_optical | 166.13 |  | 166.4239 | -0.1766 | 169.91 | 165.6 | 3.8163 | below_vwap | below_vwap,spread_too_wide |
| 15 | TSM | foundry | 409.67 |  | 410.0486 | -0.0923 | 414.385 | 406.61 | 0.105 | below_vwap | below_vwap |
| 16 | CIEN | ai_networking_optical | 401.3 |  | 401.41 | -0.0274 | 410 | 397.68 | 0.4809 | below_vwap | below_vwap,spread_too_wide |
| 17 | NVDA | ai_accelerator | 207.8 |  | 208.4819 | -0.3271 | 211.03 | 207.49 | 0.0241 | below_vwap | below_vwap |
| 18 | AMD | ai_accelerator | 511.05 |  | 511.7427 | -0.1354 | 518.33 | 507.62 | 0.4892 | below_vwap | below_vwap,spread_too_wide |
| 19 | STX | memory_hbm_storage | 772.515 |  | 774.6422 | -0.2746 | 797.155 | 768.7 | 4.9915 | below_vwap | below_vwap,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.23 |  | 709.5526 | 0.0955 | 713.55 | 708.25 | 0.0929 | watch_only | none |
| TQQQ | leveraged_tool | 72.04 |  | 71.9999 | 0.0558 | 73.09 | 71.45 | 0.0278 | watch_only | none |
| NVDA | ai_accelerator | 207.8 |  | 208.4819 | -0.3271 | 211.03 | 207.49 | 0.0241 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 393.99 |  | 395.4023 | -0.3572 | 398.69 | 392.2 | 0.3122 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 330.005 |  | 328.8163 | 0.3615 | 328.98 | 326.885 | 0.1061 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.665 |  | 371.657 | -0.2669 | 375.18 | 369.2 | 0.8876 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 511.05 |  | 511.7427 | -0.1354 | 518.33 | 507.62 | 0.4892 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 409.67 |  | 410.0486 | -0.0923 | 414.385 | 406.61 | 0.105 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 538.68 |  | 537.2883 | 0.259 | 543.4 | 535.47 | 0.1114 | watch_only | none |
| SMH | semiconductor_index | 575.57 |  | 574.8973 | 0.117 | 580.31 | 572.21 | 0.1129 | watch_only | none |
| AVGO | custom_silicon_networking | 382.4 |  | 380.7435 | 0.4351 | 386.58 | 378.53 | 4.2939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 871.835 |  | 865.3706 | 0.747 | 887.1 | 866.765 | 1.3798 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 194.84 |  | 195.3618 | -0.2671 | 201.61 | 194.19 | 3.2488 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 405.4 |  | 402.8442 | 0.6344 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.71 |  | 46.8609 | -0.322 | 47.65 | 46.165 | 0.0856 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.935 |  | 25.9654 | -0.117 | 26.71 | 25.74 | 0.0771 | below_vwap | below_vwap |
| SPY | market_regime | 752.545 |  | 751.8807 | 0.0883 | 753.51 | 751.13 | 0.0545 | watch_only | none |
| IWM | market_regime | 296.845 |  | 296.0836 | 0.2572 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.485 |  | 127.6447 | -0.1251 | 131.36 | 126.665 | 1.5688 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.77 |  | 74.1865 | -0.5614 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 295.33 |  | 294.6534 | 0.2296 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.41 |  | 401.8129 | 0.1486 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 632.94 |  | 632.3456 | 0.094 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1034.01 |  | 1025.524 | 0.8275 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 472.55 |  | 471.2135 | 0.2836 | 474.085 | 467.64 | 0.3471 | watch_only | none |
| JCI | data_center_power_cooling | 140.71 |  | 140.0084 | 0.5011 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.13 |  | 166.4239 | -0.1766 | 169.91 | 165.6 | 3.8163 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 285.77 |  | 284.3159 | 0.5114 | 288.48 | 280.67 | 0.2904 | watch_only | none |
| LITE | ai_networking_optical | 725.12 |  | 721.4096 | 0.5143 | 737.175 | 720.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 401.3 |  | 401.41 | -0.0274 | 410 | 397.68 | 0.4809 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 104 |  | 103.7953 | 0.1972 | 106.975 | 102.85 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 329.92 |  | 329.2192 | 0.2129 | 337.59 | 326.16 | 4.883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1813.9 |  | 1808.3071 | 0.3093 | 1823.13 | 1796.26 | 0.6384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 578.95 |  | 569.1323 | 1.725 | 572.69 | 562.32 | 0.8671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 328.3 |  | 325.5826 | 0.8346 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 223.175 |  | 220.4783 | 1.2231 | 222.19 | 218.09 | 0.1031 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 328.77 |  | 326.7268 | 0.6254 | 332.49 | 326.685 | 0.7604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 291.24 |  | 288.7141 | 0.8749 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.41 |  | 64.7849 | -0.5787 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.695 |  | 52.1079 | 1.1267 | 52.695 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.32 |  | 134.4958 | 0.6128 | 135.32 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 339.28 |  | 340.1256 | -0.2486 | 342.45 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 511.26 |  | 513.7359 | -0.4819 | 515.825 | 512.23 | 4.8371 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 290.59 |  | 292.0458 | -0.4985 | 293.89 | 291.35 | 0.2753 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 27.345 |  | 27.5258 | -0.6569 | 28.05 | 27.6 | 0.1097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 36.05 |  | 36.542 | -1.3464 | 37.365 | 36.4 | 0.0832 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.55 |  | 21.7763 | -1.0391 | 22.18 | 21.78 | 0.1856 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1518.12 |  | 1499.2358 | 1.2596 | 1549.47 | 1482.06 | 0.9933 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 483.74 |  | 482.6313 | 0.2297 | 498.04 | 480.14 | 0.4114 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 772.515 |  | 774.6422 | -0.2746 | 797.155 | 768.7 | 4.9915 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 254.61 |  | 254.8553 | -0.0962 | 258.07 | 252.62 | 0.0236 | below_vwap | below_vwap |
| META | cloud_ai_capex | 670.75 |  | 672.4843 | -0.2579 | 680.09 | 667.1 | 0.2415 | below_vwap | below_vwap |
| ARM | ai_accelerator | 259.76 |  | 259.9859 | -0.0869 | 265.96 | 258.1 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 164.31 |  | 164.8962 | -0.3555 | 168.11 | 162.41 | 0.1522 | below_vwap | below_vwap |
