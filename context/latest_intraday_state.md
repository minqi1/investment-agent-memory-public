# Intraday State

- Generated at: `2026-07-17T03:39:22+08:00`
- Market time ET: `2026-07-16T15:39:23-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 44, 'below_vwap': 3, 'manual_confirm_candidate': 1, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.46 |  | 708.6137 | -0.5862 | 713.55 | 708.25 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 527.07 |  | 532.9467 | -1.1027 | 543.4 | 535.47 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.875 |  | 571.2766 | -0.9455 | 580.31 | 572.21 | 0.0265 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.03 |  | 751.8247 | -0.3717 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.745 |  | 331.4373 | 0.3946 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.745 |  | 331.4373 | 0.3946 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 140.85 |  | 140.5817 | 0.1908 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | TT | data_center_power_cooling | 474.83 |  | 474.2512 | 0.122 | 474.085 | 467.64 | 4.8312 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | ANET | ai_networking_optical | 166.78 |  | 166.6045 | 0.1053 | 169.91 | 165.6 | 4.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GEV | data_center_power_cooling | 1030.26 |  | 1027.2286 | 0.2951 | 1035.07 | 1021.09 | 3.6418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | LIN | industrial_gases | 517.87 |  | 515.5649 | 0.4471 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | APD | industrial_gases | 295.865 |  | 295.145 | 0.244 | 293.89 | 291.35 | 4.012 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ARM | ai_accelerator | 258.2 |  | 257.2297 | 0.3772 | 265.96 | 258.1 | 1.3555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | IWM | market_regime | 294.755 |  | 295.9316 | -0.3976 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | VRT | data_center_power_cooling | 293.2 |  | 292.9751 | 0.0768 | 300.385 | 293.64 | 4.3759 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 12 | MSFT | cloud_ai_capex | 399.89 |  | 400.0957 | -0.0514 | 398.69 | 392.2 | 0.4376 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 527.07 |  | 532.9467 | -1.1027 | 543.4 | 535.47 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 406.09 |  | 408.4269 | -0.5722 | 414.385 | 406.61 | 0.0369 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 704.46 |  | 708.6137 | -0.5862 | 713.55 | 708.25 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | AVGO | custom_silicon_networking | 375.915 |  | 379.2738 | -0.8856 | 386.58 | 378.53 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.39 |  | 207.3057 | -0.4417 | 211.03 | 207.49 | 0.1357 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1792.75 |  | 1813.0471 | -1.1195 | 1823.13 | 1796.26 | 0.0736 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | KLAC | semiconductor_equipment | 217.47 |  | 220.4987 | -1.3736 | 222.19 | 218.09 | 0.0552 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 565.875 |  | 571.2766 | -0.9455 | 580.31 | 572.21 | 0.0265 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.745 |  | 331.4373 | 0.3946 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 399.89 |  | 400.0957 | -0.0514 | 398.69 | 392.2 | 0.4376 | below_vwap | below_vwap,spread_too_wide |
| 3 | TT | data_center_power_cooling | 474.83 |  | 474.2512 | 0.122 | 474.085 | 467.64 | 4.8312 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | JCI | data_center_power_cooling | 140.85 |  | 140.5817 | 0.1908 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 517.87 |  | 515.5649 | 0.4471 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 295.865 |  | 295.145 | 0.244 | 293.89 | 291.35 | 4.012 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | IWM | market_regime | 294.755 |  | 295.9316 | -0.3976 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 166.78 |  | 166.6045 | 0.1053 | 169.91 | 165.6 | 4.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | GEV | data_center_power_cooling | 1030.26 |  | 1027.2286 | 0.2951 | 1035.07 | 1021.09 | 3.6418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ARM | ai_accelerator | 258.2 |  | 257.2297 | 0.3772 | 265.96 | 258.1 | 1.3555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | VRT | data_center_power_cooling | 293.2 |  | 292.9751 | 0.0768 | 300.385 | 293.64 | 4.3759 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 13 | SOXX | semiconductor_index | 527.07 |  | 532.9467 | -1.1027 | 543.4 | 535.47 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | TSM | foundry | 406.09 |  | 408.4269 | -0.5722 | 414.385 | 406.61 | 0.0369 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | CIEN | ai_networking_optical | 389.44 |  | 393.0588 | -0.9207 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 704.46 |  | 708.6137 | -0.5862 | 713.55 | 708.25 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 375.915 |  | 379.2738 | -0.8856 | 386.58 | 378.53 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | MU | memory_hbm_storage | 848.26 |  | 855.5719 | -0.8546 | 887.1 | 866.765 | 0.5069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | NVDA | ai_accelerator | 206.39 |  | 207.3057 | -0.4417 | 211.03 | 207.49 | 0.1357 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AMD | ai_accelerator | 497.355 |  | 502.4739 | -1.0187 | 518.33 | 507.62 | 1.2184 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.46 |  | 708.6137 | -0.5862 | 713.55 | 708.25 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.245 |  | 71.6217 | -1.9222 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.39 |  | 207.3057 | -0.4417 | 211.03 | 207.49 | 0.1357 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.89 |  | 400.0957 | -0.0514 | 398.69 | 392.2 | 0.4376 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 332.745 |  | 331.4373 | 0.3946 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 355.065 |  | 365.5794 | -2.8761 | 375.18 | 369.2 | 0.0366 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 497.355 |  | 502.4739 | -1.0187 | 518.33 | 507.62 | 1.2184 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.09 |  | 408.4269 | -0.5722 | 414.385 | 406.61 | 0.0369 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 527.07 |  | 532.9467 | -1.1027 | 543.4 | 535.47 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.875 |  | 571.2766 | -0.9455 | 580.31 | 572.21 | 0.0265 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.915 |  | 379.2738 | -0.8856 | 386.58 | 378.53 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 848.26 |  | 855.5719 | -0.8546 | 887.1 | 866.765 | 0.5069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.94 |  | 190.5004 | -1.344 | 201.61 | 194.19 | 1.1865 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 395.11 |  | 401.1942 | -1.5165 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.47 |  | 45.7205 | -0.5479 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.915 |  | 25.2691 | -1.4013 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.03 |  | 751.8247 | -0.3717 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.755 |  | 295.9316 | -0.3976 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.07 |  | 126.3143 | -1.7768 | 131.36 | 126.665 | 0.2015 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.68 |  | 73.2865 | -0.8275 | 75.54 | 73.985 | 0.0826 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 293.2 |  | 292.9751 | 0.0768 | 300.385 | 293.64 | 4.3759 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ETN | data_center_power_cooling | 396.615 |  | 399.1276 | -0.6295 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.38 |  | 631.0117 | -0.2586 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.26 |  | 1027.2286 | 0.2951 | 1035.07 | 1021.09 | 3.6418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 474.83 |  | 474.2512 | 0.122 | 474.085 | 467.64 | 4.8312 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.85 |  | 140.5817 | 0.1908 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.78 |  | 166.6045 | 0.1053 | 169.91 | 165.6 | 4.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.3 |  | 280.2887 | -1.4231 | 288.48 | 280.67 | 1.35 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.83 |  | 707.041 | -0.737 | 737.175 | 720.21 | 3.2031 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 389.44 |  | 393.0588 | -0.9207 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.04 |  | 100.9612 | -0.9125 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.745 |  | 322.6221 | -1.8217 | 337.59 | 326.16 | 1.0734 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1792.75 |  | 1813.0471 | -1.1195 | 1823.13 | 1796.26 | 0.0736 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 562.21 |  | 568.778 | -1.1548 | 572.69 | 562.32 | 2.9384 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.39 |  | 322.1038 | -1.4634 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 217.47 |  | 220.4987 | -1.3736 | 222.19 | 218.09 | 0.0552 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 319.32 |  | 325.4838 | -1.8937 | 332.49 | 326.685 | 0.8675 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.32 |  | 285.1154 | -1.6819 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.83 |  | 63.7755 | -1.4826 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.7 |  | 51.7014 | -1.9368 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 132.955 |  | 134.3954 | -1.0717 | 138.07 | 133.73 | 0.1504 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 328.6 |  | 333.6098 | -1.5017 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.87 |  | 515.5649 | 0.4471 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.865 |  | 295.145 | 0.244 | 293.89 | 291.35 | 4.012 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.155 |  | 26.7485 | -2.2189 | 28.05 | 27.6 | 0.0765 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.035 |  | 35.4918 | -1.2871 | 37.365 | 36.4 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.985 |  | 21.1881 | -0.9587 | 22.18 | 21.78 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1417.75 |  | 1451.2667 | -2.3095 | 1549.47 | 1482.06 | 3.2446 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 463.55 |  | 471.964 | -1.7828 | 498.04 | 480.14 | 0.2416 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 745.87 |  | 761.0985 | -2.0009 | 797.155 | 768.7 | 0.2226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 251.97 |  | 254.6911 | -1.0684 | 258.07 | 252.62 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 663.7 |  | 670.3315 | -0.9893 | 680.09 | 667.1 | 3.4654 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.2 |  | 257.2297 | 0.3772 | 265.96 | 258.1 | 1.3555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 156.71 |  | 161.1484 | -2.7542 | 168.11 | 162.41 | 0.4339 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
