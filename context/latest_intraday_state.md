# Intraday State

- Generated at: `2026-07-17T01:51:47+08:00`
- Market time ET: `2026-07-16T13:51:48-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 3, 'below_vwap': 7, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.01 |  | 709.7288 | -0.3831 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.49 |  | 534.6496 | -1.5262 | 543.4 | 535.47 | 0.0722 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.63 |  | 572.6109 | -1.2191 | 580.31 | 572.21 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.67 |  | 752.6721 | -0.1331 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 295.05 |  | 294.88 | 0.0576 | 293.89 | 291.35 | 0.2372 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.745 |  | 398.4316 | 1.0826 | 398.69 | 392.2 | 0.0869 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332.095 |  | 330.5129 | 0.4787 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 295.05 |  | 294.88 | 0.0576 | 293.89 | 291.35 | 0.2372 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 256.02 |  | 255.5467 | 0.1852 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 332.095 |  | 330.5129 | 0.4787 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 167.2 |  | 166.4832 | 0.4305 | 169.91 | 165.6 | 0.0419 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 402.745 |  | 398.4316 | 1.0826 | 398.69 | 392.2 | 0.0869 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.61 |  | 140.5484 | 0.0438 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TT | data_center_power_cooling | 475.04 |  | 474.4209 | 0.1305 | 474.085 | 467.64 | 4.8859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | LIN | industrial_gases | 516.82 |  | 514.9861 | 0.3561 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SPY | market_regime | 751.67 |  | 752.6721 | -0.1331 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.33 |  | 296.3098 | -0.3307 | 296.28 | 294.65 | 0.0169 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.72 |  | 371.8435 | -0.0332 | 375.18 | 369.2 | 0.0915 | below_vwap | below_vwap |
| 12 | META | cloud_ai_capex | 668.41 |  | 672.4026 | -0.5938 | 680.09 | 667.1 | 0.1137 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 133.78 |  | 135.0366 | -0.9305 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 218.64 |  | 221.1764 | -1.1468 | 222.19 | 218.09 | 0.4071 | below_vwap | below_vwap,spread_too_wide |
| 16 | SOXX | semiconductor_index | 526.49 |  | 534.6496 | -1.5262 | 543.4 | 535.47 | 0.0722 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 707.01 |  | 709.7288 | -0.3831 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 206.55 |  | 207.4244 | -0.4215 | 211.03 | 207.49 | 0.029 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1793.58 |  | 1820.5216 | -1.4799 | 1823.13 | 1796.26 | 0.0942 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AMAT | semiconductor_equipment | 561.545 |  | 571.6982 | -1.776 | 572.69 | 562.32 | 0.0766 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 295.05 |  | 294.88 | 0.0576 | 293.89 | 291.35 | 0.2372 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.745 |  | 398.4316 | 1.0826 | 398.69 | 392.2 | 0.0869 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332.095 |  | 330.5129 | 0.4787 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.04 |  | 474.4209 | 0.1305 | 474.085 | 467.64 | 4.8859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | LIN | industrial_gases | 516.82 |  | 514.9861 | 0.3561 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 167.2 |  | 166.4832 | 0.4305 | 169.91 | 165.6 | 0.0419 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 256.02 |  | 255.5467 | 0.1852 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 218.64 |  | 221.1764 | -1.1468 | 222.19 | 218.09 | 0.4071 | below_vwap | below_vwap,spread_too_wide |
| 9 | SPY | market_regime | 751.67 |  | 752.6721 | -0.1331 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.33 |  | 296.3098 | -0.3307 | 296.28 | 294.65 | 0.0169 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ENTG | semiconductor_materials | 133.78 |  | 135.0366 | -0.9305 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GOOGL | cloud_ai_capex | 371.72 |  | 371.8435 | -0.0332 | 375.18 | 369.2 | 0.0915 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 668.41 |  | 672.4026 | -0.5938 | 680.09 | 667.1 | 0.1137 | below_vwap | below_vwap |
| 15 | JCI | data_center_power_cooling | 140.61 |  | 140.5484 | 0.0438 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SOXX | semiconductor_index | 526.49 |  | 534.6496 | -1.5262 | 543.4 | 535.47 | 0.0722 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | TSM | foundry | 404.945 |  | 409.4223 | -1.0936 | 414.385 | 406.61 | 0.2766 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | CIEN | ai_networking_optical | 388.85 |  | 395.6734 | -1.7245 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 19 | QQQ | market_regime | 707.01 |  | 709.7288 | -0.3831 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AVGO | custom_silicon_networking | 376.3 |  | 380.565 | -1.1207 | 386.58 | 378.53 | 1.5945 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.01 |  | 709.7288 | -0.3831 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.05 |  | 71.9411 | -1.2386 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.55 |  | 207.4244 | -0.4215 | 211.03 | 207.49 | 0.029 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.745 |  | 398.4316 | 1.0826 | 398.69 | 392.2 | 0.0869 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.095 |  | 330.5129 | 0.4787 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.72 |  | 371.8435 | -0.0332 | 375.18 | 369.2 | 0.0915 | below_vwap | below_vwap |
| AMD | ai_accelerator | 493.155 |  | 505.6136 | -2.4641 | 518.33 | 507.62 | 0.2251 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 404.945 |  | 409.4223 | -1.0936 | 414.385 | 406.61 | 0.2766 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.49 |  | 534.6496 | -1.5262 | 543.4 | 535.47 | 0.0722 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.63 |  | 572.6109 | -1.2191 | 580.31 | 572.21 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.3 |  | 380.565 | -1.1207 | 386.58 | 378.53 | 1.5945 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 843.475 |  | 858.4122 | -1.7401 | 887.1 | 866.765 | 0.2513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 186.84 |  | 191.5689 | -2.4685 | 201.61 | 194.19 | 0.1285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 396.87 |  | 402.9518 | -1.5093 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.815 |  | 45.9195 | -2.4054 | 47.65 | 46.165 | 0.0446 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.895 |  | 25.4127 | -2.0371 | 26.71 | 25.74 | 0.0402 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.67 |  | 752.6721 | -0.1331 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 295.33 |  | 296.3098 | -0.3307 | 296.28 | 294.65 | 0.0169 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.88 |  | 126.7119 | -0.6565 | 131.36 | 126.665 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.19 |  | 73.4235 | -1.68 | 75.54 | 73.985 | 1.1497 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.19 |  | 294.1769 | -1.6952 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.135 |  | 399.6 | -1.1174 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.54 |  | 631.7394 | -0.6647 | 640.25 | 631.005 | 4.6881 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1020.84 |  | 1028.3719 | -0.7324 | 1035.07 | 1021.09 | 4.6609 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.04 |  | 474.4209 | 0.1305 | 474.085 | 467.64 | 4.8859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.61 |  | 140.5484 | 0.0438 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.2 |  | 166.4832 | 0.4305 | 169.91 | 165.6 | 0.0419 | watch_only | none |
| COHR | ai_networking_optical | 275.83 |  | 281.3876 | -1.9751 | 288.48 | 280.67 | 0.5112 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.325 |  | 709.7737 | -1.7539 | 737.175 | 720.21 | 2.3648 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.85 |  | 395.6734 | -1.7245 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.49 |  | 101.6537 | -3.1122 | 106.975 | 102.85 | 4.8837 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 315 |  | 324.002 | -2.7784 | 337.59 | 326.16 | 4.3079 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1793.58 |  | 1820.5216 | -1.4799 | 1823.13 | 1796.26 | 0.0942 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.545 |  | 571.6982 | -1.776 | 572.69 | 562.32 | 0.0766 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 317.225 |  | 324.3544 | -2.198 | 328.96 | 324.11 | 3.042 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 218.64 |  | 221.1764 | -1.1468 | 222.19 | 218.09 | 0.4071 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 320.77 |  | 327.0509 | -1.9205 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.775 |  | 288.2458 | -2.5918 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.46 |  | 64.1674 | -2.6608 | 66.19 | 63.93 | 1.9212 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.525 |  | 52.1223 | -3.0644 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.78 |  | 135.0366 | -0.9305 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.355 |  | 337.7329 | -2.1845 | 346.26 | 338 | 4.4709 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.82 |  | 514.9861 | 0.3561 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.05 |  | 294.88 | 0.0576 | 293.89 | 291.35 | 0.2372 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 25.955 |  | 26.9188 | -3.5804 | 28.05 | 27.6 | 0.0771 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.535 |  | 35.5832 | -2.9458 | 37.365 | 36.4 | 0.029 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.835 |  | 21.257 | -1.9851 | 22.18 | 21.78 | 0.096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1418.9 |  | 1469.8 | -3.4631 | 1549.47 | 1482.06 | 1.2101 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.05 |  | 475.8711 | -4.1652 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 745.84 |  | 767.342 | -2.8021 | 797.155 | 768.7 | 0.2226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 256.02 |  | 255.5467 | 0.1852 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| META | cloud_ai_capex | 668.41 |  | 672.4026 | -0.5938 | 680.09 | 667.1 | 0.1137 | below_vwap | below_vwap |
| ARM | ai_accelerator | 255.355 |  | 257.329 | -0.7671 | 265.96 | 258.1 | 2.1108 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.54 |  | 162.2848 | -4.1562 | 168.11 | 162.41 | 2.4045 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
