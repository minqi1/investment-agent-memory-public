# Intraday State

- Generated at: `2026-07-24T02:19:51+08:00`
- Market time ET: `2026-07-23T14:19:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 20, 'below_vwap': 28, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.65 |  | 693.0007 | -0.3392 | 698.65 | 693.24 | 0.0188 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0731 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.51 |  | 580.9158 | -0.7584 | 585.98 | 576.635 | 0.0659 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.91 |  | 738.672 | -0.2385 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1032.95 |  | 1014.4287 | 1.8258 | 1023.33 | 979.08 | 0.3214 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 606.365 |  | 604.3809 | 0.3283 | 614.15 | 605.39 | 0.0577 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.12 |  | 476.7801 | 0.0713 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | CORZ | high_beta_ai_infrastructure | 24.1 |  | 24.0698 | 0.1254 | 24.46 | 23.265 | 0.083 | watch_only | none |
| 4 | GEV | data_center_power_cooling | 1032.95 |  | 1014.4287 | 1.8258 | 1023.33 | 979.08 | 0.3214 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 319.94 |  | 319.5591 | 0.1192 | 324.42 | 320.24 | 0.0844 | below_opening_15m_low | below_opening_15m_low |
| 6 | SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0731 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1788.5 |  | 1803.2309 | -0.8169 | 1806.11 | 1780.9 | 0.1247 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 557.63 |  | 565.4906 | -1.39 | 566.18 | 548.47 | 0.1417 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 290.9 |  | 291.6492 | -0.2569 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 10 | HPE | ai_server_oem | 47.75 |  | 48.3227 | -1.1852 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| 11 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 12 | CRWV | gpu_cloud_ai_factory | 81.61 |  | 82.7786 | -1.4117 | 84.415 | 80.64 | 0.147 | below_vwap | below_vwap |
| 13 | SMCI | ai_server_oem | 30.79 |  | 31.649 | -2.7142 | 31.52 | 30.23 | 0.065 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | IREN | high_beta_ai_infrastructure | 40.85 |  | 41.6778 | -1.9861 | 43.21 | 40.51 | 0.049 | below_vwap | below_vwap |
| 16 | SNDK | memory_hbm_storage | 1658.605 |  | 1642.8239 | 0.9606 | 1651.355 | 1560 | 0.4805 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SKHY | memory_hbm_storage | 172.57 |  | 173.5571 | -0.5688 | 177.88 | 168.18 | 0.2492 | below_vwap | below_vwap |
| 18 | JCI | data_center_power_cooling | 143.685 |  | 143.9207 | -0.1638 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 648.255 |  | 651.8212 | -0.5471 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 412.59 |  | 413.3502 | -0.1839 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1032.95 |  | 1014.4287 | 1.8258 | 1023.33 | 979.08 | 0.3214 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1658.605 |  | 1642.8239 | 0.9606 | 1651.355 | 1560 | 0.4805 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | META | cloud_ai_capex | 606.365 |  | 604.3809 | 0.3283 | 614.15 | 605.39 | 0.0577 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.1 |  | 24.0698 | 0.1254 | 24.46 | 23.265 | 0.083 | watch_only | none |
| 5 | TSM | foundry | 414.57 |  | 416.5954 | -0.4862 | 420.72 | 412.69 | 0.9649 | below_vwap | below_vwap,spread_too_wide |
| 6 | SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0731 | below_vwap | below_vwap |
| 7 | MU | memory_hbm_storage | 989.22 |  | 991.7012 | -0.2502 | 999.04 | 964.86 | 0.6065 | below_vwap | below_vwap,spread_too_wide |
| 8 | ASML | semiconductor_equipment | 1788.5 |  | 1803.2309 | -0.8169 | 1806.11 | 1780.9 | 0.1247 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 557.63 |  | 565.4906 | -1.39 | 566.18 | 548.47 | 0.1417 | below_vwap | below_vwap |
| 10 | ANET | ai_networking_optical | 175.94 |  | 176.7416 | -0.4535 | 177.84 | 173.19 | 3.1261 | below_vwap | below_vwap,spread_too_wide |
| 11 | JCI | data_center_power_cooling | 143.685 |  | 143.9207 | -0.1638 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 648.255 |  | 651.8212 | -0.5471 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 214.175 |  | 215.5602 | -0.6426 | 217.88 | 212.99 | 3.2684 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 412.59 |  | 413.3502 | -0.1839 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | IWM | market_regime | 290.9 |  | 291.6492 | -0.2569 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 317.69 |  | 320.6846 | -0.9338 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 279.385 |  | 279.6721 | -0.1027 | 283 | 276.24 | 1.5713 | below_vwap | below_vwap,spread_too_wide |
| 18 | WDC | memory_hbm_storage | 562.415 |  | 564.2821 | -0.3309 | 576.24 | 556.3 | 1.5451 | below_vwap | below_vwap,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505.19 |  | 507.3599 | -0.4277 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.65 |  | 693.0007 | -0.3392 | 698.65 | 693.24 | 0.0188 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.88 |  | 66.5464 | -1.0014 | 68.245 | 66.7 | 0.0304 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.28 |  | 208.5885 | -0.1479 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.46 |  | 382.5911 | -0.2956 | 391.71 | 387.245 | 0.4666 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.12 |  | 321.0414 | -0.287 | 323.25 | 320.82 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.94 |  | 319.5591 | 0.1192 | 324.42 | 320.24 | 0.0844 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 534.87 |  | 540.4593 | -1.0342 | 556.12 | 542.33 | 3.3653 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.57 |  | 416.5954 | -0.4862 | 420.72 | 412.69 | 0.9649 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0731 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.51 |  | 580.9158 | -0.7584 | 585.98 | 576.635 | 0.0659 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.74 |  | 392.2543 | -0.641 | 397.34 | 390.54 | 1.2803 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 989.22 |  | 991.7012 | -0.2502 | 999.04 | 964.86 | 0.6065 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.14 |  | 209.5323 | -1.619 | 213.785 | 207.665 | 0.097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.88 |  | 443.7615 | -1.3254 | 450.07 | 438.55 | 1.5141 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.75 |  | 48.3227 | -1.1852 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.79 |  | 31.649 | -2.7142 | 31.52 | 30.23 | 0.065 | below_vwap | below_vwap |
| SPY | market_regime | 736.91 |  | 738.672 | -0.2385 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.9 |  | 291.6492 | -0.2569 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.8 |  | 121.8682 | -1.6971 | 124.22 | 122.07 | 0.2755 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.61 |  | 82.7786 | -1.4117 | 84.415 | 80.64 | 0.147 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 302.56 |  | 306.1476 | -1.1719 | 311.13 | 303.96 | 0.4462 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.59 |  | 413.3502 | -0.1839 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 648.255 |  | 651.8212 | -0.5471 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1032.95 |  | 1014.4287 | 1.8258 | 1023.33 | 979.08 | 0.3214 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 477.12 |  | 476.7801 | 0.0713 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.685 |  | 143.9207 | -0.1638 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.94 |  | 176.7416 | -0.4535 | 177.84 | 173.19 | 3.1261 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.85 |  | 317.8609 | -1.5765 | 320.13 | 307.04 | 4.7179 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 834.29 |  | 856.9278 | -2.6417 | 880.26 | 833 | 3.2327 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 407.435 |  | 408.2727 | -0.2052 | 408.58 | 397.9 | 4.8449 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.18 |  | 114.5597 | -2.0772 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 323.96 |  | 327.6742 | -1.1335 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1788.5 |  | 1803.2309 | -0.8169 | 1806.11 | 1780.9 | 0.1247 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 557.63 |  | 565.4906 | -1.39 | 566.18 | 548.47 | 0.1417 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 317.69 |  | 320.6846 | -0.9338 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.175 |  | 215.5602 | -0.6426 | 217.88 | 212.99 | 3.2684 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 369.85 |  | 372.1735 | -0.6243 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 288.22 |  | 294.1866 | -2.0282 | 301.305 | 293.685 | 3.7992 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.73 |  | 65.2211 | -0.7529 | 67.455 | 65.81 | 4.7273 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.11 |  | 54.5411 | -0.7904 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.02 |  | 135.1717 | -0.852 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.19 |  | 507.3599 | -0.4277 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.01 |  | 295.7412 | -0.2472 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.95 |  | 30.0564 | -0.3541 | 31.13 | 29.12 | 0.1002 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.85 |  | 41.6778 | -1.9861 | 43.21 | 40.51 | 0.049 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.1 |  | 24.0698 | 0.1254 | 24.46 | 23.265 | 0.083 | watch_only | none |
| SNDK | memory_hbm_storage | 1658.605 |  | 1642.8239 | 0.9606 | 1651.355 | 1560 | 0.4805 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 562.415 |  | 564.2821 | -0.3309 | 576.24 | 556.3 | 1.5451 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.81 |  | 924.3614 | -0.4924 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 233.94 |  | 234.3489 | -0.1745 | 238.285 | 235.71 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.365 |  | 604.3809 | 0.3283 | 614.15 | 605.39 | 0.0577 | watch_only | none |
| ARM | ai_accelerator | 279.385 |  | 279.6721 | -0.1027 | 283 | 276.24 | 1.5713 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 172.57 |  | 173.5571 | -0.5688 | 177.88 | 168.18 | 0.2492 | below_vwap | below_vwap |
