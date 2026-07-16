# Intraday State

- Generated at: `2026-07-17T03:31:20+08:00`
- Market time ET: `2026-07-16T15:31:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'manual_confirm_candidate': 2, 'spread_too_wide_or_missing': 6, 'price_stale_or_missing': 1, 'below_vwap': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.43 |  | 708.803 | -0.617 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.62 |  | 533.2037 | -0.8597 | 543.4 | 535.47 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.74 |  | 571.3819 | -0.8124 | 580.31 | 572.21 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.94 |  | 751.9415 | -0.3992 | 753.51 | 751.13 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.14 |  | 140.5748 | 0.4021 | 140.83 | 139.43 | 0.085 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.34 |  | 400.0892 | 0.3126 | 398.69 | 392.2 | 0.1694 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.14 |  | 140.5748 | 0.4021 | 140.83 | 139.43 | 0.085 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.34 |  | 400.0892 | 0.3126 | 398.69 | 392.2 | 0.1694 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 295.595 |  | 295.1202 | 0.1609 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | TT | data_center_power_cooling | 475.12 |  | 474.2439 | 0.1847 | 474.085 | 467.64 | 4.8198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | LIN | industrial_gases | 517.365 |  | 515.4969 | 0.3624 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 166.72 |  | 166.6036 | 0.0698 | 169.91 | 165.6 | 3.257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | GEV | data_center_power_cooling | 1030.9 |  | 1027.1831 | 0.3619 | 1035.07 | 1021.09 | 4.4621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | CRWV | gpu_cloud_ai_factory | 73.36 |  | 73.295 | 0.0887 | 75.54 | 73.985 | 0.1363 | below_opening_15m_low | below_opening_15m_low |
| 9 | AAPL | mega_cap_platform | 333.085 |  | 331.3968 | 0.5094 | 328.98 | 326.885 | 0.3753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | IWM | market_regime | 294.77 |  | 295.962 | -0.4028 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 218.48 |  | 220.6981 | -1.0051 | 222.19 | 218.09 | 0.1877 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 563.7 |  | 568.9583 | -0.9242 | 572.69 | 562.32 | 2.9306 | below_vwap | below_vwap,spread_too_wide |
| 14 | SOXX | semiconductor_index | 528.62 |  | 533.2037 | -0.8597 | 543.4 | 535.47 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | TSM | foundry | 406.49 |  | 408.504 | -0.493 | 414.385 | 406.61 | 0.0935 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 704.43 |  | 708.803 | -0.617 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.33 |  | 207.3217 | -0.4783 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SMH | semiconductor_index | 566.74 |  | 571.3819 | -0.8124 | 580.31 | 572.21 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SPY | market_regime | 748.94 |  | 751.9415 | -0.3992 | 753.51 | 751.13 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | HPE | ai_server_oem | 45.29 |  | 45.7277 | -0.9572 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.14 |  | 140.5748 | 0.4021 | 140.83 | 139.43 | 0.085 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.34 |  | 400.0892 | 0.3126 | 398.69 | 392.2 | 0.1694 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.12 |  | 474.2439 | 0.1847 | 474.085 | 467.64 | 4.8198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 517.365 |  | 515.4969 | 0.3624 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.595 |  | 295.1202 | 0.1609 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | AAPL | mega_cap_platform | 333.085 |  | 331.3968 | 0.5094 | 328.98 | 326.885 | 0.3753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AMAT | semiconductor_equipment | 563.7 |  | 568.9583 | -0.9242 | 572.69 | 562.32 | 2.9306 | below_vwap | below_vwap,spread_too_wide |
| 8 | KLAC | semiconductor_equipment | 218.48 |  | 220.6981 | -1.0051 | 222.19 | 218.09 | 0.1877 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 294.77 |  | 295.962 | -0.4028 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ANET | ai_networking_optical | 166.72 |  | 166.6036 | 0.0698 | 169.91 | 165.6 | 3.257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | GEV | data_center_power_cooling | 1030.9 |  | 1027.1831 | 0.3619 | 1035.07 | 1021.09 | 4.4621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | CRWV | gpu_cloud_ai_factory | 73.36 |  | 73.295 | 0.0887 | 75.54 | 73.985 | 0.1363 | below_opening_15m_low | below_opening_15m_low |
| 14 | SOXX | semiconductor_index | 528.62 |  | 533.2037 | -0.8597 | 543.4 | 535.47 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | TSM | foundry | 406.49 |  | 408.504 | -0.493 | 414.385 | 406.61 | 0.0935 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | CIEN | ai_networking_optical | 388.9 |  | 393.2965 | -1.1179 | 410 | 397.68 | 1.3628 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | QQQ | market_regime | 704.43 |  | 708.803 | -0.617 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AVGO | custom_silicon_networking | 376.04 |  | 379.369 | -0.8775 | 386.58 | 378.53 | 1.5956 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | MU | memory_hbm_storage | 849.16 |  | 855.746 | -0.7696 | 887.1 | 866.765 | 0.2497 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | VRT | data_center_power_cooling | 291.52 |  | 292.9922 | -0.5025 | 300.385 | 293.64 | 1.2315 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.43 |  | 708.803 | -0.617 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.21 |  | 71.6595 | -2.0227 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.33 |  | 207.3217 | -0.4783 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.34 |  | 400.0892 | 0.3126 | 398.69 | 392.2 | 0.1694 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.085 |  | 331.3968 | 0.5094 | 328.98 | 326.885 | 0.3753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 354.46 |  | 365.8874 | -3.1232 | 375.18 | 369.2 | 0.2285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 497.64 |  | 502.676 | -1.0018 | 518.33 | 507.62 | 1.2378 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.49 |  | 408.504 | -0.493 | 414.385 | 406.61 | 0.0935 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.62 |  | 533.2037 | -0.8597 | 543.4 | 535.47 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.74 |  | 571.3819 | -0.8124 | 580.31 | 572.21 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.04 |  | 379.369 | -0.8775 | 386.58 | 378.53 | 1.5956 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 849.16 |  | 855.746 | -0.7696 | 887.1 | 866.765 | 0.2497 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.97 |  | 190.5581 | -1.3582 | 201.61 | 194.19 | 0.133 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 395.12 |  | 401.396 | -1.5635 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.29 |  | 45.7277 | -0.9572 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.015 |  | 25.2809 | -1.0518 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.94 |  | 751.9415 | -0.3992 | 753.51 | 751.13 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.77 |  | 295.962 | -0.4028 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.24 |  | 126.4042 | -1.7122 | 131.36 | 126.665 | 3.9842 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.36 |  | 73.295 | 0.0887 | 75.54 | 73.985 | 0.1363 | below_opening_15m_low | below_opening_15m_low |
| VRT | data_center_power_cooling | 291.52 |  | 292.9922 | -0.5025 | 300.385 | 293.64 | 1.2315 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.78 |  | 399.1636 | -0.5971 | 406.24 | 399.495 | 1.1921 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 629.63 |  | 631.0674 | -0.2278 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.9 |  | 1027.1831 | 0.3619 | 1035.07 | 1021.09 | 4.4621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.12 |  | 474.2439 | 0.1847 | 474.085 | 467.64 | 4.8198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.14 |  | 140.5748 | 0.4021 | 140.83 | 139.43 | 0.085 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 166.72 |  | 166.6036 | 0.0698 | 169.91 | 165.6 | 3.257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.3 |  | 280.3933 | -1.8165 | 288.48 | 280.67 | 0.6647 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.59 |  | 707.1733 | -0.7895 | 737.175 | 720.21 | 3.2042 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.9 |  | 393.2965 | -1.1179 | 410 | 397.68 | 1.3628 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 99.74 |  | 101.0181 | -1.2652 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.29 |  | 322.7587 | -1.3845 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1792.06 |  | 1814.1675 | -1.2186 | 1823.13 | 1796.26 | 2.3548 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 563.7 |  | 568.9583 | -0.9242 | 572.69 | 562.32 | 2.9306 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.76 |  | 322.3476 | -1.113 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.48 |  | 220.6981 | -1.0051 | 222.19 | 218.09 | 0.1877 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.925 |  | 325.9058 | -0.9146 | 332.49 | 326.685 | 4.0783 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 281.36 |  | 285.1627 | -1.3335 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.19 |  | 63.8052 | -0.9642 | 66.19 | 63.93 | 4.6843 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.08 |  | 51.7133 | -1.2247 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.26 |  | 134.5133 | -0.9317 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.98 |  | 333.7799 | -1.1384 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.365 |  | 515.4969 | 0.3624 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.595 |  | 295.1202 | 0.1609 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.395 |  | 26.7554 | -1.3469 | 28.05 | 27.6 | 0.0379 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.375 |  | 35.4988 | -0.3488 | 37.365 | 36.4 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.06 |  | 21.1923 | -0.6242 | 22.18 | 21.78 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1416.94 |  | 1453.3212 | -2.5033 | 1549.47 | 1482.06 | 3.2464 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 461.99 |  | 472.178 | -2.1577 | 498.04 | 480.14 | 1.5541 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 746.69 |  | 761.7804 | -1.9809 | 797.155 | 768.7 | 0.4071 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 251.41 |  | 254.7668 | -1.3176 | 258.07 | 252.62 | 0.0239 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 663.2 |  | 670.5394 | -1.0945 | 680.09 | 667.1 | 3.364 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 257.05 |  | 257.2279 | -0.0691 | 265.96 | 258.1 | 3.8903 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.81 |  | 161.2411 | -3.3683 | 168.11 | 162.41 | 1.3478 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
