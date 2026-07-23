# Intraday State

- Generated at: `2026-07-24T02:54:57+08:00`
- Market time ET: `2026-07-23T14:54:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 21, 'below_vwap': 26, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 3, 'manual_confirm_candidate': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.83 |  | 692.9174 | -0.3012 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.735 |  | 550.7634 | -0.7314 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.2 |  | 580.7698 | -0.7869 | 585.98 | 576.635 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.17 |  | 738.5636 | -0.1887 | 742.515 | 738.54 | 0.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1038 |  | 1015.2893 | 2.2369 | 1023.33 | 979.08 | 0.1426 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 607.6 |  | 604.5169 | 0.51 | 614.15 | 605.39 | 0.0691 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.4 |  | 476.8449 | 0.1164 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | ETN | data_center_power_cooling | 413.545 |  | 413.3237 | 0.0535 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | CORZ | high_beta_ai_infrastructure | 24.105 |  | 24.0728 | 0.1339 | 24.46 | 23.265 | 0.083 | watch_only | none |
| 5 | GEV | data_center_power_cooling | 1038 |  | 1015.2893 | 2.2369 | 1023.33 | 979.08 | 0.1426 | buy_precheck_manual_confirm | none |
| 6 | SNDK | memory_hbm_storage | 1646.24 |  | 1643.5903 | 0.1612 | 1651.355 | 1560 | 4.4951 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SOXX | semiconductor_index | 546.735 |  | 550.7634 | -0.7314 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1791.84 |  | 1802.2737 | -0.5789 | 1806.11 | 1780.9 | 0.0575 | below_vwap | below_vwap |
| 9 | KLAC | semiconductor_equipment | 214.96 |  | 215.5058 | -0.2533 | 217.88 | 212.99 | 0.0605 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 291.27 |  | 291.6311 | -0.1238 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 11 | SMCI | ai_server_oem | 31.115 |  | 31.5991 | -1.5319 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | IREN | high_beta_ai_infrastructure | 40.76 |  | 41.6233 | -2.0741 | 43.21 | 40.51 | 0.0245 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 557.775 |  | 564.7552 | -1.236 | 566.18 | 548.47 | 0.3227 | below_vwap | below_vwap |
| 15 | WDC | memory_hbm_storage | 563.295 |  | 564.247 | -0.1687 | 576.24 | 556.3 | 0.19 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.6 |  | 143.8918 | -0.2028 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 649.73 |  | 651.6954 | -0.3016 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 279.62 |  | 279.6673 | -0.0169 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHR | ai_networking_optical | 312.74 |  | 317.631 | -1.5398 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LITE | ai_networking_optical | 835 |  | 856.3747 | -2.4959 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1038 |  | 1015.2893 | 2.2369 | 1023.33 | 979.08 | 0.1426 | buy_precheck_manual_confirm | none |
| 2 | META | cloud_ai_capex | 607.6 |  | 604.5169 | 0.51 | 614.15 | 605.39 | 0.0691 | watch_only | none |
| 3 | CORZ | high_beta_ai_infrastructure | 24.105 |  | 24.0728 | 0.1339 | 24.46 | 23.265 | 0.083 | watch_only | none |
| 4 | TSM | foundry | 414.73 |  | 416.4648 | -0.4166 | 420.72 | 412.69 | 0.9645 | below_vwap | below_vwap,spread_too_wide |
| 5 | SOXX | semiconductor_index | 546.735 |  | 550.7634 | -0.7314 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 987.75 |  | 991.6724 | -0.3955 | 999.04 | 964.86 | 1.2169 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1791.84 |  | 1802.2737 | -0.5789 | 1806.11 | 1780.9 | 0.0575 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 557.775 |  | 564.7552 | -1.236 | 566.18 | 548.47 | 0.3227 | below_vwap | below_vwap |
| 9 | ANET | ai_networking_optical | 176.04 |  | 176.6697 | -0.3564 | 177.84 | 173.19 | 0.96 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 143.6 |  | 143.8918 | -0.2028 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 649.73 |  | 651.6954 | -0.3016 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 214.96 |  | 215.5058 | -0.2533 | 217.88 | 212.99 | 0.0605 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 291.27 |  | 291.6311 | -0.1238 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 14 | LRCX | semiconductor_equipment | 318.32 |  | 320.4371 | -0.6607 | 322.4 | 317.27 | 4.6526 | below_vwap | below_vwap,spread_too_wide |
| 15 | ARM | ai_accelerator | 279.62 |  | 279.6673 | -0.0169 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 563.295 |  | 564.247 | -0.1687 | 576.24 | 556.3 | 0.19 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 505.82 |  | 507.2359 | -0.2791 | 510.71 | 502.72 | 4.9029 | below_vwap | below_vwap,spread_too_wide |
| 19 | COHR | ai_networking_optical | 312.74 |  | 317.631 | -1.5398 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CIEN | ai_networking_optical | 406.41 |  | 408.1193 | -0.4188 | 408.58 | 397.9 | 0.5807 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.83 |  | 692.9174 | -0.3012 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.93 |  | 66.5273 | -0.8978 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.74 |  | 208.5586 | -0.3925 | 210.85 | 208.49 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 382.09 |  | 382.5355 | -0.1165 | 391.71 | 387.245 | 0.547 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.17 |  | 320.9613 | -0.2465 | 323.25 | 320.82 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.345 |  | 319.5412 | -0.0614 | 324.42 | 320.24 | 0.191 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.39 |  | 540.2027 | -0.8909 | 556.12 | 542.33 | 2.4281 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.73 |  | 416.4648 | -0.4166 | 420.72 | 412.69 | 0.9645 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.735 |  | 550.7634 | -0.7314 | 557.38 | 545.965 | 0.0549 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.2 |  | 580.7698 | -0.7869 | 585.98 | 576.635 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 390.1 |  | 392.1337 | -0.5186 | 397.34 | 390.54 | 1.3458 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 987.75 |  | 991.6724 | -0.3955 | 999.04 | 964.86 | 1.2169 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.37 |  | 209.386 | -1.4404 | 213.785 | 207.665 | 0.1018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.7 |  | 443.4217 | -1.2903 | 450.07 | 438.55 | 1.7501 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.625 |  | 48.2821 | -1.361 | 48.88 | 47.635 | 0.042 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.115 |  | 31.5991 | -1.5319 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 737.17 |  | 738.5636 | -0.1887 | 742.515 | 738.54 | 0.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.27 |  | 291.6311 | -0.1238 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.08 |  | 121.7084 | -1.3379 | 124.22 | 122.07 | 0.2665 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.66 |  | 82.7044 | -1.2628 | 84.415 | 80.64 | 3.6125 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.67 |  | 306.0551 | -1.106 | 311.13 | 303.96 | 1.3051 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.545 |  | 413.3237 | 0.0535 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 649.73 |  | 651.6954 | -0.3016 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1038 |  | 1015.2893 | 2.2369 | 1023.33 | 979.08 | 0.1426 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 477.4 |  | 476.8449 | 0.1164 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.6 |  | 143.8918 | -0.2028 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.04 |  | 176.6697 | -0.3564 | 177.84 | 173.19 | 0.96 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.74 |  | 317.631 | -1.5398 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835 |  | 856.3747 | -2.4959 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 406.41 |  | 408.1193 | -0.4188 | 408.58 | 397.9 | 0.5807 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.525 |  | 114.4792 | -1.707 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 321.51 |  | 327.342 | -1.7816 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1791.84 |  | 1802.2737 | -0.5789 | 1806.11 | 1780.9 | 0.0575 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 557.775 |  | 564.7552 | -1.236 | 566.18 | 548.47 | 0.3227 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 318.32 |  | 320.4371 | -0.6607 | 322.4 | 317.27 | 4.6526 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 214.96 |  | 215.5058 | -0.2533 | 217.88 | 212.99 | 0.0605 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.81 |  | 372.0644 | -0.6059 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.745 |  | 293.9687 | -1.4368 | 301.305 | 293.685 | 0.3175 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMKR | semiconductor_test_packaging | 64.98 |  | 65.2103 | -0.3531 | 67.455 | 65.81 | 0.1231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.455 |  | 135.0442 | -0.4363 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.43 |  | 342.7964 | -0.3986 | 347.92 | 341.755 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.82 |  | 507.2359 | -0.2791 | 510.71 | 502.72 | 4.9029 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.46 |  | 295.6843 | -0.0759 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.055 |  | 30.0552 | -0.0008 | 31.13 | 29.12 | 0.0333 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.76 |  | 41.6233 | -2.0741 | 43.21 | 40.51 | 0.0245 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.105 |  | 24.0728 | 0.1339 | 24.46 | 23.265 | 0.083 | watch_only | none |
| SNDK | memory_hbm_storage | 1646.24 |  | 1643.5903 | 0.1612 | 1651.355 | 1560 | 4.4951 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 563.295 |  | 564.247 | -0.1687 | 576.24 | 556.3 | 0.19 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 922.26 |  | 924.1079 | -0.2 | 933.5 | 908.955 | 0.8674 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.84 |  | 234.3204 | -0.205 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 607.6 |  | 604.5169 | 0.51 | 614.15 | 605.39 | 0.0691 | watch_only | none |
| ARM | ai_accelerator | 279.62 |  | 279.6673 | -0.0169 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 170.24 |  | 173.4467 | -1.8488 | 177.88 | 168.18 | 3.5244 | below_vwap | below_vwap,spread_too_wide |
