# Intraday State

- Generated at: `2026-07-24T02:47:10+08:00`
- Market time ET: `2026-07-23T14:47:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 21, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.83 |  | 692.9311 | -0.3032 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547 |  | 550.7853 | -0.6873 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.24 |  | 580.8139 | -0.7875 | 585.98 | 576.635 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.09 |  | 738.5831 | -0.2022 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 477.44 |  | 476.832 | 0.1275 | 480 | 472.33 | 0.2472 | watch_only | none |
| 2 | META | cloud_ai_capex | 606.89 |  | 604.4803 | 0.3986 | 614.15 | 605.39 | 0.2949 | watch_only | none |
| 3 | WDC | memory_hbm_storage | 564.26 |  | 564.2515 | 0.0015 | 576.24 | 556.3 | 1.1785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | CORZ | high_beta_ai_infrastructure | 24.16 |  | 24.0713 | 0.3684 | 24.46 | 23.265 | 0.0828 | watch_only | none |
| 5 | SNDK | memory_hbm_storage | 1652.4 |  | 1643.4622 | 0.5438 | 1651.355 | 1560 | 2.3644 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SOXX | semiconductor_index | 547 |  | 550.7853 | -0.6873 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| 7 | MU | memory_hbm_storage | 990.605 |  | 991.7206 | -0.1125 | 999.04 | 964.86 | 0.1474 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1796.34 |  | 1802.4981 | -0.3416 | 1806.11 | 1780.9 | 0.0696 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 558.09 |  | 564.927 | -1.2102 | 566.18 | 548.47 | 0.1308 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 291.31 |  | 291.6345 | -0.1113 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 11 | HPE | ai_server_oem | 47.66 |  | 48.2944 | -1.3135 | 48.88 | 47.635 | 0.1049 | below_vwap | below_vwap |
| 12 | SMCI | ai_server_oem | 31.145 |  | 31.6046 | -1.4543 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 40.76 |  | 41.6351 | -2.1018 | 43.21 | 40.51 | 0.0736 | below_vwap | below_vwap |
| 15 | CIEN | ai_networking_optical | 407.2 |  | 408.1626 | -0.2358 | 408.58 | 397.9 | 0.3438 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.465 |  | 143.8973 | -0.3004 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 649.62 |  | 651.7169 | -0.3217 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 318.52 |  | 320.4645 | -0.6068 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ARM | ai_accelerator | 279.62 |  | 279.6696 | -0.0177 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 313.57 |  | 317.6932 | -1.2979 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1037.61 |  | 1015.2045 | 2.207 | 1023.33 | 979.08 | 1.4032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1652.4 |  | 1643.4622 | 0.5438 | 1651.355 | 1560 | 2.3644 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TT | data_center_power_cooling | 477.44 |  | 476.832 | 0.1275 | 480 | 472.33 | 0.2472 | watch_only | none |
| 4 | META | cloud_ai_capex | 606.89 |  | 604.4803 | 0.3986 | 614.15 | 605.39 | 0.2949 | watch_only | none |
| 5 | CORZ | high_beta_ai_infrastructure | 24.16 |  | 24.0713 | 0.3684 | 24.46 | 23.265 | 0.0828 | watch_only | none |
| 6 | TSM | foundry | 414.965 |  | 416.4946 | -0.3673 | 420.72 | 412.69 | 0.723 | below_vwap | below_vwap,spread_too_wide |
| 7 | SOXX | semiconductor_index | 547 |  | 550.7853 | -0.6873 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| 8 | MU | memory_hbm_storage | 990.605 |  | 991.7206 | -0.1125 | 999.04 | 964.86 | 0.1474 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1796.34 |  | 1802.4981 | -0.3416 | 1806.11 | 1780.9 | 0.0696 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 558.09 |  | 564.927 | -1.2102 | 566.18 | 548.47 | 0.1308 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 175.89 |  | 176.6767 | -0.4453 | 177.84 | 173.19 | 1.0291 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.465 |  | 143.8973 | -0.3004 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 649.62 |  | 651.7169 | -0.3217 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 214.905 |  | 215.5144 | -0.2828 | 217.88 | 212.99 | 2.6663 | below_vwap | below_vwap,spread_too_wide |
| 15 | ETN | data_center_power_cooling | 412.895 |  | 413.325 | -0.104 | 415.53 | 406.545 | 0.6806 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.31 |  | 291.6345 | -0.1113 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 318.52 |  | 320.4645 | -0.6068 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 279.62 |  | 279.6696 | -0.0177 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505.56 |  | 507.2568 | -0.3345 | 510.71 | 502.72 | 4.9055 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.83 |  | 692.9311 | -0.3032 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.95 |  | 66.5293 | -0.8707 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.77 |  | 208.5707 | -0.3839 | 210.85 | 208.49 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.735 |  | 382.5426 | -0.2111 | 391.71 | 387.245 | 0.0131 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.205 |  | 320.9722 | -0.239 | 323.25 | 320.82 | 0.0062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.095 |  | 319.5456 | -0.141 | 324.42 | 320.24 | 0.1598 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 536.19 |  | 540.2567 | -0.7527 | 556.12 | 542.33 | 3.357 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.965 |  | 416.4946 | -0.3673 | 420.72 | 412.69 | 0.723 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547 |  | 550.7853 | -0.6873 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.24 |  | 580.8139 | -0.7875 | 585.98 | 576.635 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.91 |  | 392.1527 | -0.5719 | 397.34 | 390.54 | 1.3978 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 990.605 |  | 991.7206 | -0.1125 | 999.04 | 964.86 | 0.1474 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.63 |  | 209.4093 | -1.3272 | 213.785 | 207.665 | 3.6297 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 437.84 |  | 443.4804 | -1.2719 | 450.07 | 438.55 | 0.153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 47.66 |  | 48.2944 | -1.3135 | 48.88 | 47.635 | 0.1049 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.145 |  | 31.6046 | -1.4543 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 737.09 |  | 738.5831 | -0.2022 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.31 |  | 291.6345 | -0.1113 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.85 |  | 121.7198 | -1.5362 | 124.22 | 122.07 | 0.1669 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.64 |  | 82.7181 | -1.3033 | 84.415 | 80.64 | 3.8829 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.24 |  | 306.0752 | -1.253 | 311.13 | 303.96 | 0.6948 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.895 |  | 413.325 | -0.104 | 415.53 | 406.545 | 0.6806 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 649.62 |  | 651.7169 | -0.3217 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1037.61 |  | 1015.2045 | 2.207 | 1023.33 | 979.08 | 1.4032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.44 |  | 476.832 | 0.1275 | 480 | 472.33 | 0.2472 | watch_only | none |
| JCI | data_center_power_cooling | 143.465 |  | 143.8973 | -0.3004 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.89 |  | 176.6767 | -0.4453 | 177.84 | 173.19 | 1.0291 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.57 |  | 317.6932 | -1.2979 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.065 |  | 856.5462 | -2.5079 | 880.26 | 833 | 3.7267 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 407.2 |  | 408.1626 | -0.2358 | 408.58 | 397.9 | 0.3438 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 112.49 |  | 114.4879 | -1.7451 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 322.37 |  | 327.4316 | -1.5458 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.34 |  | 1802.4981 | -0.3416 | 1806.11 | 1780.9 | 0.0696 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.09 |  | 564.927 | -1.2102 | 566.18 | 548.47 | 0.1308 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 318.52 |  | 320.4645 | -0.6068 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.905 |  | 215.5144 | -0.2828 | 217.88 | 212.99 | 2.6663 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.98 |  | 372.0964 | -0.3 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.51 |  | 294.004 | -1.5286 | 301.305 | 293.685 | 0.4352 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.02 |  | 65.2124 | -0.295 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.385 |  | 135.0639 | -0.5027 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.43 |  | 342.7964 | -0.3986 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 505.56 |  | 507.2568 | -0.3345 | 510.71 | 502.72 | 4.9055 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.29 |  | 295.687 | -0.1343 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.05 |  | 30.055 | -0.0166 | 31.13 | 29.12 | 1.1647 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.76 |  | 41.6351 | -2.1018 | 43.21 | 40.51 | 0.0736 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.16 |  | 24.0713 | 0.3684 | 24.46 | 23.265 | 0.0828 | watch_only | none |
| SNDK | memory_hbm_storage | 1652.4 |  | 1643.4622 | 0.5438 | 1651.355 | 1560 | 2.3644 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 564.26 |  | 564.2515 | 0.0015 | 576.24 | 556.3 | 1.1785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 922.785 |  | 924.127 | -0.1452 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 233.82 |  | 234.3261 | -0.216 | 238.285 | 235.71 | 0.0086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.89 |  | 604.4803 | 0.3986 | 614.15 | 605.39 | 0.2949 | watch_only | none |
| ARM | ai_accelerator | 279.62 |  | 279.6696 | -0.0177 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 170.5 |  | 173.4898 | -1.7233 | 177.88 | 168.18 | 2.6334 | below_vwap | below_vwap,spread_too_wide |
