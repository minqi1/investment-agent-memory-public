# Intraday State

- Generated at: `2026-07-29T03:05:26+08:00`
- Market time ET: `2026-07-28T15:05:26-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'below_vwap': 7, 'watch_only': 12, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_opening_15m_low': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.65 |  | 674.2098 | 0.5103 | 677.3 | 670.84 | 0.0236 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 494.69 |  | 490.0116 | 0.9547 | 497.64 | 485.42 | 0.0425 | watch_only | none |
| SMH | semiconductor_index | 532.32 |  | 527.4359 | 0.926 | 533.01 | 523.325 | 0.0545 | watch_only | none |
| SPY | market_regime | 741.91 |  | 739.6213 | 0.3094 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.58 |  | 196.1167 | 0.7461 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.91 |  | 739.6213 | 0.3094 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 677.65 |  | 674.2098 | 0.5103 | 677.3 | 670.84 | 0.0236 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.19 |  | 331.0783 | 1.2419 | 330.21 | 324.97 | 0.0865 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.48 |  | 292.4316 | 0.3585 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 21.135 |  | 20.1358 | 4.9625 | 20.97 | 19.755 | 0.1419 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.17 |  | 61.1371 | 1.6894 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.91 |  | 739.6213 | 0.3094 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 677.65 |  | 674.2098 | 0.5103 | 677.3 | 670.84 | 0.0236 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 293.48 |  | 292.4316 | 0.3585 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 197.58 |  | 196.1167 | 0.7461 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 231.33 |  | 230.5239 | 0.3497 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 339.62 |  | 338.9685 | 0.1922 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 7 | META | cloud_ai_capex | 594.98 |  | 593.8422 | 0.1916 | 600.765 | 594.21 | 0.284 | watch_only | none |
| 8 | ARM | ai_accelerator | 245.85 |  | 245.2195 | 0.2571 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 532.32 |  | 527.4359 | 0.926 | 533.01 | 523.325 | 0.0545 | watch_only | none |
| 10 | SOXX | semiconductor_index | 494.69 |  | 490.0116 | 0.9547 | 497.64 | 485.42 | 0.0425 | watch_only | none |
| 11 | GOOGL | cloud_ai_capex | 335.19 |  | 331.0783 | 1.2419 | 330.21 | 324.97 | 0.0865 | buy_precheck_manual_confirm | none |
| 12 | COHU | semiconductor_test_packaging | 42.47 |  | 42.4356 | 0.0811 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | MU | memory_hbm_storage | 827.48 |  | 815.6625 | 1.4488 | 846.4 | 813.91 | 0.197 | watch_only | none |
| 14 | PWR | data_center_power_cooling | 587.38 |  | 582.5846 | 0.8231 | 603.25 | 584.69 | 0.189 | watch_only | none |
| 15 | AMD | ai_accelerator | 460.46 |  | 455.5807 | 1.071 | 472.485 | 453.76 | 0.1564 | watch_only | none |
| 16 | CORZ | high_beta_ai_infrastructure | 21.135 |  | 20.1358 | 4.9625 | 20.97 | 19.755 | 0.1419 | buy_precheck_manual_confirm | none |
| 17 | MRVL | custom_silicon_networking | 175.84 |  | 174.2195 | 0.9301 | 181.24 | 172.395 | 0.1535 | watch_only | none |
| 18 | ENTG | semiconductor_materials | 119.61 |  | 119.1644 | 0.374 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | HPE | ai_server_oem | 45.13 |  | 44.4531 | 1.5228 | 46.19 | 44.33 | 0.0665 | watch_only | none |
| 20 | TT | data_center_power_cooling | 467.86 |  | 465.3755 | 0.5339 | 477.73 | 460.77 | 5.0271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.58 |  | 196.1167 | 0.7461 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.91 |  | 739.6213 | 0.3094 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 677.65 |  | 674.2098 | 0.5103 | 677.3 | 670.84 | 0.0236 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.19 |  | 331.0783 | 1.2419 | 330.21 | 324.97 | 0.0865 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.48 |  | 292.4316 | 0.3585 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 21.135 |  | 20.1358 | 4.9625 | 20.97 | 19.755 | 0.1419 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.17 |  | 61.1371 | 1.6894 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| 8 | TSM | foundry | 393.515 |  | 387.8568 | 1.4588 | 390.46 | 382.495 | 1.08 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | AVGO | custom_silicon_networking | 383.45 |  | 378.6743 | 1.2612 | 378.64 | 371.57 | 1.7238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ASML | semiconductor_equipment | 1590.32 |  | 1577.429 | 0.8172 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ANET | ai_networking_optical | 169.64 |  | 165.1404 | 2.7247 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 140.86 |  | 138.6985 | 1.5584 | 139.755 | 137.31 | 4.5932 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ETN | data_center_power_cooling | 385.875 |  | 381.3728 | 1.1805 | 384.565 | 377.43 | 4.3486 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 122.28 |  | 118.6681 | 3.0437 | 117.17 | 115.25 | 0.6869 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 315.99 |  | 308.9383 | 2.2826 | 315.21 | 304.11 | 3.3261 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 827.48 |  | 815.6625 | 1.4488 | 846.4 | 813.91 | 0.197 | watch_only | none |
| 17 | SMH | semiconductor_index | 532.32 |  | 527.4359 | 0.926 | 533.01 | 523.325 | 0.0545 | watch_only | none |
| 18 | SOXX | semiconductor_index | 494.69 |  | 490.0116 | 0.9547 | 497.64 | 485.42 | 0.0425 | watch_only | none |
| 19 | STX | memory_hbm_storage | 749.01 |  | 732.8269 | 2.2083 | 774.805 | 719.02 | 0.3084 | watch_only | none |
| 20 | PWR | data_center_power_cooling | 587.38 |  | 582.5846 | 0.8231 | 603.25 | 584.69 | 0.189 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.65 |  | 674.2098 | 0.5103 | 677.3 | 670.84 | 0.0236 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.17 |  | 61.1371 | 1.6894 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.58 |  | 196.1167 | 0.7461 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.25 |  | 396.4179 | -0.0423 | 400.09 | 392.355 | 0.0404 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.62 |  | 338.9685 | 0.1922 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.19 |  | 331.0783 | 1.2419 | 330.21 | 324.97 | 0.0865 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 460.46 |  | 455.5807 | 1.071 | 472.485 | 453.76 | 0.1564 | watch_only | none |
| TSM | foundry | 393.515 |  | 387.8568 | 1.4588 | 390.46 | 382.495 | 1.08 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 494.69 |  | 490.0116 | 0.9547 | 497.64 | 485.42 | 0.0425 | watch_only | none |
| SMH | semiconductor_index | 532.32 |  | 527.4359 | 0.926 | 533.01 | 523.325 | 0.0545 | watch_only | none |
| AVGO | custom_silicon_networking | 383.45 |  | 378.6743 | 1.2612 | 378.64 | 371.57 | 1.7238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 827.48 |  | 815.6625 | 1.4488 | 846.4 | 813.91 | 0.197 | watch_only | none |
| MRVL | custom_silicon_networking | 175.84 |  | 174.2195 | 0.9301 | 181.24 | 172.395 | 0.1535 | watch_only | none |
| DELL | ai_server_oem | 390.86 |  | 375.4552 | 4.103 | 402 | 374.02 | 2.6199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.13 |  | 44.4531 | 1.5228 | 46.19 | 44.33 | 0.0665 | watch_only | none |
| SMCI | ai_server_oem | 28.45 |  | 28.0089 | 1.5748 | 28.86 | 27.59 | 0.0703 | watch_only | none |
| SPY | market_regime | 741.91 |  | 739.6213 | 0.3094 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.48 |  | 292.4316 | 0.3585 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 122.28 |  | 118.6681 | 3.0437 | 117.17 | 115.25 | 0.6869 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.83 |  | 66.2656 | 0.8518 | 68.995 | 65.635 | 2.6934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.88 |  | 266.1501 | 0.65 | 273.86 | 266.04 | 0.4554 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.875 |  | 381.3728 | 1.1805 | 384.565 | 377.43 | 4.3486 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 587.38 |  | 582.5846 | 0.8231 | 603.25 | 584.69 | 0.189 | watch_only | none |
| GEV | data_center_power_cooling | 936.73 |  | 937.5047 | -0.0826 | 955.825 | 935.665 | 1.2811 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 467.86 |  | 465.3755 | 0.5339 | 477.73 | 460.77 | 5.0271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.86 |  | 138.6985 | 1.5584 | 139.755 | 137.31 | 4.5932 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 169.64 |  | 165.1404 | 2.7247 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 242.96 |  | 237.6615 | 2.2294 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 646.74 |  | 632.3928 | 2.2687 | 673.65 | 624.91 | 4.0294 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 344.175 |  | 337.5114 | 1.9743 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.2 |  | 85.8634 | 2.7214 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 262.535 |  | 259.174 | 1.2968 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1590.32 |  | 1577.429 | 0.8172 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 480.165 |  | 476.3781 | 0.7949 | 494.87 | 477.03 | 1.1329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 272.66 |  | 266.7951 | 2.1983 | 276.85 | 267.14 | 2.8497 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 192.995 |  | 190.8159 | 1.142 | 194.96 | 189.48 | 2.083 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 315.99 |  | 308.9383 | 2.2826 | 315.21 | 304.11 | 3.3261 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 239.465 |  | 237.0631 | 1.0132 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.24 |  | 46.6734 | -0.9286 | 51.64 | 47.435 | 0.1514 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.47 |  | 42.4356 | 0.0811 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.61 |  | 119.1644 | 0.374 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 285.27 |  | 282.3758 | 1.0249 | 296.8 | 283.22 | 0.5223 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.68 |  | 518.0535 | -0.4582 | 518.6 | 511.495 | 0.254 | below_vwap | below_vwap |
| APD | industrial_gases | 295.3 |  | 295.7415 | -0.1493 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.45 |  | 26.5112 | -0.2307 | 27 | 25.42 | 2.155 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.69 |  | 33.7068 | -0.0498 | 35.08 | 33.52 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.135 |  | 20.1358 | 4.9625 | 20.97 | 19.755 | 0.1419 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1111.5 |  | 1099.2421 | 1.1151 | 1185.19 | 1114.57 | 0.9213 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 459.085 |  | 440.5271 | 4.2127 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 749.01 |  | 732.8269 | 2.2083 | 774.805 | 719.02 | 0.3084 | watch_only | none |
| AMZN | cloud_ai_capex | 231.33 |  | 230.5239 | 0.3497 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.98 |  | 593.8422 | 0.1916 | 600.765 | 594.21 | 0.284 | watch_only | none |
| ARM | ai_accelerator | 245.85 |  | 245.2195 | 0.2571 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 131.53 |  | 131.5242 | 0.0044 | 136.45 | 131.735 | 2.5089 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
