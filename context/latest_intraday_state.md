# Intraday State

- Generated at: `2026-07-18T03:44:44+08:00`
- Market time ET: `2026-07-17T15:44:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'watch_only': 4, 'below_vwap': 13, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.07 |  | 695.6526 | 0.06 | 693.36 | 686.78 | 0.0101 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.11 |  | 518.9865 | 0.7945 | 511.83 | 498.665 | 0.0688 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.4 |  | 555.2459 | 0.388 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.42 |  | 744.5449 | -0.1511 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 398 |  | 397.8318 | 0.0423 | 394.11 | 386.02 | 0.3291 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 557.4 |  | 555.2459 | 0.388 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 523.11 |  | 518.9865 | 0.7945 | 511.83 | 498.665 | 0.0688 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 470.67 |  | 469.7496 | 0.1959 | 469.08 | 460.78 | 0.1105 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.07 |  | 695.6526 | 0.06 | 693.36 | 686.78 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.955 |  | 45.7208 | 0.5122 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 188.78 |  | 187.3133 | 0.783 | 185.03 | 178.09 | 0.2755 | buy_precheck_manual_confirm | none |
| 8 | COHR | ai_networking_optical | 277.85 |  | 274.6035 | 1.1822 | 269.59 | 256.24 | 0.18 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.49 |  | 24.3277 | 0.6671 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.6877 | 0.4462 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.69 |  | 67.27 | 0.6243 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 470.67 |  | 469.7496 | 0.1959 | 469.08 | 460.78 | 0.1105 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 696.07 |  | 695.6526 | 0.06 | 693.36 | 686.78 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 398 |  | 397.8318 | 0.0423 | 394.11 | 386.02 | 0.3291 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 203.205 |  | 203.1701 | 0.0172 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| 5 | SMH | semiconductor_index | 557.4 |  | 555.2459 | 0.388 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.49 |  | 24.3277 | 0.6671 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 394.91 |  | 393.7141 | 0.3037 | 398.39 | 393.52 | 0.2659 | watch_only | none |
| 8 | SOXX | semiconductor_index | 523.11 |  | 518.9865 | 0.7945 | 511.83 | 498.665 | 0.0688 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 45.955 |  | 45.7208 | 0.5122 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 333.62 |  | 332.3723 | 0.3754 | 334.98 | 331.295 | 0.018 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.6877 | 0.4462 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.315 |  | 25.1156 | 0.7938 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| 13 | MRVL | custom_silicon_networking | 188.78 |  | 187.3133 | 0.783 | 185.03 | 178.09 | 0.2755 | buy_precheck_manual_confirm | none |
| 14 | CIEN | ai_networking_optical | 377.71 |  | 377.5865 | 0.0327 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | COHR | ai_networking_optical | 277.85 |  | 274.6035 | 1.1822 | 269.59 | 256.24 | 0.18 | buy_precheck_manual_confirm | none |
| 16 | ETN | data_center_power_cooling | 401.04 |  | 399.7679 | 0.3182 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 631.98 |  | 630.3285 | 0.262 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 313.13 |  | 312.0724 | 0.3389 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | META | cloud_ai_capex | 643.085 |  | 642.6206 | 0.0723 | 649.07 | 638.97 | 1.6281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1759.8 |  | 1756.8801 | 0.1662 | 1741.99 | 1704.935 | 4.6806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 398 |  | 397.8318 | 0.0423 | 394.11 | 386.02 | 0.3291 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 557.4 |  | 555.2459 | 0.388 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 523.11 |  | 518.9865 | 0.7945 | 511.83 | 498.665 | 0.0688 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 470.67 |  | 469.7496 | 0.1959 | 469.08 | 460.78 | 0.1105 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.07 |  | 695.6526 | 0.06 | 693.36 | 686.78 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 45.955 |  | 45.7208 | 0.5122 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 188.78 |  | 187.3133 | 0.783 | 185.03 | 178.09 | 0.2755 | buy_precheck_manual_confirm | none |
| 8 | COHR | ai_networking_optical | 277.85 |  | 274.6035 | 1.1822 | 269.59 | 256.24 | 0.18 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.49 |  | 24.3277 | 0.6671 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.6877 | 0.4462 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.69 |  | 67.27 | 0.6243 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 12 | MU | memory_hbm_storage | 861.89 |  | 864.5514 | -0.3078 | 835.82 | 804.09 | 0.362 | below_vwap | below_vwap,spread_too_wide |
| 13 | JCI | data_center_power_cooling | 140.8 |  | 140.9005 | -0.0713 | 140.765 | 137.165 | 4.8509 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 743.42 |  | 744.5449 | -0.1511 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 15 | ONTO | semiconductor_test_packaging | 277.22 |  | 277.6695 | -0.1619 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | SKHY | memory_hbm_storage | 153.52 |  | 158.628 | -3.2201 | 151.99 | 145.6 | 0.6188 | below_vwap | below_vwap,spread_too_wide |
| 17 | ANET | ai_networking_optical | 168.37 |  | 166.4643 | 1.1448 | 163.275 | 157.34 | 2.9637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AVGO | custom_silicon_networking | 372.27 |  | 370.4983 | 0.4782 | 368.42 | 357.97 | 2.0603 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 494.7 |  | 487.4137 | 1.4949 | 482.43 | 461.04 | 0.853 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1759.8 |  | 1756.8801 | 0.1662 | 1741.99 | 1704.935 | 4.6806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.07 |  | 695.6526 | 0.06 | 693.36 | 686.78 | 0.0101 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.69 |  | 67.27 | 0.6243 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.205 |  | 203.1701 | 0.0172 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| MSFT | cloud_ai_capex | 394.91 |  | 393.7141 | 0.3037 | 398.39 | 393.52 | 0.2659 | watch_only | none |
| AAPL | mega_cap_platform | 333.62 |  | 332.3723 | 0.3754 | 334.98 | 331.295 | 0.018 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.94 |  | 345.7049 | -0.2213 | 348.47 | 341.42 | 0.0348 | below_vwap | below_vwap |
| AMD | ai_accelerator | 494.7 |  | 487.4137 | 1.4949 | 482.43 | 461.04 | 0.853 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398 |  | 397.8318 | 0.0423 | 394.11 | 386.02 | 0.3291 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.11 |  | 518.9865 | 0.7945 | 511.83 | 498.665 | 0.0688 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.4 |  | 555.2459 | 0.388 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.27 |  | 370.4983 | 0.4782 | 368.42 | 357.97 | 2.0603 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 861.89 |  | 864.5514 | -0.3078 | 835.82 | 804.09 | 0.362 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.78 |  | 187.3133 | 0.783 | 185.03 | 178.09 | 0.2755 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 399.345 |  | 393.8773 | 1.3882 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.955 |  | 45.7208 | 0.5122 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.49 |  | 24.3277 | 0.6671 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.42 |  | 744.5449 | -0.1511 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.79 |  | 294.0751 | -0.097 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.6 |  | 126.0706 | 0.4199 | 125.02 | 121.79 | 2.2907 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.15 |  | 72.3262 | 1.1389 | 71.24 | 68.65 | 1.6541 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.795 |  | 287.8434 | 1.0254 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.04 |  | 399.7679 | 0.3182 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 631.98 |  | 630.3285 | 0.262 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1054.2 |  | 1046.7616 | 0.7106 | 1001.82 | 982.21 | 2.7405 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.67 |  | 469.7496 | 0.1959 | 469.08 | 460.78 | 0.1105 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 140.8 |  | 140.9005 | -0.0713 | 140.765 | 137.165 | 4.8509 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 168.37 |  | 166.4643 | 1.1448 | 163.275 | 157.34 | 2.9637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.85 |  | 274.6035 | 1.1822 | 269.59 | 256.24 | 0.18 | buy_precheck_manual_confirm | none |
| LITE | ai_networking_optical | 736.66 |  | 720.1941 | 2.2863 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 377.71 |  | 377.5865 | 0.0327 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 102.545 |  | 100.7728 | 1.7586 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.385 |  | 304.6374 | -0.0828 | 305.21 | 289.97 | 4.6192 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1759.8 |  | 1756.8801 | 0.1662 | 1741.99 | 1704.935 | 4.6806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 530.335 |  | 533.6952 | -0.6296 | 535.095 | 513.34 | 0.4356 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 313.13 |  | 312.0724 | 0.3389 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.29 |  | 212.2654 | 0.4827 | 210.82 | 204.71 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TER | semiconductor_test_packaging | 323.925 |  | 320.689 | 1.0091 | 308.03 | 297.18 | 4.2078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 277.22 |  | 277.6695 | -0.1619 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.37 |  | 61.6772 | 1.1232 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.885 |  | 50.0501 | 1.6682 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.43 |  | 135.3208 | 1.5587 | 129.93 | 126.945 | 4.5623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.99 |  | 319.4872 | 2.0354 | 315.89 | 307.13 | 4.9081 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 512.84 |  | 517.9464 | -0.9859 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.04 |  | 298.299 | -0.7573 | 304.36 | 299.62 | 0.0709 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 25.315 |  | 25.1156 | 0.7938 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.28 |  | 33.7289 | -1.331 | 34 | 32.26 | 0.0601 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.6877 | 0.4462 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1390.16 |  | 1425.9917 | -2.5128 | 1393.96 | 1325.48 | 0.1568 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 480.22 |  | 468.3192 | 2.5412 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 792.865 |  | 768.276 | 3.2005 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.115 |  | 247.9185 | -0.3241 | 247.72 | 243.725 | 0.0202 | below_vwap | below_vwap |
| META | cloud_ai_capex | 643.085 |  | 642.6206 | 0.0723 | 649.07 | 638.97 | 1.6281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.69 |  | 261.7572 | 1.8845 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 153.52 |  | 158.628 | -3.2201 | 151.99 | 145.6 | 0.6188 | below_vwap | below_vwap,spread_too_wide |
