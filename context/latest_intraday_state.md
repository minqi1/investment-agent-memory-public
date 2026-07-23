# Intraday State

- Generated at: `2026-07-24T02:15:59+08:00`
- Market time ET: `2026-07-23T14:16:00-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 18, 'below_vwap': 30, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.96 |  | 693.0143 | -0.2964 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577 |  | 580.9253 | -0.6757 | 585.98 | 576.635 | 0.0659 | below_vwap | below_vwap |
| SPY | market_regime | 737.02 |  | 738.7024 | -0.2278 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1033.88 |  | 1014.0932 | 1.9512 | 1023.33 | 979.08 | 0.1093 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 606.41 |  | 604.3563 | 0.3398 | 614.15 | 605.39 | 0.2375 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.24 |  | 476.7758 | 0.0974 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | CORZ | high_beta_ai_infrastructure | 24.08 |  | 24.0697 | 0.0427 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 4 | GEV | data_center_power_cooling | 1033.88 |  | 1014.0932 | 1.9512 | 1023.33 | 979.08 | 0.1093 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 320.055 |  | 319.5569 | 0.1559 | 324.42 | 320.24 | 0.1187 | below_opening_15m_low | below_opening_15m_low |
| 6 | SMH | semiconductor_index | 577 |  | 580.9253 | -0.6757 | 585.98 | 576.635 | 0.0659 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1789.54 |  | 1803.3337 | -0.7649 | 1806.11 | 1780.9 | 0.0738 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 558.7 |  | 565.5336 | -1.2084 | 566.18 | 548.47 | 0.1432 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 290.89 |  | 291.6511 | -0.261 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 11 | LIN | industrial_gases | 505.42 |  | 507.4047 | -0.3912 | 510.71 | 502.72 | 0.0396 | below_vwap | below_vwap |
| 12 | TSM | foundry | 414.53 |  | 416.6135 | -0.5001 | 420.72 | 412.69 | 0.3401 | below_vwap | below_vwap |
| 13 | HPE | ai_server_oem | 47.78 |  | 48.327 | -1.1319 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| 14 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 15 | SMCI | ai_server_oem | 30.76 |  | 31.6603 | -2.8436 | 31.52 | 30.23 | 0.0325 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 40.995 |  | 41.6817 | -1.6474 | 43.21 | 40.51 | 0.0732 | below_vwap | below_vwap |
| 18 | MU | memory_hbm_storage | 990.81 |  | 991.7149 | -0.0912 | 999.04 | 964.86 | 0.322 | below_vwap | below_vwap |
| 19 | KLAC | semiconductor_equipment | 214.08 |  | 215.5723 | -0.6923 | 217.88 | 212.99 | 0.2055 | below_vwap | below_vwap |
| 20 | ARM | ai_accelerator | 279.42 |  | 279.6752 | -0.0913 | 283 | 276.24 | 0.1718 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1033.88 |  | 1014.0932 | 1.9512 | 1023.33 | 979.08 | 0.1093 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1666.885 |  | 1642.6708 | 1.4741 | 1651.355 | 1560 | 1.4956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | META | cloud_ai_capex | 606.41 |  | 604.3563 | 0.3398 | 614.15 | 605.39 | 0.2375 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.08 |  | 24.0697 | 0.0427 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 5 | TSM | foundry | 414.53 |  | 416.6135 | -0.5001 | 420.72 | 412.69 | 0.3401 | below_vwap | below_vwap |
| 6 | SMH | semiconductor_index | 577 |  | 580.9253 | -0.6757 | 585.98 | 576.635 | 0.0659 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| 8 | MU | memory_hbm_storage | 990.81 |  | 991.7149 | -0.0912 | 999.04 | 964.86 | 0.322 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1789.54 |  | 1803.3337 | -0.7649 | 1806.11 | 1780.9 | 0.0738 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 558.7 |  | 565.5336 | -1.2084 | 566.18 | 548.47 | 0.1432 | below_vwap | below_vwap |
| 11 | ANET | ai_networking_optical | 176.24 |  | 176.746 | -0.2863 | 177.84 | 173.19 | 3.1207 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.615 |  | 143.9227 | -0.2138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 648.68 |  | 651.8594 | -0.4877 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 214.08 |  | 215.5723 | -0.6923 | 217.88 | 212.99 | 0.2055 | below_vwap | below_vwap |
| 15 | ETN | data_center_power_cooling | 413.12 |  | 413.3532 | -0.0564 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | IWM | market_regime | 290.89 |  | 291.6511 | -0.261 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 317.86 |  | 320.7548 | -0.9025 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 279.42 |  | 279.6752 | -0.0913 | 283 | 276.24 | 0.1718 | below_vwap | below_vwap |
| 19 | WDC | memory_hbm_storage | 563.005 |  | 564.2917 | -0.228 | 576.24 | 556.3 | 0.5258 | below_vwap | below_vwap,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.96 |  | 693.0143 | -0.2964 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.93 |  | 66.5503 | -0.932 | 68.245 | 66.7 | 0.0303 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.47 |  | 208.5895 | -0.0573 | 210.85 | 208.49 | 0.024 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.115 |  | 382.5984 | -0.3877 | 391.71 | 387.245 | 0.7032 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.16 |  | 321.0485 | -0.2767 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.055 |  | 319.5569 | 0.1559 | 324.42 | 320.24 | 0.1187 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 535.75 |  | 540.4763 | -0.8745 | 556.12 | 542.33 | 2.0831 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.53 |  | 416.6135 | -0.5001 | 420.72 | 412.69 | 0.3401 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.34 |  | 550.8883 | -0.6441 | 557.38 | 545.965 | 0.0713 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577 |  | 580.9253 | -0.6757 | 585.98 | 576.635 | 0.0659 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 389.705 |  | 392.2677 | -0.6533 | 397.34 | 390.54 | 1.3395 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 990.81 |  | 991.7149 | -0.0912 | 999.04 | 964.86 | 0.322 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.51 |  | 209.5648 | -1.4577 | 213.785 | 207.665 | 4.2516 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 439.33 |  | 443.7865 | -1.0042 | 450.07 | 438.55 | 1.5046 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.78 |  | 48.327 | -1.1319 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.76 |  | 31.6603 | -2.8436 | 31.52 | 30.23 | 0.0325 | below_vwap | below_vwap |
| SPY | market_regime | 737.02 |  | 738.7024 | -0.2278 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.89 |  | 291.6511 | -0.261 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.88 |  | 121.8791 | -1.6403 | 124.22 | 122.07 | 0.1084 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.695 |  | 82.782 | -1.313 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.41 |  | 306.1635 | -1.226 | 311.13 | 303.96 | 1.3062 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.12 |  | 413.3532 | -0.0564 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 648.68 |  | 651.8594 | -0.4877 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1033.88 |  | 1014.0932 | 1.9512 | 1023.33 | 979.08 | 0.1093 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 477.24 |  | 476.7758 | 0.0974 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.615 |  | 143.9227 | -0.2138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.24 |  | 176.746 | -0.2863 | 177.84 | 173.19 | 3.1207 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.8 |  | 317.8719 | -1.5956 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.56 |  | 857.0501 | -2.5074 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.75 |  | 408.2866 | -0.1314 | 408.58 | 397.9 | 4.4488 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.54 |  | 114.5705 | -1.7723 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 323.96 |  | 327.6742 | -1.1335 | 341.68 | 327.43 | 4.3215 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1789.54 |  | 1803.3337 | -0.7649 | 1806.11 | 1780.9 | 0.0738 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.7 |  | 565.5336 | -1.2084 | 566.18 | 548.47 | 0.1432 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 317.86 |  | 320.7548 | -0.9025 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.08 |  | 215.5723 | -0.6923 | 217.88 | 212.99 | 0.2055 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.9 |  | 372.1904 | -0.6154 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 288.48 |  | 294.2157 | -1.9495 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.76 |  | 65.2239 | -0.7112 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.11 |  | 54.5411 | -0.7904 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.02 |  | 135.1717 | -0.852 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.42 |  | 507.4047 | -0.3912 | 510.71 | 502.72 | 0.0396 | below_vwap | below_vwap |
| APD | industrial_gases | 295.085 |  | 295.7449 | -0.2231 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.98 |  | 30.0581 | -0.2597 | 31.13 | 29.12 | 0.0667 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.995 |  | 41.6817 | -1.6474 | 43.21 | 40.51 | 0.0732 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.08 |  | 24.0697 | 0.0427 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| SNDK | memory_hbm_storage | 1666.885 |  | 1642.6708 | 1.4741 | 1651.355 | 1560 | 1.4956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 563.005 |  | 564.2917 | -0.228 | 576.24 | 556.3 | 0.5258 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 920.1 |  | 924.4332 | -0.4687 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.06 |  | 234.3502 | -0.1238 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.41 |  | 604.3563 | 0.3398 | 614.15 | 605.39 | 0.2375 | watch_only | none |
| ARM | ai_accelerator | 279.42 |  | 279.6752 | -0.0913 | 283 | 276.24 | 0.1718 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 172.735 |  | 173.5631 | -0.4771 | 177.88 | 168.18 | 0.2026 | below_vwap | below_vwap |
