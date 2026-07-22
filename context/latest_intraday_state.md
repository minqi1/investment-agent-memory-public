# Intraday State

- Generated at: `2026-07-23T01:33:49+08:00`
- Market time ET: `2026-07-22T13:33:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 7, 'below_vwap': 12, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.515 |  | 707.472 | 0.1474 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 560.18 |  | 553.0428 | 1.2905 | 551.02 | 540.105 | 0.0446 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.13 |  | 585.6151 | 0.9417 | 581.9 | 572.01 | 0.0575 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.08 |  | 748.5073 | 0.0765 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.985 |  | 211.2 | 1.3186 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 560.18 |  | 553.0428 | 1.2905 | 551.02 | 540.105 | 0.0446 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 591.13 |  | 585.6151 | 0.9417 | 581.9 | 572.01 | 0.0575 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.515 |  | 707.472 | 0.1474 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 5 | TER | semiconductor_test_packaging | 372.55 |  | 371.5825 | 0.2604 | 369.53 | 365 | 0.3248 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.08 |  | 748.5073 | 0.0765 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1807.64 |  | 1797.9434 | 0.5393 | 1786.525 | 1767.54 | 0.0614 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.115 |  | 216.0956 | 0.009 | 215.465 | 210.975 | 0.1666 | buy_precheck_manual_confirm | none |
| 9 | DELL | ai_server_oem | 443.23 |  | 442.7162 | 0.1161 | 435.98 | 415.79 | 0.1241 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.25 |  | 70.8529 | 0.5605 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.08 |  | 748.5073 | 0.0765 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.515 |  | 707.472 | 0.1474 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.115 |  | 216.0956 | 0.009 | 215.465 | 210.975 | 0.1666 | buy_precheck_manual_confirm | none |
| 4 | TER | semiconductor_test_packaging | 372.55 |  | 371.5825 | 0.2604 | 369.53 | 365 | 0.3248 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 443.23 |  | 442.7162 | 0.1161 | 435.98 | 415.79 | 0.1241 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1807.64 |  | 1797.9434 | 0.5393 | 1786.525 | 1767.54 | 0.0614 | buy_precheck_manual_confirm | none |
| 8 | APD | industrial_gases | 297.92 |  | 297.7609 | 0.0534 | 300.24 | 297.585 | 0.2618 | watch_only | none |
| 9 | NVDA | ai_accelerator | 213.985 |  | 211.2 | 1.3186 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 10 | ARM | ai_accelerator | 285.9 |  | 285.6573 | 0.085 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 143.1 |  | 142.906 | 0.1358 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 296.18 |  | 295.3548 | 0.2794 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SOXX | semiconductor_index | 560.18 |  | 553.0428 | 1.2905 | 551.02 | 540.105 | 0.0446 | buy_precheck_manual_confirm | none |
| 14 | SMH | semiconductor_index | 591.13 |  | 585.6151 | 0.9417 | 581.9 | 572.01 | 0.0575 | buy_precheck_manual_confirm | none |
| 15 | AMAT | semiconductor_equipment | 559.875 |  | 558.4719 | 0.2512 | 559.22 | 544.305 | 2.0772 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 475.94 |  | 473.6234 | 0.4891 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SKHY | memory_hbm_storage | 167.23 |  | 166.8034 | 0.2558 | 166.63 | 162.08 | 2.4756 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ANET | ai_networking_optical | 175.21 |  | 174.8686 | 0.1952 | 175.265 | 171.06 | 3.3446 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LIN | industrial_gases | 509.44 |  | 507.2507 | 0.4316 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 643.81 |  | 640.5997 | 0.5011 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.985 |  | 211.2 | 1.3186 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 560.18 |  | 553.0428 | 1.2905 | 551.02 | 540.105 | 0.0446 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 591.13 |  | 585.6151 | 0.9417 | 581.9 | 572.01 | 0.0575 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.515 |  | 707.472 | 0.1474 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 5 | TER | semiconductor_test_packaging | 372.55 |  | 371.5825 | 0.2604 | 369.53 | 365 | 0.3248 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.08 |  | 748.5073 | 0.0765 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1807.64 |  | 1797.9434 | 0.5393 | 1786.525 | 1767.54 | 0.0614 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.115 |  | 216.0956 | 0.009 | 215.465 | 210.975 | 0.1666 | buy_precheck_manual_confirm | none |
| 9 | DELL | ai_server_oem | 443.23 |  | 442.7162 | 0.1161 | 435.98 | 415.79 | 0.1241 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.25 |  | 70.8529 | 0.5605 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 83.44 |  | 83.5257 | -0.1026 | 83.22 | 79.6 | 4.5182 | below_vwap | below_vwap,spread_too_wide |
| 13 | MU | memory_hbm_storage | 977.64 |  | 967.9223 | 1.004 | 963.41 | 936.99 | 1.2274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 422.62 |  | 420.7351 | 0.448 | 419.42 | 414.87 | 0.7903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 556.23 |  | 551.4986 | 0.8579 | 548.755 | 526.6 | 2.7812 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 475.94 |  | 473.6234 | 0.4891 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1623.01 |  | 1578.7675 | 2.8023 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 560.94 |  | 555.8745 | 0.9113 | 548.14 | 526.22 | 1.3442 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 914.735 |  | 908.8147 | 0.6514 | 899.59 | 860.605 | 0.8746 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 213.57 |  | 211.2303 | 1.1077 | 207.06 | 202.18 | 0.8803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.515 |  | 707.472 | 0.1474 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.25 |  | 70.8529 | 0.5605 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.985 |  | 211.2 | 1.3186 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.945 |  | 390.2797 | -0.5982 | 400.89 | 392.26 | 0.1263 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.84 |  | 325.138 | -0.3992 | 328.865 | 325.74 | 0.2069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.88 |  | 347.9582 | -0.0225 | 348.76 | 346.23 | 0.0489 | below_vwap | below_vwap |
| AMD | ai_accelerator | 556.23 |  | 551.4986 | 0.8579 | 548.755 | 526.6 | 2.7812 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.62 |  | 420.7351 | 0.448 | 419.42 | 414.87 | 0.7903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 560.18 |  | 553.0428 | 1.2905 | 551.02 | 540.105 | 0.0446 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.13 |  | 585.6151 | 0.9417 | 581.9 | 572.01 | 0.0575 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.895 |  | 390.1637 | 1.7253 | 387.635 | 380.205 | 0.839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 977.64 |  | 967.9223 | 1.004 | 963.41 | 936.99 | 1.2274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.57 |  | 211.2303 | 1.1077 | 207.06 | 202.18 | 0.8803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.23 |  | 442.7162 | 0.1161 | 435.98 | 415.79 | 0.1241 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 48.85 |  | 49.0289 | -0.3648 | 48.96 | 47.01 | 0.0409 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.08 |  | 748.5073 | 0.0765 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.395 |  | 295.1325 | -0.2499 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.28 |  | 126.6712 | -0.3088 | 128.79 | 125.83 | 0.0634 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.44 |  | 83.5257 | -0.1026 | 83.22 | 79.6 | 4.5182 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.165 |  | 299.0073 | 0.7216 | 297.69 | 293.905 | 1.451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.605 |  | 407.9418 | -0.0826 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.81 |  | 640.5997 | 0.5011 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 991.53 |  | 1007.3474 | -1.5702 | 1036.605 | 998.94 | 0.3217 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 475.94 |  | 473.6234 | 0.4891 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.1 |  | 142.906 | 0.1358 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.21 |  | 174.8686 | 0.1952 | 175.265 | 171.06 | 3.3446 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.87 |  | 316.1555 | -0.4066 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 828.78 |  | 840.3844 | -1.3808 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.89 |  | 405.7676 | -0.7092 | 407.12 | 397.835 | 1.8616 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.555 |  | 114.4571 | -2.5355 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.54 |  | 329.462 | 1.2378 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1807.64 |  | 1797.9434 | 0.5393 | 1786.525 | 1767.54 | 0.0614 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.875 |  | 558.4719 | 0.2512 | 559.22 | 544.305 | 2.0772 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.63 |  | 319.0338 | 0.8138 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.115 |  | 216.0956 | 0.009 | 215.465 | 210.975 | 0.1666 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 372.55 |  | 371.5825 | 0.2604 | 369.53 | 365 | 0.3248 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 296.18 |  | 295.3548 | 0.2794 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.68 |  | 67.4776 | 0.2999 | 66.73 | 64.98 | 4.078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 | 0.6983 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| ENTG | semiconductor_materials | 139.615 |  | 138.7689 | 0.6097 | 140.09 | 135.555 | 4.6628 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 346.9 |  | 344.0622 | 0.8248 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.44 |  | 507.2507 | 0.4316 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.92 |  | 297.7609 | 0.0534 | 300.24 | 297.585 | 0.2618 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 30.305 |  | 30.7676 | -1.5036 | 30.78 | 29.46 | 0.066 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.125 |  | 42.6521 | -1.2357 | 42.29 | 40.305 | 0.0475 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.845 |  | 24.1251 | -1.1612 | 24.255 | 23.58 | 0.0839 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1623.01 |  | 1578.7675 | 2.8023 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 560.94 |  | 555.8745 | 0.9113 | 548.14 | 526.22 | 1.3442 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 914.735 |  | 908.8147 | 0.6514 | 899.59 | 860.605 | 0.8746 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 242.88 |  | 244.4275 | -0.6331 | 248.43 | 244.47 | 0.0124 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 627.77 |  | 631.0971 | -0.5272 | 647.02 | 632.77 | 0.0621 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.9 |  | 285.6573 | 0.085 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 167.23 |  | 166.8034 | 0.2558 | 166.63 | 162.08 | 2.4756 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
