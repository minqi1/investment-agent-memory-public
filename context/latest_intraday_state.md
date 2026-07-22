# Intraday State

- Generated at: `2026-07-23T00:18:23+08:00`
- Market time ET: `2026-07-22T12:18:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'spread_too_wide_or_missing': 24, 'below_opening_15m_low': 6, 'watch_only': 1, 'price_stale_or_missing': 2, 'below_vwap': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.34 |  | 707.0822 | 0.3193 | 705.86 | 703.63 | 0.0113 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.47 |  | 552.1221 | 1.3309 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.16 |  | 584.6885 | 1.1068 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.69 |  | 748.2655 | 0.1904 | 747.68 | 746.425 | 0.0227 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 423.595 |  | 420.4083 | 0.758 | 419.42 | 414.87 | 0.2998 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 557.755 |  | 550.5504 | 1.3086 | 548.755 | 526.6 | 0.2707 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 919.08 |  | 906.8797 | 1.3453 | 899.59 | 860.605 | 0.2318 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.47 |  | 552.1221 | 1.3309 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.16 |  | 584.6885 | 1.1068 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.34 |  | 707.0822 | 0.3193 | 705.86 | 703.63 | 0.0113 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 372.31 |  | 371.1735 | 0.3062 | 369.53 | 365 | 0.2122 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 749.69 |  | 748.2655 | 0.1904 | 747.68 | 746.425 | 0.0227 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.15 |  | 558.3172 | 0.3283 | 559.22 | 544.305 | 0.2071 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 49.235 |  | 49.0388 | 0.4001 | 48.96 | 47.01 | 0.1219 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 32.065 |  | 31.1215 | 3.0315 | 30.66 | 28.52 | 0.0312 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 83.79 |  | 83.4921 | 0.3568 | 83.22 | 79.6 | 0.0835 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.48 |  | 70.7609 | 1.0162 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.69 |  | 748.2655 | 0.1904 | 747.68 | 746.425 | 0.0227 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.34 |  | 707.0822 | 0.3193 | 705.86 | 703.63 | 0.0113 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 560.15 |  | 558.3172 | 0.3283 | 559.22 | 544.305 | 0.2071 | buy_precheck_manual_confirm | none |
| 4 | TER | semiconductor_test_packaging | 372.31 |  | 371.1735 | 0.3062 | 369.53 | 365 | 0.2122 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 49.235 |  | 49.0388 | 0.4001 | 48.96 | 47.01 | 0.1219 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 348.51 |  | 347.879 | 0.1814 | 348.76 | 346.23 | 0.0143 | watch_only | none |
| 7 | CRWV | gpu_cloud_ai_factory | 83.79 |  | 83.4921 | 0.3568 | 83.22 | 79.6 | 0.0835 | buy_precheck_manual_confirm | none |
| 8 | TSM | foundry | 423.595 |  | 420.4083 | 0.758 | 419.42 | 414.87 | 0.2998 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 473.89 |  | 472.6473 | 0.2629 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ARM | ai_accelerator | 285.82 |  | 285.6244 | 0.0685 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 138.82 |  | 138.7592 | 0.0438 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 295.01 |  | 294.8995 | 0.0375 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SOXX | semiconductor_index | 559.47 |  | 552.1221 | 1.3309 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| 14 | SMH | semiconductor_index | 591.16 |  | 584.6885 | 1.1068 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| 15 | AMD | ai_accelerator | 557.755 |  | 550.5504 | 1.3086 | 548.755 | 526.6 | 0.2707 | buy_precheck_manual_confirm | none |
| 16 | STX | memory_hbm_storage | 919.08 |  | 906.8797 | 1.3453 | 899.59 | 860.605 | 0.2318 | buy_precheck_manual_confirm | none |
| 17 | LIN | industrial_gases | 508.14 |  | 507.0107 | 0.2227 | 507.545 | 505.59 | 4.7979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | PWR | data_center_power_cooling | 643.12 |  | 639.7018 | 0.5343 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 319.845 |  | 318.5137 | 0.418 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 142.965 |  | 142.8561 | 0.0762 | 143.27 | 141.04 | 5.0432 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 423.595 |  | 420.4083 | 0.758 | 419.42 | 414.87 | 0.2998 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 557.755 |  | 550.5504 | 1.3086 | 548.755 | 526.6 | 0.2707 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 919.08 |  | 906.8797 | 1.3453 | 899.59 | 860.605 | 0.2318 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.47 |  | 552.1221 | 1.3309 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.16 |  | 584.6885 | 1.1068 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.34 |  | 707.0822 | 0.3193 | 705.86 | 703.63 | 0.0113 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 372.31 |  | 371.1735 | 0.3062 | 369.53 | 365 | 0.2122 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 749.69 |  | 748.2655 | 0.1904 | 747.68 | 746.425 | 0.0227 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.15 |  | 558.3172 | 0.3283 | 559.22 | 544.305 | 0.2071 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 49.235 |  | 49.0388 | 0.4001 | 48.96 | 47.01 | 0.1219 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 32.065 |  | 31.1215 | 3.0315 | 30.66 | 28.52 | 0.0312 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 83.79 |  | 83.4921 | 0.3568 | 83.22 | 79.6 | 0.0835 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.48 |  | 70.7609 | 1.0162 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 14 | KLAC | semiconductor_equipment | 215.915 |  | 216.1099 | -0.0902 | 215.465 | 210.975 | 4.562 | below_vwap | below_vwap,spread_too_wide |
| 15 | NVDA | ai_accelerator | 213.625 |  | 210.3476 | 1.5581 | 207.4 | 205.01 | 0.9175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 978.02 |  | 966.0917 | 1.2347 | 963.41 | 936.99 | 1.5337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | APLD | high_beta_ai_infrastructure | 30.79 |  | 30.8428 | -0.1712 | 30.78 | 29.46 | 0.065 | below_vwap | below_vwap |
| 18 | IREN | high_beta_ai_infrastructure | 42.41 |  | 42.7644 | -0.8286 | 42.29 | 40.305 | 0.0707 | below_vwap | below_vwap |
| 19 | TT | data_center_power_cooling | 473.89 |  | 472.6473 | 0.2629 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SNDK | memory_hbm_storage | 1609.43 |  | 1572.6669 | 2.3376 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.34 |  | 707.0822 | 0.3193 | 705.86 | 703.63 | 0.0113 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.48 |  | 70.7609 | 1.0162 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.625 |  | 210.3476 | 1.5581 | 207.4 | 205.01 | 0.9175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 388.35 |  | 390.724 | -0.6076 | 400.89 | 392.26 | 0.1107 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.635 |  | 325.5213 | -0.2723 | 328.865 | 325.74 | 0.1663 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.51 |  | 347.879 | 0.1814 | 348.76 | 346.23 | 0.0143 | watch_only | none |
| AMD | ai_accelerator | 557.755 |  | 550.5504 | 1.3086 | 548.755 | 526.6 | 0.2707 | buy_precheck_manual_confirm | none |
| TSM | foundry | 423.595 |  | 420.4083 | 0.758 | 419.42 | 414.87 | 0.2998 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.47 |  | 552.1221 | 1.3309 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.16 |  | 584.6885 | 1.1068 | 581.9 | 572.01 | 0.0558 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 394.71 |  | 388.7043 | 1.5451 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 978.02 |  | 966.0917 | 1.2347 | 963.41 | 936.99 | 1.5337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.92 |  | 210.6493 | 1.5527 | 207.06 | 202.18 | 1.2294 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 445.49 |  | 442.4888 | 0.6782 | 435.98 | 415.79 | 1.1201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 49.235 |  | 49.0388 | 0.4001 | 48.96 | 47.01 | 0.1219 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 32.065 |  | 31.1215 | 3.0315 | 30.66 | 28.52 | 0.0312 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.69 |  | 748.2655 | 0.1904 | 747.68 | 746.425 | 0.0227 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.625 |  | 295.2661 | -0.2171 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.09 |  | 126.8067 | -0.5652 | 128.79 | 125.83 | 2.1255 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.79 |  | 83.4921 | 0.3568 | 83.22 | 79.6 | 0.0835 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 300.07 |  | 298.666 | 0.4701 | 297.69 | 293.905 | 1.1664 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.09 |  | 407.7375 | -0.1588 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.12 |  | 639.7018 | 0.5343 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 998.95 |  | 1009.4481 | -1.04 | 1036.605 | 998.94 | 0.6607 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.89 |  | 472.6473 | 0.2629 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.965 |  | 142.8561 | 0.0762 | 143.27 | 141.04 | 5.0432 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.95 |  | 174.707 | 0.7115 | 175.265 | 171.06 | 3.825 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 318.39 |  | 316.1535 | 0.7074 | 317.93 | 306.89 | 1.9065 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 846.88 |  | 841.1856 | 0.6769 | 840.47 | 814.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 405.915 |  | 406.1891 | -0.0675 | 407.12 | 397.835 | 3.0844 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 113.715 |  | 114.8355 | -0.9757 | 117.185 | 113.68 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.78 |  | 328.1553 | 1.714 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1804.57 |  | 1795.8351 | 0.4864 | 1786.525 | 1767.54 | 4.8266 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.15 |  | 558.3172 | 0.3283 | 559.22 | 544.305 | 0.2071 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 319.845 |  | 318.5137 | 0.418 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.915 |  | 216.1099 | -0.0902 | 215.465 | 210.975 | 4.562 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.31 |  | 371.1735 | 0.3062 | 369.53 | 365 | 0.2122 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 295.01 |  | 294.8995 | 0.0375 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.85 |  | 67.4513 | 0.5911 | 66.73 | 64.98 | 1.577 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.86 |  | 55.67 | 0.3413 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.82 |  | 138.7592 | 0.0438 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 345.54 |  | 343.3484 | 0.6383 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.14 |  | 507.0107 | 0.2227 | 507.545 | 505.59 | 4.7979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.135 |  | 297.7889 | -0.2196 | 300.24 | 297.585 | 0.0942 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.79 |  | 30.8428 | -0.1712 | 30.78 | 29.46 | 0.065 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.41 |  | 42.7644 | -0.8286 | 42.29 | 40.305 | 0.0707 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.94 |  | 24.1496 | -0.868 | 24.255 | 23.58 | 0.0835 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1609.43 |  | 1572.6669 | 2.3376 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 562.85 |  | 554.9 | 1.4327 | 548.14 | 526.22 | 1.7269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 919.08 |  | 906.8797 | 1.3453 | 899.59 | 860.605 | 0.2318 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 243.62 |  | 244.5842 | -0.3942 | 248.43 | 244.47 | 0.078 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 629.64 |  | 631.6568 | -0.3193 | 647.02 | 632.77 | 0.3097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.82 |  | 285.6244 | 0.0685 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 169.88 |  | 166.6547 | 1.9353 | 166.63 | 162.08 | 1.295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
