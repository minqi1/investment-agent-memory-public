# Intraday State

- Generated at: `2026-07-17T00:32:16+08:00`
- Market time ET: `2026-07-16T12:32:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'watch_only': 1, 'manual_confirm_candidate': 2, 'below_opening_15m_low': 30, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.56 |  | 710.1772 | -0.2277 | 713.55 | 708.25 | 0.0183 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 530.94 |  | 536.5866 | -1.0523 | 543.4 | 535.47 | 0.064 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.65 |  | 574.6302 | -0.8667 | 580.31 | 572.21 | 0.079 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.3 |  | 752.7974 | -0.0661 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.27 |  | 396.7018 | 1.1516 | 398.69 | 392.2 | 0.0349 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.23 |  | 329.8938 | 0.405 | 328.98 | 326.885 | 0.0362 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 207.62 |  | 207.5531 | 0.0322 | 211.03 | 207.49 | 0.0578 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 331.23 |  | 329.8938 | 0.405 | 328.98 | 326.885 | 0.0362 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 401.27 |  | 396.7018 | 1.1516 | 398.69 | 392.2 | 0.0349 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 515.1 |  | 514.7863 | 0.0609 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 166.69 |  | 166.3221 | 0.2212 | 169.91 | 165.6 | 3.4675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.185 |  | 294.7171 | 0.4981 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | QQQ | market_regime | 708.56 |  | 710.1772 | -0.2277 | 713.55 | 708.25 | 0.0183 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1807.8 |  | 1823.889 | -0.8821 | 1823.13 | 1796.26 | 0.0868 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 752.3 |  | 752.7974 | -0.0661 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 296.08 |  | 296.4752 | -0.1333 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.71 |  | 371.898 | -0.0505 | 375.18 | 369.2 | 0.0511 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 255.39 |  | 255.3958 | -0.0023 | 258.07 | 252.62 | 0.0274 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 218.78 |  | 221.9521 | -1.4292 | 222.19 | 218.09 | 0.1737 | below_vwap | below_vwap |
| 15 | TT | data_center_power_cooling | 473.48 |  | 474.3165 | -0.1764 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 285.09 |  | 289.8986 | -1.6587 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | DELL | ai_server_oem | 401.63 |  | 403.8452 | -0.5485 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 134.11 |  | 135.3976 | -0.951 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHU | semiconductor_test_packaging | 51.75 |  | 52.3092 | -1.0689 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | TSM | foundry | 406.64 |  | 410.7068 | -0.9902 | 414.385 | 406.61 | 0.4476 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.27 |  | 396.7018 | 1.1516 | 398.69 | 392.2 | 0.0349 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.23 |  | 329.8938 | 0.405 | 328.98 | 326.885 | 0.0362 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.185 |  | 294.7171 | 0.4981 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | NVDA | ai_accelerator | 207.62 |  | 207.5531 | 0.0322 | 211.03 | 207.49 | 0.0578 | watch_only | none |
| 5 | TSM | foundry | 406.64 |  | 410.7068 | -0.9902 | 414.385 | 406.61 | 0.4476 | below_vwap | below_vwap,spread_too_wide |
| 6 | QQQ | market_regime | 708.56 |  | 710.1772 | -0.2277 | 713.55 | 708.25 | 0.0183 | below_vwap | below_vwap |
| 7 | AVGO | custom_silicon_networking | 380.69 |  | 381.6654 | -0.2556 | 386.58 | 378.53 | 0.6462 | below_vwap | below_vwap,spread_too_wide |
| 8 | TT | data_center_power_cooling | 473.48 |  | 474.3165 | -0.1764 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 139.625 |  | 140.5806 | -0.6798 | 140.83 | 139.43 | 4.8559 | below_vwap | below_vwap,spread_too_wide |
| 10 | ASML | semiconductor_equipment | 1807.8 |  | 1823.889 | -0.8821 | 1823.13 | 1796.26 | 0.0868 | below_vwap | below_vwap |
| 11 | AMAT | semiconductor_equipment | 567.155 |  | 573.8079 | -1.1594 | 572.69 | 562.32 | 2.1105 | below_vwap | below_vwap,spread_too_wide |
| 12 | ONTO | semiconductor_test_packaging | 285.09 |  | 289.8986 | -1.6587 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 218.78 |  | 221.9521 | -1.4292 | 222.19 | 218.09 | 0.1737 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 752.3 |  | 752.7974 | -0.0661 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 296.08 |  | 296.4752 | -0.1333 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | DELL | ai_server_oem | 401.63 |  | 403.8452 | -0.5485 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 134.11 |  | 135.3976 | -0.951 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 371.71 |  | 371.898 | -0.0505 | 375.18 | 369.2 | 0.0511 | below_vwap | below_vwap |
| 20 | COHU | semiconductor_test_packaging | 51.75 |  | 52.3092 | -1.0689 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.56 |  | 710.1772 | -0.2277 | 713.55 | 708.25 | 0.0183 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.52 |  | 72.1015 | -0.8065 | 73.09 | 71.45 | 0.028 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.62 |  | 207.5531 | 0.0322 | 211.03 | 207.49 | 0.0578 | watch_only | none |
| MSFT | cloud_ai_capex | 401.27 |  | 396.7018 | 1.1516 | 398.69 | 392.2 | 0.0349 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.23 |  | 329.8938 | 0.405 | 328.98 | 326.885 | 0.0362 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.71 |  | 371.898 | -0.0505 | 375.18 | 369.2 | 0.0511 | below_vwap | below_vwap |
| AMD | ai_accelerator | 500.97 |  | 508.4328 | -1.4678 | 518.33 | 507.62 | 2.7646 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.64 |  | 410.7068 | -0.9902 | 414.385 | 406.61 | 0.4476 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.94 |  | 536.5866 | -1.0523 | 543.4 | 535.47 | 0.064 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.65 |  | 574.6302 | -0.8667 | 580.31 | 572.21 | 0.079 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.69 |  | 381.6654 | -0.2556 | 386.58 | 378.53 | 0.6462 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 852.53 |  | 861.9981 | -1.0984 | 887.1 | 866.765 | 0.3707 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.715 |  | 192.6523 | -2.0437 | 201.61 | 194.19 | 0.7048 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.63 |  | 403.8452 | -0.5485 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.49 |  | 46.1075 | -1.3392 | 47.65 | 46.165 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.075 |  | 25.5522 | -1.8675 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.3 |  | 752.7974 | -0.0661 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 296.08 |  | 296.4752 | -0.1333 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.435 |  | 126.7881 | -0.2785 | 131.36 | 126.665 | 0.4192 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.86 |  | 73.5725 | -0.9685 | 75.54 | 73.985 | 4.9684 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 290.07 |  | 295.3023 | -1.7719 | 300.385 | 293.64 | 1.8754 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 392.03 |  | 400.5073 | -2.1166 | 406.24 | 399.495 | 2.0534 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 627.87 |  | 632.6027 | -0.7481 | 640.25 | 631.005 | 4.7812 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1017.995 |  | 1030.8239 | -1.2445 | 1035.07 | 1021.09 | 4.9922 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.48 |  | 474.3165 | -0.1764 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 139.625 |  | 140.5806 | -0.6798 | 140.83 | 139.43 | 4.8559 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 166.69 |  | 166.3221 | 0.2212 | 169.91 | 165.6 | 3.4675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.06 |  | 282.7098 | -1.6447 | 288.48 | 280.67 | 1.8881 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 702.14 |  | 712.821 | -1.4984 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 391.78 |  | 396.9673 | -1.3067 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.31 |  | 102.4571 | -3.0716 | 106.975 | 102.85 | 0.9365 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 317.77 |  | 325.4429 | -2.3577 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1807.8 |  | 1823.889 | -0.8821 | 1823.13 | 1796.26 | 0.0868 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 567.155 |  | 573.8079 | -1.1594 | 572.69 | 562.32 | 2.1105 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.42 |  | 325.6082 | -1.5934 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.78 |  | 221.9521 | -1.4292 | 222.19 | 218.09 | 0.1737 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.655 |  | 328.0438 | -1.6427 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 285.09 |  | 289.8986 | -1.6587 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.18 |  | 64.4612 | -1.9876 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.75 |  | 52.3092 | -1.0689 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.11 |  | 135.3976 | -0.951 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.245 |  | 339.2397 | -1.1775 | 346.26 | 338 | 3.9374 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.1 |  | 514.7863 | 0.0609 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.185 |  | 294.7171 | 0.4981 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.43 |  | 27.1376 | -2.6075 | 28.05 | 27.6 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.025 |  | 35.7926 | -2.1446 | 37.365 | 36.4 | 0.0571 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.94 |  | 21.4392 | -2.3286 | 22.18 | 21.78 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1441.18 |  | 1478.6532 | -2.5343 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 460.935 |  | 479.4608 | -3.8639 | 498.04 | 480.14 | 0.217 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 754.29 |  | 769.7702 | -2.011 | 797.155 | 768.7 | 3.9335 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.39 |  | 255.3958 | -0.0023 | 258.07 | 252.62 | 0.0274 | below_vwap | below_vwap |
| META | cloud_ai_capex | 670.305 |  | 674.1107 | -0.5646 | 680.09 | 667.1 | 1.4337 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 253.82 |  | 258.0068 | -1.6227 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.545 |  | 163.445 | -1.7743 | 168.11 | 162.41 | 2.7967 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
