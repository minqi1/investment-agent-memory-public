# Intraday State

- Generated at: `2026-07-22T01:36:18+08:00`
- Market time ET: `2026-07-21T13:36:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 19, 'watch_only': 5, 'below_vwap': 7, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 20, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.475 |  | 706.7237 | 0.3893 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 554.2 |  | 548.6691 | 1.0081 | 550.77 | 545.11 | 0.065 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.01 |  | 580.6089 | 0.758 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.395 |  | 746.9219 | 0.1972 | 746.6 | 744.3 | 0.0067 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.43 |  | 419.7114 | 1.1243 | 418.76 | 415.025 | 0.1107 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.01 |  | 580.6089 | 0.758 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.2 |  | 548.6691 | 1.0081 | 550.77 | 545.11 | 0.065 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.475 |  | 706.7237 | 0.3893 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 543.505 |  | 533.5325 | 1.8691 | 532.365 | 524.72 | 0.3073 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 748.395 |  | 746.9219 | 0.1972 | 746.6 | 744.3 | 0.0067 | buy_precheck_manual_confirm | none |
| 7 | MU | memory_hbm_storage | 975.57 |  | 949.4127 | 2.7551 | 944.99 | 923 | 0.286 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1814.865 |  | 1810.0943 | 0.2636 | 1804.54 | 1786.51 | 0.0755 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 295.65 |  | 294.5327 | 0.3793 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.74 |  | 46.5196 | 0.4738 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1571.59 |  | 1540.3523 | 2.028 | 1540.85 | 1490.29 | 0.3003 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.57 |  | 23.9532 | 2.5752 | 23.32 | 22.79 | 0.0814 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.345 |  | 41.8565 | 1.1672 | 41.65 | 40.435 | 0.0472 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 327.15 |  | 326.1521 | 0.306 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 15 | AAOI | ai_networking_optical | 119.18 |  | 115.9017 | 2.8285 | 109.39 | 107.58 | 0.2937 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.285 |  | 24.8642 | 1.6922 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 79.99 |  | 78.3006 | 2.1576 | 76.615 | 74.55 | 0.325 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.715 |  | 30.2584 | 1.5091 | 29.735 | 28.785 | 0.0651 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.54 |  | 70.761 | 1.1009 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.395 |  | 746.9219 | 0.1972 | 746.6 | 744.3 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1814.865 |  | 1810.0943 | 0.2636 | 1804.54 | 1786.51 | 0.0755 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.15 |  | 326.1521 | 0.306 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.475 |  | 706.7237 | 0.3893 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.74 |  | 46.5196 | 0.4738 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 585.01 |  | 580.6089 | 0.758 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| 7 | NVDA | ai_accelerator | 206.69 |  | 205.992 | 0.3388 | 208.61 | 206.275 | 0.0145 | watch_only | none |
| 8 | IWM | market_regime | 295.65 |  | 294.5327 | 0.3793 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.22 |  | 247.7684 | 0.1823 | 248.915 | 247.32 | 0.0564 | watch_only | none |
| 10 | TT | data_center_power_cooling | 470.55 |  | 469.7809 | 0.1637 | 475.98 | 467.01 | 0.187 | watch_only | none |
| 11 | AVGO | custom_silicon_networking | 386.44 |  | 384.7727 | 0.4333 | 390.11 | 382.13 | 0.1061 | watch_only | none |
| 12 | SOXX | semiconductor_index | 554.2 |  | 548.6691 | 1.0081 | 550.77 | 545.11 | 0.065 | buy_precheck_manual_confirm | none |
| 13 | KLAC | semiconductor_equipment | 218.18 |  | 216.7081 | 0.6792 | 220.76 | 214.41 | 0.1879 | watch_only | none |
| 14 | TSM | foundry | 424.43 |  | 419.7114 | 1.1243 | 418.76 | 415.025 | 0.1107 | buy_precheck_manual_confirm | none |
| 15 | JCI | data_center_power_cooling | 142.2 |  | 141.8003 | 0.2819 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | DELL | ai_server_oem | 403.81 |  | 403.5374 | 0.0676 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | APD | industrial_gases | 300.06 |  | 299.1941 | 0.2894 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | IREN | high_beta_ai_infrastructure | 42.345 |  | 41.8565 | 1.1672 | 41.65 | 40.435 | 0.0472 | buy_precheck_manual_confirm | none |
| 19 | ENTG | semiconductor_materials | 142.315 |  | 141.455 | 0.608 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 641 |  | 638.2767 | 0.4267 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.43 |  | 419.7114 | 1.1243 | 418.76 | 415.025 | 0.1107 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.01 |  | 580.6089 | 0.758 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.2 |  | 548.6691 | 1.0081 | 550.77 | 545.11 | 0.065 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.475 |  | 706.7237 | 0.3893 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 543.505 |  | 533.5325 | 1.8691 | 532.365 | 524.72 | 0.3073 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 748.395 |  | 746.9219 | 0.1972 | 746.6 | 744.3 | 0.0067 | buy_precheck_manual_confirm | none |
| 7 | MU | memory_hbm_storage | 975.57 |  | 949.4127 | 2.7551 | 944.99 | 923 | 0.286 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1814.865 |  | 1810.0943 | 0.2636 | 1804.54 | 1786.51 | 0.0755 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 295.65 |  | 294.5327 | 0.3793 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.74 |  | 46.5196 | 0.4738 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| 11 | SNDK | memory_hbm_storage | 1571.59 |  | 1540.3523 | 2.028 | 1540.85 | 1490.29 | 0.3003 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 24.57 |  | 23.9532 | 2.5752 | 23.32 | 22.79 | 0.0814 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.345 |  | 41.8565 | 1.1672 | 41.65 | 40.435 | 0.0472 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 327.15 |  | 326.1521 | 0.306 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 15 | AAOI | ai_networking_optical | 119.18 |  | 115.9017 | 2.8285 | 109.39 | 107.58 | 0.2937 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.285 |  | 24.8642 | 1.6922 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 79.99 |  | 78.3006 | 2.1576 | 76.615 | 74.55 | 0.325 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 30.715 |  | 30.2584 | 1.5091 | 29.735 | 28.785 | 0.0651 | buy_precheck_manual_confirm | none |
| 19 | TQQQ | leveraged_tool | 71.54 |  | 70.761 | 1.1009 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 20 | LITE | ai_networking_optical | 836.9 |  | 823.5476 | 1.6213 | 823.31 | 800.37 | 1.631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.475 |  | 706.7237 | 0.3893 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.54 |  | 70.761 | 1.1009 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.69 |  | 205.992 | 0.3388 | 208.61 | 206.275 | 0.0145 | watch_only | none |
| MSFT | cloud_ai_capex | 398.86 |  | 399.1641 | -0.0762 | 401.45 | 396.36 | 0.0426 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.15 |  | 326.1521 | 0.306 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.14 |  | 349.1782 | -0.011 | 350.985 | 347.69 | 0.1489 | below_vwap | below_vwap |
| AMD | ai_accelerator | 543.505 |  | 533.5325 | 1.8691 | 532.365 | 524.72 | 0.3073 | buy_precheck_manual_confirm | none |
| TSM | foundry | 424.43 |  | 419.7114 | 1.1243 | 418.76 | 415.025 | 0.1107 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.2 |  | 548.6691 | 1.0081 | 550.77 | 545.11 | 0.065 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.01 |  | 580.6089 | 0.758 | 582.03 | 576.57 | 0.0239 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.44 |  | 384.7727 | 0.4333 | 390.11 | 382.13 | 0.1061 | watch_only | none |
| MU | memory_hbm_storage | 975.57 |  | 949.4127 | 2.7551 | 944.99 | 923 | 0.286 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 208.94 |  | 207.5985 | 0.6462 | 208.61 | 205.31 | 1.297 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.81 |  | 403.5374 | 0.0676 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.74 |  | 46.5196 | 0.4738 | 46.685 | 45.835 | 0.0214 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.285 |  | 24.8642 | 1.6922 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.395 |  | 746.9219 | 0.1972 | 746.6 | 744.3 | 0.0067 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.65 |  | 294.5327 | 0.3793 | 294.51 | 292.72 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.65 |  | 125.4794 | 0.136 | 126.01 | 122.48 | 1.162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 79.99 |  | 78.3006 | 2.1576 | 76.615 | 74.55 | 0.325 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 305.49 |  | 301.4517 | 1.3396 | 305.09 | 299.13 | 1.8659 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.99 |  | 406.0659 | -0.0187 | 411.01 | 404.21 | 4.7809 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 641 |  | 638.2767 | 0.4267 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1086.53 |  | 1096.889 | -0.9444 | 1140.63 | 1103.815 | 0.1933 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 470.55 |  | 469.7809 | 0.1637 | 475.98 | 467.01 | 0.187 | watch_only | none |
| JCI | data_center_power_cooling | 142.2 |  | 141.8003 | 0.2819 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.39 |  | 175.1862 | -0.4545 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 318.68 |  | 311.696 | 2.2407 | 309.72 | 302.3 | 1.3838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 836.9 |  | 823.5476 | 1.6213 | 823.31 | 800.37 | 1.631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 409.25 |  | 405.4238 | 0.9438 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 119.18 |  | 115.9017 | 2.8285 | 109.39 | 107.58 | 0.2937 | buy_precheck_manual_confirm | none |
| ALAB | ai_networking_optical | 325.52 |  | 325.9535 | -0.133 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1814.865 |  | 1810.0943 | 0.2636 | 1804.54 | 1786.51 | 0.0755 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 568.58 |  | 564.2574 | 0.7661 | 564.91 | 552.71 | 0.744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 322.67 |  | 320.3879 | 0.7123 | 328.135 | 317.17 | 4.8192 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 218.18 |  | 216.7081 | 0.6792 | 220.76 | 214.41 | 0.1879 | watch_only | none |
| TER | semiconductor_test_packaging | 377.37 |  | 369.7912 | 2.0495 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.48 |  | 296.6786 | 1.6184 | 296.68 | 291.36 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 66.84 |  | 65.976 | 1.3095 | 66.54 | 65 | 3.86 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.2 |  | 54.9647 | 2.2475 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 142.315 |  | 141.455 | 0.608 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 345.68 |  | 339.8059 | 1.7287 | 340.205 | 336.3 | 4.1715 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 507.07 |  | 506.3441 | 0.1434 | 512.83 | 507.675 | 0.14 | below_opening_15m_low | below_opening_15m_low |
| APD | industrial_gases | 300.06 |  | 299.1941 | 0.2894 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.715 |  | 30.2584 | 1.5091 | 29.735 | 28.785 | 0.0651 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.345 |  | 41.8565 | 1.1672 | 41.65 | 40.435 | 0.0472 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.57 |  | 23.9532 | 2.5752 | 23.32 | 22.79 | 0.0814 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1571.59 |  | 1540.3523 | 2.028 | 1540.85 | 1490.29 | 0.3003 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 550.54 |  | 539.84 | 1.9821 | 533.56 | 517.335 | 0.8573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 892.98 |  | 876.687 | 1.8585 | 866.73 | 845.78 | 0.8701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.22 |  | 247.7684 | 0.1823 | 248.915 | 247.32 | 0.0564 | watch_only | none |
| META | cloud_ai_capex | 645.38 |  | 647.436 | -0.3176 | 655.425 | 643.54 | 2.1445 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 293.27 |  | 286.2692 | 2.4455 | 286.39 | 275.86 | 2.2778 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 169.78 |  | 165.7775 | 2.4144 | 165.88 | 160.77 | 1.0072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
