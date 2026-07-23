# Intraday State

- Generated at: `2026-07-23T23:01:31+08:00`
- Market time ET: `2026-07-23T11:01:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 2, 'below_vwap': 35, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.6 |  | 694.9562 | -0.4829 | 698.65 | 693.24 | 0.0275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.63 |  | 553.5827 | -0.714 | 557.38 | 545.965 | 0.0964 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.11 |  | 582.4998 | -0.5819 | 585.98 | 576.635 | 0.0518 | below_vwap | below_vwap |
| SPY | market_regime | 738.3 |  | 740.0248 | -0.2331 | 742.515 | 738.54 | 0.0352 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.46 |  | 321.2416 | 0.068 | 323.25 | 320.82 | 0.0436 | watch_only | none |
| 2 | SNDK | memory_hbm_storage | 1634.745 |  | 1624.6031 | 0.6243 | 1651.355 | 1560 | 0.1535 | watch_only | none |
| 3 | TT | data_center_power_cooling | 476.925 |  | 476.8348 | 0.0189 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 297.01 |  | 296.8854 | 0.042 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 509.765 |  | 507.4013 | 0.4658 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | SMH | semiconductor_index | 579.11 |  | 582.4998 | -0.5819 | 585.98 | 576.635 | 0.0518 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 549.63 |  | 553.5827 | -0.714 | 557.38 | 545.965 | 0.0964 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.89 |  | 291.9361 | -0.0158 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 9 | HPE | ai_server_oem | 48.455 |  | 48.6538 | -0.4087 | 48.88 | 47.635 | 0.0826 | below_vwap | below_vwap |
| 10 | MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 11 | SMCI | ai_server_oem | 31.25 |  | 31.5699 | -1.0133 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | IREN | high_beta_ai_infrastructure | 41.285 |  | 42.2833 | -2.3609 | 43.21 | 40.51 | 0.0727 | below_vwap | below_vwap |
| 14 | CIEN | ai_networking_optical | 408.62 |  | 410.0868 | -0.3577 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | MRVL | custom_silicon_networking | 208.15 |  | 211.5045 | -1.586 | 213.785 | 207.665 | 0.2066 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.935 |  | 144.0974 | -0.1127 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 652.425 |  | 655.077 | -0.4048 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 215.57 |  | 216.1591 | -0.2725 | 217.88 | 212.99 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | VRT | data_center_power_cooling | 303.98 |  | 309.5365 | -1.7951 | 311.13 | 303.96 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LRCX | semiconductor_equipment | 320.99 |  | 322.0691 | -0.3351 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 567.33 |  | 567.4082 | -0.0138 | 566.18 | 548.47 | 0.9606 | below_vwap | below_vwap,spread_too_wide |
| 2 | CIEN | ai_networking_optical | 408.62 |  | 410.0868 | -0.3577 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| 3 | SNDK | memory_hbm_storage | 1634.745 |  | 1624.6031 | 0.6243 | 1651.355 | 1560 | 0.1535 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 321.46 |  | 321.2416 | 0.068 | 323.25 | 320.82 | 0.0436 | watch_only | none |
| 5 | TSM | foundry | 415.57 |  | 418.0057 | -0.5827 | 420.72 | 412.69 | 1.3548 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 579.11 |  | 582.4998 | -0.5819 | 585.98 | 576.635 | 0.0518 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 549.63 |  | 553.5827 | -0.714 | 557.38 | 545.965 | 0.0964 | below_vwap | below_vwap |
| 8 | MU | memory_hbm_storage | 987.42 |  | 989.4733 | -0.2075 | 999.04 | 964.86 | 1.0563 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1800.88 |  | 1806.6952 | -0.3219 | 1806.11 | 1780.9 | 0.3876 | below_vwap | below_vwap,spread_too_wide |
| 10 | ANET | ai_networking_optical | 175.65 |  | 177.2323 | -0.8928 | 177.84 | 173.19 | 2.7783 | below_vwap | below_vwap,spread_too_wide |
| 11 | JCI | data_center_power_cooling | 143.935 |  | 144.0974 | -0.1127 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 652.425 |  | 655.077 | -0.4048 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 215.57 |  | 216.1591 | -0.2725 | 217.88 | 212.99 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AMD | ai_accelerator | 543.91 |  | 550.0143 | -1.1098 | 556.12 | 542.33 | 1.1472 | below_vwap | below_vwap,spread_too_wide |
| 15 | VRT | data_center_power_cooling | 303.98 |  | 309.5365 | -1.7951 | 311.13 | 303.96 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ETN | data_center_power_cooling | 413.48 |  | 413.75 | -0.0653 | 415.53 | 406.545 | 2.8998 | below_vwap | below_vwap,spread_too_wide |
| 17 | GEV | data_center_power_cooling | 1005.27 |  | 1012.4393 | -0.7081 | 1023.33 | 979.08 | 3.6179 | below_vwap | below_vwap,spread_too_wide |
| 18 | IWM | market_regime | 291.89 |  | 291.9361 | -0.0158 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 19 | LRCX | semiconductor_equipment | 320.99 |  | 322.0691 | -0.3351 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 277.77 |  | 280.1007 | -0.8321 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.6 |  | 694.9562 | -0.4829 | 698.65 | 693.24 | 0.0275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.12 |  | 67.1545 | -1.5405 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.22 |  | 208.8662 | -0.7881 | 210.85 | 208.49 | 0.2027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.39 |  | 385.7496 | -1.6486 | 391.71 | 387.245 | 0.2399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.46 |  | 321.2416 | 0.068 | 323.25 | 320.82 | 0.0436 | watch_only | none |
| GOOGL | cloud_ai_capex | 316.92 |  | 320.1048 | -0.9949 | 324.42 | 320.24 | 0.9182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 543.91 |  | 550.0143 | -1.1098 | 556.12 | 542.33 | 1.1472 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.57 |  | 418.0057 | -0.5827 | 420.72 | 412.69 | 1.3548 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.63 |  | 553.5827 | -0.714 | 557.38 | 545.965 | 0.0964 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.11 |  | 582.4998 | -0.5819 | 585.98 | 576.635 | 0.0518 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.3 |  | 394.2678 | -1.0064 | 397.34 | 390.54 | 0.7712 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 987.42 |  | 989.4733 | -0.2075 | 999.04 | 964.86 | 1.0563 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 208.15 |  | 211.5045 | -1.586 | 213.785 | 207.665 | 0.2066 | below_vwap | below_vwap |
| DELL | ai_server_oem | 444.51 |  | 444.8807 | -0.0833 | 450.07 | 438.55 | 1.7097 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.455 |  | 48.6538 | -0.4087 | 48.88 | 47.635 | 0.0826 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.25 |  | 31.5699 | -1.0133 | 31.52 | 30.23 | 0.032 | below_vwap | below_vwap |
| SPY | market_regime | 738.3 |  | 740.0248 | -0.2331 | 742.515 | 738.54 | 0.0352 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.89 |  | 291.9361 | -0.0158 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 121.115 |  | 123.2856 | -1.7607 | 124.22 | 122.07 | 0.3963 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.795 |  | 83.4652 | -2.0011 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.98 |  | 309.5365 | -1.7951 | 311.13 | 303.96 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 413.48 |  | 413.75 | -0.0653 | 415.53 | 406.545 | 2.8998 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 652.425 |  | 655.077 | -0.4048 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1005.27 |  | 1012.4393 | -0.7081 | 1023.33 | 979.08 | 3.6179 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.925 |  | 476.8348 | 0.0189 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.935 |  | 144.0974 | -0.1127 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.65 |  | 177.2323 | -0.8928 | 177.84 | 173.19 | 2.7783 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 314.965 |  | 319.8737 | -1.5346 | 320.13 | 307.04 | 0.9684 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 843.27 |  | 867.97 | -2.8457 | 880.26 | 833 | 1.7776 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 408.62 |  | 410.0868 | -0.3577 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 113.26 |  | 115.9154 | -2.2908 | 118.01 | 108.505 | 0.4415 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 327.35 |  | 332.5721 | -1.5702 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1800.88 |  | 1806.6952 | -0.3219 | 1806.11 | 1780.9 | 0.3876 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 567.33 |  | 567.4082 | -0.0138 | 566.18 | 548.47 | 0.9606 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.99 |  | 322.0691 | -0.3351 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.57 |  | 216.1591 | -0.2725 | 217.88 | 212.99 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 371.955 |  | 374.1831 | -0.5955 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.73 |  | 299.8076 | -1.0265 | 301.305 | 293.685 | 0.5123 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.005 |  | 66.3093 | -1.9669 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.87 |  | 55.2651 | -0.7149 | 55.76 | 54.445 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.355 |  | 136.2202 | -0.6351 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 509.765 |  | 507.4013 | 0.4658 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.01 |  | 296.8854 | 0.042 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.64 |  | 30.3434 | -2.3183 | 31.13 | 29.12 | 0.1687 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.285 |  | 42.2833 | -2.3609 | 43.21 | 40.51 | 0.0727 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.98 |  | 24.1501 | -0.7044 | 24.46 | 23.265 | 0.1251 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1634.745 |  | 1624.6031 | 0.6243 | 1651.355 | 1560 | 0.1535 | watch_only | none |
| WDC | memory_hbm_storage | 559.28 |  | 563.4942 | -0.7479 | 576.24 | 556.3 | 1.2516 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.95 |  | 925.552 | -0.6053 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 233.02 |  | 235.1625 | -0.9111 | 238.285 | 235.71 | 0.0515 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.905 |  | 608.1642 | -1.0292 | 614.15 | 605.39 | 0.2924 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 277.77 |  | 280.1007 | -0.8321 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.595 |  | 174.4475 | -1.0619 | 177.88 | 168.18 | 1.7382 | below_vwap | below_vwap,spread_too_wide |
