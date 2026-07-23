# Intraday State

- Generated at: `2026-07-24T01:56:35+08:00`
- Market time ET: `2026-07-23T13:56:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 14, 'watch_only': 4, 'below_vwap': 27, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 7, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.46 |  | 693.0795 | -0.2337 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.87 |  | 550.9188 | -0.5534 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.77 |  | 581.1187 | -0.5763 | 585.98 | 576.635 | 0.064 | below_vwap | below_vwap |
| SPY | market_regime | 737.57 |  | 738.7574 | -0.1607 | 742.515 | 738.54 | 0.0203 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.79 |  | 31.7029 | 0.2746 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.79 |  | 31.7029 | 0.2746 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 209.25 |  | 208.581 | 0.3207 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 3 | WDC | memory_hbm_storage | 565.25 |  | 564.3189 | 0.165 | 576.24 | 556.3 | 0.2406 | watch_only | none |
| 4 | APLD | high_beta_ai_infrastructure | 30.07 |  | 30.0604 | 0.0319 | 31.13 | 29.12 | 0.0665 | watch_only | none |
| 5 | CIEN | ai_networking_optical | 408.95 |  | 408.3221 | 0.1538 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 177.09 |  | 176.7535 | 0.1904 | 177.84 | 173.19 | 1.8522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ARM | ai_accelerator | 280.495 |  | 279.6769 | 0.2925 | 283 | 276.24 | 1.1622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | CORZ | high_beta_ai_infrastructure | 24.18 |  | 24.0683 | 0.4639 | 24.46 | 23.265 | 0.0827 | watch_only | none |
| 9 | MU | memory_hbm_storage | 995.31 |  | 991.679 | 0.3661 | 999.04 | 964.86 | 1.1052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | META | cloud_ai_capex | 606.615 |  | 604.2313 | 0.3945 | 614.15 | 605.39 | 1.3188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SMH | semiconductor_index | 577.77 |  | 581.1187 | -0.5763 | 585.98 | 576.635 | 0.064 | below_vwap | below_vwap |
| 12 | SOXX | semiconductor_index | 547.87 |  | 550.9188 | -0.5534 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 391.11 |  | 392.435 | -0.3376 | 397.34 | 390.54 | 0.1227 | below_vwap | below_vwap |
| 14 | IWM | market_regime | 291.16 |  | 291.6646 | -0.173 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 15 | HPE | ai_server_oem | 48.25 |  | 48.3548 | -0.2168 | 48.88 | 47.635 | 0.1036 | below_vwap | below_vwap |
| 16 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | IREN | high_beta_ai_infrastructure | 41.07 |  | 41.7127 | -1.5408 | 43.21 | 40.51 | 0.073 | below_vwap | below_vwap |
| 19 | ASML | semiconductor_equipment | 1796.985 |  | 1803.8628 | -0.3813 | 1806.11 | 1780.9 | 0.1753 | below_vwap | below_vwap |
| 20 | AAPL | mega_cap_platform | 320.91 |  | 321.1032 | -0.0602 | 323.25 | 320.82 | 0.0156 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.79 |  | 31.7029 | 0.2746 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1031.455 |  | 1013.6163 | 1.7599 | 1023.33 | 979.08 | 0.8299 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | CIEN | ai_networking_optical | 408.95 |  | 408.3221 | 0.1538 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | SNDK | memory_hbm_storage | 1673.29 |  | 1641.7706 | 1.9198 | 1651.355 | 1560 | 1.316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.25 |  | 208.581 | 0.3207 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | WDC | memory_hbm_storage | 565.25 |  | 564.3189 | 0.165 | 576.24 | 556.3 | 0.2406 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 24.18 |  | 24.0683 | 0.4639 | 24.46 | 23.265 | 0.0827 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 30.07 |  | 30.0604 | 0.0319 | 31.13 | 29.12 | 0.0665 | watch_only | none |
| 9 | TSM | foundry | 415.65 |  | 416.7145 | -0.2555 | 420.72 | 412.69 | 0.9118 | below_vwap | below_vwap,spread_too_wide |
| 10 | SMH | semiconductor_index | 577.77 |  | 581.1187 | -0.5763 | 585.98 | 576.635 | 0.064 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 547.87 |  | 550.9188 | -0.5534 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 391.11 |  | 392.435 | -0.3376 | 397.34 | 390.54 | 0.1227 | below_vwap | below_vwap |
| 13 | ASML | semiconductor_equipment | 1796.985 |  | 1803.8628 | -0.3813 | 1806.11 | 1780.9 | 0.1753 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 559.12 |  | 565.7908 | -1.179 | 566.18 | 548.47 | 4.5894 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 476.24 |  | 476.7954 | -0.1165 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 143.58 |  | 143.9498 | -0.2569 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 648.89 |  | 651.947 | -0.4689 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 213.97 |  | 215.6589 | -0.7832 | 217.88 | 212.99 | 1.8975 | below_vwap | below_vwap,spread_too_wide |
| 19 | ETN | data_center_power_cooling | 412.38 |  | 413.3878 | -0.2438 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | IWM | market_regime | 291.16 |  | 291.6646 | -0.173 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.46 |  | 693.0795 | -0.2337 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.16 |  | 66.5639 | -0.6068 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.25 |  | 208.581 | 0.3207 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.335 |  | 382.6465 | -0.3428 | 391.71 | 387.245 | 0.333 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.91 |  | 321.1032 | -0.0602 | 323.25 | 320.82 | 0.0156 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 319.37 |  | 319.5514 | -0.0568 | 324.42 | 320.24 | 0.1002 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.655 |  | 540.7319 | -0.9389 | 556.12 | 542.33 | 2.8003 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.65 |  | 416.7145 | -0.2555 | 420.72 | 412.69 | 0.9118 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.87 |  | 550.9188 | -0.5534 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.77 |  | 581.1187 | -0.5763 | 585.98 | 576.635 | 0.064 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.11 |  | 392.435 | -0.3376 | 397.34 | 390.54 | 0.1227 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 995.31 |  | 991.679 | 0.3661 | 999.04 | 964.86 | 1.1052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 206.96 |  | 209.7132 | -1.3128 | 213.785 | 207.665 | 0.3334 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 441.81 |  | 444.0131 | -0.4962 | 450.07 | 438.55 | 0.9348 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.25 |  | 48.3548 | -0.2168 | 48.88 | 47.635 | 0.1036 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.79 |  | 31.7029 | 0.2746 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 737.57 |  | 738.7574 | -0.1607 | 742.515 | 738.54 | 0.0203 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.16 |  | 291.6646 | -0.173 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.36 |  | 121.9486 | -1.3026 | 124.22 | 122.07 | 0.2326 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.37 |  | 82.8397 | -0.567 | 84.415 | 80.64 | 0.4128 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.36 |  | 306.2567 | -0.9458 | 311.13 | 303.96 | 1.3021 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.38 |  | 413.3878 | -0.2438 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 648.89 |  | 651.947 | -0.4689 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1031.455 |  | 1013.6163 | 1.7599 | 1023.33 | 979.08 | 0.8299 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.24 |  | 476.7954 | -0.1165 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.58 |  | 143.9498 | -0.2569 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.09 |  | 176.7535 | 0.1904 | 177.84 | 173.19 | 1.8522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 313.965 |  | 318.0849 | -1.2952 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 838.21 |  | 857.7951 | -2.2832 | 880.26 | 833 | 3.7127 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 408.95 |  | 408.3221 | 0.1538 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 113.49 |  | 114.6215 | -0.9872 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 325.16 |  | 327.7526 | -0.791 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.985 |  | 1803.8628 | -0.3813 | 1806.11 | 1780.9 | 0.1753 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.12 |  | 565.7908 | -1.179 | 566.18 | 548.47 | 4.5894 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.645 |  | 321.0531 | -1.0615 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 213.97 |  | 215.6589 | -0.7832 | 217.88 | 212.99 | 1.8975 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.63 |  | 372.2764 | -0.4422 | 376.78 | 363.37 | 3.7747 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 289.1 |  | 294.4904 | -1.8304 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.96 |  | 65.2798 | -0.4899 | 67.455 | 65.81 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.18 |  | 54.5671 | -0.7093 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.54 |  | 135.3198 | -0.5763 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.71 |  | 507.4674 | -0.3463 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.195 |  | 295.8511 | -0.2218 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.07 |  | 30.0604 | 0.0319 | 31.13 | 29.12 | 0.0665 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.07 |  | 41.7127 | -1.5408 | 43.21 | 40.51 | 0.073 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.18 |  | 24.0683 | 0.4639 | 24.46 | 23.265 | 0.0827 | watch_only | none |
| SNDK | memory_hbm_storage | 1673.29 |  | 1641.7706 | 1.9198 | 1651.355 | 1560 | 1.316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 565.25 |  | 564.3189 | 0.165 | 576.24 | 556.3 | 0.2406 | watch_only | none |
| STX | memory_hbm_storage | 922.78 |  | 924.6806 | -0.2055 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.24 |  | 234.3544 | -0.0488 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.615 |  | 604.2313 | 0.3945 | 614.15 | 605.39 | 1.3188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 280.495 |  | 279.6769 | 0.2925 | 283 | 276.24 | 1.1622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.475 |  | 173.6133 | -0.0797 | 177.88 | 168.18 | 1.0664 | below_vwap | below_vwap,spread_too_wide |
