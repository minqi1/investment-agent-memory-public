# Intraday State

- Generated at: `2026-07-23T01:14:00+08:00`
- Market time ET: `2026-07-22T13:14:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 7, 'watch_only': 2, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 1, 'below_vwap': 11}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.11 |  | 707.3273 | 0.252 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 560.09 |  | 552.8308 | 1.3131 | 551.02 | 540.105 | 0.0571 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.385 |  | 585.0991 | 1.0743 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.49 |  | 748.4695 | 0.1363 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.85 |  | 211.0341 | 1.3343 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.6 |  | 420.6647 | 0.46 | 419.42 | 414.87 | 0.2035 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 560.09 |  | 552.8308 | 1.3131 | 551.02 | 540.105 | 0.0571 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 591.385 |  | 585.0991 | 1.0743 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.75 |  | 211.1172 | 1.2471 | 207.06 | 202.18 | 0.2105 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.11 |  | 707.3273 | 0.252 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.49 |  | 748.4695 | 0.1363 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1810.255 |  | 1796.8895 | 0.7438 | 1786.525 | 1767.54 | 0.0309 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 216.9 |  | 216.0753 | 0.3817 | 215.465 | 210.975 | 0.0277 | buy_precheck_manual_confirm | none |
| 10 | AMAT | semiconductor_equipment | 560.34 |  | 558.403 | 0.3469 | 559.22 | 544.305 | 0.0714 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.3 |  | 31.177 | 0.3945 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 83.8 |  | 83.521 | 0.334 | 83.22 | 79.6 | 0.1671 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.41 |  | 70.8362 | 0.81 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.49 |  | 748.4695 | 0.1363 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 560.34 |  | 558.403 | 0.3469 | 559.22 | 544.305 | 0.0714 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.11 |  | 707.3273 | 0.252 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 4 | CRWV | gpu_cloud_ai_factory | 83.8 |  | 83.521 | 0.334 | 83.22 | 79.6 | 0.1671 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 216.9 |  | 216.0753 | 0.3817 | 215.465 | 210.975 | 0.0277 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 347.97 |  | 347.9442 | 0.0074 | 348.76 | 346.23 | 0.0489 | watch_only | none |
| 7 | ETN | data_center_power_cooling | 409.07 |  | 407.8891 | 0.2895 | 409.095 | 398.16 | 0.132 | watch_only | none |
| 8 | TSM | foundry | 422.6 |  | 420.6647 | 0.46 | 419.42 | 414.87 | 0.2035 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1810.255 |  | 1796.8895 | 0.7438 | 1786.525 | 1767.54 | 0.0309 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.3 |  | 31.177 | 0.3945 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| 11 | NVDA | ai_accelerator | 213.85 |  | 211.0341 | 1.3343 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 12 | JCI | data_center_power_cooling | 143.12 |  | 142.8977 | 0.1556 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 139.15 |  | 138.7427 | 0.2936 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 295.5 |  | 295.3356 | 0.0557 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SOXX | semiconductor_index | 560.09 |  | 552.8308 | 1.3131 | 551.02 | 540.105 | 0.0571 | buy_precheck_manual_confirm | none |
| 17 | SMH | semiconductor_index | 591.385 |  | 585.0991 | 1.0743 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| 18 | ARM | ai_accelerator | 286.59 |  | 285.6395 | 0.3328 | 286.39 | 280.275 | 2.3902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ANET | ai_networking_optical | 175.4 |  | 174.8483 | 0.3155 | 175.265 | 171.06 | 2.6796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 213.75 |  | 211.1172 | 1.2471 | 207.06 | 202.18 | 0.2105 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.85 |  | 211.0341 | 1.3343 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.6 |  | 420.6647 | 0.46 | 419.42 | 414.87 | 0.2035 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 560.09 |  | 552.8308 | 1.3131 | 551.02 | 540.105 | 0.0571 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 591.385 |  | 585.0991 | 1.0743 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.75 |  | 211.1172 | 1.2471 | 207.06 | 202.18 | 0.2105 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.11 |  | 707.3273 | 0.252 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.49 |  | 748.4695 | 0.1363 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1810.255 |  | 1796.8895 | 0.7438 | 1786.525 | 1767.54 | 0.0309 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 216.9 |  | 216.0753 | 0.3817 | 215.465 | 210.975 | 0.0277 | buy_precheck_manual_confirm | none |
| 10 | AMAT | semiconductor_equipment | 560.34 |  | 558.403 | 0.3469 | 559.22 | 544.305 | 0.0714 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.3 |  | 31.177 | 0.3945 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 83.8 |  | 83.521 | 0.334 | 83.22 | 79.6 | 0.1671 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.41 |  | 70.8362 | 0.81 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 14 | DELL | ai_server_oem | 442.57 |  | 442.7189 | -0.0336 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | MU | memory_hbm_storage | 976.345 |  | 967.2597 | 0.9393 | 963.41 | 936.99 | 0.6115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 556.815 |  | 551.36 | 0.9894 | 548.755 | 526.6 | 2.7783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 476.11 |  | 473.261 | 0.602 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SNDK | memory_hbm_storage | 1616.135 |  | 1576.9827 | 2.4827 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 561.67 |  | 555.5758 | 1.0969 | 548.14 | 526.22 | 1.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 916.27 |  | 908.4582 | 0.8599 | 899.59 | 860.605 | 0.4671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.11 |  | 707.3273 | 0.252 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.41 |  | 70.8362 | 0.81 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.85 |  | 211.0341 | 1.3343 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.695 |  | 390.4295 | -0.4443 | 400.89 | 392.26 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.7 |  | 325.2127 | -0.4651 | 328.865 | 325.74 | 0.2101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.97 |  | 347.9442 | 0.0074 | 348.76 | 346.23 | 0.0489 | watch_only | none |
| AMD | ai_accelerator | 556.815 |  | 551.36 | 0.9894 | 548.755 | 526.6 | 2.7783 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.6 |  | 420.6647 | 0.46 | 419.42 | 414.87 | 0.2035 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 560.09 |  | 552.8308 | 1.3131 | 551.02 | 540.105 | 0.0571 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.385 |  | 585.0991 | 1.0743 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.985 |  | 389.9333 | 1.8084 | 387.635 | 380.205 | 4.184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 976.345 |  | 967.2597 | 0.9393 | 963.41 | 936.99 | 0.6115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.75 |  | 211.1172 | 1.2471 | 207.06 | 202.18 | 0.2105 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 442.57 |  | 442.7189 | -0.0336 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.82 |  | 49.0328 | -0.434 | 48.96 | 47.01 | 0.041 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.3 |  | 31.177 | 0.3945 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.49 |  | 748.4695 | 0.1363 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.45 |  | 295.156 | -0.2392 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.6 |  | 126.6874 | -0.069 | 128.79 | 125.83 | 0.0474 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.8 |  | 83.521 | 0.334 | 83.22 | 79.6 | 0.1671 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 301.04 |  | 298.8686 | 0.7265 | 297.69 | 293.905 | 1.342 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 409.07 |  | 407.8891 | 0.2895 | 409.095 | 398.16 | 0.132 | watch_only | none |
| PWR | data_center_power_cooling | 643.805 |  | 640.379 | 0.535 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 994.49 |  | 1008.1356 | -1.3535 | 1036.605 | 998.94 | 1.1574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.11 |  | 473.261 | 0.602 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.12 |  | 142.8977 | 0.1556 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.4 |  | 174.8483 | 0.3155 | 175.265 | 171.06 | 2.6796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.43 |  | 316.1732 | -0.2351 | 317.93 | 306.89 | 2.6789 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 833.54 |  | 840.7104 | -0.8529 | 840.47 | 814.62 | 3.3604 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 403.65 |  | 405.951 | -0.5668 | 407.12 | 397.835 | 2.138 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.79 |  | 114.6754 | -1.6441 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 334.54 |  | 329.1584 | 1.635 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1810.255 |  | 1796.8895 | 0.7438 | 1786.525 | 1767.54 | 0.0309 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.34 |  | 558.403 | 0.3469 | 559.22 | 544.305 | 0.0714 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.22 |  | 318.9411 | 0.7145 | 317.72 | 311.31 | 4.0657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.9 |  | 216.0753 | 0.3817 | 215.465 | 210.975 | 0.0277 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 373.06 |  | 371.52 | 0.4145 | 369.53 | 365 | 4.8303 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.5 |  | 295.3356 | 0.0557 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.72 |  | 67.4749 | 0.3632 | 66.73 | 64.98 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.15 |  | 138.7427 | 0.2936 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346.875 |  | 343.7268 | 0.9159 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.36 |  | 507.2072 | 0.4244 | 507.545 | 505.59 | 4.4232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.64 |  | 297.7588 | -0.0399 | 300.24 | 297.585 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.355 |  | 30.7839 | -1.3931 | 30.78 | 29.46 | 0.0659 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.02 |  | 42.6904 | -1.5705 | 42.29 | 40.305 | 0.0714 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.925 |  | 24.131 | -0.8535 | 24.255 | 23.58 | 0.0836 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1616.135 |  | 1576.9827 | 2.4827 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 561.67 |  | 555.5758 | 1.0969 | 548.14 | 526.22 | 1.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 916.27 |  | 908.4582 | 0.8599 | 899.59 | 860.605 | 0.4671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.42 |  | 244.4957 | -0.4399 | 248.43 | 244.47 | 0.0205 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 630.23 |  | 631.2819 | -0.1666 | 647.02 | 632.77 | 0.073 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 286.59 |  | 285.6395 | 0.3328 | 286.39 | 280.275 | 2.3902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.96 |  | 166.7564 | 1.3214 | 166.63 | 162.08 | 1.0121 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
