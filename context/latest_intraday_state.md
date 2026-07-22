# Intraday State

- Generated at: `2026-07-23T01:21:54+08:00`
- Market time ET: `2026-07-22T13:21:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 7, 'watch_only': 1, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 2, 'below_vwap': 11}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.68 |  | 707.415 | 0.1788 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.505 |  | 552.9281 | 1.1895 | 551.02 | 540.105 | 0.0608 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.64 |  | 585.1782 | 0.9334 | 581.9 | 572.01 | 0.0457 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.16 |  | 748.4843 | 0.0903 | 747.68 | 746.425 | 0.0107 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.43 |  | 211.094 | 1.1066 | 207.4 | 205.01 | 0.0187 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.28 |  | 420.7009 | 0.3753 | 419.42 | 414.87 | 0.3031 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 559.505 |  | 552.9281 | 1.1895 | 551.02 | 540.105 | 0.0608 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.64 |  | 585.1782 | 0.9334 | 581.9 | 572.01 | 0.0457 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 708.68 |  | 707.415 | 0.1788 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.16 |  | 748.4843 | 0.0903 | 747.68 | 746.425 | 0.0107 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1809.495 |  | 1797.1044 | 0.6895 | 1786.525 | 1767.54 | 0.0508 | buy_precheck_manual_confirm | none |
| 8 | AMKR | semiconductor_test_packaging | 67.61 |  | 67.4752 | 0.1998 | 66.73 | 64.98 | 0.1331 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.26 |  | 31.1787 | 0.2609 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 10 | CRWV | gpu_cloud_ai_factory | 83.67 |  | 83.5226 | 0.1765 | 83.22 | 79.6 | 0.0956 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.28 |  | 70.8425 | 0.6175 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.16 |  | 748.4843 | 0.0903 | 747.68 | 746.425 | 0.0107 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.68 |  | 707.415 | 0.1788 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 3 | CRWV | gpu_cloud_ai_factory | 83.67 |  | 83.5226 | 0.1765 | 83.22 | 79.6 | 0.0956 | buy_precheck_manual_confirm | none |
| 4 | AMKR | semiconductor_test_packaging | 67.61 |  | 67.4752 | 0.1998 | 66.73 | 64.98 | 0.1331 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 348.3 |  | 347.95 | 0.1006 | 348.76 | 346.23 | 0.0201 | watch_only | none |
| 6 | TSM | foundry | 422.28 |  | 420.7009 | 0.3753 | 419.42 | 414.87 | 0.3031 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 31.26 |  | 31.1787 | 0.2609 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1809.495 |  | 1797.1044 | 0.6895 | 1786.525 | 1767.54 | 0.0508 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 213.43 |  | 211.094 | 1.1066 | 207.4 | 205.01 | 0.0187 | buy_precheck_manual_confirm | none |
| 10 | LRCX | semiconductor_equipment | 320.08 |  | 318.9913 | 0.3413 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 143.085 |  | 142.9008 | 0.1289 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 408.595 |  | 407.916 | 0.1665 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 139.11 |  | 138.7448 | 0.2632 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 295.675 |  | 295.3371 | 0.1144 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APD | industrial_gases | 297.9 |  | 297.7593 | 0.0473 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SOXX | semiconductor_index | 559.505 |  | 552.9281 | 1.1895 | 551.02 | 540.105 | 0.0608 | buy_precheck_manual_confirm | none |
| 17 | SMH | semiconductor_index | 590.64 |  | 585.1782 | 0.9334 | 581.9 | 572.01 | 0.0457 | buy_precheck_manual_confirm | none |
| 18 | AMAT | semiconductor_equipment | 559.6 |  | 558.4352 | 0.2086 | 559.22 | 544.305 | 2.03 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 643.34 |  | 640.4078 | 0.4579 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TT | data_center_power_cooling | 475.91 |  | 473.513 | 0.5062 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.43 |  | 211.094 | 1.1066 | 207.4 | 205.01 | 0.0187 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.28 |  | 420.7009 | 0.3753 | 419.42 | 414.87 | 0.3031 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 559.505 |  | 552.9281 | 1.1895 | 551.02 | 540.105 | 0.0608 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.64 |  | 585.1782 | 0.9334 | 581.9 | 572.01 | 0.0457 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 708.68 |  | 707.415 | 0.1788 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.16 |  | 748.4843 | 0.0903 | 747.68 | 746.425 | 0.0107 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1809.495 |  | 1797.1044 | 0.6895 | 1786.525 | 1767.54 | 0.0508 | buy_precheck_manual_confirm | none |
| 8 | AMKR | semiconductor_test_packaging | 67.61 |  | 67.4752 | 0.1998 | 66.73 | 64.98 | 0.1331 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.26 |  | 31.1787 | 0.2609 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 10 | CRWV | gpu_cloud_ai_factory | 83.67 |  | 83.5226 | 0.1765 | 83.22 | 79.6 | 0.0956 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.28 |  | 70.8425 | 0.6175 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | TER | semiconductor_test_packaging | 371.46 |  | 371.541 | -0.0218 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | DELL | ai_server_oem | 441.96 |  | 442.7156 | -0.1707 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | MU | memory_hbm_storage | 976.77 |  | 967.4004 | 0.9685 | 963.41 | 936.99 | 0.9214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 556.63 |  | 551.4401 | 0.9412 | 548.755 | 526.6 | 2.7792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 475.91 |  | 473.513 | 0.5062 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1617.5 |  | 1577.5041 | 2.5354 | 1558.88 | 1518.99 | 2.1577 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | WDC | memory_hbm_storage | 560.43 |  | 555.7125 | 0.8489 | 548.14 | 526.22 | 4.9105 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 916.82 |  | 908.6233 | 0.9021 | 899.59 | 860.605 | 0.5377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 213.805 |  | 211.1679 | 1.2488 | 207.06 | 202.18 | 0.5285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.68 |  | 707.415 | 0.1788 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.28 |  | 70.8425 | 0.6175 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.43 |  | 211.094 | 1.1066 | 207.4 | 205.01 | 0.0187 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.79 |  | 390.3765 | -0.6626 | 400.89 | 392.26 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.56 |  | 325.191 | -0.5015 | 328.865 | 325.74 | 0.1607 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.3 |  | 347.95 | 0.1006 | 348.76 | 346.23 | 0.0201 | watch_only | none |
| AMD | ai_accelerator | 556.63 |  | 551.4401 | 0.9412 | 548.755 | 526.6 | 2.7792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.28 |  | 420.7009 | 0.3753 | 419.42 | 414.87 | 0.3031 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.505 |  | 552.9281 | 1.1895 | 551.02 | 540.105 | 0.0608 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.64 |  | 585.1782 | 0.9334 | 581.9 | 572.01 | 0.0457 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 395.99 |  | 390.0195 | 1.5308 | 387.635 | 380.205 | 2.9546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 976.77 |  | 967.4004 | 0.9685 | 963.41 | 936.99 | 0.9214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.805 |  | 211.1679 | 1.2488 | 207.06 | 202.18 | 0.5285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 441.96 |  | 442.7156 | -0.1707 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.835 |  | 49.0305 | -0.3987 | 48.96 | 47.01 | 0.0819 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.26 |  | 31.1787 | 0.2609 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.16 |  | 748.4843 | 0.0903 | 747.68 | 746.425 | 0.0107 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.32 |  | 295.1465 | -0.28 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.24 |  | 126.6837 | -0.3503 | 128.79 | 125.83 | 2.0041 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.67 |  | 83.5226 | 0.1765 | 83.22 | 79.6 | 0.0956 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 301.17 |  | 298.9228 | 0.7518 | 297.69 | 293.905 | 1.3481 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.595 |  | 407.916 | 0.1665 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.34 |  | 640.4078 | 0.4579 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 993.825 |  | 1007.6523 | -1.3722 | 1036.605 | 998.94 | 4.3509 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.91 |  | 473.513 | 0.5062 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.085 |  | 142.9008 | 0.1289 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.215 |  | 174.8551 | 0.2058 | 175.265 | 171.06 | 2.671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.49 |  | 316.1668 | -0.2141 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 831.06 |  | 840.5371 | -1.1275 | 840.47 | 814.62 | 3.6111 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.08 |  | 405.8783 | -0.9358 | 407.12 | 397.835 | 0.2338 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.475 |  | 114.58 | -2.7099 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.95 |  | 329.3297 | 1.4029 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1809.495 |  | 1797.1044 | 0.6895 | 1786.525 | 1767.54 | 0.0508 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.6 |  | 558.4352 | 0.2086 | 559.22 | 544.305 | 2.03 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.08 |  | 318.9913 | 0.3413 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.45 |  | 216.0865 | 0.1682 | 215.465 | 210.975 | 4.2874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.46 |  | 371.541 | -0.0218 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.675 |  | 295.3371 | 0.1144 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.61 |  | 67.4752 | 0.1998 | 66.73 | 64.98 | 0.1331 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.11 |  | 138.7448 | 0.2632 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.955 |  | 343.9679 | 1.1592 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.06 |  | 507.2321 | 0.5575 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.9 |  | 297.7593 | 0.0473 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.335 |  | 30.7765 | -1.4344 | 30.78 | 29.46 | 0.033 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.05 |  | 42.6761 | -1.4672 | 42.29 | 40.305 | 0.0476 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.84 |  | 24.1292 | -1.1986 | 24.255 | 23.58 | 0.0839 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1617.5 |  | 1577.5041 | 2.5354 | 1558.88 | 1518.99 | 2.1577 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 560.43 |  | 555.7125 | 0.8489 | 548.14 | 526.22 | 4.9105 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 916.82 |  | 908.6233 | 0.9021 | 899.59 | 860.605 | 0.5377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.26 |  | 244.4655 | -0.4931 | 248.43 | 244.47 | 0.0164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 629.215 |  | 631.2416 | -0.3211 | 647.02 | 632.77 | 0.0779 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 286.08 |  | 285.6434 | 0.1529 | 286.39 | 280.275 | 2.6251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.49 |  | 166.7664 | 1.0336 | 166.63 | 162.08 | 3.6857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
