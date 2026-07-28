# Intraday State

- Generated at: `2026-07-28T23:07:16+08:00`
- Market time ET: `2026-07-28T11:07:20-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 9, 'manual_confirm_candidate': 1, 'below_vwap': 13, 'below_opening_15m_low': 23, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 9}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 672.54 |  | 671.7105 | 0.1235 | 677.3 | 670.84 | 0.0684 | watch_only | none |
| SOXX | semiconductor_index | 487.2 |  | 488.4113 | -0.248 | 497.64 | 485.42 | 0.0924 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.12 |  | 525.4687 | 0.1239 | 533.01 | 523.325 | 0.1178 | watch_only | none |
| SPY | market_regime | 738.225 |  | 737.8611 | 0.0493 | 739.42 | 736.57 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.39 |  | 194.6765 | 0.8802 | 195.4 | 193.65 | 0.0204 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 385.55 |  | 384.7988 | 0.1952 | 390.46 | 382.495 | 0.1323 | watch_only | none |
| 2 | SMH | semiconductor_index | 526.12 |  | 525.4687 | 0.1239 | 533.01 | 523.325 | 0.1178 | watch_only | none |
| 3 | SPY | market_regime | 738.225 |  | 737.8611 | 0.0493 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 4 | QQQ | market_regime | 672.54 |  | 671.7105 | 0.1235 | 677.3 | 670.84 | 0.0684 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 396.24 |  | 394.9672 | 0.3223 | 400.09 | 392.355 | 0.0505 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 329.405 |  | 327.4912 | 0.5844 | 330.21 | 324.97 | 0.0273 | watch_only | none |
| 7 | NVDA | ai_accelerator | 196.39 |  | 194.6765 | 0.8802 | 195.4 | 193.65 | 0.0204 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 162.93 |  | 161.953 | 0.6033 | 165.975 | 160.51 | 0.1657 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 33.775 |  | 33.3429 | 1.296 | 35.08 | 33.52 | 0.0592 | watch_only | none |
| 10 | TT | data_center_power_cooling | 464.64 |  | 464.0998 | 0.1164 | 477.73 | 460.77 | 3.3553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ETN | data_center_power_cooling | 379.29 |  | 378.6963 | 0.1568 | 384.565 | 377.43 | 2.4493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 306.24 |  | 305.535 | 0.2307 | 315.21 | 304.11 | 3.974 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ENTG | semiconductor_materials | 120.04 |  | 119.2307 | 0.6788 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 378.03 |  | 375.9664 | 0.5489 | 378.64 | 371.57 | 1.9522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | HPE | ai_server_oem | 44.31 |  | 44.1607 | 0.338 | 46.19 | 44.33 | 0.0451 | below_opening_15m_low | below_opening_15m_low |
| 16 | AAOI | ai_networking_optical | 85.88 |  | 84.8778 | 1.1808 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SOXX | semiconductor_index | 487.2 |  | 488.4113 | -0.248 | 497.64 | 485.42 | 0.0924 | below_vwap | below_vwap |
| 18 | ORCL | cloud_ai_capex | 117.45 |  | 116.1602 | 1.1104 | 117.17 | 115.25 | 4.5551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MU | memory_hbm_storage | 812.05 |  | 811.7737 | 0.034 | 846.4 | 813.91 | 0.3904 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.39 |  | 194.6765 | 0.8802 | 195.4 | 193.65 | 0.0204 | buy_precheck_manual_confirm | none |
| 2 | ORCL | cloud_ai_capex | 117.45 |  | 116.1602 | 1.1104 | 117.17 | 115.25 | 4.5551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TSM | foundry | 385.55 |  | 384.7988 | 0.1952 | 390.46 | 382.495 | 0.1323 | watch_only | none |
| 4 | SMH | semiconductor_index | 526.12 |  | 525.4687 | 0.1239 | 533.01 | 523.325 | 0.1178 | watch_only | none |
| 5 | SPY | market_regime | 738.225 |  | 737.8611 | 0.0493 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 6 | QQQ | market_regime | 672.54 |  | 671.7105 | 0.1235 | 677.3 | 670.84 | 0.0684 | watch_only | none |
| 7 | ANET | ai_networking_optical | 162.93 |  | 161.953 | 0.6033 | 165.975 | 160.51 | 0.1657 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 329.405 |  | 327.4912 | 0.5844 | 330.21 | 324.97 | 0.0273 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 396.24 |  | 394.9672 | 0.3223 | 400.09 | 392.355 | 0.0505 | watch_only | none |
| 10 | IREN | high_beta_ai_infrastructure | 33.775 |  | 33.3429 | 1.296 | 35.08 | 33.52 | 0.0592 | watch_only | none |
| 11 | TQQQ | leveraged_tool | 60.69 |  | 60.4674 | 0.3681 | 62.01 | 60.23 | 0.0165 | watch_only | none |
| 12 | SOXX | semiconductor_index | 487.2 |  | 488.4113 | -0.248 | 497.64 | 485.42 | 0.0924 | below_vwap | below_vwap |
| 13 | ASML | semiconductor_equipment | 1568.505 |  | 1571.6866 | -0.2024 | 1586.01 | 1565.95 | 0.5891 | below_vwap | below_vwap,spread_too_wide |
| 14 | STX | memory_hbm_storage | 720.57 |  | 722.4549 | -0.2609 | 774.805 | 719.02 | 4.3105 | below_vwap | below_vwap,spread_too_wide |
| 15 | JCI | data_center_power_cooling | 137.81 |  | 137.8147 | -0.0034 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ALAB | ai_networking_optical | 254.79 |  | 255.2884 | -0.1952 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 244.3 |  | 244.6235 | -0.1323 | 253.38 | 243.72 | 4.1138 | below_vwap | below_vwap,spread_too_wide |
| 19 | LIN | industrial_gases | 518.5 |  | 518.6513 | -0.0292 | 518.6 | 511.495 | 4.3105 | below_vwap | below_vwap,spread_too_wide |
| 20 | APD | industrial_gases | 295.71 |  | 296.4205 | -0.2397 | 297.25 | 293.555 | 4.2474 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 672.54 |  | 671.7105 | 0.1235 | 677.3 | 670.84 | 0.0684 | watch_only | none |
| TQQQ | leveraged_tool | 60.69 |  | 60.4674 | 0.3681 | 62.01 | 60.23 | 0.0165 | watch_only | none |
| NVDA | ai_accelerator | 196.39 |  | 194.6765 | 0.8802 | 195.4 | 193.65 | 0.0204 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.24 |  | 394.9672 | 0.3223 | 400.09 | 392.355 | 0.0505 | watch_only | none |
| AAPL | mega_cap_platform | 338.055 |  | 338.4779 | -0.1249 | 342.87 | 337.78 | 0.0532 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 329.405 |  | 327.4912 | 0.5844 | 330.21 | 324.97 | 0.0273 | watch_only | none |
| AMD | ai_accelerator | 451.58 |  | 452.8761 | -0.2862 | 472.485 | 453.76 | 2.0373 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 385.55 |  | 384.7988 | 0.1952 | 390.46 | 382.495 | 0.1323 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 487.2 |  | 488.4113 | -0.248 | 497.64 | 485.42 | 0.0924 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.12 |  | 525.4687 | 0.1239 | 533.01 | 523.325 | 0.1178 | watch_only | none |
| AVGO | custom_silicon_networking | 378.03 |  | 375.9664 | 0.5489 | 378.64 | 371.57 | 1.9522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 812.05 |  | 811.7737 | 0.034 | 846.4 | 813.91 | 0.3904 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 174.41 |  | 172.062 | 1.3646 | 181.24 | 172.395 | 0.4874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 372.465 |  | 371.6 | 0.2328 | 402 | 374.02 | 1.1572 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 44.31 |  | 44.1607 | 0.338 | 46.19 | 44.33 | 0.0451 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.65 |  | 27.6865 | -0.1318 | 28.86 | 27.59 | 0.0723 | below_vwap | below_vwap |
| SPY | market_regime | 738.225 |  | 737.8611 | 0.0493 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| IWM | market_regime | 291.345 |  | 291.6266 | -0.0966 | 293.26 | 291.55 | 0.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 117.45 |  | 116.1602 | 1.1104 | 117.17 | 115.25 | 4.5551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 65.63 |  | 65.8877 | -0.3911 | 68.995 | 65.635 | 0.9904 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 264.92 |  | 265.5721 | -0.2455 | 273.86 | 266.04 | 1.3023 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 379.29 |  | 378.6963 | 0.1568 | 384.565 | 377.43 | 2.4493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 578.05 |  | 578.7643 | -0.1234 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 932.29 |  | 933.0287 | -0.0792 | 955.825 | 935.665 | 1.1617 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 464.64 |  | 464.0998 | 0.1164 | 477.73 | 460.77 | 3.3553 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 137.81 |  | 137.8147 | -0.0034 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 162.93 |  | 161.953 | 0.6033 | 165.975 | 160.51 | 0.1657 | watch_only | none |
| COHR | ai_networking_optical | 235.69 |  | 235.7005 | -0.0044 | 256.145 | 236.73 | 3.7252 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 630.86 |  | 624.2772 | 1.0545 | 673.65 | 624.91 | 1.3585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 337.38 |  | 335.7115 | 0.497 | 354.09 | 338.14 | 5.0566 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 85.88 |  | 84.8778 | 1.1808 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 254.79 |  | 255.2884 | -0.1952 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1568.505 |  | 1571.6866 | -0.2024 | 1586.01 | 1565.95 | 0.5891 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 472.79 |  | 477.1066 | -0.9047 | 494.87 | 477.03 | 4.0356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 262.89 |  | 265.6503 | -1.0391 | 276.85 | 267.14 | 0.7608 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 188.7 |  | 189.9442 | -0.6551 | 194.96 | 189.48 | 0.3551 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 306.24 |  | 305.535 | 0.2307 | 315.21 | 304.11 | 3.974 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 232.135 |  | 237.4397 | -2.2341 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.495 |  | 47.2111 | -1.5168 | 51.64 | 47.435 | 0.2581 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.49 |  | 42.6515 | -0.3788 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.04 |  | 119.2307 | 0.6788 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 279.14 |  | 281.7967 | -0.9428 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.5 |  | 518.6513 | -0.0292 | 518.6 | 511.495 | 4.3105 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.71 |  | 296.4205 | -0.2397 | 297.25 | 293.555 | 4.2474 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.075 |  | 26.3372 | -0.9954 | 27 | 25.42 | 0.0767 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.775 |  | 33.3429 | 1.296 | 35.08 | 33.52 | 0.0592 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 19.745 |  | 19.9504 | -1.0295 | 20.97 | 19.755 | 0.1013 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1086.47 |  | 1103.2243 | -1.5187 | 1185.19 | 1114.57 | 2.5228 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 434.42 |  | 433.538 | 0.2034 | 465.04 | 435.22 | 2.295 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| STX | memory_hbm_storage | 720.57 |  | 722.4549 | -0.2609 | 774.805 | 719.02 | 4.3105 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 229.07 |  | 229.8985 | -0.3604 | 233.05 | 229.7 | 0.0175 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 588.29 |  | 593.7277 | -0.9159 | 600.765 | 594.21 | 3.2518 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.3 |  | 244.6235 | -0.1323 | 253.38 | 243.72 | 4.1138 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 129.86 |  | 131.4104 | -1.1798 | 136.45 | 131.735 | 3.8503 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
