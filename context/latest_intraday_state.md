# Intraday State

- Generated at: `2026-07-29T03:09:16+08:00`
- Market time ET: `2026-07-28T15:09:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'manual_confirm_candidate': 6, 'below_vwap': 7, 'spread_too_wide_or_missing': 28, 'price_stale_or_missing': 1, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.915 |  | 674.2297 | 0.3983 | 677.3 | 670.84 | 0.034 | watch_only | none |
| SOXX | semiconductor_index | 493.285 |  | 490.0622 | 0.6576 | 497.64 | 485.42 | 0.0466 | watch_only | none |
| SMH | semiconductor_index | 531.24 |  | 527.4665 | 0.7154 | 533.01 | 523.325 | 0.0188 | watch_only | none |
| SPY | market_regime | 741.47 |  | 739.6432 | 0.247 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.3 |  | 196.1306 | 0.5963 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.47 |  | 739.6432 | 0.247 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.755 |  | 331.1222 | 1.0971 | 330.21 | 324.97 | 0.2539 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.97 |  | 138.757 | 1.5949 | 139.755 | 137.31 | 0.0993 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.26 |  | 292.44 | 0.2804 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.148 | 4.4271 | 20.97 | 19.755 | 0.0951 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.47 |  | 739.6432 | 0.247 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.26 |  | 292.44 | 0.2804 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 197.3 |  | 196.1306 | 0.5963 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 231.29 |  | 230.5282 | 0.3304 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.41 |  | 338.9745 | 0.1285 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 6 | SMH | semiconductor_index | 531.24 |  | 527.4665 | 0.7154 | 533.01 | 523.325 | 0.0188 | watch_only | none |
| 7 | SOXX | semiconductor_index | 493.285 |  | 490.0622 | 0.6576 | 497.64 | 485.42 | 0.0466 | watch_only | none |
| 8 | QQQ | market_regime | 676.915 |  | 674.2297 | 0.3983 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 9 | CRWV | gpu_cloud_ai_factory | 66.515 |  | 66.2683 | 0.3723 | 68.995 | 65.635 | 0.1052 | watch_only | none |
| 10 | AMAT | semiconductor_equipment | 479.365 |  | 476.4477 | 0.6123 | 494.87 | 477.03 | 0.2149 | watch_only | none |
| 11 | GOOGL | cloud_ai_capex | 334.755 |  | 331.1222 | 1.0971 | 330.21 | 324.97 | 0.2539 | buy_precheck_manual_confirm | none |
| 12 | ENTG | semiconductor_materials | 119.435 |  | 119.1727 | 0.2201 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | HPE | ai_server_oem | 44.99 |  | 44.4658 | 1.1788 | 46.19 | 44.33 | 0.1334 | watch_only | none |
| 14 | ASML | semiconductor_equipment | 1587.64 |  | 1577.5084 | 0.6423 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.148 | 4.4271 | 20.97 | 19.755 | 0.0951 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 28.36 |  | 28.0115 | 1.2443 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 17 | JCI | data_center_power_cooling | 140.97 |  | 138.757 | 1.5949 | 139.755 | 137.31 | 0.0993 | buy_precheck_manual_confirm | none |
| 18 | META | cloud_ai_capex | 594.48 |  | 593.849 | 0.1063 | 600.765 | 594.21 | 0.9605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | COHU | semiconductor_test_packaging | 42.59 |  | 42.439 | 0.3558 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TT | data_center_power_cooling | 468.87 |  | 465.4001 | 0.7456 | 477.73 | 460.77 | 0.3604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.3 |  | 196.1306 | 0.5963 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.47 |  | 739.6432 | 0.247 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.755 |  | 331.1222 | 1.0971 | 330.21 | 324.97 | 0.2539 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.97 |  | 138.757 | 1.5949 | 139.755 | 137.31 | 0.0993 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.26 |  | 292.44 | 0.2804 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.148 | 4.4271 | 20.97 | 19.755 | 0.0951 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 392.51 |  | 387.8975 | 1.1891 | 390.46 | 382.495 | 0.9299 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AVGO | custom_silicon_networking | 383.115 |  | 378.7138 | 1.1621 | 378.64 | 371.57 | 1.8402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1587.64 |  | 1577.5084 | 0.6423 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ANET | ai_networking_optical | 169.15 |  | 165.1518 | 2.4209 | 165.975 | 160.51 | 3.7836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ETN | data_center_power_cooling | 386.52 |  | 381.4214 | 1.3367 | 384.565 | 377.43 | 3.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ORCL | cloud_ai_capex | 121.56 |  | 118.7108 | 2.4001 | 117.17 | 115.25 | 1.2998 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TER | semiconductor_test_packaging | 315.455 |  | 309.0237 | 2.0812 | 315.21 | 304.11 | 0.7862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SMH | semiconductor_index | 531.24 |  | 527.4665 | 0.7154 | 533.01 | 523.325 | 0.0188 | watch_only | none |
| 15 | SOXX | semiconductor_index | 493.285 |  | 490.0622 | 0.6576 | 497.64 | 485.42 | 0.0466 | watch_only | none |
| 16 | QQQ | market_regime | 676.915 |  | 674.2297 | 0.3983 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 17 | AMAT | semiconductor_equipment | 479.365 |  | 476.4477 | 0.6123 | 494.87 | 477.03 | 0.2149 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.29 |  | 230.5282 | 0.3304 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.99 |  | 44.4658 | 1.1788 | 46.19 | 44.33 | 0.1334 | watch_only | none |
| 20 | SMCI | ai_server_oem | 28.36 |  | 28.0115 | 1.2443 | 28.86 | 27.59 | 0.0353 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.915 |  | 674.2297 | 0.3983 | 677.3 | 670.84 | 0.034 | watch_only | none |
| TQQQ | leveraged_tool | 61.92 |  | 61.1444 | 1.2685 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.3 |  | 196.1306 | 0.5963 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 395.19 |  | 396.4123 | -0.3083 | 400.09 | 392.355 | 0.0354 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.41 |  | 338.9745 | 0.1285 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.755 |  | 331.1222 | 1.0971 | 330.21 | 324.97 | 0.2539 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.53 |  | 455.6073 | 0.6415 | 472.485 | 453.76 | 4.6584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.51 |  | 387.8975 | 1.1891 | 390.46 | 382.495 | 0.9299 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.285 |  | 490.0622 | 0.6576 | 497.64 | 485.42 | 0.0466 | watch_only | none |
| SMH | semiconductor_index | 531.24 |  | 527.4665 | 0.7154 | 533.01 | 523.325 | 0.0188 | watch_only | none |
| AVGO | custom_silicon_networking | 383.115 |  | 378.7138 | 1.1621 | 378.64 | 371.57 | 1.8402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 824.76 |  | 815.8204 | 1.0958 | 846.4 | 813.91 | 1.1531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.05 |  | 174.2309 | 0.4701 | 181.24 | 172.395 | 1.3596 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 389.645 |  | 375.5577 | 3.751 | 402 | 374.02 | 2.7538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.99 |  | 44.4658 | 1.1788 | 46.19 | 44.33 | 0.1334 | watch_only | none |
| SMCI | ai_server_oem | 28.36 |  | 28.0115 | 1.2443 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.47 |  | 739.6432 | 0.247 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.26 |  | 292.44 | 0.2804 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 121.56 |  | 118.7108 | 2.4001 | 117.17 | 115.25 | 1.2998 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.515 |  | 66.2683 | 0.3723 | 68.995 | 65.635 | 0.1052 | watch_only | none |
| VRT | data_center_power_cooling | 267.95 |  | 266.1673 | 0.6698 | 273.86 | 266.04 | 0.9965 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.52 |  | 381.4214 | 1.3367 | 384.565 | 377.43 | 3.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 588.08 |  | 582.6704 | 0.9284 | 603.25 | 584.69 | 2.333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 936.715 |  | 937.4976 | -0.0835 | 955.825 | 935.665 | 0.1655 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 468.87 |  | 465.4001 | 0.7456 | 477.73 | 460.77 | 0.3604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.97 |  | 138.757 | 1.5949 | 139.755 | 137.31 | 0.0993 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169.15 |  | 165.1518 | 2.4209 | 165.975 | 160.51 | 3.7836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 242.07 |  | 237.7067 | 1.8356 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 646.84 |  | 632.4679 | 2.2724 | 673.65 | 624.91 | 0.5766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 343.365 |  | 337.5487 | 1.7231 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.795 |  | 85.882 | 2.2275 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.27 |  | 259.2158 | 0.7925 | 268.265 | 253.05 | 4.3097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1587.64 |  | 1577.5084 | 0.6423 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 479.365 |  | 476.4477 | 0.6123 | 494.87 | 477.03 | 0.2149 | watch_only | none |
| LRCX | semiconductor_equipment | 272.05 |  | 266.8719 | 1.9403 | 276.85 | 267.14 | 2.801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 192.85 |  | 190.8383 | 1.0541 | 194.96 | 189.48 | 1.3119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 315.455 |  | 309.0237 | 2.0812 | 315.21 | 304.11 | 0.7862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 240.56 |  | 237.1033 | 1.4579 | 248.8 | 236.42 | 5.0964 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.15 |  | 46.6708 | -1.1159 | 51.64 | 47.435 | 4.377 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.59 |  | 42.439 | 0.3558 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.435 |  | 119.1727 | 0.2201 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 284.82 |  | 282.4162 | 0.8511 | 296.8 | 283.22 | 0.5582 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.77 |  | 518.0337 | -0.437 | 518.6 | 511.495 | 0.0737 | below_vwap | below_vwap |
| APD | industrial_gases | 295.44 |  | 295.7399 | -0.1014 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.28 |  | 26.5105 | -0.8694 | 27 | 25.42 | 0.0381 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.515 |  | 33.7059 | -0.5665 | 35.08 | 33.52 | 0.0597 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.148 | 4.4271 | 20.97 | 19.755 | 0.0951 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1111.25 |  | 1099.4076 | 1.0772 | 1185.19 | 1114.57 | 0.2034 | below_opening_15m_low | below_opening_15m_low |
| WDC | memory_hbm_storage | 457.3 |  | 440.7235 | 3.7612 | 465.04 | 435.22 | 3.4463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 743.98 |  | 732.9847 | 1.5001 | 774.805 | 719.02 | 4.8241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.29 |  | 230.5282 | 0.3304 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.48 |  | 593.849 | 0.1063 | 600.765 | 594.21 | 0.9605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 245.14 |  | 245.2255 | -0.0349 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131.59 |  | 131.5247 | 0.0496 | 136.45 | 131.735 | 2.5078 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
