# Intraday State

- Generated at: `2026-07-24T02:08:14+08:00`
- Market time ET: `2026-07-23T14:08:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 20, 'below_vwap': 31, 'price_stale_or_missing': 2, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.53 |  | 693.0373 | -0.3618 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.78 |  | 550.9004 | -0.7479 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.18 |  | 580.9327 | -0.8181 | 585.98 | 576.635 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.87 |  | 738.738 | -0.2529 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1029.725 |  | 1013.8416 | 1.5667 | 1023.33 | 979.08 | 0.1699 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | META | cloud_ai_capex | 606.425 |  | 604.3097 | 0.35 | 614.15 | 605.39 | 0.2243 | watch_only | none |
| 2 | GEV | data_center_power_cooling | 1029.725 |  | 1013.8416 | 1.5667 | 1023.33 | 979.08 | 0.1699 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 319.84 |  | 319.5528 | 0.0899 | 324.42 | 320.24 | 0.075 | below_opening_15m_low | below_opening_15m_low |
| 4 | SOXX | semiconductor_index | 546.78 |  | 550.9004 | -0.7479 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| 5 | ASML | semiconductor_equipment | 1790.97 |  | 1803.5905 | -0.6997 | 1806.11 | 1780.9 | 0.0402 | below_vwap | below_vwap |
| 6 | IWM | market_regime | 290.96 |  | 291.6549 | -0.2383 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 7 | HPE | ai_server_oem | 47.665 |  | 48.3338 | -1.3837 | 48.88 | 47.635 | 0.0629 | below_vwap | below_vwap |
| 8 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 9 | SMCI | ai_server_oem | 30.875 |  | 31.6815 | -2.5455 | 31.52 | 30.23 | 0.0324 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | IREN | high_beta_ai_infrastructure | 40.92 |  | 41.6879 | -1.842 | 43.21 | 40.51 | 0.0733 | below_vwap | below_vwap |
| 12 | SNDK | memory_hbm_storage | 1658.725 |  | 1642.3192 | 0.9989 | 1651.355 | 1560 | 2.652 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | JCI | data_center_power_cooling | 143.58 |  | 143.927 | -0.2411 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 647.99 |  | 651.8898 | -0.5982 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ETN | data_center_power_cooling | 412.31 |  | 413.3757 | -0.2578 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LRCX | semiconductor_equipment | 317.51 |  | 320.847 | -1.0401 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 279.33 |  | 279.679 | -0.1248 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 505.64 |  | 507.427 | -0.3522 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHR | ai_networking_optical | 312.5 |  | 317.9143 | -1.7031 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHU | semiconductor_test_packaging | 54.11 |  | 54.5411 | -0.7904 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1029.725 |  | 1013.8416 | 1.5667 | 1023.33 | 979.08 | 0.1699 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1658.725 |  | 1642.3192 | 0.9989 | 1651.355 | 1560 | 2.652 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | META | cloud_ai_capex | 606.425 |  | 604.3097 | 0.35 | 614.15 | 605.39 | 0.2243 | watch_only | none |
| 4 | TSM | foundry | 414.57 |  | 416.6602 | -0.5017 | 420.72 | 412.69 | 0.4824 | below_vwap | below_vwap,spread_too_wide |
| 5 | SOXX | semiconductor_index | 546.78 |  | 550.9004 | -0.7479 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 989.4 |  | 991.7272 | -0.2347 | 999.04 | 964.86 | 0.9511 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1790.97 |  | 1803.5905 | -0.6997 | 1806.11 | 1780.9 | 0.0402 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 558.035 |  | 565.6117 | -1.3396 | 566.18 | 548.47 | 4.7363 | below_vwap | below_vwap,spread_too_wide |
| 9 | TT | data_center_power_cooling | 476.57 |  | 476.7708 | -0.0421 | 480 | 472.33 | 0.917 | below_vwap | below_vwap,spread_too_wide |
| 10 | ANET | ai_networking_optical | 175.87 |  | 176.752 | -0.499 | 177.84 | 173.19 | 3.1273 | below_vwap | below_vwap,spread_too_wide |
| 11 | JCI | data_center_power_cooling | 143.58 |  | 143.927 | -0.2411 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 647.99 |  | 651.8898 | -0.5982 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 213.73 |  | 215.5913 | -0.8633 | 217.88 | 212.99 | 3.4296 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 412.31 |  | 413.3757 | -0.2578 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | IWM | market_regime | 290.96 |  | 291.6549 | -0.2383 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 317.51 |  | 320.847 | -1.0401 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ARM | ai_accelerator | 279.33 |  | 279.679 | -0.1248 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 561.86 |  | 564.3149 | -0.435 | 576.24 | 556.3 | 4.7005 | below_vwap | below_vwap,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 505.64 |  | 507.427 | -0.3522 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.53 |  | 693.0373 | -0.3618 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.835 |  | 66.5561 | -1.0834 | 68.245 | 66.7 | 0.0304 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.34 |  | 208.5906 | -0.1201 | 210.85 | 208.49 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.14 |  | 382.6144 | -0.3854 | 391.71 | 387.245 | 0.2676 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.1 |  | 321.0806 | -0.3054 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.84 |  | 319.5528 | 0.0899 | 324.42 | 320.24 | 0.075 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 533.06 |  | 540.5425 | -1.3843 | 556.12 | 542.33 | 1.497 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.57 |  | 416.6602 | -0.5017 | 420.72 | 412.69 | 0.4824 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.78 |  | 550.9004 | -0.7479 | 557.38 | 545.965 | 0.0677 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.18 |  | 580.9327 | -0.8181 | 585.98 | 576.635 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 389.33 |  | 392.3212 | -0.7624 | 397.34 | 390.54 | 1.1789 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 989.4 |  | 991.7272 | -0.2347 | 999.04 | 964.86 | 0.9511 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.23 |  | 209.6443 | -1.6286 | 213.785 | 207.665 | 0.1406 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.41 |  | 443.8505 | -1.4511 | 450.07 | 438.55 | 0.3201 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 47.665 |  | 48.3338 | -1.3837 | 48.88 | 47.635 | 0.0629 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.875 |  | 31.6815 | -2.5455 | 31.52 | 30.23 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 736.87 |  | 738.738 | -0.2529 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.96 |  | 291.6549 | -0.2383 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.935 |  | 121.9028 | -1.6143 | 124.22 | 122.07 | 0.0834 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.56 |  | 82.7924 | -1.4886 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.23 |  | 306.1893 | -1.2931 | 311.13 | 303.96 | 0.3838 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.31 |  | 413.3757 | -0.2578 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 647.99 |  | 651.8898 | -0.5982 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1029.725 |  | 1013.8416 | 1.5667 | 1023.33 | 979.08 | 0.1699 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 476.57 |  | 476.7708 | -0.0421 | 480 | 472.33 | 0.917 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 143.58 |  | 143.927 | -0.2411 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.87 |  | 176.752 | -0.499 | 177.84 | 173.19 | 3.1273 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 312.5 |  | 317.9143 | -1.7031 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 833.825 |  | 857.3064 | -2.739 | 880.26 | 833 | 0.6884 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 406.33 |  | 408.305 | -0.4837 | 408.58 | 397.9 | 4.4053 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.56 |  | 114.5944 | -1.7753 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.82 |  | 327.7074 | -0.8811 | 341.68 | 327.43 | 4.3809 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1790.97 |  | 1803.5905 | -0.6997 | 1806.11 | 1780.9 | 0.0402 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.035 |  | 565.6117 | -1.3396 | 566.18 | 548.47 | 4.7363 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.51 |  | 320.847 | -1.0401 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 213.73 |  | 215.5913 | -0.8633 | 217.88 | 212.99 | 3.4296 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 369.97 |  | 372.2271 | -0.6064 | 376.78 | 363.37 | 4.0544 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 288.17 |  | 294.3344 | -2.0944 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.67 |  | 65.2417 | -0.8763 | 67.455 | 65.81 | 4.5616 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.11 |  | 54.5411 | -0.7904 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.96 |  | 135.2301 | -0.9392 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.64 |  | 507.427 | -0.3522 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.14 |  | 295.7778 | -0.2156 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.9 |  | 30.0589 | -0.5286 | 31.13 | 29.12 | 0.6689 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.92 |  | 41.6879 | -1.842 | 43.21 | 40.51 | 0.0733 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.06 |  | 24.0692 | -0.0384 | 24.46 | 23.265 | 0.0416 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1658.725 |  | 1642.3192 | 0.9989 | 1651.355 | 1560 | 2.652 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 561.86 |  | 564.3149 | -0.435 | 576.24 | 556.3 | 4.7005 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.82 |  | 924.5525 | -0.5119 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.255 |  | 234.3523 | -0.0415 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.425 |  | 604.3097 | 0.35 | 614.15 | 605.39 | 0.2243 | watch_only | none |
| ARM | ai_accelerator | 279.33 |  | 279.679 | -0.1248 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 171.77 |  | 173.589 | -1.0479 | 177.88 | 168.18 | 2.2123 | below_vwap | below_vwap,spread_too_wide |
