# Intraday State

- Generated at: `2026-07-17T03:55:15+08:00`
- Market time ET: `2026-07-16T15:55:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'watch_only': 1, 'price_stale_or_missing': 1, 'below_vwap': 3, 'spread_too_wide_or_missing': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.89 |  | 708.1581 | -0.4615 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.27 |  | 532.078 | -0.7157 | 543.4 | 535.47 | 0.0965 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.185 |  | 570.7525 | -0.6251 | 580.31 | 572.21 | 0.0758 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.96 |  | 751.2192 | -0.1676 | 753.51 | 751.13 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.94 |  | 400.1086 | 0.2078 | 398.69 | 392.2 | 0.2943 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.6 |  | 331.4651 | 0.3424 | 328.98 | 326.885 | 0.1233 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.94 |  | 400.1086 | 0.2078 | 398.69 | 392.2 | 0.2943 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.6 |  | 331.4651 | 0.3424 | 328.98 | 326.885 | 0.1233 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 408.86 |  | 408.318 | 0.1327 | 414.385 | 406.61 | 0.2666 | watch_only | none |
| 4 | TT | data_center_power_cooling | 474.99 |  | 474.4018 | 0.124 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | VRT | data_center_power_cooling | 293.69 |  | 293.0192 | 0.2289 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 141.29 |  | 140.622 | 0.4751 | 140.83 | 139.43 | 5.0393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | GEV | data_center_power_cooling | 1034 |  | 1027.5157 | 0.6311 | 1035.07 | 1021.09 | 3.1402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | LIN | industrial_gases | 521.26 |  | 516.1822 | 0.9837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 219.43 |  | 220.1479 | -0.3261 | 222.19 | 218.09 | 0.123 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.32 |  | 295.8425 | -0.1766 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 168.21 |  | 166.7212 | 0.893 | 169.91 | 165.6 | 3.8107 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ARM | ai_accelerator | 259.85 |  | 257.335 | 0.9773 | 265.96 | 258.1 | 3.4866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | APD | industrial_gases | 298.07 |  | 295.3018 | 0.9374 | 293.89 | 291.35 | 3.214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SOXX | semiconductor_index | 528.27 |  | 532.078 | -0.7157 | 543.4 | 535.47 | 0.0965 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 704.89 |  | 708.1581 | -0.4615 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | ASML | semiconductor_equipment | 1788.76 |  | 1808.5956 | -1.0967 | 1823.13 | 1796.26 | 0.0967 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SMH | semiconductor_index | 567.185 |  | 570.7525 | -0.6251 | 580.31 | 572.21 | 0.0758 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SPY | market_regime | 749.96 |  | 751.2192 | -0.1676 | 753.51 | 751.13 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | DELL | ai_server_oem | 392.69 |  | 400.3082 | -1.9031 | 411.65 | 400.635 | 0.0993 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.94 |  | 400.1086 | 0.2078 | 398.69 | 392.2 | 0.2943 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.6 |  | 331.4651 | 0.3424 | 328.98 | 326.885 | 0.1233 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.99 |  | 474.4018 | 0.124 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | JCI | data_center_power_cooling | 141.29 |  | 140.622 | 0.4751 | 140.83 | 139.43 | 5.0393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | LIN | industrial_gases | 521.26 |  | 516.1822 | 0.9837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 298.07 |  | 295.3018 | 0.9374 | 293.89 | 291.35 | 3.214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | TSM | foundry | 408.86 |  | 408.318 | 0.1327 | 414.385 | 406.61 | 0.2666 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 219.43 |  | 220.1479 | -0.3261 | 222.19 | 218.09 | 0.123 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.32 |  | 295.8425 | -0.1766 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ANET | ai_networking_optical | 168.21 |  | 166.7212 | 0.893 | 169.91 | 165.6 | 3.8107 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | VRT | data_center_power_cooling | 293.69 |  | 293.0192 | 0.2289 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1034 |  | 1027.5157 | 0.6311 | 1035.07 | 1021.09 | 3.1402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ARM | ai_accelerator | 259.85 |  | 257.335 | 0.9773 | 265.96 | 258.1 | 3.4866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SOXX | semiconductor_index | 528.27 |  | 532.078 | -0.7157 | 543.4 | 535.47 | 0.0965 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | CIEN | ai_networking_optical | 389.385 |  | 392.4837 | -0.7895 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 17 | QQQ | market_regime | 704.89 |  | 708.1581 | -0.4615 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AVGO | custom_silicon_networking | 374.91 |  | 377.9504 | -0.8044 | 386.58 | 378.53 | 1.0082 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | MU | memory_hbm_storage | 852.27 |  | 855.064 | -0.3268 | 887.1 | 866.765 | 0.2206 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | NVDA | ai_accelerator | 206.56 |  | 207.2332 | -0.3249 | 211.03 | 207.49 | 0.5083 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.89 |  | 708.1581 | -0.4615 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.42 |  | 71.5219 | -1.5407 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.56 |  | 207.2332 | -0.3249 | 211.03 | 207.49 | 0.5083 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 400.94 |  | 400.1086 | 0.2078 | 398.69 | 392.2 | 0.2943 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.6 |  | 331.4651 | 0.3424 | 328.98 | 326.885 | 0.1233 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 353.27 |  | 364.535 | -3.0902 | 375.18 | 369.2 | 0.1444 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 497.29 |  | 501.9054 | -0.9196 | 518.33 | 507.62 | 1.6952 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 408.86 |  | 408.318 | 0.1327 | 414.385 | 406.61 | 0.2666 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.27 |  | 532.078 | -0.7157 | 543.4 | 535.47 | 0.0965 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.185 |  | 570.7525 | -0.6251 | 580.31 | 572.21 | 0.0758 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 374.91 |  | 377.9504 | -0.8044 | 386.58 | 378.53 | 1.0082 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 852.27 |  | 855.064 | -0.3268 | 887.1 | 866.765 | 0.2206 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.095 |  | 190.1562 | -1.0839 | 201.61 | 194.19 | 0.1382 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 392.69 |  | 400.3082 | -1.9031 | 411.65 | 400.635 | 0.0993 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 45.145 |  | 45.6971 | -1.2081 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.755 |  | 25.2295 | -1.8808 | 26.71 | 25.74 | 0.0404 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.96 |  | 751.2192 | -0.1676 | 753.51 | 751.13 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.32 |  | 295.8425 | -0.1766 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.49 |  | 125.9784 | -1.1815 | 131.36 | 126.665 | 0.0803 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.94 |  | 73.2379 | -0.4067 | 75.54 | 73.985 | 0.7678 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.69 |  | 293.0192 | 0.2289 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 396.06 |  | 398.9761 | -0.7309 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.84 |  | 630.9047 | -0.1688 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1034 |  | 1027.5157 | 0.6311 | 1035.07 | 1021.09 | 3.1402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 474.99 |  | 474.4018 | 0.124 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.29 |  | 140.622 | 0.4751 | 140.83 | 139.43 | 5.0393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 168.21 |  | 166.7212 | 0.893 | 169.91 | 165.6 | 3.8107 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.35 |  | 279.8788 | -1.2608 | 288.48 | 280.67 | 2.533 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 705.22 |  | 706.6634 | -0.2043 | 737.175 | 720.21 | 4.1122 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 389.385 |  | 392.4837 | -0.7895 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.97 |  | 100.8244 | -0.8474 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.99 |  | 322.0528 | -0.951 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1788.76 |  | 1808.5956 | -1.0967 | 1823.13 | 1796.26 | 0.0967 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 559.89 |  | 567.2526 | -1.2979 | 572.69 | 562.32 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 318.94 |  | 321.4457 | -0.7795 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.43 |  | 220.1479 | -0.3261 | 222.19 | 218.09 | 0.123 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 320.49 |  | 324.4575 | -1.2228 | 332.49 | 326.685 | 4.593 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 281.23 |  | 284.644 | -1.1994 | 295.83 | 285.02 | 4.6972 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.88 |  | 63.6776 | -1.2525 | 66.19 | 63.93 | 0.8588 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.48 |  | 51.6584 | -0.3454 | 52.72 | 51.735 | 0.2914 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ENTG | semiconductor_materials | 133.3 |  | 134.1176 | -0.6096 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.47 |  | 333.1071 | -1.0919 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 521.26 |  | 516.1822 | 0.9837 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.07 |  | 295.3018 | 0.9374 | 293.89 | 291.35 | 3.214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.18 |  | 26.7094 | -1.9822 | 28.05 | 27.6 | 0.0382 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.855 |  | 35.4412 | -1.654 | 37.365 | 36.4 | 0.0287 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.975 |  | 21.1668 | -0.906 | 22.18 | 21.78 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1411.535 |  | 1447.9003 | -2.5116 | 1549.47 | 1482.06 | 0.1714 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| WDC | memory_hbm_storage | 465.11 |  | 471.3558 | -1.3251 | 498.04 | 480.14 | 4.3452 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 745.03 |  | 758.6399 | -1.794 | 797.155 | 768.7 | 4.883 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 249.19 |  | 254.1134 | -1.9375 | 258.07 | 252.62 | 0.0843 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 662.83 |  | 669.6841 | -1.0235 | 680.09 | 667.1 | 0.0438 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 259.85 |  | 257.335 | 0.9773 | 265.96 | 258.1 | 3.4866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 154.59 |  | 160.8935 | -3.9178 | 168.11 | 162.41 | 0.6469 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
