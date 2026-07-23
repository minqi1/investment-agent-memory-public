# Intraday State

- Generated at: `2026-07-24T01:14:57+08:00`
- Market time ET: `2026-07-23T13:14:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 12, 'watch_only': 4, 'price_stale_or_missing': 2, 'below_vwap': 24, 'spread_too_wide_or_missing': 13, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.71 |  | 693.1248 | -0.0598 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.15 |  | 550.983 | -0.1512 | 557.38 | 545.965 | 0.0782 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.66 |  | 581.1674 | -0.0873 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| SPY | market_regime | 738.575 |  | 738.8033 | -0.0309 | 742.515 | 738.54 | 0.019 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.22 |  | 31.6343 | 1.8516 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 417.855 |  | 416.6793 | 0.2822 | 420.72 | 412.69 | 0.0957 | watch_only | none |
| 2 | NVDA | ai_accelerator | 210.12 |  | 208.4894 | 0.7821 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| 3 | WDC | memory_hbm_storage | 566.83 |  | 564.2031 | 0.4656 | 576.24 | 556.3 | 0.3158 | watch_only | none |
| 4 | TT | data_center_power_cooling | 477.91 |  | 476.7782 | 0.2374 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | JCI | data_center_power_cooling | 144.155 |  | 143.962 | 0.1341 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ETN | data_center_power_cooling | 414.05 |  | 413.385 | 0.1609 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 4.1467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 177.23 |  | 176.719 | 0.2892 | 177.84 | 173.19 | 2.257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TER | semiconductor_test_packaging | 374.26 |  | 372.1785 | 0.5593 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SKHY | memory_hbm_storage | 174.01 |  | 173.6061 | 0.2327 | 177.88 | 168.18 | 0.4483 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | CORZ | high_beta_ai_infrastructure | 24.2 |  | 24.0531 | 0.6107 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| 12 | MU | memory_hbm_storage | 994.99 |  | 991.0777 | 0.3948 | 999.04 | 964.86 | 1.1839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SMCI | ai_server_oem | 32.22 |  | 31.6343 | 1.8516 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |
| 14 | ARM | ai_accelerator | 281.58 |  | 279.4222 | 0.7722 | 283 | 276.24 | 0.4049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | META | cloud_ai_capex | 606.26 |  | 603.8858 | 0.3931 | 614.15 | 605.39 | 1.8095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMZN | cloud_ai_capex | 234.665 |  | 234.3511 | 0.1339 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 17 | STX | memory_hbm_storage | 924.94 |  | 924.637 | 0.0328 | 933.5 | 908.955 | 4.9852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | GOOGL | cloud_ai_capex | 319.82 |  | 319.5276 | 0.0915 | 324.42 | 320.24 | 0.1626 | below_opening_15m_low | below_opening_15m_low |
| 19 | SMH | semiconductor_index | 580.66 |  | 581.1674 | -0.0873 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| 20 | SOXX | semiconductor_index | 550.15 |  | 550.983 | -0.1512 | 557.38 | 545.965 | 0.0782 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.22 |  | 31.6343 | 1.8516 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1032.99 |  | 1012.4956 | 2.0241 | 1023.33 | 979.08 | 4.7435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TSM | foundry | 417.855 |  | 416.6793 | 0.2822 | 420.72 | 412.69 | 0.0957 | watch_only | none |
| 4 | CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 4.1467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SNDK | memory_hbm_storage | 1670.805 |  | 1638.6553 | 1.962 | 1651.355 | 1560 | 3.8305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | NVDA | ai_accelerator | 210.12 |  | 208.4894 | 0.7821 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| 7 | WDC | memory_hbm_storage | 566.83 |  | 564.2031 | 0.4656 | 576.24 | 556.3 | 0.3158 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.2 |  | 24.0531 | 0.6107 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| 9 | SMH | semiconductor_index | 580.66 |  | 581.1674 | -0.0873 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 550.15 |  | 550.983 | -0.1512 | 557.38 | 545.965 | 0.0782 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 391.65 |  | 392.5854 | -0.2383 | 397.34 | 390.54 | 2.8648 | below_vwap | below_vwap,spread_too_wide |
| 12 | ASML | semiconductor_equipment | 1803.59 |  | 1804.0458 | -0.0253 | 1806.11 | 1780.9 | 0.1126 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 562.23 |  | 566.1896 | -0.6993 | 566.18 | 548.47 | 0.3202 | below_vwap | below_vwap |
| 14 | PWR | data_center_power_cooling | 650.795 |  | 652.1159 | -0.2026 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 215.6 |  | 215.7315 | -0.061 | 217.88 | 212.99 | 2.6948 | below_vwap | below_vwap,spread_too_wide |
| 16 | VRT | data_center_power_cooling | 304.19 |  | 306.3354 | -0.7003 | 311.13 | 303.96 | 1.2295 | below_vwap | below_vwap,spread_too_wide |
| 17 | IWM | market_regime | 291.43 |  | 291.6868 | -0.088 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 18 | LRCX | semiconductor_equipment | 320.39 |  | 321.3255 | -0.2911 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | SPY | market_regime | 738.575 |  | 738.8033 | -0.0309 | 742.515 | 738.54 | 0.019 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.71 |  | 693.1248 | -0.0598 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.49 |  | 66.5742 | -0.1265 | 68.245 | 66.7 | 0.015 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.12 |  | 208.4894 | 0.7821 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| MSFT | cloud_ai_capex | 381.28 |  | 382.7869 | -0.3937 | 391.71 | 387.245 | 0.8812 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.63 |  | 321.1277 | -0.155 | 323.25 | 320.82 | 0.0156 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.82 |  | 319.5276 | 0.0915 | 324.42 | 320.24 | 0.1626 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 532.485 |  | 541.9017 | -1.7377 | 556.12 | 542.33 | 1.7146 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.855 |  | 416.6793 | 0.2822 | 420.72 | 412.69 | 0.0957 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.15 |  | 550.983 | -0.1512 | 557.38 | 545.965 | 0.0782 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.66 |  | 581.1674 | -0.0873 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.65 |  | 392.5854 | -0.2383 | 397.34 | 390.54 | 2.8648 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 994.99 |  | 991.0777 | 0.3948 | 999.04 | 964.86 | 1.1839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 208.13 |  | 209.889 | -0.8381 | 213.785 | 207.665 | 1.4702 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.32 |  | 444.0718 | -0.1693 | 450.07 | 438.55 | 1.8158 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.29 |  | 48.3548 | -0.1341 | 48.88 | 47.635 | 0.0828 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.22 |  | 31.6343 | 1.8516 | 31.52 | 30.23 | 0.0621 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.575 |  | 738.8033 | -0.0309 | 742.515 | 738.54 | 0.019 | below_vwap | below_vwap |
| IWM | market_regime | 291.43 |  | 291.6868 | -0.088 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.97 |  | 122.106 | -0.9303 | 124.22 | 122.07 | 0.5291 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.6 |  | 82.8718 | -0.3279 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 304.19 |  | 306.3354 | -0.7003 | 311.13 | 303.96 | 1.2295 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.05 |  | 413.385 | 0.1609 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.795 |  | 652.1159 | -0.2026 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1032.99 |  | 1012.4956 | 2.0241 | 1023.33 | 979.08 | 4.7435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.91 |  | 476.7782 | 0.2374 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.155 |  | 143.962 | 0.1341 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.23 |  | 176.719 | 0.2892 | 177.84 | 173.19 | 2.257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316 |  | 318.26 | -0.7101 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.35 |  | 858.3687 | -1.2837 | 880.26 | 833 | 4.1329 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 4.1467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.9 |  | 114.698 | -0.6958 | 118.01 | 108.505 | 5.1097 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 327.78 |  | 327.7867 | -0.0021 | 341.68 | 327.43 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1803.59 |  | 1804.0458 | -0.0253 | 1806.11 | 1780.9 | 0.1126 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 562.23 |  | 566.1896 | -0.6993 | 566.18 | 548.47 | 0.3202 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 320.39 |  | 321.3255 | -0.2911 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.6 |  | 215.7315 | -0.061 | 217.88 | 212.99 | 2.6948 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 374.26 |  | 372.1785 | 0.5593 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.55 |  | 295.1144 | -1.2078 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.07 |  | 65.3068 | -0.3626 | 67.455 | 65.81 | 4.3799 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.95 |  | 135.3733 | -0.3127 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.69 |  | 342.8882 | 0.2339 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.65 |  | 507.5973 | -0.1866 | 510.71 | 502.72 | 0.0829 | below_vwap | below_vwap |
| APD | industrial_gases | 294.715 |  | 296.1133 | -0.4722 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.015 |  | 30.0508 | -0.1192 | 31.13 | 29.12 | 0.1333 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.94 |  | 41.7618 | -1.9678 | 43.21 | 40.51 | 0.0489 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.2 |  | 24.0531 | 0.6107 | 24.46 | 23.265 | 0.0826 | watch_only | none |
| SNDK | memory_hbm_storage | 1670.805 |  | 1638.6553 | 1.962 | 1651.355 | 1560 | 3.8305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 566.83 |  | 564.2031 | 0.4656 | 576.24 | 556.3 | 0.3158 | watch_only | none |
| STX | memory_hbm_storage | 924.94 |  | 924.637 | 0.0328 | 933.5 | 908.955 | 4.9852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.665 |  | 234.3511 | 0.1339 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.26 |  | 603.8858 | 0.3931 | 614.15 | 605.39 | 1.8095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.58 |  | 279.4222 | 0.7722 | 283 | 276.24 | 0.4049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 174.01 |  | 173.6061 | 0.2327 | 177.88 | 168.18 | 0.4483 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
