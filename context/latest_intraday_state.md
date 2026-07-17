# Intraday State

- Generated at: `2026-07-17T22:33:18+08:00`
- Market time ET: `2026-07-17T10:33:20-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 3, 'watch_only': 6, 'spread_too_wide_or_missing': 32, 'price_stale_or_missing': 1, 'below_vwap': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.31 |  | 692.4981 | 0.5505 | 693.36 | 686.78 | 0.0847 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 518.18 |  | 511.2012 | 1.3652 | 511.83 | 498.665 | 0.0926 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 554.395 |  | 549.1654 | 0.9523 | 550 | 536.9 | 0.0722 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.13 |  | 743.987 | 0.288 | 742.66 | 740.8 | 0.0161 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.81 |  | 201.6885 | 1.0519 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 399.085 |  | 393.5773 | 1.3994 | 394.11 | 386.02 | 0.1027 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 554.395 |  | 549.1654 | 0.9523 | 550 | 536.9 | 0.0722 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 518.18 |  | 511.2012 | 1.3652 | 511.83 | 498.665 | 0.0926 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 211.56 |  | 210.2118 | 0.6414 | 210.82 | 204.71 | 0.1465 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.25 |  | 293.8981 | 0.46 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.31 |  | 692.4981 | 0.5505 | 693.36 | 686.78 | 0.0847 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.73 |  | 45.0917 | 1.4155 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 746.13 |  | 743.987 | 0.288 | 742.66 | 740.8 | 0.0161 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.46 |  | 247.0799 | 0.5586 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.2662 | 1.0055 | 20.445 | 19.92 | 0.1954 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.78 |  | 66.382 | 2.106 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.13 |  | 743.987 | 0.288 | 742.66 | 740.8 | 0.0161 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.46 |  | 247.0799 | 0.5586 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 211.56 |  | 210.2118 | 0.6414 | 210.82 | 204.71 | 0.1465 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 295.25 |  | 293.8981 | 0.46 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.31 |  | 692.4981 | 0.5505 | 693.36 | 686.78 | 0.0847 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 332.855 |  | 331.8949 | 0.2893 | 334.98 | 331.295 | 0.012 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 345.41 |  | 345.3665 | 0.0126 | 348.47 | 341.42 | 0.1737 | watch_only | none |
| 8 | NVDA | ai_accelerator | 203.81 |  | 201.6885 | 1.0519 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1741.89 |  | 1732.7276 | 0.5288 | 1741.99 | 1704.935 | 0.0614 | watch_only | none |
| 10 | SMH | semiconductor_index | 554.395 |  | 549.1654 | 0.9523 | 550 | 536.9 | 0.0722 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 399.085 |  | 393.5773 | 1.3994 | 394.11 | 386.02 | 0.1027 | buy_precheck_manual_confirm | none |
| 12 | SOXX | semiconductor_index | 518.18 |  | 511.2012 | 1.3652 | 511.83 | 498.665 | 0.0926 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.2662 | 1.0055 | 20.445 | 19.92 | 0.1954 | buy_precheck_manual_confirm | none |
| 14 | HPE | ai_server_oem | 45.73 |  | 45.0917 | 1.4155 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 24.23 |  | 23.9926 | 0.9897 | 24.3 | 23.46 | 0.0413 | watch_only | none |
| 16 | APLD | high_beta_ai_infrastructure | 25.1 |  | 24.7734 | 1.3182 | 25.45 | 24.1 | 0.0398 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 33.69 |  | 33.3721 | 0.9525 | 34 | 32.26 | 0.0594 | watch_only | none |
| 18 | TT | data_center_power_cooling | 470.87 |  | 468.0088 | 0.6114 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 140.56 |  | 139.5277 | 0.7398 | 140.765 | 137.165 | 4.8236 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ETN | data_center_power_cooling | 397.33 |  | 395.3912 | 0.4904 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.81 |  | 201.6885 | 1.0519 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 399.085 |  | 393.5773 | 1.3994 | 394.11 | 386.02 | 0.1027 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 554.395 |  | 549.1654 | 0.9523 | 550 | 536.9 | 0.0722 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 518.18 |  | 511.2012 | 1.3652 | 511.83 | 498.665 | 0.0926 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 211.56 |  | 210.2118 | 0.6414 | 210.82 | 204.71 | 0.1465 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 295.25 |  | 293.8981 | 0.46 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.31 |  | 692.4981 | 0.5505 | 693.36 | 686.78 | 0.0847 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.73 |  | 45.0917 | 1.4155 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 746.13 |  | 743.987 | 0.288 | 742.66 | 740.8 | 0.0161 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.46 |  | 247.0799 | 0.5586 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.2662 | 1.0055 | 20.445 | 19.92 | 0.1954 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.78 |  | 66.382 | 2.106 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 13 | ANET | ai_networking_optical | 165.65 |  | 162.2451 | 2.0986 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 370.41 |  | 367.2803 | 0.8521 | 368.42 | 357.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AMD | ai_accelerator | 486.45 |  | 476.0451 | 2.1857 | 482.43 | 461.04 | 0.3618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 470.87 |  | 468.0088 | 0.6114 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MU | memory_hbm_storage | 865.11 |  | 843.3987 | 2.5743 | 835.82 | 804.09 | 1.3062 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | VRT | data_center_power_cooling | 284.745 |  | 281.371 | 1.1991 | 280.565 | 273.17 | 4.4215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | CIEN | ai_networking_optical | 380.45 |  | 372.0894 | 2.2469 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 397.33 |  | 395.3912 | 0.4904 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.31 |  | 692.4981 | 0.5505 | 693.36 | 686.78 | 0.0847 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.78 |  | 66.382 | 2.106 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.81 |  | 201.6885 | 1.0519 | 203.41 | 197.98 | 0.0245 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.72 |  | 394.3938 | -0.4244 | 398.39 | 393.52 | 0.056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 332.855 |  | 331.8949 | 0.2893 | 334.98 | 331.295 | 0.012 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.41 |  | 345.3665 | 0.0126 | 348.47 | 341.42 | 0.1737 | watch_only | none |
| AMD | ai_accelerator | 486.45 |  | 476.0451 | 2.1857 | 482.43 | 461.04 | 0.3618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 399.085 |  | 393.5773 | 1.3994 | 394.11 | 386.02 | 0.1027 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 518.18 |  | 511.2012 | 1.3652 | 511.83 | 498.665 | 0.0926 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 554.395 |  | 549.1654 | 0.9523 | 550 | 536.9 | 0.0722 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 370.41 |  | 367.2803 | 0.8521 | 368.42 | 357.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 865.11 |  | 843.3987 | 2.5743 | 835.82 | 804.09 | 1.3062 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 186.52 |  | 184.179 | 1.271 | 185.03 | 178.09 | 1.1634 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 395.66 |  | 384.4307 | 2.921 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.73 |  | 45.0917 | 1.4155 | 44.92 | 43.715 | 0.0437 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.23 |  | 23.9926 | 0.9897 | 24.3 | 23.46 | 0.0413 | watch_only | none |
| SPY | market_regime | 746.13 |  | 743.987 | 0.288 | 742.66 | 740.8 | 0.0161 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.25 |  | 293.8981 | 0.46 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.8 |  | 124.6365 | 0.9335 | 125.02 | 121.79 | 3.5215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.27 |  | 70.7815 | 3.5158 | 71.24 | 68.65 | 2.484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 284.745 |  | 281.371 | 1.1991 | 280.565 | 273.17 | 4.4215 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 397.33 |  | 395.3912 | 0.4904 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 626.17 |  | 621.3428 | 0.7769 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1042.22 |  | 1022.8636 | 1.8924 | 1001.82 | 982.21 | 1.1706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.87 |  | 468.0088 | 0.6114 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.56 |  | 139.5277 | 0.7398 | 140.765 | 137.165 | 4.8236 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 165.65 |  | 162.2451 | 2.0986 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.66 |  | 267.408 | 3.4599 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 722.68 |  | 693.5764 | 4.1962 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 380.45 |  | 372.0894 | 2.2469 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.01 |  | 96.7422 | 4.4115 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.23 |  | 300.1972 | 1.3434 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1741.89 |  | 1732.7276 | 0.5288 | 1741.99 | 1704.935 | 0.0614 | watch_only | none |
| AMAT | semiconductor_equipment | 533.65 |  | 527.2068 | 1.2221 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 310.81 |  | 305.615 | 1.6998 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 211.56 |  | 210.2118 | 0.6414 | 210.82 | 204.71 | 0.1465 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 313.295 |  | 308.3667 | 1.5982 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 270.04 |  | 265.7741 | 1.6051 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.08 |  | 59.8886 | 1.9894 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.85 |  | 48.3803 | 3.0378 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 134.99 |  | 132.0655 | 2.2144 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 318.09 |  | 314.1148 | 1.2655 | 315.89 | 307.13 | 3.9706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 521.2 |  | 521.8406 | -0.1228 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.37 |  | 301.8109 | -0.1461 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.1 |  | 24.7734 | 1.3182 | 25.45 | 24.1 | 0.0398 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.69 |  | 33.3721 | 0.9525 | 34 | 32.26 | 0.0594 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.2662 | 1.0055 | 20.445 | 19.92 | 0.1954 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1424.2 |  | 1396.8731 | 1.9563 | 1393.96 | 1325.48 | 1.7554 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 458.955 |  | 449.049 | 2.206 | 453.35 | 431.78 | 0.4685 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 743.91 |  | 729.1611 | 2.0227 | 724.57 | 702.24 | 4.803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.46 |  | 247.0799 | 0.5586 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 633.895 |  | 639.2521 | -0.838 | 649.07 | 638.97 | 2.5793 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 262.29 |  | 252.9748 | 3.6823 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 156.38 |  | 154.4347 | 1.2597 | 151.99 | 145.6 | 4.4763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
