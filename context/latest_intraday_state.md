# Intraday State

- Generated at: `2026-07-29T03:51:25+08:00`
- Market time ET: `2026-07-28T15:51:26-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 18, 'manual_confirm_candidate': 6, 'below_vwap': 8, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 1, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676 |  | 674.4493 | 0.2299 | 677.3 | 670.84 | 0.0222 | watch_only | none |
| SOXX | semiconductor_index | 493.94 |  | 490.4368 | 0.7143 | 497.64 | 485.42 | 0.0729 | watch_only | none |
| SMH | semiconductor_index | 531.29 |  | 527.9298 | 0.6365 | 533.01 | 523.325 | 0.032 | watch_only | none |
| SPY | market_regime | 740.91 |  | 739.8805 | 0.1391 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.165 |  | 196.2663 | 0.4579 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.91 |  | 739.8805 | 0.1391 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 333.595 |  | 331.6705 | 0.5802 | 330.21 | 324.97 | 0.0899 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.7 |  | 139.1495 | 1.1143 | 139.755 | 137.31 | 0.0355 | buy_precheck_manual_confirm | none |
| 5 | ETN | data_center_power_cooling | 386.67 |  | 381.8188 | 1.2705 | 384.565 | 377.43 | 0.3103 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.35 |  | 119.0027 | 1.1322 | 117.17 | 115.25 | 0.0997 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.91 |  | 739.8805 | 0.1391 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 676 |  | 674.4493 | 0.2299 | 677.3 | 670.84 | 0.0222 | watch_only | none |
| 3 | IWM | market_regime | 293.15 |  | 292.5059 | 0.2202 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 4 | NVDA | ai_accelerator | 197.165 |  | 196.2663 | 0.4579 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 230.8 |  | 230.574 | 0.098 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 333.595 |  | 331.6705 | 0.5802 | 330.21 | 324.97 | 0.0899 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 339.96 |  | 339.0237 | 0.2762 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 8 | MU | memory_hbm_storage | 820.655 |  | 816.6619 | 0.4889 | 846.4 | 813.91 | 0.0463 | watch_only | none |
| 9 | SMH | semiconductor_index | 531.29 |  | 527.9298 | 0.6365 | 533.01 | 523.325 | 0.032 | watch_only | none |
| 10 | SOXX | semiconductor_index | 493.94 |  | 490.4368 | 0.7143 | 497.64 | 485.42 | 0.0729 | watch_only | none |
| 11 | AMAT | semiconductor_equipment | 478.835 |  | 477.0182 | 0.3809 | 494.87 | 477.03 | 0.1253 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 33.875 |  | 33.7419 | 0.3945 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| 13 | JCI | data_center_power_cooling | 140.7 |  | 139.1495 | 1.1143 | 139.755 | 137.31 | 0.0355 | buy_precheck_manual_confirm | none |
| 14 | MRVL | custom_silicon_networking | 175.425 |  | 174.3927 | 0.5919 | 181.24 | 172.395 | 0.2508 | watch_only | none |
| 15 | ETN | data_center_power_cooling | 386.67 |  | 381.8188 | 1.2705 | 384.565 | 377.43 | 0.3103 | buy_precheck_manual_confirm | none |
| 16 | ORCL | cloud_ai_capex | 120.35 |  | 119.0027 | 1.1322 | 117.17 | 115.25 | 0.0997 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 28.415 |  | 28.0578 | 1.273 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 18 | ASML | semiconductor_equipment | 1585.92 |  | 1578.9031 | 0.4444 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | KLAC | semiconductor_equipment | 194.04 |  | 191.32 | 1.4217 | 194.96 | 189.48 | 0.201 | watch_only | none |
| 20 | GEV | data_center_power_cooling | 940.24 |  | 937.7752 | 0.2628 | 955.825 | 935.665 | 0.4031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.165 |  | 196.2663 | 0.4579 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.91 |  | 739.8805 | 0.1391 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 333.595 |  | 331.6705 | 0.5802 | 330.21 | 324.97 | 0.0899 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.7 |  | 139.1495 | 1.1143 | 139.755 | 137.31 | 0.0355 | buy_precheck_manual_confirm | none |
| 5 | ETN | data_center_power_cooling | 386.67 |  | 381.8188 | 1.2705 | 384.565 | 377.43 | 0.3103 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.35 |  | 119.0027 | 1.1322 | 117.17 | 115.25 | 0.0997 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 393.85 |  | 389.1207 | 1.2154 | 390.46 | 382.495 | 1.0486 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AVGO | custom_silicon_networking | 384.58 |  | 379.283 | 1.3966 | 378.64 | 371.57 | 3.3907 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 168.775 |  | 165.3905 | 2.0463 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TER | semiconductor_test_packaging | 319.9 |  | 311.0106 | 2.8582 | 315.21 | 304.11 | 0.497 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | MU | memory_hbm_storage | 820.655 |  | 816.6619 | 0.4889 | 846.4 | 813.91 | 0.0463 | watch_only | none |
| 12 | SMH | semiconductor_index | 531.29 |  | 527.9298 | 0.6365 | 533.01 | 523.325 | 0.032 | watch_only | none |
| 13 | SOXX | semiconductor_index | 493.94 |  | 490.4368 | 0.7143 | 497.64 | 485.42 | 0.0729 | watch_only | none |
| 14 | QQQ | market_regime | 676 |  | 674.4493 | 0.2299 | 677.3 | 670.84 | 0.0222 | watch_only | none |
| 15 | WDC | memory_hbm_storage | 460.18 |  | 443.1532 | 3.8422 | 465.04 | 435.22 | 0.2086 | watch_only | none |
| 16 | IWM | market_regime | 293.15 |  | 292.5059 | 0.2202 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 17 | AMAT | semiconductor_equipment | 478.835 |  | 477.0182 | 0.3809 | 494.87 | 477.03 | 0.1253 | watch_only | none |
| 18 | KLAC | semiconductor_equipment | 194.04 |  | 191.32 | 1.4217 | 194.96 | 189.48 | 0.201 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 230.8 |  | 230.574 | 0.098 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 20 | HPE | ai_server_oem | 45.385 |  | 44.7057 | 1.5194 | 46.19 | 44.33 | 0.0661 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676 |  | 674.4493 | 0.2299 | 677.3 | 670.84 | 0.0222 | watch_only | none |
| TQQQ | leveraged_tool | 61.7 |  | 61.1907 | 0.8324 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.165 |  | 196.2663 | 0.4579 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.18 |  | 396.0854 | -0.7335 | 400.09 | 392.355 | 0.0382 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.96 |  | 339.0237 | 0.2762 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.595 |  | 331.6705 | 0.5802 | 330.21 | 324.97 | 0.0899 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.37 |  | 456.1182 | 0.0552 | 472.485 | 453.76 | 4.6804 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.85 |  | 389.1207 | 1.2154 | 390.46 | 382.495 | 1.0486 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.94 |  | 490.4368 | 0.7143 | 497.64 | 485.42 | 0.0729 | watch_only | none |
| SMH | semiconductor_index | 531.29 |  | 527.9298 | 0.6365 | 533.01 | 523.325 | 0.032 | watch_only | none |
| AVGO | custom_silicon_networking | 384.58 |  | 379.283 | 1.3966 | 378.64 | 371.57 | 3.3907 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 820.655 |  | 816.6619 | 0.4889 | 846.4 | 813.91 | 0.0463 | watch_only | none |
| MRVL | custom_silicon_networking | 175.425 |  | 174.3927 | 0.5919 | 181.24 | 172.395 | 0.2508 | watch_only | none |
| DELL | ai_server_oem | 390.005 |  | 376.8748 | 3.484 | 402 | 374.02 | 0.1205 | watch_only | none |
| HPE | ai_server_oem | 45.385 |  | 44.7057 | 1.5194 | 46.19 | 44.33 | 0.0661 | watch_only | none |
| SMCI | ai_server_oem | 28.415 |  | 28.0578 | 1.273 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 740.91 |  | 739.8805 | 0.1391 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.15 |  | 292.5059 | 0.2202 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.35 |  | 119.0027 | 1.1322 | 117.17 | 115.25 | 0.0997 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.93 |  | 66.3296 | 0.9052 | 68.995 | 65.635 | 2.3756 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.09 |  | 266.4456 | 0.9925 | 273.86 | 266.04 | 4.7047 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.67 |  | 381.8188 | 1.2705 | 384.565 | 377.43 | 0.3103 | buy_precheck_manual_confirm | none |
| PWR | data_center_power_cooling | 587.89 |  | 583.5625 | 0.7416 | 603.25 | 584.69 | 2.1637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 940.24 |  | 937.7752 | 0.2628 | 955.825 | 935.665 | 0.4031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.09 |  | 466.1068 | 0.4255 | 477.73 | 460.77 | 4.67 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.7 |  | 139.1495 | 1.1143 | 139.755 | 137.31 | 0.0355 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 168.775 |  | 165.3905 | 2.0463 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 243.43 |  | 238.6357 | 2.0091 | 256.145 | 236.73 | 4.7242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 651.9 |  | 634.7492 | 2.702 | 673.65 | 624.91 | 2.0617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 349.36 |  | 338.41 | 3.2357 | 354.09 | 338.14 | 0.2633 | watch_only | none |
| AAOI | ai_networking_optical | 88.11 |  | 86.1737 | 2.247 | 92.95 | 84.63 | 5.0959 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 262.76 |  | 259.9035 | 1.0991 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1585.92 |  | 1578.9031 | 0.4444 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 478.835 |  | 477.0182 | 0.3809 | 494.87 | 477.03 | 0.1253 | watch_only | none |
| LRCX | semiconductor_equipment | 270.77 |  | 267.3909 | 1.2637 | 276.85 | 267.14 | 1.7543 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 194.04 |  | 191.32 | 1.4217 | 194.96 | 189.48 | 0.201 | watch_only | none |
| TER | semiconductor_test_packaging | 319.9 |  | 311.0106 | 2.8582 | 315.21 | 304.11 | 0.497 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 239.71 |  | 237.3483 | 0.995 | 248.8 | 236.42 | 0.8761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.92 |  | 46.631 | -1.5246 | 51.64 | 47.435 | 0.3267 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.32 |  | 42.4904 | -0.4011 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.79 |  | 119.2031 | -0.3466 | 121 | 117.72 | 0.261 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 284.89 |  | 282.7725 | 0.7489 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.52 |  | 517.6544 | -0.9919 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.2 |  | 295.6329 | -0.4847 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.48 |  | 26.539 | -0.2224 | 27 | 25.42 | 0.1888 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.875 |  | 33.7419 | 0.3945 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.755 |  | 20.2172 | 2.6602 | 20.97 | 19.755 | 0.0482 | watch_only | none |
| SNDK | memory_hbm_storage | 1112.195 |  | 1101.2326 | 0.9955 | 1185.19 | 1114.57 | 4.136 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 460.18 |  | 443.1532 | 3.8422 | 465.04 | 435.22 | 0.2086 | watch_only | none |
| STX | memory_hbm_storage | 743.81 |  | 734.6349 | 1.2489 | 774.805 | 719.02 | 4.6665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.8 |  | 230.574 | 0.098 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.12 |  | 593.8276 | 0.0492 | 600.765 | 594.21 | 0.0791 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 244.29 |  | 245.2983 | -0.4111 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.215 |  | 131.5495 | -1.0145 | 136.45 | 131.735 | 0.1613 | below_opening_15m_low | below_opening_15m_low,below_vwap |
