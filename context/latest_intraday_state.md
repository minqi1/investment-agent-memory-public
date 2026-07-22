# Intraday State

- Generated at: `2026-07-23T00:38:19+08:00`
- Market time ET: `2026-07-22T12:38:20-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_opening_15m_low': 7, 'watch_only': 1, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 2, 'below_vwap': 11}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.76 |  | 707.1522 | 0.2274 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.77 |  | 552.4375 | 1.3273 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.18 |  | 584.7855 | 1.0935 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.835 |  | 748.3643 | 0.1965 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.7 |  | 210.7374 | 1.4058 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.77 |  | 552.4375 | 1.3273 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 591.18 |  | 584.7855 | 1.0935 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 213.33 |  | 210.9616 | 1.1227 | 207.06 | 202.18 | 0.2578 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 708.76 |  | 707.1522 | 0.2274 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.835 |  | 748.3643 | 0.1965 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 394.81 |  | 389.1132 | 1.464 | 387.635 | 380.205 | 0.1925 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1801.575 |  | 1796.0464 | 0.3078 | 1786.525 | 1767.54 | 0.0838 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.74 |  | 31.1508 | 1.8913 | 30.66 | 28.52 | 0.0315 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.36 |  | 70.8109 | 0.7754 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.835 |  | 748.3643 | 0.1965 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.76 |  | 707.1522 | 0.2274 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1801.575 |  | 1796.0464 | 0.3078 | 1786.525 | 1767.54 | 0.0838 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 348.28 |  | 347.9372 | 0.0985 | 348.76 | 346.23 | 0.0115 | watch_only | none |
| 5 | JCI | data_center_power_cooling | 143.295 |  | 142.8712 | 0.2966 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | NVDA | ai_accelerator | 213.7 |  | 210.7374 | 1.4058 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 7 | ETN | data_center_power_cooling | 408.575 |  | 407.7179 | 0.2102 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SOXX | semiconductor_index | 559.77 |  | 552.4375 | 1.3273 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| 9 | SMH | semiconductor_index | 591.18 |  | 584.7855 | 1.0935 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| 10 | AMAT | semiconductor_equipment | 559.22 |  | 558.3674 | 0.1527 | 559.22 | 544.305 | 0.4542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | LIN | industrial_gases | 508.88 |  | 507.0836 | 0.3543 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | CIEN | ai_networking_optical | 407.97 |  | 406.2099 | 0.4333 | 407.12 | 397.835 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | MRVL | custom_silicon_networking | 213.33 |  | 210.9616 | 1.1227 | 207.06 | 202.18 | 0.2578 | buy_precheck_manual_confirm | none |
| 14 | AVGO | custom_silicon_networking | 394.81 |  | 389.1132 | 1.464 | 387.635 | 380.205 | 0.1925 | buy_precheck_manual_confirm | none |
| 15 | TT | data_center_power_cooling | 475.575 |  | 472.8726 | 0.5715 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MKSI | semiconductor_materials | 345.41 |  | 343.4993 | 0.5562 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ONTO | semiconductor_test_packaging | 296.38 |  | 295.1178 | 0.4277 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TER | semiconductor_test_packaging | 373.58 |  | 371.4074 | 0.585 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 320.5 |  | 318.6652 | 0.5758 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TSM | foundry | 422.71 |  | 420.5228 | 0.5201 | 419.42 | 414.87 | 0.3549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.7 |  | 210.7374 | 1.4058 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.77 |  | 552.4375 | 1.3273 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 591.18 |  | 584.7855 | 1.0935 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 213.33 |  | 210.9616 | 1.1227 | 207.06 | 202.18 | 0.2578 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 708.76 |  | 707.1522 | 0.2274 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 394.81 |  | 389.1132 | 1.464 | 387.635 | 380.205 | 0.1925 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.835 |  | 748.3643 | 0.1965 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1801.575 |  | 1796.0464 | 0.3078 | 1786.525 | 1767.54 | 0.0838 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.74 |  | 31.1508 | 1.8913 | 30.66 | 28.52 | 0.0315 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.36 |  | 70.8109 | 0.7754 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 216.005 |  | 216.0892 | -0.039 | 215.465 | 210.975 | 4.5138 | below_vwap | below_vwap,spread_too_wide |
| 12 | HPE | ai_server_oem | 49.04 |  | 49.0438 | -0.0078 | 48.96 | 47.01 | 0.0408 | below_vwap | below_vwap |
| 13 | MU | memory_hbm_storage | 975.64 |  | 966.5775 | 0.9376 | 963.41 | 936.99 | 1.025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | IREN | high_beta_ai_infrastructure | 42.47 |  | 42.7487 | -0.652 | 42.29 | 40.305 | 0.0471 | below_vwap | below_vwap |
| 15 | TSM | foundry | 422.71 |  | 420.5228 | 0.5201 | 419.42 | 414.87 | 0.3549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 556.21 |  | 550.8687 | 0.9696 | 548.755 | 526.6 | 0.9205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 475.575 |  | 472.8726 | 0.5715 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SNDK | memory_hbm_storage | 1611.3 |  | 1574.0014 | 2.3697 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 560.4 |  | 555.1933 | 0.9378 | 548.14 | 526.22 | 1.5168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 916.21 |  | 907.4685 | 0.9633 | 899.59 | 860.605 | 0.68 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.76 |  | 707.1522 | 0.2274 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.36 |  | 70.8109 | 0.7754 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.7 |  | 210.7374 | 1.4058 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.92 |  | 390.5676 | -0.4219 | 400.89 | 392.26 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.13 |  | 325.4011 | -0.3906 | 328.865 | 325.74 | 0.0278 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.28 |  | 347.9372 | 0.0985 | 348.76 | 346.23 | 0.0115 | watch_only | none |
| AMD | ai_accelerator | 556.21 |  | 550.8687 | 0.9696 | 548.755 | 526.6 | 0.9205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.71 |  | 420.5228 | 0.5201 | 419.42 | 414.87 | 0.3549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.77 |  | 552.4375 | 1.3273 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.18 |  | 584.7855 | 1.0935 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 394.81 |  | 389.1132 | 1.464 | 387.635 | 380.205 | 0.1925 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 975.64 |  | 966.5775 | 0.9376 | 963.41 | 936.99 | 1.025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.33 |  | 210.9616 | 1.1227 | 207.06 | 202.18 | 0.2578 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 445.8 |  | 442.6592 | 0.7095 | 435.98 | 415.79 | 1.0655 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 49.04 |  | 49.0438 | -0.0078 | 48.96 | 47.01 | 0.0408 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.74 |  | 31.1508 | 1.8913 | 30.66 | 28.52 | 0.0315 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.835 |  | 748.3643 | 0.1965 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.78 |  | 295.2361 | -0.1545 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.86 |  | 126.7367 | -0.6918 | 128.79 | 125.83 | 2.2565 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.84 |  | 83.5102 | 0.3949 | 83.22 | 79.6 | 1.4074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 300.32 |  | 298.7442 | 0.5275 | 297.69 | 293.905 | 2.6638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.575 |  | 407.7179 | 0.2102 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 644.17 |  | 640.0714 | 0.6403 | 641.19 | 628.17 | 3.6186 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1000.57 |  | 1008.8696 | -0.8227 | 1036.605 | 998.94 | 0.7965 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.575 |  | 472.8726 | 0.5715 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.295 |  | 142.8712 | 0.2966 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.2 |  | 174.7927 | 0.8051 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 317.765 |  | 316.2881 | 0.467 | 317.93 | 306.89 | 1.7812 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 839 |  | 841.2993 | -0.2733 | 840.47 | 814.62 | 4.3075 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 407.97 |  | 406.2099 | 0.4333 | 407.12 | 397.835 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 113.025 |  | 114.7695 | -1.52 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 334.66 |  | 328.4207 | 1.8998 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1801.575 |  | 1796.0464 | 0.3078 | 1786.525 | 1767.54 | 0.0838 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.22 |  | 558.3674 | 0.1527 | 559.22 | 544.305 | 0.4542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.5 |  | 318.6652 | 0.5758 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.005 |  | 216.0892 | -0.039 | 215.465 | 210.975 | 4.5138 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 373.58 |  | 371.4074 | 0.585 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.38 |  | 295.1178 | 0.4277 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.81 |  | 67.4597 | 0.5192 | 66.73 | 64.98 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.635 |  | 138.7514 | -0.0839 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.41 |  | 343.4993 | 0.5562 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.88 |  | 507.0836 | 0.3543 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.255 |  | 297.7643 | -0.171 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.69 |  | 30.8326 | -0.4624 | 30.78 | 29.46 | 0.0652 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.47 |  | 42.7487 | -0.652 | 42.29 | 40.305 | 0.0471 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.945 |  | 24.1439 | -0.8239 | 24.255 | 23.58 | 0.1253 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1611.3 |  | 1574.0014 | 2.3697 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 560.4 |  | 555.1933 | 0.9378 | 548.14 | 526.22 | 1.5168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 916.21 |  | 907.4685 | 0.9633 | 899.59 | 860.605 | 0.68 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.86 |  | 244.544 | -0.2797 | 248.43 | 244.47 | 0.0164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 628.36 |  | 631.4433 | -0.4883 | 647.02 | 632.77 | 0.1162 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.395 |  | 285.6261 | -0.0809 | 286.39 | 280.275 | 2.9503 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 167.76 |  | 166.6803 | 0.6477 | 166.63 | 162.08 | 1.4306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
