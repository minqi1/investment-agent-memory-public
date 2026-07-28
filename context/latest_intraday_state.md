# Intraday State

- Generated at: `2026-07-29T02:30:54+08:00`
- Market time ET: `2026-07-28T14:30:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 6, 'below_vwap': 13, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 15, 'below_opening_15m_low': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.57 |  | 674.0996 | 0.2181 | 677.3 | 670.84 | 0.0311 | watch_only | none |
| SOXX | semiconductor_index | 489.95 |  | 489.9613 | -0.0023 | 497.64 | 485.42 | 0.0816 | below_vwap | below_vwap |
| SMH | semiconductor_index | 528.22 |  | 527.3321 | 0.1684 | 533.01 | 523.325 | 0.0284 | watch_only | none |
| SPY | market_regime | 740.51 |  | 739.5083 | 0.1355 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.705 |  | 196.0375 | 0.3405 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 390.725 |  | 387.6433 | 0.795 | 390.46 | 382.495 | 0.1126 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 379.41 |  | 378.5723 | 0.2213 | 378.64 | 371.57 | 0.0343 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 740.51 |  | 739.5083 | 0.1355 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.88 |  | 330.6545 | 1.2779 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.48 |  | 118.4464 | 1.7169 | 117.17 | 115.25 | 0.0581 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.41 |  | 378.5723 | 0.2213 | 378.64 | 371.57 | 0.0343 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.51 |  | 739.5083 | 0.1355 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 196.705 |  | 196.0375 | 0.3405 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 390.725 |  | 387.6433 | 0.795 | 390.46 | 382.495 | 0.1126 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 528.22 |  | 527.3321 | 0.1684 | 533.01 | 523.325 | 0.0284 | watch_only | none |
| 6 | QQQ | market_regime | 675.57 |  | 674.0996 | 0.2181 | 677.3 | 670.84 | 0.0311 | watch_only | none |
| 7 | IWM | market_regime | 292.74 |  | 292.3417 | 0.1362 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 397.53 |  | 396.3482 | 0.2982 | 400.09 | 392.355 | 0.0352 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 339.84 |  | 338.9555 | 0.261 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 231.095 |  | 230.4716 | 0.2705 | 233.05 | 229.7 | 0.1731 | watch_only | none |
| 11 | PWR | data_center_power_cooling | 585.36 |  | 582.2085 | 0.5413 | 603.25 | 584.69 | 0.0803 | watch_only | none |
| 12 | SMCI | ai_server_oem | 28.21 |  | 27.9954 | 0.7667 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 13 | TER | semiconductor_test_packaging | 309.565 |  | 308.4091 | 0.3748 | 315.21 | 304.11 | 0.3263 | watch_only | none |
| 14 | GOOGL | cloud_ai_capex | 334.88 |  | 330.6545 | 1.2779 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 15 | ASML | semiconductor_equipment | 1580.25 |  | 1577.2212 | 0.192 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TT | data_center_power_cooling | 466.435 |  | 465.1736 | 0.2712 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ALAB | ai_networking_optical | 259.61 |  | 259.0587 | 0.2128 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 139.645 |  | 138.5038 | 0.8239 | 139.755 | 137.31 | 0.1074 | watch_only | none |
| 19 | LITE | ai_networking_optical | 639.56 |  | 631.9003 | 1.2122 | 673.65 | 624.91 | 0.1782 | watch_only | none |
| 20 | META | cloud_ai_capex | 594.48 |  | 593.8463 | 0.1067 | 600.765 | 594.21 | 1.0463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.705 |  | 196.0375 | 0.3405 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 390.725 |  | 387.6433 | 0.795 | 390.46 | 382.495 | 0.1126 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 379.41 |  | 378.5723 | 0.2213 | 378.64 | 371.57 | 0.0343 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 740.51 |  | 739.5083 | 0.1355 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.88 |  | 330.6545 | 1.2779 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.48 |  | 118.4464 | 1.7169 | 117.17 | 115.25 | 0.0581 | buy_precheck_manual_confirm | none |
| 7 | ANET | ai_networking_optical | 168.1 |  | 164.6875 | 2.0721 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SMH | semiconductor_index | 528.22 |  | 527.3321 | 0.1684 | 533.01 | 523.325 | 0.0284 | watch_only | none |
| 9 | QQQ | market_regime | 675.57 |  | 674.0996 | 0.2181 | 677.3 | 670.84 | 0.0311 | watch_only | none |
| 10 | STX | memory_hbm_storage | 748.97 |  | 730.9444 | 2.4661 | 774.805 | 719.02 | 0.1656 | watch_only | none |
| 11 | PWR | data_center_power_cooling | 585.36 |  | 582.2085 | 0.5413 | 603.25 | 584.69 | 0.0803 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 139.645 |  | 138.5038 | 0.8239 | 139.755 | 137.31 | 0.1074 | watch_only | none |
| 13 | IWM | market_regime | 292.74 |  | 292.3417 | 0.1362 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 14 | LITE | ai_networking_optical | 639.56 |  | 631.9003 | 1.2122 | 673.65 | 624.91 | 0.1782 | watch_only | none |
| 15 | TER | semiconductor_test_packaging | 309.565 |  | 308.4091 | 0.3748 | 315.21 | 304.11 | 0.3263 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 397.53 |  | 396.3482 | 0.2982 | 400.09 | 392.355 | 0.0352 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.095 |  | 230.4716 | 0.2705 | 233.05 | 229.7 | 0.1731 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.21 |  | 27.9954 | 0.7667 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 19 | AAPL | mega_cap_platform | 339.84 |  | 338.9555 | 0.261 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 20 | CORZ | high_beta_ai_infrastructure | 20.44 |  | 20.0545 | 1.9225 | 20.97 | 19.755 | 0.0978 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.57 |  | 674.0996 | 0.2181 | 677.3 | 670.84 | 0.0311 | watch_only | none |
| TQQQ | leveraged_tool | 61.53 |  | 61.1 | 0.7037 | 62.01 | 60.23 | 0.0163 | watch_only | none |
| NVDA | ai_accelerator | 196.705 |  | 196.0375 | 0.3405 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.53 |  | 396.3482 | 0.2982 | 400.09 | 392.355 | 0.0352 | watch_only | none |
| AAPL | mega_cap_platform | 339.84 |  | 338.9555 | 0.261 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.88 |  | 330.6545 | 1.2779 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.25 |  | 455.5265 | -0.0607 | 472.485 | 453.76 | 4.6919 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 390.725 |  | 387.6433 | 0.795 | 390.46 | 382.495 | 0.1126 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 489.95 |  | 489.9613 | -0.0023 | 497.64 | 485.42 | 0.0816 | below_vwap | below_vwap |
| SMH | semiconductor_index | 528.22 |  | 527.3321 | 0.1684 | 533.01 | 523.325 | 0.0284 | watch_only | none |
| AVGO | custom_silicon_networking | 379.41 |  | 378.5723 | 0.2213 | 378.64 | 371.57 | 0.0343 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 815.28 |  | 815.3137 | -0.0041 | 846.4 | 813.91 | 0.0736 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 174.595 |  | 174.1785 | 0.2391 | 181.24 | 172.395 | 3.5568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 383.44 |  | 374.9836 | 2.2551 | 402 | 374.02 | 1.4526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.385 |  | 44.4395 | -0.1226 | 46.19 | 44.33 | 0.0676 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.21 |  | 27.9954 | 0.7667 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 740.51 |  | 739.5083 | 0.1355 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.74 |  | 292.3417 | 0.1362 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.48 |  | 118.4464 | 1.7169 | 117.17 | 115.25 | 0.0581 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.29 |  | 66.2546 | 0.0534 | 68.995 | 65.635 | 1.9762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 264.22 |  | 266.1549 | -0.727 | 273.86 | 266.04 | 2.1649 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 384.02 |  | 381.1219 | 0.7604 | 384.565 | 377.43 | 2.5624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 585.36 |  | 582.2085 | 0.5413 | 603.25 | 584.69 | 0.0803 | watch_only | none |
| GEV | data_center_power_cooling | 936.87 |  | 937.5511 | -0.0726 | 955.825 | 935.665 | 0.8133 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 466.435 |  | 465.1736 | 0.2712 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.645 |  | 138.5038 | 0.8239 | 139.755 | 137.31 | 0.1074 | watch_only | none |
| ANET | ai_networking_optical | 168.1 |  | 164.6875 | 2.0721 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 239.88 |  | 237.3116 | 1.0823 | 256.145 | 236.73 | 4.323 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 639.56 |  | 631.9003 | 1.2122 | 673.65 | 624.91 | 0.1782 | watch_only | none |
| CIEN | ai_networking_optical | 338.8 |  | 337.3857 | 0.4192 | 354.09 | 338.14 | 3.7869 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 86.76 |  | 85.783 | 1.1389 | 92.95 | 84.63 | 4.6911 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 259.61 |  | 259.0587 | 0.2128 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1580.25 |  | 1577.2212 | 0.192 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 474.055 |  | 476.394 | -0.491 | 494.87 | 477.03 | 1.9449 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.45 |  | 266.597 | 1.4453 | 276.85 | 267.14 | 0.403 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.62 |  | 190.7603 | -0.0736 | 194.96 | 189.48 | 0.6505 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 309.565 |  | 308.4091 | 0.3748 | 315.21 | 304.11 | 0.3263 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.37 |  | 236.723 | 0.6958 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.67 |  | 46.7229 | -2.2536 | 51.64 | 47.435 | 1.1386 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.96 |  | 42.4569 | -1.1703 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.445 |  | 119.2156 | -0.6464 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.6 |  | 282.3729 | -0.2737 | 296.8 | 283.22 | 0.1953 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LIN | industrial_gases | 514.07 |  | 518.2793 | -0.8122 | 518.6 | 511.495 | 0.0642 | below_vwap | below_vwap |
| APD | industrial_gases | 294.93 |  | 295.7732 | -0.2851 | 297.25 | 293.555 | 4.4621 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.27 |  | 26.5184 | -0.9367 | 27 | 25.42 | 0.2665 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.49 |  | 33.7139 | -0.6642 | 35.08 | 33.52 | 0.0299 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.44 |  | 20.0545 | 1.9225 | 20.97 | 19.755 | 0.0978 | watch_only | none |
| SNDK | memory_hbm_storage | 1077.61 |  | 1100.3031 | -2.0624 | 1185.19 | 1114.57 | 3.0438 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.75 |  | 439.4845 | 3.4735 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 748.97 |  | 730.9444 | 2.4661 | 774.805 | 719.02 | 0.1656 | watch_only | none |
| AMZN | cloud_ai_capex | 231.095 |  | 230.4716 | 0.2705 | 233.05 | 229.7 | 0.1731 | watch_only | none |
| META | cloud_ai_capex | 594.48 |  | 593.8463 | 0.1067 | 600.765 | 594.21 | 1.0463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 243.8 |  | 245.2678 | -0.5985 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.71 |  | 131.585 | -1.4249 | 136.45 | 131.735 | 0.532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
