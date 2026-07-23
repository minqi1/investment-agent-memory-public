# Intraday State

- Generated at: `2026-07-24T03:53:07+08:00`
- Market time ET: `2026-07-23T15:53:08-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 22, 'watch_only': 2, 'below_vwap': 27, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.79 |  | 692.5063 | -0.3922 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 546.91 |  | 550.3412 | -0.6235 | 557.38 | 545.965 | 0.064 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.39 |  | 579.9811 | -0.6192 | 585.98 | 576.635 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.82 |  | 738.2581 | -0.1948 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.23 |  | 320.9121 | 0.099 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| 2 | PWR | data_center_power_cooling | 652.08 |  | 650.7605 | 0.2028 | 656.38 | 642.37 | 0.1534 | watch_only | none |
| 3 | TT | data_center_power_cooling | 479.6 |  | 477.2808 | 0.4859 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ETN | data_center_power_cooling | 413.7 |  | 413.4021 | 0.072 | 415.53 | 406.545 | 0.4037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ARM | ai_accelerator | 281.77 |  | 280.188 | 0.5646 | 283 | 276.24 | 0.6282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SOXX | semiconductor_index | 546.91 |  | 550.3412 | -0.6235 | 557.38 | 545.965 | 0.064 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1794.175 |  | 1801.0051 | -0.3792 | 1806.11 | 1780.9 | 0.0842 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.39 |  | 291.6025 | -0.0729 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 9 | SKHY | memory_hbm_storage | 169.57 |  | 172.7884 | -1.8626 | 177.88 | 168.18 | 0.0236 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 31.075 |  | 31.5465 | -1.4945 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | MU | memory_hbm_storage | 980.27 |  | 990.1488 | -0.9977 | 999.04 | 964.86 | 0.2367 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 559.225 |  | 563.2547 | -0.7154 | 566.18 | 548.47 | 0.1949 | below_vwap | below_vwap |
| 14 | LRCX | semiconductor_equipment | 318.21 |  | 319.907 | -0.5305 | 322.4 | 317.27 | 0.2074 | below_vwap | below_vwap |
| 15 | WDC | memory_hbm_storage | 558.58 |  | 563.4594 | -0.866 | 576.24 | 556.3 | 0.1575 | below_vwap | below_vwap |
| 16 | META | cloud_ai_capex | 604.82 |  | 604.7641 | 0.0092 | 614.15 | 605.39 | 0.916 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | CIEN | ai_networking_optical | 404.01 |  | 407.3449 | -0.8187 | 408.58 | 397.9 | 0.2599 | below_vwap | below_vwap |
| 18 | JCI | data_center_power_cooling | 143.47 |  | 143.7676 | -0.207 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GEV | data_center_power_cooling | 1033.29 |  | 1019.5473 | 1.3479 | 1023.33 | 979.08 | 1.5901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | COHR | ai_networking_optical | 311.88 |  | 316.3294 | -1.4066 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1033.29 |  | 1019.5473 | 1.3479 | 1023.33 | 979.08 | 1.5901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | PWR | data_center_power_cooling | 652.08 |  | 650.7605 | 0.2028 | 656.38 | 642.37 | 0.1534 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 321.23 |  | 320.9121 | 0.099 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| 4 | TSM | foundry | 413.605 |  | 416.0348 | -0.584 | 420.72 | 412.69 | 0.3893 | below_vwap | below_vwap,spread_too_wide |
| 5 | SOXX | semiconductor_index | 546.91 |  | 550.3412 | -0.6235 | 557.38 | 545.965 | 0.064 | below_vwap | below_vwap |
| 6 | MU | memory_hbm_storage | 980.27 |  | 990.1488 | -0.9977 | 999.04 | 964.86 | 0.2367 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1794.175 |  | 1801.0051 | -0.3792 | 1806.11 | 1780.9 | 0.0842 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 559.225 |  | 563.2547 | -0.7154 | 566.18 | 548.47 | 0.1949 | below_vwap | below_vwap |
| 9 | ANET | ai_networking_optical | 176.1 |  | 176.5033 | -0.2285 | 177.84 | 173.19 | 3.1232 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 143.47 |  | 143.7676 | -0.207 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 215.275 |  | 215.8372 | -0.2605 | 217.88 | 212.99 | 1.1102 | below_vwap | below_vwap,spread_too_wide |
| 12 | IWM | market_regime | 291.39 |  | 291.6025 | -0.0729 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 318.21 |  | 319.907 | -0.5305 | 322.4 | 317.27 | 0.2074 | below_vwap | below_vwap |
| 14 | WDC | memory_hbm_storage | 558.58 |  | 563.4594 | -0.866 | 576.24 | 556.3 | 0.1575 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LIN | industrial_gases | 504.945 |  | 506.8879 | -0.3833 | 510.71 | 502.72 | 5.0382 | below_vwap | below_vwap,spread_too_wide |
| 17 | COHR | ai_networking_optical | 311.88 |  | 316.3294 | -1.4066 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | CIEN | ai_networking_optical | 404.01 |  | 407.3449 | -0.8187 | 408.58 | 397.9 | 0.2599 | below_vwap | below_vwap |
| 19 | LITE | ai_networking_optical | 833.63 |  | 852.8625 | -2.255 | 880.26 | 833 | 0.3791 | below_vwap | below_vwap,spread_too_wide |
| 20 | TER | semiconductor_test_packaging | 368.79 |  | 371.585 | -0.7522 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.79 |  | 692.5063 | -0.3922 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.71 |  | 66.4381 | -1.0959 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.67 |  | 208.4203 | -0.36 | 210.85 | 208.49 | 0.0096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.39 |  | 382.2756 | -0.4933 | 391.71 | 387.245 | 0.0368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.23 |  | 320.9121 | 0.099 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| GOOGL | cloud_ai_capex | 318.42 |  | 319.3734 | -0.2985 | 324.42 | 320.24 | 0.0283 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.425 |  | 539.7979 | -0.2543 | 556.12 | 542.33 | 1.0958 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 413.605 |  | 416.0348 | -0.584 | 420.72 | 412.69 | 0.3893 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 546.91 |  | 550.3412 | -0.6235 | 557.38 | 545.965 | 0.064 | below_vwap | below_vwap |
| SMH | semiconductor_index | 576.39 |  | 579.9811 | -0.6192 | 585.98 | 576.635 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 390.02 |  | 391.7628 | -0.4449 | 397.34 | 390.54 | 1.2769 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 980.27 |  | 990.1488 | -0.9977 | 999.04 | 964.86 | 0.2367 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 206.445 |  | 209.0161 | -1.2301 | 213.785 | 207.665 | 0.6346 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 435.44 |  | 442.7513 | -1.6513 | 450.07 | 438.55 | 0.2182 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 47.44 |  | 48.161 | -1.4971 | 48.88 | 47.635 | 0.0632 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.075 |  | 31.5465 | -1.4945 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 736.82 |  | 738.2581 | -0.1948 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.39 |  | 291.6025 | -0.0729 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.58 |  | 121.4959 | -1.577 | 124.22 | 122.07 | 0.0502 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.94 |  | 82.3164 | -1.6721 | 84.415 | 80.64 | 2.9157 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.7 |  | 305.4857 | -0.9119 | 311.13 | 303.96 | 1.4866 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.7 |  | 413.4021 | 0.072 | 415.53 | 406.545 | 0.4037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 652.08 |  | 650.7605 | 0.2028 | 656.38 | 642.37 | 0.1534 | watch_only | none |
| GEV | data_center_power_cooling | 1033.29 |  | 1019.5473 | 1.3479 | 1023.33 | 979.08 | 1.5901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 479.6 |  | 477.2808 | 0.4859 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.47 |  | 143.7676 | -0.207 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.1 |  | 176.5033 | -0.2285 | 177.84 | 173.19 | 3.1232 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.88 |  | 316.3294 | -1.4066 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 833.63 |  | 852.8625 | -2.255 | 880.26 | 833 | 0.3791 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.01 |  | 407.3449 | -0.8187 | 408.58 | 397.9 | 0.2599 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.89 |  | 114.1997 | -2.0225 | 118.01 | 108.505 | 4.6921 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 320.58 |  | 325.5272 | -1.5198 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.175 |  | 1801.0051 | -0.3792 | 1806.11 | 1780.9 | 0.0842 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 559.225 |  | 563.2547 | -0.7154 | 566.18 | 548.47 | 0.1949 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 318.21 |  | 319.907 | -0.5305 | 322.4 | 317.27 | 0.2074 | below_vwap | below_vwap |
| KLAC | semiconductor_equipment | 215.275 |  | 215.8372 | -0.2605 | 217.88 | 212.99 | 1.1102 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 368.79 |  | 371.585 | -0.7522 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.81 |  | 293.4805 | -1.2507 | 301.305 | 293.685 | 4.3304 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65 |  | 65.1557 | -0.239 | 67.455 | 65.81 | 4.3538 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.265 |  | 54.4158 | -0.2772 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.925 |  | 134.8728 | -0.7028 | 137.81 | 135.66 | 0.2912 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 341.66 |  | 342.3613 | -0.2048 | 347.92 | 341.755 | 0.1932 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LIN | industrial_gases | 504.945 |  | 506.8879 | -0.3833 | 510.71 | 502.72 | 5.0382 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.07 |  | 295.5981 | -0.1787 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.685 |  | 30.0294 | -1.147 | 31.13 | 29.12 | 0.2358 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.56 |  | 41.466 | -2.1848 | 43.21 | 40.51 | 0.7643 | below_vwap | below_vwap,spread_too_wide |
| CORZ | high_beta_ai_infrastructure | 24.04 |  | 24.0736 | -0.1395 | 24.46 | 23.265 | 0.0832 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1607.15 |  | 1638.2312 | -1.8972 | 1651.355 | 1560 | 5.0306 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 558.58 |  | 563.4594 | -0.866 | 576.24 | 556.3 | 0.1575 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 913.04 |  | 921.6784 | -0.9372 | 933.5 | 908.955 | 0.2344 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 233.79 |  | 234.2227 | -0.1847 | 238.285 | 235.71 | 0.0086 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 604.82 |  | 604.7641 | 0.0092 | 614.15 | 605.39 | 0.916 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 281.77 |  | 280.188 | 0.5646 | 283 | 276.24 | 0.6282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 169.57 |  | 172.7884 | -1.8626 | 177.88 | 168.18 | 0.0236 | below_vwap | below_vwap |
