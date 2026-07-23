# Intraday State

- Generated at: `2026-07-23T23:21:12+08:00`
- Market time ET: `2026-07-23T11:21:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'watch_only': 3, 'below_vwap': 32, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.6 |  | 694.1636 | -0.5134 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.18 |  | 553.0297 | -0.8769 | 557.38 | 545.965 | 0.0821 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.105 |  | 582.0802 | -0.6829 | 585.98 | 576.635 | 0.0899 | below_vwap | below_vwap |
| SPY | market_regime | 737.5 |  | 739.5602 | -0.2786 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 992.27 |  | 989.2188 | 0.3084 | 999.04 | 964.86 | 0.3467 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 322.255 |  | 321.2808 | 0.3032 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| 3 | LIN | industrial_gases | 507.74 |  | 507.6686 | 0.0141 | 510.71 | 502.72 | 0.1595 | watch_only | none |
| 4 | SNDK | memory_hbm_storage | 1637.36 |  | 1624.8754 | 0.7683 | 1651.355 | 1560 | 0.6712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | TSM | foundry | 414.53 |  | 417.402 | -0.6881 | 420.72 | 412.69 | 0.1206 | below_vwap | below_vwap |
| 6 | SMH | semiconductor_index | 578.105 |  | 582.0802 | -0.6829 | 585.98 | 576.635 | 0.0899 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 548.18 |  | 553.0297 | -0.8769 | 557.38 | 545.965 | 0.0821 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.01 |  | 291.8666 | -0.2935 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 9 | HPE | ai_server_oem | 48.33 |  | 48.5296 | -0.4112 | 48.88 | 47.635 | 0.0828 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 31.18 |  | 31.5034 | -1.0266 | 31.52 | 30.23 | 0.0641 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.325 |  | 42.1275 | -1.9049 | 43.21 | 40.51 | 0.0484 | below_vwap | below_vwap |
| 13 | TT | data_center_power_cooling | 474.78 |  | 476.7081 | -0.4045 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ANET | ai_networking_optical | 174.655 |  | 176.937 | -1.2897 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 143.16 |  | 144.0242 | -0.6001 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 646.57 |  | 654.3218 | -1.1847 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ETN | data_center_power_cooling | 411.69 |  | 413.5388 | -0.4471 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | GEV | data_center_power_cooling | 1005.14 |  | 1011.7624 | -0.6545 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 319.27 |  | 321.8044 | -0.7875 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 277.32 |  | 279.5772 | -0.8074 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 992.27 |  | 989.2188 | 0.3084 | 999.04 | 964.86 | 0.3467 | watch_only | none |
| 2 | LIN | industrial_gases | 507.74 |  | 507.6686 | 0.0141 | 510.71 | 502.72 | 0.1595 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 322.255 |  | 321.2808 | 0.3032 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| 4 | TSM | foundry | 414.53 |  | 417.402 | -0.6881 | 420.72 | 412.69 | 0.1206 | below_vwap | below_vwap |
| 5 | SMH | semiconductor_index | 578.105 |  | 582.0802 | -0.6829 | 585.98 | 576.635 | 0.0899 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 548.18 |  | 553.0297 | -0.8769 | 557.38 | 545.965 | 0.0821 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1799.66 |  | 1805.988 | -0.3504 | 1806.11 | 1780.9 | 0.6023 | below_vwap | below_vwap,spread_too_wide |
| 8 | AMAT | semiconductor_equipment | 564.785 |  | 567.0051 | -0.3916 | 566.18 | 548.47 | 2.2433 | below_vwap | below_vwap,spread_too_wide |
| 9 | TT | data_center_power_cooling | 474.78 |  | 476.7081 | -0.4045 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ANET | ai_networking_optical | 174.655 |  | 176.937 | -1.2897 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 143.16 |  | 144.0242 | -0.6001 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 646.57 |  | 654.3218 | -1.1847 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 214.955 |  | 216.0521 | -0.5078 | 217.88 | 212.99 | 2.3586 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 411.69 |  | 413.5388 | -0.4471 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | GEV | data_center_power_cooling | 1005.14 |  | 1011.7624 | -0.6545 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | IWM | market_regime | 291.01 |  | 291.8666 | -0.2935 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 319.27 |  | 321.8044 | -0.7875 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 277.32 |  | 279.5772 | -0.8074 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 561.59 |  | 562.9951 | -0.2496 | 576.24 | 556.3 | 0.8013 | below_vwap | below_vwap,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.6 |  | 694.1636 | -0.5134 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.895 |  | 66.8448 | -1.4209 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.49 |  | 208.4814 | -0.4755 | 210.85 | 208.49 | 0.2554 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379.34 |  | 384.3516 | -1.3039 | 391.71 | 387.245 | 0.3954 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 322.255 |  | 321.2808 | 0.3032 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| GOOGL | cloud_ai_capex | 316.85 |  | 319.6607 | -0.8793 | 324.42 | 320.24 | 0.0505 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 541.66 |  | 548.5012 | -1.2472 | 556.12 | 542.33 | 1.4622 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.53 |  | 417.402 | -0.6881 | 420.72 | 412.69 | 0.1206 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.18 |  | 553.0297 | -0.8769 | 557.38 | 545.965 | 0.0821 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.105 |  | 582.0802 | -0.6829 | 585.98 | 576.635 | 0.0899 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 389.6 |  | 393.6266 | -1.0229 | 397.34 | 390.54 | 0.6699 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.27 |  | 989.2188 | 0.3084 | 999.04 | 964.86 | 0.3467 | watch_only | none |
| MRVL | custom_silicon_networking | 207.46 |  | 210.7228 | -1.5484 | 213.785 | 207.665 | 0.1832 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 443.58 |  | 444.6792 | -0.2472 | 450.07 | 438.55 | 0.4802 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.33 |  | 48.5296 | -0.4112 | 48.88 | 47.635 | 0.0828 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.18 |  | 31.5034 | -1.0266 | 31.52 | 30.23 | 0.0641 | below_vwap | below_vwap |
| SPY | market_regime | 737.5 |  | 739.5602 | -0.2786 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.01 |  | 291.8666 | -0.2935 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.35 |  | 122.9122 | -2.0846 | 124.22 | 122.07 | 0.2327 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.72 |  | 83.2386 | -1.8244 | 84.415 | 80.64 | 4.2952 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.25 |  | 308.0665 | -1.5634 | 311.13 | 303.96 | 1.7378 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 411.69 |  | 413.5388 | -0.4471 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 646.57 |  | 654.3218 | -1.1847 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1005.14 |  | 1011.7624 | -0.6545 | 1023.33 | 979.08 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 474.78 |  | 476.7081 | -0.4045 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.16 |  | 144.0242 | -0.6001 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.655 |  | 176.937 | -1.2897 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 313.13 |  | 319.3612 | -1.9511 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 831.805 |  | 864.1177 | -3.7394 | 880.26 | 833 | 4.5467 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.65 |  | 409.4197 | -1.165 | 408.58 | 397.9 | 0.4078 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.37 |  | 115.4267 | -2.6482 | 118.01 | 108.505 | 4.3339 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 326.36 |  | 331.0782 | -1.4251 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1799.66 |  | 1805.988 | -0.3504 | 1806.11 | 1780.9 | 0.6023 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 564.785 |  | 567.0051 | -0.3916 | 566.18 | 548.47 | 2.2433 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.27 |  | 321.8044 | -0.7875 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.955 |  | 216.0521 | -0.5078 | 217.88 | 212.99 | 2.3586 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.74 |  | 372.6 | -0.4992 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 292.84 |  | 298.1964 | -1.7963 | 301.305 | 293.685 | 0.4986 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.29 |  | 65.7623 | -2.2388 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.185 |  | 55.0556 | -1.5813 | 55.76 | 54.185 | 0.5721 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 134.115 |  | 135.9206 | -1.3284 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.59 |  | 344.6636 | -1.472 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.74 |  | 507.6686 | 0.0141 | 510.71 | 502.72 | 0.1595 | watch_only | none |
| APD | industrial_gases | 296.65 |  | 296.8986 | -0.0837 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.55 |  | 30.2374 | -2.2735 | 31.13 | 29.12 | 0.8799 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.325 |  | 42.1275 | -1.9049 | 43.21 | 40.51 | 0.0484 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.87 |  | 24.1176 | -1.0265 | 24.46 | 23.265 | 0.1257 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1637.36 |  | 1624.8754 | 0.7683 | 1651.355 | 1560 | 0.6712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 561.59 |  | 562.9951 | -0.2496 | 576.24 | 556.3 | 0.8013 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 921.85 |  | 923.9635 | -0.2287 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.52 |  | 234.7736 | -0.9599 | 238.285 | 235.71 | 0.0903 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.44 |  | 606.0894 | -0.7671 | 614.15 | 605.39 | 0.2876 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 277.32 |  | 279.5772 | -0.8074 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 171.29 |  | 174.0385 | -1.5793 | 177.88 | 168.18 | 1.1676 | below_vwap | below_vwap,spread_too_wide |
