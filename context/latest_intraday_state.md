# Intraday State

- Generated at: `2026-07-17T02:15:44+08:00`
- Market time ET: `2026-07-16T14:15:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 1, 'below_vwap': 9, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.55 |  | 709.6009 | -0.4299 | 713.55 | 708.25 | 0.0368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.77 |  | 534.3126 | -1.0373 | 543.4 | 535.47 | 0.0813 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.92 |  | 572.2435 | -0.9303 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.74 |  | 752.5293 | -0.2378 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.91 |  | 398.7789 | 1.2867 | 398.69 | 392.2 | 0.0916 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.91 |  | 398.7789 | 1.2867 | 398.69 | 392.2 | 0.0916 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.43 |  | 294.8921 | 0.1824 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | LIN | industrial_gases | 516.915 |  | 515.0427 | 0.3635 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ANET | ai_networking_optical | 167.705 |  | 166.5192 | 0.7121 | 169.91 | 165.6 | 3.9593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GEV | data_center_power_cooling | 1021.48 |  | 1027.7931 | -0.6142 | 1035.07 | 1021.09 | 0.1155 | below_vwap | below_vwap |
| 6 | KLAC | semiconductor_equipment | 219.65 |  | 221.0338 | -0.626 | 222.19 | 218.09 | 0.0728 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 295.09 |  | 296.1931 | -0.3724 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | AMZN | cloud_ai_capex | 253.95 |  | 255.5022 | -0.6075 | 258.07 | 252.62 | 0.0315 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ARM | ai_accelerator | 257.39 |  | 257.2806 | 0.0425 | 265.96 | 258.1 | 3.8852 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 11 | TT | data_center_power_cooling | 473.39 |  | 474.2414 | -0.1795 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 140.43 |  | 140.5107 | -0.0574 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AAPL | mega_cap_platform | 329.78 |  | 330.6047 | -0.2495 | 328.98 | 326.885 | 0.752 | below_vwap | below_vwap,spread_too_wide |
| 14 | META | cloud_ai_capex | 669.905 |  | 671.9973 | -0.3114 | 680.09 | 667.1 | 2.0854 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 528.77 |  | 534.3126 | -1.0373 | 543.4 | 535.47 | 0.0813 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 706.55 |  | 709.6009 | -0.4299 | 713.55 | 708.25 | 0.0368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.83 |  | 207.3827 | -0.2665 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | PWR | data_center_power_cooling | 627.315 |  | 631.5415 | -0.6692 | 640.25 | 631.005 | 0.1323 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 566.92 |  | 572.2435 | -0.9303 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SPY | market_regime | 750.74 |  | 752.5293 | -0.2378 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.91 |  | 398.7789 | 1.2867 | 398.69 | 392.2 | 0.0916 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 329.78 |  | 330.6047 | -0.2495 | 328.98 | 326.885 | 0.752 | below_vwap | below_vwap,spread_too_wide |
| 3 | LIN | industrial_gases | 516.915 |  | 515.0427 | 0.3635 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.43 |  | 294.8921 | 0.1824 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 473.39 |  | 474.2414 | -0.1795 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.43 |  | 140.5107 | -0.0574 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | GEV | data_center_power_cooling | 1021.48 |  | 1027.7931 | -0.6142 | 1035.07 | 1021.09 | 0.1155 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 219.65 |  | 221.0338 | -0.626 | 222.19 | 218.09 | 0.0728 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.09 |  | 296.1931 | -0.3724 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | AMZN | cloud_ai_capex | 253.95 |  | 255.5022 | -0.6075 | 258.07 | 252.62 | 0.0315 | below_vwap | below_vwap |
| 12 | META | cloud_ai_capex | 669.905 |  | 671.9973 | -0.3114 | 680.09 | 667.1 | 2.0854 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 167.705 |  | 166.5192 | 0.7121 | 169.91 | 165.6 | 3.9593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ARM | ai_accelerator | 257.39 |  | 257.2806 | 0.0425 | 265.96 | 258.1 | 3.8852 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | SOXX | semiconductor_index | 528.77 |  | 534.3126 | -1.0373 | 543.4 | 535.47 | 0.0813 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.97 |  | 409.1871 | -1.0306 | 414.385 | 406.61 | 0.4667 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | CIEN | ai_networking_optical | 390.24 |  | 395.3703 | -1.2976 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 706.55 |  | 709.6009 | -0.4299 | 713.55 | 708.25 | 0.0368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 376.11 |  | 380.2364 | -1.0852 | 386.58 | 378.53 | 1.5953 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 848.08 |  | 857.6137 | -1.1116 | 887.1 | 866.765 | 2.4691 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.55 |  | 709.6009 | -0.4299 | 713.55 | 708.25 | 0.0368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.87 |  | 71.8907 | -1.4198 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.83 |  | 207.3827 | -0.2665 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.91 |  | 398.7789 | 1.2867 | 398.69 | 392.2 | 0.0916 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 329.78 |  | 330.6047 | -0.2495 | 328.98 | 326.885 | 0.752 | below_vwap | below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 363.77 |  | 370.618 | -1.8477 | 375.18 | 369.2 | 1.457 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496.07 |  | 504.7482 | -1.7193 | 518.33 | 507.62 | 0.7035 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 404.97 |  | 409.1871 | -1.0306 | 414.385 | 406.61 | 0.4667 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.77 |  | 534.3126 | -1.0373 | 543.4 | 535.47 | 0.0813 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.92 |  | 572.2435 | -0.9303 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.11 |  | 380.2364 | -1.0852 | 386.58 | 378.53 | 1.5953 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.08 |  | 857.6137 | -1.1116 | 887.1 | 866.765 | 2.4691 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.34 |  | 191.2369 | -2.0377 | 201.61 | 194.19 | 0.443 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 398.08 |  | 402.4422 | -1.0839 | 411.65 | 400.635 | 3.8158 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.22 |  | 45.8669 | -1.4104 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.995 |  | 25.377 | -1.5055 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.74 |  | 752.5293 | -0.2378 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.09 |  | 296.1931 | -0.3724 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.12 |  | 126.6749 | -0.438 | 131.36 | 126.665 | 3.9645 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.27 |  | 73.3469 | -1.4682 | 75.54 | 73.985 | 1.1761 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.67 |  | 293.7639 | -1.734 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 394.79 |  | 399.4555 | -1.168 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.315 |  | 631.5415 | -0.6692 | 640.25 | 631.005 | 0.1323 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1021.48 |  | 1027.7931 | -0.6142 | 1035.07 | 1021.09 | 0.1155 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 473.39 |  | 474.2414 | -0.1795 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.43 |  | 140.5107 | -0.0574 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.705 |  | 166.5192 | 0.7121 | 169.91 | 165.6 | 3.9593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 274.745 |  | 281.0079 | -2.2287 | 288.48 | 280.67 | 0.5532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 699.21 |  | 708.8126 | -1.3547 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 390.24 |  | 395.3703 | -1.2976 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.51 |  | 101.5101 | -2.9555 | 106.975 | 102.85 | 4.5985 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 316.84 |  | 323.7343 | -2.1296 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.045 |  | 1819.2896 | -1.3876 | 1823.13 | 1796.26 | 0.1851 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.295 |  | 570.428 | -1.7764 | 572.69 | 562.32 | 0.4872 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.22 |  | 323.1048 | -1.5118 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.65 |  | 221.0338 | -0.626 | 222.19 | 218.09 | 0.0728 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.22 |  | 326.8252 | -1.4091 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.36 |  | 287.3186 | -2.4219 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.84 |  | 64.0108 | -1.8291 | 66.19 | 63.93 | 1.4004 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.74 |  | 51.9262 | -2.2843 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.5 |  | 134.9985 | -1.11 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.5 |  | 336.5064 | -2.0821 | 346.26 | 338 | 4.2124 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.915 |  | 515.0427 | 0.3635 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.43 |  | 294.8921 | 0.1824 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.12 |  | 26.8406 | -2.6848 | 28.05 | 27.6 | 0.0766 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.01 |  | 35.528 | -1.4581 | 37.365 | 36.4 | 0.0571 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.96 |  | 21.2362 | -1.3005 | 22.18 | 21.78 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1421 |  | 1466.537 | -3.1051 | 1549.47 | 1482.06 | 3.5186 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 457.45 |  | 474.9688 | -3.6884 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 746.6 |  | 766.4094 | -2.5847 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 253.95 |  | 255.5022 | -0.6075 | 258.07 | 252.62 | 0.0315 | below_vwap | below_vwap |
| META | cloud_ai_capex | 669.905 |  | 671.9973 | -0.3114 | 680.09 | 667.1 | 2.0854 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 257.39 |  | 257.2806 | 0.0425 | 265.96 | 258.1 | 3.8852 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| SKHY | memory_hbm_storage | 156.355 |  | 161.9941 | -3.4811 | 168.11 | 162.41 | 0.1983 | below_opening_15m_low | below_opening_15m_low,below_vwap |
