# Intraday State

- Generated at: `2026-07-17T23:19:36+08:00`
- Market time ET: `2026-07-17T11:19:38-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 3, 'watch_only': 2, 'spread_too_wide_or_missing': 29, 'price_stale_or_missing': 1, 'below_vwap': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.3 |  | 693.1832 | 0.1611 | 693.36 | 686.78 | 0.0735 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 515.29 |  | 512.383 | 0.5673 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 552.11 |  | 549.7823 | 0.4234 | 550 | 536.9 | 0.0688 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.51 |  | 744.3839 | 0.0169 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.56 |  | 202.1241 | 0.7104 | 203.41 | 197.98 | 0.0344 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 552.11 |  | 549.7823 | 0.4234 | 550 | 536.9 | 0.0688 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 515.29 |  | 512.383 | 0.5673 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 854.48 |  | 848.5128 | 0.7033 | 835.82 | 804.09 | 0.3289 | buy_precheck_manual_confirm | none |
| 5 | PWR | data_center_power_cooling | 626.205 |  | 623.5537 | 0.4252 | 616.75 | 609.05 | 0.1725 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 694.3 |  | 693.1832 | 0.1611 | 693.36 | 686.78 | 0.0735 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.32 |  | 45.2844 | 0.0786 | 44.92 | 43.715 | 0.0441 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 744.51 |  | 744.3839 | 0.0169 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.855 |  | 247.703 | 0.4651 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.45 |  | 20.3256 | 0.6119 | 20.445 | 19.92 | 0.0978 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.17 |  | 66.6432 | 0.7905 | 66.9 | 64.92 | 0.0298 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 694.3 |  | 693.1832 | 0.1611 | 693.36 | 686.78 | 0.0735 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 744.51 |  | 744.3839 | 0.0169 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 203.56 |  | 202.1241 | 0.7104 | 203.41 | 197.98 | 0.0344 | buy_precheck_manual_confirm | none |
| 4 | HPE | ai_server_oem | 45.32 |  | 45.2844 | 0.0786 | 44.92 | 43.715 | 0.0441 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 552.11 |  | 549.7823 | 0.4234 | 550 | 536.9 | 0.0688 | buy_precheck_manual_confirm | none |
| 6 | SOXX | semiconductor_index | 515.29 |  | 512.383 | 0.5673 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.45 |  | 20.3256 | 0.6119 | 20.445 | 19.92 | 0.0978 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.855 |  | 247.703 | 0.4651 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 346.29 |  | 345.5886 | 0.2029 | 348.47 | 341.42 | 0.2252 | watch_only | none |
| 10 | AAPL | mega_cap_platform | 333.67 |  | 332.2182 | 0.437 | 334.98 | 331.295 | 0.021 | watch_only | none |
| 11 | MU | memory_hbm_storage | 854.48 |  | 848.5128 | 0.7033 | 835.82 | 804.09 | 0.3289 | buy_precheck_manual_confirm | none |
| 12 | PWR | data_center_power_cooling | 626.205 |  | 623.5537 | 0.4252 | 616.75 | 609.05 | 0.1725 | buy_precheck_manual_confirm | none |
| 13 | AVGO | custom_silicon_networking | 368.73 |  | 367.9219 | 0.2196 | 368.42 | 357.97 | 3.051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TT | data_center_power_cooling | 469.75 |  | 468.7431 | 0.2148 | 469.08 | 460.78 | 4.1448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 141.08 |  | 140.3647 | 0.5096 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMAT | semiconductor_equipment | 531 |  | 528.6731 | 0.4401 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | CIEN | ai_networking_optical | 375.19 |  | 373.2 | 0.5332 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 397.02 |  | 395.9442 | 0.2717 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ORCL | cloud_ai_capex | 125.58 |  | 124.8759 | 0.5639 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ASML | semiconductor_equipment | 1744.66 |  | 1736.2677 | 0.4834 | 1741.99 | 1704.935 | 0.7159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.56 |  | 202.1241 | 0.7104 | 203.41 | 197.98 | 0.0344 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 552.11 |  | 549.7823 | 0.4234 | 550 | 536.9 | 0.0688 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 515.29 |  | 512.383 | 0.5673 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 854.48 |  | 848.5128 | 0.7033 | 835.82 | 804.09 | 0.3289 | buy_precheck_manual_confirm | none |
| 5 | PWR | data_center_power_cooling | 626.205 |  | 623.5537 | 0.4252 | 616.75 | 609.05 | 0.1725 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 694.3 |  | 693.1832 | 0.1611 | 693.36 | 686.78 | 0.0735 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.32 |  | 45.2844 | 0.0786 | 44.92 | 43.715 | 0.0441 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 744.51 |  | 744.3839 | 0.0169 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.855 |  | 247.703 | 0.4651 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.45 |  | 20.3256 | 0.6119 | 20.445 | 19.92 | 0.0978 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.17 |  | 66.6432 | 0.7905 | 66.9 | 64.92 | 0.0298 | buy_precheck_manual_confirm | none |
| 12 | SKHY | memory_hbm_storage | 154.65 |  | 154.9776 | -0.2114 | 151.99 | 145.6 | 4.9143 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 164.3 |  | 162.8696 | 0.8783 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TSM | foundry | 396.31 |  | 394.8328 | 0.3741 | 394.11 | 386.02 | 0.6056 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AVGO | custom_silicon_networking | 368.73 |  | 367.9219 | 0.2196 | 368.42 | 357.97 | 3.051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 485.26 |  | 478.3367 | 1.4474 | 482.43 | 461.04 | 1.4631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1744.66 |  | 1736.2677 | 0.4834 | 1741.99 | 1704.935 | 0.7159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 469.75 |  | 468.7431 | 0.2148 | 469.08 | 460.78 | 4.1448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 286.355 |  | 282.4691 | 1.3757 | 280.565 | 273.17 | 3.4747 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | JCI | data_center_power_cooling | 141.08 |  | 140.3647 | 0.5096 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.3 |  | 693.1832 | 0.1611 | 693.36 | 686.78 | 0.0735 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.17 |  | 66.6432 | 0.7905 | 66.9 | 64.92 | 0.0298 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.56 |  | 202.1241 | 0.7104 | 203.41 | 197.98 | 0.0344 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.83 |  | 393.4528 | -0.9208 | 398.39 | 393.52 | 0.0513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.67 |  | 332.2182 | 0.437 | 334.98 | 331.295 | 0.021 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.29 |  | 345.5886 | 0.2029 | 348.47 | 341.42 | 0.2252 | watch_only | none |
| AMD | ai_accelerator | 485.26 |  | 478.3367 | 1.4474 | 482.43 | 461.04 | 1.4631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.31 |  | 394.8328 | 0.3741 | 394.11 | 386.02 | 0.6056 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 515.29 |  | 512.383 | 0.5673 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 552.11 |  | 549.7823 | 0.4234 | 550 | 536.9 | 0.0688 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 368.73 |  | 367.9219 | 0.2196 | 368.42 | 357.97 | 3.051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 854.48 |  | 848.5128 | 0.7033 | 835.82 | 804.09 | 0.3289 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 184.26 |  | 184.4764 | -0.1173 | 185.03 | 178.09 | 1.5684 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 390.35 |  | 386.7384 | 0.9338 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.32 |  | 45.2844 | 0.0786 | 44.92 | 43.715 | 0.0441 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 23.99 |  | 24.0123 | -0.093 | 24.3 | 23.46 | 0.0417 | below_vwap | below_vwap |
| SPY | market_regime | 744.51 |  | 744.3839 | 0.0169 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.84 |  | 294.0863 | -0.0838 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.58 |  | 124.8759 | 0.5639 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 72.53 |  | 71.2736 | 1.7627 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 286.355 |  | 282.4691 | 1.3757 | 280.565 | 273.17 | 3.4747 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 397.02 |  | 395.9442 | 0.2717 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 626.205 |  | 623.5537 | 0.4252 | 616.75 | 609.05 | 0.1725 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 1040.99 |  | 1026.3229 | 1.4291 | 1001.82 | 982.21 | 0.415 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.75 |  | 468.7431 | 0.2148 | 469.08 | 460.78 | 4.1448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.08 |  | 140.3647 | 0.5096 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.3 |  | 162.8696 | 0.8783 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 274.46 |  | 268.6983 | 2.1443 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 718.195 |  | 698.8484 | 2.7684 | 694.98 | 653.305 | 3.9669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.19 |  | 373.2 | 0.5332 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 99.585 |  | 98.0855 | 1.5287 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 298.35 |  | 300.2161 | -0.6216 | 305.21 | 289.97 | 4.0489 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1744.66 |  | 1736.2677 | 0.4834 | 1741.99 | 1704.935 | 0.7159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531 |  | 528.6731 | 0.4401 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 309.61 |  | 307.3005 | 0.7515 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 209.335 |  | 210.2621 | -0.4409 | 210.82 | 204.71 | 2.1879 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 311.08 |  | 309.4415 | 0.5295 | 308.03 | 297.18 | 0.3665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 268.52 |  | 266.8468 | 0.627 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 60.905 |  | 60.2217 | 1.1346 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.14 |  | 48.5874 | 1.1373 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 133.96 |  | 132.7333 | 0.9242 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 317.42 |  | 314.8487 | 0.8167 | 315.89 | 307.13 | 0.7088 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 521.335 |  | 521.8289 | -0.0946 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.175 |  | 301.5427 | -0.122 | 304.36 | 299.62 | 4.3729 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.67 |  | 24.8091 | -0.5608 | 25.45 | 24.1 | 0.0811 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.4 |  | 33.4191 | -0.0572 | 34 | 32.26 | 0.0599 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.45 |  | 20.3256 | 0.6119 | 20.445 | 19.92 | 0.0978 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1412.82 |  | 1401.1668 | 0.8317 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 456.58 |  | 451.9521 | 1.024 | 453.35 | 431.78 | 0.368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 746.565 |  | 735.1175 | 1.5572 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.855 |  | 247.703 | 0.4651 | 247.72 | 243.725 | 0.0281 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 630.1 |  | 636.3747 | -0.986 | 649.07 | 638.97 | 0.4967 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 259.3 |  | 254.8868 | 1.7314 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 154.65 |  | 154.9776 | -0.2114 | 151.99 | 145.6 | 4.9143 | below_vwap | below_vwap,spread_too_wide |
