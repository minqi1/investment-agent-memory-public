# Intraday State

- Generated at: `2026-07-24T02:43:16+08:00`
- Market time ET: `2026-07-23T14:43:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 21, 'below_vwap': 29, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.6 |  | 692.9371 | -0.3373 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.09 |  | 550.805 | -0.6745 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.74 |  | 580.8271 | -0.7037 | 585.98 | 576.635 | 0.052 | below_vwap | below_vwap |
| SPY | market_regime | 736.82 |  | 738.5946 | -0.2403 | 742.515 | 738.54 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 477.17 |  | 476.8283 | 0.0717 | 480 | 472.33 | 0.1467 | watch_only | none |
| 2 | ARM | ai_accelerator | 279.75 |  | 279.6699 | 0.0286 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.0709 | 0.2041 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 4 | SMH | semiconductor_index | 576.74 |  | 580.8271 | -0.7037 | 585.98 | 576.635 | 0.052 | below_vwap | below_vwap |
| 5 | SOXX | semiconductor_index | 547.09 |  | 550.805 | -0.6745 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| 6 | ASML | semiconductor_equipment | 1794.65 |  | 1802.5871 | -0.4403 | 1806.11 | 1780.9 | 0.0557 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 291.18 |  | 291.6362 | -0.1564 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 8 | LIN | industrial_gases | 505.27 |  | 507.2612 | -0.3925 | 510.71 | 502.72 | 0.1148 | below_vwap | below_vwap |
| 9 | HPE | ai_server_oem | 47.68 |  | 48.2968 | -1.277 | 48.88 | 47.635 | 0.0839 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 31.12 |  | 31.6068 | -1.5402 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 40.7 |  | 41.6406 | -2.2588 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| 13 | SNDK | memory_hbm_storage | 1658.54 |  | 1643.4029 | 0.9211 | 1651.355 | 1560 | 4.4618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | META | cloud_ai_capex | 605.375 |  | 604.4769 | 0.1486 | 614.15 | 605.39 | 1.1563 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 15 | COHR | ai_networking_optical | 313.875 |  | 317.7166 | -1.2091 | 320.13 | 307.04 | 0.2836 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.45 |  | 143.9016 | -0.3138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 649.475 |  | 651.7267 | -0.3455 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 412.78 |  | 413.328 | -0.1326 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 318.55 |  | 320.4934 | -0.6064 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CIEN | ai_networking_optical | 407.235 |  | 408.1661 | -0.2281 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036.83 |  | 1015.064 | 2.1443 | 1023.33 | 979.08 | 1.4101 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1658.54 |  | 1643.4029 | 0.9211 | 1651.355 | 1560 | 4.4618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TT | data_center_power_cooling | 477.17 |  | 476.8283 | 0.0717 | 480 | 472.33 | 0.1467 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.0709 | 0.2041 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 5 | TSM | foundry | 414.85 |  | 416.5006 | -0.3963 | 420.72 | 412.69 | 0.4821 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 576.74 |  | 580.8271 | -0.7037 | 585.98 | 576.635 | 0.052 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.09 |  | 550.805 | -0.6745 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| 8 | MU | memory_hbm_storage | 991.395 |  | 991.7281 | -0.0336 | 999.04 | 964.86 | 0.3793 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1794.65 |  | 1802.5871 | -0.4403 | 1806.11 | 1780.9 | 0.0557 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 559.655 |  | 564.9924 | -0.9447 | 566.18 | 548.47 | 3.2466 | below_vwap | below_vwap,spread_too_wide |
| 11 | ANET | ai_networking_optical | 176.06 |  | 176.6794 | -0.3506 | 177.84 | 173.19 | 3.1239 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.45 |  | 143.9016 | -0.3138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 649.475 |  | 651.7267 | -0.3455 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 214.79 |  | 215.5199 | -0.3387 | 217.88 | 212.99 | 2.961 | below_vwap | below_vwap,spread_too_wide |
| 15 | ETN | data_center_power_cooling | 412.78 |  | 413.328 | -0.1326 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | IWM | market_regime | 291.18 |  | 291.6362 | -0.1564 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 318.55 |  | 320.4934 | -0.6064 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 564 |  | 564.2538 | -0.045 | 576.24 | 556.3 | 1.211 | below_vwap | below_vwap,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505.27 |  | 507.2612 | -0.3925 | 510.71 | 502.72 | 0.1148 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.6 |  | 692.9371 | -0.3373 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.88 |  | 66.5318 | -0.9797 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.875 |  | 208.5782 | -0.3371 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.41 |  | 382.5469 | -0.2972 | 391.71 | 387.245 | 0.3828 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 319.93 |  | 320.9773 | -0.3263 | 323.25 | 320.82 | 0.0531 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.86 |  | 319.5482 | -0.2154 | 324.42 | 320.24 | 0.0502 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.42 |  | 540.2782 | -0.8992 | 556.12 | 542.33 | 2.9285 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.85 |  | 416.5006 | -0.3963 | 420.72 | 412.69 | 0.4821 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.09 |  | 550.805 | -0.6745 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.74 |  | 580.8271 | -0.7037 | 585.98 | 576.635 | 0.052 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.155 |  | 392.1674 | -0.5131 | 397.34 | 390.54 | 1.3918 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 991.395 |  | 991.7281 | -0.0336 | 999.04 | 964.86 | 0.3793 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 207.085 |  | 209.4192 | -1.1146 | 213.785 | 207.665 | 0.0724 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.8 |  | 443.5137 | -1.2883 | 450.07 | 438.55 | 1.7428 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.68 |  | 48.2968 | -1.277 | 48.88 | 47.635 | 0.0839 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.12 |  | 31.6068 | -1.5402 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 736.82 |  | 738.5946 | -0.2403 | 742.515 | 738.54 | 0.0258 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.18 |  | 291.6362 | -0.1564 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.62 |  | 121.7249 | -1.7293 | 124.22 | 122.07 | 0.7942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.515 |  | 82.7218 | -1.4589 | 84.415 | 80.64 | 3.7662 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.4 |  | 306.0792 | -1.202 | 311.13 | 303.96 | 0.4993 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.78 |  | 413.328 | -0.1326 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 649.475 |  | 651.7267 | -0.3455 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1036.83 |  | 1015.064 | 2.1443 | 1023.33 | 979.08 | 1.4101 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.17 |  | 476.8283 | 0.0717 | 480 | 472.33 | 0.1467 | watch_only | none |
| JCI | data_center_power_cooling | 143.45 |  | 143.9016 | -0.3138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.06 |  | 176.6794 | -0.3506 | 177.84 | 173.19 | 3.1239 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.875 |  | 317.7166 | -1.2091 | 320.13 | 307.04 | 0.2836 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 836.465 |  | 856.5803 | -2.3483 | 880.26 | 833 | 3.7204 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 407.235 |  | 408.1661 | -0.2281 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 112.5 |  | 114.5069 | -1.7527 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 322.71 |  | 327.4634 | -1.4516 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.65 |  | 1802.5871 | -0.4403 | 1806.11 | 1780.9 | 0.0557 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.655 |  | 564.9924 | -0.9447 | 566.18 | 548.47 | 3.2466 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.55 |  | 320.4934 | -0.6064 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.79 |  | 215.5199 | -0.3387 | 217.88 | 212.99 | 2.961 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.79 |  | 372.1104 | -0.3548 | 376.78 | 363.37 | 3.8027 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 289.91 |  | 294.0119 | -1.3952 | 301.305 | 293.685 | 4.3669 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.02 |  | 65.2124 | -0.295 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.385 |  | 135.0639 | -0.5027 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.43 |  | 342.7964 | -0.3986 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 505.27 |  | 507.2612 | -0.3925 | 510.71 | 502.72 | 0.1148 | below_vwap | below_vwap |
| APD | industrial_gases | 295.245 |  | 295.6914 | -0.151 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30 |  | 30.0551 | -0.1833 | 31.13 | 29.12 | 0.0667 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.7 |  | 41.6406 | -2.2588 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.0709 | 0.2041 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| SNDK | memory_hbm_storage | 1658.54 |  | 1643.4029 | 0.9211 | 1651.355 | 1560 | 4.4618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 564 |  | 564.2538 | -0.045 | 576.24 | 556.3 | 1.211 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 923.88 |  | 924.1372 | -0.0278 | 933.5 | 908.955 | 2.2265 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.67 |  | 234.3304 | -0.2818 | 238.285 | 235.71 | 0.0941 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.375 |  | 604.4769 | 0.1486 | 614.15 | 605.39 | 1.1563 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 279.75 |  | 279.6699 | 0.0286 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 170.64 |  | 173.499 | -1.6478 | 177.88 | 168.18 | 2.5551 | below_vwap | below_vwap,spread_too_wide |
