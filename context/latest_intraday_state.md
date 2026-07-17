# Intraday State

- Generated at: `2026-07-18T02:31:40+08:00`
- Market time ET: `2026-07-17T14:31:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'spread_too_wide_or_missing': 30, 'watch_only': 4, 'below_vwap': 9, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.97 |  | 695.5269 | 0.3513 | 693.36 | 686.78 | 0.0358 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 524.91 |  | 518.3048 | 1.2744 | 511.83 | 498.665 | 0.0895 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 559.08 |  | 554.9923 | 0.7365 | 550 | 536.9 | 0.0751 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.15 |  | 744.9233 | -0.1038 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 398.14 |  | 398.1019 | 0.0096 | 394.11 | 386.02 | 0.2637 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 559.08 |  | 554.9923 | 0.7365 | 550 | 536.9 | 0.0751 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.91 |  | 518.3048 | 1.2744 | 511.83 | 498.665 | 0.0895 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.51 |  | 212.1824 | 0.6257 | 210.82 | 204.71 | 0.1124 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.97 |  | 695.5269 | 0.3513 | 693.36 | 686.78 | 0.0358 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.445 |  | 45.652 | 1.7371 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 484 |  | 466.7996 | 3.6847 | 453.35 | 431.78 | 0.2583 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.8 |  | 24.2958 | 2.0752 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.17 |  | 20.6577 | 2.48 | 20.445 | 19.92 | 0.1417 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.31 |  | 67.2003 | 1.6513 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 398.14 |  | 398.1019 | 0.0096 | 394.11 | 386.02 | 0.2637 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 697.97 |  | 695.5269 | 0.3513 | 693.36 | 686.78 | 0.0358 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.51 |  | 212.1824 | 0.6257 | 210.82 | 204.71 | 0.1124 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 559.08 |  | 554.9923 | 0.7365 | 550 | 536.9 | 0.0751 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.24 |  | 332.0018 | 0.0718 | 334.98 | 331.295 | 0.2107 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.935 |  | 33.7943 | 0.4163 | 34 | 32.26 | 0.0589 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 394.83 |  | 393.3631 | 0.3729 | 398.39 | 393.52 | 0.2001 | watch_only | none |
| 8 | SOXX | semiconductor_index | 524.91 |  | 518.3048 | 1.2744 | 511.83 | 498.665 | 0.0895 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 203.72 |  | 203.2413 | 0.2355 | 203.41 | 197.98 | 1.6346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | APLD | high_beta_ai_infrastructure | 25.32 |  | 25.0877 | 0.9259 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| 11 | CIEN | ai_networking_optical | 378.41 |  | 377.8513 | 0.1479 | 375.52 | 359.81 | 1.8234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | HPE | ai_server_oem | 46.445 |  | 45.652 | 1.7371 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 13 | ASML | semiconductor_equipment | 1769.26 |  | 1756.8555 | 0.7061 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMCI | ai_server_oem | 24.8 |  | 24.2958 | 2.0752 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| 15 | PWR | data_center_power_cooling | 634.24 |  | 629.906 | 0.688 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 21.17 |  | 20.6577 | 2.48 | 20.445 | 19.92 | 0.1417 | buy_precheck_manual_confirm | none |
| 17 | LRCX | semiconductor_equipment | 313.495 |  | 312.0903 | 0.4501 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | META | cloud_ai_capex | 647.185 |  | 642.274 | 0.7646 | 649.07 | 638.97 | 1.1836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ONTO | semiconductor_test_packaging | 279.29 |  | 277.5967 | 0.61 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 484 |  | 466.7996 | 3.6847 | 453.35 | 431.78 | 0.2583 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 398.14 |  | 398.1019 | 0.0096 | 394.11 | 386.02 | 0.2637 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 559.08 |  | 554.9923 | 0.7365 | 550 | 536.9 | 0.0751 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.91 |  | 518.3048 | 1.2744 | 511.83 | 498.665 | 0.0895 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.51 |  | 212.1824 | 0.6257 | 210.82 | 204.71 | 0.1124 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.97 |  | 695.5269 | 0.3513 | 693.36 | 686.78 | 0.0358 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.445 |  | 45.652 | 1.7371 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 484 |  | 466.7996 | 3.6847 | 453.35 | 431.78 | 0.2583 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.8 |  | 24.2958 | 2.0752 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.17 |  | 20.6577 | 2.48 | 20.445 | 19.92 | 0.1417 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.31 |  | 67.2003 | 1.6513 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| 11 | TT | data_center_power_cooling | 469.75 |  | 469.7835 | -0.0071 | 469.08 | 460.78 | 4.1086 | below_vwap | below_vwap,spread_too_wide |
| 12 | SPY | market_regime | 744.15 |  | 744.9233 | -0.1038 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 13 | AMZN | cloud_ai_capex | 247.8 |  | 248.0092 | -0.0843 | 247.72 | 243.725 | 0.0161 | below_vwap | below_vwap |
| 14 | ANET | ai_networking_optical | 169.59 |  | 166.1256 | 2.0854 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | NVDA | ai_accelerator | 203.72 |  | 203.2413 | 0.2355 | 203.41 | 197.98 | 1.6346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 373.62 |  | 370.1982 | 0.9243 | 368.42 | 357.97 | 1.7023 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 498.33 |  | 486.7253 | 2.3842 | 482.43 | 461.04 | 3.5438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ASML | semiconductor_equipment | 1769.26 |  | 1756.8555 | 0.7061 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | MU | memory_hbm_storage | 878.03 |  | 864.0747 | 1.6151 | 835.82 | 804.09 | 0.8007 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | VRT | data_center_power_cooling | 293.17 |  | 287.1858 | 2.0837 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.97 |  | 695.5269 | 0.3513 | 693.36 | 686.78 | 0.0358 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.31 |  | 67.2003 | 1.6513 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.72 |  | 203.2413 | 0.2355 | 203.41 | 197.98 | 1.6346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 394.83 |  | 393.3631 | 0.3729 | 398.39 | 393.52 | 0.2001 | watch_only | none |
| AAPL | mega_cap_platform | 332.24 |  | 332.0018 | 0.0718 | 334.98 | 331.295 | 0.2107 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.48 |  | 345.871 | -0.4022 | 348.47 | 341.42 | 0.0145 | below_vwap | below_vwap |
| AMD | ai_accelerator | 498.33 |  | 486.7253 | 2.3842 | 482.43 | 461.04 | 3.5438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.14 |  | 398.1019 | 0.0096 | 394.11 | 386.02 | 0.2637 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524.91 |  | 518.3048 | 1.2744 | 511.83 | 498.665 | 0.0895 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 559.08 |  | 554.9923 | 0.7365 | 550 | 536.9 | 0.0751 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.62 |  | 370.1982 | 0.9243 | 368.42 | 357.97 | 1.7023 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 878.03 |  | 864.0747 | 1.6151 | 835.82 | 804.09 | 0.8007 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 190.01 |  | 187.1238 | 1.5424 | 185.03 | 178.09 | 0.6736 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.55 |  | 392.814 | 2.4785 | 384 | 368.28 | 4.4218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.445 |  | 45.652 | 1.7371 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.8 |  | 24.2958 | 2.0752 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.15 |  | 744.9233 | -0.1038 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.94 |  | 294.1855 | -0.0834 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.98 |  | 126.0067 | 0.7724 | 125.02 | 121.79 | 0.9765 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 74.085 |  | 72.2009 | 2.6095 | 71.24 | 68.65 | 2.2137 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 293.17 |  | 287.1858 | 2.0837 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.57 |  | 399.7504 | 0.4552 | 389.4 | 382.38 | 2.8862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 634.24 |  | 629.906 | 0.688 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1059.5 |  | 1044.9567 | 1.3918 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.75 |  | 469.7835 | -0.0071 | 469.08 | 460.78 | 4.1086 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.7 |  | 140.9604 | -0.1847 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.59 |  | 166.1256 | 2.0854 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 279.27 |  | 273.9664 | 1.9359 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 738.06 |  | 717.3692 | 2.8843 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 378.41 |  | 377.8513 | 0.1479 | 375.52 | 359.81 | 1.8234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 103.42 |  | 100.5132 | 2.892 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 303.89 |  | 305.2264 | -0.4379 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1769.26 |  | 1756.8555 | 0.7061 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 534.96 |  | 535.2934 | -0.0623 | 535.095 | 513.34 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 313.495 |  | 312.0903 | 0.4501 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.51 |  | 212.1824 | 0.6257 | 210.82 | 204.71 | 0.1124 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 325.69 |  | 319.8575 | 1.8235 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.29 |  | 277.5967 | 0.61 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.66 |  | 61.4889 | 1.9046 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.02 |  | 49.8916 | 2.2617 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.94 |  | 134.7517 | 2.3661 | 129.93 | 126.945 | 4.4875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.845 |  | 318.7436 | 2.2279 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 514.63 |  | 519.9309 | -1.0195 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.02 |  | 299.0757 | -1.0217 | 304.36 | 299.62 | 4.0369 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.32 |  | 25.0877 | 0.9259 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.935 |  | 33.7943 | 0.4163 | 34 | 32.26 | 0.0589 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.17 |  | 20.6577 | 2.48 | 20.445 | 19.92 | 0.1417 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1433.31 |  | 1428.2807 | 0.3521 | 1393.96 | 1325.48 | 4.5266 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 484 |  | 466.7996 | 3.6847 | 453.35 | 431.78 | 0.2583 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 794.995 |  | 760.3159 | 4.5611 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.8 |  | 248.0092 | -0.0843 | 247.72 | 243.725 | 0.0161 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.185 |  | 642.274 | 0.7646 | 649.07 | 638.97 | 1.1836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 269.35 |  | 261.1193 | 3.1521 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 162.075 |  | 158.7087 | 2.1211 | 151.99 | 145.6 | 1.851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
