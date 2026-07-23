# Intraday State

- Generated at: `2026-07-24T01:10:13+08:00`
- Market time ET: `2026-07-23T13:10:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 17, 'watch_only': 5, 'spread_too_wide_or_missing': 11, 'price_stale_or_missing': 1, 'below_vwap': 21, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.87 |  | 693.1294 | -0.1817 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.01 |  | 550.9879 | -0.5405 | 557.38 | 545.965 | 0.0785 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.67 |  | 581.1739 | -0.4308 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| SPY | market_regime | 738.03 |  | 738.8054 | -0.105 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.045 |  | 31.6232 | 1.3339 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 993.275 |  | 991.0293 | 0.2266 | 999.04 | 964.86 | 0.1681 | watch_only | none |
| 2 | CIEN | ai_networking_optical | 408.32 |  | 408.1964 | 0.0303 | 408.58 | 397.9 | 0.3012 | watch_only | none |
| 3 | NVDA | ai_accelerator | 209.47 |  | 208.4668 | 0.4812 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| 4 | META | cloud_ai_capex | 606.06 |  | 603.8532 | 0.3655 | 614.15 | 605.39 | 0.297 | watch_only | none |
| 5 | TT | data_center_power_cooling | 477.885 |  | 476.7683 | 0.2342 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ETN | data_center_power_cooling | 413.46 |  | 413.3786 | 0.0197 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | MKSI | semiconductor_materials | 343.69 |  | 342.8882 | 0.2339 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SMCI | ai_server_oem | 32.045 |  | 31.6232 | 1.3339 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 416.92 |  | 416.6751 | 0.0588 | 420.72 | 412.69 | 0.6956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ANET | ai_networking_optical | 176.75 |  | 176.7167 | 0.0188 | 177.84 | 173.19 | 2.2631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TER | semiconductor_test_packaging | 372.61 |  | 372.0741 | 0.144 | 376.78 | 363.37 | 4.7503 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SKHY | memory_hbm_storage | 173.62 |  | 173.6043 | 0.009 | 177.88 | 168.18 | 0.4838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0517 | 0.3672 | 24.46 | 23.265 | 0.0829 | watch_only | none |
| 14 | ARM | ai_accelerator | 280.72 |  | 279.4116 | 0.4683 | 283 | 276.24 | 4.3353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | WDC | memory_hbm_storage | 566.26 |  | 564.1954 | 0.3659 | 576.24 | 556.3 | 1.7377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMZN | cloud_ai_capex | 234.735 |  | 234.3454 | 0.1663 | 238.285 | 235.71 | 0.017 | below_opening_15m_low | below_opening_15m_low |
| 17 | SMH | semiconductor_index | 578.67 |  | 581.1739 | -0.4308 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| 18 | SOXX | semiconductor_index | 548.01 |  | 550.9879 | -0.5405 | 557.38 | 545.965 | 0.0785 | below_vwap | below_vwap |
| 19 | IWM | market_regime | 291.33 |  | 291.688 | -0.1227 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 20 | HPE | ai_server_oem | 48.165 |  | 48.3556 | -0.3942 | 48.88 | 47.635 | 0.1038 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.045 |  | 31.6232 | 1.3339 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1028.555 |  | 1012.4327 | 1.5924 | 1023.33 | 979.08 | 2.1613 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | SNDK | memory_hbm_storage | 1666.565 |  | 1638.3651 | 1.7212 | 1651.355 | 1560 | 3.8402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | NVDA | ai_accelerator | 209.47 |  | 208.4668 | 0.4812 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| 5 | MU | memory_hbm_storage | 993.275 |  | 991.0293 | 0.2266 | 999.04 | 964.86 | 0.1681 | watch_only | none |
| 6 | CIEN | ai_networking_optical | 408.32 |  | 408.1964 | 0.0303 | 408.58 | 397.9 | 0.3012 | watch_only | none |
| 7 | META | cloud_ai_capex | 606.06 |  | 603.8532 | 0.3655 | 614.15 | 605.39 | 0.297 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0517 | 0.3672 | 24.46 | 23.265 | 0.0829 | watch_only | none |
| 9 | SMH | semiconductor_index | 578.67 |  | 581.1739 | -0.4308 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 548.01 |  | 550.9879 | -0.5405 | 557.38 | 545.965 | 0.0785 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1802.45 |  | 1804.0414 | -0.0882 | 1806.11 | 1780.9 | 0.1614 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 561.41 |  | 566.2975 | -0.8631 | 566.18 | 548.47 | 2.3138 | below_vwap | below_vwap,spread_too_wide |
| 13 | JCI | data_center_power_cooling | 143.955 |  | 143.9605 | -0.0038 | 145.035 | 141.815 | 5.1058 | below_vwap | below_vwap,spread_too_wide |
| 14 | PWR | data_center_power_cooling | 650.31 |  | 652.1356 | -0.2799 | 656.38 | 642.37 | 1.3071 | below_vwap | below_vwap,spread_too_wide |
| 15 | KLAC | semiconductor_equipment | 215.24 |  | 215.7326 | -0.2284 | 217.88 | 212.99 | 2.69 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.33 |  | 291.688 | -0.1227 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 319.47 |  | 321.3388 | -0.5816 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 506.665 |  | 507.6173 | -0.1876 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | HPE | ai_server_oem | 48.165 |  | 48.3556 | -0.3942 | 48.88 | 47.635 | 0.1038 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.87 |  | 693.1294 | -0.1817 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.28 |  | 66.575 | -0.4432 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.47 |  | 208.4668 | 0.4812 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| MSFT | cloud_ai_capex | 381.42 |  | 382.8013 | -0.3608 | 391.71 | 387.245 | 0.9307 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.615 |  | 321.131 | -0.1607 | 323.25 | 320.82 | 0.0998 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.76 |  | 319.5229 | 0.0742 | 324.42 | 320.24 | 0.6661 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMD | ai_accelerator | 529.8 |  | 542.2033 | -2.2876 | 556.12 | 542.33 | 1.3986 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 416.92 |  | 416.6751 | 0.0588 | 420.72 | 412.69 | 0.6956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.01 |  | 550.9879 | -0.5405 | 557.38 | 545.965 | 0.0785 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.67 |  | 581.1739 | -0.4308 | 585.98 | 576.635 | 0.0691 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.265 |  | 392.6075 | -0.5967 | 397.34 | 390.54 | 1.3683 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 993.275 |  | 991.0293 | 0.2266 | 999.04 | 964.86 | 0.1681 | watch_only | none |
| MRVL | custom_silicon_networking | 207.2 |  | 209.9132 | -1.2925 | 213.785 | 207.665 | 2.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 442.78 |  | 444.0742 | -0.2914 | 450.07 | 438.55 | 2.3804 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.165 |  | 48.3556 | -0.3942 | 48.88 | 47.635 | 0.1038 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.045 |  | 31.6232 | 1.3339 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.03 |  | 738.8054 | -0.105 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.33 |  | 291.688 | -0.1227 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 121.05 |  | 122.115 | -0.8721 | 124.22 | 122.07 | 0.2974 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.195 |  | 82.8828 | -0.8299 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.66 |  | 306.342 | -0.8755 | 311.13 | 303.96 | 1.9594 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.46 |  | 413.3786 | 0.0197 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.31 |  | 652.1356 | -0.2799 | 656.38 | 642.37 | 1.3071 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1028.555 |  | 1012.4327 | 1.5924 | 1023.33 | 979.08 | 2.1613 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.885 |  | 476.7683 | 0.2342 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.955 |  | 143.9605 | -0.0038 | 145.035 | 141.815 | 5.1058 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 176.75 |  | 176.7167 | 0.0188 | 177.84 | 173.19 | 2.2631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.99 |  | 318.2712 | -0.7168 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 846.39 |  | 858.4058 | -1.3998 | 880.26 | 833 | 4.303 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 408.32 |  | 408.1964 | 0.0303 | 408.58 | 397.9 | 0.3012 | watch_only | none |
| AAOI | ai_networking_optical | 113.43 |  | 114.7139 | -1.1193 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.26 |  | 327.796 | -0.1635 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1802.45 |  | 1804.0414 | -0.0882 | 1806.11 | 1780.9 | 0.1614 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 561.41 |  | 566.2975 | -0.8631 | 566.18 | 548.47 | 2.3138 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.47 |  | 321.3388 | -0.5816 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.24 |  | 215.7326 | -0.2284 | 217.88 | 212.99 | 2.69 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.61 |  | 372.0741 | 0.144 | 376.78 | 363.37 | 4.7503 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 291.83 |  | 295.2211 | -1.1487 | 301.305 | 293.685 | 0.3187 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMKR | semiconductor_test_packaging | 64.96 |  | 65.3079 | -0.5327 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.905 |  | 135.386 | -0.3553 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.69 |  | 342.8882 | 0.2339 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.665 |  | 507.6173 | -0.1876 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.72 |  | 296.1516 | -0.4834 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.85 |  | 30.0513 | -0.6699 | 31.13 | 29.12 | 0.067 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.71 |  | 41.7748 | -2.549 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0517 | 0.3672 | 24.46 | 23.265 | 0.0829 | watch_only | none |
| SNDK | memory_hbm_storage | 1666.565 |  | 1638.3651 | 1.7212 | 1651.355 | 1560 | 3.8402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 566.26 |  | 564.1954 | 0.3659 | 576.24 | 556.3 | 1.7377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 922.645 |  | 924.6392 | -0.2157 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.735 |  | 234.3454 | 0.1663 | 238.285 | 235.71 | 0.017 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.06 |  | 603.8532 | 0.3655 | 614.15 | 605.39 | 0.297 | watch_only | none |
| ARM | ai_accelerator | 280.72 |  | 279.4116 | 0.4683 | 283 | 276.24 | 4.3353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.62 |  | 173.6043 | 0.009 | 177.88 | 168.18 | 0.4838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
