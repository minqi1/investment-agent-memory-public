# Intraday State

- Generated at: `2026-07-17T01:11:55+08:00`
- Market time ET: `2026-07-16T13:11:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 14, 'watch_only': 2, 'manual_confirm_candidate': 3, 'below_opening_15m_low': 31, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.55 |  | 709.903 | -0.1906 | 713.55 | 708.25 | 0.0282 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 530.535 |  | 536.0098 | -1.0214 | 543.4 | 535.47 | 0.0584 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.585 |  | 573.5494 | -0.6912 | 580.31 | 572.21 | 0.0298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.71 |  | 752.7404 | -0.004 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.96 |  | 514.9146 | 0.203 | 515.825 | 512.23 | 0.0756 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.725 |  | 397.7775 | 0.9924 | 398.69 | 392.2 | 0.2937 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.905 |  | 330.0751 | 0.5544 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.96 |  | 514.9146 | 0.203 | 515.825 | 512.23 | 0.0756 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 207.54 |  | 207.5065 | 0.0161 | 211.03 | 207.49 | 0.0819 | watch_only | none |
| 3 | AMZN | cloud_ai_capex | 255.935 |  | 255.4615 | 0.1853 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 331.905 |  | 330.0751 | 0.5544 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 140.94 |  | 140.5318 | 0.2904 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MSFT | cloud_ai_capex | 401.725 |  | 397.7775 | 0.9924 | 398.69 | 392.2 | 0.2937 | buy_precheck_manual_confirm | none |
| 7 | APD | industrial_gases | 296.3 |  | 294.8381 | 0.4958 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ANET | ai_networking_optical | 167.635 |  | 166.4123 | 0.7347 | 169.91 | 165.6 | 0.4593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TT | data_center_power_cooling | 475.96 |  | 474.1671 | 0.3781 | 474.085 | 467.64 | 4.5571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | TSM | foundry | 406.76 |  | 410.2047 | -0.8398 | 414.385 | 406.61 | 0.1205 | below_vwap | below_vwap |
| 11 | QQQ | market_regime | 708.55 |  | 709.903 | -0.1906 | 713.55 | 708.25 | 0.0282 | below_vwap | below_vwap |
| 12 | GEV | data_center_power_cooling | 1025.9 |  | 1029.2042 | -0.321 | 1035.07 | 1021.09 | 0.1335 | below_vwap | below_vwap |
| 13 | KLAC | semiconductor_equipment | 219.985 |  | 221.5794 | -0.7195 | 222.19 | 218.09 | 0.0818 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 752.71 |  | 752.7404 | -0.004 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 296.16 |  | 296.4013 | -0.0814 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 16 | GOOGL | cloud_ai_capex | 371.08 |  | 371.8722 | -0.213 | 375.18 | 369.2 | 0.0512 | below_vwap | below_vwap |
| 17 | META | cloud_ai_capex | 669.23 |  | 673.1465 | -0.5818 | 680.09 | 667.1 | 0.0628 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ASML | semiconductor_equipment | 1808.25 |  | 1822.1543 | -0.7631 | 1823.13 | 1796.26 | 0.428 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 567.07 |  | 572.766 | -0.9945 | 572.69 | 562.32 | 2.714 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.96 |  | 514.9146 | 0.203 | 515.825 | 512.23 | 0.0756 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.725 |  | 397.7775 | 0.9924 | 398.69 | 392.2 | 0.2937 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 331.905 |  | 330.0751 | 0.5544 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.96 |  | 474.1671 | 0.3781 | 474.085 | 467.64 | 4.5571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | JCI | data_center_power_cooling | 140.94 |  | 140.5318 | 0.2904 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.3 |  | 294.8381 | 0.4958 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | NVDA | ai_accelerator | 207.54 |  | 207.5065 | 0.0161 | 211.03 | 207.49 | 0.0819 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 255.935 |  | 255.4615 | 0.1853 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 9 | TSM | foundry | 406.76 |  | 410.2047 | -0.8398 | 414.385 | 406.61 | 0.1205 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 708.55 |  | 709.903 | -0.1906 | 713.55 | 708.25 | 0.0282 | below_vwap | below_vwap |
| 11 | GEV | data_center_power_cooling | 1025.9 |  | 1029.2042 | -0.321 | 1035.07 | 1021.09 | 0.1335 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1808.25 |  | 1822.1543 | -0.7631 | 1823.13 | 1796.26 | 0.428 | below_vwap | below_vwap,spread_too_wide |
| 13 | AMAT | semiconductor_equipment | 567.07 |  | 572.766 | -0.9945 | 572.69 | 562.32 | 2.714 | below_vwap | below_vwap,spread_too_wide |
| 14 | KLAC | semiconductor_equipment | 219.985 |  | 221.5794 | -0.7195 | 222.19 | 218.09 | 0.0818 | below_vwap | below_vwap |
| 15 | SPY | market_regime | 752.71 |  | 752.7404 | -0.004 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 16 | IWM | market_regime | 296.16 |  | 296.4013 | -0.0814 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | DELL | ai_server_oem | 400.97 |  | 403.3197 | -0.5826 | 411.65 | 400.635 | 4.1824 | below_vwap | below_vwap,spread_too_wide |
| 19 | ENTG | semiconductor_materials | 134.585 |  | 135.1483 | -0.4168 | 138.07 | 133.73 | 0.4681 | below_vwap | below_vwap,spread_too_wide |
| 20 | GOOGL | cloud_ai_capex | 371.08 |  | 371.8722 | -0.213 | 375.18 | 369.2 | 0.0512 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.55 |  | 709.903 | -0.1906 | 713.55 | 708.25 | 0.0282 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.53 |  | 72.025 | -0.6873 | 73.09 | 71.45 | 0.028 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.54 |  | 207.5065 | 0.0161 | 211.03 | 207.49 | 0.0819 | watch_only | none |
| MSFT | cloud_ai_capex | 401.725 |  | 397.7775 | 0.9924 | 398.69 | 392.2 | 0.2937 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.905 |  | 330.0751 | 0.5544 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.08 |  | 371.8722 | -0.213 | 375.18 | 369.2 | 0.0512 | below_vwap | below_vwap |
| AMD | ai_accelerator | 501.02 |  | 507.0026 | -1.18 | 518.33 | 507.62 | 0.6307 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.76 |  | 410.2047 | -0.8398 | 414.385 | 406.61 | 0.1205 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.535 |  | 536.0098 | -1.0214 | 543.4 | 535.47 | 0.0584 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.585 |  | 573.5494 | -0.6912 | 580.31 | 572.21 | 0.0298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.92 |  | 381.1275 | -0.8416 | 386.58 | 378.53 | 1.0849 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 851.19 |  | 860.0376 | -1.0287 | 887.1 | 866.765 | 0.3313 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.9 |  | 192.2312 | -1.7329 | 201.61 | 194.19 | 1.1699 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.97 |  | 403.3197 | -0.5826 | 411.65 | 400.635 | 4.1824 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.37 |  | 46.0057 | -1.3817 | 47.65 | 46.165 | 0.0441 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.005 |  | 25.484 | -1.8795 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.71 |  | 752.7404 | -0.004 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 296.16 |  | 296.4013 | -0.0814 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.585 |  | 126.7572 | -0.1358 | 131.36 | 126.665 | 0.0474 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.3 |  | 73.5109 | -0.2869 | 75.54 | 73.985 | 0.0955 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 291.73 |  | 294.7776 | -1.0339 | 300.385 | 293.64 | 2.4372 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 397.085 |  | 399.9907 | -0.7264 | 406.24 | 399.495 | 5.0266 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 629.055 |  | 632.1433 | -0.4885 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1025.9 |  | 1029.2042 | -0.321 | 1035.07 | 1021.09 | 0.1335 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 475.96 |  | 474.1671 | 0.3781 | 474.085 | 467.64 | 4.5571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.94 |  | 140.5318 | 0.2904 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.635 |  | 166.4123 | 0.7347 | 169.91 | 165.6 | 0.4593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.15 |  | 281.9433 | -1.3454 | 288.48 | 280.67 | 1.8947 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.34 |  | 711.0042 | -1.4999 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 391.575 |  | 396.3417 | -1.2027 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.31 |  | 102.0844 | -2.7177 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.07 |  | 324.4002 | -2.2596 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1808.25 |  | 1822.1543 | -0.7631 | 1823.13 | 1796.26 | 0.428 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 567.07 |  | 572.766 | -0.9945 | 572.69 | 562.32 | 2.714 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.86 |  | 324.9414 | -1.256 | 328.96 | 324.11 | 4.2199 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 219.985 |  | 221.5794 | -0.7195 | 222.19 | 218.09 | 0.0818 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 325.345 |  | 327.5339 | -0.6683 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.82 |  | 289.1959 | -1.5131 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.21 |  | 64.3364 | -1.7507 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.58 |  | 52.2943 | -1.366 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.585 |  | 135.1483 | -0.4168 | 138.07 | 133.73 | 0.4681 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 335.645 |  | 338.7585 | -0.9191 | 346.26 | 338 | 3.7182 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| LIN | industrial_gases | 515.96 |  | 514.9146 | 0.203 | 515.825 | 512.23 | 0.0756 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.3 |  | 294.8381 | 0.4958 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.25 |  | 27.0189 | -2.8457 | 28.05 | 27.6 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.9 |  | 35.706 | -2.2573 | 37.365 | 36.4 | 0.0287 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.925 |  | 21.3365 | -1.9286 | 22.18 | 21.78 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1446.21 |  | 1474.8735 | -1.9435 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 460.79 |  | 477.1556 | -3.4298 | 498.04 | 480.14 | 0.434 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 753.56 |  | 769.0304 | -2.0117 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.935 |  | 255.4615 | 0.1853 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 669.23 |  | 673.1465 | -0.5818 | 680.09 | 667.1 | 0.0628 | below_vwap | below_vwap |
| ARM | ai_accelerator | 255.6 |  | 257.4851 | -0.7321 | 265.96 | 258.1 | 3.9124 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 158.42 |  | 163.1692 | -2.9106 | 168.11 | 162.41 | 0.8964 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
