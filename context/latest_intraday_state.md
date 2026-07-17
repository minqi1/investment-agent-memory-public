# Intraday State

- Generated at: `2026-07-18T02:52:16+08:00`
- Market time ET: `2026-07-17T14:52:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_vwap': 16, 'watch_only': 3, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.38 |  | 695.587 | 0.2578 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.16 |  | 518.519 | 0.895 | 511.83 | 498.665 | 0.0898 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.9 |  | 555.1548 | 0.3144 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.98 |  | 744.8801 | -0.1208 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.9 |  | 555.1548 | 0.3144 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.16 |  | 518.519 | 0.895 | 511.83 | 498.665 | 0.0898 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1053.34 |  | 1045.2519 | 0.7738 | 1001.82 | 982.21 | 0.2022 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.38 |  | 695.587 | 0.2578 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.335 |  | 45.6797 | 1.4346 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | COHR | ai_networking_optical | 277.85 |  | 274.0624 | 1.382 | 269.59 | 256.24 | 0.2123 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.34 |  | 126.0326 | 0.2439 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.605 |  | 24.3146 | 1.1944 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6654 | 1.5222 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.1 |  | 67.2211 | 1.3075 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.38 |  | 695.587 | 0.2578 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.9 |  | 555.1548 | 0.3144 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| 3 | ORCL | cloud_ai_capex | 126.34 |  | 126.0326 | 0.2439 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.865 |  | 393.4184 | 0.3677 | 398.39 | 393.52 | 0.0861 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 334.115 |  | 332.1162 | 0.6018 | 334.98 | 331.295 | 0.0299 | watch_only | none |
| 6 | GEV | data_center_power_cooling | 1053.34 |  | 1045.2519 | 0.7738 | 1001.82 | 982.21 | 0.2022 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.19 |  | 25.0924 | 0.3892 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.605 |  | 24.3146 | 1.1944 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 9 | SOXX | semiconductor_index | 523.16 |  | 518.519 | 0.895 | 511.83 | 498.665 | 0.0898 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.335 |  | 45.6797 | 1.4346 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 212.68 |  | 212.2143 | 0.2195 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | COHR | ai_networking_optical | 277.85 |  | 274.0624 | 1.382 | 269.59 | 256.24 | 0.2123 | buy_precheck_manual_confirm | none |
| 13 | ETN | data_center_power_cooling | 400.27 |  | 399.7781 | 0.123 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 278.6 |  | 277.6816 | 0.3308 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 632.675 |  | 630.1363 | 0.4029 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6654 | 1.5222 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| 17 | AVGO | custom_silicon_networking | 372.86 |  | 370.2986 | 0.6917 | 368.42 | 357.97 | 1.9364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | JCI | data_center_power_cooling | 140.81 |  | 140.9564 | -0.1039 | 140.765 | 137.165 | 0.0923 | below_vwap | below_vwap |
| 19 | SPY | market_regime | 743.98 |  | 744.8801 | -0.1208 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 20 | NVDA | ai_accelerator | 203.145 |  | 203.2415 | -0.0475 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.9 |  | 555.1548 | 0.3144 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.16 |  | 518.519 | 0.895 | 511.83 | 498.665 | 0.0898 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1053.34 |  | 1045.2519 | 0.7738 | 1001.82 | 982.21 | 0.2022 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.38 |  | 695.587 | 0.2578 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.335 |  | 45.6797 | 1.4346 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | COHR | ai_networking_optical | 277.85 |  | 274.0624 | 1.382 | 269.59 | 256.24 | 0.2123 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.34 |  | 126.0326 | 0.2439 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.605 |  | 24.3146 | 1.1944 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6654 | 1.5222 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.1 |  | 67.2211 | 1.3075 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 396.675 |  | 398.0595 | -0.3478 | 394.11 | 386.02 | 0.4235 | below_vwap | below_vwap,spread_too_wide |
| 12 | ASML | semiconductor_equipment | 1756.9 |  | 1757.0839 | -0.0105 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | TT | data_center_power_cooling | 469.12 |  | 469.7801 | -0.1405 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 140.81 |  | 140.9564 | -0.1039 | 140.765 | 137.165 | 0.0923 | below_vwap | below_vwap |
| 15 | CIEN | ai_networking_optical | 377.025 |  | 377.8285 | -0.2127 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LRCX | semiconductor_equipment | 311.895 |  | 312.1231 | -0.0731 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | SPY | market_regime | 743.98 |  | 744.8801 | -0.1208 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 18 | SNDK | memory_hbm_storage | 1417.99 |  | 1428.0461 | -0.7042 | 1393.96 | 1325.48 | 4.4464 | below_vwap | below_vwap,spread_too_wide |
| 19 | ANET | ai_networking_optical | 168.71 |  | 166.1961 | 1.5126 | 163.275 | 157.34 | 4.7537 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 372.86 |  | 370.2986 | 0.6917 | 368.42 | 357.97 | 1.9364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.38 |  | 695.587 | 0.2578 | 693.36 | 686.78 | 0.0301 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.1 |  | 67.2211 | 1.3075 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.145 |  | 203.2415 | -0.0475 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.865 |  | 393.4184 | 0.3677 | 398.39 | 393.52 | 0.0861 | watch_only | none |
| AAPL | mega_cap_platform | 334.115 |  | 332.1162 | 0.6018 | 334.98 | 331.295 | 0.0299 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.02 |  | 345.8102 | -0.2285 | 348.47 | 341.42 | 0.1449 | below_vwap | below_vwap |
| AMD | ai_accelerator | 497.25 |  | 486.874 | 2.1311 | 482.43 | 461.04 | 0.4545 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.675 |  | 398.0595 | -0.3478 | 394.11 | 386.02 | 0.4235 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.16 |  | 518.519 | 0.895 | 511.83 | 498.665 | 0.0898 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.9 |  | 555.1548 | 0.3144 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.86 |  | 370.2986 | 0.6917 | 368.42 | 357.97 | 1.9364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 872.02 |  | 864.4806 | 0.8721 | 835.82 | 804.09 | 0.914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.36 |  | 187.189 | 1.1598 | 185.03 | 178.09 | 0.433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.17 |  | 393.1864 | 2.0305 | 384 | 368.28 | 4.8558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.335 |  | 45.6797 | 1.4346 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.605 |  | 24.3146 | 1.1944 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.98 |  | 744.8801 | -0.1208 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.79 |  | 294.1505 | -0.1226 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.34 |  | 126.0326 | 0.2439 | 125.02 | 121.79 | 0.0554 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.73 |  | 72.2312 | 2.075 | 71.24 | 68.65 | 2.699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 291.83 |  | 287.3805 | 1.5483 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.27 |  | 399.7781 | 0.123 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 632.675 |  | 630.1363 | 0.4029 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1053.34 |  | 1045.2519 | 0.7738 | 1001.82 | 982.21 | 0.2022 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 469.12 |  | 469.7801 | -0.1405 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.81 |  | 140.9564 | -0.1039 | 140.765 | 137.165 | 0.0923 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 168.71 |  | 166.1961 | 1.5126 | 163.275 | 157.34 | 4.7537 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.85 |  | 274.0624 | 1.382 | 269.59 | 256.24 | 0.2123 | buy_precheck_manual_confirm | none |
| LITE | ai_networking_optical | 734.86 |  | 718.1088 | 2.3327 | 694.98 | 653.305 | 4.4158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.025 |  | 377.8285 | -0.2127 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.38 |  | 100.5902 | 1.7793 | 97.585 | 91.92 | 4.1512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 302.425 |  | 305.1429 | -0.8907 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1756.9 |  | 1757.0839 | -0.0105 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 532.015 |  | 535.1367 | -0.5834 | 535.095 | 513.34 | 0.1673 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 311.895 |  | 312.1231 | -0.0731 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.68 |  | 212.2143 | 0.2195 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TER | semiconductor_test_packaging | 323.005 |  | 320.0811 | 0.9135 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.6 |  | 277.6816 | 0.3308 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.47 |  | 61.5185 | 1.5467 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.86 |  | 49.9145 | 1.8942 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.12 |  | 134.9571 | 1.6026 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.96 |  | 318.8509 | 1.916 | 315.89 | 307.13 | 4.5513 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.86 |  | 519.022 | -0.8019 | 526.74 | 522.205 | 0.2467 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.97 |  | 298.861 | -0.9673 | 304.36 | 299.62 | 0.2399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 25.19 |  | 25.0924 | 0.3892 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.715 |  | 33.786 | -0.2102 | 34 | 32.26 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6654 | 1.5222 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1417.99 |  | 1428.0461 | -0.7042 | 1393.96 | 1325.48 | 4.4464 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.78 |  | 467.3426 | 2.8753 | 453.35 | 431.78 | 2.6707 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 786.405 |  | 761.1465 | 3.3185 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.64 |  | 247.9977 | -0.1442 | 247.72 | 243.725 | 0.0121 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.88 |  | 642.4932 | 0.8384 | 649.07 | 638.97 | 0.4661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 267.71 |  | 261.2356 | 2.4784 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 160.765 |  | 158.9245 | 1.1581 | 151.99 | 145.6 | 3.7322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
