# Intraday State

- Generated at: `2026-07-17T00:48:07+08:00`
- Market time ET: `2026-07-16T12:48:08-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 37, 'spread_too_wide_or_missing': 3, 'manual_confirm_candidate': 1, 'below_vwap': 13, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.42 |  | 710.0881 | -0.3757 | 713.55 | 708.25 | 0.0594 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.51 |  | 536.2687 | -1.4468 | 543.4 | 535.47 | 0.07 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.94 |  | 574.421 | -1.1283 | 580.31 | 572.21 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.91 |  | 752.7576 | -0.1126 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.44 |  | 329.9246 | 0.1562 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.44 |  | 329.9246 | 0.1562 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 256.2 |  | 255.4058 | 0.311 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 3 | LIN | industrial_gases | 516.36 |  | 514.8788 | 0.2877 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.445 |  | 294.7675 | 0.5691 | 293.89 | 291.35 | 3.8287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ASML | semiconductor_equipment | 1803.94 |  | 1823.1373 | -1.053 | 1823.13 | 1796.26 | 0.0887 | below_vwap | below_vwap |
| 6 | KLAC | semiconductor_equipment | 218.47 |  | 221.8211 | -1.5107 | 222.19 | 218.09 | 0.0961 | below_vwap | below_vwap |
| 7 | SPY | market_regime | 751.91 |  | 752.7576 | -0.1126 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.49 |  | 296.4188 | -0.3134 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ANET | ai_networking_optical | 166.03 |  | 166.3211 | -0.175 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | TT | data_center_power_cooling | 473.2 |  | 473.9843 | -0.1655 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 139.915 |  | 140.5388 | -0.4439 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1021.65 |  | 1029.8119 | -0.7926 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 371.51 |  | 371.8821 | -0.1001 | 375.18 | 369.2 | 0.1965 | below_vwap | below_vwap |
| 15 | MSFT | cloud_ai_capex | 402.19 |  | 396.9523 | 1.3195 | 398.69 | 392.2 | 0.6688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 379.72 |  | 381.6005 | -0.4928 | 386.58 | 378.53 | 1.3431 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMAT | semiconductor_equipment | 563.94 |  | 573.4758 | -1.6628 | 572.69 | 562.32 | 2.1314 | below_vwap | below_vwap,spread_too_wide |
| 18 | META | cloud_ai_capex | 670 |  | 673.6982 | -0.5489 | 680.09 | 667.1 | 1.8597 | below_vwap | below_vwap,spread_too_wide |
| 19 | SOXX | semiconductor_index | 528.51 |  | 536.2687 | -1.4468 | 543.4 | 535.47 | 0.07 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 707.42 |  | 710.0881 | -0.3757 | 713.55 | 708.25 | 0.0594 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.44 |  | 329.9246 | 0.1562 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.36 |  | 514.8788 | 0.2877 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | APD | industrial_gases | 296.445 |  | 294.7675 | 0.5691 | 293.89 | 291.35 | 3.8287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | MSFT | cloud_ai_capex | 402.19 |  | 396.9523 | 1.3195 | 398.69 | 392.2 | 0.6688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AMZN | cloud_ai_capex | 256.2 |  | 255.4058 | 0.311 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 6 | ANET | ai_networking_optical | 166.03 |  | 166.3211 | -0.175 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | AVGO | custom_silicon_networking | 379.72 |  | 381.6005 | -0.4928 | 386.58 | 378.53 | 1.3431 | below_vwap | below_vwap,spread_too_wide |
| 8 | TT | data_center_power_cooling | 473.2 |  | 473.9843 | -0.1655 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 139.915 |  | 140.5388 | -0.4439 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | GEV | data_center_power_cooling | 1021.65 |  | 1029.8119 | -0.7926 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ASML | semiconductor_equipment | 1803.94 |  | 1823.1373 | -1.053 | 1823.13 | 1796.26 | 0.0887 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 563.94 |  | 573.4758 | -1.6628 | 572.69 | 562.32 | 2.1314 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 218.47 |  | 221.8211 | -1.5107 | 222.19 | 218.09 | 0.0961 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 751.91 |  | 752.7576 | -0.1126 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.49 |  | 296.4188 | -0.3134 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 371.51 |  | 371.8821 | -0.1001 | 375.18 | 369.2 | 0.1965 | below_vwap | below_vwap |
| 18 | META | cloud_ai_capex | 670 |  | 673.6982 | -0.5489 | 680.09 | 667.1 | 1.8597 | below_vwap | below_vwap,spread_too_wide |
| 19 | SOXX | semiconductor_index | 528.51 |  | 536.2687 | -1.4468 | 543.4 | 535.47 | 0.07 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | TSM | foundry | 405.37 |  | 410.5111 | -1.2524 | 414.385 | 406.61 | 0.7943 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.42 |  | 710.0881 | -0.3757 | 713.55 | 708.25 | 0.0594 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.25 |  | 72.0685 | -1.1357 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.2 |  | 207.5458 | -0.1666 | 211.03 | 207.49 | 0.2075 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.19 |  | 396.9523 | 1.3195 | 398.69 | 392.2 | 0.6688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 330.44 |  | 329.9246 | 0.1562 | 328.98 | 326.885 | 0.0182 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.51 |  | 371.8821 | -0.1001 | 375.18 | 369.2 | 0.1965 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.75 |  | 507.7506 | -1.5757 | 518.33 | 507.62 | 0.5023 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.37 |  | 410.5111 | -1.2524 | 414.385 | 406.61 | 0.7943 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.51 |  | 536.2687 | -1.4468 | 543.4 | 535.47 | 0.07 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.94 |  | 574.421 | -1.1283 | 580.31 | 572.21 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 379.72 |  | 381.6005 | -0.4928 | 386.58 | 378.53 | 1.3431 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 847.21 |  | 861.2605 | -1.6314 | 887.1 | 866.765 | 0.2727 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188 |  | 192.4621 | -2.3184 | 201.61 | 194.19 | 1.0532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.14 |  | 403.5734 | -0.8507 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.265 |  | 46.079 | -1.7664 | 47.65 | 46.165 | 0.0442 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.005 |  | 25.5283 | -2.0497 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.91 |  | 752.7576 | -0.1126 | 753.51 | 751.13 | 0.008 | below_vwap | below_vwap |
| IWM | market_regime | 295.49 |  | 296.4188 | -0.3134 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.66 |  | 126.7695 | -0.0864 | 131.36 | 126.665 | 0.529 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.875 |  | 73.5249 | -0.8839 | 75.54 | 73.985 | 4.8576 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 290.25 |  | 295.0518 | -1.6274 | 300.385 | 293.64 | 4.7476 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 392.905 |  | 400.2134 | -1.8261 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.14 |  | 632.4652 | -0.842 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1021.65 |  | 1029.8119 | -0.7926 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 473.2 |  | 473.9843 | -0.1655 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 139.915 |  | 140.5388 | -0.4439 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.03 |  | 166.3211 | -0.175 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 276.08 |  | 282.3986 | -2.2375 | 288.48 | 280.67 | 3.6475 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.67 |  | 712.1745 | -1.8962 | 737.175 | 720.21 | 3.6942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.59 |  | 396.7466 | -1.5518 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.59 |  | 102.3018 | -3.6283 | 106.975 | 102.85 | 4.7266 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 318.89 |  | 324.9268 | -1.8579 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1803.94 |  | 1823.1373 | -1.053 | 1823.13 | 1796.26 | 0.0887 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 563.94 |  | 573.4758 | -1.6628 | 572.69 | 562.32 | 2.1314 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.55 |  | 325.4269 | -1.8059 | 328.96 | 324.11 | 3.8867 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 218.47 |  | 221.8211 | -1.5107 | 222.19 | 218.09 | 0.0961 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.2 |  | 327.6927 | -1.6762 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 283.86 |  | 289.623 | -1.9898 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.925 |  | 64.4066 | -2.3004 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.38 |  | 52.2999 | -1.7589 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.43 |  | 135.1924 | -1.3036 | 138.07 | 133.73 | 2.788 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 334.675 |  | 338.999 | -1.2755 | 346.26 | 338 | 3.6334 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.36 |  | 514.8788 | 0.2877 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.445 |  | 294.7675 | 0.5691 | 293.89 | 291.35 | 3.8287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.3 |  | 27.0702 | -2.8451 | 28.05 | 27.6 | 0.1141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.84 |  | 35.7573 | -2.5654 | 37.365 | 36.4 | 0.0861 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.83 |  | 21.3883 | -2.6104 | 22.18 | 21.78 | 0.048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1429.5 |  | 1476.9514 | -3.2128 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 458.84 |  | 478.0639 | -4.0212 | 498.04 | 480.14 | 0.7192 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 753.97 |  | 769.4842 | -2.0162 | 797.155 | 768.7 | 3.9086 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.2 |  | 255.4058 | 0.311 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 670 |  | 673.6982 | -0.5489 | 680.09 | 667.1 | 1.8597 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 252.785 |  | 257.8434 | -1.9618 | 265.96 | 258.1 | 3.9559 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 159.67 |  | 163.379 | -2.2702 | 168.11 | 162.41 | 0.7077 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
