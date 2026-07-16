# Intraday State

- Generated at: `2026-07-17T03:35:23+08:00`
- Market time ET: `2026-07-16T15:35:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 44, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 3, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.26 |  | 708.7079 | -0.6276 | 713.55 | 708.25 | 0.0469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.52 |  | 533.1215 | -1.0507 | 543.4 | 535.47 | 0.0777 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.07 |  | 571.3359 | -0.9217 | 580.31 | 572.21 | 0.0371 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.68 |  | 751.8766 | -0.4252 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.465 |  | 400.0943 | 0.0926 | 398.69 | 392.2 | 0.0375 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.6 |  | 331.4189 | 0.3564 | 328.98 | 326.885 | 0.003 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.465 |  | 400.0943 | 0.0926 | 398.69 | 392.2 | 0.0375 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.6 |  | 331.4189 | 0.3564 | 328.98 | 326.885 | 0.003 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.76 |  | 140.5791 | 0.1287 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.87 |  | 295.1368 | 0.2484 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 474.32 |  | 474.2392 | 0.017 | 474.085 | 467.64 | 4.8406 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 166.74 |  | 166.6035 | 0.0819 | 169.91 | 165.6 | 4.7199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | GEV | data_center_power_cooling | 1030.01 |  | 1027.2096 | 0.2726 | 1035.07 | 1021.09 | 3.665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | LIN | industrial_gases | 517.9 |  | 515.5272 | 0.4603 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ARM | ai_accelerator | 257.36 |  | 257.2268 | 0.0518 | 265.96 | 258.1 | 3.8856 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 11 | AMAT | semiconductor_equipment | 562.54 |  | 568.8536 | -1.1099 | 572.69 | 562.32 | 0.9617 | below_vwap | below_vwap,spread_too_wide |
| 12 | KLAC | semiconductor_equipment | 218.12 |  | 220.6298 | -1.1376 | 222.19 | 218.09 | 1.3112 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 527.52 |  | 533.1215 | -1.0507 | 543.4 | 535.47 | 0.0777 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 406.08 |  | 408.4779 | -0.587 | 414.385 | 406.61 | 0.0788 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 704.26 |  | 708.7079 | -0.6276 | 713.55 | 708.25 | 0.0469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | NVDA | ai_accelerator | 206.54 |  | 207.3156 | -0.3741 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | ASML | semiconductor_equipment | 1790.59 |  | 1813.7287 | -1.2758 | 1823.13 | 1796.26 | 0.1262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SMH | semiconductor_index | 566.07 |  | 571.3359 | -0.9217 | 580.31 | 572.21 | 0.0371 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SPY | market_regime | 748.68 |  | 751.8766 | -0.4252 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | IWM | market_regime | 294.51 |  | 295.953 | -0.4876 | 296.28 | 294.65 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.465 |  | 400.0943 | 0.0926 | 398.69 | 392.2 | 0.0375 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.6 |  | 331.4189 | 0.3564 | 328.98 | 326.885 | 0.003 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.32 |  | 474.2392 | 0.017 | 474.085 | 467.64 | 4.8406 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 517.9 |  | 515.5272 | 0.4603 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.87 |  | 295.1368 | 0.2484 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | AMAT | semiconductor_equipment | 562.54 |  | 568.8536 | -1.1099 | 572.69 | 562.32 | 0.9617 | below_vwap | below_vwap,spread_too_wide |
| 7 | KLAC | semiconductor_equipment | 218.12 |  | 220.6298 | -1.1376 | 222.19 | 218.09 | 1.3112 | below_vwap | below_vwap,spread_too_wide |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 166.74 |  | 166.6035 | 0.0819 | 169.91 | 165.6 | 4.7199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | JCI | data_center_power_cooling | 140.76 |  | 140.5791 | 0.1287 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | GEV | data_center_power_cooling | 1030.01 |  | 1027.2096 | 0.2726 | 1035.07 | 1021.09 | 3.665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ARM | ai_accelerator | 257.36 |  | 257.2268 | 0.0518 | 265.96 | 258.1 | 3.8856 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 13 | SOXX | semiconductor_index | 527.52 |  | 533.1215 | -1.0507 | 543.4 | 535.47 | 0.0777 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 406.08 |  | 408.4779 | -0.587 | 414.385 | 406.61 | 0.0788 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | CIEN | ai_networking_optical | 390.5 |  | 393.1527 | -0.6747 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 704.26 |  | 708.7079 | -0.6276 | 713.55 | 708.25 | 0.0469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 376.11 |  | 379.3266 | -0.848 | 386.58 | 378.53 | 0.2739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | MU | memory_hbm_storage | 847.02 |  | 855.6528 | -1.0089 | 887.1 | 866.765 | 1.1216 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 291.73 |  | 292.9736 | -0.4245 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 20 | NVDA | ai_accelerator | 206.54 |  | 207.3156 | -0.3741 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.26 |  | 708.7079 | -0.6276 | 713.55 | 708.25 | 0.0469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.22 |  | 71.6371 | -1.9782 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.54 |  | 207.3156 | -0.3741 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.465 |  | 400.0943 | 0.0926 | 398.69 | 392.2 | 0.0375 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.6 |  | 331.4189 | 0.3564 | 328.98 | 326.885 | 0.003 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 354.44 |  | 365.7464 | -3.0913 | 375.18 | 369.2 | 0.2624 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 497.42 |  | 502.5579 | -1.0223 | 518.33 | 507.62 | 1.3108 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.08 |  | 408.4779 | -0.587 | 414.385 | 406.61 | 0.0788 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.52 |  | 533.1215 | -1.0507 | 543.4 | 535.47 | 0.0777 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.07 |  | 571.3359 | -0.9217 | 580.31 | 572.21 | 0.0371 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.11 |  | 379.3266 | -0.848 | 386.58 | 378.53 | 0.2739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 847.02 |  | 855.6528 | -1.0089 | 887.1 | 866.765 | 1.1216 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.94 |  | 190.5276 | -1.3581 | 201.61 | 194.19 | 0.4523 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 394.8 |  | 401.3034 | -1.6206 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.33 |  | 45.7241 | -0.8618 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.935 |  | 25.2762 | -1.3498 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.68 |  | 751.8766 | -0.4252 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.51 |  | 295.953 | -0.4876 | 296.28 | 294.65 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.2 |  | 126.3636 | -1.7122 | 131.36 | 126.665 | 0.0644 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.86 |  | 73.2912 | -0.5884 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 291.73 |  | 292.9736 | -0.4245 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 396.4 |  | 399.1412 | -0.6868 | 406.24 | 399.495 | 0.2018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 628.87 |  | 631.0371 | -0.3434 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.01 |  | 1027.2096 | 0.2726 | 1035.07 | 1021.09 | 3.665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 474.32 |  | 474.2392 | 0.017 | 474.085 | 467.64 | 4.8406 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.76 |  | 140.5791 | 0.1287 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.74 |  | 166.6035 | 0.0819 | 169.91 | 165.6 | 4.7199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.43 |  | 280.3367 | -1.7503 | 288.48 | 280.67 | 1.3542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.21 |  | 707.1287 | -0.837 | 737.175 | 720.21 | 4.2783 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.5 |  | 393.1527 | -0.6747 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.83 |  | 100.9882 | -1.1468 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.02 |  | 322.6688 | -1.7507 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1790.59 |  | 1813.7287 | -1.2758 | 1823.13 | 1796.26 | 0.1262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 562.54 |  | 568.8536 | -1.1099 | 572.69 | 562.32 | 0.9617 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.15 |  | 322.2804 | -1.2816 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.12 |  | 220.6298 | -1.1376 | 222.19 | 218.09 | 1.3112 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 320.05 |  | 325.6763 | -1.7276 | 332.49 | 326.685 | 0.4999 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.86 |  | 285.1498 | -1.5044 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.885 |  | 63.797 | -1.4295 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.97 |  | 51.7054 | -1.4222 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.195 |  | 134.4578 | -0.9392 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.66 |  | 333.7498 | -1.2254 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.9 |  | 515.5272 | 0.4603 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.87 |  | 295.1368 | 0.2484 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.305 |  | 26.7515 | -1.6691 | 28.05 | 27.6 | 0.038 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.215 |  | 35.4962 | -0.7922 | 37.365 | 36.4 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.025 |  | 21.1896 | -0.7768 | 22.18 | 21.78 | 0.0951 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1410.45 |  | 1452.0284 | -2.8635 | 1549.47 | 1482.06 | 0.4828 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 463.1 |  | 472.0761 | -1.9014 | 498.04 | 480.14 | 0.7018 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 743.5 |  | 761.4372 | -2.3557 | 797.155 | 768.7 | 0.5488 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 251.645 |  | 254.7308 | -1.2114 | 258.07 | 252.62 | 0.9577 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| META | cloud_ai_capex | 663.455 |  | 670.4219 | -1.0392 | 680.09 | 667.1 | 0.425 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 257.36 |  | 257.2268 | 0.0518 | 265.96 | 258.1 | 3.8856 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| SKHY | memory_hbm_storage | 156.13 |  | 161.2154 | -3.1544 | 168.11 | 162.41 | 0.2178 | below_opening_15m_low | below_opening_15m_low,below_vwap |
