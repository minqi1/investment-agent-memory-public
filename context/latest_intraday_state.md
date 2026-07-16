# Intraday State

- Generated at: `2026-07-16T22:11:46+08:00`
- Market time ET: `2026-07-16T10:11:48-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 4, 'below_vwap': 10, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 5, 'below_opening_15m_low': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.49 |  | 709.9703 | 0.3549 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| SOXX | semiconductor_index | 544.89 |  | 537.9471 | 1.2906 | 543.4 | 535.47 | 0.1046 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 580.92 |  | 575.7352 | 0.9005 | 580.31 | 572.21 | 0.0551 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 753.53 |  | 752.044 | 0.1976 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 544.89 |  | 537.9471 | 1.2906 | 543.4 | 535.47 | 0.1046 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 228.345 |  | 222.0051 | 2.8557 | 222.19 | 218.09 | 0.1007 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 580.92 |  | 575.7352 | 0.9005 | 580.31 | 572.21 | 0.0551 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 753.53 |  | 752.044 | 0.1976 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 297.715 |  | 296.2812 | 0.4839 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.53 |  | 752.044 | 0.1976 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.715 |  | 296.2812 | 0.4839 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 46.92 |  | 46.8596 | 0.1288 | 47.65 | 46.165 | 0.0639 | watch_only | none |
| 4 | QQQ | market_regime | 712.49 |  | 709.9703 | 0.3549 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| 5 | SOXX | semiconductor_index | 544.89 |  | 537.9471 | 1.2906 | 543.4 | 535.47 | 0.1046 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 580.92 |  | 575.7352 | 0.9005 | 580.31 | 572.21 | 0.0551 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 27.69 |  | 27.5056 | 0.6706 | 28.05 | 27.6 | 0.1083 | watch_only | none |
| 8 | CIEN | ai_networking_optical | 402.73 |  | 401.3002 | 0.3563 | 410 | 397.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 405.08 |  | 402.0234 | 0.7603 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | META | cloud_ai_capex | 672.4 |  | 672.3408 | 0.0088 | 680.09 | 667.1 | 0.4982 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | CRWV | gpu_cloud_ai_factory | 74.36 |  | 74.1655 | 0.2623 | 75.54 | 73.985 | 4.6934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | KLAC | semiconductor_equipment | 228.345 |  | 222.0051 | 2.8557 | 222.19 | 218.09 | 0.1007 | buy_precheck_manual_confirm | none |
| 13 | ANET | ai_networking_optical | 167.32 |  | 166.4371 | 0.5305 | 169.91 | 165.6 | 3.7891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 412.365 |  | 410.406 | 0.4773 | 414.385 | 406.61 | 0.3953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 636.46 |  | 632.8541 | 0.5698 | 640.25 | 631.005 | 2.063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | DELL | ai_server_oem | 409.9 |  | 404.3129 | 1.3819 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TT | data_center_power_cooling | 478.755 |  | 472.6983 | 1.2813 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 142.135 |  | 140.0725 | 1.4725 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | NVDA | ai_accelerator | 208.22 |  | 208.4199 | -0.0959 | 211.03 | 207.49 | 0.024 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 544.89 |  | 537.9471 | 1.2906 | 543.4 | 535.47 | 0.1046 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 228.345 |  | 222.0051 | 2.8557 | 222.19 | 218.09 | 0.1007 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 580.92 |  | 575.7352 | 0.9005 | 580.31 | 572.21 | 0.0551 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 753.53 |  | 752.044 | 0.1976 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 297.715 |  | 296.2812 | 0.4839 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 478.755 |  | 472.6983 | 1.2813 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 142.135 |  | 140.0725 | 1.4725 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 1048.48 |  | 1026.8448 | 2.107 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ASML | semiconductor_equipment | 1850.42 |  | 1825.5135 | 1.3644 | 1823.13 | 1796.26 | 0.7744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | AMAT | semiconductor_equipment | 590.78 |  | 572.5149 | 3.1903 | 572.69 | 562.32 | 0.8125 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ONTO | semiconductor_test_packaging | 296.14 |  | 288.9588 | 2.4852 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | LRCX | semiconductor_equipment | 336.46 |  | 327.4418 | 2.7541 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | COHU | semiconductor_test_packaging | 53.87 |  | 52.3575 | 2.8888 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | COHR | ai_networking_optical | 289.59 |  | 284.7325 | 1.706 | 288.48 | 280.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TER | semiconductor_test_packaging | 334.575 |  | 327.606 | 2.1272 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | QQQ | market_regime | 712.49 |  | 709.9703 | 0.3549 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| 18 | HPE | ai_server_oem | 46.92 |  | 46.8596 | 0.1288 | 47.65 | 46.165 | 0.0639 | watch_only | none |
| 19 | APLD | high_beta_ai_infrastructure | 27.69 |  | 27.5056 | 0.6706 | 28.05 | 27.6 | 0.1083 | watch_only | none |
| 20 | TQQQ | leveraged_tool | 72.81 |  | 72.0621 | 1.0379 | 73.09 | 71.45 | 0.0137 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.49 |  | 709.9703 | 0.3549 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| TQQQ | leveraged_tool | 72.81 |  | 72.0621 | 1.0379 | 73.09 | 71.45 | 0.0137 | watch_only | none |
| NVDA | ai_accelerator | 208.22 |  | 208.4199 | -0.0959 | 211.03 | 207.49 | 0.024 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 392.965 |  | 395.1755 | -0.5594 | 398.69 | 392.2 | 0.5878 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 328.095 |  | 328.8384 | -0.2261 | 328.98 | 326.885 | 0.0701 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 370.275 |  | 371.432 | -0.3115 | 375.18 | 369.2 | 0.0243 | below_vwap | below_vwap |
| AMD | ai_accelerator | 516.53 |  | 512.1118 | 0.8627 | 518.33 | 507.62 | 0.4472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 412.365 |  | 410.406 | 0.4773 | 414.385 | 406.61 | 0.3953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 544.89 |  | 537.9471 | 1.2906 | 543.4 | 535.47 | 0.1046 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 580.92 |  | 575.7352 | 0.9005 | 580.31 | 572.21 | 0.0551 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.685 |  | 381.4472 | 1.111 | 386.58 | 378.53 | 3.7207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 877.62 |  | 866.5919 | 1.2726 | 887.1 | 866.765 | 3.1335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 197.345 |  | 195.4871 | 0.9504 | 201.61 | 194.19 | 1.0996 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 409.9 |  | 404.3129 | 1.3819 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.92 |  | 46.8596 | 0.1288 | 47.65 | 46.165 | 0.0639 | watch_only | none |
| SMCI | ai_server_oem | 25.94 |  | 25.959 | -0.073 | 26.71 | 25.74 | 0.0771 | below_vwap | below_vwap |
| SPY | market_regime | 753.53 |  | 752.044 | 0.1976 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.715 |  | 296.2812 | 0.4839 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.29 |  | 127.6144 | -0.2542 | 131.36 | 126.665 | 2.1604 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.36 |  | 74.1655 | 0.2623 | 75.54 | 73.985 | 4.6934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.33 |  | 295.7291 | 1.2176 | 300.385 | 293.64 | 4.1693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.08 |  | 402.0234 | 0.7603 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 636.46 |  | 632.8541 | 0.5698 | 640.25 | 631.005 | 2.063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1048.48 |  | 1026.8448 | 2.107 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 478.755 |  | 472.6983 | 1.2813 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.135 |  | 140.0725 | 1.4725 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.32 |  | 166.4371 | 0.5305 | 169.91 | 165.6 | 3.7891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 289.59 |  | 284.7325 | 1.706 | 288.48 | 280.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 734.26 |  | 722.2671 | 1.6605 | 737.175 | 720.21 | 4.956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 402.73 |  | 401.3002 | 0.3563 | 410 | 397.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 105.68 |  | 103.8517 | 1.7605 | 106.975 | 102.85 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 332.43 |  | 329.3362 | 0.9394 | 337.59 | 326.16 | 0.755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1850.42 |  | 1825.5135 | 1.3644 | 1823.13 | 1796.26 | 0.7744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 590.78 |  | 572.5149 | 3.1903 | 572.69 | 562.32 | 0.8125 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 336.46 |  | 327.4418 | 2.7541 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 228.345 |  | 222.0051 | 2.8557 | 222.19 | 218.09 | 0.1007 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 334.575 |  | 327.606 | 2.1272 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.14 |  | 288.9588 | 2.4852 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.79 |  | 64.7949 | 1.5358 | 66.19 | 63.93 | 4.6664 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 53.87 |  | 52.3575 | 2.8888 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.805 |  | 135.1374 | 1.974 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.1 |  | 513.634 | -0.2987 | 515.825 | 512.23 | 0.1992 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 291.15 |  | 291.4929 | -0.1176 | 293.89 | 291.35 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.69 |  | 27.5056 | 0.6706 | 28.05 | 27.6 | 0.1083 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 36.44 |  | 36.4977 | -0.1582 | 37.365 | 36.4 | 2.9363 | below_vwap | below_vwap,spread_too_wide |
| CORZ | high_beta_ai_infrastructure | 21.69 |  | 21.7155 | -0.1175 | 22.18 | 21.78 | 0.1383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1522.14 |  | 1500.8192 | 1.4206 | 1549.47 | 1482.06 | 0.8278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 493.44 |  | 483.0092 | 2.1595 | 498.04 | 480.14 | 4.7382 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 792.91 |  | 775.498 | 2.2453 | 797.155 | 768.7 | 4.8795 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 253.79 |  | 254.7211 | -0.3655 | 258.07 | 252.62 | 0.0552 | below_vwap | below_vwap |
| META | cloud_ai_capex | 672.4 |  | 672.3408 | 0.0088 | 680.09 | 667.1 | 0.4982 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 262.355 |  | 260.1008 | 0.8667 | 265.96 | 258.1 | 3.4915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 164.57 |  | 164.9015 | -0.201 | 168.11 | 162.41 | 2.1268 | below_vwap | below_vwap,spread_too_wide |
