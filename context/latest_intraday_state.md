# Intraday State

- Generated at: `2026-07-18T02:27:37+08:00`
- Market time ET: `2026-07-17T14:27:38-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 4, 'below_vwap': 14, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.055 |  | 695.4955 | 0.2242 | 693.36 | 686.78 | 0.0531 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 522.64 |  | 518.2576 | 0.8456 | 511.83 | 498.665 | 0.0689 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.07 |  | 554.9637 | 0.3795 | 550 | 536.9 | 0.0682 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.465 |  | 744.9438 | -0.1985 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.07 |  | 554.9637 | 0.3795 | 550 | 536.9 | 0.0682 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 522.64 |  | 518.2576 | 0.8456 | 511.83 | 498.665 | 0.0689 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.555 |  | 212.1758 | 0.1787 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1057.69 |  | 1044.879 | 1.2261 | 1001.82 | 982.21 | 0.2052 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.055 |  | 695.4955 | 0.2242 | 693.36 | 686.78 | 0.0531 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.24 |  | 45.6466 | 1.3001 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 323.24 |  | 319.7984 | 1.0762 | 308.03 | 297.18 | 0.1949 | buy_precheck_manual_confirm | none |
| 8 | SKHY | memory_hbm_storage | 160.86 |  | 158.6563 | 1.389 | 151.99 | 145.6 | 0.3357 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189 |  | 187.1092 | 1.0105 | 185.03 | 178.09 | 0.254 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 126.68 |  | 125.9989 | 0.5405 | 125.02 | 121.79 | 0.15 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.66 |  | 24.2929 | 1.5112 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.6544 | 1.8668 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 67.97 |  | 67.1944 | 1.1543 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 697.055 |  | 695.4955 | 0.2242 | 693.36 | 686.78 | 0.0531 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 212.555 |  | 212.1758 | 0.1787 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 557.07 |  | 554.9637 | 0.3795 | 550 | 536.9 | 0.0682 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 203.24 |  | 203.2398 | 0.0001 | 203.41 | 197.98 | 0.1968 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 332.36 |  | 332.001 | 0.1081 | 334.98 | 331.295 | 0.0211 | watch_only | none |
| 6 | ORCL | cloud_ai_capex | 126.68 |  | 125.9989 | 0.5405 | 125.02 | 121.79 | 0.15 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 395.08 |  | 393.3556 | 0.4384 | 398.39 | 393.52 | 0.0557 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 25.215 |  | 25.0846 | 0.5197 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| 9 | SOXX | semiconductor_index | 522.64 |  | 518.2576 | 0.8456 | 511.83 | 498.665 | 0.0689 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.24 |  | 45.6466 | 1.3001 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 11 | GEV | data_center_power_cooling | 1057.69 |  | 1044.879 | 1.2261 | 1001.82 | 982.21 | 0.2052 | buy_precheck_manual_confirm | none |
| 12 | TER | semiconductor_test_packaging | 323.24 |  | 319.7984 | 1.0762 | 308.03 | 297.18 | 0.1949 | buy_precheck_manual_confirm | none |
| 13 | SKHY | memory_hbm_storage | 160.86 |  | 158.6563 | 1.389 | 151.99 | 145.6 | 0.3357 | buy_precheck_manual_confirm | none |
| 14 | MRVL | custom_silicon_networking | 189 |  | 187.1092 | 1.0105 | 185.03 | 178.09 | 0.254 | buy_precheck_manual_confirm | none |
| 15 | ONTO | semiconductor_test_packaging | 278.29 |  | 277.5833 | 0.2546 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ASML | semiconductor_equipment | 1764.86 |  | 1756.6639 | 0.4666 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SMCI | ai_server_oem | 24.66 |  | 24.2929 | 1.5112 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| 18 | ETN | data_center_power_cooling | 400.26 |  | 399.7408 | 0.1299 | 389.4 | 382.38 | 3.4852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 633.215 |  | 629.8398 | 0.5359 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.6544 | 1.8668 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.07 |  | 554.9637 | 0.3795 | 550 | 536.9 | 0.0682 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 522.64 |  | 518.2576 | 0.8456 | 511.83 | 498.665 | 0.0689 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.555 |  | 212.1758 | 0.1787 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1057.69 |  | 1044.879 | 1.2261 | 1001.82 | 982.21 | 0.2052 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 697.055 |  | 695.4955 | 0.2242 | 693.36 | 686.78 | 0.0531 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.24 |  | 45.6466 | 1.3001 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 323.24 |  | 319.7984 | 1.0762 | 308.03 | 297.18 | 0.1949 | buy_precheck_manual_confirm | none |
| 8 | SKHY | memory_hbm_storage | 160.86 |  | 158.6563 | 1.389 | 151.99 | 145.6 | 0.3357 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189 |  | 187.1092 | 1.0105 | 185.03 | 178.09 | 0.254 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 126.68 |  | 125.9989 | 0.5405 | 125.02 | 121.79 | 0.15 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.66 |  | 24.2929 | 1.5112 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.6544 | 1.8668 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 67.97 |  | 67.1944 | 1.1543 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 14 | TSM | foundry | 397.12 |  | 398.1072 | -0.248 | 394.11 | 386.02 | 0.5515 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 469.19 |  | 469.7855 | -0.1268 | 469.08 | 460.78 | 4.3415 | below_vwap | below_vwap,spread_too_wide |
| 16 | CIEN | ai_networking_optical | 377.73 |  | 377.8515 | -0.0321 | 375.52 | 359.81 | 1.3105 | below_vwap | below_vwap,spread_too_wide |
| 17 | LRCX | semiconductor_equipment | 312.04 |  | 312.0861 | -0.0148 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | SPY | market_regime | 743.465 |  | 744.9438 | -0.1985 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 19 | SNDK | memory_hbm_storage | 1422.03 |  | 1428.2117 | -0.4328 | 1393.96 | 1325.48 | 4.6166 | below_vwap | below_vwap,spread_too_wide |
| 20 | ANET | ai_networking_optical | 168.84 |  | 166.1012 | 1.6489 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.055 |  | 695.4955 | 0.2242 | 693.36 | 686.78 | 0.0531 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.97 |  | 67.1944 | 1.1543 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.24 |  | 203.2398 | 0.0001 | 203.41 | 197.98 | 0.1968 | watch_only | none |
| MSFT | cloud_ai_capex | 395.08 |  | 393.3556 | 0.4384 | 398.39 | 393.52 | 0.0557 | watch_only | none |
| AAPL | mega_cap_platform | 332.36 |  | 332.001 | 0.1081 | 334.98 | 331.295 | 0.0211 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.155 |  | 345.8812 | -0.4991 | 348.47 | 341.42 | 0.2818 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.18 |  | 486.6945 | 1.7435 | 482.43 | 461.04 | 2.9605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 397.12 |  | 398.1072 | -0.248 | 394.11 | 386.02 | 0.5515 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 522.64 |  | 518.2576 | 0.8456 | 511.83 | 498.665 | 0.0689 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.07 |  | 554.9637 | 0.3795 | 550 | 536.9 | 0.0682 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.355 |  | 370.1784 | 0.588 | 368.42 | 357.97 | 2.0652 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 872.55 |  | 863.9407 | 0.9965 | 835.82 | 804.09 | 1.0555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189 |  | 187.1092 | 1.0105 | 185.03 | 178.09 | 0.254 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 401.705 |  | 392.7423 | 2.2821 | 384 | 368.28 | 4.1523 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.24 |  | 45.6466 | 1.3001 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.66 |  | 24.2929 | 1.5112 | 24.3 | 23.46 | 0.0811 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.465 |  | 744.9438 | -0.1985 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.72 |  | 294.1881 | -0.1591 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.68 |  | 125.9989 | 0.5405 | 125.02 | 121.79 | 0.15 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.48 |  | 72.193 | 1.7827 | 71.24 | 68.65 | 3.0484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.215 |  | 287.1555 | 1.7619 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.26 |  | 399.7408 | 0.1299 | 389.4 | 382.38 | 3.4852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 633.215 |  | 629.8398 | 0.5359 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1057.69 |  | 1044.879 | 1.2261 | 1001.82 | 982.21 | 0.2052 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 469.19 |  | 469.7855 | -0.1268 | 469.08 | 460.78 | 4.3415 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.67 |  | 140.9635 | -0.2082 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.84 |  | 166.1012 | 1.6489 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.58 |  | 273.925 | 1.6994 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 734.95 |  | 717.1255 | 2.4855 | 694.98 | 653.305 | 2.1267 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.73 |  | 377.8515 | -0.0321 | 375.52 | 359.81 | 1.3105 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.84 |  | 100.4924 | 2.3361 | 97.585 | 91.92 | 4.5605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 301.99 |  | 305.2489 | -1.0676 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1764.86 |  | 1756.6639 | 0.4666 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 532.45 |  | 535.3465 | -0.5411 | 535.095 | 513.34 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 312.04 |  | 312.0861 | -0.0148 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.555 |  | 212.1758 | 0.1787 | 210.82 | 204.71 | 0.0659 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 323.24 |  | 319.7984 | 1.0762 | 308.03 | 297.18 | 0.1949 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 278.29 |  | 277.5833 | 0.2546 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.19 |  | 61.4759 | 1.1615 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.88 |  | 49.8843 | 1.9959 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.08 |  | 134.6559 | 1.8002 | 129.93 | 126.945 | 4.9825 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 323.93 |  | 318.6878 | 1.6449 | 315.89 | 307.13 | 4.5936 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.32 |  | 519.9928 | -1.0909 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.9 |  | 299.0844 | -1.0647 | 304.36 | 299.62 | 4.8597 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.215 |  | 25.0846 | 0.5197 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.75 |  | 33.7941 | -0.1304 | 34 | 32.26 | 0.0889 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.04 |  | 20.6544 | 1.8668 | 20.445 | 19.92 | 0.0951 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1422.03 |  | 1428.2117 | -0.4328 | 1393.96 | 1325.48 | 4.6166 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.97 |  | 466.7219 | 3.0528 | 453.35 | 431.78 | 0.7568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 788.75 |  | 760.1829 | 3.7579 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.65 |  | 248.011 | -0.1455 | 247.72 | 243.725 | 0.0121 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.83 |  | 642.2313 | 0.716 | 649.07 | 638.97 | 0.8086 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.26 |  | 261.0691 | 2.7544 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 160.86 |  | 158.6563 | 1.389 | 151.99 | 145.6 | 0.3357 | buy_precheck_manual_confirm | none |
