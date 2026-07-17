# Intraday State

- Generated at: `2026-07-18T02:11:25+08:00`
- Market time ET: `2026-07-17T14:11:26-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'watch_only': 4, 'below_vwap': 7, 'spread_too_wide_or_missing': 30, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.21 |  | 695.4325 | 0.3994 | 693.36 | 686.78 | 0.0587 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 524 |  | 517.9907 | 1.1601 | 511.83 | 498.665 | 0.0725 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.91 |  | 554.8568 | 0.7305 | 550 | 536.9 | 0.0823 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.27 |  | 744.9882 | -0.0964 | 742.66 | 740.8 | 0.0322 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.88 |  | 203.2368 | 0.3165 | 203.41 | 197.98 | 0.1521 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.91 |  | 554.8568 | 0.7305 | 550 | 536.9 | 0.0823 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524 |  | 517.9907 | 1.1601 | 511.83 | 498.665 | 0.0725 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1765.985 |  | 1756.3136 | 0.5507 | 1741.99 | 1704.935 | 0.1427 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 212.34 |  | 212.1663 | 0.0819 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 877.375 |  | 863.6396 | 1.5904 | 835.82 | 804.09 | 0.1721 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 294.24 |  | 294.2117 | 0.0096 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 698.21 |  | 695.4325 | 0.3994 | 693.36 | 686.78 | 0.0587 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.37 |  | 45.6294 | 1.6231 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.765 |  | 24.283 | 1.9849 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.13 |  | 20.6426 | 2.3611 | 20.445 | 19.92 | 0.0947 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 68.25 |  | 67.179 | 1.5942 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.24 |  | 294.2117 | 0.0096 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 203.88 |  | 203.2368 | 0.3165 | 203.41 | 197.98 | 0.1521 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.34 |  | 212.1663 | 0.0819 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 698.21 |  | 695.4325 | 0.3994 | 693.36 | 686.78 | 0.0587 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1765.985 |  | 1756.3136 | 0.5507 | 1741.99 | 1704.935 | 0.1427 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 332.49 |  | 331.9808 | 0.1534 | 334.98 | 331.295 | 0.006 | watch_only | none |
| 7 | SMH | semiconductor_index | 558.91 |  | 554.8568 | 0.7305 | 550 | 536.9 | 0.0823 | buy_precheck_manual_confirm | none |
| 8 | IREN | high_beta_ai_infrastructure | 33.91 |  | 33.7888 | 0.3586 | 34 | 32.26 | 0.0295 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 395.385 |  | 393.2645 | 0.5392 | 398.39 | 393.52 | 0.2504 | watch_only | none |
| 10 | JCI | data_center_power_cooling | 141.09 |  | 140.9659 | 0.0881 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 524 |  | 517.9907 | 1.1601 | 511.83 | 498.665 | 0.0725 | buy_precheck_manual_confirm | none |
| 12 | TT | data_center_power_cooling | 470.035 |  | 469.7763 | 0.0551 | 469.08 | 460.78 | 4.1444 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | APLD | high_beta_ai_infrastructure | 25.34 |  | 25.0789 | 1.0413 | 25.45 | 24.1 | 0.0789 | watch_only | none |
| 14 | TSM | foundry | 398.29 |  | 398.136 | 0.0387 | 394.11 | 386.02 | 0.8813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | HPE | ai_server_oem | 46.37 |  | 45.6294 | 1.6231 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 24.765 |  | 24.283 | 1.9849 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 17 | MU | memory_hbm_storage | 877.375 |  | 863.6396 | 1.5904 | 835.82 | 804.09 | 0.1721 | buy_precheck_manual_confirm | none |
| 18 | PWR | data_center_power_cooling | 634.625 |  | 629.6143 | 0.7958 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | CORZ | high_beta_ai_infrastructure | 21.13 |  | 20.6426 | 2.3611 | 20.445 | 19.92 | 0.0947 | buy_precheck_manual_confirm | none |
| 20 | META | cloud_ai_capex | 647.01 |  | 642.0007 | 0.7803 | 649.07 | 638.97 | 0.8222 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.88 |  | 203.2368 | 0.3165 | 203.41 | 197.98 | 0.1521 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.91 |  | 554.8568 | 0.7305 | 550 | 536.9 | 0.0823 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524 |  | 517.9907 | 1.1601 | 511.83 | 498.665 | 0.0725 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1765.985 |  | 1756.3136 | 0.5507 | 1741.99 | 1704.935 | 0.1427 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 212.34 |  | 212.1663 | 0.0819 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 877.375 |  | 863.6396 | 1.5904 | 835.82 | 804.09 | 0.1721 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 294.24 |  | 294.2117 | 0.0096 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 698.21 |  | 695.4325 | 0.3994 | 693.36 | 686.78 | 0.0587 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.37 |  | 45.6294 | 1.6231 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.765 |  | 24.283 | 1.9849 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.13 |  | 20.6426 | 2.3611 | 20.445 | 19.92 | 0.0947 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 68.25 |  | 67.179 | 1.5942 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| 13 | LRCX | semiconductor_equipment | 311.5 |  | 312.1038 | -0.1935 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | SPY | market_regime | 744.27 |  | 744.9882 | -0.0964 | 742.66 | 740.8 | 0.0322 | below_vwap | below_vwap |
| 15 | ANET | ai_networking_optical | 168.96 |  | 166.0256 | 1.7674 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TSM | foundry | 398.29 |  | 398.136 | 0.0387 | 394.11 | 386.02 | 0.8813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 373.5 |  | 370.1056 | 0.9172 | 368.42 | 357.97 | 2.1419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 497.83 |  | 486.5693 | 2.3143 | 482.43 | 461.04 | 3.4148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 470.035 |  | 469.7763 | 0.0551 | 469.08 | 460.78 | 4.1444 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | VRT | data_center_power_cooling | 292.835 |  | 286.9875 | 2.0375 | 280.565 | 273.17 | 4.8321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.21 |  | 695.4325 | 0.3994 | 693.36 | 686.78 | 0.0587 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.25 |  | 67.179 | 1.5942 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.88 |  | 203.2368 | 0.3165 | 203.41 | 197.98 | 0.1521 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 395.385 |  | 393.2645 | 0.5392 | 398.39 | 393.52 | 0.2504 | watch_only | none |
| AAPL | mega_cap_platform | 332.49 |  | 331.9808 | 0.1534 | 334.98 | 331.295 | 0.006 | watch_only | none |
| GOOGL | cloud_ai_capex | 343.7 |  | 345.9543 | -0.6516 | 348.47 | 341.42 | 0.2124 | below_vwap | below_vwap |
| AMD | ai_accelerator | 497.83 |  | 486.5693 | 2.3143 | 482.43 | 461.04 | 3.4148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.29 |  | 398.136 | 0.0387 | 394.11 | 386.02 | 0.8813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524 |  | 517.9907 | 1.1601 | 511.83 | 498.665 | 0.0725 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.91 |  | 554.8568 | 0.7305 | 550 | 536.9 | 0.0823 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.5 |  | 370.1056 | 0.9172 | 368.42 | 357.97 | 2.1419 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 877.375 |  | 863.6396 | 1.5904 | 835.82 | 804.09 | 0.1721 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 189.865 |  | 187.0659 | 1.4963 | 185.03 | 178.09 | 0.4793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.43 |  | 392.4939 | 2.5315 | 384 | 368.28 | 4.6095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.37 |  | 45.6294 | 1.6231 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.765 |  | 24.283 | 1.9849 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.27 |  | 744.9882 | -0.0964 | 742.66 | 740.8 | 0.0322 | below_vwap | below_vwap |
| IWM | market_regime | 294.24 |  | 294.2117 | 0.0096 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.51 |  | 125.9648 | 1.2267 | 125.02 | 121.79 | 3.0194 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.645 |  | 72.1593 | 2.059 | 71.24 | 68.65 | 1.032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.835 |  | 286.9875 | 2.0375 | 280.565 | 273.17 | 4.8321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 401.52 |  | 399.6985 | 0.4557 | 389.4 | 382.38 | 2.899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 634.625 |  | 629.6143 | 0.7958 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1060.62 |  | 1044.6019 | 1.5334 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 470.035 |  | 469.7763 | 0.0551 | 469.08 | 460.78 | 4.1444 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.09 |  | 140.9659 | 0.0881 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.96 |  | 166.0256 | 1.7674 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.79 |  | 273.8644 | 1.7985 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 737.65 |  | 715.9392 | 3.0325 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 379.83 |  | 377.8074 | 0.5353 | 375.52 | 359.81 | 4.2045 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 103.32 |  | 100.4381 | 2.8694 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304 |  | 305.2986 | -0.4254 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1765.985 |  | 1756.3136 | 0.5507 | 1741.99 | 1704.935 | 0.1427 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 533.3 |  | 535.4973 | -0.4103 | 535.095 | 513.34 | 3.4446 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 311.5 |  | 312.1038 | -0.1935 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.34 |  | 212.1663 | 0.0819 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 325.24 |  | 319.4016 | 1.8279 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.83 |  | 277.5413 | 0.8246 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.54 |  | 61.4343 | 1.7999 | 60.51 | 57.99 | 4.0454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 50.97 |  | 49.8667 | 2.2125 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.315 |  | 134.3465 | 2.954 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.15 |  | 318.5098 | 2.0848 | 315.89 | 307.13 | 4.5025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.86 |  | 520.0932 | -1.0062 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.26 |  | 299.2998 | -1.0156 | 304.36 | 299.62 | 4.037 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.34 |  | 25.0789 | 1.0413 | 25.45 | 24.1 | 0.0789 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.91 |  | 33.7888 | 0.3586 | 34 | 32.26 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.13 |  | 20.6426 | 2.3611 | 20.445 | 19.92 | 0.0947 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1431.98 |  | 1428.3099 | 0.257 | 1393.96 | 1325.48 | 3.454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 481.755 |  | 466.3361 | 3.3064 | 453.35 | 431.78 | 1.6087 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 786.76 |  | 759.3913 | 3.604 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.31 |  | 248.0256 | -0.2885 | 247.72 | 243.725 | 0.004 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.01 |  | 642.0007 | 0.7803 | 649.07 | 638.97 | 0.8222 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.495 |  | 261.0121 | 2.8669 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.61 |  | 158.5688 | 0.6566 | 151.99 | 145.6 | 1.5601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
