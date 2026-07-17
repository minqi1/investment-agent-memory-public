# Intraday State

- Generated at: `2026-07-18T00:10:47+08:00`
- Market time ET: `2026-07-17T12:10:48-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 5, 'watch_only': 1, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1, 'below_vwap': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.04 |  | 693.7541 | 0.7619 | 693.36 | 686.78 | 0.0429 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 528.33 |  | 514.4667 | 2.6947 | 511.83 | 498.665 | 0.089 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 563.1 |  | 551.1542 | 2.1674 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.92 |  | 744.625 | 0.1739 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.71 |  | 202.4904 | 1.0961 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 563.1 |  | 551.1542 | 2.1674 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 528.33 |  | 514.4667 | 2.6947 | 511.83 | 498.665 | 0.089 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1784.63 |  | 1743.4419 | 2.3625 | 1741.99 | 1704.935 | 0.2185 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 215.92 |  | 210.8798 | 2.3901 | 210.82 | 204.71 | 0.0973 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 294.62 |  | 294.011 | 0.2071 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 699.04 |  | 693.7541 | 0.7619 | 693.36 | 686.78 | 0.0429 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.9 |  | 45.3536 | 1.2046 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.92 |  | 744.625 | 0.1739 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.43 |  | 24.0492 | 1.5834 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.489 | 2.1035 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.53 |  | 24.8493 | 2.7392 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.28 |  | 33.4686 | 2.4243 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.56 |  | 66.8333 | 2.5835 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.62 |  | 294.011 | 0.2071 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 745.92 |  | 744.625 | 0.1739 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 699.04 |  | 693.7541 | 0.7619 | 693.36 | 686.78 | 0.0429 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 346.74 |  | 346.063 | 0.1956 | 348.47 | 341.42 | 0.349 | watch_only | none |
| 5 | NVDA | ai_accelerator | 204.71 |  | 202.4904 | 1.0961 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.9 |  | 45.3536 | 1.2046 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.53 |  | 24.8493 | 2.7392 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.43 |  | 24.0492 | 1.5834 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 9 | SMH | semiconductor_index | 563.1 |  | 551.1542 | 2.1674 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 528.33 |  | 514.4667 | 2.6947 | 511.83 | 498.665 | 0.089 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 215.92 |  | 210.8798 | 2.3901 | 210.82 | 204.71 | 0.0973 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.28 |  | 33.4686 | 2.4243 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | TT | data_center_power_cooling | 472.75 |  | 469.2584 | 0.7441 | 469.08 | 460.78 | 3.4098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ASML | semiconductor_equipment | 1784.63 |  | 1743.4419 | 2.3625 | 1741.99 | 1704.935 | 0.2185 | buy_precheck_manual_confirm | none |
| 15 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.489 | 2.1035 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| 16 | AMZN | cloud_ai_capex | 247.71 |  | 247.8795 | -0.0684 | 247.72 | 243.725 | 0.0323 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 403.355 |  | 398.3299 | 1.2615 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 371.65 |  | 368.1942 | 0.9386 | 368.42 | 357.97 | 1.2081 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | JCI | data_center_power_cooling | 142.18 |  | 140.6964 | 1.0544 | 140.765 | 137.165 | 4.7967 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.71 |  | 202.4904 | 1.0961 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 563.1 |  | 551.1542 | 2.1674 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 528.33 |  | 514.4667 | 2.6947 | 511.83 | 498.665 | 0.089 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1784.63 |  | 1743.4419 | 2.3625 | 1741.99 | 1704.935 | 0.2185 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 215.92 |  | 210.8798 | 2.3901 | 210.82 | 204.71 | 0.0973 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 294.62 |  | 294.011 | 0.2071 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 699.04 |  | 693.7541 | 0.7619 | 693.36 | 686.78 | 0.0429 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.9 |  | 45.3536 | 1.2046 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.92 |  | 744.625 | 0.1739 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.43 |  | 24.0492 | 1.5834 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.489 | 2.1035 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.53 |  | 24.8493 | 2.7392 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.28 |  | 33.4686 | 2.4243 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.56 |  | 66.8333 | 2.5835 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 167.83 |  | 163.5316 | 2.6285 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TSM | foundry | 403.66 |  | 396.0187 | 1.9295 | 394.11 | 386.02 | 1.4046 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 371.65 |  | 368.1942 | 0.9386 | 368.42 | 357.97 | 1.2081 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 548.28 |  | 530.1337 | 3.423 | 535.095 | 513.34 | 1.7455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 501.9 |  | 482.573 | 4.005 | 482.43 | 461.04 | 1.2114 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 472.75 |  | 469.2584 | 0.7441 | 469.08 | 460.78 | 3.4098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.04 |  | 693.7541 | 0.7619 | 693.36 | 686.78 | 0.0429 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.56 |  | 66.8333 | 2.5835 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.71 |  | 202.4904 | 1.0961 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 391.555 |  | 392.9846 | -0.3638 | 398.39 | 393.52 | 0.2682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.575 |  | 332.4256 | -0.5567 | 334.98 | 331.295 | 0.0182 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.74 |  | 346.063 | 0.1956 | 348.47 | 341.42 | 0.349 | watch_only | none |
| AMD | ai_accelerator | 501.9 |  | 482.573 | 4.005 | 482.43 | 461.04 | 1.2114 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 403.66 |  | 396.0187 | 1.9295 | 394.11 | 386.02 | 1.4046 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.33 |  | 514.4667 | 2.6947 | 511.83 | 498.665 | 0.089 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 563.1 |  | 551.1542 | 2.1674 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.65 |  | 368.1942 | 0.9386 | 368.42 | 357.97 | 1.2081 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 886.95 |  | 853.5808 | 3.9093 | 835.82 | 804.09 | 0.6697 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 190.68 |  | 184.9716 | 3.0861 | 185.03 | 178.09 | 2.9683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 395.31 |  | 387.8744 | 1.917 | 384 | 368.28 | 3.1545 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.9 |  | 45.3536 | 1.2046 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.43 |  | 24.0492 | 1.5834 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.92 |  | 744.625 | 0.1739 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.62 |  | 294.011 | 0.2071 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.15 |  | 125.1745 | 1.5782 | 125.02 | 121.79 | 0.4247 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 74.13 |  | 71.6835 | 3.4129 | 71.24 | 68.65 | 1.8751 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 295.07 |  | 283.5194 | 4.074 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 403.355 |  | 398.3299 | 1.2615 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 635.975 |  | 625.8981 | 1.61 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1061.85 |  | 1038.6431 | 2.2344 | 1001.82 | 982.21 | 3.7576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 472.75 |  | 469.2584 | 0.7441 | 469.08 | 460.78 | 3.4098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 142.18 |  | 140.6964 | 1.0544 | 140.765 | 137.165 | 4.7967 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.83 |  | 163.5316 | 2.6285 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 282.785 |  | 270.8588 | 4.4031 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 734.97 |  | 704.2926 | 4.3558 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 385.13 |  | 374.3246 | 2.8866 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.335 |  | 98.7733 | 4.6183 | 97.585 | 91.92 | 4.1903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 307.18 |  | 300.7145 | 2.15 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1784.63 |  | 1743.4419 | 2.3625 | 1741.99 | 1704.935 | 0.2185 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 548.28 |  | 530.1337 | 3.423 | 535.095 | 513.34 | 1.7455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.6 |  | 309.5569 | 3.5674 | 306.51 | 298.89 | 4.5789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 215.92 |  | 210.8798 | 2.3901 | 210.82 | 204.71 | 0.0973 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 322.78 |  | 310.4476 | 3.9725 | 308.03 | 297.18 | 4.3342 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 276.29 |  | 267.8207 | 3.1623 | 265.71 | 258.355 | 3.9017 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.96 |  | 60.7727 | 3.5992 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.03 |  | 49.3643 | 3.3743 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.03 |  | 133.1461 | 3.668 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.32 |  | 316.1436 | 2.9026 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 517.15 |  | 521.474 | -0.8292 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 298.935 |  | 301.1434 | -0.7333 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.53 |  | 24.8493 | 2.7392 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.28 |  | 33.4686 | 2.4243 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.489 | 2.1035 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1491.15 |  | 1413.9099 | 5.4629 | 1393.96 | 1325.48 | 4.5703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 479.6 |  | 454.2924 | 5.5708 | 453.35 | 431.78 | 0.6735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 775.31 |  | 740.5495 | 4.6939 | 724.57 | 702.24 | 4.0113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.71 |  | 247.8795 | -0.0684 | 247.72 | 243.725 | 0.0323 | below_vwap | below_vwap |
| META | cloud_ai_capex | 632.975 |  | 635.0846 | -0.3322 | 649.07 | 638.97 | 0.7157 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 266.87 |  | 256.4912 | 4.0464 | 252.95 | 243.21 | 4.1219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.025 |  | 156.4345 | 6.1307 | 151.99 | 145.6 | 0.8432 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
