# Intraday State

- Generated at: `2026-07-18T02:03:18+08:00`
- Market time ET: `2026-07-17T14:03:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 2, 'below_vwap': 5, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.02 |  | 695.3919 | 0.5217 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 526.36 |  | 517.8837 | 1.6367 | 511.83 | 498.665 | 0.0798 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 560.48 |  | 554.7223 | 1.0379 | 550 | 536.9 | 0.0785 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.89 |  | 744.9964 | -0.0143 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.51 |  | 203.2254 | 0.6321 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 560.48 |  | 554.7223 | 1.0379 | 550 | 536.9 | 0.0785 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 526.36 |  | 517.8837 | 1.6367 | 511.83 | 498.665 | 0.0798 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.32 |  | 294.2125 | 0.0365 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.02 |  | 695.3919 | 0.5217 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.4 |  | 45.6121 | 1.7273 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | ONTO | semiconductor_test_packaging | 280.13 |  | 277.4428 | 0.9685 | 265.71 | 258.355 | 0.2713 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.87 |  | 24.2756 | 2.4486 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.955 |  | 72.1455 | 2.5081 | 71.24 | 68.65 | 0.3245 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.6384 | 3.0117 | 20.445 | 19.92 | 0.0941 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.635 |  | 25.0729 | 2.242 | 25.45 | 24.1 | 0.039 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.005 |  | 33.785 | 0.6511 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.5 |  | 67.1721 | 1.9769 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.32 |  | 294.2125 | 0.0365 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 204.51 |  | 203.2254 | 0.6321 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 3 | IREN | high_beta_ai_infrastructure | 34.005 |  | 33.785 | 0.6511 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 332.1 |  | 331.9791 | 0.0364 | 334.98 | 331.295 | 0.009 | watch_only | none |
| 5 | QQQ | market_regime | 699.02 |  | 695.3919 | 0.5217 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 395 |  | 393.2367 | 0.4484 | 398.39 | 393.52 | 0.1392 | watch_only | none |
| 7 | JCI | data_center_power_cooling | 140.99 |  | 140.9653 | 0.0175 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ALAB | ai_networking_optical | 306.13 |  | 305.2946 | 0.2736 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 560.48 |  | 554.7223 | 1.0379 | 550 | 536.9 | 0.0785 | buy_precheck_manual_confirm | none |
| 10 | AMAT | semiconductor_equipment | 536.315 |  | 535.4941 | 0.1533 | 535.095 | 513.34 | 4.3948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ONTO | semiconductor_test_packaging | 280.13 |  | 277.4428 | 0.9685 | 265.71 | 258.355 | 0.2713 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.635 |  | 25.0729 | 2.242 | 25.45 | 24.1 | 0.039 | buy_precheck_manual_confirm | none |
| 13 | LRCX | semiconductor_equipment | 313.12 |  | 312.098 | 0.3274 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TSM | foundry | 399.14 |  | 398.1287 | 0.254 | 394.11 | 386.02 | 2.3801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 380.63 |  | 377.6617 | 0.786 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SOXX | semiconductor_index | 526.36 |  | 517.8837 | 1.6367 | 511.83 | 498.665 | 0.0798 | buy_precheck_manual_confirm | none |
| 17 | HPE | ai_server_oem | 46.4 |  | 45.6121 | 1.7273 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 24.87 |  | 24.2756 | 2.4486 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| 19 | PWR | data_center_power_cooling | 633.58 |  | 629.5417 | 0.6415 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.6384 | 3.0117 | 20.445 | 19.92 | 0.0941 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.51 |  | 203.2254 | 0.6321 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 560.48 |  | 554.7223 | 1.0379 | 550 | 536.9 | 0.0785 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 526.36 |  | 517.8837 | 1.6367 | 511.83 | 498.665 | 0.0798 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.32 |  | 294.2125 | 0.0365 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.02 |  | 695.3919 | 0.5217 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.4 |  | 45.6121 | 1.7273 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | ONTO | semiconductor_test_packaging | 280.13 |  | 277.4428 | 0.9685 | 265.71 | 258.355 | 0.2713 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.87 |  | 24.2756 | 2.4486 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.955 |  | 72.1455 | 2.5081 | 71.24 | 68.65 | 0.3245 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.6384 | 3.0117 | 20.445 | 19.92 | 0.0941 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.635 |  | 25.0729 | 2.242 | 25.45 | 24.1 | 0.039 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.005 |  | 33.785 | 0.6511 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.5 |  | 67.1721 | 1.9769 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| 14 | TT | data_center_power_cooling | 469.585 |  | 469.7779 | -0.0411 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SPY | market_regime | 744.89 |  | 744.9964 | -0.0143 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 16 | ANET | ai_networking_optical | 169.235 |  | 165.9802 | 1.9609 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | TSM | foundry | 399.14 |  | 398.1287 | 0.254 | 394.11 | 386.02 | 2.3801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AVGO | custom_silicon_networking | 374.14 |  | 370.0412 | 1.1077 | 368.42 | 357.97 | 1.5796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 536.315 |  | 535.4941 | 0.1533 | 535.095 | 513.34 | 4.3948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 499.11 |  | 486.441 | 2.6044 | 482.43 | 461.04 | 4.7825 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.02 |  | 695.3919 | 0.5217 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.5 |  | 67.1721 | 1.9769 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.51 |  | 203.2254 | 0.6321 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 395 |  | 393.2367 | 0.4484 | 398.39 | 393.52 | 0.1392 | watch_only | none |
| AAPL | mega_cap_platform | 332.1 |  | 331.9791 | 0.0364 | 334.98 | 331.295 | 0.009 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.32 |  | 345.9894 | -0.4825 | 348.47 | 341.42 | 0.0639 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.11 |  | 486.441 | 2.6044 | 482.43 | 461.04 | 4.7825 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 399.14 |  | 398.1287 | 0.254 | 394.11 | 386.02 | 2.3801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.36 |  | 517.8837 | 1.6367 | 511.83 | 498.665 | 0.0798 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 560.48 |  | 554.7223 | 1.0379 | 550 | 536.9 | 0.0785 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 374.14 |  | 370.0412 | 1.1077 | 368.42 | 357.97 | 1.5796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 882.88 |  | 863.3889 | 2.2575 | 835.82 | 804.09 | 0.8144 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 191.15 |  | 187.0061 | 2.2159 | 185.03 | 178.09 | 0.9992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 402.4 |  | 392.2861 | 2.5782 | 384 | 368.28 | 4.6098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.4 |  | 45.6121 | 1.7273 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.87 |  | 24.2756 | 2.4486 | 24.3 | 23.46 | 0.0402 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.89 |  | 744.9964 | -0.0143 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.32 |  | 294.2125 | 0.0365 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.59 |  | 125.9221 | 1.3245 | 125.02 | 121.79 | 3.5112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.955 |  | 72.1455 | 2.5081 | 71.24 | 68.65 | 0.3245 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 293.8 |  | 286.8986 | 2.4055 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.35 |  | 399.6579 | 0.4234 | 389.4 | 382.38 | 3.7623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 633.58 |  | 629.5417 | 0.6415 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1061.13 |  | 1044.4154 | 1.6004 | 1001.82 | 982.21 | 2.2712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.585 |  | 469.7779 | -0.0411 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.99 |  | 140.9653 | 0.0175 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 169.235 |  | 165.9802 | 1.9609 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 279.93 |  | 273.7871 | 2.2437 | 269.59 | 256.24 | 4.1618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 738.105 |  | 715.3486 | 3.1812 | 694.98 | 653.305 | 0.9985 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 380.63 |  | 377.6617 | 0.786 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.89 |  | 100.4025 | 3.4735 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 306.13 |  | 305.2946 | 0.2736 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1769.1 |  | 1756.1009 | 0.7402 | 1741.99 | 1704.935 | 3.3644 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 536.315 |  | 535.4941 | 0.1533 | 535.095 | 513.34 | 4.3948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 313.12 |  | 312.098 | 0.3274 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.59 |  | 212.1456 | 0.6808 | 210.82 | 204.71 | 2.2988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 325.16 |  | 319.1549 | 1.8816 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.13 |  | 277.4428 | 0.9685 | 265.71 | 258.355 | 0.2713 | buy_precheck_manual_confirm | none |
| AMKR | semiconductor_test_packaging | 62.6 |  | 61.4088 | 1.9398 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.02 |  | 49.8577 | 2.3312 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.54 |  | 134.3022 | 2.4108 | 129.93 | 126.945 | 4.6241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.76 |  | 318.3519 | 2.327 | 315.89 | 307.13 | 4.5524 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.01 |  | 520.2031 | -1.1905 | 526.74 | 522.205 | 0.0428 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.83 |  | 299.3574 | -1.1783 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.635 |  | 25.0729 | 2.242 | 25.45 | 24.1 | 0.039 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.005 |  | 33.785 | 0.6511 | 34 | 32.26 | 0.0294 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 21.26 |  | 20.6384 | 3.0117 | 20.445 | 19.92 | 0.0941 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1439.1 |  | 1428.1525 | 0.7666 | 1393.96 | 1325.48 | 1.4676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 484.43 |  | 466.0479 | 3.9443 | 453.35 | 431.78 | 1.1023 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 784.155 |  | 759.0524 | 3.3071 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.695 |  | 248.0332 | -0.1363 | 247.72 | 243.725 | 0.0444 | below_vwap | below_vwap |
| META | cloud_ai_capex | 649.81 |  | 641.853 | 1.2397 | 649.07 | 638.97 | 2.3376 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 270.31 |  | 260.9821 | 3.5741 | 252.95 | 243.21 | 2.364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 160.355 |  | 158.5298 | 1.1513 | 151.99 | 145.6 | 1.4842 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
