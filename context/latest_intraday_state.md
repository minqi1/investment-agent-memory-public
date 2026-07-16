# Intraday State

- Generated at: `2026-07-17T00:56:02+08:00`
- Market time ET: `2026-07-16T12:56:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 13, 'below_opening_15m_low': 33, 'manual_confirm_candidate': 3, 'watch_only': 2, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.545 |  | 710.011 | -0.2065 | 713.55 | 708.25 | 0.0663 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 529.91 |  | 536.1481 | -1.1635 | 543.4 | 535.47 | 0.0774 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.87 |  | 574.2242 | -0.9324 | 580.31 | 572.21 | 0.0316 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.645 |  | 752.7444 | -0.0132 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.985 |  | 514.8888 | 0.2129 | 515.825 | 512.23 | 0.2112 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 403.95 |  | 397.3303 | 1.666 | 398.69 | 392.2 | 0.1238 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.885 |  | 329.9728 | 0.5795 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.985 |  | 514.8888 | 0.2129 | 515.825 | 512.23 | 0.2112 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.045 |  | 371.8808 | 0.0442 | 375.18 | 369.2 | 0.0511 | watch_only | none |
| 3 | AMZN | cloud_ai_capex | 256.25 |  | 255.4304 | 0.3209 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 331.885 |  | 329.9728 | 0.5795 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 474.11 |  | 473.9763 | 0.0282 | 474.085 | 467.64 | 5.0305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 166.66 |  | 166.3207 | 0.204 | 169.91 | 165.6 | 3.1921 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | MSFT | cloud_ai_capex | 403.95 |  | 397.3303 | 1.666 | 398.69 | 392.2 | 0.1238 | buy_precheck_manual_confirm | none |
| 8 | APD | industrial_gases | 296.36 |  | 294.7969 | 0.5302 | 293.89 | 291.35 | 1.0528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | QQQ | market_regime | 708.545 |  | 710.011 | -0.2065 | 713.55 | 708.25 | 0.0663 | below_vwap | below_vwap |
| 10 | ASML | semiconductor_equipment | 1806.91 |  | 1822.6404 | -0.8631 | 1823.13 | 1796.26 | 0.1422 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 752.645 |  | 752.7444 | -0.0132 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.87 |  | 296.4112 | -0.1826 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 13 | META | cloud_ai_capex | 670.555 |  | 673.577 | -0.4487 | 680.09 | 667.1 | 0.0522 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AMAT | semiconductor_equipment | 565 |  | 573.0069 | -1.3973 | 572.69 | 562.32 | 0.1611 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 140.51 |  | 140.5244 | -0.0102 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CRWV | gpu_cloud_ai_factory | 73.53 |  | 73.519 | 0.015 | 75.54 | 73.985 | 4.1344 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | ENTG | semiconductor_materials | 134.27 |  | 135.1633 | -0.6609 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 379.13 |  | 381.4226 | -0.6011 | 386.58 | 378.53 | 1.0788 | below_vwap | below_vwap,spread_too_wide |
| 20 | KLAC | semiconductor_equipment | 218.42 |  | 221.7197 | -1.4882 | 222.19 | 218.09 | 5.0179 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.985 |  | 514.8888 | 0.2129 | 515.825 | 512.23 | 0.2112 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 403.95 |  | 397.3303 | 1.666 | 398.69 | 392.2 | 0.1238 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.885 |  | 329.9728 | 0.5795 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 474.11 |  | 473.9763 | 0.0282 | 474.085 | 467.64 | 5.0305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 296.36 |  | 294.7969 | 0.5302 | 293.89 | 291.35 | 1.0528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GOOGL | cloud_ai_capex | 372.045 |  | 371.8808 | 0.0442 | 375.18 | 369.2 | 0.0511 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 256.25 |  | 255.4304 | 0.3209 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 8 | QQQ | market_regime | 708.545 |  | 710.011 | -0.2065 | 713.55 | 708.25 | 0.0663 | below_vwap | below_vwap |
| 9 | AVGO | custom_silicon_networking | 379.13 |  | 381.4226 | -0.6011 | 386.58 | 378.53 | 1.0788 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 140.51 |  | 140.5244 | -0.0102 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ASML | semiconductor_equipment | 1806.91 |  | 1822.6404 | -0.8631 | 1823.13 | 1796.26 | 0.1422 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 565 |  | 573.0069 | -1.3973 | 572.69 | 562.32 | 0.1611 | below_vwap | below_vwap |
| 13 | KLAC | semiconductor_equipment | 218.42 |  | 221.7197 | -1.4882 | 222.19 | 218.09 | 5.0179 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 752.645 |  | 752.7444 | -0.0132 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.87 |  | 296.4112 | -0.1826 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 134.27 |  | 135.1633 | -0.6609 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ORCL | cloud_ai_capex | 126.73 |  | 126.7614 | -0.0248 | 131.36 | 126.665 | 3.1563 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 670.555 |  | 673.577 | -0.4487 | 680.09 | 667.1 | 0.0522 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 166.66 |  | 166.3207 | 0.204 | 169.91 | 165.6 | 3.1921 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.545 |  | 710.011 | -0.2065 | 713.55 | 708.25 | 0.0663 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.54 |  | 72.0544 | -0.7139 | 73.09 | 71.45 | 0.028 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.385 |  | 207.5295 | -0.0696 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.95 |  | 397.3303 | 1.666 | 398.69 | 392.2 | 0.1238 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.885 |  | 329.9728 | 0.5795 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.045 |  | 371.8808 | 0.0442 | 375.18 | 369.2 | 0.0511 | watch_only | none |
| AMD | ai_accelerator | 499.87 |  | 507.48 | -1.4996 | 518.33 | 507.62 | 1.1423 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.35 |  | 410.377 | -0.9813 | 414.385 | 406.61 | 1.26 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.91 |  | 536.1481 | -1.1635 | 543.4 | 535.47 | 0.0774 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.87 |  | 574.2242 | -0.9324 | 580.31 | 572.21 | 0.0316 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.13 |  | 381.4226 | -0.6011 | 386.58 | 378.53 | 1.0788 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 849.51 |  | 860.5684 | -1.285 | 887.1 | 866.765 | 0.1895 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.31 |  | 192.3665 | -2.1088 | 201.61 | 194.19 | 0.1221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 400.5 |  | 403.4438 | -0.7297 | 411.65 | 400.635 | 4.4295 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.34 |  | 46.0671 | -1.5784 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.08 |  | 25.5157 | -1.7077 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.645 |  | 752.7444 | -0.0132 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.87 |  | 296.4112 | -0.1826 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.73 |  | 126.7614 | -0.0248 | 131.36 | 126.665 | 3.1563 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.53 |  | 73.519 | 0.015 | 75.54 | 73.985 | 4.1344 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 290.085 |  | 294.9479 | -1.6487 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 393.94 |  | 400.1212 | -1.5448 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.02 |  | 632.3255 | -0.839 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1020.695 |  | 1029.3826 | -0.844 | 1035.07 | 1021.09 | 4.4783 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.11 |  | 473.9763 | 0.0282 | 474.085 | 467.64 | 5.0305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.51 |  | 140.5244 | -0.0102 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.66 |  | 166.3207 | 0.204 | 169.91 | 165.6 | 3.1921 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.295 |  | 282.2141 | -1.3887 | 288.48 | 280.67 | 4.8653 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698 |  | 711.5055 | -1.8982 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 391.94 |  | 396.5467 | -1.1617 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.92 |  | 102.207 | -3.216 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.78 |  | 324.7775 | -1.5387 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1806.91 |  | 1822.6404 | -0.8631 | 1823.13 | 1796.26 | 0.1422 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565 |  | 573.0069 | -1.3973 | 572.69 | 562.32 | 0.1611 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.8 |  | 325.1991 | -1.6602 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.42 |  | 221.7197 | -1.4882 | 222.19 | 218.09 | 5.0179 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 323.32 |  | 327.6177 | -1.3118 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.96 |  | 289.5487 | -1.5848 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.12 |  | 64.3889 | -1.9706 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.38 |  | 52.2999 | -1.7589 | 52.72 | 51.735 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.27 |  | 135.1633 | -0.6609 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.11 |  | 338.8412 | -1.1012 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 515.985 |  | 514.8888 | 0.2129 | 515.825 | 512.23 | 0.2112 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.36 |  | 294.7969 | 0.5302 | 293.89 | 291.35 | 1.0528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.405 |  | 27.0483 | -2.3783 | 28.05 | 27.6 | 0.0379 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35 |  | 35.7393 | -2.0686 | 37.365 | 36.4 | 0.0571 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.97 |  | 21.3648 | -1.848 | 22.18 | 21.78 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1441.04 |  | 1475.8842 | -2.3609 | 1549.47 | 1482.06 | 4.1068 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 460.38 |  | 477.5942 | -3.6044 | 498.04 | 480.14 | 2.8107 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 756.17 |  | 769.4268 | -1.7229 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 256.25 |  | 255.4304 | 0.3209 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 670.555 |  | 673.577 | -0.4487 | 680.09 | 667.1 | 0.0522 | below_vwap | below_vwap |
| ARM | ai_accelerator | 253.97 |  | 257.7005 | -1.4476 | 265.96 | 258.1 | 2.6381 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 160.07 |  | 163.3175 | -1.9885 | 168.11 | 162.41 | 2.805 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
