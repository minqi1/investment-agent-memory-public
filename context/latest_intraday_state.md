# Intraday State

- Generated at: `2026-07-18T02:19:31+08:00`
- Market time ET: `2026-07-17T14:19:31-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_vwap': 13, 'watch_only': 3, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.115 |  | 695.4698 | 0.2366 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 522.36 |  | 518.1741 | 0.8078 | 511.83 | 498.665 | 0.0976 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.62 |  | 554.9207 | 0.3062 | 550 | 536.9 | 0.0287 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.74 |  | 744.9676 | -0.1648 | 742.66 | 740.8 | 0.0175 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.62 |  | 554.9207 | 0.3062 | 550 | 536.9 | 0.0287 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 372.425 |  | 370.1527 | 0.6139 | 368.42 | 357.97 | 0.1101 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 522.36 |  | 518.1741 | 0.8078 | 511.83 | 498.665 | 0.0976 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1761.93 |  | 1756.5796 | 0.3046 | 1741.99 | 1704.935 | 0.0897 | buy_precheck_manual_confirm | none |
| 5 | GEV | data_center_power_cooling | 1058.01 |  | 1044.6923 | 1.2748 | 1001.82 | 982.21 | 0.1333 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 697.115 |  | 695.4698 | 0.2366 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.205 |  | 45.6392 | 1.2396 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| 8 | SNDK | memory_hbm_storage | 1428.48 |  | 1428.3561 | 0.0087 | 1393.96 | 1325.48 | 0.3318 | buy_precheck_manual_confirm | none |
| 9 | TER | semiconductor_test_packaging | 322.51 |  | 319.6354 | 0.8993 | 308.03 | 297.18 | 0.2015 | buy_precheck_manual_confirm | none |
| 10 | COHR | ai_networking_optical | 278.45 |  | 273.8935 | 1.6636 | 269.59 | 256.24 | 0.1544 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.66 |  | 24.2891 | 1.5272 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.6489 | 1.9427 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.05 |  | 67.1875 | 1.2837 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.115 |  | 695.4698 | 0.2366 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.62 |  | 554.9207 | 0.3062 | 550 | 536.9 | 0.0287 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1761.93 |  | 1756.5796 | 0.3046 | 1741.99 | 1704.935 | 0.0897 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 372.425 |  | 370.1527 | 0.6139 | 368.42 | 357.97 | 0.1101 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.41 |  | 331.9983 | 0.124 | 334.98 | 331.295 | 0.012 | watch_only | none |
| 6 | SNDK | memory_hbm_storage | 1428.48 |  | 1428.3561 | 0.0087 | 1393.96 | 1325.48 | 0.3318 | buy_precheck_manual_confirm | none |
| 7 | IREN | high_beta_ai_infrastructure | 33.915 |  | 33.7936 | 0.3591 | 34 | 32.26 | 0.0295 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 395.6 |  | 393.3125 | 0.5816 | 398.39 | 393.52 | 0.2578 | watch_only | none |
| 9 | SOXX | semiconductor_index | 522.36 |  | 518.1741 | 0.8078 | 511.83 | 498.665 | 0.0976 | buy_precheck_manual_confirm | none |
| 10 | GEV | data_center_power_cooling | 1058.01 |  | 1044.6923 | 1.2748 | 1001.82 | 982.21 | 0.1333 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 46.205 |  | 45.6392 | 1.2396 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| 12 | CIEN | ai_networking_optical | 377.98 |  | 377.8539 | 0.0334 | 375.52 | 359.81 | 3.8732 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TER | semiconductor_test_packaging | 322.51 |  | 319.6354 | 0.8993 | 308.03 | 297.18 | 0.2015 | buy_precheck_manual_confirm | none |
| 14 | ONTO | semiconductor_test_packaging | 277.925 |  | 277.5711 | 0.1275 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SMCI | ai_server_oem | 24.66 |  | 24.2891 | 1.5272 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 16 | ETN | data_center_power_cooling | 400.46 |  | 399.7237 | 0.1842 | 389.4 | 382.38 | 2.6594 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | PWR | data_center_power_cooling | 632.95 |  | 629.7033 | 0.5156 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.6489 | 1.9427 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| 19 | META | cloud_ai_capex | 646.52 |  | 642.1065 | 0.6873 | 649.07 | 638.97 | 0.8847 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | COHR | ai_networking_optical | 278.45 |  | 273.8935 | 1.6636 | 269.59 | 256.24 | 0.1544 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.62 |  | 554.9207 | 0.3062 | 550 | 536.9 | 0.0287 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 372.425 |  | 370.1527 | 0.6139 | 368.42 | 357.97 | 0.1101 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 522.36 |  | 518.1741 | 0.8078 | 511.83 | 498.665 | 0.0976 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1761.93 |  | 1756.5796 | 0.3046 | 1741.99 | 1704.935 | 0.0897 | buy_precheck_manual_confirm | none |
| 5 | GEV | data_center_power_cooling | 1058.01 |  | 1044.6923 | 1.2748 | 1001.82 | 982.21 | 0.1333 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 697.115 |  | 695.4698 | 0.2366 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.205 |  | 45.6392 | 1.2396 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| 8 | SNDK | memory_hbm_storage | 1428.48 |  | 1428.3561 | 0.0087 | 1393.96 | 1325.48 | 0.3318 | buy_precheck_manual_confirm | none |
| 9 | TER | semiconductor_test_packaging | 322.51 |  | 319.6354 | 0.8993 | 308.03 | 297.18 | 0.2015 | buy_precheck_manual_confirm | none |
| 10 | COHR | ai_networking_optical | 278.45 |  | 273.8935 | 1.6636 | 269.59 | 256.24 | 0.1544 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.66 |  | 24.2891 | 1.5272 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.6489 | 1.9427 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.05 |  | 67.1875 | 1.2837 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 14 | TSM | foundry | 396.98 |  | 398.126 | -0.2878 | 394.11 | 386.02 | 0.6499 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 469.685 |  | 469.794 | -0.0232 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 212.05 |  | 212.171 | -0.057 | 210.82 | 204.71 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | LRCX | semiconductor_equipment | 310.82 |  | 312.0984 | -0.4096 | 306.51 | 298.89 | 3.7385 | below_vwap | below_vwap,spread_too_wide |
| 18 | SPY | market_regime | 743.74 |  | 744.9676 | -0.1648 | 742.66 | 740.8 | 0.0175 | below_vwap | below_vwap |
| 19 | ANET | ai_networking_optical | 168.65 |  | 166.0537 | 1.5635 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 495.76 |  | 486.6416 | 1.8737 | 482.43 | 461.04 | 3.1608 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.115 |  | 695.4698 | 0.2366 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.05 |  | 67.1875 | 1.2837 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.07 |  | 203.239 | -0.0832 | 203.41 | 197.98 | 0.0936 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 395.6 |  | 393.3125 | 0.5816 | 398.39 | 393.52 | 0.2578 | watch_only | none |
| AAPL | mega_cap_platform | 332.41 |  | 331.9983 | 0.124 | 334.98 | 331.295 | 0.012 | watch_only | none |
| GOOGL | cloud_ai_capex | 343.55 |  | 345.8928 | -0.6773 | 348.47 | 341.42 | 0.0873 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.76 |  | 486.6416 | 1.8737 | 482.43 | 461.04 | 3.1608 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.98 |  | 398.126 | -0.2878 | 394.11 | 386.02 | 0.6499 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 522.36 |  | 518.1741 | 0.8078 | 511.83 | 498.665 | 0.0976 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.62 |  | 554.9207 | 0.3062 | 550 | 536.9 | 0.0287 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.425 |  | 370.1527 | 0.6139 | 368.42 | 357.97 | 0.1101 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 874.71 |  | 863.8106 | 1.2618 | 835.82 | 804.09 | 1.5868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 188.905 |  | 187.0926 | 0.9687 | 185.03 | 178.09 | 0.9052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 400.81 |  | 392.584 | 2.0954 | 384 | 368.28 | 4.8876 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.205 |  | 45.6392 | 1.2396 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.66 |  | 24.2891 | 1.5272 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.74 |  | 744.9676 | -0.1648 | 742.66 | 740.8 | 0.0175 | below_vwap | below_vwap |
| IWM | market_regime | 293.705 |  | 294.2011 | -0.1686 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.98 |  | 125.9902 | 0.7856 | 125.02 | 121.79 | 1.0395 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.52 |  | 72.1784 | 1.8587 | 71.24 | 68.65 | 3.6725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.095 |  | 287.087 | 1.7444 | 280.565 | 273.17 | 4.1904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 400.46 |  | 399.7237 | 0.1842 | 389.4 | 382.38 | 2.6594 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 632.95 |  | 629.7033 | 0.5156 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1058.01 |  | 1044.6923 | 1.2748 | 1001.82 | 982.21 | 0.1333 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 469.685 |  | 469.794 | -0.0232 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.65 |  | 140.967 | -0.2249 | 140.765 | 137.165 | 4.8702 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 168.65 |  | 166.0537 | 1.5635 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.45 |  | 273.8935 | 1.6636 | 269.59 | 256.24 | 0.1544 | buy_precheck_manual_confirm | none |
| LITE | ai_networking_optical | 735.035 |  | 716.6589 | 2.5641 | 694.98 | 653.305 | 4.5835 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.98 |  | 377.8539 | 0.0334 | 375.52 | 359.81 | 3.8732 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 102.6 |  | 100.4748 | 2.1151 | 97.585 | 91.92 | 4.2593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 302.085 |  | 305.2768 | -1.0456 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1761.93 |  | 1756.5796 | 0.3046 | 1741.99 | 1704.935 | 0.0897 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 531.035 |  | 535.436 | -0.8219 | 535.095 | 513.34 | 0.6214 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 310.82 |  | 312.0984 | -0.4096 | 306.51 | 298.89 | 3.7385 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 212.05 |  | 212.171 | -0.057 | 210.82 | 204.71 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 322.51 |  | 319.6354 | 0.8993 | 308.03 | 297.18 | 0.2015 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 277.925 |  | 277.5711 | 0.1275 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.29 |  | 61.4558 | 1.3573 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.935 |  | 49.872 | 2.1315 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.045 |  | 134.6061 | 1.8119 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.13 |  | 318.6165 | 1.7305 | 315.89 | 307.13 | 4.3193 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.925 |  | 520.0397 | -0.9835 | 526.74 | 522.205 | 0.2253 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.905 |  | 299.2188 | -1.1075 | 304.36 | 299.62 | 4.0655 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.27 |  | 25.0811 | 0.7531 | 25.45 | 24.1 | 3.0471 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.915 |  | 33.7936 | 0.3591 | 34 | 32.26 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.6489 | 1.9427 | 20.445 | 19.92 | 0.0475 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1428.48 |  | 1428.3561 | 0.0087 | 1393.96 | 1325.48 | 0.3318 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 480.785 |  | 466.5898 | 3.0423 | 453.35 | 431.78 | 0.6094 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 786.71 |  | 759.7259 | 3.5518 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.56 |  | 248.0148 | -0.1834 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.52 |  | 642.1065 | 0.6873 | 649.07 | 638.97 | 0.8847 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.97 |  | 261.031 | 3.0414 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.71 |  | 158.6 | 0.6999 | 151.99 | 145.6 | 1.1834 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
