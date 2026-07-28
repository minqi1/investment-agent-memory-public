# Intraday State

- Generated at: `2026-07-28T22:33:06+08:00`
- Market time ET: `2026-07-28T10:33:07-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 36, 'watch_only': 6, 'below_vwap': 11, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.4 |  | 671.2353 | -0.1244 | 677.3 | 670.84 | 0.0746 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 484.61 |  | 488.2662 | -0.7488 | 497.64 | 485.42 | 0.097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 522.75 |  | 524.939 | -0.417 | 533.01 | 523.325 | 0.067 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.645 |  | 737.5093 | 0.0184 | 739.42 | 736.57 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 194.36 |  | 194.0165 | 0.177 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| 2 | SPY | market_regime | 737.645 |  | 737.5093 | 0.0184 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 3 | GOOGL | cloud_ai_capex | 327.7 |  | 327.052 | 0.1981 | 330.21 | 324.97 | 0.116 | watch_only | none |
| 4 | APD | industrial_gases | 297.11 |  | 296.4477 | 0.2234 | 297.25 | 293.555 | 0.1313 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 395.39 |  | 394.6295 | 0.1927 | 400.09 | 392.355 | 0.1088 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 375.82 |  | 375.2323 | 0.1566 | 378.64 | 371.57 | 0.1783 | watch_only | none |
| 7 | ANET | ai_networking_optical | 162.06 |  | 161.5412 | 0.3212 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | LIN | industrial_gases | 520.32 |  | 518.5663 | 0.3382 | 518.6 | 511.495 | 3.9553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | AAPL | mega_cap_platform | 338.27 |  | 338.6769 | -0.1201 | 342.87 | 337.78 | 0.0118 | below_vwap | below_vwap |
| 11 | CORZ | high_beta_ai_infrastructure | 19.82 |  | 19.9595 | -0.6988 | 20.97 | 19.755 | 0.1009 | below_vwap | below_vwap |
| 12 | APLD | high_beta_ai_infrastructure | 26.11 |  | 26.3012 | -0.7271 | 27 | 25.42 | 0.1149 | below_vwap | below_vwap |
| 13 | TT | data_center_power_cooling | 462.25 |  | 464.333 | -0.4486 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ARM | ai_accelerator | 244.07 |  | 244.763 | -0.2831 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 42.13 |  | 42.7283 | -1.4003 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | TSM | foundry | 382.93 |  | 384.8477 | -0.4983 | 390.46 | 382.495 | 2.2249 | below_vwap | below_vwap,spread_too_wide |
| 17 | ASML | semiconductor_equipment | 1568 |  | 1570.0619 | -0.1313 | 1586.01 | 1565.95 | 0.6626 | below_vwap | below_vwap,spread_too_wide |
| 18 | ORCL | cloud_ai_capex | 115.53 |  | 115.7117 | -0.157 | 117.17 | 115.25 | 4.2413 | below_vwap | below_vwap,spread_too_wide |
| 19 | ENTG | semiconductor_materials | 118.185 |  | 119.2356 | -0.8812 | 121 | 117.72 | 1.1254 | below_vwap | below_vwap,spread_too_wide |
| 20 | SMH | semiconductor_index | 522.75 |  | 524.939 | -0.417 | 533.01 | 523.325 | 0.067 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 520.32 |  | 518.5663 | 0.3382 | 518.6 | 511.495 | 3.9553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | NVDA | ai_accelerator | 194.36 |  | 194.0165 | 0.177 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 375.82 |  | 375.2323 | 0.1566 | 378.64 | 371.57 | 0.1783 | watch_only | none |
| 4 | SPY | market_regime | 737.645 |  | 737.5093 | 0.0184 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 327.7 |  | 327.052 | 0.1981 | 330.21 | 324.97 | 0.116 | watch_only | none |
| 6 | APD | industrial_gases | 297.11 |  | 296.4477 | 0.2234 | 297.25 | 293.555 | 0.1313 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 395.39 |  | 394.6295 | 0.1927 | 400.09 | 392.355 | 0.1088 | watch_only | none |
| 8 | TSM | foundry | 382.93 |  | 384.8477 | -0.4983 | 390.46 | 382.495 | 2.2249 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1568 |  | 1570.0619 | -0.1313 | 1586.01 | 1565.95 | 0.6626 | below_vwap | below_vwap,spread_too_wide |
| 10 | TT | data_center_power_cooling | 462.25 |  | 464.333 | -0.4486 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ARM | ai_accelerator | 244.07 |  | 244.763 | -0.2831 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ORCL | cloud_ai_capex | 115.53 |  | 115.7117 | -0.157 | 117.17 | 115.25 | 4.2413 | below_vwap | below_vwap,spread_too_wide |
| 14 | ENTG | semiconductor_materials | 118.185 |  | 119.2356 | -0.8812 | 121 | 117.72 | 1.1254 | below_vwap | below_vwap,spread_too_wide |
| 15 | COHU | semiconductor_test_packaging | 42.13 |  | 42.7283 | -1.4003 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | AAPL | mega_cap_platform | 338.27 |  | 338.6769 | -0.1201 | 342.87 | 337.78 | 0.0118 | below_vwap | below_vwap |
| 17 | CORZ | high_beta_ai_infrastructure | 19.82 |  | 19.9595 | -0.6988 | 20.97 | 19.755 | 0.1009 | below_vwap | below_vwap |
| 18 | APLD | high_beta_ai_infrastructure | 26.11 |  | 26.3012 | -0.7271 | 27 | 25.42 | 0.1149 | below_vwap | below_vwap |
| 19 | ANET | ai_networking_optical | 162.06 |  | 161.5412 | 0.3212 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 805.55 |  | 811.4798 | -0.7307 | 846.4 | 813.91 | 0.2892 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.4 |  | 671.2353 | -0.1244 | 677.3 | 670.84 | 0.0746 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 60.08 |  | 60.3894 | -0.5124 | 62.01 | 60.23 | 0.0333 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 194.36 |  | 194.0165 | 0.177 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| MSFT | cloud_ai_capex | 395.39 |  | 394.6295 | 0.1927 | 400.09 | 392.355 | 0.1088 | watch_only | none |
| AAPL | mega_cap_platform | 338.27 |  | 338.6769 | -0.1201 | 342.87 | 337.78 | 0.0118 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 327.7 |  | 327.052 | 0.1981 | 330.21 | 324.97 | 0.116 | watch_only | none |
| AMD | ai_accelerator | 448.47 |  | 453.6821 | -1.1488 | 472.485 | 453.76 | 2.0982 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 382.93 |  | 384.8477 | -0.4983 | 390.46 | 382.495 | 2.2249 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 484.61 |  | 488.2662 | -0.7488 | 497.64 | 485.42 | 0.097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 522.75 |  | 524.939 | -0.417 | 533.01 | 523.325 | 0.067 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.82 |  | 375.2323 | 0.1566 | 378.64 | 371.57 | 0.1783 | watch_only | none |
| MU | memory_hbm_storage | 805.55 |  | 811.4798 | -0.7307 | 846.4 | 813.91 | 0.2892 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 169.07 |  | 171.8475 | -1.6162 | 181.24 | 172.395 | 2.9751 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 367.77 |  | 370.536 | -0.7465 | 402 | 374.02 | 0.3943 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.73 |  | 44.0233 | -0.6662 | 46.19 | 44.33 | 0.1143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.505 |  | 27.6329 | -0.4628 | 28.86 | 27.59 | 0.0727 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.645 |  | 737.5093 | 0.0184 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| IWM | market_regime | 290.655 |  | 291.6911 | -0.3552 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.53 |  | 115.7117 | -0.157 | 117.17 | 115.25 | 4.2413 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 65.48 |  | 65.9445 | -0.7044 | 68.995 | 65.635 | 4.1998 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 260.01 |  | 266.2549 | -2.3455 | 273.86 | 266.04 | 3.4614 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 376.47 |  | 378.6919 | -0.5867 | 384.565 | 377.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 572.02 |  | 579.8826 | -1.3559 | 603.25 | 584.69 | 4.5278 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 921.23 |  | 934.3546 | -1.4047 | 955.825 | 935.665 | 0.5731 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 462.25 |  | 464.333 | -0.4486 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 136.85 |  | 137.8651 | -0.7363 | 139.755 | 137.31 | 4.7863 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 162.06 |  | 161.5412 | 0.3212 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 229.6 |  | 236.8116 | -3.0453 | 256.145 | 236.73 | 1.0758 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 609.83 |  | 623.6986 | -2.2236 | 673.65 | 624.91 | 4.1011 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 330.375 |  | 336.092 | -1.701 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 83.335 |  | 84.7497 | -1.6692 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 252.47 |  | 255.3238 | -1.1177 | 268.265 | 253.05 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1568 |  | 1570.0619 | -0.1313 | 1586.01 | 1565.95 | 0.6626 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 471.33 |  | 478.0846 | -1.4128 | 494.87 | 477.03 | 0.6004 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 261.22 |  | 266.1048 | -1.8357 | 276.85 | 267.14 | 0.2259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 188.69 |  | 190.0453 | -0.7131 | 194.96 | 189.48 | 0.1166 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 302.565 |  | 305.1834 | -0.858 | 315.21 | 304.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 231.3 |  | 238.0735 | -2.8451 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.845 |  | 47.3395 | -3.1569 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.13 |  | 42.7283 | -1.4003 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.185 |  | 119.2356 | -0.8812 | 121 | 117.72 | 1.1254 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 278.54 |  | 282.6861 | -1.4667 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 520.32 |  | 518.5663 | 0.3382 | 518.6 | 511.495 | 3.9553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.11 |  | 296.4477 | 0.2234 | 297.25 | 293.555 | 0.1313 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 26.11 |  | 26.3012 | -0.7271 | 27 | 25.42 | 0.1149 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.115 |  | 33.2608 | -0.4384 | 35.08 | 33.52 | 0.0302 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.82 |  | 19.9595 | -0.6988 | 20.97 | 19.755 | 0.1009 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1086.78 |  | 1104.5295 | -1.607 | 1185.19 | 1114.57 | 4.0993 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 427.695 |  | 433.8044 | -1.4083 | 465.04 | 435.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 714.46 |  | 721.8486 | -1.0236 | 774.805 | 719.02 | 0.3975 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 228.94 |  | 230.279 | -0.5815 | 233.05 | 229.7 | 0.0175 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 593.43 |  | 595.0126 | -0.266 | 600.765 | 594.21 | 0.5746 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.07 |  | 244.763 | -0.2831 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.64 |  | 131.2712 | -0.4809 | 136.45 | 131.735 | 0.1148 | below_opening_15m_low | below_opening_15m_low,below_vwap |
