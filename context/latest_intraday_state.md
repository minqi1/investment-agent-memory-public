# Intraday State

- Generated at: `2026-07-18T03:40:42+08:00`
- Market time ET: `2026-07-17T15:40:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'manual_confirm_candidate': 11, 'watch_only': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 20, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.42 |  | 695.6525 | -0.0334 | 693.36 | 686.78 | 0.0187 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 521.6 |  | 518.9329 | 0.514 | 511.83 | 498.665 | 0.0844 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.84 |  | 555.2341 | 0.1091 | 550 | 536.9 | 0.072 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.81 |  | 744.5839 | -0.2382 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 168.22 |  | 166.4419 | 1.0683 | 163.275 | 157.34 | 0.1367 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 555.84 |  | 555.2341 | 0.1091 | 550 | 536.9 | 0.072 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 494.325 |  | 487.3526 | 1.4307 | 482.43 | 461.04 | 0.1537 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 521.6 |  | 518.9329 | 0.514 | 511.83 | 498.665 | 0.0844 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 212.64 |  | 212.2538 | 0.182 | 210.82 | 204.71 | 0.0705 | buy_precheck_manual_confirm | none |
| 6 | PWR | data_center_power_cooling | 631.16 |  | 630.3198 | 0.1333 | 616.75 | 609.05 | 0.1537 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.89 |  | 45.7186 | 0.375 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 8 | WDC | memory_hbm_storage | 480.155 |  | 468.1381 | 2.567 | 453.35 | 431.78 | 0.2728 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.45 |  | 24.3267 | 0.507 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.745 |  | 20.6867 | 0.2818 | 20.445 | 19.92 | 0.0964 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.515 |  | 67.2673 | 0.3682 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 555.84 |  | 555.2341 | 0.1091 | 550 | 536.9 | 0.072 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 212.64 |  | 212.2538 | 0.182 | 210.82 | 204.71 | 0.0705 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 20.745 |  | 20.6867 | 0.2818 | 20.445 | 19.92 | 0.0964 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.45 |  | 24.3267 | 0.507 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 333.43 |  | 332.3468 | 0.3259 | 334.98 | 331.295 | 0.009 | watch_only | none |
| 6 | PWR | data_center_power_cooling | 631.16 |  | 630.3198 | 0.1333 | 616.75 | 609.05 | 0.1537 | buy_precheck_manual_confirm | none |
| 7 | SOXX | semiconductor_index | 521.6 |  | 518.9329 | 0.514 | 511.83 | 498.665 | 0.0844 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.89 |  | 45.7186 | 0.375 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | MSFT | cloud_ai_capex | 395.14 |  | 393.6992 | 0.366 | 398.39 | 393.52 | 0.0202 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 25.285 |  | 25.1142 | 0.6803 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| 11 | TT | data_center_power_cooling | 470.535 |  | 469.735 | 0.1703 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ANET | ai_networking_optical | 168.22 |  | 166.4419 | 1.0683 | 163.275 | 157.34 | 0.1367 | buy_precheck_manual_confirm | none |
| 13 | AMD | ai_accelerator | 494.325 |  | 487.3526 | 1.4307 | 482.43 | 461.04 | 0.1537 | buy_precheck_manual_confirm | none |
| 14 | LRCX | semiconductor_equipment | 312.12 |  | 312.0677 | 0.0167 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 371.695 |  | 370.4783 | 0.3284 | 368.42 | 357.97 | 2.311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ORCL | cloud_ai_capex | 126.275 |  | 126.0599 | 0.1706 | 125.02 | 121.79 | 1.9402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ETN | data_center_power_cooling | 400.89 |  | 399.7552 | 0.2839 | 389.4 | 382.38 | 3.1505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 322.095 |  | 320.5409 | 0.4848 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 480.155 |  | 468.1381 | 2.567 | 453.35 | 431.78 | 0.2728 | buy_precheck_manual_confirm | none |
| 20 | AMKR | semiconductor_test_packaging | 62.13 |  | 61.6642 | 0.7554 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 168.22 |  | 166.4419 | 1.0683 | 163.275 | 157.34 | 0.1367 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 555.84 |  | 555.2341 | 0.1091 | 550 | 536.9 | 0.072 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 494.325 |  | 487.3526 | 1.4307 | 482.43 | 461.04 | 0.1537 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 521.6 |  | 518.9329 | 0.514 | 511.83 | 498.665 | 0.0844 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 212.64 |  | 212.2538 | 0.182 | 210.82 | 204.71 | 0.0705 | buy_precheck_manual_confirm | none |
| 6 | PWR | data_center_power_cooling | 631.16 |  | 630.3198 | 0.1333 | 616.75 | 609.05 | 0.1537 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.89 |  | 45.7186 | 0.375 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 8 | WDC | memory_hbm_storage | 480.155 |  | 468.1381 | 2.567 | 453.35 | 431.78 | 0.2728 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.45 |  | 24.3267 | 0.507 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.745 |  | 20.6867 | 0.2818 | 20.445 | 19.92 | 0.0964 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.515 |  | 67.2673 | 0.3682 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |
| 12 | TSM | foundry | 396.86 |  | 397.837 | -0.2456 | 394.11 | 386.02 | 0.6501 | below_vwap | below_vwap,spread_too_wide |
| 13 | ASML | semiconductor_equipment | 1754.31 |  | 1756.8668 | -0.1455 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | MU | memory_hbm_storage | 861.56 |  | 864.5897 | -0.3504 | 835.82 | 804.09 | 0.8856 | below_vwap | below_vwap,spread_too_wide |
| 15 | CIEN | ai_networking_optical | 375.92 |  | 377.5971 | -0.4442 | 375.52 | 359.81 | 4.3493 | below_vwap | below_vwap,spread_too_wide |
| 16 | QQQ | market_regime | 695.42 |  | 695.6525 | -0.0334 | 693.36 | 686.78 | 0.0187 | below_vwap | below_vwap |
| 17 | SPY | market_regime | 742.81 |  | 744.5839 | -0.2382 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 18 | ONTO | semiconductor_test_packaging | 276.555 |  | 277.6751 | -0.4034 | 265.71 | 258.355 | 0.3688 | below_vwap | below_vwap,spread_too_wide |
| 19 | SKHY | memory_hbm_storage | 153.805 |  | 158.6516 | -3.0548 | 151.99 | 145.6 | 0.4616 | below_vwap | below_vwap,spread_too_wide |
| 20 | AVGO | custom_silicon_networking | 371.695 |  | 370.4783 | 0.3284 | 368.42 | 357.97 | 2.311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.42 |  | 695.6525 | -0.0334 | 693.36 | 686.78 | 0.0187 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.515 |  | 67.2673 | 0.3682 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.615 |  | 203.173 | -0.2746 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 395.14 |  | 393.6992 | 0.366 | 398.39 | 393.52 | 0.0202 | watch_only | none |
| AAPL | mega_cap_platform | 333.43 |  | 332.3468 | 0.3259 | 334.98 | 331.295 | 0.009 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.27 |  | 345.7167 | -0.4185 | 348.47 | 341.42 | 0.7349 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 494.325 |  | 487.3526 | 1.4307 | 482.43 | 461.04 | 0.1537 | buy_precheck_manual_confirm | none |
| TSM | foundry | 396.86 |  | 397.837 | -0.2456 | 394.11 | 386.02 | 0.6501 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 521.6 |  | 518.9329 | 0.514 | 511.83 | 498.665 | 0.0844 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.84 |  | 555.2341 | 0.1091 | 550 | 536.9 | 0.072 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.695 |  | 370.4783 | 0.3284 | 368.42 | 357.97 | 2.311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 861.56 |  | 864.5897 | -0.3504 | 835.82 | 804.09 | 0.8856 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.305 |  | 187.3025 | 0.5352 | 185.03 | 178.09 | 1.2374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 398.985 |  | 393.8184 | 1.3119 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.89 |  | 45.7186 | 0.375 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.45 |  | 24.3267 | 0.507 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.81 |  | 744.5839 | -0.2382 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.54 |  | 294.0789 | -0.1833 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.275 |  | 126.0599 | 0.1706 | 125.02 | 121.79 | 1.9402 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.155 |  | 72.3174 | 1.1582 | 71.24 | 68.65 | 4.511 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.795 |  | 287.7883 | 1.0448 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.89 |  | 399.7552 | 0.2839 | 389.4 | 382.38 | 3.1505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 631.16 |  | 630.3198 | 0.1333 | 616.75 | 609.05 | 0.1537 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 1054.365 |  | 1046.565 | 0.7453 | 1001.82 | 982.21 | 0.6326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.535 |  | 469.735 | 0.1703 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.72 |  | 140.9029 | -0.1298 | 140.765 | 137.165 | 0.1066 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 168.22 |  | 166.4419 | 1.0683 | 163.275 | 157.34 | 0.1367 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 278.445 |  | 274.4798 | 1.4446 | 269.59 | 256.24 | 3.7458 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 736.51 |  | 720.0011 | 2.2929 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 375.92 |  | 377.5971 | -0.4442 | 375.52 | 359.81 | 4.3493 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.34 |  | 100.7595 | 1.5686 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 303.74 |  | 304.6425 | -0.2962 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1754.31 |  | 1756.8668 | -0.1455 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 529.4 |  | 533.7689 | -0.8185 | 535.095 | 513.34 | 0.8179 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 312.12 |  | 312.0677 | 0.0167 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 212.64 |  | 212.2538 | 0.182 | 210.82 | 204.71 | 0.0705 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 322.095 |  | 320.5409 | 0.4848 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 276.555 |  | 277.6751 | -0.4034 | 265.71 | 258.355 | 0.3688 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.13 |  | 61.6642 | 0.7554 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.96 |  | 50.0435 | 1.8314 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.91 |  | 135.2707 | 1.2119 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.815 |  | 319.4214 | 2.0016 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 513.085 |  | 518.0148 | -0.9517 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.635 |  | 298.3987 | -0.9262 | 304.36 | 299.62 | 4.1842 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.285 |  | 25.1142 | 0.6803 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.27 |  | 33.7377 | -1.3864 | 34 | 32.26 | 0.0301 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.745 |  | 20.6867 | 0.2818 | 20.445 | 19.92 | 0.0964 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1388.86 |  | 1426.2413 | -2.621 | 1393.96 | 1325.48 | 2.6201 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.155 |  | 468.1381 | 2.567 | 453.35 | 431.78 | 0.2728 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 792.12 |  | 767.4677 | 3.2122 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 246.85 |  | 247.9264 | -0.4342 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 642.23 |  | 642.62 | -0.0607 | 649.07 | 638.97 | 2.0382 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 266.48 |  | 261.7227 | 1.8177 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 153.805 |  | 158.6516 | -3.0548 | 151.99 | 145.6 | 0.4616 | below_vwap | below_vwap,spread_too_wide |
