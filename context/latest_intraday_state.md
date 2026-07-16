# Intraday State

- Generated at: `2026-07-17T00:44:09+08:00`
- Market time ET: `2026-07-16T12:44:10-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 36, 'manual_confirm_candidate': 2, 'spread_too_wide_or_missing': 2, 'below_vwap': 14, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.7 |  | 710.1095 | -0.3393 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.33 |  | 536.3714 | -1.1264 | 543.4 | 535.47 | 0.0641 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.24 |  | 574.476 | -0.9114 | 580.31 | 572.21 | 0.0703 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.84 |  | 752.7729 | -0.1239 | 753.51 | 751.13 | 0.0106 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.86 |  | 514.8628 | 0.1937 | 515.825 | 512.23 | 0.0911 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.39 |  | 396.9091 | 1.1289 | 398.69 | 392.2 | 0.2167 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.86 |  | 514.8628 | 0.1937 | 515.825 | 512.23 | 0.0911 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.66 |  | 255.4017 | 0.1011 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 401.39 |  | 396.9091 | 1.1289 | 398.69 | 392.2 | 0.2167 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 329.95 |  | 329.9184 | 0.0096 | 328.98 | 326.885 | 0.5728 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 296.415 |  | 294.7573 | 0.5624 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TT | data_center_power_cooling | 472.85 |  | 474.0096 | -0.2446 | 474.085 | 467.64 | 0.1438 | below_vwap | below_vwap |
| 7 | JCI | data_center_power_cooling | 140 |  | 140.544 | -0.3871 | 140.83 | 139.43 | 0.0857 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1809.52 |  | 1823.3234 | -0.757 | 1823.13 | 1796.26 | 0.0879 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 751.84 |  | 752.7729 | -0.1239 | 753.51 | 751.13 | 0.0106 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.88 |  | 296.441 | -0.1892 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.285 |  | 371.8853 | -0.1614 | 375.18 | 369.2 | 0.0754 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1021.51 |  | 1030.2064 | -0.8441 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ANET | ai_networking_optical | 166.215 |  | 166.3215 | -0.064 | 169.91 | 165.6 | 0.3911 | below_vwap | below_vwap,spread_too_wide |
| 15 | AVGO | custom_silicon_networking | 380.3 |  | 381.6476 | -0.3531 | 386.58 | 378.53 | 1.341 | below_vwap | below_vwap,spread_too_wide |
| 16 | AMAT | semiconductor_equipment | 566.83 |  | 573.6036 | -1.1809 | 572.69 | 562.32 | 2.4999 | below_vwap | below_vwap,spread_too_wide |
| 17 | KLAC | semiconductor_equipment | 219.66 |  | 221.869 | -0.9956 | 222.19 | 218.09 | 0.8741 | below_vwap | below_vwap,spread_too_wide |
| 18 | ENTG | semiconductor_materials | 134.16 |  | 135.2551 | -0.8097 | 138.07 | 133.73 | 3.2126 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 668.445 |  | 673.8011 | -0.7949 | 680.09 | 667.1 | 1.1145 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 530.33 |  | 536.3714 | -1.1264 | 543.4 | 535.47 | 0.0641 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.86 |  | 514.8628 | 0.1937 | 515.825 | 512.23 | 0.0911 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.39 |  | 396.9091 | 1.1289 | 398.69 | 392.2 | 0.2167 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.415 |  | 294.7573 | 0.5624 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | AAPL | mega_cap_platform | 329.95 |  | 329.9184 | 0.0096 | 328.98 | 326.885 | 0.5728 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AMZN | cloud_ai_capex | 255.66 |  | 255.4017 | 0.1011 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 6 | ANET | ai_networking_optical | 166.215 |  | 166.3215 | -0.064 | 169.91 | 165.6 | 0.3911 | below_vwap | below_vwap,spread_too_wide |
| 7 | AVGO | custom_silicon_networking | 380.3 |  | 381.6476 | -0.3531 | 386.58 | 378.53 | 1.341 | below_vwap | below_vwap,spread_too_wide |
| 8 | TT | data_center_power_cooling | 472.85 |  | 474.0096 | -0.2446 | 474.085 | 467.64 | 0.1438 | below_vwap | below_vwap |
| 9 | JCI | data_center_power_cooling | 140 |  | 140.544 | -0.3871 | 140.83 | 139.43 | 0.0857 | below_vwap | below_vwap |
| 10 | GEV | data_center_power_cooling | 1021.51 |  | 1030.2064 | -0.8441 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ASML | semiconductor_equipment | 1809.52 |  | 1823.3234 | -0.757 | 1823.13 | 1796.26 | 0.0879 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 566.83 |  | 573.6036 | -1.1809 | 572.69 | 562.32 | 2.4999 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 219.66 |  | 221.869 | -0.9956 | 222.19 | 218.09 | 0.8741 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 751.84 |  | 752.7729 | -0.1239 | 753.51 | 751.13 | 0.0106 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.88 |  | 296.441 | -0.1892 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 134.16 |  | 135.2551 | -0.8097 | 138.07 | 133.73 | 3.2126 | below_vwap | below_vwap,spread_too_wide |
| 18 | GOOGL | cloud_ai_capex | 371.285 |  | 371.8853 | -0.1614 | 375.18 | 369.2 | 0.0754 | below_vwap | below_vwap |
| 19 | META | cloud_ai_capex | 668.445 |  | 673.8011 | -0.7949 | 680.09 | 667.1 | 1.1145 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 530.33 |  | 536.3714 | -1.1264 | 543.4 | 535.47 | 0.0641 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.7 |  | 710.1095 | -0.3393 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.28 |  | 72.0731 | -1.1003 | 73.09 | 71.45 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.17 |  | 207.5498 | -0.183 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.39 |  | 396.9091 | 1.1289 | 398.69 | 392.2 | 0.2167 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 329.95 |  | 329.9184 | 0.0096 | 328.98 | 326.885 | 0.5728 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 371.285 |  | 371.8853 | -0.1614 | 375.18 | 369.2 | 0.0754 | below_vwap | below_vwap |
| AMD | ai_accelerator | 500.87 |  | 507.9267 | -1.3893 | 518.33 | 507.62 | 0.6748 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.42 |  | 410.6036 | -1.0189 | 414.385 | 406.61 | 0.342 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.33 |  | 536.3714 | -1.1264 | 543.4 | 535.47 | 0.0641 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.24 |  | 574.476 | -0.9114 | 580.31 | 572.21 | 0.0703 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.3 |  | 381.6476 | -0.3531 | 386.58 | 378.53 | 1.341 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.6 |  | 861.4699 | -1.494 | 887.1 | 866.765 | 0.2357 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.61 |  | 192.5109 | -2.0263 | 201.61 | 194.19 | 0.7688 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.38 |  | 403.6193 | -1.0503 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.32 |  | 46.084 | -1.6578 | 47.65 | 46.165 | 0.0441 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.03 |  | 25.5346 | -1.9763 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.84 |  | 752.7729 | -0.1239 | 753.51 | 751.13 | 0.0106 | below_vwap | below_vwap |
| IWM | market_regime | 295.88 |  | 296.441 | -0.1892 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.53 |  | 126.7717 | -0.1907 | 131.36 | 126.665 | 0.4584 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.93 |  | 73.5321 | -0.8189 | 75.54 | 73.985 | 2.2762 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 290.19 |  | 295.0977 | -1.6631 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 391.795 |  | 400.347 | -2.1361 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.92 |  | 632.4845 | -0.8798 | 640.25 | 631.005 | 4.6673 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1021.51 |  | 1030.2064 | -0.8441 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 472.85 |  | 474.0096 | -0.2446 | 474.085 | 467.64 | 0.1438 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 140 |  | 140.544 | -0.3871 | 140.83 | 139.43 | 0.0857 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 166.215 |  | 166.3215 | -0.064 | 169.91 | 165.6 | 0.3911 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 277 |  | 282.4708 | -1.9368 | 288.48 | 280.67 | 1.7617 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.59 |  | 712.4226 | -1.6609 | 737.175 | 720.21 | 3.0203 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 391.96 |  | 396.7767 | -1.214 | 410 | 397.68 | 4.5719 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 99.09 |  | 102.3698 | -3.2039 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.76 |  | 325.037 | -1.9312 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1809.52 |  | 1823.3234 | -0.757 | 1823.13 | 1796.26 | 0.0879 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.83 |  | 573.6036 | -1.1809 | 572.69 | 562.32 | 2.4999 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.52 |  | 325.4631 | -1.5188 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.66 |  | 221.869 | -0.9956 | 222.19 | 218.09 | 0.8741 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.905 |  | 327.8318 | -1.5028 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.82 |  | 289.7452 | -1.6998 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.025 |  | 64.4159 | -2.1592 | 66.19 | 63.93 | 0.2221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 51.685 |  | 52.3066 | -1.1884 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.16 |  | 135.2551 | -0.8097 | 138.07 | 133.73 | 3.2126 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 335.4 |  | 339.0211 | -1.0681 | 346.26 | 338 | 3.9207 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.86 |  | 514.8628 | 0.1937 | 515.825 | 512.23 | 0.0911 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.415 |  | 294.7573 | 0.5624 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.33 |  | 27.1026 | -2.8506 | 28.05 | 27.6 | 0.076 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.91 |  | 35.7663 | -2.394 | 37.365 | 36.4 | 0.0859 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.865 |  | 21.4127 | -2.558 | 22.18 | 21.78 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1434.09 |  | 1477.2506 | -2.9217 | 1549.47 | 1482.06 | 3.8352 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 458.12 |  | 478.4025 | -4.2396 | 498.04 | 480.14 | 1.0019 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 754.49 |  | 769.5317 | -1.9547 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.66 |  | 255.4017 | 0.1011 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 668.445 |  | 673.8011 | -0.7949 | 680.09 | 667.1 | 1.1145 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 253.89 |  | 257.8636 | -1.541 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.035 |  | 163.4039 | -2.0617 | 168.11 | 162.41 | 2.8056 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
