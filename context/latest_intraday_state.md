# Intraday State

- Generated at: `2026-07-23T03:11:15+08:00`
- Market time ET: `2026-07-22T15:11:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 20, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.24 |  | 707.4514 | -0.0299 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.62 |  | 554.0128 | 0.8316 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.3 |  | 586.5879 | 0.6328 | 581.9 | 572.01 | 0.0373 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.16 |  | 748.5015 | -0.0456 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.64 |  | 211.6223 | 0.9534 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.82 |  | 421.0436 | 0.4219 | 419.42 | 414.87 | 0.026 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.62 |  | 554.0128 | 0.8316 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.3 |  | 586.5879 | 0.6328 | 581.9 | 572.01 | 0.0373 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1803.86 |  | 1799.1773 | 0.2603 | 1786.525 | 1767.54 | 0.0676 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 216.67 |  | 216.1589 | 0.2365 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 302.73 |  | 299.6861 | 1.0157 | 297.69 | 293.905 | 0.2444 | buy_precheck_manual_confirm | none |
| 8 | PWR | data_center_power_cooling | 643.4 |  | 641.592 | 0.2818 | 641.19 | 628.17 | 0.115 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 70.875 |  | 70.8601 | 0.021 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | PWR | data_center_power_cooling | 643.4 |  | 641.592 | 0.2818 | 641.19 | 628.17 | 0.115 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 216.67 |  | 216.1589 | 0.2365 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1803.86 |  | 1799.1773 | 0.2603 | 1786.525 | 1767.54 | 0.0676 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 175.22 |  | 174.9575 | 0.15 | 175.265 | 171.06 | 0.1484 | watch_only | none |
| 5 | TSM | foundry | 422.82 |  | 421.0436 | 0.4219 | 419.42 | 414.87 | 0.026 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 244.625 |  | 244.1872 | 0.1793 | 248.43 | 244.47 | 0.0164 | watch_only | none |
| 7 | SMH | semiconductor_index | 590.3 |  | 586.5879 | 0.6328 | 581.9 | 572.01 | 0.0373 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 558.62 |  | 554.0128 | 0.8316 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 213.64 |  | 211.6223 | 0.9534 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 10 | ENTG | semiconductor_materials | 138.95 |  | 138.8605 | 0.0645 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 296.01 |  | 295.3972 | 0.2074 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | AMAT | semiconductor_equipment | 560.075 |  | 558.8328 | 0.2223 | 559.22 | 544.305 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | MU | memory_hbm_storage | 968.64 |  | 968.4707 | 0.0175 | 963.41 | 936.99 | 1.2389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 302.73 |  | 299.6861 | 1.0157 | 297.69 | 293.905 | 0.2444 | buy_precheck_manual_confirm | none |
| 15 | TER | semiconductor_test_packaging | 371.925 |  | 371.6667 | 0.0695 | 369.53 | 365 | 5.1139 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LIN | industrial_gases | 509.33 |  | 507.4498 | 0.3705 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MKSI | semiconductor_materials | 347.22 |  | 345.507 | 0.4958 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 320.73 |  | 319.5651 | 0.3645 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 556.81 |  | 556.2496 | 0.1007 | 548.14 | 526.22 | 1.0578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ALAB | ai_networking_optical | 331.37 |  | 329.923 | 0.4386 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.64 |  | 211.6223 | 0.9534 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.82 |  | 421.0436 | 0.4219 | 419.42 | 414.87 | 0.026 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.62 |  | 554.0128 | 0.8316 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.3 |  | 586.5879 | 0.6328 | 581.9 | 572.01 | 0.0373 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1803.86 |  | 1799.1773 | 0.2603 | 1786.525 | 1767.54 | 0.0676 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 216.67 |  | 216.1589 | 0.2365 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 302.73 |  | 299.6861 | 1.0157 | 297.69 | 293.905 | 0.2444 | buy_precheck_manual_confirm | none |
| 8 | PWR | data_center_power_cooling | 643.4 |  | 641.592 | 0.2818 | 641.19 | 628.17 | 0.115 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 70.875 |  | 70.8601 | 0.021 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 906.33 |  | 909.4111 | -0.3388 | 899.59 | 860.605 | 1.7146 | below_vwap | below_vwap,spread_too_wide |
| 11 | QQQ | market_regime | 707.24 |  | 707.4514 | -0.0299 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 748.16 |  | 748.5015 | -0.0456 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 13 | AMKR | semiconductor_test_packaging | 67.29 |  | 67.468 | -0.2639 | 66.73 | 64.98 | 2.3183 | below_vwap | below_vwap,spread_too_wide |
| 14 | SMCI | ai_server_oem | 30.665 |  | 31.1477 | -1.5499 | 30.66 | 28.52 | 0.0326 | below_vwap | below_vwap |
| 15 | CRWV | gpu_cloud_ai_factory | 83.29 |  | 83.3456 | -0.0667 | 83.22 | 79.6 | 0.1081 | below_vwap | below_vwap |
| 16 | MU | memory_hbm_storage | 968.64 |  | 968.4707 | 0.0175 | 963.41 | 936.99 | 1.2389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 556.47 |  | 552.4452 | 0.7285 | 548.755 | 526.6 | 0.4331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SNDK | memory_hbm_storage | 1606.8 |  | 1582.3076 | 1.5479 | 1558.88 | 1518.99 | 3.9507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | WDC | memory_hbm_storage | 556.81 |  | 556.2496 | 0.1007 | 548.14 | 526.22 | 1.0578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 212.575 |  | 211.5311 | 0.4935 | 207.06 | 202.18 | 1.002 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.24 |  | 707.4514 | -0.0299 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.875 |  | 70.8601 | 0.021 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.64 |  | 211.6223 | 0.9534 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.285 |  | 389.7309 | -0.1144 | 400.89 | 392.26 | 0.4213 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 324.36 |  | 324.9562 | -0.1835 | 328.865 | 325.74 | 0.3669 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 345.99 |  | 347.642 | -0.4752 | 348.76 | 346.23 | 0.0462 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 556.47 |  | 552.4452 | 0.7285 | 548.755 | 526.6 | 0.4331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.82 |  | 421.0436 | 0.4219 | 419.42 | 414.87 | 0.026 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.62 |  | 554.0128 | 0.8316 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.3 |  | 586.5879 | 0.6328 | 581.9 | 572.01 | 0.0373 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.755 |  | 392.0129 | 1.4648 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 968.64 |  | 968.4707 | 0.0175 | 963.41 | 936.99 | 1.2389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.575 |  | 211.5311 | 0.4935 | 207.06 | 202.18 | 1.002 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 442.66 |  | 442.3532 | 0.0694 | 435.98 | 415.79 | 0.5693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.33 |  | 48.9301 | -1.2264 | 48.96 | 47.01 | 0.2897 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.665 |  | 31.1477 | -1.5499 | 30.66 | 28.52 | 0.0326 | below_vwap | below_vwap |
| SPY | market_regime | 748.16 |  | 748.5015 | -0.0456 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.665 |  | 294.927 | -0.4279 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.57 |  | 126.4702 | -0.7118 | 128.79 | 125.83 | 2.4449 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.29 |  | 83.3456 | -0.0667 | 83.22 | 79.6 | 0.1081 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 302.73 |  | 299.6861 | 1.0157 | 297.69 | 293.905 | 0.2444 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.295 |  | 407.7379 | -0.3539 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.4 |  | 641.592 | 0.2818 | 641.19 | 628.17 | 0.115 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 994.5 |  | 1004.3564 | -0.9814 | 1036.605 | 998.94 | 0.8517 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.46 |  | 473.8871 | -0.0901 | 473.865 | 466.83 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.36 |  | 142.9081 | -0.3835 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.22 |  | 174.9575 | 0.15 | 175.265 | 171.06 | 0.1484 | watch_only | none |
| COHR | ai_networking_optical | 315.38 |  | 316.0214 | -0.203 | 317.93 | 306.89 | 0.1839 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 827.615 |  | 837.9879 | -1.2378 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 401.2 |  | 405.0403 | -0.9481 | 407.12 | 397.835 | 1.6849 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.68 |  | 113.9807 | -2.8959 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.37 |  | 329.923 | 0.4386 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1803.86 |  | 1799.1773 | 0.2603 | 1786.525 | 1767.54 | 0.0676 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.075 |  | 558.8328 | 0.2223 | 559.22 | 544.305 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.73 |  | 319.5651 | 0.3645 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.67 |  | 216.1589 | 0.2365 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 371.925 |  | 371.6667 | 0.0695 | 369.53 | 365 | 5.1139 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.01 |  | 295.3972 | 0.2074 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.29 |  | 67.468 | -0.2639 | 66.73 | 64.98 | 2.3183 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.28 |  | 55.625 | -0.6202 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.95 |  | 138.8605 | 0.0645 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.22 |  | 345.507 | 0.4958 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.33 |  | 507.4498 | 0.3705 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297 |  | 297.8046 | -0.2702 | 300.24 | 297.585 | 4.7374 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.03 |  | 30.6713 | -2.0908 | 30.78 | 29.46 | 0.0666 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.465 |  | 42.4575 | -2.3376 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.595 |  | 23.9839 | -1.6217 | 24.255 | 23.58 | 0.0848 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1606.8 |  | 1582.3076 | 1.5479 | 1558.88 | 1518.99 | 3.9507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 556.81 |  | 556.2496 | 0.1007 | 548.14 | 526.22 | 1.0578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 906.33 |  | 909.4111 | -0.3388 | 899.59 | 860.605 | 1.7146 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 244.625 |  | 244.1872 | 0.1793 | 248.43 | 244.47 | 0.0164 | watch_only | none |
| META | cloud_ai_capex | 627.415 |  | 630.2554 | -0.4507 | 647.02 | 632.77 | 0.373 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.36 |  | 285.5803 | -0.0772 | 286.39 | 280.275 | 2.807 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.14 |  | 166.7362 | -0.3576 | 166.63 | 162.08 | 1.4385 | below_vwap | below_vwap,spread_too_wide |
