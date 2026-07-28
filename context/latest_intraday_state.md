# Intraday State

- Generated at: `2026-07-29T03:43:45+08:00`
- Market time ET: `2026-07-28T15:43:46-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 17, 'manual_confirm_candidate': 6, 'below_vwap': 7, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.3 |  | 674.4105 | 0.2802 | 677.3 | 670.84 | 0.034 | watch_only | none |
| SOXX | semiconductor_index | 493.73 |  | 490.344 | 0.6905 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| SMH | semiconductor_index | 531.23 |  | 527.8007 | 0.6497 | 533.01 | 523.325 | 0.0358 | watch_only | none |
| SPY | market_regime | 741.11 |  | 739.8276 | 0.1733 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.23 |  | 196.2465 | 0.5012 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.64 |  | 388.8155 | 1.2408 | 390.46 | 382.495 | 0.1423 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.11 |  | 739.8276 | 0.1733 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.29 |  | 331.5555 | 0.8247 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.58 |  | 118.957 | 1.3643 | 117.17 | 115.25 | 0.0332 | buy_precheck_manual_confirm | none |
| 6 | TER | semiconductor_test_packaging | 319.72 |  | 310.5054 | 2.9676 | 315.21 | 304.11 | 0.1783 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.11 |  | 739.8276 | 0.1733 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 676.3 |  | 674.4105 | 0.2802 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 3 | IWM | market_regime | 293.1 |  | 292.4875 | 0.2094 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | NVDA | ai_accelerator | 197.23 |  | 196.2465 | 0.5012 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 230.93 |  | 230.5661 | 0.1578 | 233.05 | 229.7 | 0.0217 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 339.845 |  | 339.0068 | 0.2473 | 342.87 | 337.78 | 0.0177 | watch_only | none |
| 7 | SMH | semiconductor_index | 531.23 |  | 527.8007 | 0.6497 | 533.01 | 523.325 | 0.0358 | watch_only | none |
| 8 | SOXX | semiconductor_index | 493.73 |  | 490.344 | 0.6905 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| 9 | TT | data_center_power_cooling | 468.03 |  | 465.9595 | 0.4443 | 477.73 | 460.77 | 0.2949 | watch_only | none |
| 10 | AMAT | semiconductor_equipment | 479.91 |  | 476.9351 | 0.6238 | 494.87 | 477.03 | 0.2 | watch_only | none |
| 11 | APLD | high_beta_ai_infrastructure | 26.68 |  | 26.5382 | 0.5344 | 27 | 25.42 | 0.075 | watch_only | none |
| 12 | TSM | foundry | 393.64 |  | 388.8155 | 1.2408 | 390.46 | 382.495 | 0.1423 | buy_precheck_manual_confirm | none |
| 13 | GOOGL | cloud_ai_capex | 334.29 |  | 331.5555 | 0.8247 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 14 | ORCL | cloud_ai_capex | 120.58 |  | 118.957 | 1.3643 | 117.17 | 115.25 | 0.0332 | buy_precheck_manual_confirm | none |
| 15 | HPE | ai_server_oem | 45.32 |  | 44.6636 | 1.4696 | 46.19 | 44.33 | 0.0662 | watch_only | none |
| 16 | SMCI | ai_server_oem | 28.4 |  | 28.0469 | 1.2589 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 34.145 |  | 33.7336 | 1.2196 | 35.08 | 33.52 | 0.0293 | watch_only | none |
| 18 | GEV | data_center_power_cooling | 940.21 |  | 937.6734 | 0.2705 | 955.825 | 935.665 | 0.352 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | CRWV | gpu_cloud_ai_factory | 67.155 |  | 66.308 | 1.2773 | 68.995 | 65.635 | 0.1787 | watch_only | none |
| 20 | ASML | semiconductor_equipment | 1587.28 |  | 1578.7288 | 0.5416 | 1586.01 | 1565.95 | 2.3279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.23 |  | 196.2465 | 0.5012 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.64 |  | 388.8155 | 1.2408 | 390.46 | 382.495 | 0.1423 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.11 |  | 739.8276 | 0.1733 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.29 |  | 331.5555 | 0.8247 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.58 |  | 118.957 | 1.3643 | 117.17 | 115.25 | 0.0332 | buy_precheck_manual_confirm | none |
| 6 | TER | semiconductor_test_packaging | 319.72 |  | 310.5054 | 2.9676 | 315.21 | 304.11 | 0.1783 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 383.995 |  | 379.1537 | 1.2769 | 378.64 | 371.57 | 3.2631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1587.28 |  | 1578.7288 | 0.5416 | 1586.01 | 1565.95 | 2.3279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 169.14 |  | 165.3027 | 2.3214 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 140.39 |  | 139.0605 | 0.9561 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 386.1 |  | 381.6954 | 1.154 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SMH | semiconductor_index | 531.23 |  | 527.8007 | 0.6497 | 533.01 | 523.325 | 0.0358 | watch_only | none |
| 13 | SOXX | semiconductor_index | 493.73 |  | 490.344 | 0.6905 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| 14 | QQQ | market_regime | 676.3 |  | 674.4105 | 0.2802 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 15 | TT | data_center_power_cooling | 468.03 |  | 465.9595 | 0.4443 | 477.73 | 460.77 | 0.2949 | watch_only | none |
| 16 | IWM | market_regime | 293.1 |  | 292.4875 | 0.2094 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 17 | AMAT | semiconductor_equipment | 479.91 |  | 476.9351 | 0.6238 | 494.87 | 477.03 | 0.2 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 230.93 |  | 230.5661 | 0.1578 | 233.05 | 229.7 | 0.0217 | watch_only | none |
| 19 | HPE | ai_server_oem | 45.32 |  | 44.6636 | 1.4696 | 46.19 | 44.33 | 0.0662 | watch_only | none |
| 20 | CIEN | ai_networking_optical | 349.38 |  | 338.0739 | 3.3443 | 354.09 | 338.14 | 0.1574 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.3 |  | 674.4105 | 0.2802 | 677.3 | 670.84 | 0.034 | watch_only | none |
| TQQQ | leveraged_tool | 61.75 |  | 61.183 | 0.9267 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.23 |  | 196.2465 | 0.5012 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.24 |  | 396.1526 | -0.7352 | 400.09 | 392.355 | 0.8138 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 339.845 |  | 339.0068 | 0.2473 | 342.87 | 337.78 | 0.0177 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.29 |  | 331.5555 | 0.8247 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.33 |  | 456.0878 | 0.4916 | 472.485 | 453.76 | 1.8458 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.64 |  | 388.8155 | 1.2408 | 390.46 | 382.495 | 0.1423 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.73 |  | 490.344 | 0.6905 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| SMH | semiconductor_index | 531.23 |  | 527.8007 | 0.6497 | 533.01 | 523.325 | 0.0358 | watch_only | none |
| AVGO | custom_silicon_networking | 383.995 |  | 379.1537 | 1.2769 | 378.64 | 371.57 | 3.2631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 820.4 |  | 816.5427 | 0.4724 | 846.4 | 813.91 | 1.6407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.34 |  | 174.3638 | 0.5599 | 181.24 | 172.395 | 3.6843 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 389.93 |  | 376.5359 | 3.5572 | 402 | 374.02 | 0.277 | watch_only | none |
| HPE | ai_server_oem | 45.32 |  | 44.6636 | 1.4696 | 46.19 | 44.33 | 0.0662 | watch_only | none |
| SMCI | ai_server_oem | 28.4 |  | 28.0469 | 1.2589 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 741.11 |  | 739.8276 | 0.1733 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.1 |  | 292.4875 | 0.2094 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.58 |  | 118.957 | 1.3643 | 117.17 | 115.25 | 0.0332 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.155 |  | 66.308 | 1.2773 | 68.995 | 65.635 | 0.1787 | watch_only | none |
| VRT | data_center_power_cooling | 268.01 |  | 266.3834 | 0.6106 | 273.86 | 266.04 | 0.4142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.1 |  | 381.6954 | 1.154 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 588.18 |  | 583.3893 | 0.8212 | 603.25 | 584.69 | 2.2323 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 940.21 |  | 937.6734 | 0.2705 | 955.825 | 935.665 | 0.352 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.03 |  | 465.9595 | 0.4443 | 477.73 | 460.77 | 0.2949 | watch_only | none |
| JCI | data_center_power_cooling | 140.39 |  | 139.0605 | 0.9561 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 169.14 |  | 165.3027 | 2.3214 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 244.26 |  | 238.4711 | 2.4275 | 256.145 | 236.73 | 0.5813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 653.19 |  | 634.0208 | 3.0234 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 349.38 |  | 338.0739 | 3.3443 | 354.09 | 338.14 | 0.1574 | watch_only | none |
| AAOI | ai_networking_optical | 88.355 |  | 86.0936 | 2.6267 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 263.315 |  | 259.7988 | 1.3534 | 268.265 | 253.05 | 4.8079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1587.28 |  | 1578.7288 | 0.5416 | 1586.01 | 1565.95 | 2.3279 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 479.91 |  | 476.9351 | 0.6238 | 494.87 | 477.03 | 0.2 | watch_only | none |
| LRCX | semiconductor_equipment | 271.45 |  | 267.3042 | 1.551 | 276.85 | 267.14 | 3.7723 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.89 |  | 191.2358 | 1.3879 | 194.96 | 189.48 | 1.7536 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 319.72 |  | 310.5054 | 2.9676 | 315.21 | 304.11 | 0.1783 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 240.32 |  | 237.297 | 1.2739 | 248.8 | 236.42 | 4.8685 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.35 |  | 46.6492 | -0.6415 | 51.64 | 47.435 | 0.1079 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.42 |  | 42.4962 | -0.1794 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.04 |  | 119.2253 | -0.1554 | 121 | 117.72 | 0.1344 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 286.08 |  | 282.6947 | 1.1975 | 296.8 | 283.22 | 0.4719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.395 |  | 517.7703 | -0.845 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.94 |  | 295.686 | -0.2523 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.68 |  | 26.5382 | 0.5344 | 27 | 25.42 | 0.075 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.145 |  | 33.7336 | 1.2196 | 35.08 | 33.52 | 0.0293 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.855 |  | 20.1979 | 3.2531 | 20.97 | 19.755 | 0.0959 | watch_only | none |
| SNDK | memory_hbm_storage | 1106.78 |  | 1101.0513 | 0.5203 | 1185.19 | 1114.57 | 4.3342 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 460.025 |  | 442.6447 | 3.9265 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 745.505 |  | 734.2653 | 1.5307 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 230.93 |  | 230.5661 | 0.1578 | 233.05 | 229.7 | 0.0217 | watch_only | none |
| META | cloud_ai_capex | 593.385 |  | 593.8235 | -0.0738 | 600.765 | 594.21 | 0.118 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 245.27 |  | 245.3219 | -0.0211 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131.68 |  | 131.5635 | 0.0886 | 136.45 | 131.735 | 0.6531 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
