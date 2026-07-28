# Intraday State

- Generated at: `2026-07-28T22:29:13+08:00`
- Market time ET: `2026-07-28T10:29:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'below_vwap': 12, 'watch_only': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.03 |  | 671.2591 | -0.1831 | 677.3 | 670.84 | 0.0821 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 484.25 |  | 488.4505 | -0.86 | 497.64 | 485.42 | 0.0971 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 521.875 |  | 524.9971 | -0.5947 | 533.01 | 523.325 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.33 |  | 737.507 | -0.024 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 375.4 |  | 375.2142 | 0.0495 | 378.64 | 371.57 | 0.1438 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 327.89 |  | 327.0311 | 0.2626 | 330.21 | 324.97 | 0.2013 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 395.21 |  | 394.6064 | 0.153 | 400.09 | 392.355 | 0.2632 | watch_only | none |
| 4 | APD | industrial_gases | 297.51 |  | 296.3604 | 0.3879 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 520.77 |  | 518.5047 | 0.4369 | 518.6 | 511.495 | 3.8904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | NVDA | ai_accelerator | 193.72 |  | 194.0111 | -0.15 | 195.4 | 193.65 | 0.0206 | below_vwap | below_vwap |
| 7 | SPY | market_regime | 737.33 |  | 737.507 | -0.024 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | TT | data_center_power_cooling | 462.03 |  | 464.4282 | -0.5164 | 477.73 | 460.77 | 0.2879 | below_vwap | below_vwap |
| 10 | ANET | ai_networking_optical | 161.47 |  | 161.5438 | -0.0457 | 165.975 | 160.51 | 0.3344 | below_vwap | below_vwap |
| 11 | ARM | ai_accelerator | 244.05 |  | 244.7915 | -0.3029 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | TER | semiconductor_test_packaging | 305.19 |  | 305.3372 | -0.0482 | 315.21 | 304.11 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | APLD | high_beta_ai_infrastructure | 26.045 |  | 26.308 | -0.9998 | 27 | 25.42 | 0.2304 | below_vwap | below_vwap |
| 14 | COHU | semiconductor_test_packaging | 42.09 |  | 42.7536 | -1.5521 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TSM | foundry | 382.68 |  | 384.9451 | -0.5884 | 390.46 | 382.495 | 0.4129 | below_vwap | below_vwap,spread_too_wide |
| 16 | ASML | semiconductor_equipment | 1567.74 |  | 1570.1856 | -0.1558 | 1586.01 | 1565.95 | 0.6532 | below_vwap | below_vwap,spread_too_wide |
| 17 | ENTG | semiconductor_materials | 118.415 |  | 119.3096 | -0.7498 | 121 | 117.72 | 4.6447 | below_vwap | below_vwap,spread_too_wide |
| 18 | SMH | semiconductor_index | 521.875 |  | 524.9971 | -0.5947 | 533.01 | 523.325 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SOXX | semiconductor_index | 484.25 |  | 488.4505 | -0.86 | 497.64 | 485.42 | 0.0971 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 670.03 |  | 671.2591 | -0.1831 | 677.3 | 670.84 | 0.0821 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 520.77 |  | 518.5047 | 0.4369 | 518.6 | 511.495 | 3.8904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | APD | industrial_gases | 297.51 |  | 296.3604 | 0.3879 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | AVGO | custom_silicon_networking | 375.4 |  | 375.2142 | 0.0495 | 378.64 | 371.57 | 0.1438 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 327.89 |  | 327.0311 | 0.2626 | 330.21 | 324.97 | 0.2013 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 395.21 |  | 394.6064 | 0.153 | 400.09 | 392.355 | 0.2632 | watch_only | none |
| 6 | NVDA | ai_accelerator | 193.72 |  | 194.0111 | -0.15 | 195.4 | 193.65 | 0.0206 | below_vwap | below_vwap |
| 7 | TSM | foundry | 382.68 |  | 384.9451 | -0.5884 | 390.46 | 382.495 | 0.4129 | below_vwap | below_vwap,spread_too_wide |
| 8 | SPY | market_regime | 737.33 |  | 737.507 | -0.024 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1567.74 |  | 1570.1856 | -0.1558 | 1586.01 | 1565.95 | 0.6532 | below_vwap | below_vwap,spread_too_wide |
| 10 | TT | data_center_power_cooling | 462.03 |  | 464.4282 | -0.5164 | 477.73 | 460.77 | 0.2879 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 161.47 |  | 161.5438 | -0.0457 | 165.975 | 160.51 | 0.3344 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ARM | ai_accelerator | 244.05 |  | 244.7915 | -0.3029 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 305.19 |  | 305.3372 | -0.0482 | 315.21 | 304.11 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 118.415 |  | 119.3096 | -0.7498 | 121 | 117.72 | 4.6447 | below_vwap | below_vwap,spread_too_wide |
| 16 | COHU | semiconductor_test_packaging | 42.09 |  | 42.7536 | -1.5521 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | APLD | high_beta_ai_infrastructure | 26.045 |  | 26.308 | -0.9998 | 27 | 25.42 | 0.2304 | below_vwap | below_vwap |
| 18 | MU | memory_hbm_storage | 800.61 |  | 811.6818 | -1.3641 | 846.4 | 813.91 | 1.8436 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | SMH | semiconductor_index | 521.875 |  | 524.9971 | -0.5947 | 533.01 | 523.325 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SOXX | semiconductor_index | 484.25 |  | 488.4505 | -0.86 | 497.64 | 485.42 | 0.0971 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.03 |  | 671.2591 | -0.1831 | 677.3 | 670.84 | 0.0821 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 59.95 |  | 60.3998 | -0.7448 | 62.01 | 60.23 | 0.0334 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 193.72 |  | 194.0111 | -0.15 | 195.4 | 193.65 | 0.0206 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 395.21 |  | 394.6064 | 0.153 | 400.09 | 392.355 | 0.2632 | watch_only | none |
| AAPL | mega_cap_platform | 337.735 |  | 338.6954 | -0.2836 | 342.87 | 337.78 | 0.3642 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 327.89 |  | 327.0311 | 0.2626 | 330.21 | 324.97 | 0.2013 | watch_only | none |
| AMD | ai_accelerator | 446.945 |  | 453.9173 | -1.536 | 472.485 | 453.76 | 1.9734 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 382.68 |  | 384.9451 | -0.5884 | 390.46 | 382.495 | 0.4129 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 484.25 |  | 488.4505 | -0.86 | 497.64 | 485.42 | 0.0971 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 521.875 |  | 524.9971 | -0.5947 | 533.01 | 523.325 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.4 |  | 375.2142 | 0.0495 | 378.64 | 371.57 | 0.1438 | watch_only | none |
| MU | memory_hbm_storage | 800.61 |  | 811.6818 | -1.3641 | 846.4 | 813.91 | 1.8436 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 168.49 |  | 172.0486 | -2.0684 | 181.24 | 172.395 | 1.3532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 366.61 |  | 370.5711 | -1.0689 | 402 | 374.02 | 2.695 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.365 |  | 44.0449 | -1.5436 | 46.19 | 44.33 | 0.1384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.345 |  | 27.6432 | -1.0788 | 28.86 | 27.59 | 0.0731 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.33 |  | 737.507 | -0.024 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 290.71 |  | 291.7376 | -0.3522 | 293.26 | 291.55 | 0.0138 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.19 |  | 115.7254 | -0.4627 | 117.17 | 115.25 | 0.2084 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 65.325 |  | 65.9555 | -0.9559 | 68.995 | 65.635 | 4.9292 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 260.31 |  | 266.507 | -2.3253 | 273.86 | 266.04 | 4.8058 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 376.95 |  | 378.7579 | -0.4773 | 384.565 | 377.43 | 3.6344 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 572.07 |  | 580.3804 | -1.4319 | 603.25 | 584.69 | 4.1586 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 920.035 |  | 934.6415 | -1.5628 | 955.825 | 935.665 | 0.3217 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 462.03 |  | 464.4282 | -0.5164 | 477.73 | 460.77 | 0.2879 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 136.81 |  | 137.9591 | -0.8329 | 139.755 | 137.31 | 0.3143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ANET | ai_networking_optical | 161.47 |  | 161.5438 | -0.0457 | 165.975 | 160.51 | 0.3344 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 229.735 |  | 237.1003 | -3.1064 | 256.145 | 236.73 | 0.8053 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 608.52 |  | 624.5932 | -2.5734 | 673.65 | 624.91 | 4.4255 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 329.91 |  | 336.1786 | -1.8647 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 82.4 |  | 84.7879 | -2.8163 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 252.47 |  | 255.3238 | -1.1177 | 268.265 | 253.05 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1567.74 |  | 1570.1856 | -0.1558 | 1586.01 | 1565.95 | 0.6532 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 471.785 |  | 478.1858 | -1.3386 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 261.565 |  | 266.1995 | -1.741 | 276.85 | 267.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 188.81 |  | 190.1235 | -0.6908 | 194.96 | 189.48 | 1.663 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 305.19 |  | 305.3372 | -0.0482 | 315.21 | 304.11 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 232.79 |  | 238.1384 | -2.2459 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.75 |  | 47.3762 | -3.4325 | 51.64 | 47.435 | 4.8962 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.09 |  | 42.7536 | -1.5521 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.415 |  | 119.3096 | -0.7498 | 121 | 117.72 | 4.6447 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 278.74 |  | 282.8597 | -1.4565 | 296.8 | 283.22 | 0.8467 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 520.77 |  | 518.5047 | 0.4369 | 518.6 | 511.495 | 3.8904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.51 |  | 296.3604 | 0.3879 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.045 |  | 26.308 | -0.9998 | 27 | 25.42 | 0.2304 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 32.89 |  | 33.2701 | -1.1425 | 35.08 | 33.52 | 0.0608 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.61 |  | 19.9683 | -1.7946 | 20.97 | 19.755 | 0.051 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1082.29 |  | 1104.9248 | -2.0485 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 426.205 |  | 434.0027 | -1.7967 | 465.04 | 435.22 | 0.1736 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 713.53 |  | 722.045 | -1.1793 | 774.805 | 719.02 | 3.8905 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 229.625 |  | 230.3284 | -0.3054 | 233.05 | 229.7 | 0.0261 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 593.8 |  | 595.0589 | -0.2116 | 600.765 | 594.21 | 0.0926 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 244.05 |  | 244.7915 | -0.3029 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.975 |  | 131.318 | -1.0227 | 136.45 | 131.735 | 1.7003 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
