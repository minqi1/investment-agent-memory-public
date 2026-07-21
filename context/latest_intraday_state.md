# Intraday State

- Generated at: `2026-07-22T02:19:29+08:00`
- Market time ET: `2026-07-21T14:19:30-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 4, 'below_vwap': 11, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.505 |  | 707 | 0.3543 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 553.2 |  | 549.0562 | 0.7547 | 550.77 | 545.11 | 0.0434 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.2 |  | 580.8144 | 0.5829 | 582.03 | 576.57 | 0.0291 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.13 |  | 747.0776 | 0.1409 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 584.2 |  | 580.8144 | 0.5829 | 582.03 | 576.57 | 0.0291 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 553.2 |  | 549.0562 | 0.7547 | 550.77 | 545.11 | 0.0434 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.505 |  | 707 | 0.3543 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.13 |  | 747.0776 | 0.1409 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 567.96 |  | 564.6851 | 0.58 | 564.91 | 552.71 | 0.1532 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 208.7 |  | 207.7273 | 0.4682 | 208.61 | 205.31 | 0.3258 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 296.02 |  | 294.6368 | 0.4695 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.17 |  | 24.0126 | 0.6554 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 126.59 |  | 125.6244 | 0.7686 | 126.01 | 122.48 | 0.0395 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.365 |  | 24.9216 | 1.7791 | 24.77 | 24.34 | 0.0394 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 30.41 |  | 30.2846 | 0.414 | 29.735 | 28.785 | 0.0658 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.55 |  | 70.7906 | 1.0728 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.13 |  | 747.0776 | 0.1409 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.505 |  | 707 | 0.3543 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 584.2 |  | 580.8144 | 0.5829 | 582.03 | 576.57 | 0.0291 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 553.2 |  | 549.0562 | 0.7547 | 550.77 | 545.11 | 0.0434 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 296.02 |  | 294.6368 | 0.4695 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 208.7 |  | 207.7273 | 0.4682 | 208.61 | 205.31 | 0.3258 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 248.49 |  | 247.84 | 0.2622 | 248.915 | 247.32 | 0.0805 | watch_only | none |
| 8 | HPE | ai_server_oem | 46.565 |  | 46.5392 | 0.0554 | 46.685 | 45.835 | 0.0215 | watch_only | none |
| 9 | ORCL | cloud_ai_capex | 126.59 |  | 125.6244 | 0.7686 | 126.01 | 122.48 | 0.0395 | buy_precheck_manual_confirm | none |
| 10 | AMAT | semiconductor_equipment | 567.96 |  | 564.6851 | 0.58 | 564.91 | 552.71 | 0.1532 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 24.17 |  | 24.0126 | 0.6554 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 30.41 |  | 30.2846 | 0.414 | 29.735 | 28.785 | 0.0658 | buy_precheck_manual_confirm | none |
| 13 | TT | data_center_power_cooling | 469.97 |  | 469.9236 | 0.0099 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 639.54 |  | 638.6249 | 0.1433 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 142.02 |  | 141.8537 | 0.1172 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CIEN | ai_networking_optical | 405.94 |  | 405.6053 | 0.0825 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 385.975 |  | 384.8721 | 0.2866 | 390.11 | 382.13 | 0.3757 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 320.97 |  | 320.4817 | 0.1524 | 328.135 | 317.17 | 0.7103 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | NVDA | ai_accelerator | 206.08 |  | 206.0429 | 0.018 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low |
| 20 | KLAC | semiconductor_equipment | 217.88 |  | 216.8709 | 0.4653 | 220.76 | 214.41 | 1.4641 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 584.2 |  | 580.8144 | 0.5829 | 582.03 | 576.57 | 0.0291 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 553.2 |  | 549.0562 | 0.7547 | 550.77 | 545.11 | 0.0434 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.505 |  | 707 | 0.3543 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.13 |  | 747.0776 | 0.1409 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 567.96 |  | 564.6851 | 0.58 | 564.91 | 552.71 | 0.1532 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 208.7 |  | 207.7273 | 0.4682 | 208.61 | 205.31 | 0.3258 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 296.02 |  | 294.6368 | 0.4695 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.17 |  | 24.0126 | 0.6554 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 126.59 |  | 125.6244 | 0.7686 | 126.01 | 122.48 | 0.0395 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.365 |  | 24.9216 | 1.7791 | 24.77 | 24.34 | 0.0394 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 30.41 |  | 30.2846 | 0.414 | 29.735 | 28.785 | 0.0658 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.55 |  | 70.7906 | 1.0728 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 13 | ASML | semiconductor_equipment | 1805.095 |  | 1809.8411 | -0.2622 | 1804.54 | 1786.51 | 0.0294 | below_vwap | below_vwap |
| 14 | TSM | foundry | 423.97 |  | 420.2849 | 0.8768 | 418.76 | 415.025 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 541.6 |  | 534.6141 | 1.3067 | 532.365 | 524.72 | 2.644 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 975.69 |  | 951.9435 | 2.4945 | 944.99 | 923 | 0.3966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 837.95 |  | 824.7749 | 1.5974 | 823.31 | 800.37 | 1.5049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 405.94 |  | 405.6053 | 0.0825 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | STX | memory_hbm_storage | 896.69 |  | 878.1345 | 2.1131 | 866.73 | 845.78 | 0.4338 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 291.76 |  | 286.6291 | 1.7901 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.505 |  | 707 | 0.3543 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.55 |  | 70.7906 | 1.0728 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.08 |  | 206.0429 | 0.018 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 398.73 |  | 399.1472 | -0.1045 | 401.45 | 396.36 | 0.143 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.57 |  | 326.2435 | 0.4066 | 325.59 | 322.63 | 1.1417 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 348.91 |  | 349.1699 | -0.0744 | 350.985 | 347.69 | 0.0143 | below_vwap | below_vwap |
| AMD | ai_accelerator | 541.6 |  | 534.6141 | 1.3067 | 532.365 | 524.72 | 2.644 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.97 |  | 420.2849 | 0.8768 | 418.76 | 415.025 | 0.3821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.2 |  | 549.0562 | 0.7547 | 550.77 | 545.11 | 0.0434 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.2 |  | 580.8144 | 0.5829 | 582.03 | 576.57 | 0.0291 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.975 |  | 384.8721 | 0.2866 | 390.11 | 382.13 | 0.3757 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 975.69 |  | 951.9435 | 2.4945 | 944.99 | 923 | 0.3966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 208.7 |  | 207.7273 | 0.4682 | 208.61 | 205.31 | 0.3258 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 402.94 |  | 403.5344 | -0.1473 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.565 |  | 46.5392 | 0.0554 | 46.685 | 45.835 | 0.0215 | watch_only | none |
| SMCI | ai_server_oem | 25.365 |  | 24.9216 | 1.7791 | 24.77 | 24.34 | 0.0394 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.13 |  | 747.0776 | 0.1409 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.02 |  | 294.6368 | 0.4695 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.59 |  | 125.6244 | 0.7686 | 126.01 | 122.48 | 0.0395 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 78.95 |  | 78.5293 | 0.5357 | 76.615 | 74.55 | 1.8113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 304.5 |  | 301.866 | 0.8726 | 305.09 | 299.13 | 3.8785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 404.35 |  | 406.0352 | -0.415 | 411.01 | 404.21 | 0.0618 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 639.54 |  | 638.6249 | 0.1433 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1082.22 |  | 1095.8234 | -1.2414 | 1140.63 | 1103.815 | 1.4683 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 469.97 |  | 469.9236 | 0.0099 | 475.98 | 467.01 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.02 |  | 141.8537 | 0.1172 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.17 |  | 175.1429 | -0.5555 | 176.06 | 172.32 | 4.8688 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 317.81 |  | 312.4925 | 1.7017 | 309.72 | 302.3 | 1.7495 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 837.95 |  | 824.7749 | 1.5974 | 823.31 | 800.37 | 1.5049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 405.94 |  | 405.6053 | 0.0825 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 119.41 |  | 116.3269 | 2.6503 | 109.39 | 107.58 | 0.4104 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 322.39 |  | 325.6827 | -1.011 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.095 |  | 1809.8411 | -0.2622 | 1804.54 | 1786.51 | 0.0294 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 567.96 |  | 564.6851 | 0.58 | 564.91 | 552.71 | 0.1532 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.97 |  | 320.4817 | 0.1524 | 328.135 | 317.17 | 0.7103 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 217.88 |  | 216.8709 | 0.4653 | 220.76 | 214.41 | 1.4641 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 378.12 |  | 371.0543 | 1.9042 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 300.36 |  | 297.2178 | 1.0572 | 296.68 | 291.36 | 4.7976 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 66.72 |  | 66.1155 | 0.9143 | 66.54 | 65 | 4.1667 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.27 |  | 55.085 | 2.1513 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 141.475 |  | 141.5942 | -0.0842 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.26 |  | 340.0146 | 1.5427 | 340.205 | 336.3 | 0.4229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.76 |  | 506.3864 | 0.0738 | 512.83 | 507.675 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 299 |  | 299.252 | -0.0842 | 301.84 | 296.5 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.41 |  | 30.2846 | 0.414 | 29.735 | 28.785 | 0.0658 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 41.18 |  | 41.8507 | -1.6027 | 41.65 | 40.435 | 0.0486 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.17 |  | 24.0126 | 0.6554 | 23.32 | 22.79 | 0.0827 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1566.98 |  | 1542.306 | 1.5998 | 1540.85 | 1490.29 | 0.7971 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 550.18 |  | 540.5901 | 1.774 | 533.56 | 517.335 | 0.6107 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 896.69 |  | 878.1345 | 2.1131 | 866.73 | 845.78 | 0.4338 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.49 |  | 247.84 | 0.2622 | 248.915 | 247.32 | 0.0805 | watch_only | none |
| META | cloud_ai_capex | 647.09 |  | 647.374 | -0.0439 | 655.425 | 643.54 | 0.9767 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 291.76 |  | 286.6291 | 1.7901 | 286.39 | 275.86 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 170.42 |  | 167.1342 | 1.966 | 165.88 | 160.77 | 1.2675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
