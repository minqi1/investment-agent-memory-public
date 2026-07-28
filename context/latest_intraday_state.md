# Intraday State

- Generated at: `2026-07-29T02:07:52+08:00`
- Market time ET: `2026-07-28T14:07:53-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 12, 'manual_confirm_candidate': 2, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_vwap': 9, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.36 |  | 674.0066 | 0.3492 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.8 |  | 489.9508 | 0.3774 | 497.64 | 485.42 | 0.0529 | watch_only | none |
| SMH | semiconductor_index | 529.92 |  | 527.317 | 0.4936 | 533.01 | 523.325 | 0.051 | watch_only | none |
| SPY | market_regime | 741.02 |  | 739.4626 | 0.2106 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.05 |  | 196.0026 | 0.5344 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.02 |  | 739.4626 | 0.2106 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.02 |  | 739.4626 | 0.2106 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 676.36 |  | 674.0066 | 0.3492 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 3 | IWM | market_regime | 293.03 |  | 292.3229 | 0.2419 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | KLAC | semiconductor_equipment | 191.18 |  | 190.7569 | 0.2218 | 194.96 | 189.48 | 0.1098 | watch_only | none |
| 5 | NVDA | ai_accelerator | 197.05 |  | 196.0026 | 0.5344 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 231.13 |  | 230.4528 | 0.2939 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 339.51 |  | 338.926 | 0.1723 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 8 | TSM | foundry | 390.2 |  | 387.55 | 0.6838 | 390.46 | 382.495 | 0.0692 | watch_only | none |
| 9 | SMH | semiconductor_index | 529.92 |  | 527.317 | 0.4936 | 533.01 | 523.325 | 0.051 | watch_only | none |
| 10 | SOXX | semiconductor_index | 491.8 |  | 489.9508 | 0.3774 | 497.64 | 485.42 | 0.0529 | watch_only | none |
| 11 | ASML | semiconductor_equipment | 1579.99 |  | 1577.1716 | 0.1787 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 379.69 |  | 378.5467 | 0.302 | 378.64 | 371.57 | 2.1781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SMCI | ai_server_oem | 28.315 |  | 27.9853 | 1.1782 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 14 | TER | semiconductor_test_packaging | 308.92 |  | 308.4203 | 0.162 | 315.21 | 304.11 | 4.8233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MSFT | cloud_ai_capex | 397.63 |  | 396.31 | 0.3331 | 400.09 | 392.355 | 0.6413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | CRWV | gpu_cloud_ai_factory | 66.355 |  | 66.2549 | 0.1511 | 68.995 | 65.635 | 2.1852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MU | memory_hbm_storage | 819.49 |  | 815.2875 | 0.5155 | 846.4 | 813.91 | 1.2105 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 466.84 |  | 465.059 | 0.383 | 477.73 | 460.77 | 4.9289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 585.08 |  | 582.0773 | 0.5159 | 603.25 | 584.69 | 2.5638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 457.78 |  | 455.5182 | 0.4965 | 472.485 | 453.76 | 4.0937 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.05 |  | 196.0026 | 0.5344 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.02 |  | 739.4626 | 0.2106 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 379.69 |  | 378.5467 | 0.302 | 378.64 | 371.57 | 2.1781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | ANET | ai_networking_optical | 167.61 |  | 164.3777 | 1.9664 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | GOOGL | cloud_ai_capex | 334.52 |  | 330.4122 | 1.2432 | 330.21 | 324.97 | 0.4394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ETN | data_center_power_cooling | 385.26 |  | 381.0017 | 1.1176 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ORCL | cloud_ai_capex | 120.515 |  | 118.2461 | 1.9188 | 117.17 | 115.25 | 2.9125 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | TSM | foundry | 390.2 |  | 387.55 | 0.6838 | 390.46 | 382.495 | 0.0692 | watch_only | none |
| 9 | SMH | semiconductor_index | 529.92 |  | 527.317 | 0.4936 | 533.01 | 523.325 | 0.051 | watch_only | none |
| 10 | SOXX | semiconductor_index | 491.8 |  | 489.9508 | 0.3774 | 497.64 | 485.42 | 0.0529 | watch_only | none |
| 11 | QQQ | market_regime | 676.36 |  | 674.0066 | 0.3492 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 12 | STX | memory_hbm_storage | 752.17 |  | 729.8066 | 3.0643 | 774.805 | 719.02 | 0.3031 | watch_only | none |
| 13 | IWM | market_regime | 293.03 |  | 292.3229 | 0.2419 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 14 | KLAC | semiconductor_equipment | 191.18 |  | 190.7569 | 0.2218 | 194.96 | 189.48 | 0.1098 | watch_only | none |
| 15 | AMZN | cloud_ai_capex | 231.13 |  | 230.4528 | 0.2939 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| 16 | SMCI | ai_server_oem | 28.315 |  | 27.9853 | 1.1782 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 17 | AAPL | mega_cap_platform | 339.51 |  | 338.926 | 0.1723 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 18 | CORZ | high_beta_ai_infrastructure | 20.535 |  | 20.0412 | 2.4637 | 20.97 | 19.755 | 0.0487 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 61.745 |  | 61.0899 | 1.0724 | 62.01 | 60.23 | 0.0324 | watch_only | none |
| 20 | GEV | data_center_power_cooling | 937.02 |  | 937.5411 | -0.0556 | 955.825 | 935.665 | 1.9701 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.36 |  | 674.0066 | 0.3492 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.745 |  | 61.0899 | 1.0724 | 62.01 | 60.23 | 0.0324 | watch_only | none |
| NVDA | ai_accelerator | 197.05 |  | 196.0026 | 0.5344 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.63 |  | 396.31 | 0.3331 | 400.09 | 392.355 | 0.6413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 339.51 |  | 338.926 | 0.1723 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.52 |  | 330.4122 | 1.2432 | 330.21 | 324.97 | 0.4394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 457.78 |  | 455.5182 | 0.4965 | 472.485 | 453.76 | 4.0937 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 390.2 |  | 387.55 | 0.6838 | 390.46 | 382.495 | 0.0692 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.8 |  | 489.9508 | 0.3774 | 497.64 | 485.42 | 0.0529 | watch_only | none |
| SMH | semiconductor_index | 529.92 |  | 527.317 | 0.4936 | 533.01 | 523.325 | 0.051 | watch_only | none |
| AVGO | custom_silicon_networking | 379.69 |  | 378.5467 | 0.302 | 378.64 | 371.57 | 2.1781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 819.49 |  | 815.2875 | 0.5155 | 846.4 | 813.91 | 1.2105 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.26 |  | 174.1556 | 0.6341 | 181.24 | 172.395 | 3.6917 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 382.11 |  | 374.8642 | 1.9329 | 402 | 374.02 | 0.5522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.32 |  | 44.4417 | -0.2739 | 46.19 | 44.33 | 0.0677 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 28.315 |  | 27.9853 | 1.1782 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.02 |  | 739.4626 | 0.2106 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.03 |  | 292.3229 | 0.2419 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.515 |  | 118.2461 | 1.9188 | 117.17 | 115.25 | 2.9125 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.355 |  | 66.2549 | 0.1511 | 68.995 | 65.635 | 2.1852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.21 |  | 266.224 | -0.3809 | 273.86 | 266.04 | 0.4902 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 385.26 |  | 381.0017 | 1.1176 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.08 |  | 582.0773 | 0.5159 | 603.25 | 584.69 | 2.5638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 937.02 |  | 937.5411 | -0.0556 | 955.825 | 935.665 | 1.9701 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 466.84 |  | 465.059 | 0.383 | 477.73 | 460.77 | 4.9289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.62 |  | 138.407 | 0.8764 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.61 |  | 164.3777 | 1.9664 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.76 |  | 237.1972 | 1.502 | 256.145 | 236.73 | 4.3363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 642.46 |  | 631.6134 | 1.7173 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 340.89 |  | 337.3021 | 1.0637 | 354.09 | 338.14 | 0.6483 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.135 |  | 85.7564 | 1.6076 | 92.95 | 84.63 | 3.5807 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 261.975 |  | 258.9927 | 1.1515 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1579.99 |  | 1577.1716 | 0.1787 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 474.12 |  | 476.5353 | -0.5068 | 494.87 | 477.03 | 5.0578 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.2 |  | 266.4158 | 1.4204 | 276.85 | 267.14 | 1.362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.18 |  | 190.7569 | 0.2218 | 194.96 | 189.48 | 0.1098 | watch_only | none |
| TER | semiconductor_test_packaging | 308.92 |  | 308.4203 | 0.162 | 315.21 | 304.11 | 4.8233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 238.05 |  | 236.6224 | 0.6033 | 248.8 | 236.42 | 0.4621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.07 |  | 46.7639 | -1.4839 | 51.64 | 47.435 | 4.2544 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.1 |  | 42.4846 | -0.9053 | 44.155 | 41.78 | 1.0689 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 118.56 |  | 119.364 | -0.6736 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 282.135 |  | 282.417 | -0.0998 | 296.8 | 283.22 | 0.3722 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.345 |  | 518.3997 | -0.7822 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.42 |  | 295.8145 | -0.4714 | 297.25 | 293.555 | 4.5411 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.38 |  | 26.5232 | -0.5401 | 27 | 25.42 | 2.6156 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.71 |  | 33.7188 | -0.0262 | 35.08 | 33.52 | 0.0593 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.535 |  | 20.0412 | 2.4637 | 20.97 | 19.755 | 0.0487 | watch_only | none |
| SNDK | memory_hbm_storage | 1080.105 |  | 1100.8851 | -1.8876 | 1185.19 | 1114.57 | 1.561 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.23 |  | 438.8806 | 3.4974 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 752.17 |  | 729.8066 | 3.0643 | 774.805 | 719.02 | 0.3031 | watch_only | none |
| AMZN | cloud_ai_capex | 231.13 |  | 230.4528 | 0.2939 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| META | cloud_ai_capex | 593.31 |  | 593.8337 | -0.0882 | 600.765 | 594.21 | 0.1365 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 244.22 |  | 245.3113 | -0.4449 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.96 |  | 131.6366 | -0.514 | 136.45 | 131.735 | 1.3057 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
