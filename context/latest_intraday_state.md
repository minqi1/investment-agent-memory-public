# Intraday State

- Generated at: `2026-07-24T01:48:32+08:00`
- Market time ET: `2026-07-23T13:48:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 8, 'below_vwap': 25, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.29 |  | 693.0881 | -0.1152 | 698.65 | 693.24 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.34 |  | 550.9288 | -0.4699 | 557.38 | 545.965 | 0.0657 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.33 |  | 581.126 | -0.309 | 585.98 | 576.635 | 0.0656 | below_vwap | below_vwap |
| SPY | market_regime | 738.18 |  | 738.7661 | -0.0793 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.91 |  | 31.7008 | 0.66 | 31.52 | 30.23 | 0.0627 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 416.945 |  | 416.7195 | 0.0541 | 420.72 | 412.69 | 0.3382 | watch_only | none |
| 2 | HPE | ai_server_oem | 48.4 |  | 48.3552 | 0.0927 | 48.88 | 47.635 | 0.062 | watch_only | none |
| 3 | ANET | ai_networking_optical | 177.34 |  | 176.7481 | 0.3349 | 177.84 | 173.19 | 0.2143 | watch_only | none |
| 4 | WDC | memory_hbm_storage | 565.76 |  | 564.2901 | 0.2605 | 576.24 | 556.3 | 0.2121 | watch_only | none |
| 5 | SMCI | ai_server_oem | 31.91 |  | 31.7008 | 0.66 | 31.52 | 30.23 | 0.0627 | buy_precheck_manual_confirm | none |
| 6 | NVDA | ai_accelerator | 209.74 |  | 208.5712 | 0.5604 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 7 | MU | memory_hbm_storage | 998.83 |  | 991.634 | 0.7257 | 999.04 | 964.86 | 0.3014 | watch_only | none |
| 8 | TER | semiconductor_test_packaging | 372.675 |  | 372.2809 | 0.1059 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | CIEN | ai_networking_optical | 409.3 |  | 408.2863 | 0.2483 | 408.58 | 397.9 | 3.7161 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | APLD | high_beta_ai_infrastructure | 30.18 |  | 30.0592 | 0.402 | 31.13 | 29.12 | 0.1657 | watch_only | none |
| 11 | ARM | ai_accelerator | 281.5 |  | 279.6518 | 0.6609 | 283 | 276.24 | 2.7673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | META | cloud_ai_capex | 607.415 |  | 604.1304 | 0.5437 | 614.15 | 605.39 | 1.3171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | AMZN | cloud_ai_capex | 234.37 |  | 234.3548 | 0.0065 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 14 | CORZ | high_beta_ai_infrastructure | 24.28 |  | 24.0667 | 0.8863 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| 15 | SMH | semiconductor_index | 579.33 |  | 581.126 | -0.309 | 585.98 | 576.635 | 0.0656 | below_vwap | below_vwap |
| 16 | SOXX | semiconductor_index | 548.34 |  | 550.9288 | -0.4699 | 557.38 | 545.965 | 0.0657 | below_vwap | below_vwap |
| 17 | ASML | semiconductor_equipment | 1799.99 |  | 1803.9762 | -0.221 | 1806.11 | 1780.9 | 0.0911 | below_vwap | below_vwap |
| 18 | IWM | market_regime | 291.39 |  | 291.6675 | -0.0951 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 19 | MRVL | custom_silicon_networking | 208.06 |  | 209.7351 | -0.7987 | 213.785 | 207.665 | 0.1154 | below_vwap | below_vwap |
| 20 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.91 |  | 31.7008 | 0.66 | 31.52 | 30.23 | 0.0627 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1029.305 |  | 1013.5442 | 1.555 | 1023.33 | 979.08 | 0.7374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TSM | foundry | 416.945 |  | 416.7195 | 0.0541 | 420.72 | 412.69 | 0.3382 | watch_only | none |
| 4 | CIEN | ai_networking_optical | 409.3 |  | 408.2863 | 0.2483 | 408.58 | 397.9 | 3.7161 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SNDK | memory_hbm_storage | 1675.59 |  | 1641.4924 | 2.0772 | 1651.355 | 1560 | 4.4164 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | NVDA | ai_accelerator | 209.74 |  | 208.5712 | 0.5604 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 7 | MU | memory_hbm_storage | 998.83 |  | 991.634 | 0.7257 | 999.04 | 964.86 | 0.3014 | watch_only | none |
| 8 | ANET | ai_networking_optical | 177.34 |  | 176.7481 | 0.3349 | 177.84 | 173.19 | 0.2143 | watch_only | none |
| 9 | WDC | memory_hbm_storage | 565.76 |  | 564.2901 | 0.2605 | 576.24 | 556.3 | 0.2121 | watch_only | none |
| 10 | HPE | ai_server_oem | 48.4 |  | 48.3552 | 0.0927 | 48.88 | 47.635 | 0.062 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 24.28 |  | 24.0667 | 0.8863 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| 12 | APLD | high_beta_ai_infrastructure | 30.18 |  | 30.0592 | 0.402 | 31.13 | 29.12 | 0.1657 | watch_only | none |
| 13 | SMH | semiconductor_index | 579.33 |  | 581.126 | -0.309 | 585.98 | 576.635 | 0.0656 | below_vwap | below_vwap |
| 14 | SOXX | semiconductor_index | 548.34 |  | 550.9288 | -0.4699 | 557.38 | 545.965 | 0.0657 | below_vwap | below_vwap |
| 15 | AVGO | custom_silicon_networking | 391.7 |  | 392.4938 | -0.2022 | 397.34 | 390.54 | 1.1565 | below_vwap | below_vwap,spread_too_wide |
| 16 | ASML | semiconductor_equipment | 1799.99 |  | 1803.9762 | -0.221 | 1806.11 | 1780.9 | 0.0911 | below_vwap | below_vwap |
| 17 | AMAT | semiconductor_equipment | 560.75 |  | 565.96 | -0.9206 | 566.18 | 548.47 | 4.6545 | below_vwap | below_vwap,spread_too_wide |
| 18 | TT | data_center_power_cooling | 476.21 |  | 476.8012 | -0.124 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 143.72 |  | 143.958 | -0.1653 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 649.8 |  | 652.0081 | -0.3387 | 656.38 | 642.37 | 0.3478 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.29 |  | 693.0881 | -0.1152 | 698.65 | 693.24 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.38 |  | 66.5662 | -0.2797 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.74 |  | 208.5712 | 0.5604 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.82 |  | 382.6666 | -0.4826 | 391.71 | 387.245 | 0.0656 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.985 |  | 321.1032 | -0.0368 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 319.53 |  | 319.5533 | -0.0073 | 324.42 | 320.24 | 0.0407 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 534.265 |  | 540.8169 | -1.2115 | 556.12 | 542.33 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 416.945 |  | 416.7195 | 0.0541 | 420.72 | 412.69 | 0.3382 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.34 |  | 550.9288 | -0.4699 | 557.38 | 545.965 | 0.0657 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.33 |  | 581.126 | -0.309 | 585.98 | 576.635 | 0.0656 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.7 |  | 392.4938 | -0.2022 | 397.34 | 390.54 | 1.1565 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 998.83 |  | 991.634 | 0.7257 | 999.04 | 964.86 | 0.3014 | watch_only | none |
| MRVL | custom_silicon_networking | 208.06 |  | 209.7351 | -0.7987 | 213.785 | 207.665 | 0.1154 | below_vwap | below_vwap |
| DELL | ai_server_oem | 443.57 |  | 444.03 | -0.1036 | 450.07 | 438.55 | 0.3201 | below_vwap | below_vwap |
| HPE | ai_server_oem | 48.4 |  | 48.3552 | 0.0927 | 48.88 | 47.635 | 0.062 | watch_only | none |
| SMCI | ai_server_oem | 31.91 |  | 31.7008 | 0.66 | 31.52 | 30.23 | 0.0627 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.18 |  | 738.7661 | -0.0793 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.39 |  | 291.6675 | -0.0951 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.38 |  | 121.9634 | -1.2982 | 124.22 | 122.07 | 0.3489 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.72 |  | 82.8427 | -0.1482 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.54 |  | 306.2663 | -0.8902 | 311.13 | 303.96 | 1.3013 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.41 |  | 413.3919 | -0.2375 | 415.53 | 406.545 | 0.742 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 649.8 |  | 652.0081 | -0.3387 | 656.38 | 642.37 | 0.3478 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1029.305 |  | 1013.5442 | 1.555 | 1023.33 | 979.08 | 0.7374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.21 |  | 476.8012 | -0.124 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.72 |  | 143.958 | -0.1653 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.34 |  | 176.7481 | 0.3349 | 177.84 | 173.19 | 0.2143 | watch_only | none |
| COHR | ai_networking_optical | 315.225 |  | 318.1362 | -0.9151 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 844.35 |  | 857.9583 | -1.5861 | 880.26 | 833 | 4.3323 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 409.3 |  | 408.2863 | 0.2483 | 408.58 | 397.9 | 3.7161 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.52 |  | 114.6328 | -0.9708 | 118.01 | 108.505 | 5.0564 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 326.77 |  | 327.7679 | -0.3044 | 341.68 | 327.43 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ASML | semiconductor_equipment | 1799.99 |  | 1803.9762 | -0.221 | 1806.11 | 1780.9 | 0.0911 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 560.75 |  | 565.96 | -0.9206 | 566.18 | 548.47 | 4.6545 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.3 |  | 321.1251 | -0.8797 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.74 |  | 215.689 | -0.44 | 217.88 | 212.99 | 2.1934 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.675 |  | 372.2809 | 0.1059 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.02 |  | 294.5759 | -1.5466 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.96 |  | 65.2798 | -0.4899 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.335 |  | 54.5816 | -0.4518 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.685 |  | 135.3296 | -0.4763 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.76 |  | 507.4817 | -0.3393 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.28 |  | 295.8695 | -0.1993 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.18 |  | 30.0592 | 0.402 | 31.13 | 29.12 | 0.1657 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.39 |  | 41.7176 | -0.7854 | 43.21 | 40.51 | 0.0242 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.28 |  | 24.0667 | 0.8863 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| SNDK | memory_hbm_storage | 1675.59 |  | 1641.4924 | 2.0772 | 1651.355 | 1560 | 4.4164 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 565.76 |  | 564.2901 | 0.2605 | 576.24 | 556.3 | 0.2121 | watch_only | none |
| STX | memory_hbm_storage | 923.99 |  | 924.6755 | -0.0741 | 933.5 | 908.955 | 4.9265 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 234.37 |  | 234.3548 | 0.0065 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 607.415 |  | 604.1304 | 0.5437 | 614.15 | 605.39 | 1.3171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.5 |  | 279.6518 | 0.6609 | 283 | 276.24 | 2.7673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.585 |  | 173.614 | -0.0167 | 177.88 | 168.18 | 0.2535 | below_vwap | below_vwap |
