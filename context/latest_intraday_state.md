# Intraday State

- Generated at: `2026-07-17T02:35:41+08:00`
- Market time ET: `2026-07-16T14:35:42-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 9, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.59 |  | 709.4692 | -0.4058 | 713.55 | 708.25 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.09 |  | 533.9057 | -0.902 | 543.4 | 535.47 | 0.0662 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.45 |  | 572.0013 | -0.7957 | 580.31 | 572.21 | 0.0458 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.69 |  | 752.4315 | -0.2314 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.39 |  | 399.21 | 1.2976 | 398.69 | 392.2 | 0.0915 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.3 |  | 330.611 | 0.2084 | 328.98 | 326.885 | 0.0573 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.3 |  | 330.611 | 0.2084 | 328.98 | 326.885 | 0.0573 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 404.39 |  | 399.21 | 1.2976 | 398.69 | 392.2 | 0.0915 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.56 |  | 140.5166 | 0.0309 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 517.15 |  | 515.1063 | 0.3968 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.84 |  | 294.9335 | 0.3074 | 293.89 | 291.35 | 3.9988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.805 |  | 166.5708 | 0.741 | 169.91 | 165.6 | 3.5398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1796.76 |  | 1818.649 | -1.2036 | 1823.13 | 1796.26 | 0.0824 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 220.1 |  | 221.0126 | -0.4129 | 222.19 | 218.09 | 0.1136 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.32 |  | 296.1633 | -0.2847 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 10 | AMZN | cloud_ai_capex | 252.925 |  | 255.3999 | -0.969 | 258.07 | 252.62 | 0.0079 | below_vwap | below_vwap |
| 11 | META | cloud_ai_capex | 668.395 |  | 671.6814 | -0.4893 | 680.09 | 667.1 | 0.0509 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ARM | ai_accelerator | 257.64 |  | 257.2987 | 0.1326 | 265.96 | 258.1 | 3.8814 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 14 | TT | data_center_power_cooling | 473.18 |  | 474.1727 | -0.2094 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 134.115 |  | 134.9797 | -0.6406 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | GEV | data_center_power_cooling | 1022.36 |  | 1027.6509 | -0.5149 | 1035.07 | 1021.09 | 0.359 | below_vwap | below_vwap,spread_too_wide |
| 17 | SOXX | semiconductor_index | 529.09 |  | 533.9057 | -0.902 | 543.4 | 535.47 | 0.0662 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | CIEN | ai_networking_optical | 390.605 |  | 394.9208 | -1.0928 | 410 | 397.68 | 0.0973 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | QQQ | market_regime | 706.59 |  | 709.4692 | -0.4058 | 713.55 | 708.25 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | NVDA | ai_accelerator | 206.7 |  | 207.3634 | -0.3199 | 211.03 | 207.49 | 0.0242 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.39 |  | 399.21 | 1.2976 | 398.69 | 392.2 | 0.0915 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.3 |  | 330.611 | 0.2084 | 328.98 | 326.885 | 0.0573 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 517.15 |  | 515.1063 | 0.3968 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.84 |  | 294.9335 | 0.3074 | 293.89 | 291.35 | 3.9988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TT | data_center_power_cooling | 473.18 |  | 474.1727 | -0.2094 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1022.36 |  | 1027.6509 | -0.5149 | 1035.07 | 1021.09 | 0.359 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1796.76 |  | 1818.649 | -1.2036 | 1823.13 | 1796.26 | 0.0824 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 220.1 |  | 221.0126 | -0.4129 | 222.19 | 218.09 | 0.1136 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.32 |  | 296.1633 | -0.2847 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 134.115 |  | 134.9797 | -0.6406 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AMZN | cloud_ai_capex | 252.925 |  | 255.3999 | -0.969 | 258.07 | 252.62 | 0.0079 | below_vwap | below_vwap |
| 13 | META | cloud_ai_capex | 668.395 |  | 671.6814 | -0.4893 | 680.09 | 667.1 | 0.0509 | below_vwap | below_vwap |
| 14 | ANET | ai_networking_optical | 167.805 |  | 166.5708 | 0.741 | 169.91 | 165.6 | 3.5398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 140.56 |  | 140.5166 | 0.0309 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ARM | ai_accelerator | 257.64 |  | 257.2987 | 0.1326 | 265.96 | 258.1 | 3.8814 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | SOXX | semiconductor_index | 529.09 |  | 533.9057 | -0.902 | 543.4 | 535.47 | 0.0662 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | TSM | foundry | 404.88 |  | 408.9728 | -1.0008 | 414.385 | 406.61 | 0.4619 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | CIEN | ai_networking_optical | 390.605 |  | 394.9208 | -1.0928 | 410 | 397.68 | 0.0973 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 706.59 |  | 709.4692 | -0.4058 | 713.55 | 708.25 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.59 |  | 709.4692 | -0.4058 | 713.55 | 708.25 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.92 |  | 71.8439 | -1.286 | 73.09 | 71.45 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.7 |  | 207.3634 | -0.3199 | 211.03 | 207.49 | 0.0242 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.39 |  | 399.21 | 1.2976 | 398.69 | 392.2 | 0.0915 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.3 |  | 330.611 | 0.2084 | 328.98 | 326.885 | 0.0573 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 360.85 |  | 369.3388 | -2.2984 | 375.18 | 369.2 | 0.0776 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 496.48 |  | 504.2528 | -1.5415 | 518.33 | 507.62 | 0.8419 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 404.88 |  | 408.9728 | -1.0008 | 414.385 | 406.61 | 0.4619 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.09 |  | 533.9057 | -0.902 | 543.4 | 535.47 | 0.0662 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.45 |  | 572.0013 | -0.7957 | 580.31 | 572.21 | 0.0458 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.64 |  | 380.0746 | -0.9037 | 386.58 | 378.53 | 0.6903 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 851.34 |  | 857.5311 | -0.722 | 887.1 | 866.765 | 2.2236 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.99 |  | 191.1149 | -1.6351 | 201.61 | 194.19 | 0.8458 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 396.755 |  | 402.3516 | -1.391 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.445 |  | 45.8267 | -0.833 | 47.65 | 46.165 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.875 |  | 25.3424 | -1.8445 | 26.71 | 25.74 | 0.0402 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.69 |  | 752.4315 | -0.2314 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.32 |  | 296.1633 | -0.2847 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.2 |  | 126.6477 | -0.3535 | 131.36 | 126.665 | 0.9113 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.89 |  | 73.3147 | -0.5792 | 75.54 | 73.985 | 2.7027 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.85 |  | 293.5871 | -1.6135 | 300.385 | 293.64 | 1.3467 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.93 |  | 399.3691 | -1.1115 | 406.24 | 399.495 | 0.1393 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 627.89 |  | 631.4529 | -0.5642 | 640.25 | 631.005 | 0.3934 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1022.36 |  | 1027.6509 | -0.5149 | 1035.07 | 1021.09 | 0.359 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.18 |  | 474.1727 | -0.2094 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.56 |  | 140.5166 | 0.0309 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.805 |  | 166.5708 | 0.741 | 169.91 | 165.6 | 3.5398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.335 |  | 280.8164 | -1.5959 | 288.48 | 280.67 | 2.4897 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 703.185 |  | 708.5491 | -0.7571 | 737.175 | 720.21 | 0.1237 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 390.605 |  | 394.9208 | -1.0928 | 410 | 397.68 | 0.0973 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.19 |  | 101.4207 | -2.1994 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 321.58 |  | 323.5559 | -0.6107 | 337.59 | 326.16 | 0.4385 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1796.76 |  | 1818.649 | -1.2036 | 1823.13 | 1796.26 | 0.0824 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 560.665 |  | 570.2616 | -1.6828 | 572.69 | 562.32 | 1.4358 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.75 |  | 323.0026 | -1.6262 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.1 |  | 221.0126 | -0.4129 | 222.19 | 218.09 | 0.1136 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.725 |  | 326.7614 | -1.2353 | 332.49 | 326.685 | 4.6789 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.38 |  | 286.7653 | -2.2267 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.125 |  | 63.9734 | -1.3262 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.76 |  | 51.8867 | -2.1715 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.115 |  | 134.9797 | -0.6406 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.5 |  | 335.012 | -1.6453 | 346.26 | 338 | 4.2033 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 517.15 |  | 515.1063 | 0.3968 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.84 |  | 294.9335 | 0.3074 | 293.89 | 291.35 | 3.9988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.075 |  | 26.8076 | -2.7328 | 28.05 | 27.6 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.25 |  | 35.5055 | -0.7197 | 37.365 | 36.4 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.91 |  | 21.2252 | -1.4852 | 22.18 | 21.78 | 0.0956 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1422.62 |  | 1464.2502 | -2.8431 | 1549.47 | 1482.06 | 2.5305 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 460.015 |  | 474.4721 | -3.047 | 498.04 | 480.14 | 0.2391 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 746.775 |  | 765.6308 | -2.4628 | 797.155 | 768.7 | 4.7364 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 252.925 |  | 255.3999 | -0.969 | 258.07 | 252.62 | 0.0079 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.395 |  | 671.6814 | -0.4893 | 680.09 | 667.1 | 0.0509 | below_vwap | below_vwap |
| ARM | ai_accelerator | 257.64 |  | 257.2987 | 0.1326 | 265.96 | 258.1 | 3.8814 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| SKHY | memory_hbm_storage | 156.83 |  | 161.8034 | -3.0738 | 168.11 | 162.41 | 0.3953 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
