# Intraday State

- Generated at: `2026-07-24T03:49:15+08:00`
- Market time ET: `2026-07-23T15:49:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 22, 'below_vwap': 30, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.295 |  | 692.5573 | -0.4711 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.72 |  | 550.4644 | -0.6802 | 557.38 | 545.965 | 0.0585 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.2 |  | 580.1645 | -0.6833 | 585.98 | 576.635 | 0.026 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 735.98 |  | 738.314 | -0.3161 | 742.515 | 738.54 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036.04 |  | 1019.2922 | 1.6431 | 1023.33 | 979.08 | 0.2828 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 479.8 |  | 477.1382 | 0.5579 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | ARM | ai_accelerator | 281.49 |  | 280.0956 | 0.4978 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | GEV | data_center_power_cooling | 1036.04 |  | 1019.2922 | 1.6431 | 1023.33 | 979.08 | 0.2828 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 546.72 |  | 550.4644 | -0.6802 | 557.38 | 545.965 | 0.0585 | below_vwap | below_vwap |
| 5 | MU | memory_hbm_storage | 980.18 |  | 990.4182 | -1.0337 | 999.04 | 964.86 | 0.1459 | below_vwap | below_vwap |
| 6 | ASML | semiconductor_equipment | 1794.83 |  | 1801.1127 | -0.3488 | 1806.11 | 1780.9 | 0.0513 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 291.29 |  | 291.6081 | -0.1091 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 8 | SMCI | ai_server_oem | 31.06 |  | 31.5544 | -1.5669 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | IREN | high_beta_ai_infrastructure | 40.555 |  | 41.4783 | -2.226 | 43.21 | 40.51 | 0.0493 | below_vwap | below_vwap |
| 11 | AAPL | mega_cap_platform | 320.87 |  | 320.9105 | -0.0126 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| 12 | WDC | memory_hbm_storage | 558.575 |  | 563.5875 | -0.8894 | 576.24 | 556.3 | 0.324 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 143.65 |  | 143.773 | -0.0856 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LRCX | semiconductor_equipment | 318.83 |  | 319.9586 | -0.3527 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | CIEN | ai_networking_optical | 402.93 |  | 407.4003 | -1.0973 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | TER | semiconductor_test_packaging | 369.24 |  | 371.6453 | -0.6472 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | COHU | semiconductor_test_packaging | 54.28 |  | 54.4184 | -0.2544 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AAOI | ai_networking_optical | 111.745 |  | 114.2552 | -2.197 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | TSM | foundry | 413.58 |  | 416.0923 | -0.6038 | 420.72 | 412.69 | 0.3651 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 559.76 |  | 563.3233 | -0.6326 | 566.18 | 548.47 | 3.0245 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036.04 |  | 1019.2922 | 1.6431 | 1023.33 | 979.08 | 0.2828 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 413.58 |  | 416.0923 | -0.6038 | 420.72 | 412.69 | 0.3651 | below_vwap | below_vwap,spread_too_wide |
| 3 | SOXX | semiconductor_index | 546.72 |  | 550.4644 | -0.6802 | 557.38 | 545.965 | 0.0585 | below_vwap | below_vwap |
| 4 | MU | memory_hbm_storage | 980.18 |  | 990.4182 | -1.0337 | 999.04 | 964.86 | 0.1459 | below_vwap | below_vwap |
| 5 | ASML | semiconductor_equipment | 1794.83 |  | 1801.1127 | -0.3488 | 1806.11 | 1780.9 | 0.0513 | below_vwap | below_vwap |
| 6 | AMAT | semiconductor_equipment | 559.76 |  | 563.3233 | -0.6326 | 566.18 | 548.47 | 3.0245 | below_vwap | below_vwap,spread_too_wide |
| 7 | ANET | ai_networking_optical | 175.92 |  | 176.5205 | -0.3402 | 177.84 | 173.19 | 2.3363 | below_vwap | below_vwap,spread_too_wide |
| 8 | JCI | data_center_power_cooling | 143.65 |  | 143.773 | -0.0856 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | PWR | data_center_power_cooling | 650.13 |  | 650.7209 | -0.0908 | 656.38 | 642.37 | 1.3213 | below_vwap | below_vwap,spread_too_wide |
| 10 | KLAC | semiconductor_equipment | 215.57 |  | 215.8444 | -0.1271 | 217.88 | 212.99 | 0.9231 | below_vwap | below_vwap,spread_too_wide |
| 11 | ETN | data_center_power_cooling | 413.32 |  | 413.3962 | -0.0184 | 415.53 | 406.545 | 0.5952 | below_vwap | below_vwap,spread_too_wide |
| 12 | IWM | market_regime | 291.29 |  | 291.6081 | -0.1091 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 318.83 |  | 319.9586 | -0.3527 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | WDC | memory_hbm_storage | 558.575 |  | 563.5875 | -0.8894 | 576.24 | 556.3 | 0.324 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | MKSI | semiconductor_materials | 341.99 |  | 342.4139 | -0.1238 | 347.92 | 341.755 | 4.851 | below_vwap | below_vwap,spread_too_wide |
| 17 | LIN | industrial_gases | 505.205 |  | 507.0133 | -0.3567 | 510.71 | 502.72 | 5.0158 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 311.27 |  | 316.3878 | -1.6176 | 320.13 | 307.04 | 4.411 | below_vwap | below_vwap,spread_too_wide |
| 19 | CIEN | ai_networking_optical | 402.93 |  | 407.4003 | -1.0973 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | TER | semiconductor_test_packaging | 369.24 |  | 371.6453 | -0.6472 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.295 |  | 692.5573 | -0.4711 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.47 |  | 66.4566 | -1.4846 | 68.245 | 66.7 | 0.0153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.29 |  | 208.4307 | -0.5473 | 210.85 | 208.49 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.735 |  | 382.3093 | -0.6734 | 391.71 | 387.245 | 0.0237 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.87 |  | 320.9105 | -0.0126 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 318.325 |  | 319.3938 | -0.3346 | 324.42 | 320.24 | 0.0157 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.28 |  | 539.8134 | -0.2841 | 556.12 | 542.33 | 1.7649 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 413.58 |  | 416.0923 | -0.6038 | 420.72 | 412.69 | 0.3651 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.72 |  | 550.4644 | -0.6802 | 557.38 | 545.965 | 0.0585 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.2 |  | 580.1645 | -0.6833 | 585.98 | 576.635 | 0.026 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.73 |  | 391.82 | -0.5334 | 397.34 | 390.54 | 1.2829 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 980.18 |  | 990.4182 | -1.0337 | 999.04 | 964.86 | 0.1459 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.45 |  | 209.0654 | -1.251 | 213.785 | 207.665 | 0.7411 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 437.4 |  | 442.843 | -1.2291 | 450.07 | 438.55 | 1.7513 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.555 |  | 48.1737 | -1.2843 | 48.88 | 47.635 | 0.0421 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.06 |  | 31.5544 | -1.5669 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 735.98 |  | 738.314 | -0.3161 | 742.515 | 738.54 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.29 |  | 291.6081 | -0.1091 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.71 |  | 121.5382 | -1.5042 | 124.22 | 122.07 | 0.2673 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.98 |  | 82.3456 | -1.6584 | 84.415 | 80.64 | 3.0625 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.955 |  | 305.5417 | -0.8466 | 311.13 | 303.96 | 0.845 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.32 |  | 413.3962 | -0.0184 | 415.53 | 406.545 | 0.5952 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 650.13 |  | 650.7209 | -0.0908 | 656.38 | 642.37 | 1.3213 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1036.04 |  | 1019.2922 | 1.6431 | 1023.33 | 979.08 | 0.2828 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 479.8 |  | 477.1382 | 0.5579 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.65 |  | 143.773 | -0.0856 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.92 |  | 176.5205 | -0.3402 | 177.84 | 173.19 | 2.3363 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.27 |  | 316.3878 | -1.6176 | 320.13 | 307.04 | 4.411 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 830.99 |  | 853.0518 | -2.5862 | 880.26 | 833 | 3.7305 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.93 |  | 407.4003 | -1.0973 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 111.745 |  | 114.2552 | -2.197 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.79 |  | 325.7343 | -1.8249 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.83 |  | 1801.1127 | -0.3488 | 1806.11 | 1780.9 | 0.0513 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.76 |  | 563.3233 | -0.6326 | 566.18 | 548.47 | 3.0245 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.83 |  | 319.9586 | -0.3527 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.57 |  | 215.8444 | -0.1271 | 217.88 | 212.99 | 0.9231 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 369.24 |  | 371.6453 | -0.6472 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.69 |  | 293.5311 | -1.3086 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.99 |  | 65.1605 | -0.2617 | 67.455 | 65.81 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 54.28 |  | 54.4184 | -0.2544 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.27 |  | 134.9339 | -0.492 | 137.81 | 135.66 | 0.4245 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 341.99 |  | 342.4139 | -0.1238 | 347.92 | 341.755 | 4.851 | below_vwap | below_vwap,spread_too_wide |
| LIN | industrial_gases | 505.205 |  | 507.0133 | -0.3567 | 510.71 | 502.72 | 5.0158 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.99 |  | 295.6218 | -0.2137 | 299.26 | 295.795 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 29.79 |  | 30.0356 | -0.8176 | 31.13 | 29.12 | 0.0336 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.555 |  | 41.4783 | -2.226 | 43.21 | 40.51 | 0.0493 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.06 |  | 24.074 | -0.0581 | 24.46 | 23.265 | 0.0416 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1608.675 |  | 1638.8931 | -1.8438 | 1651.355 | 1560 | 0.4345 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 558.575 |  | 563.5875 | -0.8894 | 576.24 | 556.3 | 0.324 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 913.14 |  | 922.0295 | -0.9641 | 933.5 | 908.955 | 4.4363 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 232.98 |  | 234.2364 | -0.5364 | 238.285 | 235.71 | 0.0215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 603.315 |  | 604.775 | -0.2414 | 614.15 | 605.39 | 0.2851 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 281.49 |  | 280.0956 | 0.4978 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 169.03 |  | 172.8197 | -2.1929 | 177.88 | 168.18 | 0.562 | below_vwap | below_vwap,spread_too_wide |
