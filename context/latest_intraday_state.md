# Intraday State

- Generated at: `2026-07-17T03:03:28+08:00`
- Market time ET: `2026-07-16T15:03:29-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 39, 'watch_only': 1, 'manual_confirm_candidate': 2, 'below_vwap': 9, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.41 |  | 709.2747 | -0.4039 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.16 |  | 533.781 | -0.8657 | 543.4 | 535.47 | 0.0416 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.12 |  | 571.6598 | -0.6192 | 580.31 | 572.21 | 0.0704 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.615 |  | 752.2546 | -0.218 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 405.69 |  | 399.7756 | 1.4794 | 398.69 | 392.2 | 0.0394 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.29 |  | 330.8314 | 0.7432 | 328.98 | 326.885 | 0.099 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 207.51 |  | 207.3471 | 0.0785 | 211.03 | 207.49 | 0.0193 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 333.29 |  | 330.8314 | 0.7432 | 328.98 | 326.885 | 0.099 | buy_precheck_manual_confirm | none |
| 3 | ANET | ai_networking_optical | 166.75 |  | 166.5868 | 0.098 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | JCI | data_center_power_cooling | 140.7 |  | 140.5221 | 0.1266 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 405.69 |  | 399.7756 | 1.4794 | 398.69 | 392.2 | 0.0394 | buy_precheck_manual_confirm | none |
| 6 | LIN | industrial_gases | 518.245 |  | 515.2423 | 0.5828 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | APD | industrial_gases | 296.065 |  | 295.0014 | 0.3605 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | IREN | high_beta_ai_infrastructure | 35.575 |  | 35.5 | 0.2113 | 37.365 | 36.4 | 0.0281 | below_opening_15m_low | below_opening_15m_low |
| 9 | TT | data_center_power_cooling | 473.71 |  | 474.1176 | -0.086 | 474.085 | 467.64 | 0.133 | below_vwap | below_vwap |
| 10 | ASML | semiconductor_equipment | 1796.84 |  | 1817.6779 | -1.1464 | 1823.13 | 1796.26 | 0.1085 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.14 |  | 296.1152 | -0.3293 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | TSM | foundry | 407.3 |  | 408.7234 | -0.3483 | 414.385 | 406.61 | 0.221 | below_vwap | below_vwap |
| 14 | AMZN | cloud_ai_capex | 253.19 |  | 255.1015 | -0.7493 | 258.07 | 252.62 | 0.2054 | below_vwap | below_vwap |
| 15 | GEV | data_center_power_cooling | 1023.76 |  | 1027.1505 | -0.3301 | 1035.07 | 1021.09 | 4.4942 | below_vwap | below_vwap,spread_too_wide |
| 16 | KLAC | semiconductor_equipment | 219.67 |  | 220.9336 | -0.5719 | 222.19 | 218.09 | 4.6297 | below_vwap | below_vwap,spread_too_wide |
| 17 | META | cloud_ai_capex | 667.595 |  | 671.2799 | -0.5489 | 680.09 | 667.1 | 0.4044 | below_vwap | below_vwap,spread_too_wide |
| 18 | SOXX | semiconductor_index | 529.16 |  | 533.781 | -0.8657 | 543.4 | 535.47 | 0.0416 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | QQQ | market_regime | 706.41 |  | 709.2747 | -0.4039 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 568.12 |  | 571.6598 | -0.6192 | 580.31 | 572.21 | 0.0704 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 405.69 |  | 399.7756 | 1.4794 | 398.69 | 392.2 | 0.0394 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.29 |  | 330.8314 | 0.7432 | 328.98 | 326.885 | 0.099 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 518.245 |  | 515.2423 | 0.5828 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.065 |  | 295.0014 | 0.3605 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | NVDA | ai_accelerator | 207.51 |  | 207.3471 | 0.0785 | 211.03 | 207.49 | 0.0193 | watch_only | none |
| 6 | TSM | foundry | 407.3 |  | 408.7234 | -0.3483 | 414.385 | 406.61 | 0.221 | below_vwap | below_vwap |
| 7 | TT | data_center_power_cooling | 473.71 |  | 474.1176 | -0.086 | 474.085 | 467.64 | 0.133 | below_vwap | below_vwap |
| 8 | GEV | data_center_power_cooling | 1023.76 |  | 1027.1505 | -0.3301 | 1035.07 | 1021.09 | 4.4942 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1796.84 |  | 1817.6779 | -1.1464 | 1823.13 | 1796.26 | 0.1085 | below_vwap | below_vwap |
| 10 | KLAC | semiconductor_equipment | 219.67 |  | 220.9336 | -0.5719 | 222.19 | 218.09 | 4.6297 | below_vwap | below_vwap,spread_too_wide |
| 11 | IWM | market_regime | 295.14 |  | 296.1152 | -0.3293 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AMZN | cloud_ai_capex | 253.19 |  | 255.1015 | -0.7493 | 258.07 | 252.62 | 0.2054 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 667.595 |  | 671.2799 | -0.5489 | 680.09 | 667.1 | 0.4044 | below_vwap | below_vwap,spread_too_wide |
| 15 | ANET | ai_networking_optical | 166.75 |  | 166.5868 | 0.098 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 140.7 |  | 140.5221 | 0.1266 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 35.575 |  | 35.5 | 0.2113 | 37.365 | 36.4 | 0.0281 | below_opening_15m_low | below_opening_15m_low |
| 18 | SOXX | semiconductor_index | 529.16 |  | 533.781 | -0.8657 | 543.4 | 535.47 | 0.0416 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | CIEN | ai_networking_optical | 388.2 |  | 394.3263 | -1.5536 | 410 | 397.68 | 0.2756 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 706.41 |  | 709.2747 | -0.4039 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.41 |  | 709.2747 | -0.4039 | 713.55 | 708.25 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.9 |  | 71.7831 | -1.2302 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.51 |  | 207.3471 | 0.0785 | 211.03 | 207.49 | 0.0193 | watch_only | none |
| MSFT | cloud_ai_capex | 405.69 |  | 399.7756 | 1.4794 | 398.69 | 392.2 | 0.0394 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.29 |  | 330.8314 | 0.7432 | 328.98 | 326.885 | 0.099 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 357.04 |  | 368.1461 | -3.0168 | 375.18 | 369.2 | 0.3949 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496 |  | 503.6832 | -1.5254 | 518.33 | 507.62 | 1.3508 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 407.3 |  | 408.7234 | -0.3483 | 414.385 | 406.61 | 0.221 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.16 |  | 533.781 | -0.8657 | 543.4 | 535.47 | 0.0416 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.12 |  | 571.6598 | -0.6192 | 580.31 | 572.21 | 0.0704 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.27 |  | 379.8173 | -0.934 | 386.58 | 378.53 | 0.3375 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 848.9 |  | 856.7602 | -0.9174 | 887.1 | 866.765 | 0.1531 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.365 |  | 190.9636 | -1.3608 | 201.61 | 194.19 | 0.4937 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 395.63 |  | 402.026 | -1.5909 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.21 |  | 45.7784 | -1.2416 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.09 |  | 25.3099 | -0.8687 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.615 |  | 752.2546 | -0.218 | 753.51 | 751.13 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.14 |  | 296.1152 | -0.3293 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.8 |  | 126.6103 | -0.64 | 131.36 | 126.665 | 0.159 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.15 |  | 73.2962 | -0.1994 | 75.54 | 73.985 | 0.3418 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 289.09 |  | 293.2858 | -1.4306 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.41 |  | 399.2279 | -0.9563 | 406.24 | 399.495 | 0.2226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 627.95 |  | 631.214 | -0.5171 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1023.76 |  | 1027.1505 | -0.3301 | 1035.07 | 1021.09 | 4.4942 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.71 |  | 474.1176 | -0.086 | 474.085 | 467.64 | 0.133 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 140.7 |  | 140.5221 | 0.1266 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.75 |  | 166.5868 | 0.098 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 275.61 |  | 280.6181 | -1.7847 | 288.48 | 280.67 | 2.4963 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.16 |  | 708.1566 | -1.4116 | 737.175 | 720.21 | 2.8131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.2 |  | 394.3263 | -1.5536 | 410 | 397.68 | 0.2756 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.09 |  | 101.2558 | -2.139 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.27 |  | 323.3128 | -1.5597 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.84 |  | 1817.6779 | -1.1464 | 1823.13 | 1796.26 | 0.1085 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 561.87 |  | 569.8128 | -1.3939 | 572.69 | 562.32 | 0.6995 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.67 |  | 322.8774 | -1.6128 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.67 |  | 220.9336 | -0.5719 | 222.19 | 218.09 | 4.6297 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.965 |  | 326.6027 | -1.1138 | 332.49 | 326.685 | 4.2481 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 279.89 |  | 286.3034 | -2.2401 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.02 |  | 63.8816 | -1.3488 | 66.19 | 63.93 | 1.8566 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.94 |  | 51.762 | -1.588 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.39 |  | 134.8127 | -1.0553 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.42 |  | 334.1388 | -1.7115 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.245 |  | 515.2423 | 0.5828 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.065 |  | 295.0014 | 0.3605 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.295 |  | 26.7779 | -1.8035 | 28.05 | 27.6 | 0.038 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.575 |  | 35.5 | 0.2113 | 37.365 | 36.4 | 0.0281 | below_opening_15m_low | below_opening_15m_low |
| CORZ | high_beta_ai_infrastructure | 21.065 |  | 21.2034 | -0.6527 | 22.18 | 21.78 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1412.425 |  | 1460.4589 | -3.289 | 1549.47 | 1482.06 | 0.7179 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.12 |  | 473.4239 | -3.0214 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 743.87 |  | 764.0155 | -2.6368 | 797.155 | 768.7 | 4.4712 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 253.19 |  | 255.1015 | -0.7493 | 258.07 | 252.62 | 0.2054 | below_vwap | below_vwap |
| META | cloud_ai_capex | 667.595 |  | 671.2799 | -0.5489 | 680.09 | 667.1 | 0.4044 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 256.65 |  | 257.2847 | -0.2467 | 265.96 | 258.1 | 3.8964 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.18 |  | 161.5962 | -3.3517 | 168.11 | 162.41 | 0.7491 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
