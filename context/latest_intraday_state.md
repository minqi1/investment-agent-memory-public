# Intraday State

- Generated at: `2026-07-17T23:42:36+08:00`
- Market time ET: `2026-07-17T11:42:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 3, 'watch_only': 5, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_vwap': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.25 |  | 693.3751 | 0.4146 | 693.36 | 686.78 | 0.0417 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 519.04 |  | 512.7672 | 1.2233 | 511.83 | 498.665 | 0.0944 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.65 |  | 549.943 | 1.0378 | 550 | 536.9 | 0.0918 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.32 |  | 744.4525 | 0.1165 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.29 |  | 202.2869 | 0.9902 | 203.41 | 197.98 | 0.0636 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 398.525 |  | 395.2534 | 0.8277 | 394.11 | 386.02 | 0.0703 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.65 |  | 549.943 | 1.0378 | 550 | 536.9 | 0.0918 | buy_precheck_manual_confirm | none |
| 4 | AMAT | semiconductor_equipment | 536.83 |  | 528.9724 | 1.4854 | 535.095 | 513.34 | 0.3055 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 519.04 |  | 512.7672 | 1.2233 | 511.83 | 498.665 | 0.0944 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 211.29 |  | 210.2385 | 0.5002 | 210.82 | 204.71 | 0.1467 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.25 |  | 693.3751 | 0.4146 | 693.36 | 686.78 | 0.0417 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.56 |  | 45.2977 | 0.5791 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.32 |  | 744.4525 | 0.1165 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.78 |  | 247.8328 | 0.3822 | 247.72 | 243.725 | 0.1929 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.3902 | 1.4703 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.735 |  | 66.7107 | 1.5354 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.32 |  | 744.4525 | 0.1165 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 211.29 |  | 210.2385 | 0.5002 | 210.82 | 204.71 | 0.1467 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.25 |  | 693.3751 | 0.4146 | 693.36 | 686.78 | 0.0417 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.08 |  | 294.0298 | 0.0171 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 333.635 |  | 332.4724 | 0.3497 | 334.98 | 331.295 | 0.012 | watch_only | none |
| 6 | HPE | ai_server_oem | 45.56 |  | 45.2977 | 0.5791 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 24.88 |  | 24.8107 | 0.2792 | 25.45 | 24.1 | 0.0402 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 248.78 |  | 247.8328 | 0.3822 | 247.72 | 243.725 | 0.1929 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 347.96 |  | 345.7244 | 0.6467 | 348.47 | 341.42 | 0.0345 | watch_only | none |
| 10 | NVDA | ai_accelerator | 204.29 |  | 202.2869 | 0.9902 | 203.41 | 197.98 | 0.0636 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.145 |  | 24.0168 | 0.5338 | 24.3 | 23.46 | 0.0414 | watch_only | none |
| 12 | AMAT | semiconductor_equipment | 536.83 |  | 528.9724 | 1.4854 | 535.095 | 513.34 | 0.3055 | buy_precheck_manual_confirm | none |
| 13 | TSM | foundry | 398.525 |  | 395.2534 | 0.8277 | 394.11 | 386.02 | 0.0703 | buy_precheck_manual_confirm | none |
| 14 | SMH | semiconductor_index | 555.65 |  | 549.943 | 1.0378 | 550 | 536.9 | 0.0918 | buy_precheck_manual_confirm | none |
| 15 | SOXX | semiconductor_index | 519.04 |  | 512.7672 | 1.2233 | 511.83 | 498.665 | 0.0944 | buy_precheck_manual_confirm | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.3902 | 1.4703 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| 17 | TT | data_center_power_cooling | 470.76 |  | 469.0746 | 0.3593 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 141.38 |  | 140.509 | 0.6199 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 369.58 |  | 368.0414 | 0.4181 | 368.42 | 357.97 | 4.3969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ANET | ai_networking_optical | 165.185 |  | 163.0538 | 1.3071 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.29 |  | 202.2869 | 0.9902 | 203.41 | 197.98 | 0.0636 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 398.525 |  | 395.2534 | 0.8277 | 394.11 | 386.02 | 0.0703 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.65 |  | 549.943 | 1.0378 | 550 | 536.9 | 0.0918 | buy_precheck_manual_confirm | none |
| 4 | AMAT | semiconductor_equipment | 536.83 |  | 528.9724 | 1.4854 | 535.095 | 513.34 | 0.3055 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 519.04 |  | 512.7672 | 1.2233 | 511.83 | 498.665 | 0.0944 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 211.29 |  | 210.2385 | 0.5002 | 210.82 | 204.71 | 0.1467 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.25 |  | 693.3751 | 0.4146 | 693.36 | 686.78 | 0.0417 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.56 |  | 45.2977 | 0.5791 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.32 |  | 744.4525 | 0.1165 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.78 |  | 247.8328 | 0.3822 | 247.72 | 243.725 | 0.1929 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.3902 | 1.4703 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.735 |  | 66.7107 | 1.5354 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 13 | ANET | ai_networking_optical | 165.185 |  | 163.0538 | 1.3071 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 369.58 |  | 368.0414 | 0.4181 | 368.42 | 357.97 | 4.3969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 491.025 |  | 480.2626 | 2.2409 | 482.43 | 461.04 | 0.7861 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ASML | semiconductor_equipment | 1758.355 |  | 1739.4711 | 1.0856 | 1741.99 | 1704.935 | 2.3403 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 470.76 |  | 469.0746 | 0.3593 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MU | memory_hbm_storage | 861.03 |  | 849.538 | 1.3527 | 835.82 | 804.09 | 0.439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 288.11 |  | 282.7437 | 1.8979 | 280.565 | 273.17 | 3.7173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | JCI | data_center_power_cooling | 141.38 |  | 140.509 | 0.6199 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.25 |  | 693.3751 | 0.4146 | 693.36 | 686.78 | 0.0417 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.735 |  | 66.7107 | 1.5354 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.29 |  | 202.2869 | 0.9902 | 203.41 | 197.98 | 0.0636 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.285 |  | 393.1006 | -0.2075 | 398.39 | 393.52 | 0.4792 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 333.635 |  | 332.4724 | 0.3497 | 334.98 | 331.295 | 0.012 | watch_only | none |
| GOOGL | cloud_ai_capex | 347.96 |  | 345.7244 | 0.6467 | 348.47 | 341.42 | 0.0345 | watch_only | none |
| AMD | ai_accelerator | 491.025 |  | 480.2626 | 2.2409 | 482.43 | 461.04 | 0.7861 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.525 |  | 395.2534 | 0.8277 | 394.11 | 386.02 | 0.0703 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 519.04 |  | 512.7672 | 1.2233 | 511.83 | 498.665 | 0.0944 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.65 |  | 549.943 | 1.0378 | 550 | 536.9 | 0.0918 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 369.58 |  | 368.0414 | 0.4181 | 368.42 | 357.97 | 4.3969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 861.03 |  | 849.538 | 1.3527 | 835.82 | 804.09 | 0.439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 186.1 |  | 184.5207 | 0.8559 | 185.03 | 178.09 | 0.7577 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 391.24 |  | 387.011 | 1.0927 | 384 | 368.28 | 0.8102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.56 |  | 45.2977 | 0.5791 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.145 |  | 24.0168 | 0.5338 | 24.3 | 23.46 | 0.0414 | watch_only | none |
| SPY | market_regime | 745.32 |  | 744.4525 | 0.1165 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.08 |  | 294.0298 | 0.0171 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 126.015 |  | 124.9856 | 0.8236 | 125.02 | 121.79 | 0.8967 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.14 |  | 71.4396 | 2.3801 | 71.24 | 68.65 | 1.2989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 288.11 |  | 282.7437 | 1.8979 | 280.565 | 273.17 | 3.7173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 400.1 |  | 396.1387 | 1 | 389.4 | 382.38 | 4.3514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 629.56 |  | 624.445 | 0.8191 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1044.91 |  | 1027.7816 | 1.6665 | 1001.82 | 982.21 | 0.3589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.76 |  | 469.0746 | 0.3593 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.38 |  | 140.509 | 0.6199 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.185 |  | 163.0538 | 1.3071 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.18 |  | 269.2689 | 2.5666 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 721.15 |  | 700.3135 | 2.9753 | 694.98 | 653.305 | 3.9506 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 378.545 |  | 373.4004 | 1.3778 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.15 |  | 98.2869 | 2.913 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 299.76 |  | 300.1874 | -0.1424 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1758.355 |  | 1739.4711 | 1.0856 | 1741.99 | 1704.935 | 2.3403 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 536.83 |  | 528.9724 | 1.4854 | 535.095 | 513.34 | 0.3055 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 313.825 |  | 307.942 | 1.9104 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 211.29 |  | 210.2385 | 0.5002 | 210.82 | 204.71 | 0.1467 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 316.44 |  | 309.8779 | 2.1176 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 271.645 |  | 267.0715 | 1.7125 | 265.71 | 258.355 | 4.7157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 61.46 |  | 60.4224 | 1.7172 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.95 |  | 48.7899 | 2.3778 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.41 |  | 132.9773 | 2.5814 | 129.93 | 126.945 | 3.9513 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 320.11 |  | 315.0411 | 1.609 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 520.72 |  | 521.761 | -0.1995 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 300.325 |  | 301.443 | -0.3709 | 304.36 | 299.62 | 2.6804 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.88 |  | 24.8107 | 0.2792 | 25.45 | 24.1 | 0.0402 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.41 |  | 33.4265 | -0.0494 | 34 | 32.26 | 0.0299 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.69 |  | 20.3902 | 1.4703 | 20.445 | 19.92 | 0.0483 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1438.64 |  | 1402.6793 | 2.5637 | 1393.96 | 1325.48 | 0.9266 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 462.85 |  | 452.319 | 2.3282 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 753.12 |  | 736.0944 | 2.313 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.78 |  | 247.8328 | 0.3822 | 247.72 | 243.725 | 0.1929 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 630.51 |  | 635.6395 | -0.807 | 649.07 | 638.97 | 0.341 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 259.69 |  | 255.18 | 1.7674 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 161.155 |  | 155.5315 | 3.6157 | 151.99 | 145.6 | 3.841 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
