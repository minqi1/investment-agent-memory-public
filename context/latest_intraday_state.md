# Intraday State

- Generated at: `2026-07-22T00:01:43+08:00`
- Market time ET: `2026-07-21T12:01:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 16, 'below_opening_15m_low': 3, 'below_vwap': 6, 'watch_only': 6, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.86 |  | 705.878 | 0.2808 | 707.09 | 704.52 | 0.0057 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 549.26 |  | 547.1971 | 0.377 | 550.77 | 545.11 | 0.0619 | watch_only | none |
| SMH | semiconductor_index | 580.47 |  | 579.1733 | 0.2239 | 582.03 | 576.57 | 0.0362 | watch_only | none |
| SPY | market_regime | 747.72 |  | 746.1957 | 0.2043 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 420.02 |  | 417.9552 | 0.494 | 418.76 | 415.025 | 0.1286 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 707.86 |  | 705.878 | 0.2808 | 707.09 | 704.52 | 0.0057 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 747.72 |  | 746.1957 | 0.2043 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 954.405 |  | 939.1569 | 1.6236 | 944.99 | 923 | 0.1153 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1811.87 |  | 1805.0427 | 0.3782 | 1804.54 | 1786.51 | 0.0762 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.365 |  | 294.2148 | 0.3909 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | STX | memory_hbm_storage | 888.36 |  | 872.0731 | 1.8676 | 866.73 | 845.78 | 0.2274 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.77 |  | 46.3915 | 0.8158 | 46.685 | 45.835 | 0.0641 | buy_precheck_manual_confirm | none |
| 9 | ARM | ai_accelerator | 290.28 |  | 284.827 | 1.9145 | 286.39 | 275.86 | 0.2825 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.065 |  | 23.7813 | 1.1928 | 23.32 | 22.79 | 0.0416 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 41.765 |  | 41.676 | 0.2135 | 41.65 | 40.435 | 0.0479 | buy_precheck_manual_confirm | none |
| 12 | AAPL | mega_cap_platform | 328.73 |  | 325.3212 | 1.0478 | 325.59 | 322.63 | 0.2434 | buy_precheck_manual_confirm | none |
| 13 | SMCI | ai_server_oem | 25.185 |  | 24.7606 | 1.7141 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 14 | CRWV | gpu_cloud_ai_factory | 78.015 |  | 77.2051 | 1.0491 | 76.615 | 74.55 | 0.0897 | buy_precheck_manual_confirm | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.43 |  | 30.0963 | 1.1087 | 29.735 | 28.785 | 0.0657 | buy_precheck_manual_confirm | none |
| 16 | TQQQ | leveraged_tool | 71.05 |  | 70.552 | 0.7059 | 70.84 | 70.09 | 0.0281 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.86 |  | 705.878 | 0.2808 | 707.09 | 704.52 | 0.0057 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 747.72 |  | 746.1957 | 0.2043 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 41.765 |  | 41.676 | 0.2135 | 41.65 | 40.435 | 0.0479 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 420.02 |  | 417.9552 | 0.494 | 418.76 | 415.025 | 0.1286 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.365 |  | 294.2148 | 0.3909 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1811.87 |  | 1805.0427 | 0.3782 | 1804.54 | 1786.51 | 0.0762 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 580.47 |  | 579.1733 | 0.2239 | 582.03 | 576.57 | 0.0362 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 216.43 |  | 216.1369 | 0.1356 | 220.76 | 214.41 | 0.1294 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 247.98 |  | 247.7578 | 0.0897 | 248.915 | 247.32 | 0.0363 | watch_only | none |
| 10 | ORCL | cloud_ai_capex | 125.15 |  | 125.0554 | 0.0756 | 126.01 | 122.48 | 0.04 | watch_only | none |
| 11 | GOOGL | cloud_ai_capex | 349.42 |  | 349.1315 | 0.0826 | 350.985 | 347.69 | 0.2261 | watch_only | none |
| 12 | SOXX | semiconductor_index | 549.26 |  | 547.1971 | 0.377 | 550.77 | 545.11 | 0.0619 | watch_only | none |
| 13 | HPE | ai_server_oem | 46.77 |  | 46.3915 | 0.8158 | 46.685 | 45.835 | 0.0641 | buy_precheck_manual_confirm | none |
| 14 | LRCX | semiconductor_equipment | 319.57 |  | 319.2931 | 0.0867 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TT | data_center_power_cooling | 469.76 |  | 469.0204 | 0.1577 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 637.59 |  | 636.76 | 0.1303 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | DELL | ai_server_oem | 403.11 |  | 402.4587 | 0.1618 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AAPL | mega_cap_platform | 328.73 |  | 325.3212 | 1.0478 | 325.59 | 322.63 | 0.2434 | buy_precheck_manual_confirm | none |
| 19 | CORZ | high_beta_ai_infrastructure | 24.065 |  | 23.7813 | 1.1928 | 23.32 | 22.79 | 0.0416 | buy_precheck_manual_confirm | none |
| 20 | CRWV | gpu_cloud_ai_factory | 78.015 |  | 77.2051 | 1.0491 | 76.615 | 74.55 | 0.0897 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 420.02 |  | 417.9552 | 0.494 | 418.76 | 415.025 | 0.1286 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 707.86 |  | 705.878 | 0.2808 | 707.09 | 704.52 | 0.0057 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 747.72 |  | 746.1957 | 0.2043 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 954.405 |  | 939.1569 | 1.6236 | 944.99 | 923 | 0.1153 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1811.87 |  | 1805.0427 | 0.3782 | 1804.54 | 1786.51 | 0.0762 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.365 |  | 294.2148 | 0.3909 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | STX | memory_hbm_storage | 888.36 |  | 872.0731 | 1.8676 | 866.73 | 845.78 | 0.2274 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.77 |  | 46.3915 | 0.8158 | 46.685 | 45.835 | 0.0641 | buy_precheck_manual_confirm | none |
| 9 | ARM | ai_accelerator | 290.28 |  | 284.827 | 1.9145 | 286.39 | 275.86 | 0.2825 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.065 |  | 23.7813 | 1.1928 | 23.32 | 22.79 | 0.0416 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 41.765 |  | 41.676 | 0.2135 | 41.65 | 40.435 | 0.0479 | buy_precheck_manual_confirm | none |
| 12 | AAPL | mega_cap_platform | 328.73 |  | 325.3212 | 1.0478 | 325.59 | 322.63 | 0.2434 | buy_precheck_manual_confirm | none |
| 13 | SMCI | ai_server_oem | 25.185 |  | 24.7606 | 1.7141 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 14 | CRWV | gpu_cloud_ai_factory | 78.015 |  | 77.2051 | 1.0491 | 76.615 | 74.55 | 0.0897 | buy_precheck_manual_confirm | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.43 |  | 30.0963 | 1.1087 | 29.735 | 28.785 | 0.0657 | buy_precheck_manual_confirm | none |
| 16 | TQQQ | leveraged_tool | 71.05 |  | 70.552 | 0.7059 | 70.84 | 70.09 | 0.0281 | buy_precheck_manual_confirm | none |
| 17 | LITE | ai_networking_optical | 825.67 |  | 819.4366 | 0.7607 | 823.31 | 800.37 | 1.3286 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 408.59 |  | 404.6379 | 0.9767 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | MRVL | custom_silicon_networking | 208.7 |  | 206.9679 | 0.8369 | 208.61 | 205.31 | 1.5189 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 544.265 |  | 537.3009 | 1.2961 | 533.56 | 517.335 | 0.3675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.86 |  | 705.878 | 0.2808 | 707.09 | 704.52 | 0.0057 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.05 |  | 70.552 | 0.7059 | 70.84 | 70.09 | 0.0281 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.87 |  | 206.1337 | -0.1279 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.44 |  | 399.4593 | -0.2552 | 401.45 | 396.36 | 0.507 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 328.73 |  | 325.3212 | 1.0478 | 325.59 | 322.63 | 0.2434 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.42 |  | 349.1315 | 0.0826 | 350.985 | 347.69 | 0.2261 | watch_only | none |
| AMD | ai_accelerator | 532.175 |  | 530.9066 | 0.2389 | 532.365 | 524.72 | 1.1857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 420.02 |  | 417.9552 | 0.494 | 418.76 | 415.025 | 0.1286 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.26 |  | 547.1971 | 0.377 | 550.77 | 545.11 | 0.0619 | watch_only | none |
| SMH | semiconductor_index | 580.47 |  | 579.1733 | 0.2239 | 582.03 | 576.57 | 0.0362 | watch_only | none |
| AVGO | custom_silicon_networking | 385.815 |  | 384.3645 | 0.3774 | 390.11 | 382.13 | 1.1379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 954.405 |  | 939.1569 | 1.6236 | 944.99 | 923 | 0.1153 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 208.7 |  | 206.9679 | 0.8369 | 208.61 | 205.31 | 1.5189 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.11 |  | 402.4587 | 0.1618 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.77 |  | 46.3915 | 0.8158 | 46.685 | 45.835 | 0.0641 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.185 |  | 24.7606 | 1.7141 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.72 |  | 746.1957 | 0.2043 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.365 |  | 294.2148 | 0.3909 | 294.51 | 292.72 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.15 |  | 125.0554 | 0.0756 | 126.01 | 122.48 | 0.04 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 78.015 |  | 77.2051 | 1.0491 | 76.615 | 74.55 | 0.0897 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 303.735 |  | 300.5753 | 1.0512 | 305.09 | 299.13 | 0.4609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.19 |  | 405.7472 | 0.3556 | 411.01 | 404.21 | 4.5335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 637.59 |  | 636.76 | 0.1303 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1083.86 |  | 1098.6813 | -1.349 | 1140.63 | 1103.815 | 0.7316 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 469.76 |  | 469.0204 | 0.1577 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.815 |  | 141.244 | 0.4043 | 142.15 | 140.105 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ANET | ai_networking_optical | 175.05 |  | 175.4273 | -0.2151 | 176.06 | 172.32 | 0.2856 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 313.56 |  | 308.6261 | 1.5987 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 825.67 |  | 819.4366 | 0.7607 | 823.31 | 800.37 | 1.3286 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 408.59 |  | 404.6379 | 0.9767 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 115.01 |  | 113.8569 | 1.0128 | 109.39 | 107.58 | 4.6257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 328.255 |  | 325.9803 | 0.6978 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1811.87 |  | 1805.0427 | 0.3782 | 1804.54 | 1786.51 | 0.0762 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 562.33 |  | 563.0146 | -0.1216 | 564.91 | 552.71 | 1.8655 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.57 |  | 319.2931 | 0.0867 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.43 |  | 216.1369 | 0.1356 | 220.76 | 214.41 | 0.1294 | watch_only | none |
| TER | semiconductor_test_packaging | 372.79 |  | 368.381 | 1.1969 | 365.97 | 356.39 | 2.2452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 297.42 |  | 294.8287 | 0.8789 | 296.68 | 291.36 | 0.965 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.17 |  | 65.644 | 0.8013 | 66.54 | 65 | 4.9116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.46 |  | 54.7097 | 1.3713 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 141.66 |  | 140.6229 | 0.7375 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 342.72 |  | 338.7443 | 1.1737 | 340.205 | 336.3 | 5.112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 505.22 |  | 507.6397 | -0.4767 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 297.61 |  | 298.9265 | -0.4404 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.43 |  | 30.0963 | 1.1087 | 29.735 | 28.785 | 0.0657 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.765 |  | 41.676 | 0.2135 | 41.65 | 40.435 | 0.0479 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.065 |  | 23.7813 | 1.1928 | 23.32 | 22.79 | 0.0416 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1539.07 |  | 1530.3392 | 0.5705 | 1540.85 | 1490.29 | 4.0284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 544.265 |  | 537.3009 | 1.2961 | 533.56 | 517.335 | 0.3675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 888.36 |  | 872.0731 | 1.8676 | 866.73 | 845.78 | 0.2274 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.98 |  | 247.7578 | 0.0897 | 248.915 | 247.32 | 0.0363 | watch_only | none |
| META | cloud_ai_capex | 647.74 |  | 647.4346 | 0.0472 | 655.425 | 643.54 | 1.3123 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 290.28 |  | 284.827 | 1.9145 | 286.39 | 275.86 | 0.2825 | buy_precheck_manual_confirm | none |
| SKHY | memory_hbm_storage | 164.71 |  | 165.0368 | -0.198 | 165.88 | 160.77 | 2.981 | below_vwap | below_vwap,spread_too_wide |
