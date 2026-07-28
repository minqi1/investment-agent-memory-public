# Intraday State

- Generated at: `2026-07-29T02:53:52+08:00`
- Market time ET: `2026-07-28T14:53:53-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'spread_too_wide_or_missing': 19, 'below_vwap': 9, 'manual_confirm_candidate': 6, 'price_stale_or_missing': 1, 'below_opening_15m_low': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.29 |  | 674.1583 | 0.3162 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| SOXX | semiconductor_index | 491.175 |  | 489.9886 | 0.2421 | 497.64 | 485.42 | 0.0631 | watch_only | none |
| SMH | semiconductor_index | 529.46 |  | 527.3739 | 0.3956 | 533.01 | 523.325 | 0.051 | watch_only | none |
| SPY | market_regime | 741.24 |  | 739.582 | 0.2242 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 391.61 |  | 387.7752 | 0.9889 | 390.46 | 382.495 | 0.0919 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.925 |  | 378.6295 | 0.6063 | 378.64 | 371.57 | 0.1024 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.24 |  | 739.582 | 0.2242 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.665 |  | 330.9509 | 1.4244 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 139.975 |  | 138.5778 | 1.0082 | 139.755 | 137.31 | 0.1286 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 121.26 |  | 118.5807 | 2.2595 | 117.17 | 115.25 | 0.066 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.24 |  | 739.582 | 0.2242 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.925 |  | 378.6295 | 0.6063 | 378.64 | 371.57 | 0.1024 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 491.175 |  | 489.9886 | 0.2421 | 497.64 | 485.42 | 0.0631 | watch_only | none |
| 4 | QQQ | market_regime | 676.29 |  | 674.1583 | 0.3162 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| 5 | IWM | market_regime | 293.24 |  | 292.3884 | 0.2913 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 6 | HPE | ai_server_oem | 44.45 |  | 44.4418 | 0.0185 | 46.19 | 44.33 | 0.045 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1581.31 |  | 1577.3378 | 0.2518 | 1586.01 | 1565.95 | 0.2846 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 397.085 |  | 396.4044 | 0.1717 | 400.09 | 392.355 | 0.1511 | watch_only | none |
| 9 | MRVL | custom_silicon_networking | 174.45 |  | 174.2071 | 0.1395 | 181.24 | 172.395 | 0.2752 | watch_only | none |
| 10 | SMH | semiconductor_index | 529.46 |  | 527.3739 | 0.3956 | 533.01 | 523.325 | 0.051 | watch_only | none |
| 11 | TSM | foundry | 391.61 |  | 387.7752 | 0.9889 | 390.46 | 382.495 | 0.0919 | buy_precheck_manual_confirm | none |
| 12 | TT | data_center_power_cooling | 467.11 |  | 465.2677 | 0.396 | 477.73 | 460.77 | 0.1006 | watch_only | none |
| 13 | JCI | data_center_power_cooling | 139.975 |  | 138.5778 | 1.0082 | 139.755 | 137.31 | 0.1286 | buy_precheck_manual_confirm | none |
| 14 | AMZN | cloud_ai_capex | 231.32 |  | 230.5076 | 0.3525 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 15 | SMCI | ai_server_oem | 28.19 |  | 28.0042 | 0.6636 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 16 | GOOGL | cloud_ai_capex | 335.665 |  | 330.9509 | 1.4244 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 17 | TER | semiconductor_test_packaging | 311.77 |  | 308.6961 | 0.9958 | 315.21 | 304.11 | 0.1251 | watch_only | none |
| 18 | AMD | ai_accelerator | 455.64 |  | 455.5422 | 0.0215 | 472.485 | 453.76 | 2.4208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | KLAC | semiconductor_equipment | 191.3 |  | 190.7855 | 0.2697 | 194.96 | 189.48 | 0.3816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CRWV | gpu_cloud_ai_factory | 66.46 |  | 66.2601 | 0.3016 | 68.995 | 65.635 | 2.0764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 391.61 |  | 387.7752 | 0.9889 | 390.46 | 382.495 | 0.0919 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.925 |  | 378.6295 | 0.6063 | 378.64 | 371.57 | 0.1024 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.24 |  | 739.582 | 0.2242 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.665 |  | 330.9509 | 1.4244 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 139.975 |  | 138.5778 | 1.0082 | 139.755 | 137.31 | 0.1286 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 121.26 |  | 118.5807 | 2.2595 | 117.17 | 115.25 | 0.066 | buy_precheck_manual_confirm | none |
| 7 | NVDA | ai_accelerator | 197 |  | 196.0848 | 0.4667 | 195.4 | 193.65 | 0.7157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 168.54 |  | 165.0537 | 2.1122 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 384.99 |  | 381.3009 | 0.9675 | 384.565 | 377.43 | 2.6416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMH | semiconductor_index | 529.46 |  | 527.3739 | 0.3956 | 533.01 | 523.325 | 0.051 | watch_only | none |
| 11 | SOXX | semiconductor_index | 491.175 |  | 489.9886 | 0.2421 | 497.64 | 485.42 | 0.0631 | watch_only | none |
| 12 | QQQ | market_regime | 676.29 |  | 674.1583 | 0.3162 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| 13 | ASML | semiconductor_equipment | 1581.31 |  | 1577.3378 | 0.2518 | 1586.01 | 1565.95 | 0.2846 | watch_only | none |
| 14 | TT | data_center_power_cooling | 467.11 |  | 465.2677 | 0.396 | 477.73 | 460.77 | 0.1006 | watch_only | none |
| 15 | IWM | market_regime | 293.24 |  | 292.3884 | 0.2913 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 16 | TER | semiconductor_test_packaging | 311.77 |  | 308.6961 | 0.9958 | 315.21 | 304.11 | 0.1251 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 397.085 |  | 396.4044 | 0.1717 | 400.09 | 392.355 | 0.1511 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.32 |  | 230.5076 | 0.3525 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.45 |  | 44.4418 | 0.0185 | 46.19 | 44.33 | 0.045 | watch_only | none |
| 20 | MRVL | custom_silicon_networking | 174.45 |  | 174.2071 | 0.1395 | 181.24 | 172.395 | 0.2752 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.29 |  | 674.1583 | 0.3162 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| TQQQ | leveraged_tool | 61.74 |  | 61.1153 | 1.0221 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197 |  | 196.0848 | 0.4667 | 195.4 | 193.65 | 0.7157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 397.085 |  | 396.4044 | 0.1717 | 400.09 | 392.355 | 0.1511 | watch_only | none |
| AAPL | mega_cap_platform | 338.88 |  | 338.9584 | -0.0231 | 342.87 | 337.78 | 0.0089 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 335.665 |  | 330.9509 | 1.4244 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.64 |  | 455.5422 | 0.0215 | 472.485 | 453.76 | 2.4208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.61 |  | 387.7752 | 0.9889 | 390.46 | 382.495 | 0.0919 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.175 |  | 489.9886 | 0.2421 | 497.64 | 485.42 | 0.0631 | watch_only | none |
| SMH | semiconductor_index | 529.46 |  | 527.3739 | 0.3956 | 533.01 | 523.325 | 0.051 | watch_only | none |
| AVGO | custom_silicon_networking | 380.925 |  | 378.6295 | 0.6063 | 378.64 | 371.57 | 0.1024 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.015 |  | 815.5202 | 0.4285 | 846.4 | 813.91 | 1.2478 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 174.45 |  | 174.2071 | 0.1395 | 181.24 | 172.395 | 0.2752 | watch_only | none |
| DELL | ai_server_oem | 387.93 |  | 375.2717 | 3.3731 | 402 | 374.02 | 3.5702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.45 |  | 44.4418 | 0.0185 | 46.19 | 44.33 | 0.045 | watch_only | none |
| SMCI | ai_server_oem | 28.19 |  | 28.0042 | 0.6636 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| SPY | market_regime | 741.24 |  | 739.582 | 0.2242 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.24 |  | 292.3884 | 0.2913 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 121.26 |  | 118.5807 | 2.2595 | 117.17 | 115.25 | 0.066 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.46 |  | 66.2601 | 0.3016 | 68.995 | 65.635 | 2.0764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.2 |  | 266.1345 | 0.4004 | 273.86 | 266.04 | 2.6422 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 384.99 |  | 381.3009 | 0.9675 | 384.565 | 377.43 | 2.6416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 585.76 |  | 582.4582 | 0.5669 | 603.25 | 584.69 | 2.1033 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 935.1 |  | 937.5609 | -0.2625 | 955.825 | 935.665 | 0.9806 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 467.11 |  | 465.2677 | 0.396 | 477.73 | 460.77 | 0.1006 | watch_only | none |
| JCI | data_center_power_cooling | 139.975 |  | 138.5778 | 1.0082 | 139.755 | 137.31 | 0.1286 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 168.54 |  | 165.0537 | 2.1122 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 241.23 |  | 237.4975 | 1.5716 | 256.145 | 236.73 | 4.6595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 643.71 |  | 632.2975 | 1.8049 | 673.65 | 624.91 | 4.095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.91 |  | 337.459 | 1.0226 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.39 |  | 85.844 | 1.8009 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.395 |  | 259.0985 | 0.8863 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1581.31 |  | 1577.3378 | 0.2518 | 1586.01 | 1565.95 | 0.2846 | watch_only | none |
| AMAT | semiconductor_equipment | 475.74 |  | 476.3366 | -0.1253 | 494.87 | 477.03 | 0.4267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.37 |  | 266.6736 | 1.3861 | 276.85 | 267.14 | 4.4384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.3 |  | 190.7855 | 0.2697 | 194.96 | 189.48 | 0.3816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 311.77 |  | 308.6961 | 0.9958 | 315.21 | 304.11 | 0.1251 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.99 |  | 236.7841 | 0.9316 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.07 |  | 46.6866 | -3.4626 | 51.64 | 47.435 | 2.1966 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.03 |  | 42.4394 | -0.9646 | 44.155 | 41.78 | 0.571 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 118.56 |  | 119.1632 | -0.5062 | 121 | 117.72 | 4.833 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 282.79 |  | 282.3596 | 0.1524 | 296.8 | 283.22 | 0.1803 | below_opening_15m_low | below_opening_15m_low |
| LIN | industrial_gases | 516.575 |  | 518.0948 | -0.2934 | 518.6 | 511.495 | 4.7021 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.46 |  | 295.7462 | -0.0968 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.23 |  | 26.5148 | -1.0743 | 27 | 25.42 | 0.1525 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.53 |  | 33.7085 | -0.5295 | 35.08 | 33.52 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.88 |  | 20.1068 | 3.8453 | 20.97 | 19.755 | 0.0958 | watch_only | none |
| SNDK | memory_hbm_storage | 1083.22 |  | 1099.4274 | -1.4742 | 1185.19 | 1114.57 | 3.0465 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.1 |  | 440.072 | 3.6421 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 746.98 |  | 732.3458 | 1.9983 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.32 |  | 230.5076 | 0.3525 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594.19 |  | 593.8227 | 0.0618 | 600.765 | 594.21 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 244.78 |  | 245.214 | -0.177 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.27 |  | 131.531 | -0.9587 | 136.45 | 131.735 | 1.1822 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
