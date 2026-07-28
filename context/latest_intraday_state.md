# Intraday State

- Generated at: `2026-07-29T01:06:33+08:00`
- Market time ET: `2026-07-28T13:06:34-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'watch_only': 12, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_vwap': 5, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.03 |  | 673.7661 | 0.6328 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 494.23 |  | 489.7927 | 0.9059 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| SMH | semiconductor_index | 531.65 |  | 527.1234 | 0.8587 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| SPY | market_regime | 742.155 |  | 739.2127 | 0.398 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.4 |  | 195.7992 | 0.8176 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 381.805 |  | 378.3077 | 0.9245 | 378.64 | 371.57 | 0.11 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.155 |  | 739.2127 | 0.398 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.03 |  | 673.7661 | 0.6328 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.36 |  | 329.6721 | 1.422 | 330.21 | 324.97 | 0.1376 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.56 |  | 292.1592 | 0.4795 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.95 |  | 117.9186 | 2.5707 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.195 |  | 60.9834 | 1.9868 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 678.03 |  | 673.7661 | 0.6328 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.56 |  | 292.1592 | 0.4795 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.155 |  | 739.2127 | 0.398 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 339.63 |  | 338.8592 | 0.2275 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 5 | MU | memory_hbm_storage | 821 |  | 814.8328 | 0.7569 | 846.4 | 813.91 | 0.1376 | watch_only | none |
| 6 | MSFT | cloud_ai_capex | 398.64 |  | 396.091 | 0.6435 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 231.89 |  | 230.229 | 0.7214 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| 8 | HPE | ai_server_oem | 44.7 |  | 44.4483 | 0.5662 | 46.19 | 44.33 | 0.0895 | watch_only | none |
| 9 | NVDA | ai_accelerator | 197.4 |  | 195.7992 | 0.8176 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 381.805 |  | 378.3077 | 0.9245 | 378.64 | 371.57 | 0.11 | buy_precheck_manual_confirm | none |
| 11 | GOOGL | cloud_ai_capex | 334.36 |  | 329.6721 | 1.422 | 330.21 | 324.97 | 0.1376 | buy_precheck_manual_confirm | none |
| 12 | SMH | semiconductor_index | 531.65 |  | 527.1234 | 0.8587 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| 13 | SOXX | semiconductor_index | 494.23 |  | 489.7927 | 0.9059 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| 14 | ENTG | semiconductor_materials | 119.47 |  | 119.4418 | 0.0236 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 139.59 |  | 138.2651 | 0.9583 | 139.755 | 137.31 | 0.1433 | watch_only | none |
| 16 | IREN | high_beta_ai_infrastructure | 34.205 |  | 33.7022 | 1.4918 | 35.08 | 33.52 | 0.0292 | watch_only | none |
| 17 | ASML | semiconductor_equipment | 1584.33 |  | 1576.7796 | 0.4789 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ARM | ai_accelerator | 246.655 |  | 245.2755 | 0.5624 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ORCL | cloud_ai_capex | 120.95 |  | 117.9186 | 2.5707 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |
| 20 | TT | data_center_power_cooling | 468.075 |  | 464.8319 | 0.6977 | 477.73 | 460.77 | 3.978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.4 |  | 195.7992 | 0.8176 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 381.805 |  | 378.3077 | 0.9245 | 378.64 | 371.57 | 0.11 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.155 |  | 739.2127 | 0.398 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.03 |  | 673.7661 | 0.6328 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.36 |  | 329.6721 | 1.422 | 330.21 | 324.97 | 0.1376 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.56 |  | 292.1592 | 0.4795 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.95 |  | 117.9186 | 2.5707 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.195 |  | 60.9834 | 1.9868 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 392.12 |  | 387.175 | 1.2772 | 390.46 | 382.495 | 1.8311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ANET | ai_networking_optical | 167.745 |  | 163.9282 | 2.3283 | 165.975 | 160.51 | 0.7631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ETN | data_center_power_cooling | 384.94 |  | 380.3402 | 1.2094 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | MU | memory_hbm_storage | 821 |  | 814.8328 | 0.7569 | 846.4 | 813.91 | 0.1376 | watch_only | none |
| 13 | SMH | semiconductor_index | 531.65 |  | 527.1234 | 0.8587 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| 14 | SOXX | semiconductor_index | 494.23 |  | 489.7927 | 0.9059 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| 15 | JCI | data_center_power_cooling | 139.59 |  | 138.2651 | 0.9583 | 139.755 | 137.31 | 0.1433 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 398.64 |  | 396.091 | 0.6435 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.89 |  | 230.229 | 0.7214 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| 18 | HPE | ai_server_oem | 44.7 |  | 44.4483 | 0.5662 | 46.19 | 44.33 | 0.0895 | watch_only | none |
| 19 | MRVL | custom_silicon_networking | 177 |  | 173.9262 | 1.7673 | 181.24 | 172.395 | 0.3277 | watch_only | none |
| 20 | SMCI | ai_server_oem | 28.45 |  | 27.9293 | 1.8643 | 28.86 | 27.59 | 0.0703 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.03 |  | 673.7661 | 0.6328 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.195 |  | 60.9834 | 1.9868 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.4 |  | 195.7992 | 0.8176 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.64 |  | 396.091 | 0.6435 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| AAPL | mega_cap_platform | 339.63 |  | 338.8592 | 0.2275 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.36 |  | 329.6721 | 1.422 | 330.21 | 324.97 | 0.1376 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.51 |  | 455.2109 | 0.7247 | 472.485 | 453.76 | 4.6586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.12 |  | 387.175 | 1.2772 | 390.46 | 382.495 | 1.8311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 494.23 |  | 489.7927 | 0.9059 | 497.64 | 485.42 | 0.0728 | watch_only | none |
| SMH | semiconductor_index | 531.65 |  | 527.1234 | 0.8587 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| AVGO | custom_silicon_networking | 381.805 |  | 378.3077 | 0.9245 | 378.64 | 371.57 | 0.11 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 821 |  | 814.8328 | 0.7569 | 846.4 | 813.91 | 0.1376 | watch_only | none |
| MRVL | custom_silicon_networking | 177 |  | 173.9262 | 1.7673 | 181.24 | 172.395 | 0.3277 | watch_only | none |
| DELL | ai_server_oem | 385.17 |  | 374.3559 | 2.8887 | 402 | 374.02 | 0.4829 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.7 |  | 44.4483 | 0.5662 | 46.19 | 44.33 | 0.0895 | watch_only | none |
| SMCI | ai_server_oem | 28.45 |  | 27.9293 | 1.8643 | 28.86 | 27.59 | 0.0703 | watch_only | none |
| SPY | market_regime | 742.155 |  | 739.2127 | 0.398 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.56 |  | 292.1592 | 0.4795 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.95 |  | 117.9186 | 2.5707 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.8 |  | 66.188 | 2.4356 | 68.995 | 65.635 | 4.2625 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.2 |  | 266.2418 | 0.7355 | 273.86 | 266.04 | 0.9098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 384.94 |  | 380.3402 | 1.2094 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 587.33 |  | 581.6316 | 0.9797 | 603.25 | 584.69 | 2.1691 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 946.59 |  | 937.144 | 1.008 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.075 |  | 464.8319 | 0.6977 | 477.73 | 460.77 | 3.978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.59 |  | 138.2651 | 0.9583 | 139.755 | 137.31 | 0.1433 | watch_only | none |
| ANET | ai_networking_optical | 167.745 |  | 163.9282 | 2.3283 | 165.975 | 160.51 | 0.7631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 241.35 |  | 236.5628 | 2.0237 | 256.145 | 236.73 | 4.885 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 647.425 |  | 629.9672 | 2.7712 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 342.66 |  | 336.8275 | 1.7316 | 354.09 | 338.14 | 1.6576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.095 |  | 85.5838 | 2.9342 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.165 |  | 258.6706 | 2.5107 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1584.33 |  | 1576.7796 | 0.4789 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 476.05 |  | 477.0089 | -0.201 | 494.87 | 477.03 | 3.3316 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 269.21 |  | 266.116 | 1.1626 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 192.245 |  | 190.6174 | 0.8538 | 194.96 | 189.48 | 0.8271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 312 |  | 307.9645 | 1.3104 | 315.21 | 304.11 | 0.3622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 237.72 |  | 236.5238 | 0.5057 | 248.8 | 236.42 | 0.875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.31 |  | 46.8236 | -1.0969 | 51.64 | 47.435 | 3.6493 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.285 |  | 42.5111 | -0.5319 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.47 |  | 119.4418 | 0.0236 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 285.32 |  | 282.3041 | 1.0683 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 518.4 |  | 518.5626 | -0.0313 | 518.6 | 511.495 | 4.3113 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.67 |  | 295.8775 | -0.0701 | 297.25 | 293.555 | 4.1634 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.54 |  | 26.5416 | -0.0059 | 27 | 25.42 | 0.0754 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 34.205 |  | 33.7022 | 1.4918 | 35.08 | 33.52 | 0.0292 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.36 |  | 20.0107 | 1.7455 | 20.97 | 19.755 | 0.0982 | watch_only | none |
| SNDK | memory_hbm_storage | 1095.545 |  | 1102.7021 | -0.649 | 1185.19 | 1114.57 | 0.6107 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 458.5 |  | 437.408 | 4.822 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 754.495 |  | 726.3233 | 3.8787 | 774.805 | 719.02 | 0.4573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.89 |  | 230.229 | 0.7214 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| META | cloud_ai_capex | 593.26 |  | 593.8622 | -0.1014 | 600.765 | 594.21 | 1.0569 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 246.655 |  | 245.2755 | 0.5624 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.82 |  | 131.6246 | 0.9082 | 136.45 | 131.735 | 0.8959 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
