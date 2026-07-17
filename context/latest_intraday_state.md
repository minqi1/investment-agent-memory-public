# Intraday State

- Generated at: `2026-07-18T01:59:14+08:00`
- Market time ET: `2026-07-17T13:59:15-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 15, 'watch_only': 1, 'below_vwap': 5, 'spread_too_wide_or_missing': 32, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.65 |  | 695.368 | 0.472 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 525.53 |  | 517.8536 | 1.4823 | 511.83 | 498.665 | 0.0856 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 560.27 |  | 554.6819 | 1.0074 | 550 | 536.9 | 0.075 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.52 |  | 745.0036 | -0.0649 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.43 |  | 203.219 | 0.5959 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 560.27 |  | 554.6819 | 1.0074 | 550 | 536.9 | 0.075 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 374.35 |  | 369.9853 | 1.1797 | 368.42 | 357.97 | 0.0427 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 525.53 |  | 517.8536 | 1.4823 | 511.83 | 498.665 | 0.0856 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.42 |  | 294.2121 | 0.0707 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1060.85 |  | 1044.1768 | 1.5968 | 1001.82 | 982.21 | 0.214 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 698.65 |  | 695.368 | 0.472 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.395 |  | 45.6022 | 1.7385 | 44.92 | 43.715 | 0.0431 | buy_precheck_manual_confirm | none |
| 9 | SKHY | memory_hbm_storage | 159.285 |  | 158.5013 | 0.4945 | 151.99 | 145.6 | 0.2951 | buy_precheck_manual_confirm | none |
| 10 | COHR | ai_networking_optical | 280.97 |  | 273.7302 | 2.6449 | 269.59 | 256.24 | 0.2883 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.865 |  | 24.2726 | 2.4408 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.315 |  | 20.6318 | 3.3113 | 20.445 | 19.92 | 0.0469 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 25.775 |  | 25.0689 | 2.8166 | 25.45 | 24.1 | 0.0388 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 34.065 |  | 33.7822 | 0.837 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 15 | TQQQ | leveraged_tool | 68.51 |  | 67.1623 | 2.0067 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.42 |  | 294.2121 | 0.0707 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 204.43 |  | 203.219 | 0.5959 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 698.65 |  | 695.368 | 0.472 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.92 |  | 393.2204 | 0.4322 | 398.39 | 393.52 | 0.0734 | watch_only | none |
| 5 | IREN | high_beta_ai_infrastructure | 34.065 |  | 33.7822 | 0.837 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 6 | SKHY | memory_hbm_storage | 159.285 |  | 158.5013 | 0.4945 | 151.99 | 145.6 | 0.2951 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 537.24 |  | 535.4831 | 0.3281 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 141.31 |  | 140.9651 | 0.2447 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 560.27 |  | 554.6819 | 1.0074 | 550 | 536.9 | 0.075 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 374.35 |  | 369.9853 | 1.1797 | 368.42 | 357.97 | 0.0427 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 525.53 |  | 517.8536 | 1.4823 | 511.83 | 498.665 | 0.0856 | buy_precheck_manual_confirm | none |
| 12 | ALAB | ai_networking_optical | 306.3 |  | 305.2908 | 0.3306 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TT | data_center_power_cooling | 469.85 |  | 469.7772 | 0.0155 | 469.08 | 460.78 | 4.1928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 399.26 |  | 398.1185 | 0.2867 | 394.11 | 386.02 | 2.2416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | APLD | high_beta_ai_infrastructure | 25.775 |  | 25.0689 | 2.8166 | 25.45 | 24.1 | 0.0388 | buy_precheck_manual_confirm | none |
| 16 | HPE | ai_server_oem | 46.395 |  | 45.6022 | 1.7385 | 44.92 | 43.715 | 0.0431 | buy_precheck_manual_confirm | none |
| 17 | ASML | semiconductor_equipment | 1769.91 |  | 1755.962 | 0.7943 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SMCI | ai_server_oem | 24.865 |  | 24.2726 | 2.4408 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| 19 | ETN | data_center_power_cooling | 401.68 |  | 399.6407 | 0.5103 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 633.93 |  | 629.5122 | 0.7018 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.43 |  | 203.219 | 0.5959 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 560.27 |  | 554.6819 | 1.0074 | 550 | 536.9 | 0.075 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 374.35 |  | 369.9853 | 1.1797 | 368.42 | 357.97 | 0.0427 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 525.53 |  | 517.8536 | 1.4823 | 511.83 | 498.665 | 0.0856 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.42 |  | 294.2121 | 0.0707 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1060.85 |  | 1044.1768 | 1.5968 | 1001.82 | 982.21 | 0.214 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 698.65 |  | 695.368 | 0.472 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.395 |  | 45.6022 | 1.7385 | 44.92 | 43.715 | 0.0431 | buy_precheck_manual_confirm | none |
| 9 | SKHY | memory_hbm_storage | 159.285 |  | 158.5013 | 0.4945 | 151.99 | 145.6 | 0.2951 | buy_precheck_manual_confirm | none |
| 10 | COHR | ai_networking_optical | 280.97 |  | 273.7302 | 2.6449 | 269.59 | 256.24 | 0.2883 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.865 |  | 24.2726 | 2.4408 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.315 |  | 20.6318 | 3.3113 | 20.445 | 19.92 | 0.0469 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 25.775 |  | 25.0689 | 2.8166 | 25.45 | 24.1 | 0.0388 | buy_precheck_manual_confirm | none |
| 14 | IREN | high_beta_ai_infrastructure | 34.065 |  | 33.7822 | 0.837 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 15 | TQQQ | leveraged_tool | 68.51 |  | 67.1623 | 2.0067 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| 16 | SPY | market_regime | 744.52 |  | 745.0036 | -0.0649 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 17 | ANET | ai_networking_optical | 169.665 |  | 165.8957 | 2.2721 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TSM | foundry | 399.26 |  | 398.1185 | 0.2867 | 394.11 | 386.02 | 2.2416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 537.24 |  | 535.4831 | 0.3281 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 500.48 |  | 486.2636 | 2.9236 | 482.43 | 461.04 | 0.9411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.65 |  | 695.368 | 0.472 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.51 |  | 67.1623 | 2.0067 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.43 |  | 203.219 | 0.5959 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.92 |  | 393.2204 | 0.4322 | 398.39 | 393.52 | 0.0734 | watch_only | none |
| AAPL | mega_cap_platform | 331.46 |  | 331.9803 | -0.1567 | 334.98 | 331.295 | 0.0121 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 344.25 |  | 346.0111 | -0.509 | 348.47 | 341.42 | 0.1714 | below_vwap | below_vwap |
| AMD | ai_accelerator | 500.48 |  | 486.2636 | 2.9236 | 482.43 | 461.04 | 0.9411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 399.26 |  | 398.1185 | 0.2867 | 394.11 | 386.02 | 2.2416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.53 |  | 517.8536 | 1.4823 | 511.83 | 498.665 | 0.0856 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 560.27 |  | 554.6819 | 1.0074 | 550 | 536.9 | 0.075 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 374.35 |  | 369.9853 | 1.1797 | 368.42 | 357.97 | 0.0427 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 885.13 |  | 863.1564 | 2.5457 | 835.82 | 804.09 | 1.619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 191.42 |  | 186.9527 | 2.3895 | 185.03 | 178.09 | 1.0657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.72 |  | 392.142 | 2.6975 | 384 | 368.28 | 4.4671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.395 |  | 45.6022 | 1.7385 | 44.92 | 43.715 | 0.0431 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.865 |  | 24.2726 | 2.4408 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.52 |  | 745.0036 | -0.0649 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.42 |  | 294.2121 | 0.0707 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.46 |  | 125.9071 | 1.2334 | 125.02 | 121.79 | 0.6669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.94 |  | 72.127 | 2.5136 | 71.24 | 68.65 | 0.7168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 293.98 |  | 286.8465 | 2.4869 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.68 |  | 399.6407 | 0.5103 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 633.93 |  | 629.5122 | 0.7018 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1060.85 |  | 1044.1768 | 1.5968 | 1001.82 | 982.21 | 0.214 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 469.85 |  | 469.7772 | 0.0155 | 469.08 | 460.78 | 4.1928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.31 |  | 140.9651 | 0.2447 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 169.665 |  | 165.8957 | 2.2721 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 280.97 |  | 273.7302 | 2.6449 | 269.59 | 256.24 | 0.2883 | buy_precheck_manual_confirm | none |
| LITE | ai_networking_optical | 738.58 |  | 715.0077 | 3.2968 | 694.98 | 653.305 | 0.8354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 380.58 |  | 377.6263 | 0.7822 | 375.52 | 359.81 | 4.6219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 103.8 |  | 100.3796 | 3.4074 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 306.3 |  | 305.2908 | 0.3306 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1769.91 |  | 1755.962 | 0.7943 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 537.24 |  | 535.4831 | 0.3281 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 313.85 |  | 312.0852 | 0.5655 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.51 |  | 212.1335 | 0.6489 | 210.82 | 204.71 | 2.398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 325.115 |  | 319.1066 | 1.8829 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.37 |  | 277.3949 | 1.0725 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.54 |  | 61.3887 | 1.8754 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.32 |  | 49.8408 | 2.9679 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.03 |  | 134.2784 | 2.7939 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.95 |  | 318.2787 | 2.4102 | 315.89 | 307.13 | 4.8811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.17 |  | 520.2079 | -1.1607 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.09 |  | 299.5042 | -1.14 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.775 |  | 25.0689 | 2.8166 | 25.45 | 24.1 | 0.0388 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.065 |  | 33.7822 | 0.837 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 21.315 |  | 20.6318 | 3.3113 | 20.445 | 19.92 | 0.0469 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1440.49 |  | 1428.0441 | 0.8715 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 485.27 |  | 465.7786 | 4.1847 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 782.6 |  | 758.7281 | 3.1463 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.41 |  | 248.0377 | -0.2531 | 247.72 | 243.725 | 0.0364 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.99 |  | 641.6936 | 1.1371 | 649.07 | 638.97 | 2.3036 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.05 |  | 260.9171 | 3.8836 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.285 |  | 158.5013 | 0.4945 | 151.99 | 145.6 | 0.2951 | buy_precheck_manual_confirm | none |
