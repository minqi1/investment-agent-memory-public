# Intraday State

- Generated at: `2026-07-17T01:43:51+08:00`
- Market time ET: `2026-07-16T13:43:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'below_vwap': 8, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.5 |  | 709.7845 | -0.4627 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.53 |  | 534.7994 | -1.5463 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.55 |  | 572.9273 | -1.2877 | 580.31 | 572.21 | 0.0248 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.27 |  | 752.6962 | -0.1895 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.7 |  | 398.3354 | 1.0957 | 398.69 | 392.2 | 0.1987 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.695 |  | 330.4447 | 0.681 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 332.695 |  | 330.4447 | 0.681 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.05 |  | 514.9635 | 0.211 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MSFT | cloud_ai_capex | 402.7 |  | 398.3354 | 1.0957 | 398.69 | 392.2 | 0.1987 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 475.19 |  | 474.4058 | 0.1653 | 474.085 | 467.64 | 4.8612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 167.02 |  | 166.4809 | 0.3238 | 169.91 | 165.6 | 3.305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 294.96 |  | 294.8779 | 0.0278 | 293.89 | 291.35 | 4.6616 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SPY | market_regime | 751.27 |  | 752.6962 | -0.1895 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.27 |  | 296.3422 | -0.3618 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | GOOGL | cloud_ai_capex | 371.3 |  | 371.8458 | -0.1468 | 375.18 | 369.2 | 0.0835 | below_vwap | below_vwap |
| 10 | AMZN | cloud_ai_capex | 255.19 |  | 255.5462 | -0.1394 | 258.07 | 252.62 | 0.0196 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 140.54 |  | 140.5454 | -0.0039 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 219.3 |  | 221.2259 | -0.8706 | 222.19 | 218.09 | 0.725 | below_vwap | below_vwap,spread_too_wide |
| 14 | META | cloud_ai_capex | 668.81 |  | 672.5371 | -0.5542 | 680.09 | 667.1 | 2.3325 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 526.53 |  | 534.7994 | -1.5463 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.395 |  | 409.805 | -1.3201 | 414.385 | 406.61 | 0.0272 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 706.5 |  | 709.7845 | -0.4627 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 206.335 |  | 207.4584 | -0.5415 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AMD | ai_accelerator | 492.83 |  | 505.9623 | -2.5955 | 518.33 | 507.62 | 0.1319 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | ASML | semiconductor_equipment | 1795.67 |  | 1821.0053 | -1.3913 | 1823.13 | 1796.26 | 0.0924 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.7 |  | 398.3354 | 1.0957 | 398.69 | 392.2 | 0.1987 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.695 |  | 330.4447 | 0.681 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.19 |  | 474.4058 | 0.1653 | 474.085 | 467.64 | 4.8612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 516.05 |  | 514.9635 | 0.211 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 294.96 |  | 294.8779 | 0.0278 | 293.89 | 291.35 | 4.6616 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | JCI | data_center_power_cooling | 140.54 |  | 140.5454 | -0.0039 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 219.3 |  | 221.2259 | -0.8706 | 222.19 | 218.09 | 0.725 | below_vwap | below_vwap,spread_too_wide |
| 8 | SPY | market_regime | 751.27 |  | 752.6962 | -0.1895 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.27 |  | 296.3422 | -0.3618 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GOOGL | cloud_ai_capex | 371.3 |  | 371.8458 | -0.1468 | 375.18 | 369.2 | 0.0835 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 255.19 |  | 255.5462 | -0.1394 | 258.07 | 252.62 | 0.0196 | below_vwap | below_vwap |
| 13 | META | cloud_ai_capex | 668.81 |  | 672.5371 | -0.5542 | 680.09 | 667.1 | 2.3325 | below_vwap | below_vwap,spread_too_wide |
| 14 | ANET | ai_networking_optical | 167.02 |  | 166.4809 | 0.3238 | 169.91 | 165.6 | 3.305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SOXX | semiconductor_index | 526.53 |  | 534.7994 | -1.5463 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.395 |  | 409.805 | -1.3201 | 414.385 | 406.61 | 0.0272 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 390.45 |  | 395.9085 | -1.3787 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 706.5 |  | 709.7845 | -0.4627 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 376.48 |  | 380.6695 | -1.1006 | 386.58 | 378.53 | 1.5937 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 842.8 |  | 858.7995 | -1.863 | 887.1 | 866.765 | 0.356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.5 |  | 709.7845 | -0.4627 | 713.55 | 708.25 | 0.0057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.91 |  | 71.9588 | -1.4575 | 73.09 | 71.45 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.335 |  | 207.4584 | -0.5415 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.7 |  | 398.3354 | 1.0957 | 398.69 | 392.2 | 0.1987 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.695 |  | 330.4447 | 0.681 | 328.98 | 326.885 | 0.018 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.3 |  | 371.8458 | -0.1468 | 375.18 | 369.2 | 0.0835 | below_vwap | below_vwap |
| AMD | ai_accelerator | 492.83 |  | 505.9623 | -2.5955 | 518.33 | 507.62 | 0.1319 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 404.395 |  | 409.805 | -1.3201 | 414.385 | 406.61 | 0.0272 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.53 |  | 534.7994 | -1.5463 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.55 |  | 572.9273 | -1.2877 | 580.31 | 572.21 | 0.0248 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.48 |  | 380.6695 | -1.1006 | 386.58 | 378.53 | 1.5937 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 842.8 |  | 858.7995 | -1.863 | 887.1 | 866.765 | 0.356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 186.5 |  | 191.7303 | -2.7279 | 201.61 | 194.19 | 0.1555 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 398.2 |  | 403.0987 | -1.2153 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.29 |  | 45.956 | -1.4493 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.93 |  | 25.4329 | -1.9775 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.27 |  | 752.6962 | -0.1895 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 295.27 |  | 296.3422 | -0.3618 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.05 |  | 126.7333 | -0.5392 | 131.36 | 126.665 | 0.1745 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.4 |  | 73.4609 | -1.4442 | 75.54 | 73.985 | 1.2431 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.445 |  | 294.3672 | -2.0118 | 300.385 | 293.64 | 1.2203 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.99 |  | 399.65 | -1.166 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.13 |  | 631.8687 | -0.75 | 640.25 | 631.005 | 4.747 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1019.23 |  | 1028.534 | -0.9046 | 1035.07 | 1021.09 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 475.19 |  | 474.4058 | 0.1653 | 474.085 | 467.64 | 4.8612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.54 |  | 140.5454 | -0.0039 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.02 |  | 166.4809 | 0.3238 | 169.91 | 165.6 | 3.305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.21 |  | 281.5809 | -1.9074 | 288.48 | 280.67 | 1.0391 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 696.93 |  | 710.0915 | -1.8535 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 390.45 |  | 395.9085 | -1.3787 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.695 |  | 101.8144 | -3.0638 | 106.975 | 102.85 | 4.7419 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 315 |  | 324.0353 | -2.7884 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1795.67 |  | 1821.0053 | -1.3913 | 1823.13 | 1796.26 | 0.0924 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.83 |  | 571.9237 | -1.7649 | 572.69 | 562.32 | 1.52 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.78 |  | 324.5278 | -2.0793 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.3 |  | 221.2259 | -0.8706 | 222.19 | 218.09 | 0.725 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 321.38 |  | 327.2057 | -1.7804 | 332.49 | 326.685 | 3.7806 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.82 |  | 288.3839 | -2.6229 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.46 |  | 64.2037 | -2.7159 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.04 |  | 52.175 | -2.1754 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.59 |  | 135.0977 | -1.116 | 138.07 | 133.73 | 4.8731 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 330.44 |  | 337.9544 | -2.2235 | 346.26 | 338 | 4.609 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.05 |  | 514.9635 | 0.211 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 294.96 |  | 294.8779 | 0.0278 | 293.89 | 291.35 | 4.6616 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.08 |  | 26.9592 | -3.2612 | 28.05 | 27.6 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.49 |  | 35.6078 | -3.1392 | 37.365 | 36.4 | 0.058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.765 |  | 21.2709 | -2.3782 | 22.18 | 21.78 | 0.0482 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1418.435 |  | 1471.1255 | -3.5816 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 456.44 |  | 476.1123 | -4.1319 | 498.04 | 480.14 | 3.1351 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 746.75 |  | 767.6413 | -2.7215 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.19 |  | 255.5462 | -0.1394 | 258.07 | 252.62 | 0.0196 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.81 |  | 672.5371 | -0.5542 | 680.09 | 667.1 | 2.3325 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.21 |  | 257.3573 | -0.8344 | 265.96 | 258.1 | 2.2139 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.55 |  | 162.4875 | -4.2696 | 168.11 | 162.41 | 0.4629 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
