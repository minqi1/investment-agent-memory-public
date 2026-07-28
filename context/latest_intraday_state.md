# Intraday State

- Generated at: `2026-07-29T03:24:35+08:00`
- Market time ET: `2026-07-28T15:24:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_vwap': 4, 'watch_only': 12, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.73 |  | 674.3089 | 0.5074 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 497.63 |  | 490.1648 | 1.523 | 497.64 | 485.42 | 0.0482 | watch_only | none |
| SMH | semiconductor_index | 534.49 |  | 527.6109 | 1.3038 | 533.01 | 523.325 | 0.0281 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 741.76 |  | 739.7119 | 0.2769 | 739.42 | 736.57 | 0.0013 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.88 |  | 196.1801 | 0.8665 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 394.515 |  | 388.2807 | 1.6056 | 390.46 | 382.495 | 0.2915 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 534.49 |  | 527.6109 | 1.3038 | 533.01 | 523.325 | 0.0281 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 384.67 |  | 378.9091 | 1.5204 | 378.64 | 371.57 | 0.0884 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 741.76 |  | 739.7119 | 0.2769 | 739.42 | 736.57 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 677.73 |  | 674.3089 | 0.5074 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.925 |  | 331.2664 | 0.8026 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 141.12 |  | 138.9094 | 1.5914 | 139.755 | 137.31 | 0.0638 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 293.35 |  | 292.4515 | 0.3072 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 10 | TER | semiconductor_test_packaging | 320.895 |  | 309.5867 | 3.6527 | 315.21 | 304.11 | 0.2244 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.09 |  | 20.1715 | 4.5533 | 20.97 | 19.755 | 0.0474 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 62.15 |  | 61.1538 | 1.629 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.76 |  | 739.7119 | 0.2769 | 739.42 | 736.57 | 0.0013 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.35 |  | 292.4515 | 0.3072 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 677.73 |  | 674.3089 | 0.5074 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 230.88 |  | 230.5444 | 0.1456 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.24 |  | 338.9835 | 0.0757 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 6 | TT | data_center_power_cooling | 469.26 |  | 465.7073 | 0.7629 | 477.73 | 460.77 | 0.1108 | watch_only | none |
| 7 | SMH | semiconductor_index | 534.49 |  | 527.6109 | 1.3038 | 533.01 | 523.325 | 0.0281 | buy_precheck_manual_confirm | none |
| 8 | IREN | high_beta_ai_infrastructure | 33.9 |  | 33.7037 | 0.5826 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| 9 | NVDA | ai_accelerator | 197.88 |  | 196.1801 | 0.8665 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 10 | GOOGL | cloud_ai_capex | 333.925 |  | 331.2664 | 0.8026 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| 11 | VRT | data_center_power_cooling | 269.56 |  | 266.2365 | 1.2483 | 273.86 | 266.04 | 0.1224 | watch_only | none |
| 12 | APLD | high_beta_ai_infrastructure | 26.83 |  | 26.5138 | 1.1927 | 27 | 25.42 | 0.0745 | watch_only | none |
| 13 | GEV | data_center_power_cooling | 940.1 |  | 937.4924 | 0.2781 | 955.825 | 935.665 | 0.4212 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | CORZ | high_beta_ai_infrastructure | 21.09 |  | 20.1715 | 4.5533 | 20.97 | 19.755 | 0.0474 | buy_precheck_manual_confirm | none |
| 15 | JCI | data_center_power_cooling | 141.12 |  | 138.9094 | 1.5914 | 139.755 | 137.31 | 0.0638 | buy_precheck_manual_confirm | none |
| 16 | COHU | semiconductor_test_packaging | 42.91 |  | 42.459 | 1.0623 | 44.155 | 41.78 | 0.233 | watch_only | none |
| 17 | ENTG | semiconductor_materials | 120 |  | 119.187 | 0.6821 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TSM | foundry | 394.515 |  | 388.2807 | 1.6056 | 390.46 | 382.495 | 0.2915 | buy_precheck_manual_confirm | none |
| 19 | SOXX | semiconductor_index | 497.63 |  | 490.1648 | 1.523 | 497.64 | 485.42 | 0.0482 | watch_only | none |
| 20 | AVGO | custom_silicon_networking | 384.67 |  | 378.9091 | 1.5204 | 378.64 | 371.57 | 0.0884 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.88 |  | 196.1801 | 0.8665 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 394.515 |  | 388.2807 | 1.6056 | 390.46 | 382.495 | 0.2915 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 534.49 |  | 527.6109 | 1.3038 | 533.01 | 523.325 | 0.0281 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 384.67 |  | 378.9091 | 1.5204 | 378.64 | 371.57 | 0.0884 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 741.76 |  | 739.7119 | 0.2769 | 739.42 | 736.57 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 677.73 |  | 674.3089 | 0.5074 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.925 |  | 331.2664 | 0.8026 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 141.12 |  | 138.9094 | 1.5914 | 139.755 | 137.31 | 0.0638 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 293.35 |  | 292.4515 | 0.3072 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 10 | TER | semiconductor_test_packaging | 320.895 |  | 309.5867 | 3.6527 | 315.21 | 304.11 | 0.2244 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.09 |  | 20.1715 | 4.5533 | 20.97 | 19.755 | 0.0474 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 62.15 |  | 61.1538 | 1.629 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| 13 | ASML | semiconductor_equipment | 1597.39 |  | 1577.9308 | 1.2332 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ANET | ai_networking_optical | 169.5 |  | 165.2045 | 2.6001 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ETN | data_center_power_cooling | 388.495 |  | 381.5773 | 1.8129 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ORCL | cloud_ai_capex | 120.96 |  | 118.8472 | 1.7777 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MU | memory_hbm_storage | 828.82 |  | 816.0691 | 1.5625 | 846.4 | 813.91 | 0.2594 | watch_only | none |
| 18 | SOXX | semiconductor_index | 497.63 |  | 490.1648 | 1.523 | 497.64 | 485.42 | 0.0482 | watch_only | none |
| 19 | TT | data_center_power_cooling | 469.26 |  | 465.7073 | 0.7629 | 477.73 | 460.77 | 0.1108 | watch_only | none |
| 20 | VRT | data_center_power_cooling | 269.56 |  | 266.2365 | 1.2483 | 273.86 | 266.04 | 0.1224 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.73 |  | 674.3089 | 0.5074 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.15 |  | 61.1538 | 1.629 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.88 |  | 196.1801 | 0.8665 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.08 |  | 396.3229 | -0.8183 | 400.09 | 392.355 | 0.2748 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.24 |  | 338.9835 | 0.0757 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.925 |  | 331.2664 | 0.8026 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 464.07 |  | 455.7547 | 1.8245 | 472.485 | 453.76 | 4.6028 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.515 |  | 388.2807 | 1.6056 | 390.46 | 382.495 | 0.2915 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 497.63 |  | 490.1648 | 1.523 | 497.64 | 485.42 | 0.0482 | watch_only | none |
| SMH | semiconductor_index | 534.49 |  | 527.6109 | 1.3038 | 533.01 | 523.325 | 0.0281 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 384.67 |  | 378.9091 | 1.5204 | 378.64 | 371.57 | 0.0884 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 828.82 |  | 816.0691 | 1.5625 | 846.4 | 813.91 | 0.2594 | watch_only | none |
| MRVL | custom_silicon_networking | 177.23 |  | 174.271 | 1.6979 | 181.24 | 172.395 | 4.9202 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 394.08 |  | 375.9883 | 4.8118 | 402 | 374.02 | 1.8753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.285 |  | 44.559 | 1.6292 | 46.19 | 44.33 | 0.0883 | watch_only | none |
| SMCI | ai_server_oem | 28.52 |  | 28.0236 | 1.7714 | 28.86 | 27.59 | 0.0701 | watch_only | none |
| SPY | market_regime | 741.76 |  | 739.7119 | 0.2769 | 739.42 | 736.57 | 0.0013 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.35 |  | 292.4515 | 0.3072 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.96 |  | 118.8472 | 1.7777 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 66.69 |  | 66.2747 | 0.6266 | 68.995 | 65.635 | 2.6541 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.56 |  | 266.2365 | 1.2483 | 273.86 | 266.04 | 0.1224 | watch_only | none |
| ETN | data_center_power_cooling | 388.495 |  | 381.5773 | 1.8129 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 591.07 |  | 582.9009 | 1.4014 | 603.25 | 584.69 | 0.3621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 940.1 |  | 937.4924 | 0.2781 | 955.825 | 935.665 | 0.4212 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.26 |  | 465.7073 | 0.7629 | 477.73 | 460.77 | 0.1108 | watch_only | none |
| JCI | data_center_power_cooling | 141.12 |  | 138.9094 | 1.5914 | 139.755 | 137.31 | 0.0638 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169.5 |  | 165.2045 | 2.6001 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 244.17 |  | 237.9693 | 2.6057 | 256.145 | 236.73 | 0.6962 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 653.49 |  | 632.9146 | 3.2509 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 348.42 |  | 337.6912 | 3.1771 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.63 |  | 85.9522 | 3.1154 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 264.44 |  | 259.3548 | 1.9607 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1597.39 |  | 1577.9308 | 1.2332 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 482.39 |  | 476.6779 | 1.1983 | 494.87 | 477.03 | 3.1966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 274.05 |  | 267.074 | 2.612 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 194.89 |  | 190.9764 | 2.0492 | 194.96 | 189.48 | 0.8774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 320.895 |  | 309.5867 | 3.6527 | 315.21 | 304.11 | 0.2244 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 242.46 |  | 237.1734 | 2.229 | 248.8 | 236.42 | 0.4702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.27 |  | 46.6653 | -0.847 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.91 |  | 42.459 | 1.0623 | 44.155 | 41.78 | 0.233 | watch_only | none |
| ENTG | semiconductor_materials | 120 |  | 119.187 | 0.6821 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 287.43 |  | 282.4858 | 1.7503 | 296.8 | 283.22 | 0.4418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.13 |  | 517.9471 | -0.5439 | 518.6 | 511.495 | 0.1223 | below_vwap | below_vwap |
| APD | industrial_gases | 295.285 |  | 295.7269 | -0.1494 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.83 |  | 26.5138 | 1.1927 | 27 | 25.42 | 0.0745 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.9 |  | 33.7037 | 0.5826 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.09 |  | 20.1715 | 4.5533 | 20.97 | 19.755 | 0.0474 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1124.09 |  | 1100.088 | 2.1818 | 1185.19 | 1114.57 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 462.425 |  | 441.407 | 4.7616 | 465.04 | 435.22 | 0.2898 | watch_only | none |
| STX | memory_hbm_storage | 752.53 |  | 733.5414 | 2.5886 | 774.805 | 719.02 | 1.1827 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.88 |  | 230.5444 | 0.1456 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 593.58 |  | 593.8487 | -0.0453 | 600.765 | 594.21 | 0.1735 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 247.77 |  | 245.2553 | 1.0253 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.47 |  | 131.5332 | 0.7122 | 136.45 | 131.735 | 1.9703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
