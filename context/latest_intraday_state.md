# Intraday State

- Generated at: `2026-07-24T03:06:35+08:00`
- Market time ET: `2026-07-23T15:06:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 25, 'below_vwap': 24, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.78 |  | 692.867 | -0.4455 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 544.79 |  | 550.7248 | -1.0776 | 557.38 | 545.965 | 0.0422 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.34 |  | 580.632 | -0.9114 | 585.98 | 576.635 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.88 |  | 738.5206 | -0.2221 | 742.515 | 738.54 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ETN | data_center_power_cooling | 413.365 |  | 413.3288 | 0.0088 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | TT | data_center_power_cooling | 478.1 |  | 476.862 | 0.2596 | 480 | 472.33 | 0.6275 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | APD | industrial_gases | 296.06 |  | 295.681 | 0.1282 | 299.26 | 295.795 | 5.1138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | META | cloud_ai_capex | 605.94 |  | 604.5916 | 0.223 | 614.15 | 605.39 | 0.8252 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TSM | foundry | 414.33 |  | 416.4119 | -0.5 | 420.72 | 412.69 | 0.029 | below_vwap | below_vwap |
| 6 | ASML | semiconductor_equipment | 1790.35 |  | 1801.998 | -0.6464 | 1806.11 | 1780.9 | 0.0771 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 291.22 |  | 291.6137 | -0.135 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 8 | WDC | memory_hbm_storage | 561.23 |  | 564.1967 | -0.5258 | 576.24 | 556.3 | 0.0784 | below_vwap | below_vwap |
| 9 | GEV | data_center_power_cooling | 1028.95 |  | 1016.0791 | 1.2667 | 1023.33 | 979.08 | 4.8632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMCI | ai_server_oem | 30.95 |  | 31.5871 | -2.0168 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | MU | memory_hbm_storage | 983.23 |  | 991.4399 | -0.8281 | 999.04 | 964.86 | 0.2593 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 143.21 |  | 143.8766 | -0.4633 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 649.68 |  | 651.6361 | -0.3002 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ARM | ai_accelerator | 278.4 |  | 279.6292 | -0.4396 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LIN | industrial_gases | 506.41 |  | 507.2129 | -0.1583 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LITE | ai_networking_optical | 834.545 |  | 855.4342 | -2.4419 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | TER | semiconductor_test_packaging | 368.31 |  | 371.9976 | -0.9913 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | AAOI | ai_networking_optical | 111.82 |  | 114.4371 | -2.2869 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | AMAT | semiconductor_equipment | 555.56 |  | 564.4813 | -1.5804 | 566.18 | 548.47 | 3.7764 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1028.95 |  | 1016.0791 | 1.2667 | 1023.33 | 979.08 | 4.8632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | TSM | foundry | 414.33 |  | 416.4119 | -0.5 | 420.72 | 412.69 | 0.029 | below_vwap | below_vwap |
| 3 | MU | memory_hbm_storage | 983.23 |  | 991.4399 | -0.8281 | 999.04 | 964.86 | 0.2593 | below_vwap | below_vwap |
| 4 | ASML | semiconductor_equipment | 1790.35 |  | 1801.998 | -0.6464 | 1806.11 | 1780.9 | 0.0771 | below_vwap | below_vwap |
| 5 | AMAT | semiconductor_equipment | 555.56 |  | 564.4813 | -1.5804 | 566.18 | 548.47 | 3.7764 | below_vwap | below_vwap,spread_too_wide |
| 6 | ANET | ai_networking_optical | 175.37 |  | 176.6589 | -0.7296 | 177.84 | 173.19 | 3.1362 | below_vwap | below_vwap,spread_too_wide |
| 7 | JCI | data_center_power_cooling | 143.21 |  | 143.8766 | -0.4633 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | PWR | data_center_power_cooling | 649.68 |  | 651.6361 | -0.3002 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 214.7 |  | 215.4878 | -0.3656 | 217.88 | 212.99 | 2.9343 | below_vwap | below_vwap,spread_too_wide |
| 10 | IWM | market_regime | 291.22 |  | 291.6137 | -0.135 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 11 | ARM | ai_accelerator | 278.4 |  | 279.6292 | -0.4396 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | WDC | memory_hbm_storage | 561.23 |  | 564.1967 | -0.5258 | 576.24 | 556.3 | 0.0784 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LIN | industrial_gases | 506.41 |  | 507.2129 | -0.1583 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | COHR | ai_networking_optical | 311.71 |  | 317.5336 | -1.834 | 320.13 | 307.04 | 4.44 | below_vwap | below_vwap,spread_too_wide |
| 16 | CIEN | ai_networking_optical | 404.92 |  | 408.0085 | -0.757 | 408.58 | 397.9 | 4.1169 | below_vwap | below_vwap,spread_too_wide |
| 17 | LITE | ai_networking_optical | 834.545 |  | 855.4342 | -2.4419 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | TER | semiconductor_test_packaging | 368.31 |  | 371.9976 | -0.9913 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | CRWV | gpu_cloud_ai_factory | 80.945 |  | 82.6169 | -2.0237 | 84.415 | 80.64 | 0.9266 | below_vwap | below_vwap,spread_too_wide |
| 20 | SNDK | memory_hbm_storage | 1628.185 |  | 1643.2223 | -0.9151 | 1651.355 | 1560 | 4.5449 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.78 |  | 692.867 | -0.4455 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.67 |  | 66.5172 | -1.2737 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.44 |  | 208.5399 | -0.5275 | 210.85 | 208.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.57 |  | 382.5237 | -0.2493 | 391.71 | 387.245 | 0.2883 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.8 |  | 320.952 | -0.0474 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.66 |  | 319.5298 | -0.2722 | 324.42 | 320.24 | 0.1224 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 534.365 |  | 540.107 | -1.0631 | 556.12 | 542.33 | 0.219 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 414.33 |  | 416.4119 | -0.5 | 420.72 | 412.69 | 0.029 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 544.79 |  | 550.7248 | -1.0776 | 557.38 | 545.965 | 0.0422 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.34 |  | 580.632 | -0.9114 | 585.98 | 576.635 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.38 |  | 392.0808 | -0.6888 | 397.34 | 390.54 | 1.2995 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 983.23 |  | 991.4399 | -0.8281 | 999.04 | 964.86 | 0.2593 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 205.84 |  | 209.3451 | -1.6743 | 213.785 | 207.665 | 0.0923 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 434.38 |  | 443.3024 | -2.0127 | 450.07 | 438.55 | 2.3988 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.42 |  | 48.259 | -1.7385 | 48.88 | 47.635 | 0.0422 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.95 |  | 31.5871 | -2.0168 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 736.88 |  | 738.5206 | -0.2221 | 742.515 | 738.54 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.22 |  | 291.6137 | -0.135 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.8 |  | 121.6866 | -1.5504 | 124.22 | 122.07 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.945 |  | 82.6169 | -2.0237 | 84.415 | 80.64 | 0.9266 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.17 |  | 305.9319 | -1.5565 | 311.13 | 303.96 | 1.4942 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.365 |  | 413.3288 | 0.0088 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 649.68 |  | 651.6361 | -0.3002 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.95 |  | 1016.0791 | 1.2667 | 1023.33 | 979.08 | 4.8632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.1 |  | 476.862 | 0.2596 | 480 | 472.33 | 0.6275 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 143.21 |  | 143.8766 | -0.4633 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.37 |  | 176.6589 | -0.7296 | 177.84 | 173.19 | 3.1362 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.71 |  | 317.5336 | -1.834 | 320.13 | 307.04 | 4.44 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 834.545 |  | 855.4342 | -2.4419 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 404.92 |  | 408.0085 | -0.757 | 408.58 | 397.9 | 4.1169 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.82 |  | 114.4371 | -2.2869 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.51 |  | 326.9242 | -2.2679 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1790.35 |  | 1801.998 | -0.6464 | 1806.11 | 1780.9 | 0.0771 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 555.56 |  | 564.4813 | -1.5804 | 566.18 | 548.47 | 3.7764 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 316.97 |  | 320.3758 | -1.0631 | 322.4 | 317.27 | 4.4799 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 214.7 |  | 215.4878 | -0.3656 | 217.88 | 212.99 | 2.9343 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 368.31 |  | 371.9976 | -0.9913 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.605 |  | 293.7929 | -1.4255 | 301.305 | 293.685 | 4.2299 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.81 |  | 65.1961 | -0.5922 | 67.455 | 65.81 | 4.6906 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.55 |  | 135.0103 | -0.3409 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.27 |  | 342.7356 | -0.7194 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 506.41 |  | 507.2129 | -0.1583 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.06 |  | 295.681 | 0.1282 | 299.26 | 295.795 | 5.1138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 29.725 |  | 30.0524 | -1.0893 | 31.13 | 29.12 | 0.0673 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.49 |  | 41.5791 | -2.6194 | 43.21 | 40.51 | 0.0247 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.95 |  | 24.071 | -0.5029 | 24.46 | 23.265 | 0.0835 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1628.185 |  | 1643.2223 | -0.9151 | 1651.355 | 1560 | 4.5449 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 561.23 |  | 564.1967 | -0.5258 | 576.24 | 556.3 | 0.0784 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 919.16 |  | 923.9357 | -0.5169 | 933.5 | 908.955 | 4.7489 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.42 |  | 234.3101 | -0.3799 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.94 |  | 604.5916 | 0.223 | 614.15 | 605.39 | 0.8252 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 278.4 |  | 279.6292 | -0.4396 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 168.075 |  | 173.3184 | -3.0253 | 177.88 | 168.18 | 1.0055 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
