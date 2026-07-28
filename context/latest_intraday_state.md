# Intraday State

- Generated at: `2026-07-29T00:12:39+08:00`
- Market time ET: `2026-07-28T12:12:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'watch_only': 16, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 2, 'below_vwap': 5, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.98 |  | 673.3029 | 0.6946 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 495.06 |  | 489.483 | 1.1394 | 497.64 | 485.42 | 0.0788 | watch_only | none |
| SMH | semiconductor_index | 532.46 |  | 526.7944 | 1.0755 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| SPY | market_regime | 741.75 |  | 738.8508 | 0.3924 | 739.42 | 736.57 | 0.0337 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.995 |  | 195.521 | 1.2653 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.93 |  | 386.7348 | 1.3433 | 390.46 | 382.495 | 0.0791 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 383.44 |  | 377.7472 | 1.507 | 378.64 | 371.57 | 0.0496 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.75 |  | 738.8508 | 0.3924 | 739.42 | 736.57 | 0.0337 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 677.98 |  | 673.3029 | 0.6946 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 333.105 |  | 328.9805 | 1.2537 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.6 |  | 117.3961 | 2.7292 | 117.17 | 115.25 | 0.0746 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.18 |  | 60.8172 | 2.2407 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.75 |  | 738.8508 | 0.3924 | 739.42 | 736.57 | 0.0337 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 677.98 |  | 673.3029 | 0.6946 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 292.94 |  | 292.0255 | 0.3132 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 397.255 |  | 395.8093 | 0.3652 | 400.09 | 392.355 | 0.0654 | watch_only | none |
| 5 | AMZN | cloud_ai_capex | 231.23 |  | 230.0341 | 0.5199 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| 6 | TSM | foundry | 391.93 |  | 386.7348 | 1.3433 | 390.46 | 382.495 | 0.0791 | buy_precheck_manual_confirm | none |
| 7 | AAPL | mega_cap_platform | 339.88 |  | 338.6734 | 0.3563 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 8 | META | cloud_ai_capex | 596.59 |  | 593.56 | 0.5105 | 600.765 | 594.21 | 0.171 | watch_only | none |
| 9 | NVDA | ai_accelerator | 197.995 |  | 195.521 | 1.2653 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 10 | GOOGL | cloud_ai_capex | 333.105 |  | 328.9805 | 1.2537 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| 11 | ARM | ai_accelerator | 245.82 |  | 245.1168 | 0.2869 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SMH | semiconductor_index | 532.46 |  | 526.7944 | 1.0755 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| 13 | SOXX | semiconductor_index | 495.06 |  | 489.483 | 1.1394 | 497.64 | 485.42 | 0.0788 | watch_only | none |
| 14 | KLAC | semiconductor_equipment | 192.415 |  | 190.4702 | 1.0211 | 194.96 | 189.48 | 0.1091 | watch_only | none |
| 15 | HPE | ai_server_oem | 44.98 |  | 44.407 | 1.2903 | 46.19 | 44.33 | 0.1112 | watch_only | none |
| 16 | ASML | semiconductor_equipment | 1586.03 |  | 1575.8384 | 0.6467 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 588.725 |  | 580.7339 | 1.376 | 603.25 | 584.69 | 0.3499 | watch_only | none |
| 18 | SKHY | memory_hbm_storage | 132.64 |  | 131.5253 | 0.8475 | 136.45 | 131.735 | 0.3317 | watch_only | none |
| 19 | AVGO | custom_silicon_networking | 383.44 |  | 377.7472 | 1.507 | 378.64 | 371.57 | 0.0496 | buy_precheck_manual_confirm | none |
| 20 | JCI | data_center_power_cooling | 139.13 |  | 138.0619 | 0.7737 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.995 |  | 195.521 | 1.2653 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.93 |  | 386.7348 | 1.3433 | 390.46 | 382.495 | 0.0791 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 383.44 |  | 377.7472 | 1.507 | 378.64 | 371.57 | 0.0496 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.75 |  | 738.8508 | 0.3924 | 739.42 | 736.57 | 0.0337 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 677.98 |  | 673.3029 | 0.6946 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 333.105 |  | 328.9805 | 1.2537 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.6 |  | 117.3961 | 2.7292 | 117.17 | 115.25 | 0.0746 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.18 |  | 60.8172 | 2.2407 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1586.03 |  | 1575.8384 | 0.6467 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ANET | ai_networking_optical | 167.13 |  | 163.5396 | 2.1954 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 386.315 |  | 379.6782 | 1.748 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SMH | semiconductor_index | 532.46 |  | 526.7944 | 1.0755 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| 13 | SOXX | semiconductor_index | 495.06 |  | 489.483 | 1.1394 | 497.64 | 485.42 | 0.0788 | watch_only | none |
| 14 | PWR | data_center_power_cooling | 588.725 |  | 580.7339 | 1.376 | 603.25 | 584.69 | 0.3499 | watch_only | none |
| 15 | WDC | memory_hbm_storage | 452.53 |  | 435.9194 | 3.8105 | 465.04 | 435.22 | 0.2077 | watch_only | none |
| 16 | IWM | market_regime | 292.94 |  | 292.0255 | 0.3132 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 17 | SKHY | memory_hbm_storage | 132.64 |  | 131.5253 | 0.8475 | 136.45 | 131.735 | 0.3317 | watch_only | none |
| 18 | KLAC | semiconductor_equipment | 192.415 |  | 190.4702 | 1.0211 | 194.96 | 189.48 | 0.1091 | watch_only | none |
| 19 | APLD | high_beta_ai_infrastructure | 27.03 |  | 26.5169 | 1.9352 | 27 | 25.42 | 3.5886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | META | cloud_ai_capex | 596.59 |  | 593.56 | 0.5105 | 600.765 | 594.21 | 0.171 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.98 |  | 673.3029 | 0.6946 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.18 |  | 60.8172 | 2.2407 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.995 |  | 195.521 | 1.2653 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.255 |  | 395.8093 | 0.3652 | 400.09 | 392.355 | 0.0654 | watch_only | none |
| AAPL | mega_cap_platform | 339.88 |  | 338.6734 | 0.3563 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.105 |  | 328.9805 | 1.2537 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 461.97 |  | 454.4678 | 1.6508 | 472.485 | 453.76 | 4.2232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.93 |  | 386.7348 | 1.3433 | 390.46 | 382.495 | 0.0791 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.06 |  | 489.483 | 1.1394 | 497.64 | 485.42 | 0.0788 | watch_only | none |
| SMH | semiconductor_index | 532.46 |  | 526.7944 | 1.0755 | 533.01 | 523.325 | 0.0413 | watch_only | none |
| AVGO | custom_silicon_networking | 383.44 |  | 377.7472 | 1.507 | 378.64 | 371.57 | 0.0496 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 821.3 |  | 813.7411 | 0.9289 | 846.4 | 813.91 | 1.0763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 177.94 |  | 173.5662 | 2.52 | 181.24 | 172.395 | 1.36 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 384.1 |  | 373.5062 | 2.8363 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.98 |  | 44.407 | 1.2903 | 46.19 | 44.33 | 0.1112 | watch_only | none |
| SMCI | ai_server_oem | 28.365 |  | 27.8682 | 1.7826 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.75 |  | 738.8508 | 0.3924 | 739.42 | 736.57 | 0.0337 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.94 |  | 292.0255 | 0.3132 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.6 |  | 117.3961 | 2.7292 | 117.17 | 115.25 | 0.0746 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.99 |  | 66.0252 | 1.4612 | 68.995 | 65.635 | 3.2094 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.38 |  | 266.0588 | 0.8724 | 273.86 | 266.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 386.315 |  | 379.6782 | 1.748 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 588.725 |  | 580.7339 | 1.376 | 603.25 | 584.69 | 0.3499 | watch_only | none |
| GEV | data_center_power_cooling | 950.62 |  | 935.6353 | 1.6016 | 955.825 | 935.665 | 5.1061 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 467.13 |  | 464.5316 | 0.5594 | 477.73 | 460.77 | 4.9622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.13 |  | 138.0619 | 0.7737 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.13 |  | 163.5396 | 2.1954 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 239.68 |  | 236.0913 | 1.52 | 256.145 | 236.73 | 1.6689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 644.36 |  | 627.3581 | 2.7101 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 343.33 |  | 336.4393 | 2.0481 | 354.09 | 338.14 | 5.103 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.24 |  | 85.3263 | 2.2428 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.705 |  | 257.7327 | 3.0932 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1586.03 |  | 1575.8384 | 0.6467 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 477.93 |  | 477.314 | 0.1291 | 494.87 | 477.03 | 0.7093 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 268.915 |  | 265.8595 | 1.1493 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 192.415 |  | 190.4702 | 1.0211 | 194.96 | 189.48 | 0.1091 | watch_only | none |
| TER | semiconductor_test_packaging | 312.45 |  | 307.1122 | 1.7381 | 315.21 | 304.11 | 0.1248 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.04 |  | 236.4521 | 0.6715 | 248.8 | 236.42 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 45.9 |  | 47.009 | -2.3592 | 51.64 | 47.435 | 0.1961 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.27 |  | 42.546 | -0.6486 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.13 |  | 119.461 | -0.2771 | 121 | 117.72 | 0.3693 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 284.695 |  | 281.9377 | 0.978 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 518.32 |  | 518.5299 | -0.0405 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.57 |  | 295.9127 | -0.1158 | 297.25 | 293.555 | 0.4703 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.03 |  | 26.5169 | 1.9352 | 27 | 25.42 | 3.5886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.29 |  | 33.6312 | 1.959 | 35.08 | 33.52 | 0.0583 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.415 |  | 19.9854 | 2.1497 | 20.97 | 19.755 | 0.049 | watch_only | none |
| SNDK | memory_hbm_storage | 1109.84 |  | 1102.8579 | 0.6331 | 1185.19 | 1114.57 | 0.2153 | below_opening_15m_low | below_opening_15m_low |
| WDC | memory_hbm_storage | 452.53 |  | 435.9194 | 3.8105 | 465.04 | 435.22 | 0.2077 | watch_only | none |
| STX | memory_hbm_storage | 745.63 |  | 724.3574 | 2.9368 | 774.805 | 719.02 | 1.7194 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.23 |  | 230.0341 | 0.5199 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| META | cloud_ai_capex | 596.59 |  | 593.56 | 0.5105 | 600.765 | 594.21 | 0.171 | watch_only | none |
| ARM | ai_accelerator | 245.82 |  | 245.1168 | 0.2869 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.64 |  | 131.5253 | 0.8475 | 136.45 | 131.735 | 0.3317 | watch_only | none |
