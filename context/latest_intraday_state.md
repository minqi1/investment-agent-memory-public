# Intraday State

- Generated at: `2026-07-23T21:59:04+08:00`
- Market time ET: `2026-07-23T09:59:05-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'watch_only': 10, 'below_opening_15m_low': 2, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 21, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.24 |  | 696.3303 | -0.1566 | 698.65 | 693.24 | 0.0834 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 553.68 |  | 553.4956 | 0.0333 | 557.38 | 545.965 | 0.13 | watch_only | none |
| SMH | semiconductor_index | 582.775 |  | 582.32 | 0.0781 | 585.98 | 576.635 | 0.0961 | watch_only | none |
| SPY | market_regime | 739.83 |  | 740.7585 | -0.1253 | 742.515 | 738.54 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.725 |  | 31.1882 | 1.7213 | 31.52 | 30.23 | 0.0946 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 418.76 |  | 417.8843 | 0.2095 | 420.72 | 412.69 | 0.117 | watch_only | none |
| 2 | SMH | semiconductor_index | 582.775 |  | 582.32 | 0.0781 | 585.98 | 576.635 | 0.0961 | watch_only | none |
| 3 | SOXX | semiconductor_index | 553.68 |  | 553.4956 | 0.0333 | 557.38 | 545.965 | 0.13 | watch_only | none |
| 4 | HPE | ai_server_oem | 48.565 |  | 48.5192 | 0.0944 | 48.88 | 47.635 | 0.1441 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 389.26 |  | 389.024 | 0.0607 | 391.71 | 387.245 | 0.0745 | watch_only | none |
| 6 | AMD | ai_accelerator | 550.26 |  | 550.2537 | 0.0011 | 556.12 | 542.33 | 0.1654 | watch_only | none |
| 7 | MRVL | custom_silicon_networking | 212.32 |  | 211.9407 | 0.179 | 213.785 | 207.665 | 0.2402 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 124.14 |  | 123.408 | 0.5931 | 124.22 | 122.07 | 0.0644 | watch_only | none |
| 9 | TT | data_center_power_cooling | 476.97 |  | 476.8209 | 0.0313 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | GEV | data_center_power_cooling | 1014.74 |  | 1005.2071 | 0.9484 | 1023.33 | 979.08 | 0.3321 | watch_only | none |
| 11 | SMCI | ai_server_oem | 31.725 |  | 31.1882 | 1.7213 | 31.52 | 30.23 | 0.0946 | buy_precheck_manual_confirm | none |
| 12 | AVGO | custom_silicon_networking | 394.22 |  | 394.1858 | 0.0087 | 397.34 | 390.54 | 0.761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ASML | semiconductor_equipment | 1802.99 |  | 1797.9055 | 0.2828 | 1806.11 | 1780.9 | 0.6256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 310.45 |  | 308.0429 | 0.7814 | 311.13 | 303.96 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ETN | data_center_power_cooling | 414.38 |  | 412.6548 | 0.4181 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ARM | ai_accelerator | 280.895 |  | 280.1066 | 0.2815 | 283 | 276.24 | 1.958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ENTG | semiconductor_materials | 137.8 |  | 137.0245 | 0.5659 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 928.41 |  | 926.9323 | 0.1594 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 656.725 |  | 653.2545 | 0.5313 | 656.38 | 642.37 | 4.4052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMAT | semiconductor_equipment | 563.76 |  | 561.1492 | 0.4653 | 566.18 | 548.47 | 4.9489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.725 |  | 31.1882 | 1.7213 | 31.52 | 30.23 | 0.0946 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 178.535 |  | 177.2779 | 0.7091 | 177.84 | 173.19 | 1.3947 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | PWR | data_center_power_cooling | 656.725 |  | 653.2545 | 0.5313 | 656.38 | 642.37 | 4.4052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | TSM | foundry | 418.76 |  | 417.8843 | 0.2095 | 420.72 | 412.69 | 0.117 | watch_only | none |
| 5 | COHR | ai_networking_optical | 324.16 |  | 318.4132 | 1.8048 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | CIEN | ai_networking_optical | 413.25 |  | 405.0999 | 2.0119 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | LITE | ai_networking_optical | 889.01 |  | 872.1654 | 1.9313 | 880.26 | 833 | 3.9831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SMH | semiconductor_index | 582.775 |  | 582.32 | 0.0781 | 585.98 | 576.635 | 0.0961 | watch_only | none |
| 9 | SOXX | semiconductor_index | 553.68 |  | 553.4956 | 0.0333 | 557.38 | 545.965 | 0.13 | watch_only | none |
| 10 | AMD | ai_accelerator | 550.26 |  | 550.2537 | 0.0011 | 556.12 | 542.33 | 0.1654 | watch_only | none |
| 11 | GEV | data_center_power_cooling | 1014.74 |  | 1005.2071 | 0.9484 | 1023.33 | 979.08 | 0.3321 | watch_only | none |
| 12 | HPE | ai_server_oem | 48.565 |  | 48.5192 | 0.0944 | 48.88 | 47.635 | 0.1441 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 389.26 |  | 389.024 | 0.0607 | 391.71 | 387.245 | 0.0745 | watch_only | none |
| 14 | MRVL | custom_silicon_networking | 212.32 |  | 211.9407 | 0.179 | 213.785 | 207.665 | 0.2402 | watch_only | none |
| 15 | ORCL | cloud_ai_capex | 124.14 |  | 123.408 | 0.5931 | 124.22 | 122.07 | 0.0644 | watch_only | none |
| 16 | AAOI | ai_networking_optical | 117.89 |  | 115.9699 | 1.6557 | 118.01 | 108.505 | 0.3308 | watch_only | none |
| 17 | NVDA | ai_accelerator | 209.21 |  | 209.4273 | -0.1038 | 210.85 | 208.49 | 0.1099 | below_vwap | below_vwap |
| 18 | MU | memory_hbm_storage | 979.705 |  | 985.9229 | -0.6307 | 999.04 | 964.86 | 2.3272 | below_vwap | below_vwap,spread_too_wide |
| 19 | JCI | data_center_power_cooling | 143.97 |  | 144.0364 | -0.0461 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 215.04 |  | 216.1085 | -0.4944 | 217.88 | 212.99 | 0.1628 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.24 |  | 696.3303 | -0.1566 | 698.65 | 693.24 | 0.0834 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.21 |  | 67.4859 | -0.4088 | 68.245 | 66.7 | 0.0298 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 209.21 |  | 209.4273 | -0.1038 | 210.85 | 208.49 | 0.1099 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 389.26 |  | 389.024 | 0.0607 | 391.71 | 387.245 | 0.0745 | watch_only | none |
| AAPL | mega_cap_platform | 319.84 |  | 321.203 | -0.4243 | 323.25 | 320.82 | 0.0594 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.93 |  | 321.1749 | -0.0762 | 324.42 | 320.24 | 0.0499 | below_vwap | below_vwap |
| AMD | ai_accelerator | 550.26 |  | 550.2537 | 0.0011 | 556.12 | 542.33 | 0.1654 | watch_only | none |
| TSM | foundry | 418.76 |  | 417.8843 | 0.2095 | 420.72 | 412.69 | 0.117 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.68 |  | 553.4956 | 0.0333 | 557.38 | 545.965 | 0.13 | watch_only | none |
| SMH | semiconductor_index | 582.775 |  | 582.32 | 0.0781 | 585.98 | 576.635 | 0.0961 | watch_only | none |
| AVGO | custom_silicon_networking | 394.22 |  | 394.1858 | 0.0087 | 397.34 | 390.54 | 0.761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 979.705 |  | 985.9229 | -0.6307 | 999.04 | 964.86 | 2.3272 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 212.32 |  | 211.9407 | 0.179 | 213.785 | 207.665 | 0.2402 | watch_only | none |
| DELL | ai_server_oem | 442.37 |  | 443.7219 | -0.3047 | 450.07 | 438.55 | 0.6149 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.565 |  | 48.5192 | 0.0944 | 48.88 | 47.635 | 0.1441 | watch_only | none |
| SMCI | ai_server_oem | 31.725 |  | 31.1882 | 1.7213 | 31.52 | 30.23 | 0.0946 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.83 |  | 740.7585 | -0.1253 | 742.515 | 738.54 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 291.615 |  | 291.8859 | -0.0928 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.14 |  | 123.408 | 0.5931 | 124.22 | 122.07 | 0.0644 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 83.62 |  | 83.1715 | 0.5392 | 84.415 | 80.64 | 4.1617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 310.45 |  | 308.0429 | 0.7814 | 311.13 | 303.96 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 414.38 |  | 412.6548 | 0.4181 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 656.725 |  | 653.2545 | 0.5313 | 656.38 | 642.37 | 4.4052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1014.74 |  | 1005.2071 | 0.9484 | 1023.33 | 979.08 | 0.3321 | watch_only | none |
| TT | data_center_power_cooling | 476.97 |  | 476.8209 | 0.0313 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.97 |  | 144.0364 | -0.0461 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 178.535 |  | 177.2779 | 0.7091 | 177.84 | 173.19 | 1.3947 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 324.16 |  | 318.4132 | 1.8048 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 889.01 |  | 872.1654 | 1.9313 | 880.26 | 833 | 3.9831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 413.25 |  | 405.0999 | 2.0119 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 117.89 |  | 115.9699 | 1.6557 | 118.01 | 108.505 | 0.3308 | watch_only | none |
| ALAB | ai_networking_optical | 340.41 |  | 335.2505 | 1.539 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1802.99 |  | 1797.9055 | 0.2828 | 1806.11 | 1780.9 | 0.6256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 563.76 |  | 561.1492 | 0.4653 | 566.18 | 548.47 | 4.9489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320 |  | 320.4439 | -0.1385 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.04 |  | 216.1085 | -0.4944 | 217.88 | 212.99 | 0.1628 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 375.25 |  | 372.6649 | 0.6937 | 376.78 | 363.37 | 4.2292 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 300.6 |  | 299.2318 | 0.4573 | 301.305 | 293.685 | 1.0313 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 67.33 |  | 66.686 | 0.9658 | 67.455 | 65.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.195 |  | 54.8181 | 0.6875 | 55.195 | 54.445 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.8 |  | 137.0245 | 0.5659 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.61 |  | 344.6698 | 0.853 | 347.68 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.65 |  | 506.9467 | -0.0585 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 296.85 |  | 297.5261 | -0.2272 | 299.26 | 295.795 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| APLD | high_beta_ai_infrastructure | 30.47 |  | 30.3918 | 0.2575 | 31.13 | 29.12 | 3.7742 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 42.2 |  | 42.3186 | -0.2802 | 43.21 | 40.51 | 0.0711 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.055 |  | 24.1014 | -0.1924 | 24.46 | 23.265 | 0.1663 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1612.025 |  | 1618.6645 | -0.4102 | 1651.355 | 1560 | 3.2258 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 563.88 |  | 569.8703 | -1.0512 | 576.24 | 556.3 | 2.8197 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 928.41 |  | 926.9323 | 0.1594 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 235.59 |  | 236.7673 | -0.4972 | 238.285 | 235.71 | 0.034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 610.045 |  | 610.275 | -0.0377 | 614.15 | 605.39 | 1.4196 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 280.895 |  | 280.1066 | 0.2815 | 283 | 276.24 | 1.958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.5 |  | 174.0297 | -0.3044 | 177.88 | 168.18 | 0.5303 | below_vwap | below_vwap,spread_too_wide |
