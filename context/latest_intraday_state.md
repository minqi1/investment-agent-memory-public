# Intraday State

- Generated at: `2026-07-24T01:52:42+08:00`
- Market time ET: `2026-07-23T13:52:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 14, 'watch_only': 6, 'below_vwap': 27, 'price_stale_or_missing': 2, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.91 |  | 693.0826 | -0.1692 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.16 |  | 550.9273 | -0.3208 | 557.38 | 545.965 | 0.0692 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.02 |  | 581.1235 | -0.362 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| SPY | market_regime | 737.93 |  | 738.761 | -0.1125 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.775 |  | 31.7025 | 0.2287 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.775 |  | 31.7025 | 0.2287 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 994.99 |  | 991.6552 | 0.3363 | 999.04 | 964.86 | 0.1106 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 321.29 |  | 321.1038 | 0.058 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| 4 | WDC | memory_hbm_storage | 566.05 |  | 564.3107 | 0.3082 | 576.24 | 556.3 | 0.2297 | watch_only | none |
| 5 | NVDA | ai_accelerator | 209.59 |  | 208.5766 | 0.4858 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | APLD | high_beta_ai_infrastructure | 30.085 |  | 30.0603 | 0.0821 | 31.13 | 29.12 | 0.0997 | watch_only | none |
| 7 | CIEN | ai_networking_optical | 409.13 |  | 408.3033 | 0.2025 | 408.58 | 397.9 | 3.9254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 177.27 |  | 176.7504 | 0.294 | 177.84 | 173.19 | 1.6134 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ARM | ai_accelerator | 281.1 |  | 279.664 | 0.5135 | 283 | 276.24 | 0.6901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | META | cloud_ai_capex | 606.99 |  | 604.1857 | 0.4641 | 614.15 | 605.39 | 1.318 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | AMZN | cloud_ai_capex | 234.37 |  | 234.3546 | 0.0066 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 12 | CORZ | high_beta_ai_infrastructure | 24.29 |  | 24.0677 | 0.9236 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| 13 | SMH | semiconductor_index | 579.02 |  | 581.1235 | -0.362 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| 14 | SOXX | semiconductor_index | 549.16 |  | 550.9273 | -0.3208 | 557.38 | 545.965 | 0.0692 | below_vwap | below_vwap |
| 15 | KLAC | semiconductor_equipment | 214.37 |  | 215.6762 | -0.6056 | 217.88 | 212.99 | 0.0746 | below_vwap | below_vwap |
| 16 | IWM | market_regime | 291.245 |  | 291.6667 | -0.1446 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | HPE | ai_server_oem | 48.31 |  | 48.3552 | -0.0936 | 48.88 | 47.635 | 0.0414 | below_vwap | below_vwap |
| 18 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 19 | GEV | data_center_power_cooling | 1028.16 |  | 1013.6061 | 1.4359 | 1023.33 | 979.08 | 1.9365 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.775 |  | 31.7025 | 0.2287 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1028.16 |  | 1013.6061 | 1.4359 | 1023.33 | 979.08 | 1.9365 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | CIEN | ai_networking_optical | 409.13 |  | 408.3033 | 0.2025 | 408.58 | 397.9 | 3.9254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1671.27 |  | 1641.6849 | 1.8021 | 1651.355 | 1560 | 4.4278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.59 |  | 208.5766 | 0.4858 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | MU | memory_hbm_storage | 994.99 |  | 991.6552 | 0.3363 | 999.04 | 964.86 | 0.1106 | watch_only | none |
| 7 | WDC | memory_hbm_storage | 566.05 |  | 564.3107 | 0.3082 | 576.24 | 556.3 | 0.2297 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 321.29 |  | 321.1038 | 0.058 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.29 |  | 24.0677 | 0.9236 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 30.085 |  | 30.0603 | 0.0821 | 31.13 | 29.12 | 0.0997 | watch_only | none |
| 11 | TSM | foundry | 416.34 |  | 416.7187 | -0.0909 | 420.72 | 412.69 | 0.4852 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMH | semiconductor_index | 579.02 |  | 581.1235 | -0.362 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| 13 | SOXX | semiconductor_index | 549.16 |  | 550.9273 | -0.3208 | 557.38 | 545.965 | 0.0692 | below_vwap | below_vwap |
| 14 | AVGO | custom_silicon_networking | 391.275 |  | 392.4713 | -0.3048 | 397.34 | 390.54 | 1.2089 | below_vwap | below_vwap,spread_too_wide |
| 15 | ASML | semiconductor_equipment | 1797.365 |  | 1803.9436 | -0.3647 | 1806.11 | 1780.9 | 0.1619 | below_vwap | below_vwap |
| 16 | AMAT | semiconductor_equipment | 559.6 |  | 565.9314 | -1.1188 | 566.18 | 548.47 | 0.8738 | below_vwap | below_vwap,spread_too_wide |
| 17 | TT | data_center_power_cooling | 476.41 |  | 476.8003 | -0.0819 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 143.71 |  | 143.9554 | -0.1705 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 649.33 |  | 651.9835 | -0.407 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 214.37 |  | 215.6762 | -0.6056 | 217.88 | 212.99 | 0.0746 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.91 |  | 693.0826 | -0.1692 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.3 |  | 66.5659 | -0.3994 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.59 |  | 208.5766 | 0.4858 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.2 |  | 382.6573 | -0.3808 | 391.71 | 387.245 | 0.0367 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.29 |  | 321.1038 | 0.058 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| GOOGL | cloud_ai_capex | 319.26 |  | 319.5522 | -0.0914 | 324.42 | 320.24 | 0.094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.92 |  | 540.7561 | -0.8943 | 556.12 | 542.33 | 2.4798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 416.34 |  | 416.7187 | -0.0909 | 420.72 | 412.69 | 0.4852 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.16 |  | 550.9273 | -0.3208 | 557.38 | 545.965 | 0.0692 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.02 |  | 581.1235 | -0.362 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.275 |  | 392.4713 | -0.3048 | 397.34 | 390.54 | 1.2089 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 994.99 |  | 991.6552 | 0.3363 | 999.04 | 964.86 | 0.1106 | watch_only | none |
| MRVL | custom_silicon_networking | 207.74 |  | 209.7277 | -0.9478 | 213.785 | 207.665 | 0.1685 | below_vwap | below_vwap |
| DELL | ai_server_oem | 443.02 |  | 444.0264 | -0.2267 | 450.07 | 438.55 | 0.3205 | below_vwap | below_vwap |
| HPE | ai_server_oem | 48.31 |  | 48.3552 | -0.0936 | 48.88 | 47.635 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.775 |  | 31.7025 | 0.2287 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 737.93 |  | 738.761 | -0.1125 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.245 |  | 291.6667 | -0.1446 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.35 |  | 121.9542 | -1.3154 | 124.22 | 122.07 | 0.0914 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.54 |  | 82.8415 | -0.3639 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.085 |  | 306.262 | -1.0373 | 311.13 | 303.96 | 1.3033 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.66 |  | 413.3901 | -0.1766 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 649.33 |  | 651.9835 | -0.407 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.16 |  | 1013.6061 | 1.4359 | 1023.33 | 979.08 | 1.9365 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.41 |  | 476.8003 | -0.0819 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.71 |  | 143.9554 | -0.1705 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.27 |  | 176.7504 | 0.294 | 177.84 | 173.19 | 1.6134 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.61 |  | 318.1286 | -1.106 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 841.38 |  | 857.8874 | -1.9242 | 880.26 | 833 | 4.6234 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 409.13 |  | 408.3033 | 0.2025 | 408.58 | 397.9 | 3.9254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.425 |  | 114.6262 | -1.048 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.51 |  | 327.7592 | -0.3811 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1797.365 |  | 1803.9436 | -0.3647 | 1806.11 | 1780.9 | 0.1619 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.6 |  | 565.9314 | -1.1188 | 566.18 | 548.47 | 0.8738 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.21 |  | 321.0958 | -0.8987 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.37 |  | 215.6762 | -0.6056 | 217.88 | 212.99 | 0.0746 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 372.12 |  | 372.2816 | -0.0434 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.755 |  | 294.5645 | -1.6327 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.96 |  | 65.2798 | -0.4899 | 67.455 | 65.81 | 4.8337 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.335 |  | 54.5816 | -0.4518 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.66 |  | 135.3223 | -0.4894 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.595 |  | 507.4763 | -0.3707 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.16 |  | 295.8563 | -0.2353 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.085 |  | 30.0603 | 0.0821 | 31.13 | 29.12 | 0.0997 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.25 |  | 41.7159 | -1.1169 | 43.21 | 40.51 | 0.0727 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.29 |  | 24.0677 | 0.9236 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| SNDK | memory_hbm_storage | 1671.27 |  | 1641.6849 | 1.8021 | 1651.355 | 1560 | 4.4278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 566.05 |  | 564.3107 | 0.3082 | 576.24 | 556.3 | 0.2297 | watch_only | none |
| STX | memory_hbm_storage | 923.52 |  | 924.6868 | -0.1262 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.37 |  | 234.3546 | 0.0066 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.99 |  | 604.1857 | 0.4641 | 614.15 | 605.39 | 1.318 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.1 |  | 279.664 | 0.5135 | 283 | 276.24 | 0.6901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.085 |  | 173.6137 | -0.3046 | 177.88 | 168.18 | 0.4333 | below_vwap | below_vwap,spread_too_wide |
