# Intraday State

- Generated at: `2026-07-24T02:12:06+08:00`
- Market time ET: `2026-07-23T14:12:07-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'watch_only': 2, 'below_vwap': 28, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.67 |  | 693.0294 | -0.3405 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.3 |  | 550.897 | -0.8345 | 557.38 | 545.965 | 0.0842 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.27 |  | 580.931 | -0.8023 | 585.98 | 576.635 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.95 |  | 738.7302 | -0.241 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 208.62 |  | 208.5892 | 0.0147 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.07 |  | 476.7722 | 0.0625 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | CORZ | high_beta_ai_infrastructure | 24.09 |  | 24.0694 | 0.0857 | 24.46 | 23.265 | 0.1245 | watch_only | none |
| 4 | META | cloud_ai_capex | 606.785 |  | 604.326 | 0.4069 | 614.15 | 605.39 | 0.6263 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GOOGL | cloud_ai_capex | 319.79 |  | 319.5535 | 0.074 | 324.42 | 320.24 | 0.2533 | below_opening_15m_low | below_opening_15m_low |
| 6 | SOXX | semiconductor_index | 546.3 |  | 550.897 | -0.8345 | 557.38 | 545.965 | 0.0842 | below_vwap | below_vwap |
| 7 | MU | memory_hbm_storage | 989.19 |  | 991.7183 | -0.2549 | 999.04 | 964.86 | 0.1425 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1789.76 |  | 1803.4823 | -0.7609 | 1806.11 | 1780.9 | 0.1101 | below_vwap | below_vwap |
| 9 | KLAC | semiconductor_equipment | 213.67 |  | 215.5821 | -0.8869 | 217.88 | 212.99 | 0.103 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 290.96 |  | 291.6521 | -0.2373 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 11 | TSM | foundry | 414.42 |  | 416.6351 | -0.5317 | 420.72 | 412.69 | 0.1906 | below_vwap | below_vwap |
| 12 | HPE | ai_server_oem | 47.76 |  | 48.3297 | -1.1787 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| 13 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 14 | SKHY | memory_hbm_storage | 172.09 |  | 173.5731 | -0.8545 | 177.88 | 168.18 | 0.1162 | below_vwap | below_vwap |
| 15 | SMCI | ai_server_oem | 30.88 |  | 31.6727 | -2.5028 | 31.52 | 30.23 | 0.0648 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 40.99 |  | 41.686 | -1.6696 | 43.21 | 40.51 | 0.0732 | below_vwap | below_vwap |
| 18 | SNDK | memory_hbm_storage | 1659.955 |  | 1642.4284 | 1.0671 | 1651.355 | 1560 | 1.7591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | WDC | memory_hbm_storage | 560.92 |  | 564.3029 | -0.5995 | 576.24 | 556.3 | 0.2318 | below_vwap | below_vwap |
| 20 | PWR | data_center_power_cooling | 648.305 |  | 651.8816 | -0.5487 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1031.25 |  | 1013.9347 | 1.7077 | 1023.33 | 979.08 | 1.696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1659.955 |  | 1642.4284 | 1.0671 | 1651.355 | 1560 | 1.7591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | NVDA | ai_accelerator | 208.62 |  | 208.5892 | 0.0147 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.09 |  | 24.0694 | 0.0857 | 24.46 | 23.265 | 0.1245 | watch_only | none |
| 5 | TSM | foundry | 414.42 |  | 416.6351 | -0.5317 | 420.72 | 412.69 | 0.1906 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 546.3 |  | 550.897 | -0.8345 | 557.38 | 545.965 | 0.0842 | below_vwap | below_vwap |
| 7 | MU | memory_hbm_storage | 989.19 |  | 991.7183 | -0.2549 | 999.04 | 964.86 | 0.1425 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1789.76 |  | 1803.4823 | -0.7609 | 1806.11 | 1780.9 | 0.1101 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 558.08 |  | 565.5776 | -1.3256 | 566.18 | 548.47 | 4.3238 | below_vwap | below_vwap,spread_too_wide |
| 10 | ANET | ai_networking_optical | 176.06 |  | 176.7494 | -0.3901 | 177.84 | 173.19 | 2.2379 | below_vwap | below_vwap,spread_too_wide |
| 11 | JCI | data_center_power_cooling | 143.59 |  | 143.9247 | -0.2326 | 145.035 | 141.815 | 2.3609 | below_vwap | below_vwap,spread_too_wide |
| 12 | PWR | data_center_power_cooling | 648.305 |  | 651.8816 | -0.5487 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 213.67 |  | 215.5821 | -0.8869 | 217.88 | 212.99 | 0.103 | below_vwap | below_vwap |
| 14 | ETN | data_center_power_cooling | 412.65 |  | 413.3552 | -0.1706 | 415.53 | 406.545 | 0.7852 | below_vwap | below_vwap,spread_too_wide |
| 15 | IWM | market_regime | 290.96 |  | 291.6521 | -0.2373 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 16 | ARM | ai_accelerator | 279.28 |  | 279.6773 | -0.1421 | 283 | 276.24 | 2.7893 | below_vwap | below_vwap,spread_too_wide |
| 17 | WDC | memory_hbm_storage | 560.92 |  | 564.3029 | -0.5995 | 576.24 | 556.3 | 0.2318 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 505.65 |  | 507.4186 | -0.3485 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | HPE | ai_server_oem | 47.76 |  | 48.3297 | -1.1787 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.67 |  | 693.0294 | -0.3405 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.89 |  | 66.554 | -0.9977 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.62 |  | 208.5892 | 0.0147 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| MSFT | cloud_ai_capex | 381.17 |  | 382.6073 | -0.3757 | 391.71 | 387.245 | 0.021 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.19 |  | 321.0573 | -0.2701 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.79 |  | 319.5535 | 0.074 | 324.42 | 320.24 | 0.2533 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 534.475 |  | 540.5038 | -1.1154 | 556.12 | 542.33 | 1.9346 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.42 |  | 416.6351 | -0.5317 | 420.72 | 412.69 | 0.1906 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.3 |  | 550.897 | -0.8345 | 557.38 | 545.965 | 0.0842 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.27 |  | 580.931 | -0.8023 | 585.98 | 576.635 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.315 |  | 392.2937 | -0.7593 | 397.34 | 390.54 | 1.7698 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 989.19 |  | 991.7183 | -0.2549 | 999.04 | 964.86 | 0.1425 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.065 |  | 209.5993 | -1.6862 | 213.785 | 207.665 | 0.2426 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 438.41 |  | 443.8285 | -1.2209 | 450.07 | 438.55 | 1.672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.76 |  | 48.3297 | -1.1787 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.88 |  | 31.6727 | -2.5028 | 31.52 | 30.23 | 0.0648 | below_vwap | below_vwap |
| SPY | market_regime | 736.95 |  | 738.7302 | -0.241 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.96 |  | 291.6521 | -0.2373 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.035 |  | 121.8897 | -1.5217 | 124.22 | 122.07 | 0.1666 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.705 |  | 82.7886 | -1.3089 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302 |  | 306.1808 | -1.3655 | 311.13 | 303.96 | 0.4073 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.65 |  | 413.3552 | -0.1706 | 415.53 | 406.545 | 0.7852 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 648.305 |  | 651.8816 | -0.5487 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1031.25 |  | 1013.9347 | 1.7077 | 1023.33 | 979.08 | 1.696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.07 |  | 476.7722 | 0.0625 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.59 |  | 143.9247 | -0.2326 | 145.035 | 141.815 | 2.3609 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 176.06 |  | 176.7494 | -0.3901 | 177.84 | 173.19 | 2.2379 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.535 |  | 317.9021 | -2.0029 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 833.13 |  | 857.103 | -2.797 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 406.03 |  | 408.2961 | -0.555 | 408.58 | 397.9 | 4.7435 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.3 |  | 114.5792 | -1.9892 | 118.01 | 108.505 | 0.8014 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 324.82 |  | 327.7074 | -0.8811 | 341.68 | 327.43 | 4.2177 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| ASML | semiconductor_equipment | 1789.76 |  | 1803.4823 | -0.7609 | 1806.11 | 1780.9 | 0.1101 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.08 |  | 565.5776 | -1.3256 | 566.18 | 548.47 | 4.3238 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 316.99 |  | 320.7793 | -1.1813 | 322.4 | 317.27 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 213.67 |  | 215.5821 | -0.8869 | 217.88 | 212.99 | 0.103 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.08 |  | 372.2133 | -0.8418 | 376.78 | 363.37 | 0.3766 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 288.17 |  | 294.3344 | -2.0944 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.69 |  | 65.2278 | -0.8245 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.11 |  | 54.5411 | -0.7904 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.86 |  | 135.2032 | -0.9935 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.65 |  | 507.4186 | -0.3485 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.24 |  | 295.7688 | -0.1788 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.95 |  | 30.0585 | -0.3609 | 31.13 | 29.12 | 0.0668 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.99 |  | 41.686 | -1.6696 | 43.21 | 40.51 | 0.0732 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.09 |  | 24.0694 | 0.0857 | 24.46 | 23.265 | 0.1245 | watch_only | none |
| SNDK | memory_hbm_storage | 1659.955 |  | 1642.4284 | 1.0671 | 1651.355 | 1560 | 1.7591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 560.92 |  | 564.3029 | -0.5995 | 576.24 | 556.3 | 0.2318 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 918.24 |  | 924.5183 | -0.6791 | 933.5 | 908.955 | 4.7765 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 234.26 |  | 234.3517 | -0.0391 | 238.285 | 235.71 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.785 |  | 604.326 | 0.4069 | 614.15 | 605.39 | 0.6263 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.28 |  | 279.6773 | -0.1421 | 283 | 276.24 | 2.7893 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 172.09 |  | 173.5731 | -0.8545 | 177.88 | 168.18 | 0.1162 | below_vwap | below_vwap |
