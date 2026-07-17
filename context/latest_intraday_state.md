# Intraday State

- Generated at: `2026-07-17T22:27:59+08:00`
- Market time ET: `2026-07-17T10:28:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 4, 'spread_too_wide_or_missing': 34, 'price_stale_or_missing': 1, 'below_vwap': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.42 |  | 692.2624 | 0.745 | 693.36 | 686.78 | 0.0401 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 520.08 |  | 510.9554 | 1.7858 | 511.83 | 498.665 | 0.15 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.93 |  | 549.0389 | 1.4372 | 550 | 536.9 | 0.088 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.72 |  | 743.8146 | 0.3906 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.26 |  | 201.5757 | 1.3317 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.93 |  | 549.0389 | 1.4372 | 550 | 536.9 | 0.088 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 489.9 |  | 475.4374 | 3.042 | 482.43 | 461.04 | 0.2041 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 520.08 |  | 510.9554 | 1.7858 | 511.83 | 498.665 | 0.15 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 866.76 |  | 840.7725 | 3.0909 | 835.82 | 804.09 | 0.2965 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.63 |  | 293.8641 | 0.6009 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 697.42 |  | 692.2624 | 0.745 | 693.36 | 686.78 | 0.0401 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.95 |  | 45.0022 | 2.1061 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 746.72 |  | 743.8146 | 0.3906 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 460.615 |  | 448.7563 | 2.6426 | 453.35 | 431.78 | 0.191 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.74 |  | 247.0121 | 0.6995 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.31 |  | 23.9651 | 1.4394 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.09 |  | 66.3136 | 2.6787 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 295.63 |  | 293.8641 | 0.6009 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 697.42 |  | 692.2624 | 0.745 | 693.36 | 686.78 | 0.0401 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 746.72 |  | 743.8146 | 0.3906 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 248.74 |  | 247.0121 | 0.6995 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 204.26 |  | 201.5757 | 1.3317 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.31 |  | 23.9651 | 1.4394 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 556.93 |  | 549.0389 | 1.4372 | 550 | 536.9 | 0.088 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 25.09 |  | 24.7631 | 1.3203 | 25.45 | 24.1 | 0.0399 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 33.79 |  | 33.3392 | 1.3521 | 34 | 32.26 | 0.0592 | watch_only | none |
| 10 | GOOGL | cloud_ai_capex | 346.43 |  | 345.3532 | 0.3118 | 348.47 | 341.42 | 1.1027 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ASML | semiconductor_equipment | 1743.94 |  | 1732.303 | 0.6718 | 1741.99 | 1704.935 | 0.7288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SOXX | semiconductor_index | 520.08 |  | 510.9554 | 1.7858 | 511.83 | 498.665 | 0.15 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 45.95 |  | 45.0022 | 2.1061 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| 14 | AMD | ai_accelerator | 489.9 |  | 475.4374 | 3.042 | 482.43 | 461.04 | 0.2041 | buy_precheck_manual_confirm | none |
| 15 | MU | memory_hbm_storage | 866.76 |  | 840.7725 | 3.0909 | 835.82 | 804.09 | 0.2965 | buy_precheck_manual_confirm | none |
| 16 | JCI | data_center_power_cooling | 140.96 |  | 139.4417 | 1.0888 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 460.615 |  | 448.7563 | 2.6426 | 453.35 | 431.78 | 0.191 | buy_precheck_manual_confirm | none |
| 18 | TT | data_center_power_cooling | 471.8 |  | 467.839 | 0.8467 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 370.915 |  | 367.1455 | 1.0267 | 368.42 | 357.97 | 1.0488 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ORCL | cloud_ai_capex | 126.24 |  | 124.5268 | 1.3758 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.26 |  | 201.5757 | 1.3317 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.93 |  | 549.0389 | 1.4372 | 550 | 536.9 | 0.088 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 489.9 |  | 475.4374 | 3.042 | 482.43 | 461.04 | 0.2041 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 520.08 |  | 510.9554 | 1.7858 | 511.83 | 498.665 | 0.15 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 866.76 |  | 840.7725 | 3.0909 | 835.82 | 804.09 | 0.2965 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.63 |  | 293.8641 | 0.6009 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 697.42 |  | 692.2624 | 0.745 | 693.36 | 686.78 | 0.0401 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.95 |  | 45.0022 | 2.1061 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 746.72 |  | 743.8146 | 0.3906 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 10 | WDC | memory_hbm_storage | 460.615 |  | 448.7563 | 2.6426 | 453.35 | 431.78 | 0.191 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.74 |  | 247.0121 | 0.6995 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.31 |  | 23.9651 | 1.4394 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.09 |  | 66.3136 | 2.6787 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 166.43 |  | 162.1121 | 2.6635 | 163.275 | 157.34 | 3.7794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 399.09 |  | 393.3345 | 1.4633 | 394.11 | 386.02 | 2.631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 370.915 |  | 367.1455 | 1.0267 | 368.42 | 357.97 | 1.0488 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 537.39 |  | 526.8078 | 2.0087 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ASML | semiconductor_equipment | 1743.94 |  | 1732.303 | 0.6718 | 1741.99 | 1704.935 | 0.7288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 471.8 |  | 467.839 | 0.8467 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 212.71 |  | 210.0835 | 1.2502 | 210.82 | 204.71 | 2.3365 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.42 |  | 692.2624 | 0.745 | 693.36 | 686.78 | 0.0401 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.09 |  | 66.3136 | 2.6787 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.26 |  | 201.5757 | 1.3317 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.44 |  | 394.4892 | -0.266 | 398.39 | 393.52 | 0.0585 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 331.27 |  | 331.8874 | -0.186 | 334.98 | 331.295 | 0.0362 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.43 |  | 345.3532 | 0.3118 | 348.47 | 341.42 | 1.1027 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 489.9 |  | 475.4374 | 3.042 | 482.43 | 461.04 | 0.2041 | buy_precheck_manual_confirm | none |
| TSM | foundry | 399.09 |  | 393.3345 | 1.4633 | 394.11 | 386.02 | 2.631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 520.08 |  | 510.9554 | 1.7858 | 511.83 | 498.665 | 0.15 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.93 |  | 549.0389 | 1.4372 | 550 | 536.9 | 0.088 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 370.915 |  | 367.1455 | 1.0267 | 368.42 | 357.97 | 1.0488 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 866.76 |  | 840.7725 | 3.0909 | 835.82 | 804.09 | 0.2965 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 188.05 |  | 184.0219 | 2.1889 | 185.03 | 178.09 | 0.6647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 397.33 |  | 383.2386 | 3.6769 | 384 | 368.28 | 4.0822 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.95 |  | 45.0022 | 2.1061 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.31 |  | 23.9651 | 1.4394 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.72 |  | 743.8146 | 0.3906 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.63 |  | 293.8641 | 0.6009 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.24 |  | 124.5268 | 1.3758 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 71.9 |  | 70.7041 | 1.6914 | 71.24 | 68.65 | 4.2003 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 286.55 |  | 281.1795 | 1.91 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 398.7 |  | 395.0817 | 0.9158 | 389.4 | 382.38 | 3.0098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 629.04 |  | 620.9304 | 1.306 | 616.75 | 609.05 | 4.8041 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1049.04 |  | 1021.7725 | 2.6687 | 1001.82 | 982.21 | 1.0972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 471.8 |  | 467.839 | 0.8467 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.96 |  | 139.4417 | 1.0888 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.43 |  | 162.1121 | 2.6635 | 163.275 | 157.34 | 3.7794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.38 |  | 267.2159 | 4.1779 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 727 |  | 692.548 | 4.9747 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 382.24 |  | 371.9715 | 2.7606 | 375.52 | 359.81 | 3.9739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 101.54 |  | 96.5524 | 5.1657 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 306.46 |  | 300.0679 | 2.1302 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1743.94 |  | 1732.303 | 0.6718 | 1741.99 | 1704.935 | 0.7288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 537.39 |  | 526.8078 | 2.0087 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 311.655 |  | 305.2381 | 2.1023 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 212.71 |  | 210.0835 | 1.2502 | 210.82 | 204.71 | 2.3365 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 315.55 |  | 308.2072 | 2.3824 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 271.09 |  | 265.6934 | 2.0311 | 265.71 | 258.355 | 4.2495 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 61.43 |  | 59.7683 | 2.7803 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.11 |  | 48.3461 | 3.6485 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.01 |  | 131.9674 | 3.0633 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 319.705 |  | 313.9556 | 1.8313 | 315.89 | 307.13 | 4.8482 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 520.91 |  | 521.8656 | -0.1831 | 526.74 | 522.205 | 0.3571 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 301.28 |  | 301.9383 | -0.218 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.09 |  | 24.7631 | 1.3203 | 25.45 | 24.1 | 0.0399 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.79 |  | 33.3392 | 1.3521 | 34 | 32.26 | 0.0592 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.58 |  | 20.2422 | 1.6687 | 20.445 | 19.92 | 0.5345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SNDK | memory_hbm_storage | 1438.905 |  | 1394.8569 | 3.1579 | 1393.96 | 1325.48 | 1.376 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 460.615 |  | 448.7563 | 2.6426 | 453.35 | 431.78 | 0.191 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 745.69 |  | 728.7001 | 2.3315 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.74 |  | 247.0121 | 0.6995 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 635.7 |  | 639.4197 | -0.5817 | 649.07 | 638.97 | 5.0055 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 262.81 |  | 252.6773 | 4.0101 | 252.95 | 243.21 | 0.3615 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 157.43 |  | 154.3239 | 2.0127 | 151.99 | 145.6 | 1.7532 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
