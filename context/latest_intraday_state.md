# Intraday State

- Generated at: `2026-07-23T22:52:06+08:00`
- Market time ET: `2026-07-23T10:52:07-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 9, 'watch_only': 4, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 12, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.19 |  | 695.3906 | -0.4603 | 698.65 | 693.24 | 0.0679 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 552.56 |  | 553.854 | -0.2336 | 557.38 | 545.965 | 0.0796 | below_vwap | below_vwap |
| SMH | semiconductor_index | 581.49 |  | 582.6535 | -0.1997 | 585.98 | 576.635 | 0.0825 | below_vwap | below_vwap |
| SPY | market_regime | 738.52 |  | 740.1592 | -0.2215 | 742.515 | 738.54 | 0.0244 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.41 |  | 1806.969 | 0.0797 | 1806.11 | 1780.9 | 0.1305 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 569.95 |  | 567.3123 | 0.465 | 566.18 | 548.47 | 0.2158 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.41 |  | 1806.969 | 0.0797 | 1806.11 | 1780.9 | 0.1305 | buy_precheck_manual_confirm | none |
| 2 | HPE | ai_server_oem | 48.83 |  | 48.6688 | 0.3312 | 48.88 | 47.635 | 0.0819 | watch_only | none |
| 3 | AMAT | semiconductor_equipment | 569.95 |  | 567.3123 | 0.465 | 566.18 | 548.47 | 0.2158 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 321.25 |  | 321.2462 | 0.0012 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| 5 | DELL | ai_server_oem | 447.25 |  | 444.879 | 0.533 | 450.07 | 438.55 | 0.3287 | watch_only | none |
| 6 | PWR | data_center_power_cooling | 657.01 |  | 655.2444 | 0.2694 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TT | data_center_power_cooling | 477.47 |  | 476.8431 | 0.1315 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 144.37 |  | 144.1084 | 0.1815 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 414.6 |  | 413.8141 | 0.1899 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | CRWV | gpu_cloud_ai_factory | 83.655 |  | 83.5808 | 0.0887 | 84.415 | 80.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | CORZ | high_beta_ai_infrastructure | 24.22 |  | 24.1545 | 0.2714 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| 12 | LRCX | semiconductor_equipment | 323.02 |  | 322.1463 | 0.2712 | 322.4 | 317.27 | 3.3589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | MU | memory_hbm_storage | 990.06 |  | 989.4496 | 0.0617 | 999.04 | 964.86 | 0.7818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | KLAC | semiconductor_equipment | 216.4 |  | 216.2082 | 0.0887 | 217.88 | 212.99 | 2.8235 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | GEV | data_center_power_cooling | 1013.35 |  | 1012.8635 | 0.048 | 1023.33 | 979.08 | 1.2987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LIN | industrial_gases | 508.045 |  | 507.1754 | 0.1715 | 510.71 | 502.72 | 2.9367 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | CIEN | ai_networking_optical | 411.06 |  | 410.1714 | 0.2166 | 408.58 | 397.9 | 0.6714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SNDK | memory_hbm_storage | 1636.43 |  | 1624.1664 | 0.7551 | 1651.355 | 1560 | 3.9721 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SMH | semiconductor_index | 581.49 |  | 582.6535 | -0.1997 | 585.98 | 576.635 | 0.0825 | below_vwap | below_vwap |
| 20 | SOXX | semiconductor_index | 552.56 |  | 553.854 | -0.2336 | 557.38 | 545.965 | 0.0796 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.41 |  | 1806.969 | 0.0797 | 1806.11 | 1780.9 | 0.1305 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 569.95 |  | 567.3123 | 0.465 | 566.18 | 548.47 | 0.2158 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 31.52 |  | 31.5911 | -0.225 | 31.52 | 30.23 | 0.0635 | below_vwap | below_vwap |
| 4 | PWR | data_center_power_cooling | 657.01 |  | 655.2444 | 0.2694 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LRCX | semiconductor_equipment | 323.02 |  | 322.1463 | 0.2712 | 322.4 | 317.27 | 3.3589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | CIEN | ai_networking_optical | 411.06 |  | 410.1714 | 0.2166 | 408.58 | 397.9 | 0.6714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | HPE | ai_server_oem | 48.83 |  | 48.6688 | 0.3312 | 48.88 | 47.635 | 0.0819 | watch_only | none |
| 8 | DELL | ai_server_oem | 447.25 |  | 444.879 | 0.533 | 450.07 | 438.55 | 0.3287 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 321.25 |  | 321.2462 | 0.0012 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.22 |  | 24.1545 | 0.2714 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| 11 | TSM | foundry | 417.34 |  | 418.1888 | -0.203 | 420.72 | 412.69 | 3.5343 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMH | semiconductor_index | 581.49 |  | 582.6535 | -0.1997 | 585.98 | 576.635 | 0.0825 | below_vwap | below_vwap |
| 13 | SOXX | semiconductor_index | 552.56 |  | 553.854 | -0.2336 | 557.38 | 545.965 | 0.0796 | below_vwap | below_vwap |
| 14 | AVGO | custom_silicon_networking | 392.3 |  | 394.6071 | -0.5847 | 397.34 | 390.54 | 1.1649 | below_vwap | below_vwap,spread_too_wide |
| 15 | ANET | ai_networking_optical | 176.715 |  | 177.3433 | -0.3543 | 177.84 | 173.19 | 2.2805 | below_vwap | below_vwap,spread_too_wide |
| 16 | AMD | ai_accelerator | 545.32 |  | 550.4237 | -0.9272 | 556.12 | 542.33 | 1.0691 | below_vwap | below_vwap,spread_too_wide |
| 17 | VRT | data_center_power_cooling | 307.705 |  | 309.7328 | -0.6547 | 311.13 | 303.96 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | IWM | market_regime | 291.83 |  | 291.9344 | -0.0358 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| 19 | ARM | ai_accelerator | 279.14 |  | 280.3037 | -0.4152 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 558.685 |  | 563.8672 | -0.9191 | 576.24 | 556.3 | 0.1969 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.19 |  | 695.3906 | -0.4603 | 698.65 | 693.24 | 0.0679 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.385 |  | 67.2777 | -1.327 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.15 |  | 208.9712 | -0.393 | 210.85 | 208.49 | 0.048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.47 |  | 386.3552 | -1.7821 | 391.71 | 387.245 | 0.0211 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.25 |  | 321.2462 | 0.0012 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| GOOGL | cloud_ai_capex | 317.35 |  | 320.2975 | -0.9202 | 324.42 | 320.24 | 0.4412 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 545.32 |  | 550.4237 | -0.9272 | 556.12 | 542.33 | 1.0691 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 417.34 |  | 418.1888 | -0.203 | 420.72 | 412.69 | 3.5343 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.56 |  | 553.854 | -0.2336 | 557.38 | 545.965 | 0.0796 | below_vwap | below_vwap |
| SMH | semiconductor_index | 581.49 |  | 582.6535 | -0.1997 | 585.98 | 576.635 | 0.0825 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 392.3 |  | 394.6071 | -0.5847 | 397.34 | 390.54 | 1.1649 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 990.06 |  | 989.4496 | 0.0617 | 999.04 | 964.86 | 0.7818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.32 |  | 211.8327 | -1.1862 | 213.785 | 207.665 | 0.7166 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 447.25 |  | 444.879 | 0.533 | 450.07 | 438.55 | 0.3287 | watch_only | none |
| HPE | ai_server_oem | 48.83 |  | 48.6688 | 0.3312 | 48.88 | 47.635 | 0.0819 | watch_only | none |
| SMCI | ai_server_oem | 31.52 |  | 31.5911 | -0.225 | 31.52 | 30.23 | 0.0635 | below_vwap | below_vwap |
| SPY | market_regime | 738.52 |  | 740.1592 | -0.2215 | 742.515 | 738.54 | 0.0244 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.83 |  | 291.9344 | -0.0358 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 122.195 |  | 123.3609 | -0.9451 | 124.22 | 122.07 | 0.0737 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.655 |  | 83.5808 | 0.0887 | 84.415 | 80.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 307.705 |  | 309.7328 | -0.6547 | 311.13 | 303.96 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 414.6 |  | 413.8141 | 0.1899 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 657.01 |  | 655.2444 | 0.2694 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1013.35 |  | 1012.8635 | 0.048 | 1023.33 | 979.08 | 1.2987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.47 |  | 476.8431 | 0.1315 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.37 |  | 144.1084 | 0.1815 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.715 |  | 177.3433 | -0.3543 | 177.84 | 173.19 | 2.2805 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 318 |  | 320.1866 | -0.6829 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 851.435 |  | 869.3186 | -2.0572 | 880.26 | 833 | 2.7001 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 411.06 |  | 410.1714 | 0.2166 | 408.58 | 397.9 | 0.6714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 114.33 |  | 116.1215 | -1.5428 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 328.88 |  | 332.7265 | -1.1561 | 341.68 | 327.43 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1808.41 |  | 1806.969 | 0.0797 | 1806.11 | 1780.9 | 0.1305 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 569.95 |  | 567.3123 | 0.465 | 566.18 | 548.47 | 0.2158 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 323.02 |  | 322.1463 | 0.2712 | 322.4 | 317.27 | 3.3589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.4 |  | 216.2082 | 0.0887 | 217.88 | 212.99 | 2.8235 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373.59 |  | 374.4305 | -0.2245 | 376.78 | 363.37 | 4.6441 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 299.96 |  | 300.0511 | -0.0304 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.725 |  | 66.4814 | -1.1378 | 67.455 | 65.81 | 3.5603 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.87 |  | 55.2651 | -0.7149 | 55.76 | 54.445 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.955 |  | 136.737 | -0.5719 | 137.81 | 135.66 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.965 |  | 345.2972 | 0.1934 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 508.045 |  | 507.1754 | 0.1715 | 510.71 | 502.72 | 2.9367 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.67 |  | 296.8601 | -0.064 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.11 |  | 30.3737 | -0.8682 | 31.13 | 29.12 | 0.0664 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.19 |  | 42.3394 | -0.3528 | 43.21 | 40.51 | 0.0474 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.22 |  | 24.1545 | 0.2714 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| SNDK | memory_hbm_storage | 1636.43 |  | 1624.1664 | 0.7551 | 1651.355 | 1560 | 3.9721 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.685 |  | 563.8672 | -0.9191 | 576.24 | 556.3 | 0.1969 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 922.68 |  | 926.364 | -0.3977 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.72 |  | 235.4227 | -1.148 | 238.285 | 235.71 | 0.0172 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 603.05 |  | 608.7131 | -0.9303 | 614.15 | 605.39 | 0.2106 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 279.14 |  | 280.3037 | -0.4152 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 174.09 |  | 174.5832 | -0.2825 | 177.88 | 168.18 | 1.7232 | below_vwap | below_vwap,spread_too_wide |
