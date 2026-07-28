# Intraday State

- Generated at: `2026-07-29T01:02:43+08:00`
- Market time ET: `2026-07-28T13:02:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'watch_only': 14, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_vwap': 4, 'below_opening_15m_low': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.81 |  | 673.7207 | 0.7554 | 677.3 | 670.84 | 0.0177 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 495.915 |  | 489.7795 | 1.2527 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| SMH | semiconductor_index | 533.61 |  | 527.0874 | 1.2375 | 533.01 | 523.325 | 0.075 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.61 |  | 739.1649 | 0.4661 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.04 |  | 195.7757 | 1.1566 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 533.61 |  | 527.0874 | 1.2375 | 533.01 | 523.325 | 0.075 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.61 |  | 739.1649 | 0.4661 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.81 |  | 673.7207 | 0.7554 | 677.3 | 670.84 | 0.0177 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1588.56 |  | 1576.688 | 0.753 | 1586.01 | 1565.95 | 0.09 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 334.47 |  | 329.5585 | 1.4903 | 330.21 | 324.97 | 0.2751 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.65 |  | 292.1462 | 0.5147 | 293.26 | 291.55 | 0.0136 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.46 |  | 60.9692 | 2.4451 | 62.01 | 60.23 | 0.032 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 678.81 |  | 673.7207 | 0.7554 | 677.3 | 670.84 | 0.0177 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1588.56 |  | 1576.688 | 0.753 | 1586.01 | 1565.95 | 0.09 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 293.65 |  | 292.1462 | 0.5147 | 293.26 | 291.55 | 0.0136 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 742.61 |  | 739.1649 | 0.4661 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 339.785 |  | 338.8542 | 0.2747 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 6 | TT | data_center_power_cooling | 468.22 |  | 464.7941 | 0.7371 | 477.73 | 460.77 | 0.1217 | watch_only | none |
| 7 | SMH | semiconductor_index | 533.61 |  | 527.0874 | 1.2375 | 533.01 | 523.325 | 0.075 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 398.555 |  | 396.0724 | 0.6268 | 400.09 | 392.355 | 0.0176 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 231.42 |  | 230.2083 | 0.5263 | 233.05 | 229.7 | 0.0691 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 26.7 |  | 26.5411 | 0.5988 | 27 | 25.42 | 0.1498 | watch_only | none |
| 11 | NVDA | ai_accelerator | 198.04 |  | 195.7757 | 1.1566 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 12 | MU | memory_hbm_storage | 826.395 |  | 814.7574 | 1.4284 | 846.4 | 813.91 | 0.0908 | watch_only | none |
| 13 | SOXX | semiconductor_index | 495.915 |  | 489.7795 | 1.2527 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| 14 | GOOGL | cloud_ai_capex | 334.47 |  | 329.5585 | 1.4903 | 330.21 | 324.97 | 0.2751 | buy_precheck_manual_confirm | none |
| 15 | KLAC | semiconductor_equipment | 193.03 |  | 190.5986 | 1.2757 | 194.96 | 189.48 | 0.0622 | watch_only | none |
| 16 | HPE | ai_server_oem | 44.885 |  | 44.4449 | 0.9902 | 46.19 | 44.33 | 0.1114 | watch_only | none |
| 17 | ARM | ai_accelerator | 248.285 |  | 245.2522 | 1.2366 | 253.38 | 243.72 | 0.2658 | watch_only | none |
| 18 | ENTG | semiconductor_materials | 120.06 |  | 119.4416 | 0.5178 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | COHR | ai_networking_optical | 243.06 |  | 236.4866 | 2.7796 | 256.145 | 236.73 | 0.1234 | watch_only | none |
| 20 | AMAT | semiconductor_equipment | 479.55 |  | 477.0009 | 0.5344 | 494.87 | 477.03 | 2.6421 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.04 |  | 195.7757 | 1.1566 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 533.61 |  | 527.0874 | 1.2375 | 533.01 | 523.325 | 0.075 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.61 |  | 739.1649 | 0.4661 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.81 |  | 673.7207 | 0.7554 | 677.3 | 670.84 | 0.0177 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1588.56 |  | 1576.688 | 0.753 | 1586.01 | 1565.95 | 0.09 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 334.47 |  | 329.5585 | 1.4903 | 330.21 | 324.97 | 0.2751 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.65 |  | 292.1462 | 0.5147 | 293.26 | 291.55 | 0.0136 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.46 |  | 60.9692 | 2.4451 | 62.01 | 60.23 | 0.032 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 392.85 |  | 387.1508 | 1.4721 | 390.46 | 382.495 | 1.8862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | AVGO | custom_silicon_networking | 383.53 |  | 378.2855 | 1.3864 | 378.64 | 371.57 | 3.1627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ANET | ai_networking_optical | 168.06 |  | 163.9105 | 2.5315 | 165.975 | 160.51 | 0.7735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | JCI | data_center_power_cooling | 139.82 |  | 138.2612 | 1.1274 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ETN | data_center_power_cooling | 385.65 |  | 380.3119 | 1.4036 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ORCL | cloud_ai_capex | 121.16 |  | 117.8656 | 2.795 | 117.17 | 115.25 | 0.8419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MU | memory_hbm_storage | 826.395 |  | 814.7574 | 1.4284 | 846.4 | 813.91 | 0.0908 | watch_only | none |
| 16 | SOXX | semiconductor_index | 495.915 |  | 489.7795 | 1.2527 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| 17 | TT | data_center_power_cooling | 468.22 |  | 464.7941 | 0.7371 | 477.73 | 460.77 | 0.1217 | watch_only | none |
| 18 | KLAC | semiconductor_equipment | 193.03 |  | 190.5986 | 1.2757 | 194.96 | 189.48 | 0.0622 | watch_only | none |
| 19 | ARM | ai_accelerator | 248.285 |  | 245.2522 | 1.2366 | 253.38 | 243.72 | 0.2658 | watch_only | none |
| 20 | MSFT | cloud_ai_capex | 398.555 |  | 396.0724 | 0.6268 | 400.09 | 392.355 | 0.0176 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.81 |  | 673.7207 | 0.7554 | 677.3 | 670.84 | 0.0177 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.46 |  | 60.9692 | 2.4451 | 62.01 | 60.23 | 0.032 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 198.04 |  | 195.7757 | 1.1566 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.555 |  | 396.0724 | 0.6268 | 400.09 | 392.355 | 0.0176 | watch_only | none |
| AAPL | mega_cap_platform | 339.785 |  | 338.8542 | 0.2747 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.47 |  | 329.5585 | 1.4903 | 330.21 | 324.97 | 0.2751 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 461.82 |  | 455.1801 | 1.4587 | 472.485 | 453.76 | 3.3693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.85 |  | 387.1508 | 1.4721 | 390.46 | 382.495 | 1.8862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.915 |  | 489.7795 | 1.2527 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| SMH | semiconductor_index | 533.61 |  | 527.0874 | 1.2375 | 533.01 | 523.325 | 0.075 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 383.53 |  | 378.2855 | 1.3864 | 378.64 | 371.57 | 3.1627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 826.395 |  | 814.7574 | 1.4284 | 846.4 | 813.91 | 0.0908 | watch_only | none |
| MRVL | custom_silicon_networking | 177.685 |  | 173.9117 | 2.1696 | 181.24 | 172.395 | 2.0992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 386.41 |  | 374.3171 | 3.2307 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.885 |  | 44.4449 | 0.9902 | 46.19 | 44.33 | 0.1114 | watch_only | none |
| SMCI | ai_server_oem | 28.56 |  | 27.9242 | 2.2768 | 28.86 | 27.59 | 0.035 | watch_only | none |
| SPY | market_regime | 742.61 |  | 739.1649 | 0.4661 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.65 |  | 292.1462 | 0.5147 | 293.26 | 291.55 | 0.0136 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 121.16 |  | 117.8656 | 2.795 | 117.17 | 115.25 | 0.8419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 68.12 |  | 66.1534 | 2.9728 | 68.995 | 65.635 | 4.3306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.93 |  | 266.2307 | 1.0139 | 273.86 | 266.04 | 1.4353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.65 |  | 380.3119 | 1.4036 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 588.89 |  | 581.5399 | 1.2639 | 603.25 | 584.69 | 2.357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 949.04 |  | 937.1138 | 1.2727 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.22 |  | 464.7941 | 0.7371 | 477.73 | 460.77 | 0.1217 | watch_only | none |
| JCI | data_center_power_cooling | 139.82 |  | 138.2612 | 1.1274 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.06 |  | 163.9105 | 2.5315 | 165.975 | 160.51 | 0.7735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 243.06 |  | 236.4866 | 2.7796 | 256.145 | 236.73 | 0.1234 | watch_only | none |
| LITE | ai_networking_optical | 652.16 |  | 629.8187 | 3.5473 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 343.99 |  | 336.8147 | 2.1303 | 354.09 | 338.14 | 0.3779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.595 |  | 85.5724 | 3.5322 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.165 |  | 258.6706 | 2.5107 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1588.56 |  | 1576.688 | 0.753 | 1586.01 | 1565.95 | 0.09 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 479.55 |  | 477.0009 | 0.5344 | 494.87 | 477.03 | 2.6421 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 270.52 |  | 266.1056 | 1.6589 | 276.85 | 267.14 | 3.2308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.03 |  | 190.5986 | 1.2757 | 194.96 | 189.48 | 0.0622 | watch_only | none |
| TER | semiconductor_test_packaging | 313.74 |  | 307.8823 | 1.9026 | 315.21 | 304.11 | 0.4335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 238.36 |  | 236.4978 | 0.7874 | 248.8 | 236.42 | 4.2415 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.375 |  | 46.8242 | -0.9593 | 51.64 | 47.435 | 2.5876 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.42 |  | 42.5152 | -0.224 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.06 |  | 119.4416 | 0.5178 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 286.18 |  | 282.2481 | 1.3931 | 296.8 | 283.22 | 0.5346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 518.43 |  | 518.5632 | -0.0257 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.63 |  | 295.9015 | -0.0918 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.7 |  | 26.5411 | 0.5988 | 27 | 25.42 | 0.1498 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.475 |  | 33.6968 | 2.3093 | 35.08 | 33.52 | 0.029 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.35 |  | 20.0082 | 1.7081 | 20.97 | 19.755 | 0.0983 | watch_only | none |
| SNDK | memory_hbm_storage | 1102.08 |  | 1102.7216 | -0.0582 | 1185.19 | 1114.57 | 1.3157 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.99 |  | 437.3226 | 5.1832 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 754.32 |  | 725.9497 | 3.908 | 774.805 | 719.02 | 0.9532 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.42 |  | 230.2083 | 0.5263 | 233.05 | 229.7 | 0.0691 | watch_only | none |
| META | cloud_ai_capex | 593.78 |  | 593.8734 | -0.0157 | 600.765 | 594.21 | 0.6619 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 248.285 |  | 245.2522 | 1.2366 | 253.38 | 243.72 | 0.2658 | watch_only | none |
| SKHY | memory_hbm_storage | 133.62 |  | 131.6158 | 1.5228 | 136.45 | 131.735 | 0.9729 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
