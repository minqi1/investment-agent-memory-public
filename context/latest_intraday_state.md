# Intraday State

- Generated at: `2026-07-23T01:02:02+08:00`
- Market time ET: `2026-07-22T13:02:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 7, 'watch_only': 3, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 2, 'below_vwap': 9}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709 |  | 707.2644 | 0.2454 | 705.86 | 703.63 | 0.0183 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.355 |  | 552.6565 | 1.2121 | 551.02 | 540.105 | 0.0715 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.555 |  | 584.9627 | 0.956 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.88 |  | 748.4449 | 0.1917 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.175 |  | 210.9164 | 1.545 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.9 |  | 420.6013 | 0.5465 | 419.42 | 414.87 | 0.279 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 559.355 |  | 552.6565 | 1.2121 | 551.02 | 540.105 | 0.0715 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.555 |  | 584.9627 | 0.956 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.54 |  | 211.0456 | 1.1819 | 207.06 | 202.18 | 0.2997 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709 |  | 707.2644 | 0.2454 | 705.86 | 703.63 | 0.0183 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.88 |  | 748.4449 | 0.1917 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1807.14 |  | 1796.4765 | 0.5936 | 1786.525 | 1767.54 | 0.0575 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 216.22 |  | 216.058 | 0.075 | 215.465 | 210.975 | 0.0971 | buy_precheck_manual_confirm | none |
| 10 | LIN | industrial_gases | 509.4 |  | 507.167 | 0.4403 | 507.545 | 505.59 | 0.157 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.56 |  | 31.1695 | 1.2527 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.45 |  | 70.8273 | 0.8792 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.88 |  | 748.4449 | 0.1917 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709 |  | 707.2644 | 0.2454 | 705.86 | 703.63 | 0.0183 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.22 |  | 216.058 | 0.075 | 215.465 | 210.975 | 0.0971 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1807.14 |  | 1796.4765 | 0.5936 | 1786.525 | 1767.54 | 0.0575 | buy_precheck_manual_confirm | none |
| 5 | LIN | industrial_gases | 509.4 |  | 507.167 | 0.4403 | 507.545 | 505.59 | 0.157 | buy_precheck_manual_confirm | none |
| 6 | ARM | ai_accelerator | 286.07 |  | 285.623 | 0.1565 | 286.39 | 280.275 | 0.2062 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 348.12 |  | 347.9451 | 0.0503 | 348.76 | 346.23 | 0.2356 | watch_only | none |
| 8 | ANET | ai_networking_optical | 175.11 |  | 174.8242 | 0.1635 | 175.265 | 171.06 | 0.1542 | watch_only | none |
| 9 | TSM | foundry | 422.9 |  | 420.6013 | 0.5465 | 419.42 | 414.87 | 0.279 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 590.555 |  | 584.9627 | 0.956 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| 11 | JCI | data_center_power_cooling | 143.22 |  | 142.8861 | 0.2337 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 408.77 |  | 407.8525 | 0.225 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 139.03 |  | 138.7083 | 0.2319 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 296.27 |  | 295.3431 | 0.3139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SOXX | semiconductor_index | 559.355 |  | 552.6565 | 1.2121 | 551.02 | 540.105 | 0.0715 | buy_precheck_manual_confirm | none |
| 16 | TT | data_center_power_cooling | 475.47 |  | 473.0732 | 0.5066 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SMCI | ai_server_oem | 31.56 |  | 31.1695 | 1.2527 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 18 | AMKR | semiconductor_test_packaging | 67.685 |  | 67.4707 | 0.3176 | 66.73 | 64.98 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | MRVL | custom_silicon_networking | 213.54 |  | 211.0456 | 1.1819 | 207.06 | 202.18 | 0.2997 | buy_precheck_manual_confirm | none |
| 20 | AMAT | semiconductor_equipment | 558.63 |  | 558.3643 | 0.0476 | 559.22 | 544.305 | 2.0479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.175 |  | 210.9164 | 1.545 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.9 |  | 420.6013 | 0.5465 | 419.42 | 414.87 | 0.279 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 559.355 |  | 552.6565 | 1.2121 | 551.02 | 540.105 | 0.0715 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.555 |  | 584.9627 | 0.956 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.54 |  | 211.0456 | 1.1819 | 207.06 | 202.18 | 0.2997 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709 |  | 707.2644 | 0.2454 | 705.86 | 703.63 | 0.0183 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.88 |  | 748.4449 | 0.1917 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1807.14 |  | 1796.4765 | 0.5936 | 1786.525 | 1767.54 | 0.0575 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 216.22 |  | 216.058 | 0.075 | 215.465 | 210.975 | 0.0971 | buy_precheck_manual_confirm | none |
| 10 | LIN | industrial_gases | 509.4 |  | 507.167 | 0.4403 | 507.545 | 505.59 | 0.157 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.56 |  | 31.1695 | 1.2527 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.45 |  | 70.8273 | 0.8792 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 13 | MU | memory_hbm_storage | 975.07 |  | 966.9803 | 0.8366 | 963.41 | 936.99 | 0.6153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 556.115 |  | 551.0932 | 0.9112 | 548.755 | 526.6 | 2.7818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.47 |  | 473.0732 | 0.5066 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1613.58 |  | 1575.8063 | 2.3971 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 561.44 |  | 555.4561 | 1.0773 | 548.14 | 526.22 | 4.5775 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 915.68 |  | 908.1552 | 0.8286 | 899.59 | 860.605 | 0.4761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 372.515 |  | 371.4406 | 0.2892 | 369.53 | 365 | 4.8213 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 396.8 |  | 389.6939 | 1.8235 | 387.635 | 380.205 | 0.8846 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709 |  | 707.2644 | 0.2454 | 705.86 | 703.63 | 0.0183 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.45 |  | 70.8273 | 0.8792 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 214.175 |  | 210.9164 | 1.545 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.215 |  | 390.4732 | -0.3222 | 400.89 | 392.26 | 0.2955 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.15 |  | 325.2694 | -0.3442 | 328.865 | 325.74 | 0.1604 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.12 |  | 347.9451 | 0.0503 | 348.76 | 346.23 | 0.2356 | watch_only | none |
| AMD | ai_accelerator | 556.115 |  | 551.0932 | 0.9112 | 548.755 | 526.6 | 2.7818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.9 |  | 420.6013 | 0.5465 | 419.42 | 414.87 | 0.279 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.355 |  | 552.6565 | 1.2121 | 551.02 | 540.105 | 0.0715 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.555 |  | 584.9627 | 0.956 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.8 |  | 389.6939 | 1.8235 | 387.635 | 380.205 | 0.8846 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 975.07 |  | 966.9803 | 0.8366 | 963.41 | 936.99 | 0.6153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.54 |  | 211.0456 | 1.1819 | 207.06 | 202.18 | 0.2997 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 443.16 |  | 442.7141 | 0.1007 | 435.98 | 415.79 | 0.7988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.81 |  | 49.0373 | -0.4636 | 48.96 | 47.01 | 0.041 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.56 |  | 31.1695 | 1.2527 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.88 |  | 748.4449 | 0.1917 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.63 |  | 295.1926 | -0.1906 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.76 |  | 126.6887 | 0.0563 | 128.79 | 125.83 | 1.6882 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 83.715 |  | 83.5144 | 0.2403 | 83.22 | 79.6 | 1.5648 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 300.635 |  | 298.8046 | 0.6126 | 297.69 | 293.905 | 1.2374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.77 |  | 407.8525 | 0.225 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.74 |  | 640.2153 | 0.5505 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 996.05 |  | 1008.3958 | -1.2243 | 1036.605 | 998.94 | 1.005 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.47 |  | 473.0732 | 0.5066 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.22 |  | 142.8861 | 0.2337 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.11 |  | 174.8242 | 0.1635 | 175.265 | 171.06 | 0.1542 | watch_only | none |
| COHR | ai_networking_optical | 315.99 |  | 316.1776 | -0.0593 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.63 |  | 840.925 | -0.6297 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 403.44 |  | 405.993 | -0.6288 | 407.12 | 397.835 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 112.74 |  | 114.7115 | -1.7186 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 334.3 |  | 328.9597 | 1.6234 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1807.14 |  | 1796.4765 | 0.5936 | 1786.525 | 1767.54 | 0.0575 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 558.63 |  | 558.3643 | 0.0476 | 559.22 | 544.305 | 2.0479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.72 |  | 318.8426 | 0.5888 | 317.72 | 311.31 | 4.7019 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.22 |  | 216.058 | 0.075 | 215.465 | 210.975 | 0.0971 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 372.515 |  | 371.4406 | 0.2892 | 369.53 | 365 | 4.8213 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.27 |  | 295.3431 | 0.3139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.685 |  | 67.4707 | 0.3176 | 66.73 | 64.98 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.03 |  | 138.7083 | 0.2319 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 345.16 |  | 343.6069 | 0.452 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.4 |  | 507.167 | 0.4403 | 507.545 | 505.59 | 0.157 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 297.73 |  | 297.7606 | -0.0103 | 300.24 | 297.585 | 0.084 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 30.32 |  | 30.795 | -1.5425 | 30.78 | 29.46 | 0.066 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.01 |  | 42.7078 | -1.6339 | 42.29 | 40.305 | 0.0476 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.84 |  | 24.1348 | -1.2214 | 24.255 | 23.58 | 0.1258 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1613.58 |  | 1575.8063 | 2.3971 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 561.44 |  | 555.4561 | 1.0773 | 548.14 | 526.22 | 4.5775 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 915.68 |  | 908.1552 | 0.8286 | 899.59 | 860.605 | 0.4761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.91 |  | 244.5208 | -0.2498 | 248.43 | 244.47 | 0.0164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 629.945 |  | 631.3234 | -0.2183 | 647.02 | 632.77 | 0.327 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 286.07 |  | 285.623 | 0.1565 | 286.39 | 280.275 | 0.2062 | watch_only | none |
| SKHY | memory_hbm_storage | 167.95 |  | 166.7 | 0.7498 | 166.63 | 162.08 | 4.7633 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
