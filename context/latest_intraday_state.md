# Intraday State

- Generated at: `2026-07-18T03:32:37+08:00`
- Market time ET: `2026-07-17T15:32:38-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'watch_only': 4, 'below_vwap': 13, 'spread_too_wide_or_missing': 27, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.49 |  | 695.639 | 0.1223 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 524.19 |  | 518.8379 | 1.0316 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.89 |  | 555.1873 | 0.4868 | 550 | 536.9 | 0.086 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.2 |  | 744.6725 | -0.1977 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.89 |  | 555.1873 | 0.4868 | 550 | 536.9 | 0.086 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 497.48 |  | 487.24 | 2.1016 | 482.43 | 461.04 | 0.1467 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.19 |  | 518.8379 | 1.0316 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.7 |  | 212.2048 | 0.7046 | 210.82 | 204.71 | 0.0749 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.49 |  | 695.639 | 0.1223 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.03 |  | 45.7118 | 0.6961 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.52 |  | 24.3244 | 0.8041 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6836 | 0.7564 | 20.445 | 19.92 | 0.096 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.88 |  | 67.2604 | 0.9213 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.49 |  | 695.639 | 0.1223 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 203.19 |  | 203.1763 | 0.0068 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| 3 | SMH | semiconductor_index | 557.89 |  | 555.1873 | 0.4868 | 550 | 536.9 | 0.086 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.7 |  | 212.2048 | 0.7046 | 210.82 | 204.71 | 0.0749 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.73 |  | 332.332 | 0.1198 | 334.98 | 331.295 | 0.015 | watch_only | none |
| 6 | HPE | ai_server_oem | 46.03 |  | 45.7118 | 0.6961 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 395.23 |  | 393.6441 | 0.4029 | 398.39 | 393.52 | 0.0405 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6836 | 0.7564 | 20.445 | 19.92 | 0.096 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.52 |  | 24.3244 | 0.8041 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 524.19 |  | 518.8379 | 1.0316 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.425 |  | 25.1086 | 1.26 | 25.45 | 24.1 | 0.0787 | watch_only | none |
| 12 | PWR | data_center_power_cooling | 630.85 |  | 630.2976 | 0.0876 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 312.52 |  | 312.0581 | 0.148 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | META | cloud_ai_capex | 644.035 |  | 642.5996 | 0.2234 | 649.07 | 638.97 | 1.1071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 397.88 |  | 397.835 | 0.0113 | 394.11 | 386.02 | 0.5177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ONTO | semiconductor_test_packaging | 278.61 |  | 277.6548 | 0.344 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ASML | semiconductor_equipment | 1759.08 |  | 1756.8226 | 0.1285 | 1741.99 | 1704.935 | 2.8396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 497.48 |  | 487.24 | 2.1016 | 482.43 | 461.04 | 0.1467 | buy_precheck_manual_confirm | none |
| 19 | ORCL | cloud_ai_capex | 126.41 |  | 126.0408 | 0.2929 | 125.02 | 121.79 | 1.7245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ETN | data_center_power_cooling | 400.53 |  | 399.7398 | 0.1977 | 389.4 | 382.38 | 2.7389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.89 |  | 555.1873 | 0.4868 | 550 | 536.9 | 0.086 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 497.48 |  | 487.24 | 2.1016 | 482.43 | 461.04 | 0.1467 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.19 |  | 518.8379 | 1.0316 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.7 |  | 212.2048 | 0.7046 | 210.82 | 204.71 | 0.0749 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.49 |  | 695.639 | 0.1223 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.03 |  | 45.7118 | 0.6961 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.52 |  | 24.3244 | 0.8041 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6836 | 0.7564 | 20.445 | 19.92 | 0.096 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.88 |  | 67.2604 | 0.9213 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 10 | TT | data_center_power_cooling | 469.38 |  | 469.718 | -0.072 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | SPY | market_regime | 743.2 |  | 744.6725 | -0.1977 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 12 | SNDK | memory_hbm_storage | 1408.32 |  | 1426.6616 | -1.2856 | 1393.96 | 1325.48 | 4.3527 | below_vwap | below_vwap,spread_too_wide |
| 13 | SKHY | memory_hbm_storage | 154 |  | 158.7356 | -2.9833 | 151.99 | 145.6 | 1.4935 | below_vwap | below_vwap,spread_too_wide |
| 14 | ANET | ai_networking_optical | 168.34 |  | 166.3785 | 1.1789 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 397.88 |  | 397.835 | 0.0113 | 394.11 | 386.02 | 0.5177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 372.63 |  | 370.4307 | 0.5937 | 368.42 | 357.97 | 2.061 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1759.08 |  | 1756.8226 | 0.1285 | 1741.99 | 1704.935 | 2.8396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MU | memory_hbm_storage | 868.05 |  | 864.5855 | 0.4007 | 835.82 | 804.09 | 2.2038 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 291.06 |  | 287.7203 | 1.1607 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 400.53 |  | 399.7398 | 0.1977 | 389.4 | 382.38 | 2.7389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.49 |  | 695.639 | 0.1223 | 693.36 | 686.78 | 0.033 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.88 |  | 67.2604 | 0.9213 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.19 |  | 203.1763 | 0.0068 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| MSFT | cloud_ai_capex | 395.23 |  | 393.6441 | 0.4029 | 398.39 | 393.52 | 0.0405 | watch_only | none |
| AAPL | mega_cap_platform | 332.73 |  | 332.332 | 0.1198 | 334.98 | 331.295 | 0.015 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.18 |  | 345.7513 | -0.1652 | 348.47 | 341.42 | 0.1304 | below_vwap | below_vwap |
| AMD | ai_accelerator | 497.48 |  | 487.24 | 2.1016 | 482.43 | 461.04 | 0.1467 | buy_precheck_manual_confirm | none |
| TSM | foundry | 397.88 |  | 397.835 | 0.0113 | 394.11 | 386.02 | 0.5177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524.19 |  | 518.8379 | 1.0316 | 511.83 | 498.665 | 0.0935 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.89 |  | 555.1873 | 0.4868 | 550 | 536.9 | 0.086 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.63 |  | 370.4307 | 0.5937 | 368.42 | 357.97 | 2.061 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 868.05 |  | 864.5855 | 0.4007 | 835.82 | 804.09 | 2.2038 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.56 |  | 187.2846 | 1.215 | 185.03 | 178.09 | 0.997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 398.42 |  | 393.6731 | 1.2058 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.03 |  | 45.7118 | 0.6961 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.52 |  | 24.3244 | 0.8041 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.2 |  | 744.6725 | -0.1977 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.54 |  | 294.0883 | -0.1864 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.41 |  | 126.0408 | 0.2929 | 125.02 | 121.79 | 1.7245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.255 |  | 72.2945 | 1.3286 | 71.24 | 68.65 | 4.5048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 291.06 |  | 287.7203 | 1.1607 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.53 |  | 399.7398 | 0.1977 | 389.4 | 382.38 | 2.7389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 630.85 |  | 630.2976 | 0.0876 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1054.04 |  | 1046.2898 | 0.7407 | 1001.82 | 982.21 | 4.6924 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.38 |  | 469.718 | -0.072 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.695 |  | 140.9162 | -0.157 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.34 |  | 166.3785 | 1.1789 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 277.85 |  | 274.369 | 1.2687 | 269.59 | 256.24 | 1.5548 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 736.58 |  | 719.6088 | 2.3584 | 694.98 | 653.305 | 4.4055 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.4 |  | 377.6334 | -0.5914 | 375.52 | 359.81 | 4.4646 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 103.085 |  | 100.7238 | 2.3443 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.5 |  | 304.6405 | -0.0461 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1759.08 |  | 1756.8226 | 0.1285 | 1741.99 | 1704.935 | 2.8396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.18 |  | 533.883 | -0.5063 | 535.095 | 513.34 | 1.1578 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 312.52 |  | 312.0581 | 0.148 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.7 |  | 212.2048 | 0.7046 | 210.82 | 204.71 | 0.0749 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.28 |  | 320.4058 | 1.2092 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.61 |  | 277.6548 | 0.344 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.53 |  | 61.6395 | 1.4447 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.94 |  | 50.0091 | 1.8614 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.02 |  | 135.2098 | 1.3388 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.12 |  | 319.291 | 1.8256 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.38 |  | 518.3365 | -1.1492 | 526.74 | 522.205 | 0.2459 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.29 |  | 298.5313 | -1.0857 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.425 |  | 25.1086 | 1.26 | 25.45 | 24.1 | 0.0787 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.55 |  | 33.746 | -0.5808 | 34 | 32.26 | 0.0596 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6836 | 0.7564 | 20.445 | 19.92 | 0.096 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1408.32 |  | 1426.6616 | -1.2856 | 1393.96 | 1325.48 | 4.3527 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.745 |  | 468.012 | 2.7207 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 794.52 |  | 766.1341 | 3.7051 | 724.57 | 702.24 | 1.2876 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.12 |  | 247.9552 | -0.3369 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 644.035 |  | 642.5996 | 0.2234 | 649.07 | 638.97 | 1.1071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.06 |  | 261.6707 | 2.4417 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 154 |  | 158.7356 | -2.9833 | 151.99 | 145.6 | 1.4935 | below_vwap | below_vwap,spread_too_wide |
