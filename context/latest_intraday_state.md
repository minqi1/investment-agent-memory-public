# Intraday State

- Generated at: `2026-07-17T22:09:40+08:00`
- Market time ET: `2026-07-17T10:09:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 4, 'watch_only': 2, 'spread_too_wide_or_missing': 35, 'price_stale_or_missing': 1, 'below_vwap': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.19 |  | 691.2206 | 0.7189 | 693.36 | 686.78 | 0.0517 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 520.8 |  | 508.9795 | 2.3224 | 511.83 | 498.665 | 0.144 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.31 |  | 545.7503 | 1.9349 | 550 | 536.9 | 0.1168 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.19 |  | 742.9772 | 0.4324 | 742.66 | 740.8 | 0.0563 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.6 |  | 200.5426 | 2.0232 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.31 |  | 545.7503 | 1.9349 | 550 | 536.9 | 0.1168 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 520.8 |  | 508.9795 | 2.3224 | 511.83 | 498.665 | 0.144 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 212.995 |  | 209.0372 | 1.8934 | 210.82 | 204.71 | 0.1315 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.61 |  | 293.6234 | 0.6766 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.19 |  | 691.2206 | 0.7189 | 693.36 | 686.78 | 0.0517 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.39 |  | 44.5283 | 1.9351 | 44.92 | 43.715 | 0.0881 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.19 |  | 742.9772 | 0.4324 | 742.66 | 740.8 | 0.0563 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.09 |  | 246.6882 | 0.5683 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.3 |  | 23.7637 | 2.2568 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.65 |  | 20.198 | 2.2377 | 20.445 | 19.92 | 0.0969 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.2 |  | 33.1256 | 3.2433 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 67.74 |  | 65.9556 | 2.7054 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 248.09 |  | 246.6882 | 0.5683 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 295.61 |  | 293.6234 | 0.6766 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.19 |  | 691.2206 | 0.7189 | 693.36 | 686.78 | 0.0517 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 746.19 |  | 742.9772 | 0.4324 | 742.66 | 740.8 | 0.0563 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 347.09 |  | 345.1171 | 0.5717 | 348.47 | 341.42 | 0.1959 | watch_only | none |
| 6 | NVDA | ai_accelerator | 204.6 |  | 200.5426 | 2.0232 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.3 |  | 23.7637 | 2.2568 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| 8 | SMH | semiconductor_index | 556.31 |  | 545.7503 | 1.9349 | 550 | 536.9 | 0.1168 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 471.06 |  | 467.453 | 0.7716 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | KLAC | semiconductor_equipment | 212.995 |  | 209.0372 | 1.8934 | 210.82 | 204.71 | 0.1315 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 34.2 |  | 33.1256 | 3.2433 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| 12 | APD | industrial_gases | 302.47 |  | 302.044 | 0.1411 | 304.36 | 299.62 | 4.817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | HPE | ai_server_oem | 45.39 |  | 44.5283 | 1.9351 | 44.92 | 43.715 | 0.0881 | buy_precheck_manual_confirm | none |
| 14 | CORZ | high_beta_ai_infrastructure | 20.65 |  | 20.198 | 2.2377 | 20.445 | 19.92 | 0.0969 | buy_precheck_manual_confirm | none |
| 15 | SOXX | semiconductor_index | 520.8 |  | 508.9795 | 2.3224 | 511.83 | 498.665 | 0.144 | buy_precheck_manual_confirm | none |
| 16 | ASML | semiconductor_equipment | 1740.83 |  | 1727.2198 | 0.788 | 1741.99 | 1704.935 | 0.4745 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | APLD | high_beta_ai_infrastructure | 25.305 |  | 24.6554 | 2.6348 | 25.45 | 24.1 | 0.079 | watch_only | none |
| 18 | AVGO | custom_silicon_networking | 369.84 |  | 365.0121 | 1.3227 | 368.42 | 357.97 | 2.2361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 535.13 |  | 524.4358 | 2.0392 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ORCL | cloud_ai_capex | 125.23 |  | 123.9161 | 1.0603 | 125.02 | 121.79 | 3.4816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.6 |  | 200.5426 | 2.0232 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.31 |  | 545.7503 | 1.9349 | 550 | 536.9 | 0.1168 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 520.8 |  | 508.9795 | 2.3224 | 511.83 | 498.665 | 0.144 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 212.995 |  | 209.0372 | 1.8934 | 210.82 | 204.71 | 0.1315 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.61 |  | 293.6234 | 0.6766 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.19 |  | 691.2206 | 0.7189 | 693.36 | 686.78 | 0.0517 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.39 |  | 44.5283 | 1.9351 | 44.92 | 43.715 | 0.0881 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.19 |  | 742.9772 | 0.4324 | 742.66 | 740.8 | 0.0563 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.09 |  | 246.6882 | 0.5683 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.3 |  | 23.7637 | 2.2568 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.65 |  | 20.198 | 2.2377 | 20.445 | 19.92 | 0.0969 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.2 |  | 33.1256 | 3.2433 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 67.74 |  | 65.9556 | 2.7054 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 165.22 |  | 161.2207 | 2.4806 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 399.36 |  | 391.6038 | 1.9806 | 394.11 | 386.02 | 0.9816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 369.84 |  | 365.0121 | 1.3227 | 368.42 | 357.97 | 2.2361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 535.13 |  | 524.4358 | 2.0392 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 488.91 |  | 471.2853 | 3.7397 | 482.43 | 461.04 | 2.5219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 471.06 |  | 467.453 | 0.7716 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 857.63 |  | 831.6607 | 3.1226 | 835.82 | 804.09 | 2.915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.19 |  | 691.2206 | 0.7189 | 693.36 | 686.78 | 0.0517 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.74 |  | 65.9556 | 2.7054 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.6 |  | 200.5426 | 2.0232 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.22 |  | 394.9059 | -0.6801 | 398.39 | 393.52 | 0.1453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.05 |  | 332.4301 | -0.716 | 334.98 | 331.295 | 0.0848 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.09 |  | 345.1171 | 0.5717 | 348.47 | 341.42 | 0.1959 | watch_only | none |
| AMD | ai_accelerator | 488.91 |  | 471.2853 | 3.7397 | 482.43 | 461.04 | 2.5219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 399.36 |  | 391.6038 | 1.9806 | 394.11 | 386.02 | 0.9816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 520.8 |  | 508.9795 | 2.3224 | 511.83 | 498.665 | 0.144 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.31 |  | 545.7503 | 1.9349 | 550 | 536.9 | 0.1168 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 369.84 |  | 365.0121 | 1.3227 | 368.42 | 357.97 | 2.2361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 857.63 |  | 831.6607 | 3.1226 | 835.82 | 804.09 | 2.915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 186.86 |  | 182.4297 | 2.4285 | 185.03 | 178.09 | 0.7546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 389.115 |  | 377.7546 | 3.0074 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.39 |  | 44.5283 | 1.9351 | 44.92 | 43.715 | 0.0881 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.3 |  | 23.7637 | 2.2568 | 24.3 | 23.46 | 0.0823 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.19 |  | 742.9772 | 0.4324 | 742.66 | 740.8 | 0.0563 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.61 |  | 293.6234 | 0.6766 | 294.205 | 291.675 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.23 |  | 123.9161 | 1.0603 | 125.02 | 121.79 | 3.4816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 71.51 |  | 69.8415 | 2.389 | 71.24 | 68.65 | 2.2794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 287.785 |  | 279.0023 | 3.1479 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.02 |  | 392.9907 | 1.7887 | 389.4 | 382.38 | 4.3673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 624.16 |  | 617.144 | 1.1369 | 616.75 | 609.05 | 0.4678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1052.34 |  | 1017.3362 | 3.4407 | 1001.82 | 982.21 | 4.7523 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 471.06 |  | 467.453 | 0.7716 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.8 |  | 139.1948 | 1.8716 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.22 |  | 161.2207 | 2.4806 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 273.215 |  | 266.3484 | 2.578 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 709.31 |  | 679.4784 | 4.3904 | 694.98 | 653.305 | 5.1078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 380.66 |  | 370.2044 | 2.8243 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 99.31 |  | 95.2057 | 4.311 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.51 |  | 298.012 | 2.1805 | 305.21 | 289.97 | 4.1838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1740.83 |  | 1727.2198 | 0.788 | 1741.99 | 1704.935 | 0.4745 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 535.13 |  | 524.4358 | 2.0392 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 312.66 |  | 303.695 | 2.952 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 212.995 |  | 209.0372 | 1.8934 | 210.82 | 204.71 | 0.1315 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 315.08 |  | 304.1681 | 3.5874 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 270.78 |  | 264.6502 | 2.3162 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.11 |  | 59.2011 | 3.2244 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.44 |  | 48.0491 | 4.976 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.325 |  | 130.5961 | 3.621 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 319.17 |  | 312.1157 | 2.2601 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 521.86 |  | 522.3653 | -0.0967 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 302.47 |  | 302.044 | 0.1411 | 304.36 | 299.62 | 4.817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 25.305 |  | 24.6554 | 2.6348 | 25.45 | 24.1 | 0.079 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.2 |  | 33.1256 | 3.2433 | 34 | 32.26 | 0.0585 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.65 |  | 20.198 | 2.2377 | 20.445 | 19.92 | 0.0969 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1432.88 |  | 1377.1425 | 4.0473 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 457.285 |  | 443.6467 | 3.0741 | 453.35 | 431.78 | 0.5336 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 741.32 |  | 721.4419 | 2.7553 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.09 |  | 246.6882 | 0.5683 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 636.27 |  | 641.872 | -0.8728 | 649.07 | 638.97 | 1.9253 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 261.055 |  | 250.0558 | 4.3987 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 157.93 |  | 152.5669 | 3.5152 | 151.99 | 145.6 | 1.7223 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
