# Intraday State

- Generated at: `2026-07-18T00:55:11+08:00`
- Market time ET: `2026-07-17T12:55:12-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 4, 'spread_too_wide_or_missing': 35, 'price_stale_or_missing': 1, 'below_vwap': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701.34 |  | 694.3241 | 1.0105 | 693.36 | 686.78 | 0.0613 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 529.24 |  | 516.0764 | 2.5507 | 511.83 | 498.665 | 0.085 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 564.17 |  | 553.0539 | 2.01 | 550 | 536.9 | 0.0514 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.89 |  | 744.8028 | 0.2802 | 742.66 | 740.8 | 0.0013 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 205.96 |  | 202.7826 | 1.5669 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 564.17 |  | 553.0539 | 2.01 | 550 | 536.9 | 0.0514 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 529.24 |  | 516.0764 | 2.5507 | 511.83 | 498.665 | 0.085 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.71 |  | 294.0544 | 0.2229 | 294.205 | 291.675 | 0.0204 | buy_precheck_manual_confirm | none |
| 5 | PWR | data_center_power_cooling | 633.44 |  | 627.9933 | 0.8673 | 616.75 | 609.05 | 0.2036 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 701.34 |  | 694.3241 | 1.0105 | 693.36 | 686.78 | 0.0613 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.045 |  | 45.4475 | 1.3146 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.89 |  | 744.8028 | 0.2802 | 742.66 | 740.8 | 0.0013 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 249.1 |  | 247.9587 | 0.4603 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.84 |  | 24.1369 | 2.9131 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.985 |  | 20.5414 | 2.1594 | 20.445 | 19.92 | 0.143 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.25 |  | 33.5694 | 2.0273 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 69.24 |  | 66.9714 | 3.3874 | 66.9 | 64.92 | 0.0144 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.71 |  | 294.0544 | 0.2229 | 294.205 | 291.675 | 0.0204 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 746.89 |  | 744.8028 | 0.2802 | 742.66 | 740.8 | 0.0013 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 249.1 |  | 247.9587 | 0.4603 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 332.74 |  | 332.2698 | 0.1415 | 334.98 | 331.295 | 0.027 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 347.18 |  | 346.1486 | 0.298 | 348.47 | 341.42 | 0.2794 | watch_only | none |
| 6 | MSFT | cloud_ai_capex | 394.55 |  | 392.993 | 0.3962 | 398.39 | 393.52 | 0.0684 | watch_only | none |
| 7 | QQQ | market_regime | 701.34 |  | 694.3241 | 1.0105 | 693.36 | 686.78 | 0.0613 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.045 |  | 45.4475 | 1.3146 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 205.96 |  | 202.7826 | 1.5669 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 633.44 |  | 627.9933 | 0.8673 | 616.75 | 609.05 | 0.2036 | buy_precheck_manual_confirm | none |
| 11 | JCI | data_center_power_cooling | 141.65 |  | 140.7661 | 0.628 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 34.25 |  | 33.5694 | 2.0273 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 564.17 |  | 553.0539 | 2.01 | 550 | 536.9 | 0.0514 | buy_precheck_manual_confirm | none |
| 14 | SOXX | semiconductor_index | 529.24 |  | 516.0764 | 2.5507 | 511.83 | 498.665 | 0.085 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 24.84 |  | 24.1369 | 2.9131 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.985 |  | 20.5414 | 2.1594 | 20.445 | 19.92 | 0.143 | buy_precheck_manual_confirm | none |
| 17 | APLD | high_beta_ai_infrastructure | 25.42 |  | 24.91 | 2.0472 | 25.45 | 24.1 | 0.0787 | watch_only | none |
| 18 | TT | data_center_power_cooling | 473.36 |  | 469.4989 | 0.8224 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | CIEN | ai_networking_optical | 379.03 |  | 375.284 | 0.9982 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 402.105 |  | 399.1451 | 0.7415 | 389.4 | 382.38 | 3.2131 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 205.96 |  | 202.7826 | 1.5669 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 564.17 |  | 553.0539 | 2.01 | 550 | 536.9 | 0.0514 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 529.24 |  | 516.0764 | 2.5507 | 511.83 | 498.665 | 0.085 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.71 |  | 294.0544 | 0.2229 | 294.205 | 291.675 | 0.0204 | buy_precheck_manual_confirm | none |
| 5 | PWR | data_center_power_cooling | 633.44 |  | 627.9933 | 0.8673 | 616.75 | 609.05 | 0.2036 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 701.34 |  | 694.3241 | 1.0105 | 693.36 | 686.78 | 0.0613 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.045 |  | 45.4475 | 1.3146 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.89 |  | 744.8028 | 0.2802 | 742.66 | 740.8 | 0.0013 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 249.1 |  | 247.9587 | 0.4603 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.84 |  | 24.1369 | 2.9131 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.985 |  | 20.5414 | 2.1594 | 20.445 | 19.92 | 0.143 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.25 |  | 33.5694 | 2.0273 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 69.24 |  | 66.9714 | 3.3874 | 66.9 | 64.92 | 0.0144 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 168.94 |  | 164.3855 | 2.7706 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 402.56 |  | 396.9913 | 1.4027 | 394.11 | 386.02 | 0.621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 375.38 |  | 368.9373 | 1.7463 | 368.42 | 357.97 | 2.5281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 545.59 |  | 533.7091 | 2.2261 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 502.3 |  | 484.0263 | 3.7754 | 482.43 | 461.04 | 0.4937 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1782.605 |  | 1747.3972 | 2.0149 | 1741.99 | 1704.935 | 1.2521 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 473.36 |  | 469.4989 | 0.8224 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701.34 |  | 694.3241 | 1.0105 | 693.36 | 686.78 | 0.0613 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 69.24 |  | 66.9714 | 3.3874 | 66.9 | 64.92 | 0.0144 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 205.96 |  | 202.7826 | 1.5669 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.55 |  | 392.993 | 0.3962 | 398.39 | 393.52 | 0.0684 | watch_only | none |
| AAPL | mega_cap_platform | 332.74 |  | 332.2698 | 0.1415 | 334.98 | 331.295 | 0.027 | watch_only | none |
| GOOGL | cloud_ai_capex | 347.18 |  | 346.1486 | 0.298 | 348.47 | 341.42 | 0.2794 | watch_only | none |
| AMD | ai_accelerator | 502.3 |  | 484.0263 | 3.7754 | 482.43 | 461.04 | 0.4937 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 402.56 |  | 396.9913 | 1.4027 | 394.11 | 386.02 | 0.621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.24 |  | 516.0764 | 2.5507 | 511.83 | 498.665 | 0.085 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 564.17 |  | 553.0539 | 2.01 | 550 | 536.9 | 0.0514 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 375.38 |  | 368.9373 | 1.7463 | 368.42 | 357.97 | 2.5281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 892.375 |  | 857.4378 | 4.0746 | 835.82 | 804.09 | 0.8158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 191.52 |  | 185.5465 | 3.2194 | 185.03 | 178.09 | 0.7049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 399.25 |  | 389.1561 | 2.5938 | 384 | 368.28 | 3.5416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.045 |  | 45.4475 | 1.3146 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.84 |  | 24.1369 | 2.9131 | 24.3 | 23.46 | 0.0403 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.89 |  | 744.8028 | 0.2802 | 742.66 | 740.8 | 0.0013 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.71 |  | 294.0544 | 0.2229 | 294.205 | 291.675 | 0.0204 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 128.23 |  | 125.5119 | 2.1656 | 125.02 | 121.79 | 4.8351 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.185 |  | 71.8117 | 1.9124 | 71.24 | 68.65 | 1.749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 293.81 |  | 284.735 | 3.1872 | 280.565 | 273.17 | 5.1053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.105 |  | 399.1451 | 0.7415 | 389.4 | 382.38 | 3.2131 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 633.44 |  | 627.9933 | 0.8673 | 616.75 | 609.05 | 0.2036 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 1055.25 |  | 1040.6761 | 1.4004 | 1001.82 | 982.21 | 1.013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 473.36 |  | 469.4989 | 0.8224 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.65 |  | 140.7661 | 0.628 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.94 |  | 164.3855 | 2.7706 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 280.86 |  | 272.5503 | 3.0489 | 269.59 | 256.24 | 4.739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 729.34 |  | 708.153 | 2.9919 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 379.03 |  | 375.284 | 0.9982 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 102.62 |  | 99.0425 | 3.612 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 307.875 |  | 302.7434 | 1.695 | 305.21 | 289.97 | 4.7389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1782.605 |  | 1747.3972 | 2.0149 | 1741.99 | 1704.935 | 1.2521 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 545.59 |  | 533.7091 | 2.2261 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 317.02 |  | 311.0014 | 1.9352 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.38 |  | 211.4608 | 1.8534 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TER | semiconductor_test_packaging | 324.36 |  | 315.4676 | 2.8188 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 283.12 |  | 273.9575 | 3.3445 | 265.71 | 258.355 | 3.8994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.66 |  | 61.0202 | 2.6873 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.08 |  | 49.5378 | 3.1132 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.445 |  | 133.6922 | 3.555 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 326.92 |  | 316.898 | 3.1625 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 516.73 |  | 520.9509 | -0.8102 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 297.275 |  | 300.1315 | -0.9518 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.42 |  | 24.91 | 2.0472 | 25.45 | 24.1 | 0.0787 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.25 |  | 33.5694 | 2.0273 | 34 | 32.26 | 0.0292 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.985 |  | 20.5414 | 2.1594 | 20.445 | 19.92 | 0.143 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1466.515 |  | 1420.5491 | 3.2358 | 1393.96 | 1325.48 | 2.0382 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 479.32 |  | 459.5775 | 4.2958 | 453.35 | 431.78 | 0.943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 785.465 |  | 748.9803 | 4.8712 | 724.57 | 702.24 | 2.7143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 249.1 |  | 247.9587 | 0.4603 | 247.72 | 243.725 | 0.0161 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 647.66 |  | 639.1361 | 1.3337 | 649.07 | 638.97 | 2.9645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 269.27 |  | 258.2462 | 4.2687 | 252.95 | 243.21 | 3.7137 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 163.55 |  | 157.5537 | 3.8059 | 151.99 | 145.6 | 0.6726 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
