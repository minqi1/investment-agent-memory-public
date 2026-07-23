# Intraday State

- Generated at: `2026-07-24T02:58:49+08:00`
- Market time ET: `2026-07-23T14:58:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 23, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.18 |  | 692.9028 | -0.393 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545.42 |  | 550.7538 | -0.9685 | 557.38 | 545.965 | 0.0678 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.61 |  | 580.7403 | -0.8834 | 585.98 | 576.635 | 0.0434 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.77 |  | 738.5476 | -0.2407 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 606.69 |  | 604.5474 | 0.3544 | 614.15 | 605.39 | 0.2967 | watch_only | none |
| 2 | ETN | data_center_power_cooling | 413.43 |  | 413.3249 | 0.0254 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | TT | data_center_power_cooling | 477.5 |  | 476.8483 | 0.1367 | 480 | 472.33 | 0.7037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | MU | memory_hbm_storage | 983.245 |  | 991.5975 | -0.8423 | 999.04 | 964.86 | 0.0946 | below_vwap | below_vwap |
| 5 | ASML | semiconductor_equipment | 1791.8 |  | 1802.1691 | -0.5754 | 1806.11 | 1780.9 | 0.0703 | below_vwap | below_vwap |
| 6 | JCI | data_center_power_cooling | 143.55 |  | 143.8885 | -0.2352 | 145.035 | 141.815 | 0.0348 | below_vwap | below_vwap |
| 7 | KLAC | semiconductor_equipment | 214.78 |  | 215.5006 | -0.3344 | 217.88 | 212.99 | 0.0745 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.11 |  | 291.6223 | -0.1757 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 9 | LIN | industrial_gases | 505.935 |  | 507.2335 | -0.256 | 510.71 | 502.72 | 0.1107 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 30.99 |  | 31.596 | -1.9179 | 31.52 | 30.23 | 0.0645 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 40.53 |  | 41.6135 | -2.6038 | 43.21 | 40.51 | 0.0493 | below_vwap | below_vwap |
| 13 | PWR | data_center_power_cooling | 649.19 |  | 651.6516 | -0.3778 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LITE | ai_networking_optical | 834.36 |  | 856.1992 | -2.5507 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 369.06 |  | 372.0343 | -0.7995 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | TSM | foundry | 414.355 |  | 416.4473 | -0.5024 | 420.72 | 412.69 | 0.5744 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMAT | semiconductor_equipment | 556.76 |  | 564.6216 | -1.3924 | 566.18 | 548.47 | 3.6748 | below_vwap | below_vwap,spread_too_wide |
| 18 | ANET | ai_networking_optical | 175.89 |  | 176.6629 | -0.4375 | 177.84 | 173.19 | 2.4106 | below_vwap | below_vwap,spread_too_wide |
| 19 | LRCX | semiconductor_equipment | 318.03 |  | 320.4093 | -0.7426 | 322.4 | 317.27 | 4.7543 | below_vwap | below_vwap,spread_too_wide |
| 20 | ARM | ai_accelerator | 278.87 |  | 279.6584 | -0.2819 | 283 | 276.24 | 1.0112 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1038.83 |  | 1015.7208 | 2.2752 | 1023.33 | 979.08 | 0.5901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | META | cloud_ai_capex | 606.69 |  | 604.5474 | 0.3544 | 614.15 | 605.39 | 0.2967 | watch_only | none |
| 3 | TSM | foundry | 414.355 |  | 416.4473 | -0.5024 | 420.72 | 412.69 | 0.5744 | below_vwap | below_vwap,spread_too_wide |
| 4 | MU | memory_hbm_storage | 983.245 |  | 991.5975 | -0.8423 | 999.04 | 964.86 | 0.0946 | below_vwap | below_vwap |
| 5 | ASML | semiconductor_equipment | 1791.8 |  | 1802.1691 | -0.5754 | 1806.11 | 1780.9 | 0.0703 | below_vwap | below_vwap |
| 6 | AMAT | semiconductor_equipment | 556.76 |  | 564.6216 | -1.3924 | 566.18 | 548.47 | 3.6748 | below_vwap | below_vwap,spread_too_wide |
| 7 | ANET | ai_networking_optical | 175.89 |  | 176.6629 | -0.4375 | 177.84 | 173.19 | 2.4106 | below_vwap | below_vwap,spread_too_wide |
| 8 | JCI | data_center_power_cooling | 143.55 |  | 143.8885 | -0.2352 | 145.035 | 141.815 | 0.0348 | below_vwap | below_vwap |
| 9 | PWR | data_center_power_cooling | 649.19 |  | 651.6516 | -0.3778 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | KLAC | semiconductor_equipment | 214.78 |  | 215.5006 | -0.3344 | 217.88 | 212.99 | 0.0745 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 291.11 |  | 291.6223 | -0.1757 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 12 | LRCX | semiconductor_equipment | 318.03 |  | 320.4093 | -0.7426 | 322.4 | 317.27 | 4.7543 | below_vwap | below_vwap,spread_too_wide |
| 13 | ARM | ai_accelerator | 278.87 |  | 279.6584 | -0.2819 | 283 | 276.24 | 1.0112 | below_vwap | below_vwap,spread_too_wide |
| 14 | WDC | memory_hbm_storage | 561.48 |  | 564.2223 | -0.486 | 576.24 | 556.3 | 1.8184 | below_vwap | below_vwap,spread_too_wide |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LIN | industrial_gases | 505.935 |  | 507.2335 | -0.256 | 510.71 | 502.72 | 0.1107 | below_vwap | below_vwap |
| 17 | COHR | ai_networking_optical | 312.46 |  | 317.5861 | -1.6141 | 320.13 | 307.04 | 0.3712 | below_vwap | below_vwap,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 405.61 |  | 408.0897 | -0.6076 | 408.58 | 397.9 | 4.7558 | below_vwap | below_vwap,spread_too_wide |
| 19 | LITE | ai_networking_optical | 834.36 |  | 856.1992 | -2.5507 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | TER | semiconductor_test_packaging | 369.06 |  | 372.0343 | -0.7995 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.18 |  | 692.9028 | -0.393 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.73 |  | 66.5235 | -1.1928 | 68.245 | 66.7 | 0.0304 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.48 |  | 208.5512 | -0.5136 | 210.85 | 208.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.86 |  | 382.5305 | -0.1753 | 391.71 | 387.245 | 0.2645 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.335 |  | 320.9544 | -0.193 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.795 |  | 319.5366 | -0.2321 | 324.42 | 320.24 | 0.0345 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 534.81 |  | 540.1688 | -0.9921 | 556.12 | 542.33 | 2.9917 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.355 |  | 416.4473 | -0.5024 | 420.72 | 412.69 | 0.5744 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.42 |  | 550.7538 | -0.9685 | 557.38 | 545.965 | 0.0678 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.61 |  | 580.7403 | -0.8834 | 585.98 | 576.635 | 0.0434 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.77 |  | 392.1147 | -0.598 | 397.34 | 390.54 | 1.2854 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 983.245 |  | 991.5975 | -0.8423 | 999.04 | 964.86 | 0.0946 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 205.905 |  | 209.3793 | -1.6593 | 213.785 | 207.665 | 0.1506 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 436.36 |  | 443.3977 | -1.5872 | 450.07 | 438.55 | 1.925 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.57 |  | 48.2657 | -1.4413 | 48.88 | 47.635 | 0.042 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.99 |  | 31.596 | -1.9179 | 31.52 | 30.23 | 0.0645 | below_vwap | below_vwap |
| SPY | market_regime | 736.77 |  | 738.5476 | -0.2407 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.11 |  | 291.6223 | -0.1757 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.88 |  | 121.6971 | -1.4931 | 124.22 | 122.07 | 0.0334 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.26 |  | 82.6672 | -1.7022 | 84.415 | 80.64 | 3.3842 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.24 |  | 306.0321 | -1.2391 | 311.13 | 303.96 | 1.3069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.43 |  | 413.3249 | 0.0254 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 649.19 |  | 651.6516 | -0.3778 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1038.83 |  | 1015.7208 | 2.2752 | 1023.33 | 979.08 | 0.5901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.5 |  | 476.8483 | 0.1367 | 480 | 472.33 | 0.7037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 143.55 |  | 143.8885 | -0.2352 | 145.035 | 141.815 | 0.0348 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 175.89 |  | 176.6629 | -0.4375 | 177.84 | 173.19 | 2.4106 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.46 |  | 317.5861 | -1.6141 | 320.13 | 307.04 | 0.3712 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 834.36 |  | 856.1992 | -2.5507 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 405.61 |  | 408.0897 | -0.6076 | 408.58 | 397.9 | 4.7558 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.79 |  | 114.4605 | -2.3332 | 118.01 | 108.505 | 3.4529 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 320.51 |  | 327.1965 | -2.0436 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1791.8 |  | 1802.1691 | -0.5754 | 1806.11 | 1780.9 | 0.0703 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 556.76 |  | 564.6216 | -1.3924 | 566.18 | 548.47 | 3.6748 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.03 |  | 320.4093 | -0.7426 | 322.4 | 317.27 | 4.7543 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 214.78 |  | 215.5006 | -0.3344 | 217.88 | 212.99 | 0.0745 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.06 |  | 372.0343 | -0.7995 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.65 |  | 293.8817 | -1.4399 | 301.305 | 293.685 | 0.4799 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.89 |  | 65.2081 | -0.4878 | 67.455 | 65.81 | 4.4691 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.49 |  | 135.0309 | -0.4006 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.98 |  | 342.7759 | -0.5239 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 505.935 |  | 507.2335 | -0.256 | 510.71 | 502.72 | 0.1107 | below_vwap | below_vwap |
| APD | industrial_gases | 295.505 |  | 295.6804 | -0.0593 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.94 |  | 30.0543 | -0.3802 | 31.13 | 29.12 | 0.3006 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.53 |  | 41.6135 | -2.6038 | 43.21 | 40.51 | 0.0493 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.05 |  | 24.0725 | -0.0934 | 24.46 | 23.265 | 0.0832 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1636.99 |  | 1643.537 | -0.3984 | 1651.355 | 1560 | 4.5205 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 561.48 |  | 564.2223 | -0.486 | 576.24 | 556.3 | 1.8184 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.53 |  | 924.0512 | -0.4893 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 233.62 |  | 234.3168 | -0.2974 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.69 |  | 604.5474 | 0.3544 | 614.15 | 605.39 | 0.2967 | watch_only | none |
| ARM | ai_accelerator | 278.87 |  | 279.6584 | -0.2819 | 283 | 276.24 | 1.0112 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 169.16 |  | 173.3866 | -2.4377 | 177.88 | 168.18 | 4.1322 | below_vwap | below_vwap,spread_too_wide |
