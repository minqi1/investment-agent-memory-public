# Intraday State

- Generated at: `2026-07-18T02:07:23+08:00`
- Market time ET: `2026-07-17T14:07:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'watch_only': 4, 'below_vwap': 7, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.26 |  | 695.4206 | 0.4083 | 693.36 | 686.78 | 0.0415 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 525.56 |  | 517.9526 | 1.4687 | 511.83 | 498.665 | 0.0894 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 559.35 |  | 554.8375 | 0.8133 | 550 | 536.9 | 0.0733 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.29 |  | 744.9936 | -0.0944 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.045 |  | 203.2323 | 0.3999 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 559.35 |  | 554.8375 | 0.8133 | 550 | 536.9 | 0.0733 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 525.56 |  | 517.9526 | 1.4687 | 511.83 | 498.665 | 0.0894 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1766.76 |  | 1756.1805 | 0.6024 | 1741.99 | 1704.935 | 0.0515 | buy_precheck_manual_confirm | none |
| 5 | GEV | data_center_power_cooling | 1062 |  | 1044.5058 | 1.6749 | 1001.82 | 982.21 | 0.1036 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 698.26 |  | 695.4206 | 0.4083 | 693.36 | 686.78 | 0.0415 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.39 |  | 45.6195 | 1.6889 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.78 |  | 24.2812 | 2.0544 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.68 |  | 72.1532 | 2.1161 | 71.24 | 68.65 | 0.1086 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.16 |  | 20.6402 | 2.5184 | 20.445 | 19.92 | 0.0473 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 68.31 |  | 67.1762 | 1.6879 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.045 |  | 203.2323 | 0.3999 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 698.26 |  | 695.4206 | 0.4083 | 693.36 | 686.78 | 0.0415 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1766.76 |  | 1756.1805 | 0.6024 | 1741.99 | 1704.935 | 0.0515 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 332.18 |  | 331.9797 | 0.0603 | 334.98 | 331.295 | 0.009 | watch_only | none |
| 5 | IREN | high_beta_ai_infrastructure | 33.865 |  | 33.7868 | 0.2315 | 34 | 32.26 | 0.0295 | watch_only | none |
| 6 | MSFT | cloud_ai_capex | 394.98 |  | 393.2508 | 0.4397 | 398.39 | 393.52 | 0.0684 | watch_only | none |
| 7 | SMH | semiconductor_index | 559.35 |  | 554.8375 | 0.8133 | 550 | 536.9 | 0.0733 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 525.56 |  | 517.9526 | 1.4687 | 511.83 | 498.665 | 0.0894 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 469.88 |  | 469.7757 | 0.0222 | 469.08 | 460.78 | 4.1628 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | APLD | high_beta_ai_infrastructure | 25.41 |  | 25.0768 | 1.3288 | 25.45 | 24.1 | 0.0787 | watch_only | none |
| 11 | LRCX | semiconductor_equipment | 312.81 |  | 312.1029 | 0.2265 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ALAB | ai_networking_optical | 307.63 |  | 305.3072 | 0.7608 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 398.49 |  | 398.1335 | 0.0895 | 394.11 | 386.02 | 2.3965 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | CIEN | ai_networking_optical | 380.14 |  | 377.7347 | 0.6368 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | GEV | data_center_power_cooling | 1062 |  | 1044.5058 | 1.6749 | 1001.82 | 982.21 | 0.1036 | buy_precheck_manual_confirm | none |
| 16 | HPE | ai_server_oem | 46.39 |  | 45.6195 | 1.6889 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 24.78 |  | 24.2812 | 2.0544 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 18 | CRWV | gpu_cloud_ai_factory | 73.68 |  | 72.1532 | 2.1161 | 71.24 | 68.65 | 0.1086 | buy_precheck_manual_confirm | none |
| 19 | PWR | data_center_power_cooling | 634.345 |  | 629.5885 | 0.7555 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 21.16 |  | 20.6402 | 2.5184 | 20.445 | 19.92 | 0.0473 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.045 |  | 203.2323 | 0.3999 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 559.35 |  | 554.8375 | 0.8133 | 550 | 536.9 | 0.0733 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 525.56 |  | 517.9526 | 1.4687 | 511.83 | 498.665 | 0.0894 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1766.76 |  | 1756.1805 | 0.6024 | 1741.99 | 1704.935 | 0.0515 | buy_precheck_manual_confirm | none |
| 5 | GEV | data_center_power_cooling | 1062 |  | 1044.5058 | 1.6749 | 1001.82 | 982.21 | 0.1036 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 698.26 |  | 695.4206 | 0.4083 | 693.36 | 686.78 | 0.0415 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.39 |  | 45.6195 | 1.6889 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.78 |  | 24.2812 | 2.0544 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.68 |  | 72.1532 | 2.1161 | 71.24 | 68.65 | 0.1086 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.16 |  | 20.6402 | 2.5184 | 20.445 | 19.92 | 0.0473 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 68.31 |  | 67.1762 | 1.6879 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| 12 | AMAT | semiconductor_equipment | 535.46 |  | 535.501 | -0.0077 | 535.095 | 513.34 | 3.793 | below_vwap | below_vwap,spread_too_wide |
| 13 | JCI | data_center_power_cooling | 140.88 |  | 140.9652 | -0.0605 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | SPY | market_regime | 744.29 |  | 744.9936 | -0.0944 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 15 | ANET | ai_networking_optical | 169.28 |  | 165.9934 | 1.9799 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TSM | foundry | 398.49 |  | 398.1335 | 0.0895 | 394.11 | 386.02 | 2.3965 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 373.52 |  | 370.0773 | 0.9303 | 368.42 | 357.97 | 1.7697 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 499.26 |  | 486.5049 | 2.6218 | 482.43 | 461.04 | 3.7175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 469.88 |  | 469.7757 | 0.0222 | 469.08 | 460.78 | 4.1628 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | KLAC | semiconductor_equipment | 213.19 |  | 212.1587 | 0.4861 | 210.82 | 204.71 | 0.4034 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.26 |  | 695.4206 | 0.4083 | 693.36 | 686.78 | 0.0415 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.31 |  | 67.1762 | 1.6879 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.045 |  | 203.2323 | 0.3999 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.98 |  | 393.2508 | 0.4397 | 398.39 | 393.52 | 0.0684 | watch_only | none |
| AAPL | mega_cap_platform | 332.18 |  | 331.9797 | 0.0603 | 334.98 | 331.295 | 0.009 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.25 |  | 345.9782 | -0.4995 | 348.47 | 341.42 | 0.1888 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.26 |  | 486.5049 | 2.6218 | 482.43 | 461.04 | 3.7175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.49 |  | 398.1335 | 0.0895 | 394.11 | 386.02 | 2.3965 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.56 |  | 517.9526 | 1.4687 | 511.83 | 498.665 | 0.0894 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 559.35 |  | 554.8375 | 0.8133 | 550 | 536.9 | 0.0733 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.52 |  | 370.0773 | 0.9303 | 368.42 | 357.97 | 1.7697 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 880.92 |  | 863.5417 | 2.0124 | 835.82 | 804.09 | 0.462 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 190.55 |  | 187.0335 | 1.8801 | 185.03 | 178.09 | 0.7452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.59 |  | 392.4044 | 2.5957 | 384 | 368.28 | 4.4015 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.39 |  | 45.6195 | 1.6889 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.78 |  | 24.2812 | 2.0544 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.29 |  | 744.9936 | -0.0944 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.08 |  | 294.2124 | -0.045 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 127.39 |  | 125.9496 | 1.1436 | 125.02 | 121.79 | 2.9359 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.68 |  | 72.1532 | 2.1161 | 71.24 | 68.65 | 0.1086 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 293.07 |  | 286.9506 | 2.1326 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.585 |  | 399.68 | 0.4766 | 389.4 | 382.38 | 3.8921 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 634.345 |  | 629.5885 | 0.7555 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1062 |  | 1044.5058 | 1.6749 | 1001.82 | 982.21 | 0.1036 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 469.88 |  | 469.7757 | 0.0222 | 469.08 | 460.78 | 4.1628 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.88 |  | 140.9652 | -0.0605 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.28 |  | 165.9934 | 1.9799 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.63 |  | 273.8154 | 1.7583 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 737.43 |  | 715.619 | 3.0479 | 694.98 | 653.305 | 1.7886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 380.14 |  | 377.7347 | 0.6368 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.5 |  | 100.4293 | 3.0576 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 307.63 |  | 305.3072 | 0.7608 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1766.76 |  | 1756.1805 | 0.6024 | 1741.99 | 1704.935 | 0.0515 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 535.46 |  | 535.501 | -0.0077 | 535.095 | 513.34 | 3.793 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 312.81 |  | 312.1029 | 0.2265 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.19 |  | 212.1587 | 0.4861 | 210.82 | 204.71 | 0.4034 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 325.02 |  | 319.2172 | 1.8178 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.95 |  | 277.5061 | 0.8807 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.64 |  | 61.4256 | 1.977 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.03 |  | 49.8624 | 2.3417 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.97 |  | 134.3348 | 2.7061 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.49 |  | 318.4317 | 2.2166 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 514.14 |  | 520.1431 | -1.1541 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.08 |  | 299.3239 | -1.0837 | 304.36 | 299.62 | 4.769 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.41 |  | 25.0768 | 1.3288 | 25.45 | 24.1 | 0.0787 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.865 |  | 33.7868 | 0.2315 | 34 | 32.26 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.16 |  | 20.6402 | 2.5184 | 20.445 | 19.92 | 0.0473 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1435.945 |  | 1428.2477 | 0.5389 | 1393.96 | 1325.48 | 2.5739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 482.94 |  | 466.2111 | 3.5883 | 453.35 | 431.78 | 1.2465 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 783.92 |  | 759.2031 | 3.2556 | 724.57 | 702.24 | 4.4137 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.45 |  | 248.0311 | -0.2343 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.61 |  | 641.9351 | 0.884 | 649.07 | 638.97 | 0.6933 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 270.03 |  | 261.0085 | 3.4564 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.41 |  | 158.5493 | 0.5428 | 151.99 | 145.6 | 0.941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
