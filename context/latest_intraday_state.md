# Intraday State

- Generated at: `2026-07-24T03:02:41+08:00`
- Market time ET: `2026-07-23T15:02:42-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 21, 'below_vwap': 28, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.63 |  | 692.886 | -0.3256 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545.89 |  | 550.7357 | -0.8799 | 557.38 | 545.965 | 0.0659 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.845 |  | 580.7241 | -0.8402 | 585.98 | 576.635 | 0.0434 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.155 |  | 738.5323 | -0.1865 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 477.95 |  | 476.8529 | 0.2301 | 480 | 472.33 | 0.2845 | watch_only | none |
| 2 | META | cloud_ai_capex | 606.34 |  | 604.5726 | 0.2923 | 614.15 | 605.39 | 0.2787 | watch_only | none |
| 3 | ETN | data_center_power_cooling | 414.06 |  | 413.3278 | 0.1771 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.82 |  | 295.6803 | 0.0472 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ASML | semiconductor_equipment | 1792.82 |  | 1802.0546 | -0.5124 | 1806.11 | 1780.9 | 0.0496 | below_vwap | below_vwap |
| 6 | AMAT | semiconductor_equipment | 556.79 |  | 564.5405 | -1.3729 | 566.18 | 548.47 | 0.1329 | below_vwap | below_vwap |
| 7 | KLAC | semiconductor_equipment | 214.84 |  | 215.4948 | -0.3038 | 217.88 | 212.99 | 0.0186 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.365 |  | 291.6164 | -0.0862 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 9 | SMCI | ai_server_oem | 30.965 |  | 31.592 | -1.9847 | 31.52 | 30.23 | 0.0646 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | IREN | high_beta_ai_infrastructure | 40.52 |  | 41.602 | -2.6008 | 43.21 | 40.51 | 0.0494 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 983.74 |  | 991.5166 | -0.7843 | 999.04 | 964.86 | 0.305 | below_vwap | below_vwap |
| 13 | AAPL | mega_cap_platform | 320.85 |  | 320.9526 | -0.032 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| 14 | JCI | data_center_power_cooling | 143.38 |  | 143.8833 | -0.3498 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 649.8 |  | 651.6399 | -0.2824 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ARM | ai_accelerator | 278.98 |  | 279.6519 | -0.2403 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | COHR | ai_networking_optical | 312.12 |  | 317.5487 | -1.7096 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LITE | ai_networking_optical | 836.16 |  | 855.5776 | -2.2695 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | TER | semiconductor_test_packaging | 369.72 |  | 372.0179 | -0.6177 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | AAOI | ai_networking_optical | 112.03 |  | 114.4456 | -2.1107 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036.985 |  | 1015.9482 | 2.0707 | 1023.33 | 979.08 | 3.8573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | TT | data_center_power_cooling | 477.95 |  | 476.8529 | 0.2301 | 480 | 472.33 | 0.2845 | watch_only | none |
| 3 | META | cloud_ai_capex | 606.34 |  | 604.5726 | 0.2923 | 614.15 | 605.39 | 0.2787 | watch_only | none |
| 4 | TSM | foundry | 414.21 |  | 416.4291 | -0.5329 | 420.72 | 412.69 | 0.9657 | below_vwap | below_vwap,spread_too_wide |
| 5 | MU | memory_hbm_storage | 983.74 |  | 991.5166 | -0.7843 | 999.04 | 964.86 | 0.305 | below_vwap | below_vwap |
| 6 | ASML | semiconductor_equipment | 1792.82 |  | 1802.0546 | -0.5124 | 1806.11 | 1780.9 | 0.0496 | below_vwap | below_vwap |
| 7 | AMAT | semiconductor_equipment | 556.79 |  | 564.5405 | -1.3729 | 566.18 | 548.47 | 0.1329 | below_vwap | below_vwap |
| 8 | ANET | ai_networking_optical | 175.88 |  | 176.6616 | -0.4424 | 177.84 | 173.19 | 2.4392 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 143.38 |  | 143.8833 | -0.3498 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 649.8 |  | 651.6399 | -0.2824 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 214.84 |  | 215.4948 | -0.3038 | 217.88 | 212.99 | 0.0186 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 291.365 |  | 291.6164 | -0.0862 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 318.25 |  | 320.3913 | -0.6683 | 322.4 | 317.27 | 4.6693 | below_vwap | below_vwap,spread_too_wide |
| 14 | ARM | ai_accelerator | 278.98 |  | 279.6519 | -0.2403 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 562.17 |  | 564.2071 | -0.3611 | 576.24 | 556.3 | 1.6098 | below_vwap | below_vwap,spread_too_wide |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LIN | industrial_gases | 506.11 |  | 507.2178 | -0.2184 | 510.71 | 502.72 | 4.9001 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 312.12 |  | 317.5487 | -1.7096 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | CIEN | ai_networking_optical | 405.745 |  | 408.041 | -0.5627 | 408.58 | 397.9 | 4.7542 | below_vwap | below_vwap,spread_too_wide |
| 20 | LITE | ai_networking_optical | 836.16 |  | 855.5776 | -2.2695 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.63 |  | 692.886 | -0.3256 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.79 |  | 66.5206 | -1.0982 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.63 |  | 208.5452 | -0.4388 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.83 |  | 382.5275 | -0.1823 | 391.71 | 387.245 | 0.2462 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.85 |  | 320.9526 | -0.032 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 318.865 |  | 319.5323 | -0.2088 | 324.42 | 320.24 | 0.0439 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.07 |  | 540.135 | -0.9377 | 556.12 | 542.33 | 0.157 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 414.21 |  | 416.4291 | -0.5329 | 420.72 | 412.69 | 0.9657 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.89 |  | 550.7357 | -0.8799 | 557.38 | 545.965 | 0.0659 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.845 |  | 580.7241 | -0.8402 | 585.98 | 576.635 | 0.0434 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.9 |  | 392.1025 | -0.5617 | 397.34 | 390.54 | 1.3362 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 983.74 |  | 991.5166 | -0.7843 | 999.04 | 964.86 | 0.305 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.57 |  | 209.3649 | -1.3349 | 213.785 | 207.665 | 0.1888 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 436.99 |  | 443.3594 | -1.4366 | 450.07 | 438.55 | 1.9222 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.59 |  | 48.262 | -1.3925 | 48.88 | 47.635 | 0.042 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.965 |  | 31.592 | -1.9847 | 31.52 | 30.23 | 0.0646 | below_vwap | below_vwap |
| SPY | market_regime | 737.155 |  | 738.5323 | -0.1865 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.365 |  | 291.6164 | -0.0862 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120 |  | 121.6905 | -1.3892 | 124.22 | 122.07 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.12 |  | 82.626 | -1.8226 | 84.415 | 80.64 | 0.4068 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.935 |  | 306.0184 | -1.3344 | 311.13 | 303.96 | 0.2782 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 414.06 |  | 413.3278 | 0.1771 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 649.8 |  | 651.6399 | -0.2824 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1036.985 |  | 1015.9482 | 2.0707 | 1023.33 | 979.08 | 3.8573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.95 |  | 476.8529 | 0.2301 | 480 | 472.33 | 0.2845 | watch_only | none |
| JCI | data_center_power_cooling | 143.38 |  | 143.8833 | -0.3498 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.88 |  | 176.6616 | -0.4424 | 177.84 | 173.19 | 2.4392 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.12 |  | 317.5487 | -1.7096 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 836.16 |  | 855.5776 | -2.2695 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 405.745 |  | 408.041 | -0.5627 | 408.58 | 397.9 | 4.7542 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.03 |  | 114.4456 | -2.1107 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.26 |  | 326.9828 | -2.056 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1792.82 |  | 1802.0546 | -0.5124 | 1806.11 | 1780.9 | 0.0496 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 556.79 |  | 564.5405 | -1.3729 | 566.18 | 548.47 | 0.1329 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 318.25 |  | 320.3913 | -0.6683 | 322.4 | 317.27 | 4.6693 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 214.84 |  | 215.4948 | -0.3038 | 217.88 | 212.99 | 0.0186 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.72 |  | 372.0179 | -0.6177 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.69 |  | 293.8387 | -1.4119 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.94 |  | 65.1995 | -0.3981 | 67.455 | 65.81 | 4.866 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.59 |  | 135.0239 | -0.3214 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.98 |  | 342.7759 | -0.5239 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 506.11 |  | 507.2178 | -0.2184 | 510.71 | 502.72 | 4.9001 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.82 |  | 295.6803 | 0.0472 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.81 |  | 30.0535 | -0.8101 | 31.13 | 29.12 | 0.4696 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.52 |  | 41.602 | -2.6008 | 43.21 | 40.51 | 0.0494 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.05 |  | 24.0723 | -0.0928 | 24.46 | 23.265 | 0.0416 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1637.655 |  | 1643.4565 | -0.353 | 1651.355 | 1560 | 4.5187 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 562.17 |  | 564.2071 | -0.3611 | 576.24 | 556.3 | 1.6098 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.84 |  | 924.0029 | -0.4505 | 933.5 | 908.955 | 0.8393 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.59 |  | 234.3133 | -0.3087 | 238.285 | 235.71 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.34 |  | 604.5726 | 0.2923 | 614.15 | 605.39 | 0.2787 | watch_only | none |
| ARM | ai_accelerator | 278.98 |  | 279.6519 | -0.2403 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 168.7 |  | 173.3501 | -2.6825 | 177.88 | 168.18 | 4.1434 | below_vwap | below_vwap,spread_too_wide |
