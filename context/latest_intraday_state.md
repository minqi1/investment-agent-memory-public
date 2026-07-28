# Intraday State

- Generated at: `2026-07-29T02:19:26+08:00`
- Market time ET: `2026-07-28T14:19:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 6, 'below_vwap': 13, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 1, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.64 |  | 674.032 | 0.2386 | 677.3 | 670.84 | 0.0237 | watch_only | none |
| SOXX | semiconductor_index | 490.5 |  | 489.9582 | 0.1106 | 497.64 | 485.42 | 0.055 | watch_only | none |
| SMH | semiconductor_index | 528.23 |  | 527.3239 | 0.1718 | 533.01 | 523.325 | 0.0379 | watch_only | none |
| SPY | market_regime | 740.67 |  | 739.49 | 0.1596 | 739.42 | 736.57 | 0.0338 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.94 |  | 196.0173 | 0.4707 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.37 |  | 378.5573 | 0.2147 | 378.64 | 371.57 | 0.1133 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.67 |  | 739.49 | 0.1596 | 739.42 | 736.57 | 0.0338 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 167.95 |  | 164.607 | 2.0309 | 165.975 | 160.51 | 0.125 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.725 |  | 330.5305 | 1.269 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.44 |  | 118.3558 | 1.761 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.37 |  | 378.5573 | 0.2147 | 378.64 | 371.57 | 0.1133 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.67 |  | 739.49 | 0.1596 | 739.42 | 736.57 | 0.0338 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 196.94 |  | 196.0173 | 0.4707 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 528.23 |  | 527.3239 | 0.1718 | 533.01 | 523.325 | 0.0379 | watch_only | none |
| 5 | SOXX | semiconductor_index | 490.5 |  | 489.9582 | 0.1106 | 497.64 | 485.42 | 0.055 | watch_only | none |
| 6 | QQQ | market_regime | 675.64 |  | 674.032 | 0.2386 | 677.3 | 670.84 | 0.0237 | watch_only | none |
| 7 | GEV | data_center_power_cooling | 938.16 |  | 937.5402 | 0.0661 | 955.825 | 935.665 | 0.0821 | watch_only | none |
| 8 | IWM | market_regime | 292.72 |  | 292.3333 | 0.1323 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 397.225 |  | 396.3275 | 0.2264 | 400.09 | 392.355 | 0.0277 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 231.215 |  | 230.4651 | 0.3254 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 11 | AAPL | mega_cap_platform | 339.71 |  | 338.936 | 0.2284 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 12 | SMCI | ai_server_oem | 28.165 |  | 27.9922 | 0.6172 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 13 | PWR | data_center_power_cooling | 586.02 |  | 582.1442 | 0.6658 | 603.25 | 584.69 | 0.3055 | watch_only | none |
| 14 | ONTO | semiconductor_test_packaging | 237.66 |  | 236.6944 | 0.408 | 248.8 | 236.42 | 0.3408 | watch_only | none |
| 15 | GOOGL | cloud_ai_capex | 334.725 |  | 330.5305 | 1.269 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |
| 16 | ASML | semiconductor_equipment | 1580 |  | 1577.1982 | 0.1776 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ANET | ai_networking_optical | 167.95 |  | 164.607 | 2.0309 | 165.975 | 160.51 | 0.125 | buy_precheck_manual_confirm | none |
| 18 | MRVL | custom_silicon_networking | 174.68 |  | 174.1689 | 0.2935 | 181.24 | 172.395 | 3.286 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 749.33 |  | 730.5685 | 2.5681 | 774.805 | 719.02 | 0.1041 | watch_only | none |
| 20 | TSM | foundry | 390.305 |  | 387.6031 | 0.6971 | 390.46 | 382.495 | 1.3784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.94 |  | 196.0173 | 0.4707 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.37 |  | 378.5573 | 0.2147 | 378.64 | 371.57 | 0.1133 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.67 |  | 739.49 | 0.1596 | 739.42 | 736.57 | 0.0338 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 167.95 |  | 164.607 | 2.0309 | 165.975 | 160.51 | 0.125 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.725 |  | 330.5305 | 1.269 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.44 |  | 118.3558 | 1.761 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 139.89 |  | 138.4507 | 1.0396 | 139.755 | 137.31 | 3.4313 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ETN | data_center_power_cooling | 384.96 |  | 381.0639 | 1.0224 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 528.23 |  | 527.3239 | 0.1718 | 533.01 | 523.325 | 0.0379 | watch_only | none |
| 10 | SOXX | semiconductor_index | 490.5 |  | 489.9582 | 0.1106 | 497.64 | 485.42 | 0.055 | watch_only | none |
| 11 | QQQ | market_regime | 675.64 |  | 674.032 | 0.2386 | 677.3 | 670.84 | 0.0237 | watch_only | none |
| 12 | STX | memory_hbm_storage | 749.33 |  | 730.5685 | 2.5681 | 774.805 | 719.02 | 0.1041 | watch_only | none |
| 13 | PWR | data_center_power_cooling | 586.02 |  | 582.1442 | 0.6658 | 603.25 | 584.69 | 0.3055 | watch_only | none |
| 14 | GEV | data_center_power_cooling | 938.16 |  | 937.5402 | 0.0661 | 955.825 | 935.665 | 0.0821 | watch_only | none |
| 15 | IWM | market_regime | 292.72 |  | 292.3333 | 0.1323 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 397.225 |  | 396.3275 | 0.2264 | 400.09 | 392.355 | 0.0277 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.215 |  | 230.4651 | 0.3254 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 18 | ONTO | semiconductor_test_packaging | 237.66 |  | 236.6944 | 0.408 | 248.8 | 236.42 | 0.3408 | watch_only | none |
| 19 | SMCI | ai_server_oem | 28.165 |  | 27.9922 | 0.6172 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.71 |  | 338.936 | 0.2284 | 342.87 | 337.78 | 0.0088 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.64 |  | 674.032 | 0.2386 | 677.3 | 670.84 | 0.0237 | watch_only | none |
| TQQQ | leveraged_tool | 61.55 |  | 61.0966 | 0.7422 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 196.94 |  | 196.0173 | 0.4707 | 195.4 | 193.65 | 0.0559 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.225 |  | 396.3275 | 0.2264 | 400.09 | 392.355 | 0.0277 | watch_only | none |
| AAPL | mega_cap_platform | 339.71 |  | 338.936 | 0.2284 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.725 |  | 330.5305 | 1.269 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.29 |  | 455.5281 | -0.0523 | 472.485 | 453.76 | 2.2184 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 390.305 |  | 387.6031 | 0.6971 | 390.46 | 382.495 | 1.3784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.5 |  | 489.9582 | 0.1106 | 497.64 | 485.42 | 0.055 | watch_only | none |
| SMH | semiconductor_index | 528.23 |  | 527.3239 | 0.1718 | 533.01 | 523.325 | 0.0379 | watch_only | none |
| AVGO | custom_silicon_networking | 379.37 |  | 378.5573 | 0.2147 | 378.64 | 371.57 | 0.1133 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 814.36 |  | 815.3204 | -0.1178 | 846.4 | 813.91 | 0.1756 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 174.68 |  | 174.1689 | 0.2935 | 181.24 | 172.395 | 3.286 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 382.86 |  | 374.9405 | 2.1122 | 402 | 374.02 | 0.5224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.4 |  | 44.4404 | -0.091 | 46.19 | 44.33 | 0.045 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.165 |  | 27.9922 | 0.6172 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| SPY | market_regime | 740.67 |  | 739.49 | 0.1596 | 739.42 | 736.57 | 0.0338 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.72 |  | 292.3333 | 0.1323 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.44 |  | 118.3558 | 1.761 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.19 |  | 66.254 | -0.0966 | 68.995 | 65.635 | 2.4022 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 265.02 |  | 266.1905 | -0.4397 | 273.86 | 266.04 | 0.2755 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 384.96 |  | 381.0639 | 1.0224 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 586.02 |  | 582.1442 | 0.6658 | 603.25 | 584.69 | 0.3055 | watch_only | none |
| GEV | data_center_power_cooling | 938.16 |  | 937.5402 | 0.0661 | 955.825 | 935.665 | 0.0821 | watch_only | none |
| TT | data_center_power_cooling | 467.32 |  | 465.092 | 0.479 | 477.73 | 460.77 | 4.8018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.89 |  | 138.4507 | 1.0396 | 139.755 | 137.31 | 3.4313 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.95 |  | 164.607 | 2.0309 | 165.975 | 160.51 | 0.125 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 240.23 |  | 237.262 | 1.2509 | 256.145 | 236.73 | 4.1502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 641.13 |  | 631.7474 | 1.4852 | 673.65 | 624.91 | 3.9571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 339.095 |  | 337.3628 | 0.5135 | 354.09 | 338.14 | 0.3863 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 86.62 |  | 85.7769 | 0.9829 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.445 |  | 259.0458 | 0.5401 | 268.265 | 253.05 | 4.0316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1580 |  | 1577.1982 | 0.1776 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 473.46 |  | 476.4379 | -0.625 | 494.87 | 477.03 | 0.1542 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 269.76 |  | 266.5376 | 1.209 | 276.85 | 267.14 | 1.2011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.61 |  | 190.7627 | -0.0801 | 194.96 | 189.48 | 0.0472 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 307.65 |  | 308.4081 | -0.2458 | 315.21 | 304.11 | 0.2503 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 237.66 |  | 236.6944 | 0.408 | 248.8 | 236.42 | 0.3408 | watch_only | none |
| AMKR | semiconductor_test_packaging | 45.485 |  | 46.734 | -2.6727 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 41.945 |  | 42.4722 | -1.2413 | 44.155 | 41.78 | 0.5483 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 118.45 |  | 119.2999 | -0.7124 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.62 |  | 282.3846 | -0.2708 | 296.8 | 283.22 | 4.5061 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.27 |  | 518.3269 | -0.7827 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.36 |  | 295.79 | -0.4835 | 297.25 | 293.555 | 0.1189 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.25 |  | 26.5206 | -1.0205 | 27 | 25.42 | 0.0381 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.53 |  | 33.7164 | -0.5529 | 35.08 | 33.52 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.55 |  | 20.0489 | 2.4992 | 20.97 | 19.755 | 0.0487 | watch_only | none |
| SNDK | memory_hbm_storage | 1073.71 |  | 1100.5516 | -2.4389 | 1185.19 | 1114.57 | 0.2505 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| WDC | memory_hbm_storage | 454.375 |  | 439.1076 | 3.4769 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 749.33 |  | 730.5685 | 2.5681 | 774.805 | 719.02 | 0.1041 | watch_only | none |
| AMZN | cloud_ai_capex | 231.215 |  | 230.4651 | 0.3254 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.7 |  | 593.8307 | -0.022 | 600.765 | 594.21 | 1.2565 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 243.405 |  | 245.2777 | -0.7635 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.27 |  | 131.6253 | -1.0297 | 136.45 | 131.735 | 0.7139 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
