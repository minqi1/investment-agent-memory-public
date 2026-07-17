# Intraday State

- Generated at: `2026-07-17T23:29:44+08:00`
- Market time ET: `2026-07-17T11:29:46-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 3, 'watch_only': 2, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_vwap': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.56 |  | 693.2202 | 0.1933 | 693.36 | 686.78 | 0.0446 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 515.24 |  | 512.448 | 0.5448 | 511.83 | 498.665 | 0.1203 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 551.985 |  | 549.8527 | 0.3878 | 550 | 536.9 | 0.0779 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.12 |  | 744.3911 | 0.0979 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.81 |  | 202.1898 | 0.8013 | 203.41 | 197.98 | 0.0294 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 551.985 |  | 549.8527 | 0.3878 | 550 | 536.9 | 0.0779 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 515.24 |  | 512.448 | 0.5448 | 511.83 | 498.665 | 0.1203 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 854.29 |  | 848.787 | 0.6483 | 835.82 | 804.09 | 0.0597 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 388.91 |  | 386.8329 | 0.537 | 384 | 368.28 | 0.2674 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 694.56 |  | 693.2202 | 0.1933 | 693.36 | 686.78 | 0.0446 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.12 |  | 744.3911 | 0.0979 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 8 | STX | memory_hbm_storage | 747.1 |  | 735.3489 | 1.598 | 724.57 | 702.24 | 0.1124 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.38 |  | 247.7809 | 0.2418 | 247.72 | 243.725 | 0.0322 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.515 |  | 20.3375 | 0.873 | 20.445 | 19.92 | 0.0487 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.24 |  | 66.6591 | 0.8715 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 694.56 |  | 693.2202 | 0.1933 | 693.36 | 686.78 | 0.0446 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 745.12 |  | 744.3911 | 0.0979 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 248.38 |  | 247.7809 | 0.2418 | 247.72 | 243.725 | 0.0322 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 551.985 |  | 549.8527 | 0.3878 | 550 | 536.9 | 0.0779 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 515.24 |  | 512.448 | 0.5448 | 511.83 | 498.665 | 0.1203 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.445 |  | 33.4206 | 0.0731 | 34 | 32.26 | 0.0299 | watch_only | none |
| 7 | NVDA | ai_accelerator | 203.81 |  | 202.1898 | 0.8013 | 203.41 | 197.98 | 0.0294 | buy_precheck_manual_confirm | none |
| 8 | DELL | ai_server_oem | 388.91 |  | 386.8329 | 0.537 | 384 | 368.28 | 0.2674 | buy_precheck_manual_confirm | none |
| 9 | MU | memory_hbm_storage | 854.29 |  | 848.787 | 0.6483 | 835.82 | 804.09 | 0.0597 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 334.58 |  | 332.3055 | 0.6845 | 334.98 | 331.295 | 0.0359 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.515 |  | 20.3375 | 0.873 | 20.445 | 19.92 | 0.0487 | buy_precheck_manual_confirm | none |
| 12 | AVGO | custom_silicon_networking | 368.48 |  | 367.9488 | 0.1444 | 368.42 | 357.97 | 3.0531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | AMAT | semiconductor_equipment | 531.5 |  | 528.7715 | 0.516 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TT | data_center_power_cooling | 470.93 |  | 468.9843 | 0.4149 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | CIEN | ai_networking_optical | 375.02 |  | 373.2492 | 0.4744 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | GOOGL | cloud_ai_capex | 346.72 |  | 345.6245 | 0.317 | 348.47 | 341.42 | 0.398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 184.49 |  | 184.4737 | 0.0088 | 185.03 | 178.09 | 1.6695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ORCL | cloud_ai_capex | 125.58 |  | 124.8939 | 0.5494 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ASML | semiconductor_equipment | 1747.31 |  | 1736.7707 | 0.6068 | 1741.99 | 1704.935 | 0.6994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 747.1 |  | 735.3489 | 1.598 | 724.57 | 702.24 | 0.1124 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.81 |  | 202.1898 | 0.8013 | 203.41 | 197.98 | 0.0294 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 551.985 |  | 549.8527 | 0.3878 | 550 | 536.9 | 0.0779 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 515.24 |  | 512.448 | 0.5448 | 511.83 | 498.665 | 0.1203 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 854.29 |  | 848.787 | 0.6483 | 835.82 | 804.09 | 0.0597 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 388.91 |  | 386.8329 | 0.537 | 384 | 368.28 | 0.2674 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 694.56 |  | 693.2202 | 0.1933 | 693.36 | 686.78 | 0.0446 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.12 |  | 744.3911 | 0.0979 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 8 | STX | memory_hbm_storage | 747.1 |  | 735.3489 | 1.598 | 724.57 | 702.24 | 0.1124 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.38 |  | 247.7809 | 0.2418 | 247.72 | 243.725 | 0.0322 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.515 |  | 20.3375 | 0.873 | 20.445 | 19.92 | 0.0487 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.24 |  | 66.6591 | 0.8715 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 45.26 |  | 45.2818 | -0.048 | 44.92 | 43.715 | 0.0221 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 164.79 |  | 162.9202 | 1.1477 | 163.275 | 157.34 | 4.442 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 397.29 |  | 395.0593 | 0.5646 | 394.11 | 386.02 | 1.1629 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AVGO | custom_silicon_networking | 368.48 |  | 367.9488 | 0.1444 | 368.42 | 357.97 | 3.0531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 485.3 |  | 478.5697 | 1.4063 | 482.43 | 461.04 | 1.2281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1747.31 |  | 1736.7707 | 0.6068 | 1741.99 | 1704.935 | 0.6994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 470.93 |  | 468.9843 | 0.4149 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | VRT | data_center_power_cooling | 288.77 |  | 282.6015 | 2.1827 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 141.61 |  | 140.4004 | 0.8615 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.56 |  | 693.2202 | 0.1933 | 693.36 | 686.78 | 0.0446 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.24 |  | 66.6591 | 0.8715 | 66.9 | 64.92 | 0.0297 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.81 |  | 202.1898 | 0.8013 | 203.41 | 197.98 | 0.0294 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 390.715 |  | 393.228 | -0.6391 | 398.39 | 393.52 | 0.041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 334.58 |  | 332.3055 | 0.6845 | 334.98 | 331.295 | 0.0359 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.72 |  | 345.6245 | 0.317 | 348.47 | 341.42 | 0.398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 485.3 |  | 478.5697 | 1.4063 | 482.43 | 461.04 | 1.2281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 397.29 |  | 395.0593 | 0.5646 | 394.11 | 386.02 | 1.1629 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 515.24 |  | 512.448 | 0.5448 | 511.83 | 498.665 | 0.1203 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 551.985 |  | 549.8527 | 0.3878 | 550 | 536.9 | 0.0779 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 368.48 |  | 367.9488 | 0.1444 | 368.42 | 357.97 | 3.0531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 854.29 |  | 848.787 | 0.6483 | 835.82 | 804.09 | 0.0597 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 184.49 |  | 184.4737 | 0.0088 | 185.03 | 178.09 | 1.6695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 388.91 |  | 386.8329 | 0.537 | 384 | 368.28 | 0.2674 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 45.26 |  | 45.2818 | -0.048 | 44.92 | 43.715 | 0.0221 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 24.01 |  | 24.0116 | -0.0066 | 24.3 | 23.46 | 0.0416 | below_vwap | below_vwap |
| SPY | market_regime | 745.12 |  | 744.3911 | 0.0979 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.035 |  | 294.0479 | -0.0044 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.58 |  | 124.8939 | 0.5494 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 72.72 |  | 71.3066 | 1.9821 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 288.77 |  | 282.6015 | 2.1827 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 399.24 |  | 395.9734 | 0.825 | 389.4 | 382.38 | 4.4159 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 627.95 |  | 623.8039 | 0.6647 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1044.88 |  | 1026.9265 | 1.7483 | 1001.82 | 982.21 | 1.025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.93 |  | 468.9843 | 0.4149 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.61 |  | 140.4004 | 0.8615 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.79 |  | 162.9202 | 1.1477 | 163.275 | 157.34 | 4.442 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 274.06 |  | 268.9672 | 1.8935 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 717.02 |  | 699.3403 | 2.528 | 694.98 | 653.305 | 1.0251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.02 |  | 373.2492 | 0.4744 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 99.62 |  | 98.1548 | 1.4927 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 298.59 |  | 300.198 | -0.5356 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1747.31 |  | 1736.7707 | 0.6068 | 1741.99 | 1704.935 | 0.6994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.5 |  | 528.7715 | 0.516 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 309.51 |  | 307.4072 | 0.684 | 306.51 | 298.89 | 1.9773 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 209.56 |  | 210.2219 | -0.3149 | 210.82 | 204.71 | 0.2004 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 311.12 |  | 309.5287 | 0.5141 | 308.03 | 297.18 | 4.1399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 269.31 |  | 266.9612 | 0.8798 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 60.96 |  | 60.2726 | 1.1405 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.36 |  | 48.6516 | 1.4561 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 134.675 |  | 132.8143 | 1.401 | 129.93 | 126.945 | 4.923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 317.87 |  | 314.9446 | 0.9289 | 315.89 | 307.13 | 4.4138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 521.375 |  | 521.8005 | -0.0815 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 300.945 |  | 301.5252 | -0.1924 | 304.36 | 299.62 | 2.4024 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.805 |  | 24.8074 | -0.0099 | 25.45 | 24.1 | 0.0403 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.445 |  | 33.4206 | 0.0731 | 34 | 32.26 | 0.0299 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.515 |  | 20.3375 | 0.873 | 20.445 | 19.92 | 0.0487 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1414.95 |  | 1401.3758 | 0.9686 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 457.04 |  | 452.0702 | 1.0993 | 453.35 | 431.78 | 4.1572 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 747.1 |  | 735.3489 | 1.598 | 724.57 | 702.24 | 0.1124 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 248.38 |  | 247.7809 | 0.2418 | 247.72 | 243.725 | 0.0322 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 628.5 |  | 636.0132 | -1.1813 | 649.07 | 638.97 | 0.5871 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.53 |  | 255.0057 | 1.382 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 155.9 |  | 154.9784 | 0.5947 | 151.99 | 145.6 | 4.8749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
