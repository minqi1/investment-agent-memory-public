# Intraday State

- Generated at: `2026-07-17T00:09:52+08:00`
- Market time ET: `2026-07-16T12:09:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 18, 'below_opening_15m_low': 30, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'watch_only': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.98 |  | 710.4477 | -0.2066 | 713.55 | 708.25 | 0.0635 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 532.255 |  | 537.2167 | -0.9236 | 543.4 | 535.47 | 0.0996 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 570.36 |  | 575.1167 | -0.8271 | 580.31 | 572.21 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.85 |  | 752.8684 | -0.0024 | 753.51 | 751.13 | 0.0239 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.225 |  | 396.4098 | 0.9624 | 398.69 | 392.2 | 0.1374 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.45 |  | 329.8067 | 0.4983 | 328.98 | 326.885 | 0.0453 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.45 |  | 329.8067 | 0.4983 | 328.98 | 326.885 | 0.0453 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 256.12 |  | 255.3348 | 0.3075 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 3 | GEV | data_center_power_cooling | 1033.45 |  | 1032.6093 | 0.0814 | 1035.07 | 1021.09 | 0.3 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 400.225 |  | 396.4098 | 0.9624 | 398.69 | 392.2 | 0.1374 | buy_precheck_manual_confirm | none |
| 5 | APD | industrial_gases | 296.645 |  | 294.6123 | 0.69 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | LIN | industrial_gases | 516.99 |  | 514.6751 | 0.4498 | 515.825 | 512.23 | 0.3946 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 167.22 |  | 166.3081 | 0.5483 | 169.91 | 165.6 | 4.3834 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | IWM | market_regime | 296.44 |  | 296.6058 | -0.0559 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 9 | TSM | foundry | 408.31 |  | 411.0798 | -0.6738 | 414.385 | 406.61 | 0.0833 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 708.98 |  | 710.4477 | -0.2066 | 713.55 | 708.25 | 0.0635 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1811.28 |  | 1825.1189 | -0.7582 | 1823.13 | 1796.26 | 0.0657 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 569.64 |  | 574.5755 | -0.859 | 572.69 | 562.32 | 0.093 | below_vwap | below_vwap |
| 13 | KLAC | semiconductor_equipment | 220.29 |  | 222.6767 | -1.0718 | 222.19 | 218.09 | 0.1498 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 752.85 |  | 752.8684 | -0.0024 | 753.51 | 751.13 | 0.0239 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 140.35 |  | 140.6718 | -0.2287 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ONTO | semiconductor_test_packaging | 288.6 |  | 290.5498 | -0.6711 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | GOOGL | cloud_ai_capex | 370.52 |  | 371.9574 | -0.3864 | 375.18 | 369.2 | 0.1619 | below_vwap | below_vwap |
| 19 | SKHY | memory_hbm_storage | 163.49 |  | 163.5692 | -0.0484 | 168.11 | 162.41 | 0.2324 | below_vwap | below_vwap |
| 20 | ENTG | semiconductor_materials | 134.76 |  | 135.9339 | -0.8636 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.225 |  | 396.4098 | 0.9624 | 398.69 | 392.2 | 0.1374 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.45 |  | 329.8067 | 0.4983 | 328.98 | 326.885 | 0.0453 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.14 |  | 474.3589 | -0.0462 | 474.085 | 467.64 | 4.9395 | below_vwap | below_vwap,spread_too_wide |
| 4 | IWM | market_regime | 296.44 |  | 296.6058 | -0.0559 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 5 | LIN | industrial_gases | 516.99 |  | 514.6751 | 0.4498 | 515.825 | 512.23 | 0.3946 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.645 |  | 294.6123 | 0.69 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | GEV | data_center_power_cooling | 1033.45 |  | 1032.6093 | 0.0814 | 1035.07 | 1021.09 | 0.3 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 256.12 |  | 255.3348 | 0.3075 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 9 | TSM | foundry | 408.31 |  | 411.0798 | -0.6738 | 414.385 | 406.61 | 0.0833 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 708.98 |  | 710.4477 | -0.2066 | 713.55 | 708.25 | 0.0635 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 380.72 |  | 381.8105 | -0.2856 | 386.58 | 378.53 | 0.6882 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 140.35 |  | 140.6718 | -0.2287 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ASML | semiconductor_equipment | 1811.28 |  | 1825.1189 | -0.7582 | 1823.13 | 1796.26 | 0.0657 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 569.64 |  | 574.5755 | -0.859 | 572.69 | 562.32 | 0.093 | below_vwap | below_vwap |
| 15 | ONTO | semiconductor_test_packaging | 288.6 |  | 290.5498 | -0.6711 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 220.29 |  | 222.6767 | -1.0718 | 222.19 | 218.09 | 0.1498 | below_vwap | below_vwap |
| 17 | SPY | market_regime | 752.85 |  | 752.8684 | -0.0024 | 753.51 | 751.13 | 0.0239 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ENTG | semiconductor_materials | 134.76 |  | 135.9339 | -0.8636 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | GOOGL | cloud_ai_capex | 370.52 |  | 371.9574 | -0.3864 | 375.18 | 369.2 | 0.1619 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.98 |  | 710.4477 | -0.2066 | 713.55 | 708.25 | 0.0635 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.75 |  | 72.1755 | -0.5896 | 73.09 | 71.45 | 0.0279 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.025 |  | 207.6205 | -0.2868 | 211.03 | 207.49 | 0.1932 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.225 |  | 396.4098 | 0.9624 | 398.69 | 392.2 | 0.1374 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.45 |  | 329.8067 | 0.4983 | 328.98 | 326.885 | 0.0453 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.52 |  | 371.9574 | -0.3864 | 375.18 | 369.2 | 0.1619 | below_vwap | below_vwap |
| AMD | ai_accelerator | 504.1 |  | 509.8432 | -1.1265 | 518.33 | 507.62 | 0.2281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 408.31 |  | 411.0798 | -0.6738 | 414.385 | 406.61 | 0.0833 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 532.255 |  | 537.2167 | -0.9236 | 543.4 | 535.47 | 0.0996 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 570.36 |  | 575.1167 | -0.8271 | 580.31 | 572.21 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.72 |  | 381.8105 | -0.2856 | 386.58 | 378.53 | 0.6882 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 852.44 |  | 863.2897 | -1.2568 | 887.1 | 866.765 | 1.5614 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.94 |  | 193.3052 | -2.2582 | 201.61 | 194.19 | 1.5666 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.06 |  | 404.4607 | -1.088 | 411.65 | 400.635 | 4.5693 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.73 |  | 46.1824 | -0.9796 | 47.65 | 46.165 | 0.0656 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.17 |  | 25.6469 | -1.8596 | 26.71 | 25.74 | 0.0795 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.85 |  | 752.8684 | -0.0024 | 753.51 | 751.13 | 0.0239 | below_vwap | below_vwap |
| IWM | market_regime | 296.44 |  | 296.6058 | -0.0559 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.2 |  | 126.9418 | -0.5844 | 131.36 | 126.665 | 0.0634 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.61 |  | 73.7011 | -1.4804 | 75.54 | 73.985 | 0.0964 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 291.9 |  | 296.0335 | -1.3963 | 300.385 | 293.64 | 2.381 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.53 |  | 400.9637 | -1.6046 | 406.24 | 399.495 | 1.3687 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 630.115 |  | 633.043 | -0.4625 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1033.45 |  | 1032.6093 | 0.0814 | 1035.07 | 1021.09 | 0.3 | watch_only | none |
| TT | data_center_power_cooling | 474.14 |  | 474.3589 | -0.0462 | 474.085 | 467.64 | 4.9395 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.35 |  | 140.6718 | -0.2287 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.22 |  | 166.3081 | 0.5483 | 169.91 | 165.6 | 4.3834 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.55 |  | 283.3491 | -2.0466 | 288.48 | 280.67 | 1.5889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 703.52 |  | 713.7083 | -1.4275 | 737.175 | 720.21 | 2.2714 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.165 |  | 397.7251 | -0.6437 | 410 | 397.68 | 4.6841 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 100.22 |  | 102.8895 | -2.5945 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.555 |  | 326.4824 | -2.4281 | 337.59 | 326.16 | 3.6257 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1811.28 |  | 1825.1189 | -0.7582 | 1823.13 | 1796.26 | 0.0657 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 569.64 |  | 574.5755 | -0.859 | 572.69 | 562.32 | 0.093 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 322.27 |  | 326.4647 | -1.2849 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.29 |  | 222.6767 | -1.0718 | 222.19 | 218.09 | 0.1498 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 325.23 |  | 328.7095 | -1.0585 | 332.49 | 326.685 | 0.7349 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 288.6 |  | 290.5498 | -0.6711 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.74 |  | 64.5535 | -1.2602 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.885 |  | 52.6281 | -1.412 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.76 |  | 135.9339 | -0.8636 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 336.815 |  | 340.3238 | -1.031 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 516.99 |  | 514.6751 | 0.4498 | 515.825 | 512.23 | 0.3946 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.645 |  | 294.6123 | 0.69 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.375 |  | 27.2404 | -3.1768 | 28.05 | 27.6 | 0.0758 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.05 |  | 35.8867 | -2.3314 | 37.365 | 36.4 | 0.0571 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.05 |  | 21.4881 | -2.039 | 22.18 | 21.78 | 0.095 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1440 |  | 1484.4038 | -2.9914 | 1549.47 | 1482.06 | 4.8611 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 467.94 |  | 481.1098 | -2.7374 | 498.04 | 480.14 | 0.7522 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 759.845 |  | 771.7755 | -1.5458 | 797.155 | 768.7 | 4.747 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.12 |  | 255.3348 | 0.3075 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 672.77 |  | 674.9068 | -0.3166 | 680.09 | 667.1 | 0.7135 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.5 |  | 258.3487 | -1.1027 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 163.49 |  | 163.5692 | -0.0484 | 168.11 | 162.41 | 0.2324 | below_vwap | below_vwap |
