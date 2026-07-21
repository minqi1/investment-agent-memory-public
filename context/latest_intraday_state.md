# Intraday State

- Generated at: `2026-07-22T02:35:10+08:00`
- Market time ET: `2026-07-21T14:35:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 5, 'below_vwap': 12, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.925 |  | 707.1362 | 0.253 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 552.41 |  | 549.126 | 0.598 | 550.77 | 545.11 | 0.0272 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.475 |  | 580.9589 | 0.4331 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.03 |  | 747.1227 | 0.1214 | 746.6 | 744.3 | 0.0241 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 583.475 |  | 580.9589 | 0.4331 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 552.41 |  | 549.126 | 0.598 | 550.77 | 545.11 | 0.0272 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.925 |  | 707.1362 | 0.253 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| 4 | AMD | ai_accelerator | 542.21 |  | 534.8764 | 1.3711 | 532.365 | 524.72 | 0.3338 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.03 |  | 747.1227 | 0.1214 | 746.6 | 744.3 | 0.0241 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 970.155 |  | 952.5857 | 1.8444 | 944.99 | 923 | 0.1958 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 296.045 |  | 294.6602 | 0.47 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0193 | 0.232 | 23.32 | 22.79 | 0.0415 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 327.51 |  | 326.2656 | 0.3814 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.29 |  | 24.9407 | 1.4007 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 30.295 |  | 30.2899 | 0.0168 | 29.735 | 28.785 | 0.066 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.37 |  | 70.8034 | 0.8002 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 708.925 |  | 707.1362 | 0.253 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.03 |  | 747.1227 | 0.1214 | 746.6 | 744.3 | 0.0241 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 583.475 |  | 580.9589 | 0.4331 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 552.41 |  | 549.126 | 0.598 | 550.77 | 545.11 | 0.0272 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 296.045 |  | 294.6602 | 0.47 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 217.405 |  | 216.9047 | 0.2307 | 220.76 | 214.41 | 0.0368 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 327.51 |  | 326.2656 | 0.3814 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0193 | 0.232 | 23.32 | 22.79 | 0.0415 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 470.71 |  | 469.9302 | 0.1659 | 475.98 | 467.01 | 0.1848 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 30.295 |  | 30.2899 | 0.0168 | 29.735 | 28.785 | 0.066 | buy_precheck_manual_confirm | none |
| 11 | AMAT | semiconductor_equipment | 565.73 |  | 564.7379 | 0.1757 | 564.91 | 552.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 142.18 |  | 141.8596 | 0.2258 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 639.37 |  | 638.6456 | 0.1134 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | CIEN | ai_networking_optical | 406.375 |  | 405.6354 | 0.1823 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AMD | ai_accelerator | 542.21 |  | 534.8764 | 1.3711 | 532.365 | 524.72 | 0.3338 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 25.29 |  | 24.9407 | 1.4007 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 17 | AVGO | custom_silicon_networking | 385.78 |  | 384.8897 | 0.2313 | 390.11 | 382.13 | 0.3759 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MRVL | custom_silicon_networking | 207.92 |  | 207.7431 | 0.0852 | 208.61 | 205.31 | 0.5146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | META | cloud_ai_capex | 647.61 |  | 647.3709 | 0.0369 | 655.425 | 643.54 | 1.2569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | NVDA | ai_accelerator | 206.22 |  | 206.0491 | 0.0829 | 208.61 | 206.275 | 0.0097 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 583.475 |  | 580.9589 | 0.4331 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 552.41 |  | 549.126 | 0.598 | 550.77 | 545.11 | 0.0272 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.925 |  | 707.1362 | 0.253 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| 4 | AMD | ai_accelerator | 542.21 |  | 534.8764 | 1.3711 | 532.365 | 524.72 | 0.3338 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.03 |  | 747.1227 | 0.1214 | 746.6 | 744.3 | 0.0241 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 970.155 |  | 952.5857 | 1.8444 | 944.99 | 923 | 0.1958 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 296.045 |  | 294.6602 | 0.47 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0193 | 0.232 | 23.32 | 22.79 | 0.0415 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 327.51 |  | 326.2656 | 0.3814 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.29 |  | 24.9407 | 1.4007 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 30.295 |  | 30.2899 | 0.0168 | 29.735 | 28.785 | 0.066 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.37 |  | 70.8034 | 0.8002 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 13 | TSM | foundry | 423.51 |  | 420.3858 | 0.7432 | 418.76 | 415.025 | 0.3802 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | LITE | ai_networking_optical | 835.5 |  | 825.0565 | 1.2658 | 823.31 | 800.37 | 0.4309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 406.375 |  | 405.6354 | 0.1823 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMAT | semiconductor_equipment | 565.73 |  | 564.7379 | 0.1757 | 564.91 | 552.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 142.18 |  | 141.8596 | 0.2258 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 893.545 |  | 878.5509 | 1.7067 | 866.73 | 845.78 | 0.7621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ARM | ai_accelerator | 289.675 |  | 286.7132 | 1.033 | 286.39 | 275.86 | 2.3371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 548.07 |  | 540.8085 | 1.3427 | 533.56 | 517.335 | 0.8758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.925 |  | 707.1362 | 0.253 | 707.09 | 704.52 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.37 |  | 70.8034 | 0.8002 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.22 |  | 206.0491 | 0.0829 | 208.61 | 206.275 | 0.0097 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 398.645 |  | 399.1335 | -0.1224 | 401.45 | 396.36 | 0.0351 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.51 |  | 326.2656 | 0.3814 | 325.59 | 322.63 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.53 |  | 349.1579 | -0.1798 | 350.985 | 347.69 | 0.023 | below_vwap | below_vwap |
| AMD | ai_accelerator | 542.21 |  | 534.8764 | 1.3711 | 532.365 | 524.72 | 0.3338 | buy_precheck_manual_confirm | none |
| TSM | foundry | 423.51 |  | 420.3858 | 0.7432 | 418.76 | 415.025 | 0.3802 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.41 |  | 549.126 | 0.598 | 550.77 | 545.11 | 0.0272 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.475 |  | 580.9589 | 0.4331 | 582.03 | 576.57 | 0.036 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.78 |  | 384.8897 | 0.2313 | 390.11 | 382.13 | 0.3759 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 970.155 |  | 952.5857 | 1.8444 | 944.99 | 923 | 0.1958 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 207.92 |  | 207.7431 | 0.0852 | 208.61 | 205.31 | 0.5146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.5 |  | 403.5318 | -0.0079 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.415 |  | 46.5384 | -0.2651 | 46.685 | 45.835 | 0.0215 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.29 |  | 24.9407 | 1.4007 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.03 |  | 747.1227 | 0.1214 | 746.6 | 744.3 | 0.0241 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.045 |  | 294.6602 | 0.47 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.935 |  | 125.693 | 0.9882 | 126.01 | 122.48 | 1.5205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.805 |  | 78.5595 | 0.3125 | 76.615 | 74.55 | 2.043 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 304.35 |  | 301.9453 | 0.7964 | 305.09 | 299.13 | 3.8804 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 403.74 |  | 405.935 | -0.5407 | 411.01 | 404.21 | 4.5995 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 639.37 |  | 638.6456 | 0.1134 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1087.01 |  | 1095.6233 | -0.7862 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 470.71 |  | 469.9302 | 0.1659 | 475.98 | 467.01 | 0.1848 | watch_only | none |
| JCI | data_center_power_cooling | 142.18 |  | 141.8596 | 0.2258 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 173.86 |  | 175.1051 | -0.711 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 317.425 |  | 312.7968 | 1.4796 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 835.5 |  | 825.0565 | 1.2658 | 823.31 | 800.37 | 0.4309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 406.375 |  | 405.6354 | 0.1823 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 118.58 |  | 116.4367 | 1.8407 | 109.39 | 107.58 | 4.2166 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 321.66 |  | 325.5175 | -1.185 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1803.39 |  | 1809.5636 | -0.3412 | 1804.54 | 1786.51 | 0.0743 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.73 |  | 564.7379 | 0.1757 | 564.91 | 552.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 320.16 |  | 320.4843 | -0.1012 | 328.135 | 317.17 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 217.405 |  | 216.9047 | 0.2307 | 220.76 | 214.41 | 0.0368 | watch_only | none |
| TER | semiconductor_test_packaging | 377.69 |  | 371.5618 | 1.6493 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 300.27 |  | 297.2871 | 1.0034 | 296.68 | 291.36 | 4.5959 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.58 |  | 66.1523 | 0.6465 | 66.54 | 65 | 4.3557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.235 |  | 55.0993 | 2.0612 | 54.53 | 54.03 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 140.97 |  | 141.5675 | -0.4221 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.24 |  | 340.0683 | 1.5208 | 340.205 | 336.3 | 4.4751 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.42 |  | 506.3912 | 0.0057 | 512.83 | 507.675 | 4.1171 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| APD | industrial_gases | 299 |  | 299.3138 | -0.1048 | 301.84 | 296.5 | 4.7023 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.295 |  | 30.2899 | 0.0168 | 29.735 | 28.785 | 0.066 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 40.71 |  | 41.8069 | -2.6238 | 41.65 | 40.435 | 0.0737 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0193 | 0.232 | 23.32 | 22.79 | 0.0415 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1556.28 |  | 1542.9775 | 0.8621 | 1540.85 | 1490.29 | 1.9277 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 548.07 |  | 540.8085 | 1.3427 | 533.56 | 517.335 | 0.8758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 893.545 |  | 878.5509 | 1.7067 | 866.73 | 845.78 | 0.7621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.82 |  | 247.855 | -0.0141 | 248.915 | 247.32 | 0.0242 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.61 |  | 647.3709 | 0.0369 | 655.425 | 643.54 | 1.2569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 289.675 |  | 286.7132 | 1.033 | 286.39 | 275.86 | 2.3371 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 170.55 |  | 167.2119 | 1.9963 | 165.88 | 160.77 | 1.6887 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
