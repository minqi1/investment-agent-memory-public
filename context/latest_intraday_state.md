# Intraday State

- Generated at: `2026-07-29T02:50:02+08:00`
- Market time ET: `2026-07-28T14:50:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 13, 'manual_confirm_candidate': 6, 'below_vwap': 9, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.33 |  | 674.137 | 0.3253 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.11 |  | 489.9792 | 0.2308 | 497.64 | 485.42 | 0.0448 | watch_only | none |
| SMH | semiconductor_index | 529.33 |  | 527.3666 | 0.3723 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| SPY | market_regime | 741.235 |  | 739.5554 | 0.2271 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.115 |  | 196.0765 | 0.5296 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.79 |  | 378.6179 | 0.5737 | 378.64 | 371.57 | 0.0893 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.235 |  | 739.5554 | 0.2271 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 168.61 |  | 165.0375 | 2.1646 | 165.975 | 160.51 | 0.261 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.695 |  | 330.8714 | 1.4578 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 20.97 |  | 20.0982 | 4.3376 | 20.97 | 19.755 | 0.0954 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.235 |  | 739.5554 | 0.2271 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.79 |  | 378.6179 | 0.5737 | 378.64 | 371.57 | 0.0893 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 491.11 |  | 489.9792 | 0.2308 | 497.64 | 485.42 | 0.0448 | watch_only | none |
| 4 | QQQ | market_regime | 676.33 |  | 674.137 | 0.3253 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 5 | IWM | market_regime | 293.11 |  | 292.3835 | 0.2485 | 293.26 | 291.55 | 0.0205 | watch_only | none |
| 6 | KLAC | semiconductor_equipment | 191.25 |  | 190.7783 | 0.2472 | 194.96 | 189.48 | 0.0732 | watch_only | none |
| 7 | NVDA | ai_accelerator | 197.115 |  | 196.0765 | 0.5296 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 397.595 |  | 396.3843 | 0.3054 | 400.09 | 392.355 | 0.0327 | watch_only | none |
| 9 | HPE | ai_server_oem | 44.5 |  | 44.4405 | 0.1339 | 46.19 | 44.33 | 0.0449 | watch_only | none |
| 10 | SMH | semiconductor_index | 529.33 |  | 527.3666 | 0.3723 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| 11 | AMZN | cloud_ai_capex | 231.45 |  | 230.4948 | 0.4144 | 233.05 | 229.7 | 0.0259 | watch_only | none |
| 12 | MRVL | custom_silicon_networking | 174.905 |  | 174.2046 | 0.4021 | 181.24 | 172.395 | 0.1258 | watch_only | none |
| 13 | ASML | semiconductor_equipment | 1581.13 |  | 1577.3158 | 0.2418 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 335.695 |  | 330.8714 | 1.4578 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 15 | TER | semiconductor_test_packaging | 312.235 |  | 308.6414 | 1.1643 | 315.21 | 304.11 | 0.1313 | watch_only | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.97 |  | 20.0982 | 4.3376 | 20.97 | 19.755 | 0.0954 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 28.23 |  | 28.003 | 0.8105 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 18 | TT | data_center_power_cooling | 466.76 |  | 465.22 | 0.331 | 477.73 | 460.77 | 4.9233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 266.46 |  | 266.1265 | 0.1253 | 273.86 | 266.04 | 0.5179 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | GEV | data_center_power_cooling | 938.69 |  | 937.5706 | 0.1194 | 955.825 | 935.665 | 2.17 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.115 |  | 196.0765 | 0.5296 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.79 |  | 378.6179 | 0.5737 | 378.64 | 371.57 | 0.0893 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.235 |  | 739.5554 | 0.2271 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 168.61 |  | 165.0375 | 2.1646 | 165.975 | 160.51 | 0.261 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.695 |  | 330.8714 | 1.4578 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 20.97 |  | 20.0982 | 4.3376 | 20.97 | 19.755 | 0.0954 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 391.7 |  | 387.7689 | 1.0138 | 390.46 | 382.495 | 1.034 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | JCI | data_center_power_cooling | 139.915 |  | 138.5712 | 0.9698 | 139.755 | 137.31 | 3.2091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ETN | data_center_power_cooling | 385.15 |  | 381.2568 | 1.0211 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ORCL | cloud_ai_capex | 121.13 |  | 118.5125 | 2.2086 | 117.17 | 115.25 | 0.7182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SMH | semiconductor_index | 529.33 |  | 527.3666 | 0.3723 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| 12 | SOXX | semiconductor_index | 491.11 |  | 489.9792 | 0.2308 | 497.64 | 485.42 | 0.0448 | watch_only | none |
| 13 | QQQ | market_regime | 676.33 |  | 674.137 | 0.3253 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 14 | IWM | market_regime | 293.11 |  | 292.3835 | 0.2485 | 293.26 | 291.55 | 0.0205 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 191.25 |  | 190.7783 | 0.2472 | 194.96 | 189.48 | 0.0732 | watch_only | none |
| 16 | TER | semiconductor_test_packaging | 312.235 |  | 308.6414 | 1.1643 | 315.21 | 304.11 | 0.1313 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 397.595 |  | 396.3843 | 0.3054 | 400.09 | 392.355 | 0.0327 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.45 |  | 230.4948 | 0.4144 | 233.05 | 229.7 | 0.0259 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.5 |  | 44.4405 | 0.1339 | 46.19 | 44.33 | 0.0449 | watch_only | none |
| 20 | CIEN | ai_networking_optical | 341.49 |  | 337.4357 | 1.2015 | 354.09 | 338.14 | 0.2401 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.33 |  | 674.137 | 0.3253 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.79 |  | 61.1133 | 1.1073 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.115 |  | 196.0765 | 0.5296 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.595 |  | 396.3843 | 0.3054 | 400.09 | 392.355 | 0.0327 | watch_only | none |
| AAPL | mega_cap_platform | 338.7 |  | 338.9612 | -0.077 | 342.87 | 337.78 | 0.2332 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 335.695 |  | 330.8714 | 1.4578 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.97 |  | 455.5389 | 0.0946 | 472.485 | 453.76 | 4.6845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.7 |  | 387.7689 | 1.0138 | 390.46 | 382.495 | 1.034 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.11 |  | 489.9792 | 0.2308 | 497.64 | 485.42 | 0.0448 | watch_only | none |
| SMH | semiconductor_index | 529.33 |  | 527.3666 | 0.3723 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| AVGO | custom_silicon_networking | 380.79 |  | 378.6179 | 0.5737 | 378.64 | 371.57 | 0.0893 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 818.51 |  | 815.4764 | 0.372 | 846.4 | 813.91 | 0.6561 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 174.905 |  | 174.2046 | 0.4021 | 181.24 | 172.395 | 0.1258 | watch_only | none |
| DELL | ai_server_oem | 387.47 |  | 375.2276 | 3.2627 | 402 | 374.02 | 3.399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.5 |  | 44.4405 | 0.1339 | 46.19 | 44.33 | 0.0449 | watch_only | none |
| SMCI | ai_server_oem | 28.23 |  | 28.003 | 0.8105 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 741.235 |  | 739.5554 | 0.2271 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.11 |  | 292.3835 | 0.2485 | 293.26 | 291.55 | 0.0205 | watch_only | none |
| ORCL | cloud_ai_capex | 121.13 |  | 118.5125 | 2.2086 | 117.17 | 115.25 | 0.7182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.6 |  | 66.2586 | 0.5153 | 68.995 | 65.635 | 1.952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.46 |  | 266.1265 | 0.1253 | 273.86 | 266.04 | 0.5179 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.15 |  | 381.2568 | 1.0211 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 586.12 |  | 582.3947 | 0.6396 | 603.25 | 584.69 | 0.6637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 938.69 |  | 937.5706 | 0.1194 | 955.825 | 935.665 | 2.17 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.76 |  | 465.22 | 0.331 | 477.73 | 460.77 | 4.9233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.915 |  | 138.5712 | 0.9698 | 139.755 | 137.31 | 3.2091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 168.61 |  | 165.0375 | 2.1646 | 165.975 | 160.51 | 0.261 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 241.57 |  | 237.4486 | 1.7357 | 256.145 | 236.73 | 0.8983 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 645.54 |  | 632.2319 | 2.1049 | 673.65 | 624.91 | 4.4769 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 341.49 |  | 337.4357 | 1.2015 | 354.09 | 338.14 | 0.2401 | watch_only | none |
| AAOI | ai_networking_optical | 87.41 |  | 85.8211 | 1.8514 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.62 |  | 259.0867 | 0.5918 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1581.13 |  | 1577.3158 | 0.2418 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.65 |  | 476.3444 | -0.1458 | 494.87 | 477.03 | 0.1619 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 270.62 |  | 266.6662 | 1.4827 | 276.85 | 267.14 | 3.6361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.25 |  | 190.7783 | 0.2472 | 194.96 | 189.48 | 0.0732 | watch_only | none |
| TER | semiconductor_test_packaging | 312.235 |  | 308.6414 | 1.1643 | 315.21 | 304.11 | 0.1313 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.87 |  | 236.7709 | 0.8865 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.38 |  | 46.7009 | -2.8284 | 51.64 | 47.435 | 0.2424 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.07 |  | 42.4407 | -0.8733 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.82 |  | 119.1698 | -0.2935 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 282.12 |  | 282.3584 | -0.0844 | 296.8 | 283.22 | 4.9305 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.515 |  | 518.1073 | -0.3073 | 518.6 | 511.495 | 0.0987 | below_vwap | below_vwap |
| APD | industrial_gases | 295.6 |  | 295.7501 | -0.0508 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.43 |  | 26.5157 | -0.323 | 27 | 25.42 | 0.227 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.63 |  | 33.709 | -0.2343 | 35.08 | 33.52 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.97 |  | 20.0982 | 4.3376 | 20.97 | 19.755 | 0.0954 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1081.25 |  | 1099.5478 | -1.6641 | 1185.19 | 1114.57 | 2.277 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.2 |  | 439.9927 | 3.6836 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 749.69 |  | 732.1328 | 2.3981 | 774.805 | 719.02 | 4.5726 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.45 |  | 230.4948 | 0.4144 | 233.05 | 229.7 | 0.0259 | watch_only | none |
| META | cloud_ai_capex | 594.15 |  | 593.8196 | 0.0556 | 600.765 | 594.21 | 0.1178 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 244.63 |  | 245.2195 | -0.2404 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.42 |  | 131.5384 | -0.8502 | 136.45 | 131.735 | 0.3297 | below_opening_15m_low | below_opening_15m_low,below_vwap |
