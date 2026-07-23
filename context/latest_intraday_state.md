# Intraday State

- Generated at: `2026-07-24T02:31:33+08:00`
- Market time ET: `2026-07-23T14:31:34-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'watch_only': 1, 'below_vwap': 30, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.99 |  | 692.9739 | -0.2863 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.94 |  | 550.8558 | -0.7109 | 557.38 | 545.965 | 0.0603 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.23 |  | 580.8833 | -0.6289 | 585.98 | 576.635 | 0.0537 | below_vwap | below_vwap |
| SPY | market_regime | 737.49 |  | 738.6353 | -0.1551 | 742.515 | 738.54 | 0.0014 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 208.62 |  | 208.5862 | 0.0162 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.89 |  | 476.8092 | 0.2267 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MU | memory_hbm_storage | 991.995 |  | 991.7001 | 0.0297 | 999.04 | 964.86 | 0.6048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | META | cloud_ai_capex | 605.955 |  | 604.4508 | 0.2488 | 614.15 | 605.39 | 0.8482 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SMH | semiconductor_index | 577.23 |  | 580.8833 | -0.6289 | 585.98 | 576.635 | 0.0537 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 546.94 |  | 550.8558 | -0.7109 | 557.38 | 545.965 | 0.0603 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1792.36 |  | 1802.8878 | -0.5839 | 1806.11 | 1780.9 | 0.0759 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 214.6 |  | 215.5369 | -0.4347 | 217.88 | 212.99 | 0.0419 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 291.195 |  | 291.6431 | -0.1536 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 10 | LRCX | semiconductor_equipment | 318.15 |  | 320.5914 | -0.7615 | 322.4 | 317.27 | 0.066 | below_vwap | below_vwap |
| 11 | CRWV | gpu_cloud_ai_factory | 81.63 |  | 82.7537 | -1.3579 | 84.415 | 80.64 | 0.098 | below_vwap | below_vwap |
| 12 | SMCI | ai_server_oem | 30.905 |  | 31.6262 | -2.2803 | 31.52 | 30.23 | 0.0647 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 40.71 |  | 41.6544 | -2.2672 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1661.24 |  | 1643.1394 | 1.1016 | 1651.355 | 1560 | 1.6957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | PWR | data_center_power_cooling | 650.135 |  | 651.765 | -0.2501 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ETN | data_center_power_cooling | 413.06 |  | 413.34 | -0.0677 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 279.46 |  | 279.6599 | -0.0715 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | MKSI | semiconductor_materials | 341.89 |  | 342.8233 | -0.2722 | 347.92 | 341.755 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505.3 |  | 507.3081 | -0.3958 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036.92 |  | 1014.7459 | 2.1852 | 1023.33 | 979.08 | 0.515 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1661.24 |  | 1643.1394 | 1.1016 | 1651.355 | 1560 | 1.6957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | NVDA | ai_accelerator | 208.62 |  | 208.5862 | 0.0162 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 4 | TSM | foundry | 414.97 |  | 416.5494 | -0.3792 | 420.72 | 412.69 | 0.9639 | below_vwap | below_vwap,spread_too_wide |
| 5 | SMH | semiconductor_index | 577.23 |  | 580.8833 | -0.6289 | 585.98 | 576.635 | 0.0537 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 546.94 |  | 550.8558 | -0.7109 | 557.38 | 545.965 | 0.0603 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1792.36 |  | 1802.8878 | -0.5839 | 1806.11 | 1780.9 | 0.0759 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 558.055 |  | 565.1528 | -1.2559 | 566.18 | 548.47 | 0.6236 | below_vwap | below_vwap,spread_too_wide |
| 9 | ANET | ai_networking_optical | 176.02 |  | 176.7134 | -0.3924 | 177.84 | 173.19 | 3.1246 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 143.69 |  | 143.9143 | -0.1558 | 145.035 | 141.815 | 2.5054 | below_vwap | below_vwap,spread_too_wide |
| 11 | PWR | data_center_power_cooling | 650.135 |  | 651.765 | -0.2501 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 214.6 |  | 215.5369 | -0.4347 | 217.88 | 212.99 | 0.0419 | below_vwap | below_vwap |
| 13 | ETN | data_center_power_cooling | 413.06 |  | 413.34 | -0.0677 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IWM | market_regime | 291.195 |  | 291.6431 | -0.1536 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 318.15 |  | 320.5914 | -0.7615 | 322.4 | 317.27 | 0.066 | below_vwap | below_vwap |
| 16 | ARM | ai_accelerator | 279.46 |  | 279.6599 | -0.0715 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 562.47 |  | 564.264 | -0.3179 | 576.24 | 556.3 | 1.6374 | below_vwap | below_vwap,spread_too_wide |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | MKSI | semiconductor_materials | 341.89 |  | 342.8233 | -0.2722 | 347.92 | 341.755 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505.3 |  | 507.3081 | -0.3958 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.99 |  | 692.9739 | -0.2863 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.05 |  | 66.5411 | -0.7381 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.62 |  | 208.5862 | 0.0162 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| MSFT | cloud_ai_capex | 381.78 |  | 382.5699 | -0.2065 | 391.71 | 387.245 | 0.482 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.35 |  | 321.0196 | -0.2086 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.53 |  | 319.5616 | -0.0099 | 324.42 | 320.24 | 0.0376 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.92 |  | 540.3531 | -0.8204 | 556.12 | 542.33 | 4.0379 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.97 |  | 416.5494 | -0.3792 | 420.72 | 412.69 | 0.9639 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.94 |  | 550.8558 | -0.7109 | 557.38 | 545.965 | 0.0603 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.23 |  | 580.8833 | -0.6289 | 585.98 | 576.635 | 0.0537 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.29 |  | 392.217 | -0.4913 | 397.34 | 390.54 | 0.4279 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 991.995 |  | 991.7001 | 0.0297 | 999.04 | 964.86 | 0.6048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 206.57 |  | 209.4612 | -1.3803 | 213.785 | 207.665 | 4.0471 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 437.19 |  | 443.6648 | -1.4594 | 450.07 | 438.55 | 1.7452 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.61 |  | 48.3058 | -1.4404 | 48.88 | 47.635 | 0.105 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.905 |  | 31.6262 | -2.2803 | 31.52 | 30.23 | 0.0647 | below_vwap | below_vwap |
| SPY | market_regime | 737.49 |  | 738.6353 | -0.1551 | 742.515 | 738.54 | 0.0014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.195 |  | 291.6431 | -0.1536 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.66 |  | 121.7756 | -1.7373 | 124.22 | 122.07 | 0.3092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.63 |  | 82.7537 | -1.3579 | 84.415 | 80.64 | 0.098 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 302.67 |  | 306.1117 | -1.1243 | 311.13 | 303.96 | 1.3051 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.06 |  | 413.34 | -0.0677 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 650.135 |  | 651.765 | -0.2501 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1036.92 |  | 1014.7459 | 2.1852 | 1023.33 | 979.08 | 0.515 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.89 |  | 476.8092 | 0.2267 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.69 |  | 143.9143 | -0.1558 | 145.035 | 141.815 | 2.5054 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 176.02 |  | 176.7134 | -0.3924 | 177.84 | 173.19 | 3.1246 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.29 |  | 317.7649 | -1.4082 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.115 |  | 856.7662 | -2.5271 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.84 |  | 408.2328 | -0.0962 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 112.19 |  | 114.5397 | -2.0515 | 118.01 | 108.505 | 0.3298 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 323.5 |  | 327.6091 | -1.2543 | 341.68 | 327.43 | 4.2751 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1792.36 |  | 1802.8878 | -0.5839 | 1806.11 | 1780.9 | 0.0759 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.055 |  | 565.1528 | -1.2559 | 566.18 | 548.47 | 0.6236 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.15 |  | 320.5914 | -0.7615 | 322.4 | 317.27 | 0.066 | below_vwap | below_vwap |
| KLAC | semiconductor_equipment | 214.6 |  | 215.5369 | -0.4347 | 217.88 | 212.99 | 0.0419 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.6 |  | 372.1403 | -0.6826 | 376.78 | 363.37 | 0.441 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 289.39 |  | 294.0522 | -1.5855 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.89 |  | 65.2161 | -0.5001 | 67.455 | 65.81 | 4.3304 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.18 |  | 54.5255 | -0.6337 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.195 |  | 135.1021 | -0.6714 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.89 |  | 342.8233 | -0.2722 | 347.92 | 341.755 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 505.3 |  | 507.3081 | -0.3958 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.13 |  | 295.7094 | -0.196 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.99 |  | 30.0556 | -0.2182 | 31.13 | 29.12 | 0.3334 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.71 |  | 41.6544 | -2.2672 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.07 |  | 24.0703 | -0.0014 | 24.46 | 23.265 | 0.0415 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1661.24 |  | 1643.1394 | 1.1016 | 1651.355 | 1560 | 1.6957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 562.47 |  | 564.264 | -0.3179 | 576.24 | 556.3 | 1.6374 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 922.355 |  | 924.1523 | -0.1945 | 933.5 | 908.955 | 2.679 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 234.02 |  | 234.3398 | -0.1365 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.955 |  | 604.4508 | 0.2488 | 614.15 | 605.39 | 0.8482 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.46 |  | 279.6599 | -0.0715 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.4 |  | 173.5329 | -0.6528 | 177.88 | 168.18 | 1.4501 | below_vwap | below_vwap,spread_too_wide |
