# Intraday State

- Generated at: `2026-07-22T00:22:01+08:00`
- Market time ET: `2026-07-21T12:22:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 3, 'below_vwap': 6, 'watch_only': 4, 'spread_too_wide_or_missing': 28, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.98 |  | 706.1481 | 0.401 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 552.07 |  | 547.4085 | 0.8516 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.14 |  | 579.2907 | 0.6645 | 582.03 | 576.57 | 0.0292 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.47 |  | 746.3536 | 0.2836 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 421.86 |  | 418.2545 | 0.862 | 418.76 | 415.025 | 0.2631 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.14 |  | 579.2907 | 0.6645 | 582.03 | 576.57 | 0.0292 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.07 |  | 547.4085 | 0.8516 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.98 |  | 706.1481 | 0.401 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.47 |  | 746.3536 | 0.2836 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1819.05 |  | 1806.2248 | 0.7101 | 1804.54 | 1786.51 | 0.0726 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.76 |  | 294.2764 | 0.5041 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.84 |  | 46.414 | 0.9179 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.18 |  | 23.8037 | 1.5809 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 41.93 |  | 41.6981 | 0.556 | 41.65 | 40.435 | 0.0477 | buy_precheck_manual_confirm | none |
| 11 | AAPL | mega_cap_platform | 329.18 |  | 325.565 | 1.1104 | 325.59 | 322.63 | 0.0365 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 25.305 |  | 24.7903 | 2.076 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 30.455 |  | 30.1421 | 1.0382 | 29.735 | 28.785 | 0.0985 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 71.405 |  | 70.5853 | 1.1612 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.47 |  | 746.3536 | 0.2836 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.14 |  | 579.2907 | 0.6645 | 582.03 | 576.57 | 0.0292 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 708.98 |  | 706.1481 | 0.401 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 295.76 |  | 294.2764 | 0.5041 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 349.395 |  | 349.1363 | 0.0741 | 350.985 | 347.69 | 0.0286 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 41.93 |  | 41.6981 | 0.556 | 41.65 | 40.435 | 0.0477 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1819.05 |  | 1806.2248 | 0.7101 | 1804.54 | 1786.51 | 0.0726 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 386.56 |  | 384.4597 | 0.5463 | 390.11 | 382.13 | 0.0905 | watch_only | none |
| 9 | SOXX | semiconductor_index | 552.07 |  | 547.4085 | 0.8516 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| 10 | KLAC | semiconductor_equipment | 217.435 |  | 216.2271 | 0.5586 | 220.76 | 214.41 | 0.1472 | watch_only | none |
| 11 | HPE | ai_server_oem | 46.84 |  | 46.414 | 0.9179 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 12 | ORCL | cloud_ai_capex | 125.55 |  | 125.065 | 0.3878 | 126.01 | 122.48 | 0.0478 | watch_only | none |
| 13 | TSM | foundry | 421.86 |  | 418.2545 | 0.862 | 418.76 | 415.025 | 0.2631 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 329.18 |  | 325.565 | 1.1104 | 325.59 | 322.63 | 0.0365 | buy_precheck_manual_confirm | none |
| 15 | APD | industrial_gases | 298.92 |  | 298.7675 | 0.051 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | APLD | high_beta_ai_infrastructure | 30.455 |  | 30.1421 | 1.0382 | 29.735 | 28.785 | 0.0985 | buy_precheck_manual_confirm | none |
| 17 | TT | data_center_power_cooling | 470.705 |  | 469.1582 | 0.3297 | 475.98 | 467.01 | 5.1242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ETN | data_center_power_cooling | 408 |  | 405.8607 | 0.5271 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | DELL | ai_server_oem | 405.3 |  | 402.6818 | 0.6502 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 141.59 |  | 140.7841 | 0.5724 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 421.86 |  | 418.2545 | 0.862 | 418.76 | 415.025 | 0.2631 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 583.14 |  | 579.2907 | 0.6645 | 582.03 | 576.57 | 0.0292 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 552.07 |  | 547.4085 | 0.8516 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.98 |  | 706.1481 | 0.401 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.47 |  | 746.3536 | 0.2836 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1819.05 |  | 1806.2248 | 0.7101 | 1804.54 | 1786.51 | 0.0726 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 295.76 |  | 294.2764 | 0.5041 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.84 |  | 46.414 | 0.9179 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.18 |  | 23.8037 | 1.5809 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 41.93 |  | 41.6981 | 0.556 | 41.65 | 40.435 | 0.0477 | buy_precheck_manual_confirm | none |
| 11 | AAPL | mega_cap_platform | 329.18 |  | 325.565 | 1.1104 | 325.59 | 322.63 | 0.0365 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 25.305 |  | 24.7903 | 2.076 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 30.455 |  | 30.1421 | 1.0382 | 29.735 | 28.785 | 0.0985 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 71.405 |  | 70.5853 | 1.1612 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| 15 | AMD | ai_accelerator | 535.65 |  | 531.034 | 0.8692 | 532.365 | 524.72 | 1.4188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 969.62 |  | 941.9509 | 2.9374 | 944.99 | 923 | 0.6332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 833.7 |  | 820.6044 | 1.5958 | 823.31 | 800.37 | 0.5182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 410.69 |  | 404.9463 | 1.4184 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMAT | semiconductor_equipment | 566.67 |  | 563.1717 | 0.6212 | 564.91 | 552.71 | 2.91 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 210.01 |  | 207.243 | 1.3351 | 208.61 | 205.31 | 0.9238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.98 |  | 706.1481 | 0.401 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.405 |  | 70.5853 | 1.1612 | 70.84 | 70.09 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.69 |  | 206.1292 | -0.2131 | 208.61 | 206.275 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 397.79 |  | 399.2831 | -0.3739 | 401.45 | 396.36 | 0.3771 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 329.18 |  | 325.565 | 1.1104 | 325.59 | 322.63 | 0.0365 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 349.395 |  | 349.1363 | 0.0741 | 350.985 | 347.69 | 0.0286 | watch_only | none |
| AMD | ai_accelerator | 535.65 |  | 531.034 | 0.8692 | 532.365 | 524.72 | 1.4188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.86 |  | 418.2545 | 0.862 | 418.76 | 415.025 | 0.2631 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.07 |  | 547.4085 | 0.8516 | 550.77 | 545.11 | 0.0598 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 583.14 |  | 579.2907 | 0.6645 | 582.03 | 576.57 | 0.0292 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.56 |  | 384.4597 | 0.5463 | 390.11 | 382.13 | 0.0905 | watch_only | none |
| MU | memory_hbm_storage | 969.62 |  | 941.9509 | 2.9374 | 944.99 | 923 | 0.6332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 210.01 |  | 207.243 | 1.3351 | 208.61 | 205.31 | 0.9238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 405.3 |  | 402.6818 | 0.6502 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.84 |  | 46.414 | 0.9179 | 46.685 | 45.835 | 0.0427 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.305 |  | 24.7903 | 2.076 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.47 |  | 746.3536 | 0.2836 | 746.6 | 744.3 | 0.0013 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.76 |  | 294.2764 | 0.5041 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.55 |  | 125.065 | 0.3878 | 126.01 | 122.48 | 0.0478 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 78.6 |  | 77.3848 | 1.5704 | 76.615 | 74.55 | 1.145 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 304.78 |  | 300.7737 | 1.332 | 305.09 | 299.13 | 2.2278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408 |  | 405.8607 | 0.5271 | 411.01 | 404.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 640.605 |  | 637.1994 | 0.5345 | 645.815 | 635.91 | 2.9066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1089.125 |  | 1098.1525 | -0.8221 | 1140.63 | 1103.815 | 0.6941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.705 |  | 469.1582 | 0.3297 | 475.98 | 467.01 | 5.1242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 142.76 |  | 141.3786 | 0.9771 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.65 |  | 175.3633 | -0.4067 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.86 |  | 309.1039 | 2.1857 | 309.72 | 302.3 | 4.5242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 833.7 |  | 820.6044 | 1.5958 | 823.31 | 800.37 | 0.5182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 410.69 |  | 404.9463 | 1.4184 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 117.05 |  | 114.1702 | 2.5224 | 109.39 | 107.58 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 324.93 |  | 326.0385 | -0.34 | 329.97 | 323.92 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1819.05 |  | 1806.2248 | 0.7101 | 1804.54 | 1786.51 | 0.0726 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 566.67 |  | 563.1717 | 0.6212 | 564.91 | 552.71 | 2.91 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 322.34 |  | 319.5015 | 0.8884 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.435 |  | 216.2271 | 0.5586 | 220.76 | 214.41 | 0.1472 | watch_only | none |
| TER | semiconductor_test_packaging | 375.045 |  | 368.6919 | 1.7231 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 298.775 |  | 295.3516 | 1.1591 | 296.68 | 291.36 | 4.6423 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.68 |  | 65.7231 | 1.4559 | 66.54 | 65 | 4.2142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.605 |  | 54.767 | 1.5301 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 141.59 |  | 140.7841 | 0.5724 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 343.97 |  | 338.9675 | 1.4758 | 340.205 | 336.3 | 4.7737 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 505.02 |  | 506.7797 | -0.3472 | 512.83 | 507.675 | 3.889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 298.92 |  | 298.7675 | 0.051 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.455 |  | 30.1421 | 1.0382 | 29.735 | 28.785 | 0.0985 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.93 |  | 41.6981 | 0.556 | 41.65 | 40.435 | 0.0477 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.18 |  | 23.8037 | 1.5809 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1570.06 |  | 1532.2642 | 2.4667 | 1540.85 | 1490.29 | 1.9044 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 551.2 |  | 537.8109 | 2.4895 | 533.56 | 517.335 | 4.8639 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 896.52 |  | 873.5844 | 2.6255 | 866.73 | 845.78 | 1.1545 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.39 |  | 247.7458 | -0.1436 | 248.915 | 247.32 | 0.0566 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.06 |  | 647.4086 | -0.0538 | 655.425 | 643.54 | 0.0572 | below_vwap | below_vwap |
| ARM | ai_accelerator | 291.09 |  | 285.1887 | 2.0693 | 286.39 | 275.86 | 3.0953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.73 |  | 165.0923 | 0.992 | 165.88 | 160.77 | 0.4018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
