# Intraday State

- Generated at: `2026-07-23T23:05:28+08:00`
- Market time ET: `2026-07-23T11:05:29-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 14, 'watch_only': 1, 'below_vwap': 36, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.03 |  | 694.8301 | -0.5469 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.065 |  | 553.5118 | -0.8034 | 557.38 | 545.965 | 0.0965 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.64 |  | 582.457 | -0.6553 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| SPY | market_regime | 737.6 |  | 739.9723 | -0.3206 | 742.515 | 738.54 | 0.0176 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.35 |  | 321.2488 | 0.0315 | 323.25 | 320.82 | 0.0218 | watch_only | none |
| 2 | APD | industrial_gases | 297.17 |  | 296.9123 | 0.0868 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | LIN | industrial_gases | 510.16 |  | 507.4453 | 0.535 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | SNDK | memory_hbm_storage | 1637.205 |  | 1624.7488 | 0.7667 | 1651.355 | 1560 | 0.5461 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SMH | semiconductor_index | 578.64 |  | 582.457 | -0.6553 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 549.065 |  | 553.5118 | -0.8034 | 557.38 | 545.965 | 0.0965 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 291.4 |  | 291.9293 | -0.1813 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 8 | HPE | ai_server_oem | 48.43 |  | 48.6467 | -0.4454 | 48.88 | 47.635 | 0.0826 | below_vwap | below_vwap |
| 9 | MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 10 | SMCI | ai_server_oem | 31.09 |  | 31.5546 | -1.4724 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.23 |  | 42.2553 | -2.4263 | 43.21 | 40.51 | 0.0728 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 565.4 |  | 567.3775 | -0.3485 | 566.18 | 548.47 | 0.2158 | below_vwap | below_vwap |
| 14 | TT | data_center_power_cooling | 475.6 |  | 476.7839 | -0.2483 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ANET | ai_networking_optical | 175.325 |  | 177.1935 | -1.0545 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 143.78 |  | 144.0915 | -0.2162 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 650.78 |  | 654.904 | -0.6297 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 412.45 |  | 413.7172 | -0.3063 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 319.91 |  | 322.0085 | -0.6517 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 276.49 |  | 280.0632 | -1.2758 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.35 |  | 321.2488 | 0.0315 | 323.25 | 320.82 | 0.0218 | watch_only | none |
| 2 | TSM | foundry | 415.2 |  | 417.9057 | -0.6474 | 420.72 | 412.69 | 1.0116 | below_vwap | below_vwap,spread_too_wide |
| 3 | SMH | semiconductor_index | 578.64 |  | 582.457 | -0.6553 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| 4 | SOXX | semiconductor_index | 549.065 |  | 553.5118 | -0.8034 | 557.38 | 545.965 | 0.0965 | below_vwap | below_vwap |
| 5 | MU | memory_hbm_storage | 987.93 |  | 989.4301 | -0.1516 | 999.04 | 964.86 | 0.8806 | below_vwap | below_vwap,spread_too_wide |
| 6 | ASML | semiconductor_equipment | 1803.44 |  | 1806.6721 | -0.1789 | 1806.11 | 1780.9 | 0.3771 | below_vwap | below_vwap,spread_too_wide |
| 7 | AMAT | semiconductor_equipment | 565.4 |  | 567.3775 | -0.3485 | 566.18 | 548.47 | 0.2158 | below_vwap | below_vwap |
| 8 | TT | data_center_power_cooling | 475.6 |  | 476.7839 | -0.2483 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 175.325 |  | 177.1935 | -1.0545 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 143.78 |  | 144.0915 | -0.2162 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 650.78 |  | 654.904 | -0.6297 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 215.05 |  | 216.1447 | -0.5064 | 217.88 | 212.99 | 2.4366 | below_vwap | below_vwap,spread_too_wide |
| 13 | AMD | ai_accelerator | 544.45 |  | 549.8868 | -0.9887 | 556.12 | 542.33 | 2.2794 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 412.45 |  | 413.7172 | -0.3063 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | GEV | data_center_power_cooling | 999.21 |  | 1012.1577 | -1.2792 | 1023.33 | 979.08 | 2.6671 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.4 |  | 291.9293 | -0.1813 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 319.91 |  | 322.0085 | -0.6517 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 276.49 |  | 280.0632 | -1.2758 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 559.62 |  | 563.4091 | -0.6725 | 576.24 | 556.3 | 0.3627 | below_vwap | below_vwap,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.03 |  | 694.8301 | -0.5469 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.96 |  | 67.0661 | -1.6493 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.91 |  | 208.7673 | -0.8897 | 210.85 | 208.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 378.51 |  | 385.4094 | -1.7901 | 391.71 | 387.245 | 0.6816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 321.35 |  | 321.2488 | 0.0315 | 323.25 | 320.82 | 0.0218 | watch_only | none |
| GOOGL | cloud_ai_capex | 316.405 |  | 320.0131 | -1.1275 | 324.42 | 320.24 | 0.0348 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 544.45 |  | 549.8868 | -0.9887 | 556.12 | 542.33 | 2.2794 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 415.2 |  | 417.9057 | -0.6474 | 420.72 | 412.69 | 1.0116 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.065 |  | 553.5118 | -0.8034 | 557.38 | 545.965 | 0.0965 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.64 |  | 582.457 | -0.6553 | 585.98 | 576.635 | 0.0795 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.18 |  | 394.175 | -1.0135 | 397.34 | 390.54 | 2.2297 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 987.93 |  | 989.4301 | -0.1516 | 999.04 | 964.86 | 0.8806 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 207.84 |  | 211.4109 | -1.6891 | 213.785 | 207.665 | 0.6928 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.11 |  | 444.8718 | -0.396 | 450.07 | 438.55 | 1.9092 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.43 |  | 48.6467 | -0.4454 | 48.88 | 47.635 | 0.0826 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.09 |  | 31.5546 | -1.4724 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 737.6 |  | 739.9723 | -0.3206 | 742.515 | 738.54 | 0.0176 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.4 |  | 291.9293 | -0.1813 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.87 |  | 123.2297 | -1.9149 | 124.22 | 122.07 | 0.0414 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.94 |  | 83.4165 | -1.77 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.57 |  | 309.3618 | -1.8722 | 311.13 | 303.96 | 3.7158 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.45 |  | 413.7172 | -0.3063 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 650.78 |  | 654.904 | -0.6297 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 999.21 |  | 1012.1577 | -1.2792 | 1023.33 | 979.08 | 2.6671 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.6 |  | 476.7839 | -0.2483 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.78 |  | 144.0915 | -0.2162 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.325 |  | 177.1935 | -1.0545 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.03 |  | 319.801 | -1.4919 | 320.13 | 307.04 | 4.0187 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 844.3 |  | 867.6375 | -2.6898 | 880.26 | 833 | 2.145 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 406.95 |  | 410.0067 | -0.7455 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 113.265 |  | 115.8601 | -2.2399 | 118.01 | 108.505 | 0.4679 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 326.38 |  | 332.3578 | -1.7986 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1803.44 |  | 1806.6721 | -0.1789 | 1806.11 | 1780.9 | 0.3771 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 565.4 |  | 567.3775 | -0.3485 | 566.18 | 548.47 | 0.2158 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.91 |  | 322.0085 | -0.6517 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.05 |  | 216.1447 | -0.5064 | 217.88 | 212.99 | 2.4366 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.625 |  | 374.0439 | -0.9141 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 294.175 |  | 299.5029 | -1.7789 | 301.305 | 293.685 | 0.5745 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.02 |  | 66.2029 | -1.7868 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.22 |  | 55.111 | -1.6168 | 55.76 | 54.22 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.355 |  | 136.2202 | -0.6351 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 510.16 |  | 507.4453 | 0.535 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.17 |  | 296.9123 | 0.0868 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.61 |  | 30.3187 | -2.3376 | 31.13 | 29.12 |  | below_vwap | below_vwap,spread_unavailable |
| IREN | high_beta_ai_infrastructure | 41.23 |  | 42.2553 | -2.4263 | 43.21 | 40.51 | 0.0728 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.92 |  | 24.1474 | -0.9415 | 24.46 | 23.265 | 0.1254 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1637.205 |  | 1624.7488 | 0.7667 | 1651.355 | 1560 | 0.5461 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 559.62 |  | 563.4091 | -0.6725 | 576.24 | 556.3 | 0.3627 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 919.93 |  | 925.3943 | -0.5905 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.63 |  | 235.0441 | -1.0271 | 238.285 | 235.71 | 0.1118 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.41 |  | 607.4517 | -0.9946 | 614.15 | 605.39 | 0.2178 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 276.49 |  | 280.0632 | -1.2758 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 171.9 |  | 174.4211 | -1.4454 | 177.88 | 168.18 | 0.5817 | below_vwap | below_vwap,spread_too_wide |
