# Intraday State

- Generated at: `2026-07-24T03:56:59+08:00`
- Market time ET: `2026-07-23T15:57:00-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'watch_only': 3, 'below_vwap': 26, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.17 |  | 692.3667 | -0.1728 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.8 |  | 550.1593 | -0.4288 | 557.38 | 545.965 | 0.0438 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.66 |  | 579.872 | -0.3815 | 585.98 | 576.635 | 0.0312 | below_vwap | below_vwap |
| SPY | market_regime | 737.54 |  | 738.2065 | -0.0903 | 742.515 | 738.54 | 0.0014 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1032.43 |  | 1020.1613 | 1.2026 | 1023.33 | 979.08 | 0.1172 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 291.66 |  | 291.5902 | 0.0239 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 321.6 |  | 320.9308 | 0.2085 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| 3 | META | cloud_ai_capex | 607.32 |  | 604.7984 | 0.4169 | 614.15 | 605.39 | 0.0428 | watch_only | none |
| 4 | GEV | data_center_power_cooling | 1032.43 |  | 1020.1613 | 1.2026 | 1023.33 | 979.08 | 0.1172 | buy_precheck_manual_confirm | none |
| 5 | PWR | data_center_power_cooling | 652.06 |  | 650.8238 | 0.1899 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TT | data_center_power_cooling | 479.59 |  | 477.4042 | 0.4579 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 216.55 |  | 215.8233 | 0.3367 | 217.88 | 212.99 | 0.3787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ETN | data_center_power_cooling | 413.84 |  | 413.4308 | 0.099 | 415.53 | 406.545 | 0.6597 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MKSI | semiconductor_materials | 343.315 |  | 342.2984 | 0.297 | 347.92 | 341.755 | 0.4253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ARM | ai_accelerator | 281.9 |  | 280.2986 | 0.5713 | 283 | 276.24 | 4.6116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 414.2 |  | 415.8651 | -0.4004 | 420.72 | 412.69 | 0.0483 | below_vwap | below_vwap |
| 12 | SMH | semiconductor_index | 577.66 |  | 579.872 | -0.3815 | 585.98 | 576.635 | 0.0312 | below_vwap | below_vwap |
| 13 | SOXX | semiconductor_index | 547.8 |  | 550.1593 | -0.4288 | 557.38 | 545.965 | 0.0438 | below_vwap | below_vwap |
| 14 | AVGO | custom_silicon_networking | 391.095 |  | 391.6892 | -0.1517 | 397.34 | 390.54 | 0.0869 | below_vwap | below_vwap |
| 15 | MU | memory_hbm_storage | 980.29 |  | 989.8362 | -0.9644 | 999.04 | 964.86 | 0.0479 | below_vwap | below_vwap |
| 16 | AMAT | semiconductor_equipment | 559.645 |  | 563.1208 | -0.6172 | 566.18 | 548.47 | 0.1287 | below_vwap | below_vwap |
| 17 | WDC | memory_hbm_storage | 556.91 |  | 563.2563 | -1.1267 | 576.24 | 556.3 | 0.149 | below_vwap | below_vwap |
| 18 | SKHY | memory_hbm_storage | 169.53 |  | 172.7349 | -1.8554 | 177.88 | 168.18 | 0.0885 | below_vwap | below_vwap |
| 19 | SNDK | memory_hbm_storage | 1600.135 |  | 1637.053 | -2.2552 | 1651.355 | 1560 | 0.0875 | below_vwap | below_vwap |
| 20 | SMCI | ai_server_oem | 31.04 |  | 31.5411 | -1.5886 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1032.43 |  | 1020.1613 | 1.2026 | 1023.33 | 979.08 | 0.1172 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 291.66 |  | 291.5902 | 0.0239 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 3 | META | cloud_ai_capex | 607.32 |  | 604.7984 | 0.4169 | 614.15 | 605.39 | 0.0428 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 321.6 |  | 320.9308 | 0.2085 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| 5 | TSM | foundry | 414.2 |  | 415.8651 | -0.4004 | 420.72 | 412.69 | 0.0483 | below_vwap | below_vwap |
| 6 | SMH | semiconductor_index | 577.66 |  | 579.872 | -0.3815 | 585.98 | 576.635 | 0.0312 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.8 |  | 550.1593 | -0.4288 | 557.38 | 545.965 | 0.0438 | below_vwap | below_vwap |
| 8 | AVGO | custom_silicon_networking | 391.095 |  | 391.6892 | -0.1517 | 397.34 | 390.54 | 0.0869 | below_vwap | below_vwap |
| 9 | MU | memory_hbm_storage | 980.29 |  | 989.8362 | -0.9644 | 999.04 | 964.86 | 0.0479 | below_vwap | below_vwap |
| 10 | ASML | semiconductor_equipment | 1794.065 |  | 1800.7165 | -0.3694 | 1806.11 | 1780.9 | 0.5373 | below_vwap | below_vwap,spread_too_wide |
| 11 | AMAT | semiconductor_equipment | 559.645 |  | 563.1208 | -0.6172 | 566.18 | 548.47 | 0.1287 | below_vwap | below_vwap |
| 12 | ANET | ai_networking_optical | 175.79 |  | 176.4745 | -0.3879 | 177.84 | 173.19 | 2.3721 | below_vwap | below_vwap,spread_too_wide |
| 13 | JCI | data_center_power_cooling | 143.35 |  | 143.7524 | -0.2799 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | LRCX | semiconductor_equipment | 317.78 |  | 319.7444 | -0.6144 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 556.91 |  | 563.2563 | -1.1267 | 576.24 | 556.3 | 0.149 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LIN | industrial_gases | 506.285 |  | 506.7825 | -0.0982 | 510.71 | 502.72 | 4.7483 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 311.51 |  | 316.2123 | -1.4871 | 320.13 | 307.04 | 4.4974 | below_vwap | below_vwap,spread_too_wide |
| 19 | CIEN | ai_networking_optical | 404.13 |  | 407.2297 | -0.7612 | 408.58 | 397.9 | 5.1048 | below_vwap | below_vwap,spread_too_wide |
| 20 | TER | semiconductor_test_packaging | 370.35 |  | 371.4381 | -0.2929 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.17 |  | 692.3667 | -0.1728 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.02 |  | 66.415 | -0.5947 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.38 |  | 208.4027 | -0.0109 | 210.85 | 208.49 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.54 |  | 382.2341 | -0.1816 | 391.71 | 387.245 | 0.0183 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.6 |  | 320.9308 | 0.2085 | 323.25 | 320.82 | 0.0155 | watch_only | none |
| GOOGL | cloud_ai_capex | 318.69 |  | 319.353 | -0.2076 | 324.42 | 320.24 | 0.0251 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.875 |  | 539.7513 | -0.1624 | 556.12 | 542.33 | 1.2971 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 414.2 |  | 415.8651 | -0.4004 | 420.72 | 412.69 | 0.0483 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.8 |  | 550.1593 | -0.4288 | 557.38 | 545.965 | 0.0438 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.66 |  | 579.872 | -0.3815 | 585.98 | 576.635 | 0.0312 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.095 |  | 391.6892 | -0.1517 | 397.34 | 390.54 | 0.0869 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 980.29 |  | 989.8362 | -0.9644 | 999.04 | 964.86 | 0.0479 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 207.33 |  | 208.892 | -0.7478 | 213.785 | 207.665 | 0.0772 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 435.73 |  | 442.5841 | -1.5486 | 450.07 | 438.55 | 1.8911 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.57 |  | 48.142 | -1.1881 | 48.88 | 47.635 | 0.042 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31.04 |  | 31.5411 | -1.5886 | 31.52 | 30.23 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 737.54 |  | 738.2065 | -0.0903 | 742.515 | 738.54 | 0.0014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.66 |  | 291.5902 | 0.0239 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 120.045 |  | 121.4335 | -1.1434 | 124.22 | 122.07 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.79 |  | 82.2434 | -1.7672 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.5 |  | 305.3689 | -0.9395 | 311.13 | 303.96 | 1.4876 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.84 |  | 413.4308 | 0.099 | 415.53 | 406.545 | 0.6597 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 652.06 |  | 650.8238 | 0.1899 | 656.38 | 642.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1032.43 |  | 1020.1613 | 1.2026 | 1023.33 | 979.08 | 0.1172 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 479.59 |  | 477.4042 | 0.4579 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.35 |  | 143.7524 | -0.2799 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.79 |  | 176.4745 | -0.3879 | 177.84 | 173.19 | 2.3721 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.51 |  | 316.2123 | -1.4871 | 320.13 | 307.04 | 4.4974 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 832.15 |  | 852.5438 | -2.3921 | 880.26 | 833 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 404.13 |  | 407.2297 | -0.7612 | 408.58 | 397.9 | 5.1048 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.47 |  | 114.1242 | -2.3257 | 118.01 | 108.505 | 4.2254 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 321.45 |  | 325.4742 | -1.2364 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.065 |  | 1800.7165 | -0.3694 | 1806.11 | 1780.9 | 0.5373 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 559.645 |  | 563.1208 | -0.6172 | 566.18 | 548.47 | 0.1287 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 317.78 |  | 319.7444 | -0.6144 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.55 |  | 215.8233 | 0.3367 | 217.88 | 212.99 | 0.3787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 370.35 |  | 371.4381 | -0.2929 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.52 |  | 293.3939 | -0.9795 | 301.305 | 293.685 | 4.5746 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.05 |  | 65.1394 | -0.1373 | 67.455 | 65.81 | 0.0461 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 54.035 |  | 54.3905 | -0.6537 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.23 |  | 134.7879 | -0.4139 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.315 |  | 342.2984 | 0.297 | 347.92 | 341.755 | 0.4253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.285 |  | 506.7825 | -0.0982 | 510.71 | 502.72 | 4.7483 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.87 |  | 295.5606 | -0.2336 | 299.26 | 295.795 | 0.061 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 29.835 |  | 30.0244 | -0.6309 | 31.13 | 29.12 | 2.0446 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.63 |  | 41.4248 | -1.9186 | 43.21 | 40.51 | 0.0246 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.985 |  | 24.0705 | -0.3551 | 24.46 | 23.265 | 0.0834 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1600.135 |  | 1637.053 | -2.2552 | 1651.355 | 1560 | 0.0875 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 556.91 |  | 563.2563 | -1.1267 | 576.24 | 556.3 | 0.149 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 910.46 |  | 921.3446 | -1.1814 | 933.5 | 908.955 | 0.0846 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 233.94 |  | 234.2026 | -0.1121 | 238.285 | 235.71 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 607.32 |  | 604.7984 | 0.4169 | 614.15 | 605.39 | 0.0428 | watch_only | none |
| ARM | ai_accelerator | 281.9 |  | 280.2986 | 0.5713 | 283 | 276.24 | 4.6116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 169.53 |  | 172.7349 | -1.8554 | 177.88 | 168.18 | 0.0885 | below_vwap | below_vwap |
