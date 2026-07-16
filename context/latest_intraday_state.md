# Intraday State

- Generated at: `2026-07-17T01:07:58+08:00`
- Market time ET: `2026-07-16T13:07:59-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 37, 'spread_too_wide_or_missing': 5, 'manual_confirm_candidate': 2, 'below_vwap': 10, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.81 |  | 709.9489 | -0.3013 | 713.55 | 708.25 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.27 |  | 536.0583 | -1.2663 | 543.4 | 535.47 | 0.0453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.81 |  | 573.6457 | -0.843 | 580.31 | 572.21 | 0.0721 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.26 |  | 752.7417 | -0.064 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.13 |  | 514.9079 | 0.2373 | 515.825 | 512.23 | 0.0988 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.04 |  | 330.0589 | 0.6002 | 328.98 | 326.885 | 0.0663 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.13 |  | 514.9079 | 0.2373 | 515.825 | 512.23 | 0.0988 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.04 |  | 330.0589 | 0.6002 | 328.98 | 326.885 | 0.0663 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.66 |  | 255.4557 | 0.08 | 258.07 | 252.62 | 0.176 | watch_only | none |
| 4 | JCI | data_center_power_cooling | 140.81 |  | 140.529 | 0.2 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 166.87 |  | 166.4091 | 0.277 | 169.91 | 165.6 | 4.6323 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | TT | data_center_power_cooling | 475.73 |  | 474.0336 | 0.3579 | 474.085 | 467.64 | 4.7001 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 296.42 |  | 294.8231 | 0.5416 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ASML | semiconductor_equipment | 1807.16 |  | 1822.3089 | -0.8313 | 1823.13 | 1796.26 | 0.0885 | below_vwap | below_vwap |
| 9 | KLAC | semiconductor_equipment | 219.56 |  | 221.6076 | -0.924 | 222.19 | 218.09 | 0.0729 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 752.26 |  | 752.7417 | -0.064 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.93 |  | 296.4031 | -0.1596 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | META | cloud_ai_capex | 668.83 |  | 673.2677 | -0.6591 | 680.09 | 667.1 | 0.2392 | below_vwap | below_vwap |
| 14 | MSFT | cloud_ai_capex | 402.1 |  | 397.7142 | 1.1027 | 398.69 | 392.2 | 0.4029 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | ENTG | semiconductor_materials | 134.67 |  | 135.1529 | -0.3573 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | GEV | data_center_power_cooling | 1025.02 |  | 1029.2673 | -0.4127 | 1035.07 | 1021.09 | 4.1658 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMAT | semiconductor_equipment | 566.81 |  | 572.8047 | -1.0466 | 572.69 | 562.32 | 2.7152 | below_vwap | below_vwap,spread_too_wide |
| 18 | GOOGL | cloud_ai_capex | 371.3 |  | 371.8765 | -0.155 | 375.18 | 369.2 | 0.4175 | below_vwap | below_vwap,spread_too_wide |
| 19 | SOXX | semiconductor_index | 529.27 |  | 536.0583 | -1.2663 | 543.4 | 535.47 | 0.0453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | TSM | foundry | 406.25 |  | 410.2552 | -0.9763 | 414.385 | 406.61 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 516.13 |  | 514.9079 | 0.2373 | 515.825 | 512.23 | 0.0988 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.04 |  | 330.0589 | 0.6002 | 328.98 | 326.885 | 0.0663 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.73 |  | 474.0336 | 0.3579 | 474.085 | 467.64 | 4.7001 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | APD | industrial_gases | 296.42 |  | 294.8231 | 0.5416 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 402.1 |  | 397.7142 | 1.1027 | 398.69 | 392.2 | 0.4029 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AMZN | cloud_ai_capex | 255.66 |  | 255.4557 | 0.08 | 258.07 | 252.62 | 0.176 | watch_only | none |
| 7 | GEV | data_center_power_cooling | 1025.02 |  | 1029.2673 | -0.4127 | 1035.07 | 1021.09 | 4.1658 | below_vwap | below_vwap,spread_too_wide |
| 8 | ASML | semiconductor_equipment | 1807.16 |  | 1822.3089 | -0.8313 | 1823.13 | 1796.26 | 0.0885 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 566.81 |  | 572.8047 | -1.0466 | 572.69 | 562.32 | 2.7152 | below_vwap | below_vwap,spread_too_wide |
| 10 | KLAC | semiconductor_equipment | 219.56 |  | 221.6076 | -0.924 | 222.19 | 218.09 | 0.0729 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 752.26 |  | 752.7417 | -0.064 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.93 |  | 296.4031 | -0.1596 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 134.67 |  | 135.1529 | -0.3573 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | GOOGL | cloud_ai_capex | 371.3 |  | 371.8765 | -0.155 | 375.18 | 369.2 | 0.4175 | below_vwap | below_vwap,spread_too_wide |
| 16 | META | cloud_ai_capex | 668.83 |  | 673.2677 | -0.6591 | 680.09 | 667.1 | 0.2392 | below_vwap | below_vwap |
| 17 | ANET | ai_networking_optical | 166.87 |  | 166.4091 | 0.277 | 169.91 | 165.6 | 4.6323 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | JCI | data_center_power_cooling | 140.81 |  | 140.529 | 0.2 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SOXX | semiconductor_index | 529.27 |  | 536.0583 | -1.2663 | 543.4 | 535.47 | 0.0453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | TSM | foundry | 406.25 |  | 410.2552 | -0.9763 | 414.385 | 406.61 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.81 |  | 709.9489 | -0.3013 | 713.55 | 708.25 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.36 |  | 72.0323 | -0.9333 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.16 |  | 207.5092 | -0.1683 | 211.03 | 207.49 | 0.5841 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 402.1 |  | 397.7142 | 1.1027 | 398.69 | 392.2 | 0.4029 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 332.04 |  | 330.0589 | 0.6002 | 328.98 | 326.885 | 0.0663 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.3 |  | 371.8765 | -0.155 | 375.18 | 369.2 | 0.4175 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 499.58 |  | 507.1681 | -1.4962 | 518.33 | 507.62 | 0.6065 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.25 |  | 410.2552 | -0.9763 | 414.385 | 406.61 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.27 |  | 536.0583 | -1.2663 | 543.4 | 535.47 | 0.0453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.81 |  | 573.6457 | -0.843 | 580.31 | 572.21 | 0.0721 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.4 |  | 381.216 | -1.001 | 386.58 | 378.53 | 1.0864 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 847.95 |  | 860.1699 | -1.4206 | 887.1 | 866.765 | 0.8125 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.18 |  | 192.2707 | -2.1276 | 201.61 | 194.19 | 0.9937 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.395 |  | 403.342 | -0.7306 | 411.65 | 400.635 | 1.1039 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.15 |  | 46.0202 | -1.891 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.975 |  | 25.4881 | -2.0131 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.26 |  | 752.7417 | -0.064 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 295.93 |  | 296.4031 | -0.1596 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.41 |  | 126.7605 | -0.2765 | 131.36 | 126.665 | 2.8162 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.05 |  | 73.5149 | -0.6324 | 75.54 | 73.985 | 4.6407 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 291.16 |  | 294.796 | -1.2334 | 300.385 | 293.64 | 2.2359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 395.06 |  | 400.0575 | -1.2492 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 628.275 |  | 632.1771 | -0.6173 | 640.25 | 631.005 | 0.616 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1025.02 |  | 1029.2673 | -0.4127 | 1035.07 | 1021.09 | 4.1658 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.73 |  | 474.0336 | 0.3579 | 474.085 | 467.64 | 4.7001 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.81 |  | 140.529 | 0.2 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.87 |  | 166.4091 | 0.277 | 169.91 | 165.6 | 4.6323 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.91 |  | 281.9632 | -1.4375 | 288.48 | 280.67 | 2.7707 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.11 |  | 711.0913 | -1.9662 | 737.175 | 720.21 | 2.8417 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.49 |  | 396.3727 | -1.4841 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.02 |  | 102.1009 | -3.0175 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.53 |  | 324.5586 | -2.4737 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1807.16 |  | 1822.3089 | -0.8313 | 1823.13 | 1796.26 | 0.0885 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.81 |  | 572.8047 | -1.0466 | 572.69 | 562.32 | 2.7152 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.73 |  | 324.9939 | -1.312 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.56 |  | 221.6076 | -0.924 | 222.19 | 218.09 | 0.0729 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 324.26 |  | 327.5402 | -1.0015 | 332.49 | 326.685 | 0.626 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 284.38 |  | 289.2336 | -1.6781 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.115 |  | 64.349 | -1.9176 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.62 |  | 52.2972 | -1.2949 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.67 |  | 135.1529 | -0.3573 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.645 |  | 338.7585 | -0.9191 | 346.26 | 338 | 3.754 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.13 |  | 514.9079 | 0.2373 | 515.825 | 512.23 | 0.0988 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.42 |  | 294.8231 | 0.5416 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.21 |  | 27.0236 | -3.0107 | 28.05 | 27.6 | 0.0763 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.88 |  | 35.7116 | -2.3285 | 37.365 | 36.4 | 0.086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.895 |  | 21.3415 | -2.0922 | 22.18 | 21.78 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1442.22 |  | 1475.0668 | -2.2268 | 1549.47 | 1482.06 | 4.9923 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.51 |  | 477.2387 | -3.7148 | 498.04 | 480.14 | 0.4527 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 751.6 |  | 769.0779 | -2.2726 | 797.155 | 768.7 | 3.8012 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.66 |  | 255.4557 | 0.08 | 258.07 | 252.62 | 0.176 | watch_only | none |
| META | cloud_ai_capex | 668.83 |  | 673.2677 | -0.6591 | 680.09 | 667.1 | 0.2392 | below_vwap | below_vwap |
| ARM | ai_accelerator | 254.76 |  | 257.5107 | -1.0682 | 265.96 | 258.1 | 1.8606 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 158.69 |  | 163.2019 | -2.7646 | 168.11 | 162.41 | 3.781 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
