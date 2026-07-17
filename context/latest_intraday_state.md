# Intraday State

- Generated at: `2026-07-18T03:48:45+08:00`
- Market time ET: `2026-07-17T15:48:46-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 15, 'watch_only': 4, 'below_vwap': 14, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.62 |  | 695.6589 | 0.1382 | 693.36 | 686.78 | 0.0359 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.64 |  | 519.0521 | 0.8839 | 511.83 | 498.665 | 0.0821 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.915 |  | 555.3027 | 0.4704 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.87 |  | 744.5132 | -0.0864 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.915 |  | 555.3027 | 0.4704 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.64 |  | 519.0521 | 0.8839 | 511.83 | 498.665 | 0.0821 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 470.79 |  | 469.7577 | 0.2197 | 469.08 | 460.78 | 0.325 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.43 |  | 212.2868 | 0.5385 | 210.82 | 204.71 | 0.0609 | buy_precheck_manual_confirm | none |
| 5 | ETN | data_center_power_cooling | 401.875 |  | 399.7949 | 0.5203 | 389.4 | 382.38 | 0.2886 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1057.25 |  | 1046.9987 | 0.9791 | 1001.82 | 982.21 | 0.1277 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.62 |  | 695.6589 | 0.1382 | 693.36 | 686.78 | 0.0359 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.965 |  | 45.7235 | 0.5281 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | MKSI | semiconductor_materials | 325.21 |  | 319.5816 | 1.7612 | 315.89 | 307.13 | 0.2614 | buy_precheck_manual_confirm | none |
| 10 | ARM | ai_accelerator | 267 |  | 261.7756 | 1.9957 | 252.95 | 243.21 | 0.3296 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 126.6 |  | 126.1037 | 0.3936 | 125.02 | 121.79 | 0.0711 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.45 |  | 24.3294 | 0.4956 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6893 | 0.7285 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| 14 | APLD | high_beta_ai_infrastructure | 25.465 |  | 25.1195 | 1.3755 | 25.45 | 24.1 | 0.0393 | buy_precheck_manual_confirm | none |
| 15 | TQQQ | leveraged_tool | 67.85 |  | 67.2752 | 0.8544 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.62 |  | 695.6589 | 0.1382 | 693.36 | 686.78 | 0.0359 | buy_precheck_manual_confirm | none |
| 2 | TT | data_center_power_cooling | 470.79 |  | 469.7577 | 0.2197 | 469.08 | 460.78 | 0.325 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 203.26 |  | 203.1692 | 0.0447 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| 4 | SMH | semiconductor_index | 557.915 |  | 555.3027 | 0.4704 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 24.45 |  | 24.3294 | 0.4956 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 213.43 |  | 212.2868 | 0.5385 | 210.82 | 204.71 | 0.0609 | buy_precheck_manual_confirm | none |
| 7 | META | cloud_ai_capex | 643.075 |  | 642.6259 | 0.0699 | 649.07 | 638.97 | 0.2379 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 126.6 |  | 126.1037 | 0.3936 | 125.02 | 121.79 | 0.0711 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 45.965 |  | 45.7235 | 0.5281 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 333.94 |  | 332.4361 | 0.4524 | 334.98 | 331.295 | 0.018 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6893 | 0.7285 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| 12 | ETN | data_center_power_cooling | 401.875 |  | 399.7949 | 0.5203 | 389.4 | 382.38 | 0.2886 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 25.465 |  | 25.1195 | 1.3755 | 25.45 | 24.1 | 0.0393 | buy_precheck_manual_confirm | none |
| 14 | MSFT | cloud_ai_capex | 395.195 |  | 393.736 | 0.3706 | 398.39 | 393.52 | 0.21 | watch_only | none |
| 15 | SOXX | semiconductor_index | 523.64 |  | 519.0521 | 0.8839 | 511.83 | 498.665 | 0.0821 | buy_precheck_manual_confirm | none |
| 16 | GEV | data_center_power_cooling | 1057.25 |  | 1046.9987 | 0.9791 | 1001.82 | 982.21 | 0.1277 | buy_precheck_manual_confirm | none |
| 17 | PWR | data_center_power_cooling | 631.385 |  | 630.3479 | 0.1645 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TSM | foundry | 398.065 |  | 397.8336 | 0.0582 | 394.11 | 386.02 | 0.4321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1761.35 |  | 1756.9102 | 0.2527 | 1741.99 | 1704.935 | 2.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | LRCX | semiconductor_equipment | 313.02 |  | 312.0799 | 0.3012 | 306.51 | 298.89 | 4.5428 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.915 |  | 555.3027 | 0.4704 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.64 |  | 519.0521 | 0.8839 | 511.83 | 498.665 | 0.0821 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 470.79 |  | 469.7577 | 0.2197 | 469.08 | 460.78 | 0.325 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.43 |  | 212.2868 | 0.5385 | 210.82 | 204.71 | 0.0609 | buy_precheck_manual_confirm | none |
| 5 | ETN | data_center_power_cooling | 401.875 |  | 399.7949 | 0.5203 | 389.4 | 382.38 | 0.2886 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1057.25 |  | 1046.9987 | 0.9791 | 1001.82 | 982.21 | 0.1277 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.62 |  | 695.6589 | 0.1382 | 693.36 | 686.78 | 0.0359 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.965 |  | 45.7235 | 0.5281 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | MKSI | semiconductor_materials | 325.21 |  | 319.5816 | 1.7612 | 315.89 | 307.13 | 0.2614 | buy_precheck_manual_confirm | none |
| 10 | ARM | ai_accelerator | 267 |  | 261.7756 | 1.9957 | 252.95 | 243.21 | 0.3296 | buy_precheck_manual_confirm | none |
| 11 | ORCL | cloud_ai_capex | 126.6 |  | 126.1037 | 0.3936 | 125.02 | 121.79 | 0.0711 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.45 |  | 24.3294 | 0.4956 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6893 | 0.7285 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| 14 | APLD | high_beta_ai_infrastructure | 25.465 |  | 25.1195 | 1.3755 | 25.45 | 24.1 | 0.0393 | buy_precheck_manual_confirm | none |
| 15 | TQQQ | leveraged_tool | 67.85 |  | 67.2752 | 0.8544 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 16 | MU | memory_hbm_storage | 861.1 |  | 864.5343 | -0.3972 | 835.82 | 804.09 | 0.2903 | below_vwap | below_vwap |
| 17 | CIEN | ai_networking_optical | 376.705 |  | 377.5807 | -0.2319 | 375.52 | 359.81 | 4.5394 | below_vwap | below_vwap,spread_too_wide |
| 18 | SPY | market_regime | 743.87 |  | 744.5132 | -0.0864 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 19 | ONTO | semiconductor_test_packaging | 277.26 |  | 277.6716 | -0.1482 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | SKHY | memory_hbm_storage | 153.33 |  | 158.5915 | -3.3176 | 151.99 | 145.6 | 0.3522 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.62 |  | 695.6589 | 0.1382 | 693.36 | 686.78 | 0.0359 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.85 |  | 67.2752 | 0.8544 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.26 |  | 203.1692 | 0.0447 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| MSFT | cloud_ai_capex | 395.195 |  | 393.736 | 0.3706 | 398.39 | 393.52 | 0.21 | watch_only | none |
| AAPL | mega_cap_platform | 333.94 |  | 332.4361 | 0.4524 | 334.98 | 331.295 | 0.018 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.34 |  | 345.7 | -0.1041 | 348.47 | 341.42 | 0.4141 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 496.67 |  | 487.535 | 1.8737 | 482.43 | 461.04 | 2.8127 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.065 |  | 397.8336 | 0.0582 | 394.11 | 386.02 | 0.4321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.64 |  | 519.0521 | 0.8839 | 511.83 | 498.665 | 0.0821 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.915 |  | 555.3027 | 0.4704 | 550 | 536.9 | 0.0233 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.165 |  | 370.5254 | 0.4425 | 368.42 | 357.97 | 2.1442 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 861.1 |  | 864.5343 | -0.3972 | 835.82 | 804.09 | 0.2903 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 189.02 |  | 187.3233 | 0.9058 | 185.03 | 178.09 | 1.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 399.76 |  | 393.9063 | 1.4861 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.965 |  | 45.7235 | 0.5281 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.45 |  | 24.3294 | 0.4956 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.87 |  | 744.5132 | -0.0864 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 294.06 |  | 294.0725 | -0.0043 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.6 |  | 126.1037 | 0.3936 | 125.02 | 121.79 | 0.0711 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.08 |  | 72.3325 | 1.0334 | 71.24 | 68.65 | 3.7356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.68 |  | 287.8947 | 0.9675 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.875 |  | 399.7949 | 0.5203 | 389.4 | 382.38 | 0.2886 | buy_precheck_manual_confirm | none |
| PWR | data_center_power_cooling | 631.385 |  | 630.3479 | 0.1645 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1057.25 |  | 1046.9987 | 0.9791 | 1001.82 | 982.21 | 0.1277 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 470.79 |  | 469.7577 | 0.2197 | 469.08 | 460.78 | 0.325 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 140.75 |  | 140.8899 | -0.0993 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.195 |  | 166.5024 | 1.0166 | 163.275 | 157.34 | 4.5245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.67 |  | 274.6733 | 1.091 | 269.59 | 256.24 | 1.635 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 736.4 |  | 720.3908 | 2.2223 | 694.98 | 653.305 | 1.3634 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 376.705 |  | 377.5807 | -0.2319 | 375.52 | 359.81 | 4.5394 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.54 |  | 100.7986 | 1.7276 | 97.585 | 91.92 | 2.5161 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 304.045 |  | 304.6312 | -0.1924 | 305.21 | 289.97 | 4.7756 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1761.35 |  | 1756.9102 | 0.2527 | 1741.99 | 1704.935 | 2.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 530.475 |  | 533.6408 | -0.5932 | 535.095 | 513.34 | 0.0961 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 313.02 |  | 312.0799 | 0.3012 | 306.51 | 298.89 | 4.5428 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 213.43 |  | 212.2868 | 0.5385 | 210.82 | 204.71 | 0.0609 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.28 |  | 320.7652 | 1.0957 | 308.03 | 297.18 | 3.9626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 277.26 |  | 277.6716 | -0.1482 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.71 |  | 61.7053 | 1.6282 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.88 |  | 50.0645 | 1.6289 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.02 |  | 135.5905 | 1.7918 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.21 |  | 319.5816 | 1.7612 | 315.89 | 307.13 | 0.2614 | buy_precheck_manual_confirm | none |
| LIN | industrial_gases | 513.265 |  | 517.707 | -0.858 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.19 |  | 298.1857 | -0.6693 | 304.36 | 299.62 | 0.054 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 25.465 |  | 25.1195 | 1.3755 | 25.45 | 24.1 | 0.0393 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 33.39 |  | 33.7231 | -0.9878 | 34 | 32.26 | 0.0299 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.84 |  | 20.6893 | 0.7285 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1386.995 |  | 1425.6674 | -2.7126 | 1393.96 | 1325.48 | 0.535 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 478.28 |  | 468.4313 | 2.1025 | 453.35 | 431.78 | 4.8737 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 787.75 |  | 769.0395 | 2.433 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.19 |  | 247.9106 | -0.2907 | 247.72 | 243.725 | 0.271 | below_vwap | below_vwap |
| META | cloud_ai_capex | 643.075 |  | 642.6259 | 0.0699 | 649.07 | 638.97 | 0.2379 | watch_only | none |
| ARM | ai_accelerator | 267 |  | 261.7756 | 1.9957 | 252.95 | 243.21 | 0.3296 | buy_precheck_manual_confirm | none |
| SKHY | memory_hbm_storage | 153.33 |  | 158.5915 | -3.3176 | 151.99 | 145.6 | 0.3522 | below_vwap | below_vwap,spread_too_wide |
