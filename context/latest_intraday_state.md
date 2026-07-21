# Intraday State

- Generated at: `2026-07-22T03:10:24+08:00`
- Market time ET: `2026-07-21T15:10:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 5, 'below_vwap': 16, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 3, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.75 |  | 707.388 | 0.1925 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 551.58 |  | 549.6036 | 0.3596 | 550.77 | 545.11 | 0.0399 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.16 |  | 581.4559 | 0.2931 | 582.03 | 576.57 | 0.0154 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.15 |  | 747.2424 | 0.1215 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.22 |  | 420.937 | 0.7799 | 418.76 | 415.025 | 0.0825 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.16 |  | 581.4559 | 0.2931 | 582.03 | 576.57 | 0.0154 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 551.58 |  | 549.6036 | 0.3596 | 550.77 | 545.11 | 0.0399 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.75 |  | 707.388 | 0.1925 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.15 |  | 747.2424 | 0.1215 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 967.72 |  | 953.9844 | 1.4398 | 944.99 | 923 | 0.3317 | buy_precheck_manual_confirm | none |
| 7 | LITE | ai_networking_optical | 833.135 |  | 825.7068 | 0.8996 | 823.31 | 800.37 | 0.0792 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 295.795 |  | 294.702 | 0.3709 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 545.57 |  | 541.19 | 0.8093 | 533.56 | 517.335 | 0.0715 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 328.25 |  | 326.3512 | 0.5818 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 126.31 |  | 125.8021 | 0.4037 | 126.01 | 122.48 | 0.0792 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 25.17 |  | 24.967 | 0.8131 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.39 |  | 70.8285 | 0.7928 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 583.16 |  | 581.4559 | 0.2931 | 582.03 | 576.57 | 0.0154 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.75 |  | 707.388 | 0.1925 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 748.15 |  | 747.2424 | 0.1215 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 551.58 |  | 549.6036 | 0.3596 | 550.77 | 545.11 | 0.0399 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 206.51 |  | 206.1157 | 0.1913 | 208.61 | 206.275 | 0.0097 | watch_only | none |
| 6 | ORCL | cloud_ai_capex | 126.31 |  | 125.8021 | 0.4037 | 126.01 | 122.48 | 0.0792 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.795 |  | 294.702 | 0.3709 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 217.165 |  | 216.9783 | 0.0861 | 220.76 | 214.41 | 0.0737 | watch_only | none |
| 9 | JCI | data_center_power_cooling | 142.06 |  | 141.8742 | 0.131 | 142.15 | 140.105 | 0.0634 | watch_only | none |
| 10 | GOOGL | cloud_ai_capex | 349.33 |  | 349.1095 | 0.0632 | 350.985 | 347.69 | 0.02 | watch_only | none |
| 11 | TSM | foundry | 424.22 |  | 420.937 | 0.7799 | 418.76 | 415.025 | 0.0825 | buy_precheck_manual_confirm | none |
| 12 | META | cloud_ai_capex | 648.69 |  | 647.3581 | 0.2057 | 655.425 | 643.54 | 0.2744 | watch_only | none |
| 13 | AAPL | mega_cap_platform | 328.25 |  | 326.3512 | 0.5818 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 14 | LITE | ai_networking_optical | 833.135 |  | 825.7068 | 0.8996 | 823.31 | 800.37 | 0.0792 | buy_precheck_manual_confirm | none |
| 15 | LRCX | semiconductor_equipment | 321.21 |  | 320.559 | 0.2031 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | WDC | memory_hbm_storage | 545.57 |  | 541.19 | 0.8093 | 533.56 | 517.335 | 0.0715 | buy_precheck_manual_confirm | none |
| 17 | AMAT | semiconductor_equipment | 565.04 |  | 564.804 | 0.0418 | 564.91 | 552.71 | 1.1433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MU | memory_hbm_storage | 967.72 |  | 953.9844 | 1.4398 | 944.99 | 923 | 0.3317 | buy_precheck_manual_confirm | none |
| 19 | SMCI | ai_server_oem | 25.17 |  | 24.967 | 0.8131 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 20 | AVGO | custom_silicon_networking | 385.5 |  | 384.9571 | 0.141 | 390.11 | 382.13 | 0.4851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.22 |  | 420.937 | 0.7799 | 418.76 | 415.025 | 0.0825 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.16 |  | 581.4559 | 0.2931 | 582.03 | 576.57 | 0.0154 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 551.58 |  | 549.6036 | 0.3596 | 550.77 | 545.11 | 0.0399 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.75 |  | 707.388 | 0.1925 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.15 |  | 747.2424 | 0.1215 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 967.72 |  | 953.9844 | 1.4398 | 944.99 | 923 | 0.3317 | buy_precheck_manual_confirm | none |
| 7 | LITE | ai_networking_optical | 833.135 |  | 825.7068 | 0.8996 | 823.31 | 800.37 | 0.0792 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 295.795 |  | 294.702 | 0.3709 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 545.57 |  | 541.19 | 0.8093 | 533.56 | 517.335 | 0.0715 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 328.25 |  | 326.3512 | 0.5818 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 126.31 |  | 125.8021 | 0.4037 | 126.01 | 122.48 | 0.0792 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 25.17 |  | 24.967 | 0.8131 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.39 |  | 70.8285 | 0.7928 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 14 | CIEN | ai_networking_optical | 404.62 |  | 405.6532 | -0.2547 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | CORZ | high_beta_ai_infrastructure | 23.865 |  | 24.0139 | -0.6201 | 23.32 | 22.79 | 0.0419 | below_vwap | below_vwap |
| 16 | CRWV | gpu_cloud_ai_factory | 78.025 |  | 78.5341 | -0.6483 | 76.615 | 74.55 | 3.1016 | below_vwap | below_vwap,spread_too_wide |
| 17 | APLD | high_beta_ai_infrastructure | 29.83 |  | 30.2737 | -1.4657 | 29.735 | 28.785 | 0.0335 | below_vwap | below_vwap |
| 18 | AMD | ai_accelerator | 542.18 |  | 535.6818 | 1.2131 | 532.365 | 524.72 | 0.7913 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 565.04 |  | 564.804 | 0.0418 | 564.91 | 552.71 | 1.1433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 891.01 |  | 879.5855 | 1.2989 | 866.73 | 845.78 | 1.119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.75 |  | 707.388 | 0.1925 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.39 |  | 70.8285 | 0.7928 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.51 |  | 206.1157 | 0.1913 | 208.61 | 206.275 | 0.0097 | watch_only | none |
| MSFT | cloud_ai_capex | 399.025 |  | 399.0784 | -0.0134 | 401.45 | 396.36 | 0.0175 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.25 |  | 326.3512 | 0.5818 | 325.59 | 322.63 | 0.0091 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.33 |  | 349.1095 | 0.0632 | 350.985 | 347.69 | 0.02 | watch_only | none |
| AMD | ai_accelerator | 542.18 |  | 535.6818 | 1.2131 | 532.365 | 524.72 | 0.7913 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 424.22 |  | 420.937 | 0.7799 | 418.76 | 415.025 | 0.0825 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.58 |  | 549.6036 | 0.3596 | 550.77 | 545.11 | 0.0399 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.16 |  | 581.4559 | 0.2931 | 582.03 | 576.57 | 0.0154 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.5 |  | 384.9571 | 0.141 | 390.11 | 382.13 | 0.4851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 967.72 |  | 953.9844 | 1.4398 | 944.99 | 923 | 0.3317 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 207.34 |  | 207.7625 | -0.2033 | 208.61 | 205.31 | 1.0369 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.03 |  | 403.5792 | -0.1361 | 405.78 | 397.185 | 4.759 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.17 |  | 46.523 | -0.7589 | 46.685 | 45.835 | 0.0217 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.17 |  | 24.967 | 0.8131 | 24.77 | 24.34 | 0.0397 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.15 |  | 747.2424 | 0.1215 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.795 |  | 294.702 | 0.3709 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.31 |  | 125.8021 | 0.4037 | 126.01 | 122.48 | 0.0792 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 78.025 |  | 78.5341 | -0.6483 | 76.615 | 74.55 | 3.1016 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.22 |  | 302.083 | 0.3764 | 305.09 | 299.13 | 1.6655 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.79 |  | 405.6701 | -0.71 | 411.01 | 404.21 | 0.1018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 637.75 |  | 638.7439 | -0.1556 | 645.815 | 635.91 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1079.6 |  | 1094.9063 | -1.398 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 471.26 |  | 470.1228 | 0.2419 | 475.98 | 467.01 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| JCI | data_center_power_cooling | 142.06 |  | 141.8742 | 0.131 | 142.15 | 140.105 | 0.0634 | watch_only | none |
| ANET | ai_networking_optical | 174.23 |  | 175.0519 | -0.4695 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.31 |  | 313.1665 | 0.6845 | 309.72 | 302.3 | 1.627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 833.135 |  | 825.7068 | 0.8996 | 823.31 | 800.37 | 0.0792 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 404.62 |  | 405.6532 | -0.2547 | 401.91 | 397.18 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 118.785 |  | 116.6221 | 1.8547 | 109.39 | 107.58 | 4.2093 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 319.915 |  | 324.9113 | -1.5378 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1803.78 |  | 1809.2725 | -0.3036 | 1804.54 | 1786.51 | 0.0615 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.04 |  | 564.804 | 0.0418 | 564.91 | 552.71 | 1.1433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.21 |  | 320.559 | 0.2031 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.165 |  | 216.9783 | 0.0861 | 220.76 | 214.41 | 0.0737 | watch_only | none |
| TER | semiconductor_test_packaging | 378.01 |  | 372.0821 | 1.5932 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 299.81 |  | 297.4641 | 0.7886 | 296.68 | 291.36 | 4.793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.56 |  | 66.1998 | 0.5441 | 66.54 | 65 | 4.5222 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.745 |  | 141.3671 | -1.1474 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 344.59 |  | 340.4655 | 1.2114 | 340.205 | 336.3 | 4.4836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.34 |  | 506.39 | -0.0099 | 512.83 | 507.675 | 0.2607 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 298.195 |  | 299.2336 | -0.3471 | 301.84 | 296.5 | 4.4769 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.83 |  | 30.2737 | -1.4657 | 29.735 | 28.785 | 0.0335 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.59 |  | 41.6838 | -2.624 | 41.65 | 40.435 | 0.0493 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.865 |  | 24.0139 | -0.6201 | 23.32 | 22.79 | 0.0419 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1553.86 |  | 1544.1114 | 0.6313 | 1540.85 | 1490.29 | 1.7724 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 545.57 |  | 541.19 | 0.8093 | 533.56 | 517.335 | 0.0715 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 891.01 |  | 879.5855 | 1.2989 | 866.73 | 845.78 | 1.119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.66 |  | 247.8268 | -0.0673 | 248.915 | 247.32 | 0.0404 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.69 |  | 647.3581 | 0.2057 | 655.425 | 643.54 | 0.2744 | watch_only | none |
| ARM | ai_accelerator | 287.91 |  | 286.8997 | 0.3521 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 171.05 |  | 167.3895 | 2.1868 | 165.88 | 160.77 | 0.4619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
