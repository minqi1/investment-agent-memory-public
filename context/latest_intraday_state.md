# Intraday State

- Generated at: `2026-07-23T22:04:05+08:00`
- Market time ET: `2026-07-23T10:04:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 22, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 1, 'watch_only': 7, 'manual_confirm_candidate': 3, 'below_opening_15m_low': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.76 |  | 696.2331 | -0.2116 | 698.65 | 693.24 | 0.0806 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 553.52 |  | 553.4823 | 0.0068 | 557.38 | 545.965 | 0.1319 | watch_only | none |
| SMH | semiconductor_index | 582.44 |  | 582.261 | 0.0307 | 585.98 | 576.635 | 0.0944 | watch_only | none |
| SPY | market_regime | 739.8 |  | 740.6369 | -0.113 | 742.515 | 738.54 | 0.0081 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1806.55 |  | 1798.5179 | 0.4466 | 1806.11 | 1780.9 | 0.1428 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 178.15 |  | 177.365 | 0.4426 | 177.84 | 173.19 | 0.2414 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.01 |  | 31.3506 | 2.1033 | 31.52 | 30.23 | 0.0625 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1806.55 |  | 1798.5179 | 0.4466 | 1806.11 | 1780.9 | 0.1428 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 582.44 |  | 582.261 | 0.0307 | 585.98 | 576.635 | 0.0944 | watch_only | none |
| 3 | SOXX | semiconductor_index | 553.52 |  | 553.4823 | 0.0068 | 557.38 | 545.965 | 0.1319 | watch_only | none |
| 4 | ANET | ai_networking_optical | 178.15 |  | 177.365 | 0.4426 | 177.84 | 173.19 | 0.2414 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 291.97 |  | 291.8751 | 0.0325 | 293.01 | 290.365 | 0.0137 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 42.38 |  | 42.2933 | 0.205 | 43.21 | 40.51 | 0.0708 | watch_only | none |
| 7 | HPE | ai_server_oem | 48.635 |  | 48.5086 | 0.2605 | 48.88 | 47.635 | 0.1851 | watch_only | none |
| 8 | LRCX | semiconductor_equipment | 320.76 |  | 320.445 | 0.0983 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | MKSI | semiconductor_materials | 345.54 |  | 344.8085 | 0.2121 | 347.68 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | LIN | industrial_gases | 507.41 |  | 506.9641 | 0.088 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | AMKR | semiconductor_test_packaging | 66.83 |  | 66.6935 | 0.2046 | 67.455 | 65.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | CORZ | high_beta_ai_infrastructure | 24.1 |  | 24.0916 | 0.0347 | 24.46 | 23.265 | 0.1245 | watch_only | none |
| 13 | APLD | high_beta_ai_infrastructure | 30.64 |  | 30.4019 | 0.7831 | 31.13 | 29.12 | 0.1305 | watch_only | none |
| 14 | TSM | foundry | 418 |  | 417.8457 | 0.0369 | 420.72 | 412.69 | 1.6746 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AVGO | custom_silicon_networking | 394.43 |  | 394.2196 | 0.0534 | 397.34 | 390.54 | 0.4893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 551 |  | 550.2266 | 0.1406 | 556.12 | 542.33 | 2.5172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ETN | data_center_power_cooling | 413.805 |  | 412.7738 | 0.2498 | 415.53 | 406.545 | 3.6539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ONTO | semiconductor_test_packaging | 300.555 |  | 299.5819 | 0.3248 | 301.305 | 293.685 | 0.7054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 374.54 |  | 372.6983 | 0.4941 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SKHY | memory_hbm_storage | 174.51 |  | 174.0048 | 0.2904 | 177.88 | 168.18 | 0.9169 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1806.55 |  | 1798.5179 | 0.4466 | 1806.11 | 1780.9 | 0.1428 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 178.15 |  | 177.365 | 0.4426 | 177.84 | 173.19 | 0.2414 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.01 |  | 31.3506 | 2.1033 | 31.52 | 30.23 | 0.0625 | buy_precheck_manual_confirm | none |
| 4 | PWR | data_center_power_cooling | 657.255 |  | 653.6812 | 0.5467 | 656.38 | 642.37 | 4.3499 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | COHR | ai_networking_optical | 323.345 |  | 318.5514 | 1.5048 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | CIEN | ai_networking_optical | 410.6 |  | 406.8208 | 0.929 | 408.58 | 397.9 | 0.5407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | COHU | semiconductor_test_packaging | 55.76 |  | 55.2317 | 0.9566 | 55.76 | 54.445 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | CRWV | gpu_cloud_ai_factory | 84.455 |  | 83.2245 | 1.4786 | 84.415 | 80.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 582.44 |  | 582.261 | 0.0307 | 585.98 | 576.635 | 0.0944 | watch_only | none |
| 10 | SOXX | semiconductor_index | 553.52 |  | 553.4823 | 0.0068 | 557.38 | 545.965 | 0.1319 | watch_only | none |
| 11 | IWM | market_regime | 291.97 |  | 291.8751 | 0.0325 | 293.01 | 290.365 | 0.0137 | watch_only | none |
| 12 | HPE | ai_server_oem | 48.635 |  | 48.5086 | 0.2605 | 48.88 | 47.635 | 0.1851 | watch_only | none |
| 13 | IREN | high_beta_ai_infrastructure | 42.38 |  | 42.2933 | 0.205 | 43.21 | 40.51 | 0.0708 | watch_only | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.1 |  | 24.0916 | 0.0347 | 24.46 | 23.265 | 0.1245 | watch_only | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.64 |  | 30.4019 | 0.7831 | 31.13 | 29.12 | 0.1305 | watch_only | none |
| 16 | NVDA | ai_accelerator | 208.84 |  | 209.3762 | -0.2561 | 210.85 | 208.49 | 0.0192 | below_vwap | below_vwap |
| 17 | MU | memory_hbm_storage | 983.41 |  | 985.3869 | -0.2006 | 999.04 | 964.86 | 2.4405 | below_vwap | below_vwap,spread_too_wide |
| 18 | TT | data_center_power_cooling | 476.28 |  | 476.7834 | -0.1056 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 143.905 |  | 144.0331 | -0.0889 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 215.175 |  | 216.0285 | -0.3951 | 217.88 | 212.99 | 0.172 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.76 |  | 696.2331 | -0.2116 | 698.65 | 693.24 | 0.0806 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.12 |  | 67.4606 | -0.5049 | 68.245 | 66.7 | 0.0298 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 208.84 |  | 209.3762 | -0.2561 | 210.85 | 208.49 | 0.0192 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 387.61 |  | 388.9616 | -0.3475 | 391.71 | 387.245 | 0.0697 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 320.895 |  | 321.1137 | -0.0681 | 323.25 | 320.82 | 0.0218 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 321.06 |  | 321.177 | -0.0364 | 324.42 | 320.24 | 0.3115 | below_vwap | below_vwap |
| AMD | ai_accelerator | 551 |  | 550.2266 | 0.1406 | 556.12 | 542.33 | 2.5172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 418 |  | 417.8457 | 0.0369 | 420.72 | 412.69 | 1.6746 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.52 |  | 553.4823 | 0.0068 | 557.38 | 545.965 | 0.1319 | watch_only | none |
| SMH | semiconductor_index | 582.44 |  | 582.261 | 0.0307 | 585.98 | 576.635 | 0.0944 | watch_only | none |
| AVGO | custom_silicon_networking | 394.43 |  | 394.2196 | 0.0534 | 397.34 | 390.54 | 0.4893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 983.41 |  | 985.3869 | -0.2006 | 999.04 | 964.86 | 2.4405 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 211.315 |  | 211.884 | -0.2686 | 213.785 | 207.665 | 0.2319 | below_vwap | below_vwap |
| DELL | ai_server_oem | 443.34 |  | 443.5603 | -0.0497 | 450.07 | 438.55 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.635 |  | 48.5086 | 0.2605 | 48.88 | 47.635 | 0.1851 | watch_only | none |
| SMCI | ai_server_oem | 32.01 |  | 31.3506 | 2.1033 | 31.52 | 30.23 | 0.0625 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.8 |  | 740.6369 | -0.113 | 742.515 | 738.54 | 0.0081 | below_vwap | below_vwap |
| IWM | market_regime | 291.97 |  | 291.8751 | 0.0325 | 293.01 | 290.365 | 0.0137 | watch_only | none |
| ORCL | cloud_ai_capex | 124.02 |  | 123.4197 | 0.4864 | 124.22 | 122.07 | 3.7091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 84.455 |  | 83.2245 | 1.4786 | 84.415 | 80.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 310.05 |  | 308.2664 | 0.5786 | 311.13 | 303.96 | 3.7059 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 413.805 |  | 412.7738 | 0.2498 | 415.53 | 406.545 | 3.6539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 657.255 |  | 653.6812 | 0.5467 | 656.38 | 642.37 | 4.3499 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1016.57 |  | 1006.5794 | 0.9925 | 1023.33 | 979.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 476.28 |  | 476.7834 | -0.1056 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.905 |  | 144.0331 | -0.0889 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 178.15 |  | 177.365 | 0.4426 | 177.84 | 173.19 | 0.2414 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 323.345 |  | 318.5514 | 1.5048 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 873 |  | 873.1143 | -0.0131 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 410.6 |  | 406.8208 | 0.929 | 408.58 | 397.9 | 0.5407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 117.73 |  | 116.1629 | 1.3491 | 118.01 | 108.505 | 0.5266 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 338.81 |  | 335.6569 | 0.9394 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.55 |  | 1798.5179 | 0.4466 | 1806.11 | 1780.9 | 0.1428 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 565.79 |  | 561.5218 | 0.7601 | 566.18 | 548.47 | 1.1471 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.76 |  | 320.445 | 0.0983 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.175 |  | 216.0285 | -0.3951 | 217.88 | 212.99 | 0.172 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 374.54 |  | 372.6983 | 0.4941 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 300.555 |  | 299.5819 | 0.3248 | 301.305 | 293.685 | 0.7054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.83 |  | 66.6935 | 0.2046 | 67.455 | 65.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.76 |  | 55.2317 | 0.9566 | 55.76 | 54.445 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.52 |  | 136.9529 | -0.3161 | 137.81 | 135.66 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.54 |  | 344.8085 | 0.2121 | 347.68 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 507.41 |  | 506.9641 | 0.088 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297 |  | 297.366 | -0.1231 | 299.26 | 295.795 | 0.2525 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 30.64 |  | 30.4019 | 0.7831 | 31.13 | 29.12 | 0.1305 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 42.38 |  | 42.2933 | 0.205 | 43.21 | 40.51 | 0.0708 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 24.1 |  | 24.0916 | 0.0347 | 24.46 | 23.265 | 0.1245 | watch_only | none |
| SNDK | memory_hbm_storage | 1611.705 |  | 1618.1798 | -0.4001 | 1651.355 | 1560 | 1.9371 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 559.155 |  | 567.9817 | -1.5541 | 576.24 | 556.3 | 4.945 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 922.985 |  | 926.7562 | -0.4069 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 235.26 |  | 236.6757 | -0.5982 | 238.285 | 235.71 | 0.17 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 609.79 |  | 610.2818 | -0.0806 | 614.15 | 605.39 | 0.3854 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 280.055 |  | 280.1623 | -0.0383 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 174.51 |  | 174.0048 | 0.2904 | 177.88 | 168.18 | 0.9169 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
