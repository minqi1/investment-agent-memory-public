# Intraday State

- Generated at: `2026-07-18T02:40:07+08:00`
- Market time ET: `2026-07-17T14:40:08-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'watch_only': 4, 'below_vwap': 13, 'spread_too_wide_or_missing': 27, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.15 |  | 695.5437 | 0.2309 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.92 |  | 518.4369 | 1.0576 | 511.83 | 498.665 | 0.0668 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.71 |  | 555.0927 | 0.4715 | 550 | 536.9 | 0.0628 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.875 |  | 744.9118 | -0.1392 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.71 |  | 555.0927 | 0.4715 | 550 | 536.9 | 0.0628 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.92 |  | 518.4369 | 1.0576 | 511.83 | 498.665 | 0.0668 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.59 |  | 212.1997 | 0.6552 | 210.82 | 204.71 | 0.117 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 872.46 |  | 864.2675 | 0.9479 | 835.82 | 804.09 | 0.3152 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.15 |  | 695.5437 | 0.2309 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.285 |  | 45.6636 | 1.3608 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.6 |  | 24.3084 | 1.1996 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 21.03 |  | 20.6608 | 1.7871 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.99 |  | 67.2086 | 1.1627 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.15 |  | 695.5437 | 0.2309 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 557.71 |  | 555.0927 | 0.4715 | 550 | 536.9 | 0.0628 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 203.4 |  | 203.2438 | 0.0768 | 203.41 | 197.98 | 0.3343 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 394.42 |  | 393.3844 | 0.2632 | 398.39 | 393.52 | 0.0482 | watch_only | none |
| 5 | KLAC | semiconductor_equipment | 213.59 |  | 212.1997 | 0.6552 | 210.82 | 204.71 | 0.117 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 332.46 |  | 332.0039 | 0.1374 | 334.98 | 331.295 | 0.009 | watch_only | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.245 |  | 25.0904 | 0.6162 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.6 |  | 24.3084 | 1.1996 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 9 | SOXX | semiconductor_index | 523.92 |  | 518.4369 | 1.0576 | 511.83 | 498.665 | 0.0668 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.285 |  | 45.6636 | 1.3608 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 11 | MU | memory_hbm_storage | 872.46 |  | 864.2675 | 0.9479 | 835.82 | 804.09 | 0.3152 | buy_precheck_manual_confirm | none |
| 12 | ASML | semiconductor_equipment | 1768.07 |  | 1756.978 | 0.6313 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 634.39 |  | 630.0575 | 0.6876 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | CORZ | high_beta_ai_infrastructure | 21.03 |  | 20.6608 | 1.7871 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| 15 | LRCX | semiconductor_equipment | 312.955 |  | 312.1229 | 0.2666 | 306.51 | 298.89 | 4.2338 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ONTO | semiconductor_test_packaging | 278.75 |  | 277.6443 | 0.3982 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 372.84 |  | 370.231 | 0.7047 | 368.42 | 357.97 | 1.9284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ORCL | cloud_ai_capex | 126.785 |  | 126.024 | 0.6039 | 125.02 | 121.79 | 1.1516 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SPY | market_regime | 743.875 |  | 744.9118 | -0.1392 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 20 | ETN | data_center_power_cooling | 401.2 |  | 399.7662 | 0.3587 | 389.4 | 382.38 | 2.9337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.71 |  | 555.0927 | 0.4715 | 550 | 536.9 | 0.0628 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.92 |  | 518.4369 | 1.0576 | 511.83 | 498.665 | 0.0668 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.59 |  | 212.1997 | 0.6552 | 210.82 | 204.71 | 0.117 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 872.46 |  | 864.2675 | 0.9479 | 835.82 | 804.09 | 0.3152 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.15 |  | 695.5437 | 0.2309 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.285 |  | 45.6636 | 1.3608 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.6 |  | 24.3084 | 1.1996 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 21.03 |  | 20.6608 | 1.7871 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.99 |  | 67.2086 | 1.1627 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 10 | TSM | foundry | 397.84 |  | 398.0938 | -0.0638 | 394.11 | 386.02 | 0.7164 | below_vwap | below_vwap,spread_too_wide |
| 11 | TT | data_center_power_cooling | 469.74 |  | 469.7851 | -0.0096 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 140.835 |  | 140.9586 | -0.0877 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | CIEN | ai_networking_optical | 376.85 |  | 377.8464 | -0.2637 | 375.52 | 359.81 | 1.1729 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 743.875 |  | 744.9118 | -0.1392 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1415.7 |  | 1428.2081 | -0.8758 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ANET | ai_networking_optical | 168.63 |  | 166.1455 | 1.4954 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 372.84 |  | 370.231 | 0.7047 | 368.42 | 357.97 | 1.9284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 496.255 |  | 486.758 | 1.9511 | 482.43 | 461.04 | 3.3934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1768.07 |  | 1756.978 | 0.6313 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | VRT | data_center_power_cooling | 292.27 |  | 287.2975 | 1.7308 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.15 |  | 695.5437 | 0.2309 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.99 |  | 67.2086 | 1.1627 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.4 |  | 203.2438 | 0.0768 | 203.41 | 197.98 | 0.3343 | watch_only | none |
| MSFT | cloud_ai_capex | 394.42 |  | 393.3844 | 0.2632 | 398.39 | 393.52 | 0.0482 | watch_only | none |
| AAPL | mega_cap_platform | 332.46 |  | 332.0039 | 0.1374 | 334.98 | 331.295 | 0.009 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.27 |  | 345.837 | -0.1639 | 348.47 | 341.42 | 0.5097 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496.255 |  | 486.758 | 1.9511 | 482.43 | 461.04 | 3.3934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 397.84 |  | 398.0938 | -0.0638 | 394.11 | 386.02 | 0.7164 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.92 |  | 518.4369 | 1.0576 | 511.83 | 498.665 | 0.0668 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.71 |  | 555.0927 | 0.4715 | 550 | 536.9 | 0.0628 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.84 |  | 370.231 | 0.7047 | 368.42 | 357.97 | 1.9284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 872.46 |  | 864.2675 | 0.9479 | 835.82 | 804.09 | 0.3152 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 189.41 |  | 187.1552 | 1.2048 | 185.03 | 178.09 | 0.623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.22 |  | 392.9811 | 2.0965 | 384 | 368.28 | 4.9499 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.285 |  | 45.6636 | 1.3608 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.6 |  | 24.3084 | 1.1996 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.875 |  | 744.9118 | -0.1392 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.71 |  | 294.1791 | -0.1595 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.785 |  | 126.024 | 0.6039 | 125.02 | 121.79 | 1.1516 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.61 |  | 72.2146 | 1.9323 | 71.24 | 68.65 | 2.9344 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.27 |  | 287.2975 | 1.7308 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.2 |  | 399.7662 | 0.3587 | 389.4 | 382.38 | 2.9337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 634.39 |  | 630.0575 | 0.6876 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1056.77 |  | 1045.0376 | 1.1227 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.74 |  | 469.7851 | -0.0096 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.835 |  | 140.9586 | -0.0877 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.63 |  | 166.1455 | 1.4954 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.08 |  | 274.0044 | 1.4874 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 733.31 |  | 717.7084 | 2.1738 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 376.85 |  | 377.8464 | -0.2637 | 375.52 | 359.81 | 1.1729 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.56 |  | 100.5351 | 2.0141 | 97.585 | 91.92 | 4.1049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 303.18 |  | 305.2113 | -0.6655 | 305.21 | 289.97 | 4.7859 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1768.07 |  | 1756.978 | 0.6313 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 534.54 |  | 535.268 | -0.136 | 535.095 | 513.34 | 0.1459 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 312.955 |  | 312.1229 | 0.2666 | 306.51 | 298.89 | 4.2338 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 213.59 |  | 212.1997 | 0.6552 | 210.82 | 204.71 | 0.117 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.405 |  | 319.9648 | 1.3877 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.75 |  | 277.6443 | 0.3982 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.39 |  | 61.5037 | 1.441 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.98 |  | 49.8958 | 2.173 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.55 |  | 134.8006 | 2.0396 | 129.93 | 126.945 | 0.4871 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 324.35 |  | 318.7773 | 1.7482 | 315.89 | 307.13 | 4.0974 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.38 |  | 519.8909 | -0.8677 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.5 |  | 298.9521 | -0.8202 | 304.36 | 299.62 | 3.9191 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.245 |  | 25.0904 | 0.6162 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.73 |  | 33.794 | -0.1895 | 34 | 32.26 | 0.0296 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.03 |  | 20.6608 | 1.7871 | 20.445 | 19.92 | 0.0476 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1415.7 |  | 1428.2081 | -0.8758 | 1393.96 | 1325.48 |  | below_vwap | below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 482.25 |  | 467.0985 | 3.2437 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 787.87 |  | 760.6582 | 3.5774 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.66 |  | 248.0055 | -0.1393 | 247.72 | 243.725 | 0.0323 | below_vwap | below_vwap |
| META | cloud_ai_capex | 647.75 |  | 642.3648 | 0.8383 | 649.07 | 638.97 | 0.7719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.17 |  | 261.1389 | 2.6925 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 161.79 |  | 158.7958 | 1.8856 | 151.99 | 145.6 | 2.4723 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
