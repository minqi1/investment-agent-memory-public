# Intraday State

- Generated at: `2026-07-18T02:23:33+08:00`
- Market time ET: `2026-07-17T14:23:34-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'watch_only': 5, 'below_vwap': 13, 'spread_too_wide_or_missing': 27, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.24 |  | 695.4779 | 0.2534 | 693.36 | 686.78 | 0.0244 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 522.4 |  | 518.1997 | 0.8106 | 511.83 | 498.665 | 0.0919 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.19 |  | 554.9426 | 0.405 | 550 | 536.9 | 0.0556 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.96 |  | 744.9574 | -0.1339 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.19 |  | 554.9426 | 0.405 | 550 | 536.9 | 0.0556 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 522.4 |  | 518.1997 | 0.8106 | 511.83 | 498.665 | 0.0919 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.63 |  | 212.1717 | 0.216 | 210.82 | 204.71 | 0.0988 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.24 |  | 695.4779 | 0.2534 | 693.36 | 686.78 | 0.0244 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.23 |  | 45.6434 | 1.2852 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.67 |  | 24.291 | 1.5601 | 24.3 | 23.46 | 0.0405 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.651 | 1.8836 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 68.045 |  | 67.1906 | 1.2715 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.24 |  | 695.4779 | 0.2534 | 693.36 | 686.78 | 0.0244 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 212.63 |  | 212.1717 | 0.216 | 210.82 | 204.71 | 0.0988 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 203.335 |  | 203.2389 | 0.0473 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| 4 | SMH | semiconductor_index | 557.19 |  | 554.9426 | 0.405 | 550 | 536.9 | 0.0556 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.52 |  | 331.9997 | 0.1567 | 334.98 | 331.295 | 0.012 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.795 |  | 33.7941 | 0.0027 | 34 | 32.26 | 0.0296 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 395.59 |  | 393.3311 | 0.5743 | 398.39 | 393.52 | 0.0859 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 25.24 |  | 25.0835 | 0.6239 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| 9 | CIEN | ai_networking_optical | 377.93 |  | 377.8493 | 0.0214 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SOXX | semiconductor_index | 522.4 |  | 518.1997 | 0.8106 | 511.83 | 498.665 | 0.0919 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 46.23 |  | 45.6434 | 1.2852 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 12 | ETN | data_center_power_cooling | 400.64 |  | 399.7323 | 0.2271 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ASML | semiconductor_equipment | 1763.92 |  | 1756.6159 | 0.4158 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMCI | ai_server_oem | 24.67 |  | 24.291 | 1.5601 | 24.3 | 23.46 | 0.0405 | buy_precheck_manual_confirm | none |
| 15 | PWR | data_center_power_cooling | 633.94 |  | 629.7952 | 0.6581 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.651 | 1.8836 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| 17 | AVGO | custom_silicon_networking | 372.56 |  | 370.1638 | 0.6473 | 368.42 | 357.97 | 2.0131 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ORCL | cloud_ai_capex | 126.82 |  | 125.9966 | 0.6535 | 125.02 | 121.79 | 1.1039 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SPY | market_regime | 743.96 |  | 744.9574 | -0.1339 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 20 | AMZN | cloud_ai_capex | 247.85 |  | 248.0129 | -0.0657 | 247.72 | 243.725 | 0.0484 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.19 |  | 554.9426 | 0.405 | 550 | 536.9 | 0.0556 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 522.4 |  | 518.1997 | 0.8106 | 511.83 | 498.665 | 0.0919 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.63 |  | 212.1717 | 0.216 | 210.82 | 204.71 | 0.0988 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.24 |  | 695.4779 | 0.2534 | 693.36 | 686.78 | 0.0244 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.23 |  | 45.6434 | 1.2852 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.67 |  | 24.291 | 1.5601 | 24.3 | 23.46 | 0.0405 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.651 | 1.8836 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 68.045 |  | 67.1906 | 1.2715 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 396.97 |  | 398.117 | -0.2881 | 394.11 | 386.02 | 2.3528 | below_vwap | below_vwap,spread_too_wide |
| 10 | TT | data_center_power_cooling | 469.685 |  | 469.794 | -0.0232 | 469.08 | 460.78 | 0.2406 | below_vwap | below_vwap |
| 11 | LRCX | semiconductor_equipment | 310.99 |  | 312.0889 | -0.3521 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | SPY | market_regime | 743.96 |  | 744.9574 | -0.1339 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 13 | ONTO | semiconductor_test_packaging | 277.53 |  | 277.5693 | -0.0141 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AMZN | cloud_ai_capex | 247.85 |  | 248.0129 | -0.0657 | 247.72 | 243.725 | 0.0484 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1418.955 |  | 1428.2658 | -0.6519 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ANET | ai_networking_optical | 168.69 |  | 166.0736 | 1.5755 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 372.56 |  | 370.1638 | 0.6473 | 368.42 | 357.97 | 2.0131 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 495.49 |  | 486.6752 | 1.8112 | 482.43 | 461.04 | 3.2372 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1763.92 |  | 1756.6159 | 0.4158 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 872.57 |  | 863.8785 | 1.0061 | 835.82 | 804.09 | 1.0555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.24 |  | 695.4779 | 0.2534 | 693.36 | 686.78 | 0.0244 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.045 |  | 67.1906 | 1.2715 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.335 |  | 203.2389 | 0.0473 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| MSFT | cloud_ai_capex | 395.59 |  | 393.3311 | 0.5743 | 398.39 | 393.52 | 0.0859 | watch_only | none |
| AAPL | mega_cap_platform | 332.52 |  | 331.9997 | 0.1567 | 334.98 | 331.295 | 0.012 | watch_only | none |
| GOOGL | cloud_ai_capex | 343.79 |  | 345.8853 | -0.6058 | 348.47 | 341.42 | 0.2007 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.49 |  | 486.6752 | 1.8112 | 482.43 | 461.04 | 3.2372 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.97 |  | 398.117 | -0.2881 | 394.11 | 386.02 | 2.3528 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 522.4 |  | 518.1997 | 0.8106 | 511.83 | 498.665 | 0.0919 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.19 |  | 554.9426 | 0.405 | 550 | 536.9 | 0.0556 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.56 |  | 370.1638 | 0.6473 | 368.42 | 357.97 | 2.0131 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 872.57 |  | 863.8785 | 1.0061 | 835.82 | 804.09 | 1.0555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 188.84 |  | 187.1022 | 0.9288 | 185.03 | 178.09 | 0.6566 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.55 |  | 392.6589 | 2.2643 | 384 | 368.28 | 4.8985 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.23 |  | 45.6434 | 1.2852 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.67 |  | 24.291 | 1.5601 | 24.3 | 23.46 | 0.0405 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.96 |  | 744.9574 | -0.1339 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.81 |  | 294.1906 | -0.1294 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.82 |  | 125.9966 | 0.6535 | 125.02 | 121.79 | 1.1039 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.485 |  | 72.1873 | 1.7977 | 71.24 | 68.65 | 3.0074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.285 |  | 287.1027 | 1.805 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.64 |  | 399.7323 | 0.2271 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 633.94 |  | 629.7952 | 0.6581 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1059.69 |  | 1044.7453 | 1.4305 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.685 |  | 469.794 | -0.0232 | 469.08 | 460.78 | 0.2406 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 140.7 |  | 140.965 | -0.188 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.69 |  | 166.0736 | 1.5755 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.12 |  | 273.9083 | 1.5376 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 734.39 |  | 716.8509 | 2.4467 | 694.98 | 653.305 | 2.1229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.93 |  | 377.8493 | 0.0214 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 102.4 |  | 100.4796 | 1.9113 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 301.83 |  | 305.2618 | -1.1242 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1763.92 |  | 1756.6159 | 0.4158 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 531.72 |  | 535.3738 | -0.6825 | 535.095 | 513.34 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 310.99 |  | 312.0889 | -0.3521 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.63 |  | 212.1717 | 0.216 | 210.82 | 204.71 | 0.0988 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 323.445 |  | 319.6917 | 1.174 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 277.53 |  | 277.5693 | -0.0141 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.26 |  | 61.4653 | 1.293 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.935 |  | 49.872 | 2.1315 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.8 |  | 134.6237 | 1.6166 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.23 |  | 318.6285 | 1.758 | 315.89 | 307.13 | 4.3179 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.04 |  | 520.0288 | -0.9593 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.235 |  | 299.116 | -0.9632 | 304.36 | 299.62 | 4.034 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.24 |  | 25.0835 | 0.6239 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.795 |  | 33.7941 | 0.0027 | 34 | 32.26 | 0.0296 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.651 | 1.8836 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1418.955 |  | 1428.2658 | -0.6519 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 480.09 |  | 466.6657 | 2.8766 | 453.35 | 431.78 | 1.8309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 787.68 |  | 759.9602 | 3.6475 | 724.57 | 702.24 | 4.3761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.85 |  | 248.0129 | -0.0657 | 247.72 | 243.725 | 0.0484 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.4 |  | 642.1585 | 0.8162 | 649.07 | 638.97 | 0.7368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.28 |  | 261.0359 | 2.7751 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 160.135 |  | 158.6243 | 0.9524 | 151.99 | 145.6 | 1.43 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
