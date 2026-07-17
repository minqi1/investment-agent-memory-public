# Intraday State

- Generated at: `2026-07-18T00:30:58+08:00`
- Market time ET: `2026-07-17T12:30:59-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 3, 'below_vwap': 2, 'spread_too_wide_or_missing': 36, 'price_stale_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.55 |  | 693.9986 | 0.7999 | 693.36 | 686.78 | 0.0715 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 526.62 |  | 515.4015 | 2.1767 | 511.83 | 498.665 | 0.1272 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.69 |  | 551.9526 | 1.7642 | 550 | 536.9 | 0.0997 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.005 |  | 744.7203 | 0.1725 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.865 |  | 202.6293 | 1.1034 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 561.69 |  | 551.9526 | 1.7642 | 550 | 536.9 | 0.0997 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 526.62 |  | 515.4015 | 2.1767 | 511.83 | 498.665 | 0.1272 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.3 |  | 294.0432 | 0.0873 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.55 |  | 693.9986 | 0.7999 | 693.36 | 686.78 | 0.0715 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46 |  | 45.3946 | 1.3337 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 746.005 |  | 744.7203 | 0.1725 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.36 |  | 247.8971 | 0.1867 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 127.56 |  | 125.3297 | 1.7795 | 125.02 | 121.79 | 0.2195 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.63 |  | 24.1002 | 2.1984 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.8 |  | 20.5192 | 1.3685 | 20.445 | 19.92 | 0.0481 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 68.59 |  | 66.8926 | 2.5374 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.3 |  | 294.0432 | 0.0873 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.36 |  | 247.8971 | 0.1867 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 746.005 |  | 744.7203 | 0.1725 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 699.55 |  | 693.9986 | 0.7999 | 693.36 | 686.78 | 0.0715 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 204.865 |  | 202.6293 | 1.1034 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 6 | APLD | high_beta_ai_infrastructure | 25.085 |  | 24.8955 | 0.7611 | 25.45 | 24.1 | 0.0797 | watch_only | none |
| 7 | HPE | ai_server_oem | 46 |  | 45.3946 | 1.3337 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 20.8 |  | 20.5192 | 1.3685 | 20.445 | 19.92 | 0.0481 | buy_precheck_manual_confirm | none |
| 9 | IREN | high_beta_ai_infrastructure | 33.98 |  | 33.5327 | 1.334 | 34 | 32.26 | 0.0589 | watch_only | none |
| 10 | JCI | data_center_power_cooling | 141.5 |  | 140.7152 | 0.5577 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | GOOGL | cloud_ai_capex | 347.03 |  | 346.1122 | 0.2652 | 348.47 | 341.42 | 0.5245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SMCI | ai_server_oem | 24.63 |  | 24.1002 | 2.1984 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 561.69 |  | 551.9526 | 1.7642 | 550 | 536.9 | 0.0997 | buy_precheck_manual_confirm | none |
| 14 | SOXX | semiconductor_index | 526.62 |  | 515.4015 | 2.1767 | 511.83 | 498.665 | 0.1272 | buy_precheck_manual_confirm | none |
| 15 | TT | data_center_power_cooling | 472.54 |  | 469.3404 | 0.6817 | 469.08 | 460.78 | 3.6568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ORCL | cloud_ai_capex | 127.56 |  | 125.3297 | 1.7795 | 125.02 | 121.79 | 0.2195 | buy_precheck_manual_confirm | none |
| 17 | CRWV | gpu_cloud_ai_factory | 72.155 |  | 71.7682 | 0.5389 | 71.24 | 68.65 | 2.4531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 379.3 |  | 374.8436 | 1.1889 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 402.34 |  | 398.9833 | 0.8413 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.865 |  | 202.6293 | 1.1034 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 561.69 |  | 551.9526 | 1.7642 | 550 | 536.9 | 0.0997 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 526.62 |  | 515.4015 | 2.1767 | 511.83 | 498.665 | 0.1272 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 294.3 |  | 294.0432 | 0.0873 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.55 |  | 693.9986 | 0.7999 | 693.36 | 686.78 | 0.0715 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46 |  | 45.3946 | 1.3337 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 746.005 |  | 744.7203 | 0.1725 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.36 |  | 247.8971 | 0.1867 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 127.56 |  | 125.3297 | 1.7795 | 125.02 | 121.79 | 0.2195 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.63 |  | 24.1002 | 2.1984 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.8 |  | 20.5192 | 1.3685 | 20.445 | 19.92 | 0.0481 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 68.59 |  | 66.8926 | 2.5374 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| 13 | ANET | ai_networking_optical | 168.01 |  | 163.9759 | 2.4602 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TSM | foundry | 401.785 |  | 396.6044 | 1.3062 | 394.11 | 386.02 | 0.3758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AVGO | custom_silicon_networking | 372.415 |  | 368.3984 | 1.0903 | 368.42 | 357.97 | 1.2056 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMAT | semiconductor_equipment | 544.125 |  | 531.6485 | 2.3468 | 535.095 | 513.34 | 0.5146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 499.38 |  | 483.2332 | 3.3414 | 482.43 | 461.04 | 0.5907 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ASML | semiconductor_equipment | 1772.335 |  | 1745.832 | 1.5181 | 1741.99 | 1704.935 | 3.6489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 472.54 |  | 469.3404 | 0.6817 | 469.08 | 460.78 | 3.6568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | KLAC | semiconductor_equipment | 214.085 |  | 211.2157 | 1.3585 | 210.82 | 204.71 | 1.2472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.55 |  | 693.9986 | 0.7999 | 693.36 | 686.78 | 0.0715 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.59 |  | 66.8926 | 2.5374 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.865 |  | 202.6293 | 1.1034 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.655 |  | 392.9386 | -0.0722 | 398.39 | 393.52 | 0.0586 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 331.74 |  | 332.2831 | -0.1634 | 334.98 | 331.295 | 0.6119 | below_vwap | below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 347.03 |  | 346.1122 | 0.2652 | 348.47 | 341.42 | 0.5245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 499.38 |  | 483.2332 | 3.3414 | 482.43 | 461.04 | 0.5907 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 401.785 |  | 396.6044 | 1.3062 | 394.11 | 386.02 | 0.3758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.62 |  | 515.4015 | 2.1767 | 511.83 | 498.665 | 0.1272 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.69 |  | 551.9526 | 1.7642 | 550 | 536.9 | 0.0997 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.415 |  | 368.3984 | 1.0903 | 368.42 | 357.97 | 1.2056 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 884.565 |  | 855.1135 | 3.4442 | 835.82 | 804.09 | 1.1305 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 190.09 |  | 185.2763 | 2.5981 | 185.03 | 178.09 | 1.9201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 394.84 |  | 388.5133 | 1.6284 | 384 | 368.28 | 0.7269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46 |  | 45.3946 | 1.3337 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.63 |  | 24.1002 | 2.1984 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.005 |  | 744.7203 | 0.1725 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.3 |  | 294.0432 | 0.0873 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.56 |  | 125.3297 | 1.7795 | 125.02 | 121.79 | 0.2195 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 72.155 |  | 71.7682 | 0.5389 | 71.24 | 68.65 | 2.4531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 294.325 |  | 284.1452 | 3.5826 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.34 |  | 398.9833 | 0.8413 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.53 |  | 627.3637 | 1.1423 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1052.97 |  | 1039.8042 | 1.2662 | 1001.82 | 982.21 | 1.227 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 472.54 |  | 469.3404 | 0.6817 | 469.08 | 460.78 | 3.6568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.5 |  | 140.7152 | 0.5577 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.01 |  | 163.9759 | 2.4602 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 281.11 |  | 271.7506 | 3.4441 | 269.59 | 256.24 | 1.2024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 728.29 |  | 705.6479 | 3.2087 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 379.3 |  | 374.8436 | 1.1889 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 102.03 |  | 98.9391 | 3.1241 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 308.54 |  | 301.9253 | 2.1908 | 305.21 | 289.97 | 0.7422 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1772.335 |  | 1745.832 | 1.5181 | 1741.99 | 1704.935 | 3.6489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 544.125 |  | 531.6485 | 2.3468 | 535.095 | 513.34 | 0.5146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 317.73 |  | 310.4535 | 2.3438 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.085 |  | 211.2157 | 1.3585 | 210.82 | 204.71 | 1.2472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 321.38 |  | 311.6492 | 3.1224 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.25 |  | 270.9964 | 3.4147 | 265.71 | 258.355 | 4.8671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.615 |  | 60.9034 | 2.8104 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.64 |  | 49.4613 | 2.383 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.23 |  | 133.455 | 2.8287 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.11 |  | 316.4383 | 2.4244 | 315.89 | 307.13 | 0.867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 516.81 |  | 521.2294 | -0.8479 | 526.74 | 522.205 | 4.3207 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 298.265 |  | 300.8348 | -0.8542 | 304.36 | 299.62 | 3.4131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.085 |  | 24.8955 | 0.7611 | 25.45 | 24.1 | 0.0797 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.98 |  | 33.5327 | 1.334 | 34 | 32.26 | 0.0589 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.8 |  | 20.5192 | 1.3685 | 20.445 | 19.92 | 0.0481 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1475.66 |  | 1417.2746 | 4.1196 | 1393.96 | 1325.48 | 2.1983 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 478.35 |  | 456.6627 | 4.7491 | 453.35 | 431.78 | 1.2501 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 780.6 |  | 745.8466 | 4.6596 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.36 |  | 247.8971 | 0.1867 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 643.54 |  | 637.8922 | 0.8854 | 649.07 | 638.97 | 0.6185 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.555 |  | 257.388 | 3.5616 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 163.105 |  | 156.9765 | 3.9041 | 151.99 | 145.6 | 4.727 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
