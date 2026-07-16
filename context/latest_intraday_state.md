# Intraday State

- Generated at: `2026-07-17T01:47:50+08:00`
- Market time ET: `2026-07-16T13:47:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'watch_only': 2, 'price_stale_or_missing': 1, 'below_vwap': 5, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.48 |  | 709.7569 | -0.4617 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.05 |  | 534.7086 | -1.6193 | 543.4 | 535.47 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.24 |  | 572.7047 | -1.3034 | 580.31 | 572.21 | 0.0336 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.43 |  | 752.6787 | -0.1659 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.81 |  | 398.3968 | 1.1077 | 398.69 | 392.2 | 0.2681 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.065 |  | 330.4824 | 0.4789 | 328.98 | 326.885 | 0.0512 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.55 |  | 255.5428 | 0.0028 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 372.01 |  | 371.8439 | 0.0447 | 375.18 | 369.2 | 0.1828 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 332.065 |  | 330.4824 | 0.4789 | 328.98 | 326.885 | 0.0512 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 516.34 |  | 514.9771 | 0.2646 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | JCI | data_center_power_cooling | 140.645 |  | 140.5478 | 0.0691 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MSFT | cloud_ai_capex | 402.81 |  | 398.3968 | 1.1077 | 398.69 | 392.2 | 0.2681 | buy_precheck_manual_confirm | none |
| 7 | TT | data_center_power_cooling | 475.23 |  | 474.4109 | 0.1727 | 474.085 | 467.64 | 5.0334 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 166.82 |  | 166.4828 | 0.2026 | 169.91 | 165.6 | 4.5558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APD | industrial_gases | 295.29 |  | 294.879 | 0.1394 | 293.89 | 291.35 | 4.4295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SPY | market_regime | 751.43 |  | 752.6787 | -0.1659 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.285 |  | 296.3333 | -0.3538 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | META | cloud_ai_capex | 668.605 |  | 672.4812 | -0.5764 | 680.09 | 667.1 | 0.0404 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 218.77 |  | 221.197 | -1.0972 | 222.19 | 218.09 | 0.6399 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 526.05 |  | 534.7086 | -1.6193 | 543.4 | 535.47 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 403.91 |  | 409.7146 | -1.4168 | 414.385 | 406.61 | 0.0545 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | QQQ | market_regime | 706.48 |  | 709.7569 | -0.4617 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | NVDA | ai_accelerator | 206.41 |  | 207.4332 | -0.4933 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1794.17 |  | 1820.7776 | -1.4613 | 1823.13 | 1796.26 | 0.0981 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 565.24 |  | 572.7047 | -1.3034 | 580.31 | 572.21 | 0.0336 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.81 |  | 398.3968 | 1.1077 | 398.69 | 392.2 | 0.2681 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 332.065 |  | 330.4824 | 0.4789 | 328.98 | 326.885 | 0.0512 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.23 |  | 474.4109 | 0.1727 | 474.085 | 467.64 | 5.0334 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 516.34 |  | 514.9771 | 0.2646 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.29 |  | 294.879 | 0.1394 | 293.89 | 291.35 | 4.4295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GOOGL | cloud_ai_capex | 372.01 |  | 371.8439 | 0.0447 | 375.18 | 369.2 | 0.1828 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 255.55 |  | 255.5428 | 0.0028 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 218.77 |  | 221.197 | -1.0972 | 222.19 | 218.09 | 0.6399 | below_vwap | below_vwap,spread_too_wide |
| 9 | SPY | market_regime | 751.43 |  | 752.6787 | -0.1659 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.285 |  | 296.3333 | -0.3538 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | META | cloud_ai_capex | 668.605 |  | 672.4812 | -0.5764 | 680.09 | 667.1 | 0.0404 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 166.82 |  | 166.4828 | 0.2026 | 169.91 | 165.6 | 4.5558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | JCI | data_center_power_cooling | 140.645 |  | 140.5478 | 0.0691 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SOXX | semiconductor_index | 526.05 |  | 534.7086 | -1.6193 | 543.4 | 535.47 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 403.91 |  | 409.7146 | -1.4168 | 414.385 | 406.61 | 0.0545 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 389.76 |  | 395.8214 | -1.5314 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 706.48 |  | 709.7569 | -0.4617 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 375.965 |  | 380.6094 | -1.2203 | 386.58 | 378.53 | 1.2634 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 841.21 |  | 858.5603 | -2.0209 | 887.1 | 866.765 | 0.1902 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.48 |  | 709.7569 | -0.4617 | 713.55 | 708.25 | 0.0099 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.88 |  | 71.9468 | -1.4828 | 73.09 | 71.45 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.41 |  | 207.4332 | -0.4933 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.81 |  | 398.3968 | 1.1077 | 398.69 | 392.2 | 0.2681 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.065 |  | 330.4824 | 0.4789 | 328.98 | 326.885 | 0.0512 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.01 |  | 371.8439 | 0.0447 | 375.18 | 369.2 | 0.1828 | watch_only | none |
| AMD | ai_accelerator | 492.72 |  | 505.7732 | -2.5808 | 518.33 | 507.62 | 1.7089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 403.91 |  | 409.7146 | -1.4168 | 414.385 | 406.61 | 0.0545 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.05 |  | 534.7086 | -1.6193 | 543.4 | 535.47 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.24 |  | 572.7047 | -1.3034 | 580.31 | 572.21 | 0.0336 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.965 |  | 380.6094 | -1.2203 | 386.58 | 378.53 | 1.2634 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 841.21 |  | 858.5603 | -2.0209 | 887.1 | 866.765 | 0.1902 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 186.74 |  | 191.656 | -2.565 | 201.61 | 194.19 | 1.7297 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 397.01 |  | 403.0261 | -1.4927 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.14 |  | 45.9392 | -1.7397 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.855 |  | 25.4212 | -2.2274 | 26.71 | 25.74 | 0.0402 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.43 |  | 752.6787 | -0.1659 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.285 |  | 296.3333 | -0.3538 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.91 |  | 126.7215 | -0.6404 | 131.36 | 126.665 | 3.1769 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.445 |  | 73.4509 | -1.3695 | 75.54 | 73.985 | 1.1457 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 288.565 |  | 294.2441 | -1.9301 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.185 |  | 399.6152 | -1.1086 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.695 |  | 631.848 | -0.8155 | 640.25 | 631.005 | 4.5907 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1019.785 |  | 1028.457 | -0.8432 | 1035.07 | 1021.09 | 4.6314 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.23 |  | 474.4109 | 0.1727 | 474.085 | 467.64 | 5.0334 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.645 |  | 140.5478 | 0.0691 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.82 |  | 166.4828 | 0.2026 | 169.91 | 165.6 | 4.5558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.68 |  | 281.4621 | -2.0543 | 288.48 | 280.67 | 2.1764 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 696.1 |  | 709.8927 | -1.9429 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 389.76 |  | 395.8214 | -1.5314 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.24 |  | 101.683 | -3.386 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 315 |  | 324.0353 | -2.7884 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.17 |  | 1820.7776 | -1.4613 | 1823.13 | 1796.26 | 0.0981 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.53 |  | 571.7792 | -1.7925 | 572.69 | 562.32 | 0.3312 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 317.235 |  | 324.4241 | -2.216 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.77 |  | 221.197 | -1.0972 | 222.19 | 218.09 | 0.6399 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 320.6 |  | 327.1092 | -1.9899 | 332.49 | 326.685 | 0.2308 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ONTO | semiconductor_test_packaging | 280.615 |  | 288.3255 | -2.6742 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.495 |  | 64.1948 | -2.6478 | 66.19 | 63.93 | 2.1762 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.91 |  | 52.1662 | -2.4081 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.42 |  | 135.0499 | -1.2069 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.45 |  | 337.8392 | -2.1872 | 346.26 | 338 | 4.6089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.34 |  | 514.9771 | 0.2646 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.29 |  | 294.879 | 0.1394 | 293.89 | 291.35 | 4.4295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.035 |  | 26.9528 | -3.4052 | 28.05 | 27.6 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.56 |  | 35.5944 | -2.9059 | 37.365 | 36.4 | 0.0579 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.79 |  | 21.2644 | -2.231 | 22.18 | 21.78 | 0.0481 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1413.52 |  | 1470.293 | -3.8613 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 455.67 |  | 475.9878 | -4.2686 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 745.27 |  | 767.4589 | -2.8912 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.55 |  | 255.5428 | 0.0028 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| META | cloud_ai_capex | 668.605 |  | 672.4812 | -0.5764 | 680.09 | 667.1 | 0.0404 | below_vwap | below_vwap |
| ARM | ai_accelerator | 254.81 |  | 257.3457 | -0.9853 | 265.96 | 258.1 | 2.0918 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 154.17 |  | 162.3693 | -5.0498 | 168.11 | 162.41 | 0.7848 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
