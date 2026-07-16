# Intraday State

- Generated at: `2026-07-17T00:24:19+08:00`
- Market time ET: `2026-07-16T12:24:20-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 36, 'manual_confirm_candidate': 2, 'below_vwap': 13, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.18 |  | 710.2349 | -0.4301 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.855 |  | 536.9214 | -1.5023 | 543.4 | 535.47 | 0.0624 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.35 |  | 574.7293 | -1.11 | 580.31 | 572.21 | 0.088 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.76 |  | 752.8161 | -0.1403 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.175 |  | 396.6148 | 0.8976 | 398.69 | 392.2 | 0.1025 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.26 |  | 329.8651 | 0.4229 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.26 |  | 329.8651 | 0.4229 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.59 |  | 255.387 | 0.0795 | 258.07 | 252.62 | 0.0391 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 400.175 |  | 396.6148 | 0.8976 | 398.69 | 392.2 | 0.1025 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 516.12 |  | 514.7689 | 0.2625 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 166.49 |  | 166.32 | 0.1022 | 169.91 | 165.6 | 4.9553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.41 |  | 294.6849 | 0.5854 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SPY | market_regime | 751.76 |  | 752.8161 | -0.1403 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.46 |  | 296.517 | -0.3565 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ASML | semiconductor_equipment | 1804.34 |  | 1824.292 | -1.0937 | 1823.13 | 1796.26 | 0.1635 | below_vwap | below_vwap |
| 11 | KLAC | semiconductor_equipment | 218.35 |  | 222.1871 | -1.727 | 222.19 | 218.09 | 0.1695 | below_vwap | below_vwap |
| 12 | TT | data_center_power_cooling | 473.53 |  | 474.3655 | -0.1761 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 139.96 |  | 140.6047 | -0.4585 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 370.74 |  | 371.9146 | -0.3158 | 375.18 | 369.2 | 0.2293 | below_vwap | below_vwap |
| 15 | ENTG | semiconductor_materials | 133.785 |  | 135.4542 | -1.2323 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 51.88 |  | 52.3223 | -0.8454 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 380 |  | 381.6967 | -0.4445 | 386.58 | 378.53 | 1.3421 | below_vwap | below_vwap,spread_too_wide |
| 18 | AMAT | semiconductor_equipment | 566.42 |  | 574.0263 | -1.3251 | 572.69 | 562.32 | 1.4936 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 668.89 |  | 674.4295 | -0.8214 | 680.09 | 667.1 | 1.1885 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 528.855 |  | 536.9214 | -1.5023 | 543.4 | 535.47 | 0.0624 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.175 |  | 396.6148 | 0.8976 | 398.69 | 392.2 | 0.1025 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.26 |  | 329.8651 | 0.4229 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 516.12 |  | 514.7689 | 0.2625 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.41 |  | 294.6849 | 0.5854 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | AMZN | cloud_ai_capex | 255.59 |  | 255.387 | 0.0795 | 258.07 | 252.62 | 0.0391 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 380 |  | 381.6967 | -0.4445 | 386.58 | 378.53 | 1.3421 | below_vwap | below_vwap,spread_too_wide |
| 7 | TT | data_center_power_cooling | 473.53 |  | 474.3655 | -0.1761 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 139.96 |  | 140.6047 | -0.4585 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ASML | semiconductor_equipment | 1804.34 |  | 1824.292 | -1.0937 | 1823.13 | 1796.26 | 0.1635 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 566.42 |  | 574.0263 | -1.3251 | 572.69 | 562.32 | 1.4936 | below_vwap | below_vwap,spread_too_wide |
| 11 | KLAC | semiconductor_equipment | 218.35 |  | 222.1871 | -1.727 | 222.19 | 218.09 | 0.1695 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 751.76 |  | 752.8161 | -0.1403 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 295.46 |  | 296.517 | -0.3565 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 133.785 |  | 135.4542 | -1.2323 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | GOOGL | cloud_ai_capex | 370.74 |  | 371.9146 | -0.3158 | 375.18 | 369.2 | 0.2293 | below_vwap | below_vwap |
| 17 | COHU | semiconductor_test_packaging | 51.88 |  | 52.3223 | -0.8454 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | META | cloud_ai_capex | 668.89 |  | 674.4295 | -0.8214 | 680.09 | 667.1 | 1.1885 | below_vwap | below_vwap,spread_too_wide |
| 19 | ANET | ai_networking_optical | 166.49 |  | 166.32 | 0.1022 | 169.91 | 165.6 | 4.9553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SOXX | semiconductor_index | 528.855 |  | 536.9214 | -1.5023 | 543.4 | 535.47 | 0.0624 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.18 |  | 710.2349 | -0.4301 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.205 |  | 72.1263 | -1.2774 | 73.09 | 71.45 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.815 |  | 207.5657 | -0.3617 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.175 |  | 396.6148 | 0.8976 | 398.69 | 392.2 | 0.1025 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.26 |  | 329.8651 | 0.4229 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.74 |  | 371.9146 | -0.3158 | 375.18 | 369.2 | 0.2293 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.61 |  | 508.9309 | -1.8315 | 518.33 | 507.62 | 2.7722 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.28 |  | 410.7895 | -1.0978 | 414.385 | 406.61 | 3.3647 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.855 |  | 536.9214 | -1.5023 | 543.4 | 535.47 | 0.0624 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.35 |  | 574.7293 | -1.11 | 580.31 | 572.21 | 0.088 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380 |  | 381.6967 | -0.4445 | 386.58 | 378.53 | 1.3421 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.47 |  | 862.7223 | -1.652 | 887.1 | 866.765 | 0.1803 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.84 |  | 192.8751 | -2.6106 | 201.61 | 194.19 | 1.496 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 397.05 |  | 404.0868 | -1.7414 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.3 |  | 46.1392 | -1.8189 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.01 |  | 25.5774 | -2.2184 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.76 |  | 752.8161 | -0.1403 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.46 |  | 296.517 | -0.3565 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.99 |  | 126.8568 | -0.6833 | 131.36 | 126.665 | 3.9686 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.4 |  | 73.6278 | -1.6676 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 289.645 |  | 295.5094 | -1.9845 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 392.215 |  | 400.6639 | -2.1087 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.755 |  | 632.7002 | -0.9397 | 640.25 | 631.005 | 4.5696 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1020.99 |  | 1032.2563 | -1.0914 | 1035.07 | 1021.09 | 4.5789 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.53 |  | 474.3655 | -0.1761 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 139.96 |  | 140.6047 | -0.4585 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.49 |  | 166.32 | 0.1022 | 169.91 | 165.6 | 4.9553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.385 |  | 282.9954 | -2.3359 | 288.48 | 280.67 | 0.4088 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.61 |  | 713.0898 | -1.6099 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 390.88 |  | 397.3289 | -1.6231 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.51 |  | 102.5516 | -3.9411 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.45 |  | 325.6055 | -2.8118 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1804.34 |  | 1824.292 | -1.0937 | 1823.13 | 1796.26 | 0.1635 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.42 |  | 574.0263 | -1.3251 | 572.69 | 562.32 | 1.4936 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.385 |  | 325.8761 | -1.685 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.35 |  | 222.1871 | -1.727 | 222.19 | 218.09 | 0.1695 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.99 |  | 328.3242 | -1.9292 | 332.49 | 326.685 | 4.3542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 284.8 |  | 290.1473 | -1.843 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.14 |  | 64.4894 | -2.0925 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.88 |  | 52.3223 | -0.8454 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.785 |  | 135.4542 | -1.2323 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 334.44 |  | 339.7597 | -1.5657 | 346.26 | 338 | 3.7346 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.12 |  | 514.7689 | 0.2625 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.41 |  | 294.6849 | 0.5854 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.28 |  | 27.1686 | -3.2706 | 28.05 | 27.6 | 0.1522 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.91 |  | 35.8183 | -2.5359 | 37.365 | 36.4 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.94 |  | 21.4626 | -2.4349 | 22.18 | 21.78 | 0.1433 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1431.47 |  | 1479.5744 | -3.2512 | 1549.47 | 1482.06 | 0.9221 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 464.01 |  | 480.144 | -3.3602 | 498.04 | 480.14 | 0.8211 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 755.26 |  | 770.6379 | -1.9955 | 797.155 | 768.7 | 4.0079 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.59 |  | 255.387 | 0.0795 | 258.07 | 252.62 | 0.0391 | watch_only | none |
| META | cloud_ai_capex | 668.89 |  | 674.4295 | -0.8214 | 680.09 | 667.1 | 1.1885 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 253.37 |  | 258.1332 | -1.8453 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.13 |  | 163.4714 | -2.044 | 168.11 | 162.41 | 1.1178 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
