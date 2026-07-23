# Intraday State

- Generated at: `2026-07-24T03:25:57+08:00`
- Market time ET: `2026-07-23T15:25:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 18, 'watch_only': 2, 'below_vwap': 28, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 5, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.91 |  | 692.7667 | -0.268 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.4 |  | 550.6205 | -0.4033 | 557.38 | 545.965 | 0.0474 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.2 |  | 580.4017 | -0.3793 | 585.98 | 576.635 | 0.0242 | below_vwap | below_vwap |
| SPY | market_regime | 737.61 |  | 738.4507 | -0.1138 | 742.515 | 738.54 | 0.0149 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1035.08 |  | 1017.1046 | 1.7673 | 1023.33 | 979.08 | 0.0696 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 320.95 |  | 320.9412 | 0.0027 | 323.25 | 320.82 | 0.0093 | watch_only | none |
| 2 | KLAC | semiconductor_equipment | 216.99 |  | 215.5747 | 0.6565 | 217.88 | 212.99 | 0.0415 | watch_only | none |
| 3 | ETN | data_center_power_cooling | 414.16 |  | 413.3536 | 0.1951 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.85 |  | 295.6942 | 0.0527 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 479.145 |  | 476.9227 | 0.466 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1035.08 |  | 1017.1046 | 1.7673 | 1023.33 | 979.08 | 0.0696 | buy_precheck_manual_confirm | none |
| 7 | ARM | ai_accelerator | 281.3 |  | 279.5724 | 0.6179 | 283 | 276.24 | 2.5631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | META | cloud_ai_capex | 607.105 |  | 604.6932 | 0.3988 | 614.15 | 605.39 | 1.0591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TSM | foundry | 415.655 |  | 416.2921 | -0.153 | 420.72 | 412.69 | 0.1299 | below_vwap | below_vwap |
| 10 | SMH | semiconductor_index | 578.2 |  | 580.4017 | -0.3793 | 585.98 | 576.635 | 0.0242 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 548.4 |  | 550.6205 | -0.4033 | 557.38 | 545.965 | 0.0474 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1800.69 |  | 1801.479 | -0.0438 | 1806.11 | 1780.9 | 0.0822 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 291.56 |  | 291.6078 | -0.0164 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 14 | WDC | memory_hbm_storage | 557.88 |  | 563.887 | -1.0653 | 576.24 | 556.3 | 0.0627 | below_vwap | below_vwap |
| 15 | SMCI | ai_server_oem | 31.11 |  | 31.5704 | -1.4585 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 40.735 |  | 41.5341 | -1.924 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| 18 | AMAT | semiconductor_equipment | 560.22 |  | 563.8551 | -0.6447 | 566.18 | 548.47 | 0.1517 | below_vwap | below_vwap |
| 19 | PWR | data_center_power_cooling | 646.56 |  | 651.2666 | -0.7227 | 656.38 | 642.37 | 0.1609 | below_vwap | below_vwap |
| 20 | JCI | data_center_power_cooling | 143.56 |  | 143.7984 | -0.1658 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1035.08 |  | 1017.1046 | 1.7673 | 1023.33 | 979.08 | 0.0696 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 216.99 |  | 215.5747 | 0.6565 | 217.88 | 212.99 | 0.0415 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 320.95 |  | 320.9412 | 0.0027 | 323.25 | 320.82 | 0.0093 | watch_only | none |
| 4 | TSM | foundry | 415.655 |  | 416.2921 | -0.153 | 420.72 | 412.69 | 0.1299 | below_vwap | below_vwap |
| 5 | SMH | semiconductor_index | 578.2 |  | 580.4017 | -0.3793 | 585.98 | 576.635 | 0.0242 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 548.4 |  | 550.6205 | -0.4033 | 557.38 | 545.965 | 0.0474 | below_vwap | below_vwap |
| 7 | AVGO | custom_silicon_networking | 390.84 |  | 391.9342 | -0.2792 | 397.34 | 390.54 | 1.7066 | below_vwap | below_vwap,spread_too_wide |
| 8 | MU | memory_hbm_storage | 986.625 |  | 990.8723 | -0.4286 | 999.04 | 964.86 | 1.9906 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1800.69 |  | 1801.479 | -0.0438 | 1806.11 | 1780.9 | 0.0822 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 560.22 |  | 563.8551 | -0.6447 | 566.18 | 548.47 | 0.1517 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 175.57 |  | 176.6038 | -0.5854 | 177.84 | 173.19 | 2.489 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.56 |  | 143.7984 | -0.1658 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 646.56 |  | 651.2666 | -0.7227 | 656.38 | 642.37 | 0.1609 | below_vwap | below_vwap |
| 14 | IWM | market_regime | 291.56 |  | 291.6078 | -0.0164 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 319.375 |  | 320.0325 | -0.2055 | 322.4 | 317.27 | 4.0579 | below_vwap | below_vwap,spread_too_wide |
| 16 | WDC | memory_hbm_storage | 557.88 |  | 563.887 | -1.0653 | 576.24 | 556.3 | 0.0627 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 505.53 |  | 507.1678 | -0.3229 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHR | ai_networking_optical | 311.87 |  | 316.9802 | -1.6122 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CIEN | ai_networking_optical | 404.58 |  | 407.7627 | -0.7805 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.91 |  | 692.7667 | -0.268 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66 |  | 66.4875 | -0.7332 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208 |  | 208.4994 | -0.2395 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.245 |  | 382.413 | -0.3054 | 391.71 | 387.245 | 0.362 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.95 |  | 320.9412 | 0.0027 | 323.25 | 320.82 | 0.0093 | watch_only | none |
| GOOGL | cloud_ai_capex | 317.92 |  | 319.4833 | -0.4893 | 324.42 | 320.24 | 0.0755 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 537.87 |  | 539.8746 | -0.3713 | 556.12 | 542.33 | 4.265 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.655 |  | 416.2921 | -0.153 | 420.72 | 412.69 | 0.1299 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.4 |  | 550.6205 | -0.4033 | 557.38 | 545.965 | 0.0474 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.2 |  | 580.4017 | -0.3793 | 585.98 | 576.635 | 0.0242 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.84 |  | 391.9342 | -0.2792 | 397.34 | 390.54 | 1.7066 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 986.625 |  | 990.8723 | -0.4286 | 999.04 | 964.86 | 1.9906 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 207.27 |  | 209.2157 | -0.93 | 213.785 | 207.665 | 1.3509 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 436.785 |  | 443.1559 | -1.4376 | 450.07 | 438.55 | 1.669 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.57 |  | 48.224 | -1.3562 | 48.88 | 47.635 | 0.042 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.11 |  | 31.5704 | -1.4585 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 737.61 |  | 738.4507 | -0.1138 | 742.515 | 738.54 | 0.0149 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.56 |  | 291.6078 | -0.0164 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.14 |  | 121.6502 | -1.2414 | 124.22 | 122.07 | 0.0333 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.185 |  | 82.4727 | -1.5614 | 84.415 | 80.64 | 4.6191 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.78 |  | 305.7507 | -0.6445 | 311.13 | 303.96 | 1.4813 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.16 |  | 413.3536 | 0.1951 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 646.56 |  | 651.2666 | -0.7227 | 656.38 | 642.37 | 0.1609 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1035.08 |  | 1017.1046 | 1.7673 | 1023.33 | 979.08 | 0.0696 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 479.145 |  | 476.9227 | 0.466 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.56 |  | 143.7984 | -0.1658 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.57 |  | 176.6038 | -0.5854 | 177.84 | 173.19 | 2.489 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.87 |  | 316.9802 | -1.6122 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 832.6 |  | 854.3627 | -2.5472 | 880.26 | 833 | 3.1372 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.58 |  | 407.7627 | -0.7805 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 112.25 |  | 114.3497 | -1.8362 | 118.01 | 108.505 | 0.1871 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 321.13 |  | 326.4439 | -1.6278 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1800.69 |  | 1801.479 | -0.0438 | 1806.11 | 1780.9 | 0.0822 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 560.22 |  | 563.8551 | -0.6447 | 566.18 | 548.47 | 0.1517 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.375 |  | 320.0325 | -0.2055 | 322.4 | 317.27 | 4.0579 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 216.99 |  | 215.5747 | 0.6565 | 217.88 | 212.99 | 0.0415 | watch_only | none |
| TER | semiconductor_test_packaging | 370.41 |  | 371.7927 | -0.3719 | 376.78 | 363.37 | 0.6533 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 289.88 |  | 293.6891 | -1.297 | 301.305 | 293.685 | 0.3036 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMKR | semiconductor_test_packaging | 64.88 |  | 65.1872 | -0.4712 | 67.455 | 65.81 | 4.0228 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.22 |  | 54.4717 | -0.462 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.44 |  | 134.8905 | -0.334 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.88 |  | 342.5228 | -0.4796 | 347.92 | 341.755 | 0.5897 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 505.53 |  | 507.1678 | -0.3229 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.85 |  | 295.6942 | 0.0527 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.8 |  | 30.0447 | -0.8146 | 31.13 | 29.12 | 1.5101 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.735 |  | 41.5341 | -1.924 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.05 |  | 24.0682 | -0.0756 | 24.46 | 23.265 | 0.0832 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1617.37 |  | 1641.0744 | -1.4444 | 1651.355 | 1560 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 557.88 |  | 563.887 | -1.0653 | 576.24 | 556.3 | 0.0627 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 916.48 |  | 923.1284 | -0.7202 | 933.5 | 908.955 | 1.0082 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.55 |  | 234.2909 | -0.3162 | 238.285 | 235.71 | 0.0385 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 607.105 |  | 604.6932 | 0.3988 | 614.15 | 605.39 | 1.0591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.3 |  | 279.5724 | 0.6179 | 283 | 276.24 | 2.5631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.46 |  | 173.0675 | -2.6622 | 177.88 | 168.18 | 3.9297 | below_vwap | below_vwap,spread_too_wide |
