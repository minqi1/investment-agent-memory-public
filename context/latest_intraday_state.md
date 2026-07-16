# Intraday State

- Generated at: `2026-07-17T01:39:51+08:00`
- Market time ET: `2026-07-16T13:39:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 2, 'below_vwap': 11, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.465 |  | 709.8316 | -0.3334 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.21 |  | 534.9176 | -1.2539 | 543.4 | 535.47 | 0.0682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.74 |  | 573.0087 | -1.094 | 580.31 | 572.21 | 0.0618 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.88 |  | 752.714 | -0.1108 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.63 |  | 398.2186 | 1.1078 | 398.69 | 392.2 | 0.1763 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.23 |  | 330.3885 | 0.86 | 328.98 | 326.885 | 0.2851 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.38 |  | 474.3816 | 0.2105 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | LIN | industrial_gases | 515.97 |  | 514.9577 | 0.1966 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | APD | industrial_gases | 295.18 |  | 294.8743 | 0.1037 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | MSFT | cloud_ai_capex | 402.63 |  | 398.2186 | 1.1078 | 398.69 | 392.2 | 0.1763 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 333.23 |  | 330.3885 | 0.86 | 328.98 | 326.885 | 0.2851 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 167.52 |  | 166.4759 | 0.6272 | 169.91 | 165.6 | 3.5399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | JCI | data_center_power_cooling | 140.53 |  | 140.5461 | -0.0115 | 140.83 | 139.43 | 0.0498 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1798.975 |  | 1821.166 | -1.2185 | 1823.13 | 1796.26 | 0.1017 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 751.88 |  | 752.714 | -0.1108 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.33 |  | 296.3524 | -0.345 | 296.28 | 294.65 | 0.0135 | below_vwap | below_vwap |
| 11 | GOOGL | cloud_ai_capex | 371.3 |  | 371.8515 | -0.1483 | 375.18 | 369.2 | 0.0162 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 255.54 |  | 255.555 | -0.0059 | 258.07 | 252.62 | 0.0196 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1023.185 |  | 1028.6772 | -0.5339 | 1035.07 | 1021.09 | 0.1984 | below_vwap | below_vwap |
| 15 | ENTG | semiconductor_materials | 133.88 |  | 135.1108 | -0.9109 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 219.665 |  | 221.2596 | -0.7207 | 222.19 | 218.09 | 0.8741 | below_vwap | below_vwap,spread_too_wide |
| 17 | META | cloud_ai_capex | 668.1 |  | 672.6325 | -0.6738 | 680.09 | 667.1 | 2.2302 | below_vwap | below_vwap,spread_too_wide |
| 18 | SOXX | semiconductor_index | 528.21 |  | 534.9176 | -1.2539 | 543.4 | 535.47 | 0.0682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | TSM | foundry | 405.11 |  | 409.8517 | -1.1569 | 414.385 | 406.61 | 0.0296 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 707.465 |  | 709.8316 | -0.3334 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.63 |  | 398.2186 | 1.1078 | 398.69 | 392.2 | 0.1763 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.23 |  | 330.3885 | 0.86 | 328.98 | 326.885 | 0.2851 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.38 |  | 474.3816 | 0.2105 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 515.97 |  | 514.9577 | 0.1966 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.18 |  | 294.8743 | 0.1037 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.53 |  | 140.5461 | -0.0115 | 140.83 | 139.43 | 0.0498 | below_vwap | below_vwap |
| 7 | GEV | data_center_power_cooling | 1023.185 |  | 1028.6772 | -0.5339 | 1035.07 | 1021.09 | 0.1984 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1798.975 |  | 1821.166 | -1.2185 | 1823.13 | 1796.26 | 0.1017 | below_vwap | below_vwap |
| 9 | KLAC | semiconductor_equipment | 219.665 |  | 221.2596 | -0.7207 | 222.19 | 218.09 | 0.8741 | below_vwap | below_vwap,spread_too_wide |
| 10 | SPY | market_regime | 751.88 |  | 752.714 | -0.1108 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.33 |  | 296.3524 | -0.345 | 296.28 | 294.65 | 0.0135 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 133.88 |  | 135.1108 | -0.9109 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 371.3 |  | 371.8515 | -0.1483 | 375.18 | 369.2 | 0.0162 | below_vwap | below_vwap |
| 15 | AMZN | cloud_ai_capex | 255.54 |  | 255.555 | -0.0059 | 258.07 | 252.62 | 0.0196 | below_vwap | below_vwap |
| 16 | META | cloud_ai_capex | 668.1 |  | 672.6325 | -0.6738 | 680.09 | 667.1 | 2.2302 | below_vwap | below_vwap,spread_too_wide |
| 17 | ANET | ai_networking_optical | 167.52 |  | 166.4759 | 0.6272 | 169.91 | 165.6 | 3.5399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SOXX | semiconductor_index | 528.21 |  | 534.9176 | -1.2539 | 543.4 | 535.47 | 0.0682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | TSM | foundry | 405.11 |  | 409.8517 | -1.1569 | 414.385 | 406.61 | 0.0296 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | CIEN | ai_networking_optical | 391.17 |  | 395.9884 | -1.2168 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.465 |  | 709.8316 | -0.3334 | 713.55 | 708.25 | 0.017 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.25 |  | 71.9747 | -1.0069 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.855 |  | 207.4713 | -0.2971 | 211.03 | 207.49 | 0.0048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.63 |  | 398.2186 | 1.1078 | 398.69 | 392.2 | 0.1763 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.23 |  | 330.3885 | 0.86 | 328.98 | 326.885 | 0.2851 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.3 |  | 371.8515 | -0.1483 | 375.18 | 369.2 | 0.0162 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.86 |  | 506.0876 | -2.0209 | 518.33 | 507.62 | 0.238 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 405.11 |  | 409.8517 | -1.1569 | 414.385 | 406.61 | 0.0296 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.21 |  | 534.9176 | -1.2539 | 543.4 | 535.47 | 0.0682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.74 |  | 573.0087 | -1.094 | 580.31 | 572.21 | 0.0618 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.34 |  | 380.7303 | -0.8905 | 386.58 | 378.53 | 0.4717 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.51 |  | 859.0244 | -1.224 | 887.1 | 866.765 | 1.2964 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.29 |  | 191.8337 | -2.3686 | 201.61 | 194.19 | 0.2243 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 399.94 |  | 403.1395 | -0.7936 | 411.65 | 400.635 | 4.5032 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.4 |  | 45.9638 | -1.2265 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.045 |  | 25.4405 | -1.5545 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.88 |  | 752.714 | -0.1108 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.33 |  | 296.3524 | -0.345 | 296.28 | 294.65 | 0.0135 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.44 |  | 126.7403 | -0.237 | 131.36 | 126.665 | 0.3322 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.555 |  | 73.4731 | -1.2495 | 75.54 | 73.985 | 0.0689 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 289.895 |  | 294.4565 | -1.5491 | 300.385 | 293.64 | 1.5764 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.95 |  | 399.6732 | -1.1818 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.84 |  | 631.9159 | -0.645 | 640.25 | 631.005 | 4.8484 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1023.185 |  | 1028.6772 | -0.5339 | 1035.07 | 1021.09 | 0.1984 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 475.38 |  | 474.3816 | 0.2105 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.53 |  | 140.5461 | -0.0115 | 140.83 | 139.43 | 0.0498 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 167.52 |  | 166.4759 | 0.6272 | 169.91 | 165.6 | 3.5399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.42 |  | 281.6303 | -1.495 | 288.48 | 280.67 | 1.0814 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.465 |  | 710.1919 | -1.792 | 737.175 | 720.21 | 0.2581 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 391.17 |  | 395.9884 | -1.2168 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.18 |  | 101.8934 | -2.6629 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 315.72 |  | 324.049 | -2.5703 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1798.975 |  | 1821.166 | -1.2185 | 1823.13 | 1796.26 | 0.1017 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 562.24 |  | 572.0376 | -1.7128 | 572.69 | 562.32 | 1.8586 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.465 |  | 324.6127 | -1.8939 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.665 |  | 221.2596 | -0.7207 | 222.19 | 218.09 | 0.8741 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.81 |  | 327.2655 | -1.3614 | 332.49 | 326.685 | 0.127 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ONTO | semiconductor_test_packaging | 281.68 |  | 288.4548 | -2.3486 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.58 |  | 64.2311 | -2.5706 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.04 |  | 52.175 | -2.1754 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.88 |  | 135.1108 | -0.9109 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.81 |  | 338.0138 | -2.1312 | 346.26 | 338 | 4.6341 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.97 |  | 514.9577 | 0.1966 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.18 |  | 294.8743 | 0.1037 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.09 |  | 26.9654 | -3.2465 | 28.05 | 27.6 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.61 |  | 35.6158 | -2.824 | 37.365 | 36.4 | 0.0578 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.83 |  | 21.274 | -2.0872 | 22.18 | 21.78 | 0.096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1432.385 |  | 1472.1023 | -2.698 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 457.51 |  | 476.2515 | -3.9352 | 498.04 | 480.14 | 0.7475 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 747.95 |  | 767.7665 | -2.5811 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.54 |  | 255.555 | -0.0059 | 258.07 | 252.62 | 0.0196 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.1 |  | 672.6325 | -0.6738 | 680.09 | 667.1 | 2.2302 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.705 |  | 257.3743 | -0.6486 | 265.96 | 258.1 | 3.0504 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.73 |  | 162.5271 | -3.5668 | 168.11 | 162.41 | 1.4356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
