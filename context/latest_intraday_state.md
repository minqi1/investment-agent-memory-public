# Intraday State

- Generated at: `2026-07-24T02:04:21+08:00`
- Market time ET: `2026-07-23T14:04:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 16, 'watch_only': 3, 'below_vwap': 30, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.22 |  | 693.0587 | -0.2653 | 698.65 | 693.24 | 0.0275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.245 |  | 550.9075 | -0.6648 | 557.38 | 545.965 | 0.0676 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.19 |  | 581.0606 | -0.6661 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| SPY | market_regime | 737.27 |  | 738.7446 | -0.1996 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 208.87 |  | 208.5898 | 0.1343 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 2 | MU | memory_hbm_storage | 994.53 |  | 991.7285 | 0.2825 | 999.04 | 964.86 | 0.0543 | watch_only | none |
| 3 | CORZ | high_beta_ai_infrastructure | 24.07 |  | 24.0692 | 0.0031 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 4 | ARM | ai_accelerator | 279.94 |  | 279.6804 | 0.0928 | 283 | 276.24 | 1.2467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | WDC | memory_hbm_storage | 564.45 |  | 564.3209 | 0.0229 | 576.24 | 556.3 | 1.1108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | META | cloud_ai_capex | 606.075 |  | 604.2975 | 0.2941 | 614.15 | 605.39 | 0.8943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | GOOGL | cloud_ai_capex | 319.87 |  | 319.5517 | 0.0996 | 324.42 | 320.24 | 0.1469 | below_opening_15m_low | below_opening_15m_low |
| 8 | SMH | semiconductor_index | 577.19 |  | 581.0606 | -0.6661 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| 9 | SOXX | semiconductor_index | 547.245 |  | 550.9075 | -0.6648 | 557.38 | 545.965 | 0.0676 | below_vwap | below_vwap |
| 10 | ASML | semiconductor_equipment | 1793.63 |  | 1803.6615 | -0.5562 | 1806.11 | 1780.9 | 0.0719 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 291 |  | 291.6571 | -0.2253 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 12 | LRCX | semiconductor_equipment | 317.735 |  | 320.91 | -0.9894 | 322.4 | 317.27 | 0.085 | below_vwap | below_vwap |
| 13 | HPE | ai_server_oem | 47.9 |  | 48.3486 | -0.9278 | 48.88 | 47.635 | 0.0626 | below_vwap | below_vwap |
| 14 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 15 | SMCI | ai_server_oem | 31.22 |  | 31.6963 | -1.5028 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 40.84 |  | 41.7011 | -2.0649 | 43.21 | 40.51 | 0.0735 | below_vwap | below_vwap |
| 18 | LITE | ai_networking_optical | 837.51 |  | 857.5261 | -2.3342 | 880.26 | 833 | 0.1528 | below_vwap | below_vwap |
| 19 | JCI | data_center_power_cooling | 143.515 |  | 143.9391 | -0.2947 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 648.73 |  | 651.9282 | -0.4906 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1030.36 |  | 1013.7552 | 1.6379 | 1023.33 | 979.08 | 1.8343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1667.935 |  | 1642.1587 | 1.5697 | 1651.355 | 1560 | 1.7986 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | NVDA | ai_accelerator | 208.87 |  | 208.5898 | 0.1343 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 4 | MU | memory_hbm_storage | 994.53 |  | 991.7285 | 0.2825 | 999.04 | 964.86 | 0.0543 | watch_only | none |
| 5 | CORZ | high_beta_ai_infrastructure | 24.07 |  | 24.0692 | 0.0031 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 6 | TSM | foundry | 415.03 |  | 416.6857 | -0.3974 | 420.72 | 412.69 | 0.7493 | below_vwap | below_vwap,spread_too_wide |
| 7 | SMH | semiconductor_index | 577.19 |  | 581.0606 | -0.6661 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 547.245 |  | 550.9075 | -0.6648 | 557.38 | 545.965 | 0.0676 | below_vwap | below_vwap |
| 9 | AVGO | custom_silicon_networking | 390.62 |  | 392.3645 | -0.4446 | 397.34 | 390.54 | 1.5437 | below_vwap | below_vwap,spread_too_wide |
| 10 | ASML | semiconductor_equipment | 1793.63 |  | 1803.6615 | -0.5562 | 1806.11 | 1780.9 | 0.0719 | below_vwap | below_vwap |
| 11 | AMAT | semiconductor_equipment | 558.715 |  | 565.6973 | -1.2343 | 566.18 | 548.47 | 4.19 | below_vwap | below_vwap,spread_too_wide |
| 12 | TT | data_center_power_cooling | 476.32 |  | 476.7783 | -0.0961 | 480 | 472.33 | 0.8965 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 176.43 |  | 176.7543 | -0.1835 | 177.84 | 173.19 | 2.0858 | below_vwap | below_vwap,spread_too_wide |
| 14 | JCI | data_center_power_cooling | 143.515 |  | 143.9391 | -0.2947 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 648.73 |  | 651.9282 | -0.4906 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 214.03 |  | 215.6135 | -0.7344 | 217.88 | 212.99 | 1.8502 | below_vwap | below_vwap,spread_too_wide |
| 17 | ETN | data_center_power_cooling | 412.54 |  | 413.3782 | -0.2028 | 415.53 | 406.545 | 0.8048 | below_vwap | below_vwap,spread_too_wide |
| 18 | IWM | market_regime | 291 |  | 291.6571 | -0.2253 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 19 | LRCX | semiconductor_equipment | 317.735 |  | 320.91 | -0.9894 | 322.4 | 317.27 | 0.085 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.22 |  | 693.0587 | -0.2653 | 698.65 | 693.24 | 0.0275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.01 |  | 66.5581 | -0.8235 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.87 |  | 208.5898 | 0.1343 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| MSFT | cloud_ai_capex | 380.95 |  | 382.6254 | -0.4379 | 391.71 | 387.245 | 0.3649 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.46 |  | 321.0927 | -0.197 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.87 |  | 319.5517 | 0.0996 | 324.42 | 320.24 | 0.1469 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 534.45 |  | 540.5799 | -1.134 | 556.12 | 542.33 | 1.9048 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.03 |  | 416.6857 | -0.3974 | 420.72 | 412.69 | 0.7493 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.245 |  | 550.9075 | -0.6648 | 557.38 | 545.965 | 0.0676 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.19 |  | 581.0606 | -0.6661 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.62 |  | 392.3645 | -0.4446 | 397.34 | 390.54 | 1.5437 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 994.53 |  | 991.7285 | 0.2825 | 999.04 | 964.86 | 0.0543 | watch_only | none |
| MRVL | custom_silicon_networking | 206.66 |  | 209.656 | -1.429 | 213.785 | 207.665 | 0.4016 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 439.02 |  | 443.9026 | -1.0999 | 450.07 | 438.55 | 1.3166 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.9 |  | 48.3486 | -0.9278 | 48.88 | 47.635 | 0.0626 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.22 |  | 31.6963 | -1.5028 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| SPY | market_regime | 737.27 |  | 738.7446 | -0.1996 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291 |  | 291.6571 | -0.2253 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.145 |  | 121.9167 | -1.4532 | 124.22 | 122.07 | 0.2247 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.99 |  | 82.8059 | -0.9854 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.35 |  | 306.193 | -1.2551 | 311.13 | 303.96 | 1.3064 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.54 |  | 413.3782 | -0.2028 | 415.53 | 406.545 | 0.8048 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 648.73 |  | 651.9282 | -0.4906 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.36 |  | 1013.7552 | 1.6379 | 1023.33 | 979.08 | 1.8343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.32 |  | 476.7783 | -0.0961 | 480 | 472.33 | 0.8965 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 143.515 |  | 143.9391 | -0.2947 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.43 |  | 176.7543 | -0.1835 | 177.84 | 173.19 | 2.0858 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.08 |  | 317.9614 | -1.5352 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 837.51 |  | 857.5261 | -2.3342 | 880.26 | 833 | 0.1528 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 407.63 |  | 408.313 | -0.1673 | 408.58 | 397.9 | 0.5839 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 113.09 |  | 114.6018 | -1.3192 | 118.01 | 108.505 | 0.3802 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 324.82 |  | 327.7074 | -0.8811 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1793.63 |  | 1803.6615 | -0.5562 | 1806.11 | 1780.9 | 0.0719 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.715 |  | 565.6973 | -1.2343 | 566.18 | 548.47 | 4.19 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.735 |  | 320.91 | -0.9894 | 322.4 | 317.27 | 0.085 | below_vwap | below_vwap |
| KLAC | semiconductor_equipment | 214.03 |  | 215.6135 | -0.7344 | 217.88 | 212.99 | 1.8502 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371 |  | 372.2429 | -0.3339 | 376.78 | 363.37 | 3.8383 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 288.54 |  | 294.3821 | -1.9845 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.68 |  | 65.2549 | -0.881 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.15 |  | 54.5517 | -0.7363 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.11 |  | 135.2444 | -0.8388 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.335 |  | 507.4491 | -0.4166 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.16 |  | 295.7991 | -0.2161 | 299.26 | 295.795 | 0.8131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.94 |  | 30.0594 | -0.3972 | 31.13 | 29.12 | 0.0668 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.84 |  | 41.7011 | -2.0649 | 43.21 | 40.51 | 0.0735 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.07 |  | 24.0692 | 0.0031 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| SNDK | memory_hbm_storage | 1667.935 |  | 1642.1587 | 1.5697 | 1651.355 | 1560 | 1.7986 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 564.45 |  | 564.3209 | 0.0229 | 576.24 | 556.3 | 1.1108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 922.155 |  | 924.6486 | -0.2697 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.28 |  | 234.3527 | -0.031 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.075 |  | 604.2975 | 0.2941 | 614.15 | 605.39 | 0.8943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.94 |  | 279.6804 | 0.0928 | 283 | 276.24 | 1.2467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 172.92 |  | 173.6036 | -0.3938 | 177.88 | 168.18 | 1.492 | below_vwap | below_vwap,spread_too_wide |
