# Intraday State

- Generated at: `2026-07-24T03:18:13+08:00`
- Market time ET: `2026-07-23T15:18:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 22, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 4, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.31 |  | 692.7894 | -0.3579 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.24 |  | 550.6505 | -0.801 | 557.38 | 545.965 | 0.0439 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.76 |  | 580.4795 | -0.6408 | 585.98 | 576.635 | 0.0364 | below_vwap | below_vwap |
| SPY | market_regime | 737.04 |  | 738.4717 | -0.1939 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 215.985 |  | 215.4953 | 0.2272 | 217.88 | 212.99 | 0.0509 | watch_only | none |
| 2 | TT | data_center_power_cooling | 478.24 |  | 476.8943 | 0.2822 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | ETN | data_center_power_cooling | 413.91 |  | 413.3353 | 0.139 | 415.53 | 406.545 | 0.4784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | META | cloud_ai_capex | 607.025 |  | 604.6495 | 0.3929 | 614.15 | 605.39 | 0.9851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 295.745 |  | 295.6912 | 0.0182 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 6 | SMH | semiconductor_index | 576.76 |  | 580.4795 | -0.6408 | 585.98 | 576.635 | 0.0364 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 546.24 |  | 550.6505 | -0.801 | 557.38 | 545.965 | 0.0439 | below_vwap | below_vwap |
| 8 | MU | memory_hbm_storage | 983.705 |  | 991.0497 | -0.7411 | 999.04 | 964.86 | 0.0681 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1794.22 |  | 1801.5804 | -0.4086 | 1806.11 | 1780.9 | 0.0608 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 291.425 |  | 291.6093 | -0.0632 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 11 | SMCI | ai_server_oem | 30.97 |  | 31.5763 | -1.9201 | 31.52 | 30.23 | 0.0646 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | IREN | high_beta_ai_infrastructure | 40.53 |  | 41.5442 | -2.4413 | 43.21 | 40.51 | 0.0493 | below_vwap | below_vwap |
| 14 | WDC | memory_hbm_storage | 557.735 |  | 564.0431 | -1.1184 | 576.24 | 556.3 | 0.2492 | below_vwap | below_vwap |
| 15 | JCI | data_center_power_cooling | 143.38 |  | 143.8055 | -0.2959 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 648.16 |  | 651.5781 | -0.5246 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 279.34 |  | 279.5593 | -0.0785 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 505.53 |  | 507.1869 | -0.3267 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | TER | semiconductor_test_packaging | 369.03 |  | 371.8538 | -0.7594 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CRWV | gpu_cloud_ai_factory | 80.72 |  | 82.5375 | -2.202 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1034.54 |  | 1016.5468 | 1.77 | 1023.33 | 979.08 | 0.5916 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | KLAC | semiconductor_equipment | 215.985 |  | 215.4953 | 0.2272 | 217.88 | 212.99 | 0.0509 | watch_only | none |
| 3 | TSM | foundry | 414.86 |  | 416.3385 | -0.3551 | 420.72 | 412.69 | 0.887 | below_vwap | below_vwap,spread_too_wide |
| 4 | SMH | semiconductor_index | 576.76 |  | 580.4795 | -0.6408 | 585.98 | 576.635 | 0.0364 | below_vwap | below_vwap |
| 5 | SOXX | semiconductor_index | 546.24 |  | 550.6505 | -0.801 | 557.38 | 545.965 | 0.0439 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 983.705 |  | 991.0497 | -0.7411 | 999.04 | 964.86 | 0.0681 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1794.22 |  | 1801.5804 | -0.4086 | 1806.11 | 1780.9 | 0.0608 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 558.16 |  | 564.0237 | -1.0396 | 566.18 | 548.47 | 0.5876 | below_vwap | below_vwap,spread_too_wide |
| 9 | ANET | ai_networking_optical | 175.3 |  | 176.631 | -0.7535 | 177.84 | 173.19 | 2.7895 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 143.38 |  | 143.8055 | -0.2959 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 648.16 |  | 651.5781 | -0.5246 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IWM | market_regime | 291.425 |  | 291.6093 | -0.0632 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 317.95 |  | 320.2134 | -0.7068 | 322.4 | 317.27 | 4.6611 | below_vwap | below_vwap,spread_too_wide |
| 14 | ARM | ai_accelerator | 279.34 |  | 279.5593 | -0.0785 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 557.735 |  | 564.0431 | -1.1184 | 576.24 | 556.3 | 0.2492 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LIN | industrial_gases | 505.53 |  | 507.1869 | -0.3267 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | COHR | ai_networking_optical | 311.32 |  | 317.3532 | -1.9011 | 320.13 | 307.04 | 4.4424 | below_vwap | below_vwap,spread_too_wide |
| 19 | CIEN | ai_networking_optical | 403.77 |  | 407.8394 | -0.9978 | 408.58 | 397.9 | 3.9032 | below_vwap | below_vwap,spread_too_wide |
| 20 | TER | semiconductor_test_packaging | 369.03 |  | 371.8538 | -0.7594 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.31 |  | 692.7894 | -0.3579 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.76 |  | 66.4956 | -1.1062 | 68.245 | 66.7 | 0.0304 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.67 |  | 208.5119 | -0.4038 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.88 |  | 382.4592 | -0.4129 | 391.71 | 387.245 | 0.0053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.765 |  | 320.9417 | -0.0551 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.065 |  | 319.5083 | -0.4517 | 324.42 | 320.24 | 0.0849 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.97 |  | 539.9166 | -0.731 | 556.12 | 542.33 | 2.4255 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.86 |  | 416.3385 | -0.3551 | 420.72 | 412.69 | 0.887 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.24 |  | 550.6505 | -0.801 | 557.38 | 545.965 | 0.0439 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.76 |  | 580.4795 | -0.6408 | 585.98 | 576.635 | 0.0364 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 389.91 |  | 391.9718 | -0.526 | 397.34 | 390.54 | 1.3644 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 983.705 |  | 991.0497 | -0.7411 | 999.04 | 964.86 | 0.0681 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.525 |  | 209.261 | -1.3075 | 213.785 | 207.665 | 0.6488 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 435.09 |  | 443.2241 | -1.8352 | 450.07 | 438.55 | 0.501 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.56 |  | 48.2392 | -1.408 | 48.88 | 47.635 | 0.0421 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.97 |  | 31.5763 | -1.9201 | 31.52 | 30.23 | 0.0646 | below_vwap | below_vwap |
| SPY | market_regime | 737.04 |  | 738.4717 | -0.1939 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.425 |  | 291.6093 | -0.0632 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.01 |  | 121.6605 | -1.3566 | 124.22 | 122.07 | 0.2166 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.72 |  | 82.5375 | -2.202 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.29 |  | 305.7934 | -1.1457 | 311.13 | 303.96 | 1.4886 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.91 |  | 413.3353 | 0.139 | 415.53 | 406.545 | 0.4784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 648.16 |  | 651.5781 | -0.5246 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1034.54 |  | 1016.5468 | 1.77 | 1023.33 | 979.08 | 0.5916 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.24 |  | 476.8943 | 0.2822 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.38 |  | 143.8055 | -0.2959 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.3 |  | 176.631 | -0.7535 | 177.84 | 173.19 | 2.7895 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.32 |  | 317.3532 | -1.9011 | 320.13 | 307.04 | 4.4424 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 827.88 |  | 854.8679 | -3.157 | 880.26 | 833 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 403.77 |  | 407.8394 | -0.9978 | 408.58 | 397.9 | 3.9032 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.51 |  | 114.3777 | -2.5073 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.71 |  | 326.49 | -1.7703 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.22 |  | 1801.5804 | -0.4086 | 1806.11 | 1780.9 | 0.0608 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.16 |  | 564.0237 | -1.0396 | 566.18 | 548.47 | 0.5876 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.95 |  | 320.2134 | -0.7068 | 322.4 | 317.27 | 4.6611 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 215.985 |  | 215.4953 | 0.2272 | 217.88 | 212.99 | 0.0509 | watch_only | none |
| TER | semiconductor_test_packaging | 369.03 |  | 371.8538 | -0.7594 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.64 |  | 293.7213 | -1.3895 | 301.305 | 293.685 | 4.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.88 |  | 65.1872 | -0.4712 | 67.455 | 65.81 | 0.2928 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.33 |  | 134.9469 | -0.4571 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.45 |  | 342.5917 | -0.6252 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 505.53 |  | 507.1869 | -0.3267 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.745 |  | 295.6912 | 0.0182 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.72 |  | 30.0478 | -1.0911 | 31.13 | 29.12 | 2.3553 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.53 |  | 41.5442 | -2.4413 | 43.21 | 40.51 | 0.0493 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.99 |  | 24.0693 | -0.3294 | 24.46 | 23.265 | 0.0834 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1617.62 |  | 1641.7159 | -1.4677 | 1651.355 | 1560 | 3.9472 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 557.735 |  | 564.0431 | -1.1184 | 576.24 | 556.3 | 0.2492 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 915.79 |  | 923.547 | -0.8399 | 933.5 | 908.955 | 1.4654 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.76 |  | 234.298 | -0.2296 | 238.285 | 235.71 | 0.0299 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 607.025 |  | 604.6495 | 0.3929 | 614.15 | 605.39 | 0.9851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.34 |  | 279.5593 | -0.0785 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 168.25 |  | 173.1399 | -2.8242 | 177.88 | 168.18 | 4.9866 | below_vwap | below_vwap,spread_too_wide |
