# Intraday State

- Generated at: `2026-07-21T23:05:58+08:00`
- Market time ET: `2026-07-21T11:05:59-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 12, 'below_opening_15m_low': 4, 'below_vwap': 13, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 21}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.075 |  | 705.122 | 0.1352 | 707.09 | 704.52 | 0.0057 | watch_only | none |
| SOXX | semiconductor_index | 547.62 |  | 546.3743 | 0.228 | 550.77 | 545.11 | 0.0803 | watch_only | none |
| SMH | semiconductor_index | 579 |  | 577.3074 | 0.2932 | 582.03 | 576.57 | 0.0432 | watch_only | none |
| SPY | market_regime | 746 |  | 745.6784 | 0.0431 | 746.6 | 744.3 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 176.735 |  | 175.2564 | 0.8437 | 176.06 | 172.32 | 0.3395 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 23.72 |  | 23.563 | 0.6663 | 23.32 | 22.79 | 0.1686 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.505 |  | 324.6863 | 0.5602 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | APLD | high_beta_ai_infrastructure | 30.055 |  | 29.8031 | 0.8452 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 326.505 |  | 324.6863 | 0.5602 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 579 |  | 577.3074 | 0.2932 | 582.03 | 576.57 | 0.0432 | watch_only | none |
| 3 | SOXX | semiconductor_index | 547.62 |  | 546.3743 | 0.228 | 550.77 | 545.11 | 0.0803 | watch_only | none |
| 4 | QQQ | market_regime | 706.075 |  | 705.122 | 0.1352 | 707.09 | 704.52 | 0.0057 | watch_only | none |
| 5 | SPY | market_regime | 746 |  | 745.6784 | 0.0431 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| 6 | IWM | market_regime | 294.28 |  | 294.0516 | 0.0777 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| 7 | KLAC | semiconductor_equipment | 215.86 |  | 215.7946 | 0.0303 | 220.76 | 214.41 | 0.0973 | watch_only | none |
| 8 | HPE | ai_server_oem | 46.365 |  | 46.293 | 0.1555 | 46.685 | 45.835 | 0.0863 | watch_only | none |
| 9 | TSM | foundry | 418.58 |  | 417.0457 | 0.3679 | 418.76 | 415.025 | 0.1433 | watch_only | none |
| 10 | AMAT | semiconductor_equipment | 563.76 |  | 561.6727 | 0.3716 | 564.91 | 552.71 | 0.0798 | watch_only | none |
| 11 | SMCI | ai_server_oem | 24.76 |  | 24.6412 | 0.4823 | 24.77 | 24.34 | 0.0404 | watch_only | none |
| 12 | ANET | ai_networking_optical | 176.735 |  | 175.2564 | 0.8437 | 176.06 | 172.32 | 0.3395 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 23.72 |  | 23.563 | 0.6663 | 23.32 | 22.79 | 0.1686 | buy_precheck_manual_confirm | none |
| 14 | DELL | ai_server_oem | 402.705 |  | 402.425 | 0.0696 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APLD | high_beta_ai_infrastructure | 30.055 |  | 29.8031 | 0.8452 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |
| 16 | ENTG | semiconductor_materials | 140.23 |  | 140.1076 | 0.0874 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | LRCX | semiconductor_equipment | 319.97 |  | 318.5473 | 0.4466 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SNDK | memory_hbm_storage | 1539.36 |  | 1521.0665 | 1.2027 | 1540.85 | 1490.29 | 0.3131 | watch_only | none |
| 19 | JCI | data_center_power_cooling | 141.2 |  | 140.5141 | 0.4881 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CRWV | gpu_cloud_ai_factory | 76.92 |  | 76.6752 | 0.3192 | 76.615 | 74.55 | 3.4841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 176.735 |  | 175.2564 | 0.8437 | 176.06 | 172.32 | 0.3395 | buy_precheck_manual_confirm | none |
| 2 | CORZ | high_beta_ai_infrastructure | 23.72 |  | 23.563 | 0.6663 | 23.32 | 22.79 | 0.1686 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 326.505 |  | 324.6863 | 0.5602 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | APLD | high_beta_ai_infrastructure | 30.055 |  | 29.8031 | 0.8452 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 948.075 |  | 933.5777 | 1.5529 | 944.99 | 923 | 0.4209 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ASML | semiconductor_equipment | 1808.4 |  | 1799.0716 | 0.5185 | 1804.54 | 1786.51 | 0.8234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LITE | ai_networking_optical | 826.6 |  | 817.3487 | 1.1319 | 823.31 | 800.37 | 1.3549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | CIEN | ai_networking_optical | 407.72 |  | 402.6384 | 1.2621 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | STX | memory_hbm_storage | 881.1 |  | 866.2317 | 1.7164 | 866.73 | 845.78 | 2.2551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ARM | ai_accelerator | 287.42 |  | 283.7445 | 1.2953 | 286.39 | 275.86 | 0.9394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | WDC | memory_hbm_storage | 545.315 |  | 535.319 | 1.8673 | 533.56 | 517.335 | 0.7849 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 371.66 |  | 366.1057 | 1.5171 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 418.58 |  | 417.0457 | 0.3679 | 418.76 | 415.025 | 0.1433 | watch_only | none |
| 14 | SMH | semiconductor_index | 579 |  | 577.3074 | 0.2932 | 582.03 | 576.57 | 0.0432 | watch_only | none |
| 15 | COHR | ai_networking_optical | 310.44 |  | 306.43 | 1.3086 | 309.72 | 302.3 | 0.5154 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ONTO | semiconductor_test_packaging | 297.03 |  | 293.5842 | 1.1737 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SOXX | semiconductor_index | 547.62 |  | 546.3743 | 0.228 | 550.77 | 545.11 | 0.0803 | watch_only | none |
| 18 | QQQ | market_regime | 706.075 |  | 705.122 | 0.1352 | 707.09 | 704.52 | 0.0057 | watch_only | none |
| 19 | SKHY | memory_hbm_storage | 166.86 |  | 164.2646 | 1.58 | 165.88 | 160.77 | 2.2174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SPY | market_regime | 746 |  | 745.6784 | 0.0431 | 746.6 | 744.3 | 0.0054 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.075 |  | 705.122 | 0.1352 | 707.09 | 704.52 | 0.0057 | watch_only | none |
| TQQQ | leveraged_tool | 70.57 |  | 70.3564 | 0.3037 | 70.84 | 70.09 | 0.0142 | watch_only | none |
| NVDA | ai_accelerator | 205.58 |  | 206.1033 | -0.2539 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.715 |  | 399.6617 | -0.2369 | 401.45 | 396.36 | 0.0627 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 326.505 |  | 324.6863 | 0.5602 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.37 |  | 349.3632 | -0.2843 | 350.985 | 347.69 | 0.1952 | below_vwap | below_vwap |
| AMD | ai_accelerator | 528.12 |  | 529.4298 | -0.2474 | 532.365 | 524.72 | 0.7082 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 418.58 |  | 417.0457 | 0.3679 | 418.76 | 415.025 | 0.1433 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.62 |  | 546.3743 | 0.228 | 550.77 | 545.11 | 0.0803 | watch_only | none |
| SMH | semiconductor_index | 579 |  | 577.3074 | 0.2932 | 582.03 | 576.57 | 0.0432 | watch_only | none |
| AVGO | custom_silicon_networking | 383.475 |  | 383.8564 | -0.0994 | 390.11 | 382.13 | 0.3599 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 948.075 |  | 933.5777 | 1.5529 | 944.99 | 923 | 0.4209 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.255 |  | 206.2112 | 0.5062 | 208.61 | 205.31 | 0.69 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.705 |  | 402.425 | 0.0696 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.365 |  | 46.293 | 0.1555 | 46.685 | 45.835 | 0.0863 | watch_only | none |
| SMCI | ai_server_oem | 24.76 |  | 24.6412 | 0.4823 | 24.77 | 24.34 | 0.0404 | watch_only | none |
| SPY | market_regime | 746 |  | 745.6784 | 0.0431 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| IWM | market_regime | 294.28 |  | 294.0516 | 0.0777 | 294.51 | 292.72 | 0.0136 | watch_only | none |
| ORCL | cloud_ai_capex | 124.66 |  | 125.0206 | -0.2884 | 126.01 | 122.48 | 1.6846 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 76.92 |  | 76.6752 | 0.3192 | 76.615 | 74.55 | 3.4841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 301.27 |  | 300.0932 | 0.3921 | 305.09 | 299.13 | 1.6696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.37 |  | 405.6229 | -0.0624 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635.59 |  | 636.5884 | -0.1568 | 645.815 | 635.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1087.585 |  | 1101.3798 | -1.2525 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 468.035 |  | 469.0292 | -0.212 | 475.98 | 467.01 | 4.8351 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 141.2 |  | 140.5141 | 0.4881 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.735 |  | 175.2564 | 0.8437 | 176.06 | 172.32 | 0.3395 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 310.44 |  | 306.43 | 1.3086 | 309.72 | 302.3 | 0.5154 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 826.6 |  | 817.3487 | 1.1319 | 823.31 | 800.37 | 1.3549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 407.72 |  | 402.6384 | 1.2621 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 114.41 |  | 111.7493 | 2.381 | 109.39 | 107.58 | 3.0504 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 324.57 |  | 324.8066 | -0.0728 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1808.4 |  | 1799.0716 | 0.5185 | 1804.54 | 1786.51 | 0.8234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 563.76 |  | 561.6727 | 0.3716 | 564.91 | 552.71 | 0.0798 | watch_only | none |
| LRCX | semiconductor_equipment | 319.97 |  | 318.5473 | 0.4466 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.86 |  | 215.7946 | 0.0303 | 220.76 | 214.41 | 0.0973 | watch_only | none |
| TER | semiconductor_test_packaging | 371.66 |  | 366.1057 | 1.5171 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 297.03 |  | 293.5842 | 1.1737 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.96 |  | 65.4331 | 0.8052 | 66.54 | 65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.745 |  | 54.6285 | 0.2133 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 140.23 |  | 140.1076 | 0.0874 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 339.24 |  | 337.7402 | 0.4441 | 340.205 | 336.3 | 3.95 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 508.075 |  | 508.979 | -0.1776 | 512.83 | 507.675 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 298.94 |  | 299.3359 | -0.1323 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.055 |  | 29.8031 | 0.8452 | 29.735 | 28.785 | 0.0665 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.4 |  | 41.5557 | -0.3748 | 41.65 | 40.435 | 0.0483 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.72 |  | 23.563 | 0.6663 | 23.32 | 22.79 | 0.1686 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1539.36 |  | 1521.0665 | 1.2027 | 1540.85 | 1490.29 | 0.3131 | watch_only | none |
| WDC | memory_hbm_storage | 545.315 |  | 535.319 | 1.8673 | 533.56 | 517.335 | 0.7849 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 881.1 |  | 866.2317 | 1.7164 | 866.73 | 845.78 | 2.2551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.245 |  | 247.7336 | -0.1972 | 248.915 | 247.32 | 0.1537 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 646.1 |  | 647.3348 | -0.1907 | 655.425 | 643.54 | 0.2647 | below_vwap | below_vwap |
| ARM | ai_accelerator | 287.42 |  | 283.7445 | 1.2953 | 286.39 | 275.86 | 0.9394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.86 |  | 164.2646 | 1.58 | 165.88 | 160.77 | 2.2174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
