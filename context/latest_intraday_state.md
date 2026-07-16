# Intraday State

- Generated at: `2026-07-17T03:19:26+08:00`
- Market time ET: `2026-07-16T15:19:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 4, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.49 |  | 709.0489 | -0.643 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.42 |  | 533.5531 | -1.1495 | 543.4 | 535.47 | 0.0645 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.18 |  | 571.5163 | -0.9337 | 580.31 | 572.21 | 0.0636 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.74 |  | 752.0891 | -0.3123 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.12 |  | 400.0015 | 0.5296 | 398.69 | 392.2 | 0.3084 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.25 |  | 331.2039 | 0.9197 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.12 |  | 400.0015 | 0.5296 | 398.69 | 392.2 | 0.3084 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 140.88 |  | 140.5615 | 0.2266 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | TT | data_center_power_cooling | 475.72 |  | 474.1694 | 0.327 | 474.085 | 467.64 | 4.6288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | AAPL | mega_cap_platform | 334.25 |  | 331.2039 | 0.9197 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 167.045 |  | 166.5948 | 0.2702 | 169.91 | 165.6 | 4.6215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GEV | data_center_power_cooling | 1028.605 |  | 1027.1136 | 0.1452 | 1035.07 | 1021.09 | 3.6914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 518.91 |  | 515.3862 | 0.6837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 296.77 |  | 295.0429 | 0.5854 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | CRWV | gpu_cloud_ai_factory | 73.3 |  | 73.2955 | 0.0061 | 75.54 | 73.985 | 0.0819 | below_opening_15m_low | below_opening_15m_low |
| 10 | KLAC | semiconductor_equipment | 219.3 |  | 220.8708 | -0.7112 | 222.19 | 218.09 | 0.0456 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 294.91 |  | 296.0261 | -0.377 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 133.76 |  | 134.7209 | -0.7133 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | SOXX | semiconductor_index | 527.42 |  | 533.5531 | -1.1495 | 543.4 | 535.47 | 0.0645 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | TSM | foundry | 406.41 |  | 408.6624 | -0.5512 | 414.385 | 406.61 | 0.0689 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 704.49 |  | 709.0489 | -0.643 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 375.48 |  | 379.5016 | -1.0597 | 386.58 | 378.53 | 0.1012 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 206.995 |  | 207.3397 | -0.1662 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AMD | ai_accelerator | 496.625 |  | 503.2042 | -1.3075 | 518.33 | 507.62 | 0.0785 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | ASML | semiconductor_equipment | 1790.365 |  | 1815.8962 | -1.406 | 1823.13 | 1796.26 | 0.1084 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.12 |  | 400.0015 | 0.5296 | 398.69 | 392.2 | 0.3084 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.25 |  | 331.2039 | 0.9197 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.72 |  | 474.1694 | 0.327 | 474.085 | 467.64 | 4.6288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | JCI | data_center_power_cooling | 140.88 |  | 140.5615 | 0.2266 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 518.91 |  | 515.3862 | 0.6837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.77 |  | 295.0429 | 0.5854 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 219.3 |  | 220.8708 | -0.7112 | 222.19 | 218.09 | 0.0456 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 294.91 |  | 296.0261 | -0.377 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ENTG | semiconductor_materials | 133.76 |  | 134.7209 | -0.7133 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ANET | ai_networking_optical | 167.045 |  | 166.5948 | 0.2702 | 169.91 | 165.6 | 4.6215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | GEV | data_center_power_cooling | 1028.605 |  | 1027.1136 | 0.1452 | 1035.07 | 1021.09 | 3.6914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | CRWV | gpu_cloud_ai_factory | 73.3 |  | 73.2955 | 0.0061 | 75.54 | 73.985 | 0.0819 | below_opening_15m_low | below_opening_15m_low |
| 14 | SOXX | semiconductor_index | 527.42 |  | 533.5531 | -1.1495 | 543.4 | 535.47 | 0.0645 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | TSM | foundry | 406.41 |  | 408.6624 | -0.5512 | 414.385 | 406.61 | 0.0689 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | CIEN | ai_networking_optical | 388.43 |  | 393.7836 | -1.3595 | 410 | 397.68 | 0.1725 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 704.49 |  | 709.0489 | -0.643 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AVGO | custom_silicon_networking | 375.48 |  | 379.5016 | -1.0597 | 386.58 | 378.53 | 0.1012 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | MU | memory_hbm_storage | 845.12 |  | 856.1475 | -1.288 | 887.1 | 866.765 | 0.478 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | VRT | data_center_power_cooling | 289.99 |  | 293.1217 | -1.0684 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.49 |  | 709.0489 | -0.643 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.345 |  | 71.7288 | -1.9293 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.995 |  | 207.3397 | -0.1662 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.12 |  | 400.0015 | 0.5296 | 398.69 | 392.2 | 0.3084 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 334.25 |  | 331.2039 | 0.9197 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 353.15 |  | 366.6275 | -3.6761 | 375.18 | 369.2 | 0.3511 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496.625 |  | 503.2042 | -1.3075 | 518.33 | 507.62 | 0.0785 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 406.41 |  | 408.6624 | -0.5512 | 414.385 | 406.61 | 0.0689 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.42 |  | 533.5531 | -1.1495 | 543.4 | 535.47 | 0.0645 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.18 |  | 571.5163 | -0.9337 | 580.31 | 572.21 | 0.0636 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.48 |  | 379.5016 | -1.0597 | 386.58 | 378.53 | 0.1012 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 845.12 |  | 856.1475 | -1.288 | 887.1 | 866.765 | 0.478 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.17 |  | 190.698 | -1.85 | 201.61 | 194.19 | 0.3045 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 395.365 |  | 401.6727 | -1.5704 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.41 |  | 45.7469 | -0.7364 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.99 |  | 25.2959 | -1.2093 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.74 |  | 752.0891 | -0.3123 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.91 |  | 296.0261 | -0.377 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.865 |  | 126.5224 | -1.31 | 131.36 | 126.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 73.3 |  | 73.2955 | 0.0061 | 75.54 | 73.985 | 0.0819 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 289.99 |  | 293.1217 | -1.0684 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 397.2 |  | 399.1855 | -0.4974 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.27 |  | 631.1348 | -0.2955 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.605 |  | 1027.1136 | 0.1452 | 1035.07 | 1021.09 | 3.6914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.72 |  | 474.1694 | 0.327 | 474.085 | 467.64 | 4.6288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.88 |  | 140.5615 | 0.2266 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.045 |  | 166.5948 | 0.2702 | 169.91 | 165.6 | 4.6215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.1 |  | 280.5115 | -1.5727 | 288.48 | 280.67 | 0.7316 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.35 |  | 707.4537 | -1.2868 | 737.175 | 720.21 | 2.7164 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.43 |  | 393.7836 | -1.3595 | 410 | 397.68 | 0.1725 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.38 |  | 101.1568 | -1.7565 | 106.975 | 102.85 | 4.6287 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 317 |  | 323.088 | -1.8843 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1790.365 |  | 1815.8962 | -1.406 | 1823.13 | 1796.26 | 0.1084 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.74 |  | 569.4011 | -1.5211 | 572.69 | 562.32 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 317.805 |  | 322.6039 | -1.4876 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.3 |  | 220.8708 | -0.7112 | 222.19 | 218.09 | 0.0456 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.21 |  | 326.3072 | -1.5621 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.41 |  | 286.1437 | -2.0038 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.75 |  | 63.8362 | -1.7016 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.65 |  | 51.7538 | -2.1327 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.76 |  | 134.7209 | -0.7133 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.54 |  | 333.8966 | -1.3048 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.91 |  | 515.3862 | 0.6837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.77 |  | 295.0429 | 0.5854 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.31 |  | 26.7667 | -1.7061 | 28.05 | 27.6 | 0.2281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.395 |  | 35.5015 | -0.3 | 37.365 | 36.4 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.03 |  | 21.1984 | -0.7945 | 22.18 | 21.78 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1392.22 |  | 1456.4601 | -4.4107 | 1549.47 | 1482.06 | 0.7176 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.555 |  | 472.5609 | -2.7522 | 498.04 | 480.14 | 1.088 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 742.78 |  | 762.5676 | -2.5949 | 797.155 | 768.7 | 4.502 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 251.54 |  | 254.8891 | -1.3139 | 258.07 | 252.62 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 663.88 |  | 670.8956 | -1.0457 | 680.09 | 667.1 | 3.1798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 256.48 |  | 257.259 | -0.3028 | 265.96 | 258.1 | 2.7682 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.89 |  | 161.3451 | -3.381 | 168.11 | 162.41 | 0.2694 | below_opening_15m_low | below_opening_15m_low,below_vwap |
