# Intraday State

- Generated at: `2026-07-16T23:36:37+08:00`
- Market time ET: `2026-07-16T11:36:38-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 3, 'below_opening_15m_low': 18, 'manual_confirm_candidate': 4, 'below_vwap': 18, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 12}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.16 |  | 710.4942 | 0.0937 | 713.55 | 708.25 | 0.0253 | watch_only | none |
| SOXX | semiconductor_index | 536.19 |  | 537.6801 | -0.2771 | 543.4 | 535.47 | 0.0597 | below_vwap | below_vwap |
| SMH | semiconductor_index | 574.015 |  | 575.6448 | -0.2831 | 580.31 | 572.21 | 0.0958 | below_vwap | below_vwap |
| SPY | market_regime | 754.09 |  | 752.8026 | 0.171 | 753.51 | 751.13 | 0.0292 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.09 |  | 752.8026 | 0.171 | 753.51 | 751.13 | 0.0292 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.05 |  | 296.6148 | 0.1467 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 399.075 |  | 395.8578 | 0.8127 | 398.69 | 392.2 | 0.2731 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.975 |  | 329.4625 | 0.4591 | 328.98 | 326.885 | 0.1964 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.09 |  | 752.8026 | 0.171 | 753.51 | 751.13 | 0.0292 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.05 |  | 296.6148 | 0.1467 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 711.16 |  | 710.4942 | 0.0937 | 713.55 | 708.25 | 0.0253 | watch_only | none |
| 4 | AMZN | cloud_ai_capex | 255.575 |  | 255.2218 | 0.1384 | 258.07 | 252.62 | 0.0548 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 330.975 |  | 329.4625 | 0.4591 | 328.98 | 326.885 | 0.1964 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 399.075 |  | 395.8578 | 0.8127 | 398.69 | 392.2 | 0.2731 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 140.87 |  | 140.7077 | 0.1153 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | COHU | semiconductor_test_packaging | 52.72 |  | 52.6707 | 0.0937 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | MKSI | semiconductor_materials | 341.585 |  | 341.2801 | 0.0893 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ENTG | semiconductor_materials | 136.34 |  | 135.9861 | 0.2603 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TT | data_center_power_cooling | 475.48 |  | 474.3551 | 0.2371 | 474.085 | 467.64 | 4.7952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ASML | semiconductor_equipment | 1828.24 |  | 1825.7188 | 0.1381 | 1823.13 | 1796.26 | 0.9966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | GEV | data_center_power_cooling | 1035.5 |  | 1032.9442 | 0.2474 | 1035.07 | 1021.09 | 0.9696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | LIN | industrial_gases | 517.155 |  | 514.205 | 0.5737 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 330.3 |  | 329.0089 | 0.3924 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | META | cloud_ai_capex | 676.475 |  | 674.9509 | 0.2258 | 680.09 | 667.1 | 0.3607 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ANET | ai_networking_optical | 167.08 |  | 166.2678 | 0.4885 | 169.91 | 165.6 | 0.7122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SOXX | semiconductor_index | 536.19 |  | 537.6801 | -0.2771 | 543.4 | 535.47 | 0.0597 | below_vwap | below_vwap |
| 19 | APD | industrial_gases | 296.86 |  | 294.3571 | 0.8503 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SMH | semiconductor_index | 574.015 |  | 575.6448 | -0.2831 | 580.31 | 572.21 | 0.0958 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.09 |  | 752.8026 | 0.171 | 753.51 | 751.13 | 0.0292 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.05 |  | 296.6148 | 0.1467 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 399.075 |  | 395.8578 | 0.8127 | 398.69 | 392.2 | 0.2731 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.975 |  | 329.4625 | 0.4591 | 328.98 | 326.885 | 0.1964 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 573.27 |  | 575.3418 | -0.3601 | 572.69 | 562.32 | 3.494 | below_vwap | below_vwap,spread_too_wide |
| 6 | KLAC | semiconductor_equipment | 222.23 |  | 222.8252 | -0.2671 | 222.19 | 218.09 | 0.1845 | below_vwap | below_vwap |
| 7 | TT | data_center_power_cooling | 475.48 |  | 474.3551 | 0.2371 | 474.085 | 467.64 | 4.7952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | JCI | data_center_power_cooling | 140.87 |  | 140.7077 | 0.1153 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | GEV | data_center_power_cooling | 1035.5 |  | 1032.9442 | 0.2474 | 1035.07 | 1021.09 | 0.9696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ASML | semiconductor_equipment | 1828.24 |  | 1825.7188 | 0.1381 | 1823.13 | 1796.26 | 0.9966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | LIN | industrial_gases | 517.155 |  | 514.205 | 0.5737 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | APD | industrial_gases | 296.86 |  | 294.3571 | 0.8503 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | COHU | semiconductor_test_packaging | 52.72 |  | 52.6707 | 0.0937 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | QQQ | market_regime | 711.16 |  | 710.4942 | 0.0937 | 713.55 | 708.25 | 0.0253 | watch_only | none |
| 15 | AMZN | cloud_ai_capex | 255.575 |  | 255.2218 | 0.1384 | 258.07 | 252.62 | 0.0548 | watch_only | none |
| 16 | TQQQ | leveraged_tool | 72.32 |  | 72.2006 | 0.1654 | 73.09 | 71.45 | 0.0277 | watch_only | none |
| 17 | SOXX | semiconductor_index | 536.19 |  | 537.6801 | -0.2771 | 543.4 | 535.47 | 0.0597 | below_vwap | below_vwap |
| 18 | TSM | foundry | 410.85 |  | 411.3869 | -0.1305 | 414.385 | 406.61 | 0.2434 | below_vwap | below_vwap |
| 19 | AVGO | custom_silicon_networking | 381.8 |  | 381.8604 | -0.0158 | 386.58 | 378.53 | 0.1938 | below_vwap | below_vwap |
| 20 | VRT | data_center_power_cooling | 294.61 |  | 296.4326 | -0.6148 | 300.385 | 293.64 | 0.8486 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.16 |  | 710.4942 | 0.0937 | 713.55 | 708.25 | 0.0253 | watch_only | none |
| TQQQ | leveraged_tool | 72.32 |  | 72.2006 | 0.1654 | 73.09 | 71.45 | 0.0277 | watch_only | none |
| NVDA | ai_accelerator | 207.22 |  | 207.6427 | -0.2036 | 211.03 | 207.49 | 0.029 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.075 |  | 395.8578 | 0.8127 | 398.69 | 392.2 | 0.2731 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.975 |  | 329.4625 | 0.4591 | 328.98 | 326.885 | 0.1964 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.65 |  | 372.0152 | -0.0982 | 375.18 | 369.2 | 0.3767 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 508.82 |  | 510.451 | -0.3195 | 518.33 | 507.62 | 0.2476 | below_vwap | below_vwap |
| TSM | foundry | 410.85 |  | 411.3869 | -0.1305 | 414.385 | 406.61 | 0.2434 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 536.19 |  | 537.6801 | -0.2771 | 543.4 | 535.47 | 0.0597 | below_vwap | below_vwap |
| SMH | semiconductor_index | 574.015 |  | 575.6448 | -0.2831 | 580.31 | 572.21 | 0.0958 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.8 |  | 381.8604 | -0.0158 | 386.58 | 378.53 | 0.1938 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 862.295 |  | 864.7178 | -0.2802 | 887.1 | 866.765 | 0.2319 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 191.89 |  | 193.9449 | -1.0595 | 201.61 | 194.19 | 0.1772 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 403.7 |  | 404.9874 | -0.3179 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.06 |  | 46.3941 | -0.7201 | 47.65 | 46.165 | 0.0217 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.4 |  | 25.7427 | -1.3312 | 26.71 | 25.74 | 0.0394 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.09 |  | 752.8026 | 0.171 | 753.51 | 751.13 | 0.0292 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.05 |  | 296.6148 | 0.1467 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.88 |  | 127.1259 | -0.1935 | 131.36 | 126.665 | 3.2708 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.445 |  | 73.9239 | -0.6479 | 75.54 | 73.985 | 0.7625 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 294.61 |  | 296.4326 | -0.6148 | 300.385 | 293.64 | 0.8486 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 397.16 |  | 401.5922 | -1.1037 | 406.24 | 399.495 | 4.6455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 632.72 |  | 633.2342 | -0.0812 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1035.5 |  | 1032.9442 | 0.2474 | 1035.07 | 1021.09 | 0.9696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.48 |  | 474.3551 | 0.2371 | 474.085 | 467.64 | 4.7952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.87 |  | 140.7077 | 0.1153 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.08 |  | 166.2678 | 0.4885 | 169.91 | 165.6 | 0.7122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 279.29 |  | 283.9421 | -1.6384 | 288.48 | 280.67 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 707.78 |  | 716.9841 | -1.2837 | 737.175 | 720.21 | 4.0973 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.65 |  | 398.5198 | -0.7201 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.35 |  | 103.1975 | -1.7903 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 325.04 |  | 328.6759 | -1.1062 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1828.24 |  | 1825.7188 | 0.1381 | 1823.13 | 1796.26 | 0.9966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 573.27 |  | 575.3418 | -0.3601 | 572.69 | 562.32 | 3.494 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 326.09 |  | 327.3031 | -0.3706 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.23 |  | 222.8252 | -0.2671 | 222.19 | 218.09 | 0.1845 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 330.3 |  | 329.0089 | 0.3924 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.375 |  | 290.5564 | -0.0624 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.525 |  | 64.6145 | -0.1385 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.72 |  | 52.6707 | 0.0937 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.34 |  | 135.9861 | 0.2603 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 341.585 |  | 341.2801 | 0.0893 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 517.155 |  | 514.205 | 0.5737 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.86 |  | 294.3571 | 0.8503 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.92 |  | 27.3802 | -1.6807 | 28.05 | 27.6 | 0.0743 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.68 |  | 36.0742 | -1.0926 | 37.365 | 36.4 | 0.0561 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.31 |  | 21.5558 | -1.1404 | 22.18 | 21.78 | 0.0939 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1467.975 |  | 1490.0586 | -1.4821 | 1549.47 | 1482.06 | 3.746 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 474.505 |  | 482.7912 | -1.7163 | 498.04 | 480.14 | 0.5016 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 769.32 |  | 777.2702 | -1.0228 | 797.155 | 768.7 | 1.1699 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.575 |  | 255.2218 | 0.1384 | 258.07 | 252.62 | 0.0548 | watch_only | none |
| META | cloud_ai_capex | 676.475 |  | 674.9509 | 0.2258 | 680.09 | 667.1 | 0.3607 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 256.825 |  | 258.67 | -0.7133 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 163.47 |  | 163.8536 | -0.2341 | 168.11 | 162.41 | 2.1655 | below_vwap | below_vwap,spread_too_wide |
