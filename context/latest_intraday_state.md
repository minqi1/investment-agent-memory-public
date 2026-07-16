# Intraday State

- Generated at: `2026-07-17T03:47:18+08:00`
- Market time ET: `2026-07-16T15:47:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 45, 'below_vwap': 2, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.13 |  | 708.4468 | -0.7505 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 525.95 |  | 532.7602 | -1.2783 | 543.4 | 535.47 | 0.0703 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.8 |  | 571.1879 | -1.1183 | 580.31 | 572.21 | 0.0513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.34 |  | 751.5287 | -0.4243 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.95 |  | 140.5972 | 0.251 | 140.83 | 139.43 | 0.0497 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.495 |  | 295.1749 | 0.4472 | 293.89 | 291.35 | 0.118 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332 |  | 331.4669 | 0.1608 | 328.98 | 326.885 | 0.0271 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.95 |  | 140.5972 | 0.251 | 140.83 | 139.43 | 0.0497 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332 |  | 331.4669 | 0.1608 | 328.98 | 326.885 | 0.0271 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.495 |  | 295.1749 | 0.4472 | 293.89 | 291.35 | 0.118 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.58 |  | 474.3208 | 0.2655 | 474.085 | 467.64 | 4.689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 166.995 |  | 166.6126 | 0.2295 | 169.91 | 165.6 | 4.5989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GEV | data_center_power_cooling | 1032.065 |  | 1027.3613 | 0.4578 | 1035.07 | 1021.09 | 4.6024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ARM | ai_accelerator | 259.06 |  | 257.2693 | 0.6961 | 265.96 | 258.1 | 1.351 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | MSFT | cloud_ai_capex | 399.765 |  | 400.1006 | -0.0839 | 398.69 | 392.2 | 0.1326 | below_vwap | below_vwap |
| 9 | LIN | industrial_gases | 520.16 |  | 515.7133 | 0.8622 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | SOXX | semiconductor_index | 525.95 |  | 532.7602 | -1.2783 | 543.4 | 535.47 | 0.0703 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 12 | TSM | foundry | 406.29 |  | 408.3793 | -0.5116 | 414.385 | 406.61 | 0.0911 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 13 | QQQ | market_regime | 703.13 |  | 708.4468 | -0.7505 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | NVDA | ai_accelerator | 206.035 |  | 207.2743 | -0.5979 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | ASML | semiconductor_equipment | 1782.64 |  | 1811.8702 | -1.6133 | 1823.13 | 1796.26 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | ETN | data_center_power_cooling | 396.47 |  | 399.0873 | -0.6558 | 406.24 | 399.495 | 0.0933 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | SMH | semiconductor_index | 564.8 |  | 571.1879 | -1.1183 | 580.31 | 572.21 | 0.0513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SPY | market_regime | 748.34 |  | 751.5287 | -0.4243 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | IWM | market_regime | 294.52 |  | 295.8957 | -0.4649 | 296.28 | 294.65 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | HPE | ai_server_oem | 45.015 |  | 45.7111 | -1.5227 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.95 |  | 140.5972 | 0.251 | 140.83 | 139.43 | 0.0497 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.495 |  | 295.1749 | 0.4472 | 293.89 | 291.35 | 0.118 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332 |  | 331.4669 | 0.1608 | 328.98 | 326.885 | 0.0271 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 399.765 |  | 400.1006 | -0.0839 | 398.69 | 392.2 | 0.1326 | below_vwap | below_vwap |
| 5 | TT | data_center_power_cooling | 475.58 |  | 474.3208 | 0.2655 | 474.085 | 467.64 | 4.689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | LIN | industrial_gases | 520.16 |  | 515.7133 | 0.8622 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 8 | ANET | ai_networking_optical | 166.995 |  | 166.6126 | 0.2295 | 169.91 | 165.6 | 4.5989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | GEV | data_center_power_cooling | 1032.065 |  | 1027.3613 | 0.4578 | 1035.07 | 1021.09 | 4.6024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ARM | ai_accelerator | 259.06 |  | 257.2693 | 0.6961 | 265.96 | 258.1 | 1.351 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SOXX | semiconductor_index | 525.95 |  | 532.7602 | -1.2783 | 543.4 | 535.47 | 0.0703 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 12 | TSM | foundry | 406.29 |  | 408.3793 | -0.5116 | 414.385 | 406.61 | 0.0911 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 13 | CIEN | ai_networking_optical | 387.43 |  | 392.9218 | -1.3977 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 14 | QQQ | market_regime | 703.13 |  | 708.4468 | -0.7505 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | AVGO | custom_silicon_networking | 372.52 |  | 378.8501 | -1.6709 | 386.58 | 378.53 | 2.416 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 16 | MU | memory_hbm_storage | 845.58 |  | 855.353 | -1.1426 | 887.1 | 866.765 | 0.7084 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | VRT | data_center_power_cooling | 292.065 |  | 293.0031 | -0.3202 | 300.385 | 293.64 | 4.814 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 18 | NVDA | ai_accelerator | 206.035 |  | 207.2743 | -0.5979 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AMD | ai_accelerator | 496.51 |  | 502.2645 | -1.1457 | 518.33 | 507.62 | 1.0795 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | PWR | data_center_power_cooling | 629.34 |  | 630.9811 | -0.2601 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.13 |  | 708.4468 | -0.7505 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 69.865 |  | 71.5775 | -2.3925 | 73.09 | 71.45 | 0.0143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.035 |  | 207.2743 | -0.5979 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.765 |  | 400.1006 | -0.0839 | 398.69 | 392.2 | 0.1326 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 332 |  | 331.4669 | 0.1608 | 328.98 | 326.885 | 0.0271 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 353.64 |  | 365.2215 | -3.1711 | 375.18 | 369.2 | 0.0622 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 496.51 |  | 502.2645 | -1.1457 | 518.33 | 507.62 | 1.0795 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.29 |  | 408.3793 | -0.5116 | 414.385 | 406.61 | 0.0911 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.95 |  | 532.7602 | -1.2783 | 543.4 | 535.47 | 0.0703 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.8 |  | 571.1879 | -1.1183 | 580.31 | 572.21 | 0.0513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 372.52 |  | 378.8501 | -1.6709 | 386.58 | 378.53 | 2.416 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 845.58 |  | 855.353 | -1.1426 | 887.1 | 866.765 | 0.7084 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 186.67 |  | 190.3959 | -1.9569 | 201.61 | 194.19 | 1.1946 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 391.745 |  | 400.8989 | -2.2833 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.015 |  | 45.7111 | -1.5227 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.755 |  | 25.2525 | -1.9703 | 26.71 | 25.74 | 0.0404 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.34 |  | 751.5287 | -0.4243 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.52 |  | 295.8957 | -0.4649 | 296.28 | 294.65 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 123.81 |  | 126.1692 | -1.8698 | 131.36 | 126.665 | 4.9996 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.74 |  | 73.2677 | -0.7202 | 75.54 | 73.985 | 0.0412 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 292.065 |  | 293.0031 | -0.3202 | 300.385 | 293.64 | 4.814 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.47 |  | 399.0873 | -0.6558 | 406.24 | 399.495 | 0.0933 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 629.34 |  | 630.9811 | -0.2601 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1032.065 |  | 1027.3613 | 0.4578 | 1035.07 | 1021.09 | 4.6024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.58 |  | 474.3208 | 0.2655 | 474.085 | 467.64 | 4.689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.95 |  | 140.5972 | 0.251 | 140.83 | 139.43 | 0.0497 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 166.995 |  | 166.6126 | 0.2295 | 169.91 | 165.6 | 4.5989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 274.1 |  | 280.1374 | -2.1551 | 288.48 | 280.67 | 1.6089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.015 |  | 706.9081 | -1.258 | 737.175 | 720.21 | 0.4327 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 387.43 |  | 392.9218 | -1.3977 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.37 |  | 100.9067 | -1.5229 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.08 |  | 322.4328 | -1.9703 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1782.64 |  | 1811.8702 | -1.6133 | 1823.13 | 1796.26 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 558.52 |  | 568.3485 | -1.7293 | 572.69 | 562.32 | 0.3796 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.25 |  | 321.6712 | -1.3744 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.01 |  | 220.3374 | -1.0563 | 222.19 | 218.09 | 1.4816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 318.02 |  | 325.055 | -2.1643 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.92 |  | 284.9944 | -2.1314 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.6 |  | 63.7364 | -1.783 | 66.19 | 63.93 | 1.3898 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.14 |  | 51.6733 | -1.032 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 132.85 |  | 134.2859 | -1.0693 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 327.66 |  | 333.4414 | -1.7338 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 520.16 |  | 515.7133 | 0.8622 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.495 |  | 295.1749 | 0.4472 | 293.89 | 291.35 | 0.118 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.01 |  | 26.725 | -2.6753 | 28.05 | 27.6 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.66 |  | 35.478 | -2.3055 | 37.365 | 36.4 | 0.0289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.875 |  | 21.1775 | -1.4285 | 22.18 | 21.78 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1407 |  | 1449.8486 | -2.9554 | 1549.47 | 1482.06 | 3.1798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 461.325 |  | 471.7515 | -2.2102 | 498.04 | 480.14 | 0.323 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 740.42 |  | 760.0238 | -2.5794 | 797.155 | 768.7 | 0.3593 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 249.665 |  | 254.5217 | -1.9082 | 258.07 | 252.62 | 0.1081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 661.595 |  | 670.0867 | -1.2673 | 680.09 | 667.1 | 3.4356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 259.06 |  | 257.2693 | 0.6961 | 265.96 | 258.1 | 1.351 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 155.97 |  | 161.0768 | -3.1704 | 168.11 | 162.41 | 0.2244 | below_opening_15m_low | below_opening_15m_low,below_vwap |
