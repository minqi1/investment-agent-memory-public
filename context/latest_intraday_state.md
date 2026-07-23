# Intraday State

- Generated at: `2026-07-24T02:23:47+08:00`
- Market time ET: `2026-07-23T14:23:48-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'below_vwap': 28, 'price_stale_or_missing': 3, 'watch_only': 2, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.04 |  | 692.9963 | -0.2823 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.71 |  | 550.8812 | -0.7572 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.075 |  | 580.907 | -0.6597 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| SPY | market_regime | 737.2 |  | 738.6583 | -0.1974 | 742.515 | 738.54 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 992.52 |  | 991.6919 | 0.0835 | 999.04 | 964.86 | 0.0736 | watch_only | none |
| 2 | CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.07 | 0.2078 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 3 | TT | data_center_power_cooling | 477.62 |  | 476.7837 | 0.1754 | 480 | 472.33 | 0.3622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | META | cloud_ai_capex | 605.42 |  | 604.4145 | 0.1664 | 614.15 | 605.39 | 0.4939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GOOGL | cloud_ai_capex | 319.71 |  | 319.5603 | 0.0469 | 324.42 | 320.24 | 0.0438 | below_opening_15m_low | below_opening_15m_low |
| 6 | SMH | semiconductor_index | 577.075 |  | 580.907 | -0.6597 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 546.71 |  | 550.8812 | -0.7572 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1791.6 |  | 1803.0502 | -0.635 | 1806.11 | 1780.9 | 0.0625 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 291.095 |  | 291.6468 | -0.1892 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 10 | HPE | ai_server_oem | 47.685 |  | 48.3193 | -1.3127 | 48.88 | 47.635 | 0.0629 | below_vwap | below_vwap |
| 11 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 12 | SMCI | ai_server_oem | 31.13 |  | 31.6382 | -1.6063 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 40.81 |  | 41.669 | -2.0615 | 43.21 | 40.51 | 0.0735 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1661.33 |  | 1642.898 | 1.1219 | 1651.355 | 1560 | 3.0698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SKHY | memory_hbm_storage | 173.15 |  | 173.5478 | -0.2292 | 177.88 | 168.18 | 0.2599 | below_vwap | below_vwap |
| 17 | JCI | data_center_power_cooling | 143.8 |  | 143.9199 | -0.0833 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 649.19 |  | 651.7694 | -0.3958 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 412.59 |  | 413.3442 | -0.1825 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LRCX | semiconductor_equipment | 317.77 |  | 320.6589 | -0.9009 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1034.88 |  | 1014.5841 | 2.0004 | 1023.33 | 979.08 | 0.5923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1661.33 |  | 1642.898 | 1.1219 | 1651.355 | 1560 | 3.0698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | MU | memory_hbm_storage | 992.52 |  | 991.6919 | 0.0835 | 999.04 | 964.86 | 0.0736 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.07 | 0.2078 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 5 | TSM | foundry | 414.87 |  | 416.5764 | -0.4096 | 420.72 | 412.69 | 0.7159 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 577.075 |  | 580.907 | -0.6597 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 546.71 |  | 550.8812 | -0.7572 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1791.6 |  | 1803.0502 | -0.635 | 1806.11 | 1780.9 | 0.0625 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 558.34 |  | 565.3493 | -1.2398 | 566.18 | 548.47 | 0.36 | below_vwap | below_vwap,spread_too_wide |
| 10 | ANET | ai_networking_optical | 175.98 |  | 176.7302 | -0.4245 | 177.84 | 173.19 | 3.1254 | below_vwap | below_vwap,spread_too_wide |
| 11 | JCI | data_center_power_cooling | 143.8 |  | 143.9199 | -0.0833 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 649.19 |  | 651.7694 | -0.3958 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 214.4 |  | 215.553 | -0.5349 | 217.88 | 212.99 | 2.1688 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 412.59 |  | 413.3442 | -0.1825 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | IWM | market_regime | 291.095 |  | 291.6468 | -0.1892 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 317.77 |  | 320.6589 | -0.9009 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 279.365 |  | 279.6634 | -0.1067 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 562.5 |  | 564.2751 | -0.3146 | 576.24 | 556.3 | 1.4542 | below_vwap | below_vwap,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505 |  | 507.3552 | -0.4642 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.04 |  | 692.9963 | -0.2823 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.99 |  | 66.544 | -0.8326 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.45 |  | 208.5867 | -0.0656 | 210.85 | 208.49 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.41 |  | 382.5824 | -0.3064 | 391.71 | 387.245 | 0.3671 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.35 |  | 321.036 | -0.2137 | 323.25 | 320.82 | 0.0406 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.71 |  | 319.5603 | 0.0469 | 324.42 | 320.24 | 0.0438 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 535.62 |  | 540.433 | -0.8906 | 556.12 | 542.33 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 414.87 |  | 416.5764 | -0.4096 | 420.72 | 412.69 | 0.7159 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.71 |  | 550.8812 | -0.7572 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.075 |  | 580.907 | -0.6597 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 389.995 |  | 392.2411 | -0.5726 | 397.34 | 390.54 | 1.3282 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.52 |  | 991.6919 | 0.0835 | 999.04 | 964.86 | 0.0736 | watch_only | none |
| MRVL | custom_silicon_networking | 206.72 |  | 209.5183 | -1.3356 | 213.785 | 207.665 | 0.5611 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 438.21 |  | 443.7586 | -1.2504 | 450.07 | 438.55 | 1.5746 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.685 |  | 48.3193 | -1.3127 | 48.88 | 47.635 | 0.0629 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.13 |  | 31.6382 | -1.6063 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 737.2 |  | 738.6583 | -0.1974 | 742.515 | 738.54 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.095 |  | 291.6468 | -0.1892 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.77 |  | 121.8506 | -1.7075 | 124.22 | 122.07 | 0.025 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.68 |  | 82.775 | -1.3228 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.47 |  | 306.126 | -1.1943 | 311.13 | 303.96 | 0.5455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.59 |  | 413.3442 | -0.1825 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 649.19 |  | 651.7694 | -0.3958 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1034.88 |  | 1014.5841 | 2.0004 | 1023.33 | 979.08 | 0.5923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.62 |  | 476.7837 | 0.1754 | 480 | 472.33 | 0.3622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 143.8 |  | 143.9199 | -0.0833 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.98 |  | 176.7302 | -0.4245 | 177.84 | 173.19 | 3.1254 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.585 |  | 317.8172 | -1.3317 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.765 |  | 856.898 | -2.4662 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 408.04 |  | 408.2492 | -0.0513 | 408.58 | 397.9 | 4.4603 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.45 |  | 114.5493 | -1.8326 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 322.86 |  | 327.6626 | -1.4657 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1791.6 |  | 1803.0502 | -0.635 | 1806.11 | 1780.9 | 0.0625 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.34 |  | 565.3493 | -1.2398 | 566.18 | 548.47 | 0.36 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.77 |  | 320.6589 | -0.9009 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.4 |  | 215.553 | -0.5349 | 217.88 | 212.99 | 2.1688 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.08 |  | 372.1614 | -0.5593 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 288.545 |  | 294.0687 | -1.8784 | 301.305 | 293.685 | 0.4089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.715 |  | 65.2178 | -0.7709 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.11 |  | 54.5411 | -0.7904 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 133.845 |  | 135.1503 | -0.9658 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505 |  | 507.3552 | -0.4642 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.21 |  | 295.7342 | -0.1773 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.99 |  | 30.0561 | -0.2198 | 31.13 | 29.12 | 0.2001 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.81 |  | 41.669 | -2.0615 | 43.21 | 40.51 | 0.0735 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.07 | 0.2078 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| SNDK | memory_hbm_storage | 1661.33 |  | 1642.898 | 1.1219 | 1651.355 | 1560 | 3.0698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 562.5 |  | 564.2751 | -0.3146 | 576.24 | 556.3 | 1.4542 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 920.98 |  | 924.2938 | -0.3585 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 233.8 |  | 234.3465 | -0.2332 | 238.285 | 235.71 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.42 |  | 604.4145 | 0.1664 | 614.15 | 605.39 | 0.4939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.365 |  | 279.6634 | -0.1067 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 173.15 |  | 173.5478 | -0.2292 | 177.88 | 168.18 | 0.2599 | below_vwap | below_vwap |
