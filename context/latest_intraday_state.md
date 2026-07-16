# Intraday State

- Generated at: `2026-07-16T22:48:35+08:00`
- Market time ET: `2026-07-16T10:48:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 5, 'below_vwap': 17, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 16, 'price_stale_or_missing': 1, 'below_opening_15m_low': 12}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.12 |  | 710.5868 | 0.2158 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| SOXX | semiconductor_index | 537.66 |  | 538.3642 | -0.1308 | 543.4 | 535.47 | 0.0632 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.01 |  | 576.2334 | -0.2123 | 580.31 | 572.21 | 0.0504 | below_vwap | below_vwap |
| SPY | market_regime | 754.26 |  | 752.5758 | 0.2238 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.32 |  | 140.6133 | 0.5026 | 140.83 | 139.43 | 0.1557 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 223.275 |  | 222.9999 | 0.1234 | 222.19 | 218.09 | 0.2777 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 754.26 |  | 752.5758 | 0.2238 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 297.14 |  | 296.5309 | 0.2054 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 330.315 |  | 329.151 | 0.3536 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.26 |  | 752.5758 | 0.2238 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.14 |  | 296.5309 | 0.2054 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 223.275 |  | 222.9999 | 0.1234 | 222.19 | 218.09 | 0.2777 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 712.12 |  | 710.5868 | 0.2158 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| 5 | JCI | data_center_power_cooling | 141.32 |  | 140.6133 | 0.5026 | 140.83 | 139.43 | 0.1557 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 372.57 |  | 371.9401 | 0.1693 | 375.18 | 369.2 | 0.0939 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 330.315 |  | 329.151 | 0.3536 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 256.12 |  | 255.1767 | 0.3697 | 258.07 | 252.62 | 0.082 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 397.94 |  | 395.2586 | 0.6784 | 398.69 | 392.2 | 0.2211 | watch_only | none |
| 10 | ONTO | semiconductor_test_packaging | 290.99 |  | 290.5622 | 0.1472 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MKSI | semiconductor_materials | 341.855 |  | 341.7668 | 0.0258 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | DELL | ai_server_oem | 406.02 |  | 405.7984 | 0.0546 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 292.735 |  | 291.8729 | 0.2954 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1036.86 |  | 1029.9649 | 0.6695 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 382.745 |  | 382.1431 | 0.1575 | 386.58 | 378.53 | 0.3893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | PWR | data_center_power_cooling | 635.16 |  | 633.489 | 0.2638 | 640.25 | 631.005 | 1.7004 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ENTG | semiconductor_materials | 136.42 |  | 135.9299 | 0.3606 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TT | data_center_power_cooling | 475.59 |  | 473.9215 | 0.3521 | 474.085 | 467.64 | 4.7457 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TSM | foundry | 414.07 |  | 411.4223 | 0.6435 | 414.385 | 406.61 | 0.9539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.32 |  | 140.6133 | 0.5026 | 140.83 | 139.43 | 0.1557 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 223.275 |  | 222.9999 | 0.1234 | 222.19 | 218.09 | 0.2777 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 754.26 |  | 752.5758 | 0.2238 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 297.14 |  | 296.5309 | 0.2054 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 330.315 |  | 329.151 | 0.3536 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1825.36 |  | 1827.5398 | -0.1193 | 1823.13 | 1796.26 | 0.5643 | below_vwap | below_vwap,spread_too_wide |
| 7 | TT | data_center_power_cooling | 475.59 |  | 473.9215 | 0.3521 | 474.085 | 467.64 | 4.7457 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | GEV | data_center_power_cooling | 1036.86 |  | 1029.9649 | 0.6695 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | AMAT | semiconductor_equipment | 578.76 |  | 575.7156 | 0.5288 | 572.69 | 562.32 | 1.1024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | QQQ | market_regime | 712.12 |  | 710.5868 | 0.2158 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 397.94 |  | 395.2586 | 0.6784 | 398.69 | 392.2 | 0.2211 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 372.57 |  | 371.9401 | 0.1693 | 375.18 | 369.2 | 0.0939 | watch_only | none |
| 14 | AMZN | cloud_ai_capex | 256.12 |  | 255.1767 | 0.3697 | 258.07 | 252.62 | 0.082 | watch_only | none |
| 15 | TQQQ | leveraged_tool | 72.56 |  | 72.2156 | 0.4769 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| 16 | ANET | ai_networking_optical | 166.05 |  | 166.3812 | -0.1991 | 169.91 | 165.6 | 0.4878 | below_vwap | below_vwap,spread_too_wide |
| 17 | SOXX | semiconductor_index | 537.66 |  | 538.3642 | -0.1308 | 543.4 | 535.47 | 0.0632 | below_vwap | below_vwap |
| 18 | VRT | data_center_power_cooling | 296.59 |  | 296.8237 | -0.0787 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | NVDA | ai_accelerator | 207.63 |  | 208.4219 | -0.3799 | 211.03 | 207.49 | 0.0193 | below_vwap | below_vwap |
| 20 | AMD | ai_accelerator | 510.95 |  | 511.1293 | -0.0351 | 518.33 | 507.62 | 0.364 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.12 |  | 710.5868 | 0.2158 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| TQQQ | leveraged_tool | 72.56 |  | 72.2156 | 0.4769 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| NVDA | ai_accelerator | 207.63 |  | 208.4219 | -0.3799 | 211.03 | 207.49 | 0.0193 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 397.94 |  | 395.2586 | 0.6784 | 398.69 | 392.2 | 0.2211 | watch_only | none |
| AAPL | mega_cap_platform | 330.315 |  | 329.151 | 0.3536 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.57 |  | 371.9401 | 0.1693 | 375.18 | 369.2 | 0.0939 | watch_only | none |
| AMD | ai_accelerator | 510.95 |  | 511.1293 | -0.0351 | 518.33 | 507.62 | 0.364 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 414.07 |  | 411.4223 | 0.6435 | 414.385 | 406.61 | 0.9539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 537.66 |  | 538.3642 | -0.1308 | 543.4 | 535.47 | 0.0632 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.01 |  | 576.2334 | -0.2123 | 580.31 | 572.21 | 0.0504 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.745 |  | 382.1431 | 0.1575 | 386.58 | 378.53 | 0.3893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 865 |  | 867.3034 | -0.2656 | 887.1 | 866.765 | 1.0902 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 192.62 |  | 195.2189 | -1.3313 | 201.61 | 194.19 | 1.1941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 406.02 |  | 405.7984 | 0.0546 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.205 |  | 46.7593 | -1.1855 | 47.65 | 46.165 | 0.0649 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.665 |  | 25.9118 | -0.9524 | 26.71 | 25.74 | 0.0779 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.26 |  | 752.5758 | 0.2238 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.14 |  | 296.5309 | 0.2054 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.62 |  | 127.3778 | -0.5949 | 131.36 | 126.665 | 1.0267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.75 |  | 74.1237 | -0.5041 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 296.59 |  | 296.8237 | -0.0787 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 400.32 |  | 402.5336 | -0.5499 | 406.24 | 399.495 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635.16 |  | 633.489 | 0.2638 | 640.25 | 631.005 | 1.7004 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1036.86 |  | 1029.9649 | 0.6695 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 475.59 |  | 473.9215 | 0.3521 | 474.085 | 467.64 | 4.7457 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.32 |  | 140.6133 | 0.5026 | 140.83 | 139.43 | 0.1557 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 166.05 |  | 166.3812 | -0.1991 | 169.91 | 165.6 | 0.4878 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 282.45 |  | 285.008 | -0.8975 | 288.48 | 280.67 | 0.5204 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 719.92 |  | 721.9762 | -0.2848 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 395.435 |  | 399.8496 | -1.1041 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.81 |  | 103.8254 | -0.978 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.86 |  | 329.5146 | -0.8056 | 337.59 | 326.16 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1825.36 |  | 1827.5398 | -0.1193 | 1823.13 | 1796.26 | 0.5643 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 578.76 |  | 575.7156 | 0.5288 | 572.69 | 562.32 | 1.1024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 327.14 |  | 328.0027 | -0.263 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 223.275 |  | 222.9999 | 0.1234 | 222.19 | 218.09 | 0.2777 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 332.02 |  | 328.632 | 1.0309 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.99 |  | 290.5622 | 0.1472 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.66 |  | 64.8205 | -0.2476 | 66.19 | 63.93 | 4.949 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.42 |  | 135.9299 | 0.3606 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 341.855 |  | 341.7668 | 0.0258 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.53 |  | 513.2755 | -0.1452 | 515.825 | 512.23 | 3.2857 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 292.735 |  | 291.8729 | 0.2954 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.45 |  | 27.4903 | -0.1466 | 28.05 | 27.6 | 0.1093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.71 |  | 36.3224 | -1.6861 | 37.365 | 36.4 | 0.056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.37 |  | 21.6314 | -1.2084 | 22.18 | 21.78 | 0.1404 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1484.07 |  | 1500.8928 | -1.1209 | 1549.47 | 1482.06 | 3.3691 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 486.41 |  | 483.9308 | 0.5123 | 498.04 | 480.14 | 2.0559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 793.29 |  | 777.7279 | 2.001 | 797.155 | 768.7 | 4.6931 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 256.12 |  | 255.1767 | 0.3697 | 258.07 | 252.62 | 0.082 | watch_only | none |
| META | cloud_ai_capex | 678.93 |  | 673.7106 | 0.7747 | 680.09 | 667.1 | 0.4404 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 256.69 |  | 259.5435 | -1.0994 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 162.61 |  | 164.6298 | -1.2269 | 168.11 | 162.41 | 0.9716 | below_vwap | below_vwap,spread_too_wide |
