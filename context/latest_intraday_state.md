# Intraday State

- Generated at: `2026-07-17T01:19:55+08:00`
- Market time ET: `2026-07-16T13:19:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 35, 'manual_confirm_candidate': 2, 'below_vwap': 12, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.64 |  | 709.8883 | -0.3167 | 713.55 | 708.25 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.37 |  | 535.9777 | -1.4194 | 543.4 | 535.47 | 0.0643 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.6 |  | 573.4422 | -1.0188 | 580.31 | 572.21 | 0.0352 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.31 |  | 752.7323 | -0.0561 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.12 |  | 397.8639 | 1.0697 | 398.69 | 392.2 | 0.1194 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.24 |  | 330.1034 | 0.6472 | 328.98 | 326.885 | 0.015 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.24 |  | 330.1034 | 0.6472 | 328.98 | 326.885 | 0.015 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 167.715 |  | 166.4324 | 0.7706 | 169.91 | 165.6 | 0.155 | watch_only | none |
| 3 | AMZN | cloud_ai_capex | 256.52 |  | 255.4927 | 0.4021 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 4 | JCI | data_center_power_cooling | 140.94 |  | 140.5415 | 0.2835 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 402.12 |  | 397.8639 | 1.0697 | 398.69 | 392.2 | 0.1194 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 475.895 |  | 474.2578 | 0.3452 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | APD | industrial_gases | 295.41 |  | 294.8575 | 0.1874 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | LIN | industrial_gases | 515.555 |  | 514.9221 | 0.1229 | 515.825 | 512.23 | 0.5819 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1800.35 |  | 1821.8084 | -1.1779 | 1823.13 | 1796.26 | 0.0811 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 752.31 |  | 752.7323 | -0.0561 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.8 |  | 296.3838 | -0.197 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 631.15 |  | 632.0502 | -0.1424 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1023.52 |  | 1029.1195 | -0.5441 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | META | cloud_ai_capex | 669.81 |  | 672.9855 | -0.4719 | 680.09 | 667.1 | 0.3479 | below_vwap | below_vwap |
| 16 | ENTG | semiconductor_materials | 134.3 |  | 135.1418 | -0.6229 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | AMAT | semiconductor_equipment | 564.53 |  | 572.6278 | -1.4142 | 572.69 | 562.32 | 2.0034 | below_vwap | below_vwap,spread_too_wide |
| 18 | KLAC | semiconductor_equipment | 218.66 |  | 221.5225 | -1.2922 | 222.19 | 218.09 | 0.4207 | below_vwap | below_vwap,spread_too_wide |
| 19 | DELL | ai_server_oem | 401.16 |  | 403.2708 | -0.5234 | 411.65 | 400.635 | 4.143 | below_vwap | below_vwap,spread_too_wide |
| 20 | GOOGL | cloud_ai_capex | 371.345 |  | 371.8606 | -0.1387 | 375.18 | 369.2 | 0.377 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.12 |  | 397.8639 | 1.0697 | 398.69 | 392.2 | 0.1194 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.24 |  | 330.1034 | 0.6472 | 328.98 | 326.885 | 0.015 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.895 |  | 474.2578 | 0.3452 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | JCI | data_center_power_cooling | 140.94 |  | 140.5415 | 0.2835 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.41 |  | 294.8575 | 0.1874 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 167.715 |  | 166.4324 | 0.7706 | 169.91 | 165.6 | 0.155 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 256.52 |  | 255.4927 | 0.4021 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 8 | PWR | data_center_power_cooling | 631.15 |  | 632.0502 | -0.1424 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | GEV | data_center_power_cooling | 1023.52 |  | 1029.1195 | -0.5441 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ASML | semiconductor_equipment | 1800.35 |  | 1821.8084 | -1.1779 | 1823.13 | 1796.26 | 0.0811 | below_vwap | below_vwap |
| 11 | AMAT | semiconductor_equipment | 564.53 |  | 572.6278 | -1.4142 | 572.69 | 562.32 | 2.0034 | below_vwap | below_vwap,spread_too_wide |
| 12 | KLAC | semiconductor_equipment | 218.66 |  | 221.5225 | -1.2922 | 222.19 | 218.09 | 0.4207 | below_vwap | below_vwap,spread_too_wide |
| 13 | SPY | market_regime | 752.31 |  | 752.7323 | -0.0561 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 14 | IWM | market_regime | 295.8 |  | 296.3838 | -0.197 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | DELL | ai_server_oem | 401.16 |  | 403.2708 | -0.5234 | 411.65 | 400.635 | 4.143 | below_vwap | below_vwap,spread_too_wide |
| 17 | ENTG | semiconductor_materials | 134.3 |  | 135.1418 | -0.6229 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | GOOGL | cloud_ai_capex | 371.345 |  | 371.8606 | -0.1387 | 375.18 | 369.2 | 0.377 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 669.81 |  | 672.9855 | -0.4719 | 680.09 | 667.1 | 0.3479 | below_vwap | below_vwap |
| 20 | LIN | industrial_gases | 515.555 |  | 514.9221 | 0.1229 | 515.825 | 512.23 | 0.5819 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.64 |  | 709.8883 | -0.3167 | 713.55 | 708.25 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.29 |  | 72.0174 | -1.0101 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.07 |  | 207.4974 | -0.206 | 211.03 | 207.49 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.12 |  | 397.8639 | 1.0697 | 398.69 | 392.2 | 0.1194 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.24 |  | 330.1034 | 0.6472 | 328.98 | 326.885 | 0.015 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.345 |  | 371.8606 | -0.1387 | 375.18 | 369.2 | 0.377 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496.885 |  | 506.8255 | -1.9613 | 518.33 | 507.62 | 0.32 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 405.35 |  | 410.1061 | -1.1597 | 414.385 | 406.61 | 0.0617 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.37 |  | 535.9777 | -1.4194 | 543.4 | 535.47 | 0.0643 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.6 |  | 573.4422 | -1.0188 | 580.31 | 572.21 | 0.0352 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.655 |  | 381.0191 | -0.8829 | 386.58 | 378.53 | 1.5888 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 844.97 |  | 859.4644 | -1.6864 | 887.1 | 866.765 | 0.071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.59 |  | 192.1733 | -2.385 | 201.61 | 194.19 | 0.4904 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.16 |  | 403.2708 | -0.5234 | 411.65 | 400.635 | 4.143 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.45 |  | 45.9943 | -1.1834 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.045 |  | 25.4642 | -1.6461 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.31 |  | 752.7323 | -0.0561 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.8 |  | 296.3838 | -0.197 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.535 |  | 126.7494 | -0.1691 | 131.36 | 126.665 | 0.0158 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.045 |  | 73.5016 | -0.6213 | 75.54 | 73.985 | 4.682 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 292.6 |  | 294.6735 | -0.7037 | 300.385 | 293.64 | 2.6008 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.655 |  | 399.9489 | -0.8236 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 631.15 |  | 632.0502 | -0.1424 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1023.52 |  | 1029.1195 | -0.5441 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 475.895 |  | 474.2578 | 0.3452 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.94 |  | 140.5415 | 0.2835 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.715 |  | 166.4324 | 0.7706 | 169.91 | 165.6 | 0.155 | watch_only | none |
| COHR | ai_networking_optical | 277.51 |  | 281.8731 | -1.5479 | 288.48 | 280.67 | 2.4792 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 699.04 |  | 710.761 | -1.6491 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 391.23 |  | 396.1916 | -1.2523 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.66 |  | 102.0284 | -3.3015 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.48 |  | 324.3365 | -2.4223 | 337.59 | 326.16 | 4.7681 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1800.35 |  | 1821.8084 | -1.1779 | 1823.13 | 1796.26 | 0.0811 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.53 |  | 572.6278 | -1.4142 | 572.69 | 562.32 | 2.0034 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.41 |  | 324.8259 | -1.6673 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.66 |  | 221.5225 | -1.2922 | 222.19 | 218.09 | 0.4207 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 323.895 |  | 327.4697 | -1.0916 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 283.67 |  | 289.1653 | -1.9004 | 295.83 | 285.02 | 0.3525 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.855 |  | 64.3102 | -2.2629 | 66.19 | 63.93 | 2.5455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.415 |  | 52.2393 | -1.578 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.3 |  | 135.1418 | -0.6229 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 333.93 |  | 338.5471 | -1.3638 | 346.26 | 338 | 3.6235 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.555 |  | 514.9221 | 0.1229 | 515.825 | 512.23 | 0.5819 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.41 |  | 294.8575 | 0.1874 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.06 |  | 27.0012 | -3.4857 | 28.05 | 27.6 | 0.0767 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.715 |  | 35.6839 | -2.7152 | 37.365 | 36.4 | 0.0576 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.86 |  | 21.3273 | -2.1912 | 22.18 | 21.78 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1425.71 |  | 1473.5763 | -3.2483 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 458.595 |  | 476.9629 | -3.851 | 498.04 | 480.14 | 0.9747 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 751.34 |  | 768.7868 | -2.2694 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 256.52 |  | 255.4927 | 0.4021 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| META | cloud_ai_capex | 669.81 |  | 672.9855 | -0.4719 | 680.09 | 667.1 | 0.3479 | below_vwap | below_vwap |
| ARM | ai_accelerator | 255.345 |  | 257.4435 | -0.8151 | 265.96 | 258.1 | 2.056 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 157.48 |  | 163.1004 | -3.446 | 168.11 | 162.41 | 2.4956 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
