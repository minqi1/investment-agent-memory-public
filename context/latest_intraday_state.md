# Intraday State

- Generated at: `2026-07-21T03:39:15+08:00`
- Market time ET: `2026-07-20T15:39:15-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `54`
- coverage_vwap: `54`
- caution_counts: `{'below_opening_15m_low': 37, 'manual_confirm_candidate': 2, 'below_vwap': 15, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.51 |  | 700.985 | -0.4957 | 705.51 | 701.82 | 0.0344 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 525.13 |  | 530.9558 | -1.0972 | 538.59 | 532.55 | 0.0533 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 558.94 |  | 565.3148 | -1.1276 | 572.46 | 567.02 | 0.059 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 742.59 |  | 744.8339 | -0.3013 | 748.69 | 746.87 | 0.0108 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.52 |  | 397.6047 | 0.9847 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 39.755 |  | 39.6923 | 0.158 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IREN | high_beta_ai_infrastructure | 39.755 |  | 39.6923 | 0.158 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.52 |  | 397.6047 | 0.9847 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 649.575 |  | 646.4601 | 0.4818 | 646.57 | 638.875 | 0.6142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | AMZN | cloud_ai_capex | 249.755 |  | 250.3659 | -0.244 | 250.2 | 248.195 | 0.044 | below_vwap | below_vwap |
| 5 | AAPL | mega_cap_platform | 328.655 |  | 326.7396 | 0.5862 | 333.63 | 330.03 | 0.0913 | below_opening_15m_low | below_opening_15m_low |
| 6 | LIN | industrial_gases | 512.46 |  | 513.1321 | -0.131 | 514.7 | 511.78 | 0.0527 | below_vwap | below_vwap |
| 7 | GOOGL | cloud_ai_capex | 352.84 |  | 355.135 | -0.6462 | 358.795 | 350.875 | 0.051 | below_vwap | below_vwap |
| 8 | LITE | ai_networking_optical |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | CORZ | high_beta_ai_infrastructure | 22.245 |  | 22.3131 | -0.305 | 22.565 | 21.85 | 0.0899 | below_vwap | below_vwap |
| 11 | APD | industrial_gases | 296.285 |  | 296.5049 | -0.0742 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8521 | -0.223 | 28.39 | 27.11 | 0.036 | below_vwap | below_vwap |
| 13 | CIEN | ai_networking_optical | 380.08 |  | 386.13 | -1.5668 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | COHR | ai_networking_optical | 286.955 |  | 293.0033 | -2.0642 | 296.46 | 286.91 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 51.24 |  | 51.5425 | -0.5869 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 310.74 |  | 313.7282 | -0.9525 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ANET | ai_networking_optical | 170.22 |  | 170.6999 | -0.2811 | 171.39 | 168.79 | 0.3995 | below_vwap | below_vwap,spread_too_wide |
| 18 | AVGO | custom_silicon_networking | 378.77 |  | 380.3377 | -0.4122 | 382.67 | 377.47 | 1.4177 | below_vwap | below_vwap,spread_too_wide |
| 19 | MRVL | custom_silicon_networking | 194.59 |  | 197.2482 | -1.3477 | 196.86 | 192.09 | 0.3546 | below_vwap | below_vwap,spread_too_wide |
| 20 | TSM | foundry | 402.15 |  | 404.0048 | -0.4591 | 409.82 | 405.51 | 0.1094 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.52 |  | 397.6047 | 0.9847 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 39.755 |  | 39.6923 | 0.158 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.285 |  | 296.5049 | -0.0742 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| 4 | META | cloud_ai_capex | 649.575 |  | 646.4601 | 0.4818 | 646.57 | 638.875 | 0.6142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 170.22 |  | 170.6999 | -0.2811 | 171.39 | 168.79 | 0.3995 | below_vwap | below_vwap,spread_too_wide |
| 6 | AVGO | custom_silicon_networking | 378.77 |  | 380.3377 | -0.4122 | 382.67 | 377.47 | 1.4177 | below_vwap | below_vwap,spread_too_wide |
| 7 | AMZN | cloud_ai_capex | 249.755 |  | 250.3659 | -0.244 | 250.2 | 248.195 | 0.044 | below_vwap | below_vwap |
| 8 | LITE | ai_networking_optical |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | CIEN | ai_networking_optical | 380.08 |  | 386.13 | -1.5668 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | LIN | industrial_gases | 512.46 |  | 513.1321 | -0.131 | 514.7 | 511.78 | 0.0527 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | GOOGL | cloud_ai_capex | 352.84 |  | 355.135 | -0.6462 | 358.795 | 350.875 | 0.051 | below_vwap | below_vwap |
| 13 | COHR | ai_networking_optical | 286.955 |  | 293.0033 | -2.0642 | 296.46 | 286.91 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | MRVL | custom_silicon_networking | 194.59 |  | 197.2482 | -1.3477 | 196.86 | 192.09 | 0.3546 | below_vwap | below_vwap,spread_too_wide |
| 15 | COHU | semiconductor_test_packaging | 51.24 |  | 51.5425 | -0.5869 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 310.74 |  | 313.7282 | -0.9525 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CORZ | high_beta_ai_infrastructure | 22.245 |  | 22.3131 | -0.305 | 22.565 | 21.85 | 0.0899 | below_vwap | below_vwap |
| 18 | APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8521 | -0.223 | 28.39 | 27.11 | 0.036 | below_vwap | below_vwap |
| 19 | AAPL | mega_cap_platform | 328.655 |  | 326.7396 | 0.5862 | 333.63 | 330.03 | 0.0913 | below_opening_15m_low | below_opening_15m_low |
| 20 | TSM | foundry | 402.15 |  | 404.0048 | -0.4591 | 409.82 | 405.51 | 0.1094 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.51 |  | 700.985 | -0.4957 | 705.51 | 701.82 | 0.0344 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 68.04 |  | 69.1053 | -1.5416 | 70.43 | 69.35 | 0.0147 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 202.92 |  | 205.1998 | -1.111 | 207.71 | 205.095 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.52 |  | 397.6047 | 0.9847 | 392.89 | 389.74 | 0.0548 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 328.655 |  | 326.7396 | 0.5862 | 333.63 | 330.03 | 0.0913 | below_opening_15m_low | below_opening_15m_low |
| GOOGL | cloud_ai_capex | 352.84 |  | 355.135 | -0.6462 | 358.795 | 350.875 | 0.051 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.68 |  | 513.7126 | -1.1743 | 522.26 | 510.97 | 0.2659 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 402.15 |  | 404.0048 | -0.4591 | 409.82 | 405.51 | 0.1094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1764000 |  | 1903393.0421 | -7.3234 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.13 |  | 530.9558 | -1.0972 | 538.59 | 532.55 | 0.0533 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 558.94 |  | 565.3148 | -1.1276 | 572.46 | 567.02 | 0.059 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 378.77 |  | 380.3377 | -0.4122 | 382.67 | 377.47 | 1.4177 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 863.47 |  | 882.4745 | -2.1535 | 898.57 | 878.92 | 3.6214 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 194.59 |  | 197.2482 | -1.3477 | 196.86 | 192.09 | 0.3546 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 383.745 |  | 389.684 | -1.5241 | 402.76 | 392.82 | 0.4065 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 44.98 |  | 45.4924 | -1.1263 | 46.21 | 45.305 | 0.0445 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 23.935 |  | 24.1636 | -0.9461 | 24.51 | 24.22 | 0.0418 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 742.59 |  | 744.8339 | -0.3013 | 748.69 | 746.87 | 0.0108 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 292.71 |  | 293.8203 | -0.3779 | 295.97 | 294.88 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 122.17 |  | 122.4067 | -0.1934 | 125.41 | 123.57 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.525 |  | 75.9301 | -3.1675 | 79.23 | 75.17 | 4.9099 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 292.235 |  | 295.4513 | -1.0886 | 300.96 | 297.175 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 400.03 |  | 403.1112 | -0.7644 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 632.51 |  | 636.5633 | -0.6367 | 644.7 | 636.38 | 1.7755 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1075.01 |  | 1077.4205 | -0.2237 | 1103.11 | 1081.14 | 0.2474 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 466.27 |  | 466.4956 | -0.0484 | 477.865 | 468.805 | 0.1137 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 138.845 |  | 140.1299 | -0.917 | 143.075 | 141.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 170.22 |  | 170.6999 | -0.2811 | 171.39 | 168.79 | 0.3995 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 286.955 |  | 293.0033 | -2.0642 | 296.46 | 286.91 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 380.08 |  | 386.13 | -1.5668 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 103.06 |  | 104.6716 | -1.5397 | 107.28 | 104.215 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 310.74 |  | 313.7282 | -0.9525 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1736.45 |  | 1750.927 | -0.8268 | 1797.04 | 1768.805 | 0.0962 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 526.6 |  | 535.1546 | -1.5985 | 554.8 | 543 | 0.1044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 306.86 |  | 311.4958 | -1.4882 | 324.32 | 319.39 | 4.2853 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 208.555 |  | 211.1863 | -1.246 | 220.28 | 216.62 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 333.885 |  | 339.4885 | -1.6506 | 349.43 | 335.335 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.385 |  | 281.4934 | -1.1042 | 288.94 | 284 | 4.6231 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.23 |  | 63.2318 | -1.5843 | 64.96 | 63.98 | 1.2213 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.24 |  | 51.5425 | -0.5869 | 52.74 | 50.72 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.045 |  | 137.0736 | -2.2095 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 324.87 |  | 328.9437 | -1.2384 | 338.1 | 328.505 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 512.46 |  | 513.1321 | -0.131 | 514.7 | 511.78 | 0.0527 | below_vwap | below_vwap |
| APD | industrial_gases | 296.285 |  | 296.5049 | -0.0742 | 296.26 | 293.84 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.79 |  | 27.8521 | -0.223 | 28.39 | 27.11 | 0.036 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 39.755 |  | 39.6923 | 0.158 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.245 |  | 22.3131 | -0.305 | 22.565 | 21.85 | 0.0899 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1386.42 |  | 1420.3692 | -2.3902 | 1449.57 | 1394.24 | 0.1399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| WDC | memory_hbm_storage | 488.78 |  | 498.3482 | -1.92 | 504.53 | 490.68 | 0.2025 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 803.88 |  | 813.7424 | -1.212 | 830.62 | 811.99 | 3.4707 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 249.755 |  | 250.3659 | -0.244 | 250.2 | 248.195 | 0.044 | below_vwap | below_vwap |
| META | cloud_ai_capex | 649.575 |  | 646.4601 | 0.4818 | 646.57 | 638.875 | 0.6142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 269.145 |  | 272.1015 | -1.0866 | 277.4 | 271.455 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 152.55 |  | 157.2037 | -2.9603 | 163.02 | 159.54 | 1.1078 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
