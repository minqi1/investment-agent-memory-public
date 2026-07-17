# Intraday State

- Generated at: `2026-07-18T02:15:30+08:00`
- Market time ET: `2026-07-17T14:15:31-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'watch_only': 4, 'below_vwap': 8, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.83 |  | 695.4396 | 0.3437 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.87 |  | 518.1362 | 1.1066 | 511.83 | 498.665 | 0.084 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.33 |  | 554.8759 | 0.6225 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.11 |  | 744.9818 | -0.117 | 742.66 | 740.8 | 0.0336 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.64 |  | 203.2392 | 0.1972 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.33 |  | 554.8759 | 0.6225 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 523.87 |  | 518.1362 | 1.1066 | 511.83 | 498.665 | 0.084 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1059.51 |  | 1044.6505 | 1.4224 | 1001.82 | 982.21 | 0.2086 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.83 |  | 695.4396 | 0.3437 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.24 |  | 45.6351 | 1.3254 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 127.25 |  | 125.9781 | 1.0096 | 125.02 | 121.79 | 0.1179 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.76 |  | 24.2853 | 1.9545 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.11 |  | 20.6455 | 2.2499 | 20.445 | 19.92 | 0.0474 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.25 |  | 67.1805 | 1.592 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.64 |  | 203.2392 | 0.1972 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 697.83 |  | 695.4396 | 0.3437 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332.605 |  | 331.9963 | 0.1833 | 334.98 | 331.295 | 0.012 | watch_only | none |
| 4 | SMH | semiconductor_index | 558.33 |  | 554.8759 | 0.6225 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 395.935 |  | 393.2796 | 0.6752 | 398.39 | 393.52 | 0.0429 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.985 |  | 33.7917 | 0.5721 | 34 | 32.26 | 0.0294 | watch_only | none |
| 7 | TT | data_center_power_cooling | 470.53 |  | 469.7903 | 0.1575 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 141.1 |  | 140.97 | 0.0922 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SOXX | semiconductor_index | 523.87 |  | 518.1362 | 1.1066 | 511.83 | 498.665 | 0.084 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.24 |  | 45.6351 | 1.3254 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 212.73 |  | 212.1699 | 0.264 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ORCL | cloud_ai_capex | 127.25 |  | 125.9781 | 1.0096 | 125.02 | 121.79 | 0.1179 | buy_precheck_manual_confirm | none |
| 13 | GEV | data_center_power_cooling | 1059.51 |  | 1044.6505 | 1.4224 | 1001.82 | 982.21 | 0.2086 | buy_precheck_manual_confirm | none |
| 14 | APLD | high_beta_ai_infrastructure | 25.38 |  | 25.0799 | 1.1965 | 25.45 | 24.1 | 0.1182 | watch_only | none |
| 15 | TSM | foundry | 398.145 |  | 398.138 | 0.0018 | 394.11 | 386.02 | 0.8866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | CIEN | ai_networking_optical | 379.17 |  | 377.8431 | 0.3512 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SMCI | ai_server_oem | 24.76 |  | 24.2853 | 1.9545 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 18 | ETN | data_center_power_cooling | 400.9 |  | 399.7163 | 0.2961 | 389.4 | 382.38 | 2.8885 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 633.92 |  | 629.6477 | 0.6785 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 21.11 |  | 20.6455 | 2.2499 | 20.445 | 19.92 | 0.0474 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.64 |  | 203.2392 | 0.1972 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.33 |  | 554.8759 | 0.6225 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 523.87 |  | 518.1362 | 1.1066 | 511.83 | 498.665 | 0.084 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1059.51 |  | 1044.6505 | 1.4224 | 1001.82 | 982.21 | 0.2086 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.83 |  | 695.4396 | 0.3437 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.24 |  | 45.6351 | 1.3254 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 127.25 |  | 125.9781 | 1.0096 | 125.02 | 121.79 | 0.1179 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.76 |  | 24.2853 | 1.9545 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.11 |  | 20.6455 | 2.2499 | 20.445 | 19.92 | 0.0474 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 68.25 |  | 67.1805 | 1.592 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| 11 | LRCX | semiconductor_equipment | 312.07 |  | 312.1022 | -0.0103 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | SPY | market_regime | 744.11 |  | 744.9818 | -0.117 | 742.66 | 740.8 | 0.0336 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 168.965 |  | 166.0394 | 1.762 | 163.275 | 157.34 | 2.6514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 398.145 |  | 398.138 | 0.0018 | 394.11 | 386.02 | 0.8866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AVGO | custom_silicon_networking | 372.96 |  | 370.1318 | 0.7641 | 368.42 | 357.97 | 2.145 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 497.36 |  | 486.6012 | 2.211 | 482.43 | 461.04 | 3.4321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1766.07 |  | 1756.4775 | 0.5461 | 1741.99 | 1704.935 | 3.2966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 470.53 |  | 469.7903 | 0.1575 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | KLAC | semiconductor_equipment | 212.73 |  | 212.1699 | 0.264 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 875.33 |  | 863.7349 | 1.3424 | 835.82 | 804.09 | 2.0278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.83 |  | 695.4396 | 0.3437 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.25 |  | 67.1805 | 1.592 | 66.9 | 64.92 | 0.0147 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.64 |  | 203.2392 | 0.1972 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 395.935 |  | 393.2796 | 0.6752 | 398.39 | 393.52 | 0.0429 | watch_only | none |
| AAPL | mega_cap_platform | 332.605 |  | 331.9963 | 0.1833 | 334.98 | 331.295 | 0.012 | watch_only | none |
| GOOGL | cloud_ai_capex | 343.01 |  | 345.9193 | -0.841 | 348.47 | 341.42 | 0.1312 | below_vwap | below_vwap |
| AMD | ai_accelerator | 497.36 |  | 486.6012 | 2.211 | 482.43 | 461.04 | 3.4321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.145 |  | 398.138 | 0.0018 | 394.11 | 386.02 | 0.8866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.87 |  | 518.1362 | 1.1066 | 511.83 | 498.665 | 0.084 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.33 |  | 554.8759 | 0.6225 | 550 | 536.9 | 0.0394 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.96 |  | 370.1318 | 0.7641 | 368.42 | 357.97 | 2.145 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 875.33 |  | 863.7349 | 1.3424 | 835.82 | 804.09 | 2.0278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.7 |  | 187.0757 | 1.4028 | 185.03 | 178.09 | 0.485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.33 |  | 392.5403 | 2.2392 | 384 | 368.28 | 0.4385 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.24 |  | 45.6351 | 1.3254 | 44.92 | 43.715 | 0.0433 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.76 |  | 24.2853 | 1.9545 | 24.3 | 23.46 | 0.0404 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.11 |  | 744.9818 | -0.117 | 742.66 | 740.8 | 0.0336 | below_vwap | below_vwap |
| IWM | market_regime | 293.95 |  | 294.2104 | -0.0885 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 127.25 |  | 125.9781 | 1.0096 | 125.02 | 121.79 | 0.1179 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.695 |  | 72.1704 | 2.1125 | 71.24 | 68.65 | 3.6502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.46 |  | 287.0251 | 1.8935 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.9 |  | 399.7163 | 0.2961 | 389.4 | 382.38 | 2.8885 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 633.92 |  | 629.6477 | 0.6785 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1059.51 |  | 1044.6505 | 1.4224 | 1001.82 | 982.21 | 0.2086 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 470.53 |  | 469.7903 | 0.1575 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.1 |  | 140.97 | 0.0922 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.965 |  | 166.0394 | 1.762 | 163.275 | 157.34 | 2.6514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 279.24 |  | 273.8768 | 1.9583 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 738.455 |  | 716.1674 | 3.1121 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 379.17 |  | 377.8431 | 0.3512 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.41 |  | 100.451 | 2.9457 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 303.75 |  | 305.2933 | -0.5055 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1766.07 |  | 1756.4775 | 0.5461 | 1741.99 | 1704.935 | 3.2966 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 534.01 |  | 535.4843 | -0.2753 | 535.095 | 513.34 | 3.6366 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 312.07 |  | 312.1022 | -0.0103 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.73 |  | 212.1699 | 0.264 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TER | semiconductor_test_packaging | 323.92 |  | 319.5034 | 1.3823 | 308.03 | 297.18 | 4.5412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 278.61 |  | 277.5488 | 0.3823 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.54 |  | 61.4429 | 1.7856 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.97 |  | 49.8667 | 2.2125 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.33 |  | 134.3968 | 2.1825 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.025 |  | 318.5903 | 2.0197 | 315.89 | 307.13 | 4.5043 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.75 |  | 520.0785 | -1.0246 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.96 |  | 299.2526 | -1.1003 | 304.36 | 299.62 | 4.112 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.38 |  | 25.0799 | 1.1965 | 25.45 | 24.1 | 0.1182 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.985 |  | 33.7917 | 0.5721 | 34 | 32.26 | 0.0294 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.11 |  | 20.6455 | 2.2499 | 20.445 | 19.92 | 0.0474 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1431.88 |  | 1428.3421 | 0.2477 | 1393.96 | 1325.48 | 2.4346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 481.09 |  | 466.5035 | 3.1268 | 453.35 | 431.78 | 0.6381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 786.52 |  | 759.5529 | 3.5504 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.27 |  | 248.0191 | -0.302 | 247.72 | 243.725 | 0.0202 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.07 |  | 642.0444 | 0.7828 | 649.07 | 638.97 | 1.2023 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 269.135 |  | 261.021 | 3.1086 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 159.655 |  | 158.5805 | 0.6776 | 151.99 | 145.6 | 0.5387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
