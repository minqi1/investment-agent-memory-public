# Intraday State

- Generated at: `2026-07-17T23:46:37+08:00`
- Market time ET: `2026-07-17T11:46:38-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 3, 'watch_only': 3, 'spread_too_wide_or_missing': 30, 'price_stale_or_missing': 1, 'below_vwap': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.28 |  | 693.3924 | 0.4164 | 693.36 | 686.78 | 0.0287 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 519.57 |  | 512.896 | 1.3012 | 511.83 | 498.665 | 0.0789 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.4 |  | 549.9578 | 1.1714 | 550 | 536.9 | 0.0863 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.05 |  | 744.4687 | 0.0781 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.33 |  | 202.3051 | 1.0009 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.4 |  | 549.9578 | 1.1714 | 550 | 536.9 | 0.0863 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 519.57 |  | 512.896 | 1.3012 | 511.83 | 498.665 | 0.0789 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 212.02 |  | 210.2696 | 0.8325 | 210.82 | 204.71 | 0.1132 | buy_precheck_manual_confirm | none |
| 5 | GEV | data_center_power_cooling | 1046.63 |  | 1027.8659 | 1.8255 | 1001.82 | 982.21 | 0.1634 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.28 |  | 693.3924 | 0.4164 | 693.36 | 686.78 | 0.0287 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.54 |  | 45.301 | 0.5276 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.05 |  | 744.4687 | 0.0781 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 464.6 |  | 452.3775 | 2.7018 | 453.35 | 431.78 | 0.2884 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.34 |  | 247.8512 | 0.1972 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 125.77 |  | 124.9959 | 0.6193 | 125.02 | 121.79 | 0.0636 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.635 |  | 20.4018 | 1.143 | 20.445 | 19.92 | 0.0485 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 67.68 |  | 66.7224 | 1.4352 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.05 |  | 744.4687 | 0.0781 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.34 |  | 247.8512 | 0.1972 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.28 |  | 693.3924 | 0.4164 | 693.36 | 686.78 | 0.0287 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 125.77 |  | 124.9959 | 0.6193 | 125.02 | 121.79 | 0.0636 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 333.24 |  | 332.5106 | 0.2194 | 334.98 | 331.295 | 0.015 | watch_only | none |
| 6 | HPE | ai_server_oem | 45.54 |  | 45.301 | 0.5276 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 347.85 |  | 345.743 | 0.6094 | 348.47 | 341.42 | 0.0575 | watch_only | none |
| 8 | NVDA | ai_accelerator | 204.33 |  | 202.3051 | 1.0009 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.105 |  | 24.0183 | 0.3608 | 24.3 | 23.46 | 0.083 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 212.02 |  | 210.2696 | 0.8325 | 210.82 | 204.71 | 0.1132 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 556.4 |  | 549.9578 | 1.1714 | 550 | 536.9 | 0.0863 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.635 |  | 20.4018 | 1.143 | 20.445 | 19.92 | 0.0485 | buy_precheck_manual_confirm | none |
| 13 | SOXX | semiconductor_index | 519.57 |  | 512.896 | 1.3012 | 511.83 | 498.665 | 0.0789 | buy_precheck_manual_confirm | none |
| 14 | JCI | data_center_power_cooling | 141.51 |  | 140.5365 | 0.6927 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 370.38 |  | 368.0502 | 0.633 | 368.42 | 357.97 | 2.8349 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 471.05 |  | 469.0845 | 0.419 | 469.08 | 460.78 | 4.3265 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | GEV | data_center_power_cooling | 1046.63 |  | 1027.8659 | 1.8255 | 1001.82 | 982.21 | 0.1634 | buy_precheck_manual_confirm | none |
| 18 | WDC | memory_hbm_storage | 464.6 |  | 452.3775 | 2.7018 | 453.35 | 431.78 | 0.2884 | buy_precheck_manual_confirm | none |
| 19 | CIEN | ai_networking_optical | 377.54 |  | 373.4287 | 1.1009 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | IWM | market_regime | 293.59 |  | 294.0122 | -0.1436 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.33 |  | 202.3051 | 1.0009 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.4 |  | 549.9578 | 1.1714 | 550 | 536.9 | 0.0863 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 519.57 |  | 512.896 | 1.3012 | 511.83 | 498.665 | 0.0789 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 212.02 |  | 210.2696 | 0.8325 | 210.82 | 204.71 | 0.1132 | buy_precheck_manual_confirm | none |
| 5 | GEV | data_center_power_cooling | 1046.63 |  | 1027.8659 | 1.8255 | 1001.82 | 982.21 | 0.1634 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.28 |  | 693.3924 | 0.4164 | 693.36 | 686.78 | 0.0287 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.54 |  | 45.301 | 0.5276 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.05 |  | 744.4687 | 0.0781 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 464.6 |  | 452.3775 | 2.7018 | 453.35 | 431.78 | 0.2884 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.34 |  | 247.8512 | 0.1972 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 125.77 |  | 124.9959 | 0.6193 | 125.02 | 121.79 | 0.0636 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.635 |  | 20.4018 | 1.143 | 20.445 | 19.92 | 0.0485 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 67.68 |  | 66.7224 | 1.4352 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 165.765 |  | 163.1078 | 1.6291 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 398.5 |  | 395.3093 | 0.8071 | 394.11 | 386.02 | 0.8883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 370.38 |  | 368.0502 | 0.633 | 368.42 | 357.97 | 2.8349 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 537.59 |  | 529.0132 | 1.6213 | 535.095 | 513.34 | 4.4997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 492.05 |  | 480.6385 | 2.3742 | 482.43 | 461.04 | 2.7274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1756.84 |  | 1739.7312 | 0.9834 | 1741.99 | 1704.935 | 1.0735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 471.05 |  | 469.0845 | 0.419 | 469.08 | 460.78 | 4.3265 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.28 |  | 693.3924 | 0.4164 | 693.36 | 686.78 | 0.0287 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.68 |  | 66.7224 | 1.4352 | 66.9 | 64.92 | 0.0296 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.33 |  | 202.3051 | 1.0009 | 203.41 | 197.98 | 0.0147 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 391.88 |  | 393.089 | -0.3076 | 398.39 | 393.52 | 0.3062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.24 |  | 332.5106 | 0.2194 | 334.98 | 331.295 | 0.015 | watch_only | none |
| GOOGL | cloud_ai_capex | 347.85 |  | 345.743 | 0.6094 | 348.47 | 341.42 | 0.0575 | watch_only | none |
| AMD | ai_accelerator | 492.05 |  | 480.6385 | 2.3742 | 482.43 | 461.04 | 2.7274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.5 |  | 395.3093 | 0.8071 | 394.11 | 386.02 | 0.8883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 519.57 |  | 512.896 | 1.3012 | 511.83 | 498.665 | 0.0789 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.4 |  | 549.9578 | 1.1714 | 550 | 536.9 | 0.0863 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 370.38 |  | 368.0502 | 0.633 | 368.42 | 357.97 | 2.8349 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 860.215 |  | 849.7212 | 1.235 | 835.82 | 804.09 | 0.6324 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 186.09 |  | 184.5329 | 0.8438 | 185.03 | 178.09 | 0.7255 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 391.2 |  | 387.0436 | 1.0739 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.54 |  | 45.301 | 0.5276 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.105 |  | 24.0183 | 0.3608 | 24.3 | 23.46 | 0.083 | watch_only | none |
| SPY | market_regime | 745.05 |  | 744.4687 | 0.0781 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.59 |  | 294.0122 | -0.1436 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.77 |  | 124.9959 | 0.6193 | 125.02 | 121.79 | 0.0636 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.17 |  | 71.4459 | 2.4132 | 71.24 | 68.65 | 1.2847 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 289.04 |  | 282.775 | 2.2155 | 280.565 | 273.17 | 3.605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 400.3 |  | 396.2148 | 1.0311 | 389.4 | 382.38 | 4.2718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 630.365 |  | 624.5462 | 0.9317 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1046.63 |  | 1027.8659 | 1.8255 | 1001.82 | 982.21 | 0.1634 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 471.05 |  | 469.0845 | 0.419 | 469.08 | 460.78 | 4.3265 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.51 |  | 140.5365 | 0.6927 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.765 |  | 163.1078 | 1.6291 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 275.55 |  | 269.3411 | 2.3052 | 269.59 | 256.24 | 4.7142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 722.19 |  | 700.5594 | 3.0876 | 694.98 | 653.305 | 3.9449 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 377.54 |  | 373.4287 | 1.1009 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 100.47 |  | 98.3106 | 2.1965 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 299.115 |  | 300.1588 | -0.3478 | 305.21 | 289.97 | 4.3662 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1756.84 |  | 1739.7312 | 0.9834 | 1741.99 | 1704.935 | 1.0735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 537.59 |  | 529.0132 | 1.6213 | 535.095 | 513.34 | 4.4997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 313.8 |  | 308.3785 | 1.7581 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 212.02 |  | 210.2696 | 0.8325 | 210.82 | 204.71 | 0.1132 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 315.16 |  | 309.9148 | 1.6925 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 270.78 |  | 267.1638 | 1.3536 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.4 |  | 60.4359 | 1.5952 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.95 |  | 48.7899 | 2.3778 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.825 |  | 132.9995 | 2.1244 | 129.93 | 126.945 | 3.8064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 318.045 |  | 315.0489 | 0.951 | 315.89 | 307.13 | 4.8232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 520.2 |  | 521.7508 | -0.2972 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 299.9 |  | 301.3778 | -0.4903 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 24.8 |  | 24.8101 | -0.0407 | 25.45 | 24.1 | 0.0403 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.335 |  | 33.4258 | -0.2718 | 34 | 32.26 | 0.03 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.635 |  | 20.4018 | 1.143 | 20.445 | 19.92 | 0.0485 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1441.395 |  | 1403.3925 | 2.7079 | 1393.96 | 1325.48 | 2.7751 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 464.6 |  | 452.3775 | 2.7018 | 453.35 | 431.78 | 0.2884 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 754.37 |  | 736.2173 | 2.4657 | 724.57 | 702.24 | 5.0174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.34 |  | 247.8512 | 0.1972 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 630.65 |  | 635.5785 | -0.7754 | 649.07 | 638.97 | 0.5756 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 260.5 |  | 255.2669 | 2.05 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 162.15 |  | 155.7151 | 4.1325 | 151.99 | 145.6 | 0.8017 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
