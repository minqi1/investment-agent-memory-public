# Intraday State

- Generated at: `2026-07-18T00:06:42+08:00`
- Market time ET: `2026-07-17T12:06:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 15, 'below_opening_15m_low': 5, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_vwap': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.92 |  | 693.7071 | 0.6073 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 525.715 |  | 514.1983 | 2.2397 | 511.83 | 498.665 | 0.0742 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 560.59 |  | 551.0581 | 1.7298 | 550 | 536.9 | 0.0874 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.3 |  | 744.6082 | 0.0929 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.365 |  | 202.4669 | 0.9375 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 560.59 |  | 551.0581 | 1.7298 | 550 | 536.9 | 0.0874 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 525.715 |  | 514.1983 | 2.2397 | 511.83 | 498.665 | 0.0742 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1773.14 |  | 1742.8932 | 1.7354 | 1741.99 | 1704.935 | 0.2673 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 214.88 |  | 210.7358 | 1.9665 | 210.82 | 204.71 | 0.0512 | buy_precheck_manual_confirm | none |
| 6 | DELL | ai_server_oem | 396.38 |  | 387.7683 | 2.2208 | 384 | 368.28 | 0.3078 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 697.92 |  | 693.7071 | 0.6073 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.89 |  | 45.3435 | 1.2052 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.3 |  | 744.6082 | 0.0929 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 772.62 |  | 739.9295 | 4.4181 | 724.57 | 702.24 | 0.1696 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 478.06 |  | 453.7645 | 5.3542 | 453.35 | 431.78 | 0.2406 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.35 |  | 24.046 | 1.2644 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.85 |  | 20.484 | 1.7868 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 34.13 |  | 33.456 | 2.0146 | 34 | 32.26 | 0.0586 | buy_precheck_manual_confirm | none |
| 15 | TQQQ | leveraged_tool | 68.26 |  | 66.8216 | 2.1527 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.3 |  | 744.6082 | 0.0929 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 697.92 |  | 693.7071 | 0.6073 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 294.13 |  | 294.0097 | 0.0409 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| 4 | NVDA | ai_accelerator | 204.365 |  | 202.4669 | 0.9375 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 24.35 |  | 24.046 | 1.2644 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.89 |  | 45.3435 | 1.2052 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| 7 | IREN | high_beta_ai_infrastructure | 34.13 |  | 33.456 | 2.0146 | 34 | 32.26 | 0.0586 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 346.5 |  | 346.0461 | 0.1312 | 348.47 | 341.42 | 1.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 560.59 |  | 551.0581 | 1.7298 | 550 | 536.9 | 0.0874 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 525.715 |  | 514.1983 | 2.2397 | 511.83 | 498.665 | 0.0742 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 214.88 |  | 210.7358 | 1.9665 | 210.82 | 204.71 | 0.0512 | buy_precheck_manual_confirm | none |
| 12 | ASML | semiconductor_equipment | 1773.14 |  | 1742.8932 | 1.7354 | 1741.99 | 1704.935 | 0.2673 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.85 |  | 20.484 | 1.7868 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| 14 | APLD | high_beta_ai_infrastructure | 25.39 |  | 24.8426 | 2.2035 | 25.45 | 24.1 | 0.0788 | watch_only | none |
| 15 | DELL | ai_server_oem | 396.38 |  | 387.7683 | 2.2208 | 384 | 368.28 | 0.3078 | buy_precheck_manual_confirm | none |
| 16 | STX | memory_hbm_storage | 772.62 |  | 739.9295 | 4.4181 | 724.57 | 702.24 | 0.1696 | buy_precheck_manual_confirm | none |
| 17 | WDC | memory_hbm_storage | 478.06 |  | 453.7645 | 5.3542 | 453.35 | 431.78 | 0.2406 | buy_precheck_manual_confirm | none |
| 18 | TT | data_center_power_cooling | 473.33 |  | 469.2321 | 0.8733 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 142.23 |  | 140.652 | 1.1219 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMZN | cloud_ai_capex | 247.67 |  | 247.8822 | -0.0856 | 247.72 | 243.725 | 0.0202 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.365 |  | 202.4669 | 0.9375 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 560.59 |  | 551.0581 | 1.7298 | 550 | 536.9 | 0.0874 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 525.715 |  | 514.1983 | 2.2397 | 511.83 | 498.665 | 0.0742 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1773.14 |  | 1742.8932 | 1.7354 | 1741.99 | 1704.935 | 0.2673 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 214.88 |  | 210.7358 | 1.9665 | 210.82 | 204.71 | 0.0512 | buy_precheck_manual_confirm | none |
| 6 | DELL | ai_server_oem | 396.38 |  | 387.7683 | 2.2208 | 384 | 368.28 | 0.3078 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 697.92 |  | 693.7071 | 0.6073 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.89 |  | 45.3435 | 1.2052 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.3 |  | 744.6082 | 0.0929 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 772.62 |  | 739.9295 | 4.4181 | 724.57 | 702.24 | 0.1696 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 478.06 |  | 453.7645 | 5.3542 | 453.35 | 431.78 | 0.2406 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.35 |  | 24.046 | 1.2644 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.85 |  | 20.484 | 1.7868 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 34.13 |  | 33.456 | 2.0146 | 34 | 32.26 | 0.0586 | buy_precheck_manual_confirm | none |
| 15 | TQQQ | leveraged_tool | 68.26 |  | 66.8216 | 2.1527 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| 16 | ANET | ai_networking_optical | 167.355 |  | 163.4886 | 2.3649 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | TSM | foundry | 402.39 |  | 395.8968 | 1.6401 | 394.11 | 386.02 | 1.4091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AVGO | custom_silicon_networking | 371.595 |  | 368.1864 | 0.9258 | 368.42 | 357.97 | 1.7492 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 544.535 |  | 529.9422 | 2.7537 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 499.11 |  | 482.4339 | 3.4567 | 482.43 | 461.04 | 0.571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.92 |  | 693.7071 | 0.6073 | 693.36 | 686.78 | 0.0086 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.26 |  | 66.8216 | 2.1527 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.365 |  | 202.4669 | 0.9375 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 391.565 |  | 393.0077 | -0.3671 | 398.39 | 393.52 | 0.069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.865 |  | 332.4883 | -0.4882 | 334.98 | 331.295 | 0.0393 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.5 |  | 346.0461 | 0.1312 | 348.47 | 341.42 | 1.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 499.11 |  | 482.4339 | 3.4567 | 482.43 | 461.04 | 0.571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 402.39 |  | 395.8968 | 1.6401 | 394.11 | 386.02 | 1.4091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.715 |  | 514.1983 | 2.2397 | 511.83 | 498.665 | 0.0742 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 560.59 |  | 551.0581 | 1.7298 | 550 | 536.9 | 0.0874 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.595 |  | 368.1864 | 0.9258 | 368.42 | 357.97 | 1.7492 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 883.03 |  | 853.3103 | 3.4829 | 835.82 | 804.09 | 3.1675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.51 |  | 184.8825 | 2.5029 | 185.03 | 178.09 | 3.1133 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 396.38 |  | 387.7683 | 2.2208 | 384 | 368.28 | 0.3078 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 45.89 |  | 45.3435 | 1.2052 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.35 |  | 24.046 | 1.2644 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.3 |  | 744.6082 | 0.0929 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.13 |  | 294.0097 | 0.0409 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 127.09 |  | 125.1433 | 1.5556 | 125.02 | 121.79 | 0.7396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.85 |  | 71.6616 | 3.0538 | 71.24 | 68.65 | 1.7874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 293.88 |  | 283.4446 | 3.6816 | 280.565 | 273.17 | 4.233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.58 |  | 398.0689 | 1.1332 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.27 |  | 625.7395 | 1.3633 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1057.93 |  | 1038.3365 | 1.887 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 473.33 |  | 469.2321 | 0.8733 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.23 |  | 140.652 | 1.1219 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.355 |  | 163.4886 | 2.3649 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 281.63 |  | 270.7589 | 4.015 | 269.59 | 256.24 | 5.0172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 732.875 |  | 703.8295 | 4.1268 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 383.75 |  | 374.2636 | 2.5347 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.75 |  | 98.7075 | 5.1085 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 307.34 |  | 300.6258 | 2.2334 | 305.21 | 289.97 | 4.2233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1773.14 |  | 1742.8932 | 1.7354 | 1741.99 | 1704.935 | 0.2673 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 544.535 |  | 529.9422 | 2.7537 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 319.01 |  | 309.1055 | 3.2043 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.88 |  | 210.7358 | 1.9665 | 210.82 | 204.71 | 0.0512 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 320.81 |  | 310.3119 | 3.3831 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 275.77 |  | 267.7615 | 2.9909 | 265.71 | 258.355 | 4.9316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.59 |  | 60.7348 | 3.0546 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.95 |  | 49.2495 | 3.4529 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.1 |  | 133.1044 | 3.7532 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.35 |  | 315.7694 | 2.7173 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 517.71 |  | 521.5098 | -0.7286 | 526.74 | 522.205 | 4.5779 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 299.315 |  | 301.1543 | -0.6107 | 304.36 | 299.62 | 3.9891 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.39 |  | 24.8426 | 2.2035 | 25.45 | 24.1 | 0.0788 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.13 |  | 33.456 | 2.0146 | 34 | 32.26 | 0.0586 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.85 |  | 20.484 | 1.7868 | 20.445 | 19.92 | 0.0959 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1491.55 |  | 1412.7628 | 5.5768 | 1393.96 | 1325.48 | 4.9043 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 478.06 |  | 453.7645 | 5.3542 | 453.35 | 431.78 | 0.2406 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 772.62 |  | 739.9295 | 4.4181 | 724.57 | 702.24 | 0.1696 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.67 |  | 247.8822 | -0.0856 | 247.72 | 243.725 | 0.0202 | below_vwap | below_vwap |
| META | cloud_ai_capex | 631.825 |  | 635.1516 | -0.5237 | 649.07 | 638.97 | 0.5175 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 264.97 |  | 256.3123 | 3.3778 | 252.95 | 243.21 | 5.0949 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 165.775 |  | 156.2007 | 6.1295 | 151.99 | 145.6 | 3.9813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
