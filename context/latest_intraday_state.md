# Intraday State

- Generated at: `2026-07-17T01:55:46+08:00`
- Market time ET: `2026-07-16T13:55:47-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 3, 'below_vwap': 7, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.86 |  | 709.7166 | -0.4025 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.26 |  | 534.5847 | -1.5572 | 543.4 | 535.47 | 0.0589 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.28 |  | 572.5245 | -1.2654 | 580.31 | 572.21 | 0.0159 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.58 |  | 752.6682 | -0.1446 | 753.51 | 751.13 | 0.0173 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.835 |  | 514.989 | 0.3585 | 515.825 | 512.23 | 0.0716 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.595 |  | 398.4657 | 1.0363 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.8 |  | 330.5394 | 0.3814 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.835 |  | 514.989 | 0.3585 | 515.825 | 512.23 | 0.0716 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 167.04 |  | 166.4857 | 0.333 | 169.91 | 165.6 | 0.0718 | watch_only | none |
| 3 | AMZN | cloud_ai_capex | 256.145 |  | 255.5545 | 0.2311 | 258.07 | 252.62 | 0.0547 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 331.8 |  | 330.5394 | 0.3814 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 402.595 |  | 398.4657 | 1.0363 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 474.77 |  | 474.4235 | 0.073 | 474.085 | 467.64 | 4.9013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 295.08 |  | 294.8808 | 0.0676 | 293.89 | 291.35 | 4.4225 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SPY | market_regime | 751.58 |  | 752.6682 | -0.1446 | 753.51 | 751.13 | 0.0173 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.205 |  | 296.3017 | -0.3701 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | GOOGL | cloud_ai_capex | 371.695 |  | 371.8425 | -0.0397 | 375.18 | 369.2 | 0.0538 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 218.75 |  | 221.1188 | -1.0713 | 222.19 | 218.09 | 0.3246 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 140.42 |  | 140.5469 | -0.0903 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | META | cloud_ai_capex | 669.905 |  | 672.3617 | -0.3654 | 680.09 | 667.1 | 2.0033 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 526.26 |  | 534.5847 | -1.5572 | 543.4 | 535.47 | 0.0589 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.35 |  | 409.3803 | -1.2288 | 414.385 | 406.61 | 0.0692 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 706.86 |  | 709.7166 | -0.4025 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AVGO | custom_silicon_networking | 376.655 |  | 380.5183 | -1.0153 | 386.58 | 378.53 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1795.58 |  | 1820.1785 | -1.3514 | 1823.13 | 1796.26 | 0.0886 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 565.28 |  | 572.5245 | -1.2654 | 580.31 | 572.21 | 0.0159 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.835 |  | 514.989 | 0.3585 | 515.825 | 512.23 | 0.0716 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.595 |  | 398.4657 | 1.0363 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.8 |  | 330.5394 | 0.3814 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 474.77 |  | 474.4235 | 0.073 | 474.085 | 467.64 | 4.9013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 295.08 |  | 294.8808 | 0.0676 | 293.89 | 291.35 | 4.4225 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.04 |  | 166.4857 | 0.333 | 169.91 | 165.6 | 0.0718 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 256.145 |  | 255.5545 | 0.2311 | 258.07 | 252.62 | 0.0547 | watch_only | none |
| 8 | JCI | data_center_power_cooling | 140.42 |  | 140.5469 | -0.0903 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 218.75 |  | 221.1188 | -1.0713 | 222.19 | 218.09 | 0.3246 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 751.58 |  | 752.6682 | -0.1446 | 753.51 | 751.13 | 0.0173 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.205 |  | 296.3017 | -0.3701 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GOOGL | cloud_ai_capex | 371.695 |  | 371.8425 | -0.0397 | 375.18 | 369.2 | 0.0538 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 669.905 |  | 672.3617 | -0.3654 | 680.09 | 667.1 | 2.0033 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 526.26 |  | 534.5847 | -1.5572 | 543.4 | 535.47 | 0.0589 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.35 |  | 409.3803 | -1.2288 | 414.385 | 406.61 | 0.0692 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 387.885 |  | 395.5979 | -1.9497 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 706.86 |  | 709.7166 | -0.4025 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 376.655 |  | 380.5183 | -1.0153 | 386.58 | 378.53 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | MU | memory_hbm_storage | 842.79 |  | 858.2848 | -1.8053 | 887.1 | 866.765 | 0.267 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.86 |  | 709.7166 | -0.4025 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.01 |  | 71.9325 | -1.2825 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.64 |  | 207.4195 | -0.3758 | 211.03 | 207.49 | 0.3581 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 402.595 |  | 398.4657 | 1.0363 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.8 |  | 330.5394 | 0.3814 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.695 |  | 371.8425 | -0.0397 | 375.18 | 369.2 | 0.0538 | below_vwap | below_vwap |
| AMD | ai_accelerator | 493.19 |  | 505.4528 | -2.4261 | 518.33 | 507.62 | 0.3183 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 404.35 |  | 409.3803 | -1.2288 | 414.385 | 406.61 | 0.0692 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.26 |  | 534.5847 | -1.5572 | 543.4 | 535.47 | 0.0589 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.28 |  | 572.5245 | -1.2654 | 580.31 | 572.21 | 0.0159 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.655 |  | 380.5183 | -1.0153 | 386.58 | 378.53 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 842.79 |  | 858.2848 | -1.8053 | 887.1 | 866.765 | 0.267 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 186.74 |  | 191.4954 | -2.4833 | 201.61 | 194.19 | 0.166 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 395.77 |  | 402.8642 | -1.7609 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.83 |  | 45.9127 | -2.3582 | 47.65 | 46.165 | 0.0446 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.87 |  | 25.4006 | -2.0888 | 26.71 | 25.74 | 0.0402 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.58 |  | 752.6682 | -0.1446 | 753.51 | 751.13 | 0.0173 | below_vwap | below_vwap |
| IWM | market_regime | 295.205 |  | 296.3017 | -0.3701 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.04 |  | 126.7052 | -0.525 | 131.36 | 126.665 | 0.7379 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.25 |  | 73.4082 | -1.5778 | 75.54 | 73.985 | 1.1626 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.55 |  | 294.1345 | -1.8986 | 300.385 | 293.64 | 1.2892 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.835 |  | 399.5828 | -1.1882 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.6 |  | 631.726 | -0.8114 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1020.145 |  | 1028.2985 | -0.7929 | 1035.07 | 1021.09 | 2.7937 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.77 |  | 474.4235 | 0.073 | 474.085 | 467.64 | 4.9013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.42 |  | 140.5469 | -0.0903 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.04 |  | 166.4857 | 0.333 | 169.91 | 165.6 | 0.0718 | watch_only | none |
| COHR | ai_networking_optical | 275.44 |  | 281.3266 | -2.0925 | 288.48 | 280.67 | 2.4978 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 695.14 |  | 709.6053 | -2.0385 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 387.885 |  | 395.5979 | -1.9497 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.2 |  | 101.6391 | -3.3836 | 106.975 | 102.85 | 4.2872 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 315.41 |  | 323.9107 | -2.6244 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1795.58 |  | 1820.1785 | -1.3514 | 1823.13 | 1796.26 | 0.0886 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.095 |  | 571.2582 | -1.9542 | 572.69 | 562.32 | 1.4069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 315.6 |  | 324.0629 | -2.6115 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.75 |  | 221.1188 | -1.0713 | 222.19 | 218.09 | 0.3246 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 320.03 |  | 327.0273 | -2.1397 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280 |  | 288.1121 | -2.8156 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.32 |  | 64.1441 | -2.8438 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.525 |  | 52.1223 | -3.0644 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.59 |  | 135.0225 | -1.0609 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.395 |  | 337.559 | -2.1223 | 346.26 | 338 | 4.5763 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.835 |  | 514.989 | 0.3585 | 515.825 | 512.23 | 0.0716 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 295.08 |  | 294.8808 | 0.0676 | 293.89 | 291.35 | 4.4225 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 25.92 |  | 26.9003 | -3.6442 | 28.05 | 27.6 | 0.0772 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.66 |  | 35.5673 | -2.5509 | 37.365 | 36.4 | 0.0289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.825 |  | 21.2562 | -2.0287 | 22.18 | 21.78 | 0.048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1412.285 |  | 1469.0239 | -3.8624 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 455.25 |  | 475.7157 | -4.3021 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 743.71 |  | 767.1722 | -3.0583 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 256.145 |  | 255.5545 | 0.2311 | 258.07 | 252.62 | 0.0547 | watch_only | none |
| META | cloud_ai_capex | 669.905 |  | 672.3617 | -0.3654 | 680.09 | 667.1 | 2.0033 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.78 |  | 257.3244 | -0.6002 | 265.96 | 258.1 | 2.1933 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.57 |  | 162.2237 | -4.1016 | 168.11 | 162.41 | 2.4041 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
