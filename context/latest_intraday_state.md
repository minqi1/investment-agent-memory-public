# Intraday State

- Generated at: `2026-07-23T22:56:56+08:00`
- Market time ET: `2026-07-23T10:56:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 14, 'watch_only': 2, 'below_vwap': 35, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.31 |  | 695.1069 | -0.5462 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.98 |  | 553.7494 | -0.8613 | 557.38 | 545.965 | 0.102 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.61 |  | 582.5765 | -0.6809 | 585.98 | 576.635 | 0.0812 | below_vwap | below_vwap |
| SPY | market_regime | 738.1 |  | 740.089 | -0.2687 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 292.04 |  | 291.9303 | 0.0376 | 293.01 | 290.365 | 0.0137 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 321.24 |  | 321.238 | 0.0006 | 323.25 | 320.82 | 0.0872 | watch_only | none |
| 3 | LIN | industrial_gases | 509.07 |  | 507.309 | 0.3471 | 510.71 | 502.72 | 4.2509 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | APD | industrial_gases | 297.08 |  | 296.8726 | 0.0699 | 299.26 | 295.795 | 0.7708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SNDK | memory_hbm_storage | 1627.72 |  | 1624.3981 | 0.2045 | 1651.355 | 1560 | 0.7784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SMH | semiconductor_index | 578.61 |  | 582.5765 | -0.6809 | 585.98 | 576.635 | 0.0812 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 548.98 |  | 553.7494 | -0.8613 | 557.38 | 545.965 | 0.102 | below_vwap | below_vwap |
| 8 | MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 9 | SMCI | ai_server_oem | 31.215 |  | 31.5807 | -1.158 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | IREN | high_beta_ai_infrastructure | 41.675 |  | 42.327 | -1.5404 | 43.21 | 40.51 | 0.072 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1799.23 |  | 1806.9315 | -0.4262 | 1806.11 | 1780.9 | 0.1567 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 176.06 |  | 177.2586 | -0.6762 | 177.84 | 173.19 | 0.2102 | below_vwap | below_vwap |
| 14 | TT | data_center_power_cooling | 476.49 |  | 476.8352 | -0.0724 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 143.92 |  | 144.1054 | -0.1287 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 652.1 |  | 655.1945 | -0.4723 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ETN | data_center_power_cooling | 413 |  | 413.7924 | -0.1915 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 320.21 |  | 322.1012 | -0.5872 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ARM | ai_accelerator | 277.27 |  | 280.2095 | -1.049 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 315.52 |  | 320.1046 | -1.4322 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 292.04 |  | 291.9303 | 0.0376 | 293.01 | 290.365 | 0.0137 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 321.24 |  | 321.238 | 0.0006 | 323.25 | 320.82 | 0.0872 | watch_only | none |
| 3 | TSM | foundry | 415.79 |  | 418.0962 | -0.5516 | 420.72 | 412.69 | 1.354 | below_vwap | below_vwap,spread_too_wide |
| 4 | SMH | semiconductor_index | 578.61 |  | 582.5765 | -0.6809 | 585.98 | 576.635 | 0.0812 | below_vwap | below_vwap |
| 5 | SOXX | semiconductor_index | 548.98 |  | 553.7494 | -0.8613 | 557.38 | 545.965 | 0.102 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 986.35 |  | 989.4331 | -0.3116 | 999.04 | 964.86 | 0.7878 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1799.23 |  | 1806.9315 | -0.4262 | 1806.11 | 1780.9 | 0.1567 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 566.13 |  | 567.3742 | -0.2193 | 566.18 | 548.47 | 4.7516 | below_vwap | below_vwap,spread_too_wide |
| 9 | TT | data_center_power_cooling | 476.49 |  | 476.8352 | -0.0724 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ANET | ai_networking_optical | 176.06 |  | 177.2586 | -0.6762 | 177.84 | 173.19 | 0.2102 | below_vwap | below_vwap |
| 11 | JCI | data_center_power_cooling | 143.92 |  | 144.1054 | -0.1287 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 652.1 |  | 655.1945 | -0.4723 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 214.66 |  | 216.1798 | -0.703 | 217.88 | 212.99 | 2.8883 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMD | ai_accelerator | 543.16 |  | 550.2572 | -1.2898 | 556.12 | 542.33 | 2.1467 | below_vwap | below_vwap,spread_too_wide |
| 15 | VRT | data_center_power_cooling | 305.185 |  | 309.6189 | -1.4321 | 311.13 | 303.96 | 0.5701 | below_vwap | below_vwap,spread_too_wide |
| 16 | ETN | data_center_power_cooling | 413 |  | 413.7924 | -0.1915 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GEV | data_center_power_cooling | 1008.145 |  | 1012.6826 | -0.4481 | 1023.33 | 979.08 | 4.3079 | below_vwap | below_vwap,spread_too_wide |
| 18 | LRCX | semiconductor_equipment | 320.21 |  | 322.1012 | -0.5872 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ARM | ai_accelerator | 277.27 |  | 280.2095 | -1.049 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 557.81 |  | 563.6337 | -1.0332 | 576.24 | 556.3 | 1.2764 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.31 |  | 695.1069 | -0.5462 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.09 |  | 67.2117 | -1.6689 | 68.245 | 66.7 | 0.0303 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.22 |  | 208.9376 | -0.8221 | 210.85 | 208.49 | 0.0531 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.875 |  | 386.1096 | -1.6147 | 391.71 | 387.245 | 0.0658 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.24 |  | 321.238 | 0.0006 | 323.25 | 320.82 | 0.0872 | watch_only | none |
| GOOGL | cloud_ai_capex | 317.695 |  | 320.1908 | -0.7795 | 324.42 | 320.24 | 0.1542 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 543.16 |  | 550.2572 | -1.2898 | 556.12 | 542.33 | 2.1467 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.79 |  | 418.0962 | -0.5516 | 420.72 | 412.69 | 1.354 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.98 |  | 553.7494 | -0.8613 | 557.38 | 545.965 | 0.102 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.61 |  | 582.5765 | -0.6809 | 585.98 | 576.635 | 0.0812 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.03 |  | 394.478 | -1.1276 | 397.34 | 390.54 | 3.2562 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 986.35 |  | 989.4331 | -0.3116 | 999.04 | 964.86 | 0.7878 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 207.47 |  | 211.6711 | -1.9847 | 213.785 | 207.665 | 2.4244 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.84 |  | 444.8854 | -0.235 | 450.07 | 438.55 | 1.7123 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.44 |  | 48.6589 | -0.4499 | 48.88 | 47.635 | 0.9909 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 31.215 |  | 31.5807 | -1.158 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| SPY | market_regime | 738.1 |  | 740.089 | -0.2687 | 742.515 | 738.54 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 292.04 |  | 291.9303 | 0.0376 | 293.01 | 290.365 | 0.0137 | watch_only | none |
| ORCL | cloud_ai_capex | 121.39 |  | 123.3296 | -1.5727 | 124.22 | 122.07 | 1.3098 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.49 |  | 83.5579 | -1.278 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 305.185 |  | 309.6189 | -1.4321 | 311.13 | 303.96 | 0.5701 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413 |  | 413.7924 | -0.1915 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 652.1 |  | 655.1945 | -0.4723 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1008.145 |  | 1012.6826 | -0.4481 | 1023.33 | 979.08 | 4.3079 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.49 |  | 476.8352 | -0.0724 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.92 |  | 144.1054 | -0.1287 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.06 |  | 177.2586 | -0.6762 | 177.84 | 173.19 | 0.2102 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 315.52 |  | 320.1046 | -1.4322 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 842.81 |  | 868.7787 | -2.9891 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 408.135 |  | 410.1103 | -0.4816 | 408.58 | 397.9 | 1.0634 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 113.215 |  | 116.0277 | -2.4241 | 118.01 | 108.505 | 0.8568 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 327 |  | 332.6521 | -1.6991 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1799.23 |  | 1806.9315 | -0.4262 | 1806.11 | 1780.9 | 0.1567 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.13 |  | 567.3742 | -0.2193 | 566.18 | 548.47 | 4.7516 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.21 |  | 322.1012 | -0.5872 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.66 |  | 216.1798 | -0.703 | 217.88 | 212.99 | 2.8883 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.065 |  | 374.3199 | -0.8696 | 376.78 | 363.37 | 4.3173 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 298.51 |  | 300.039 | -0.5096 | 301.305 | 293.685 | 4.6129 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.125 |  | 66.4167 | -1.9449 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.87 |  | 55.2651 | -0.7149 | 55.76 | 54.445 | 1.4398 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 135.435 |  | 136.2679 | -0.6112 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 509.07 |  | 507.309 | 0.3471 | 510.71 | 502.72 | 4.2509 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.08 |  | 296.8726 | 0.0699 | 299.26 | 295.795 | 0.7708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 29.87 |  | 30.3637 | -1.6259 | 31.13 | 29.12 | 4.9548 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.675 |  | 42.327 | -1.5404 | 43.21 | 40.51 | 0.072 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.05 |  | 24.1536 | -0.4289 | 24.46 | 23.265 | 0.1247 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1627.72 |  | 1624.3981 | 0.2045 | 1651.355 | 1560 | 0.7784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 557.81 |  | 563.6337 | -1.0332 | 576.24 | 556.3 | 1.2764 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 916.31 |  | 925.8933 | -1.035 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.67 |  | 235.2942 | -1.1153 | 238.285 | 235.71 | 0.0215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 603.57 |  | 608.6125 | -0.8285 | 614.15 | 605.39 | 1.0322 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 277.27 |  | 280.2095 | -1.049 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.07 |  | 174.5397 | -1.415 | 177.88 | 168.18 | 1.6621 | below_vwap | below_vwap,spread_too_wide |
