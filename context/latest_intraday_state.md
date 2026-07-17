# Intraday State

- Generated at: `2026-07-18T00:18:54+08:00`
- Market time ET: `2026-07-17T12:18:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 4, 'spread_too_wide_or_missing': 35, 'price_stale_or_missing': 1, 'below_vwap': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.665 |  | 693.8177 | 0.8428 | 693.36 | 686.78 | 0.0214 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 528.27 |  | 515.0713 | 2.5625 | 511.83 | 498.665 | 0.0909 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 562.94 |  | 551.5116 | 2.0722 | 550 | 536.9 | 0.0853 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.28 |  | 744.6704 | 0.2161 | 742.66 | 740.8 | 0.0241 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.985 |  | 202.5527 | 1.2008 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 562.94 |  | 551.5116 | 2.0722 | 550 | 536.9 | 0.0853 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 528.27 |  | 515.0713 | 2.5625 | 511.83 | 498.665 | 0.0909 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 215.125 |  | 211.0861 | 1.9134 | 210.82 | 204.71 | 0.2743 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 885.78 |  | 854.3089 | 3.6838 | 835.82 | 804.09 | 0.2055 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 294.81 |  | 294.0314 | 0.2648 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 699.665 |  | 693.8177 | 0.8428 | 693.36 | 686.78 | 0.0214 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46 |  | 45.3751 | 1.3771 | 44.92 | 43.715 | 0.0652 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 746.28 |  | 744.6704 | 0.2161 | 742.66 | 740.8 | 0.0241 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.38 |  | 247.8814 | 0.2011 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.57 |  | 24.0725 | 2.0666 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.755 |  | 20.5009 | 1.2393 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.8 |  | 66.8566 | 2.9069 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.81 |  | 294.0314 | 0.2648 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.38 |  | 247.8814 | 0.2011 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 746.28 |  | 744.6704 | 0.2161 | 742.66 | 740.8 | 0.0241 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 204.985 |  | 202.5527 | 1.2008 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 699.665 |  | 693.8177 | 0.8428 | 693.36 | 686.78 | 0.0214 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46 |  | 45.3751 | 1.3771 | 44.92 | 43.715 | 0.0652 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.755 |  | 20.5009 | 1.2393 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 8 | IREN | high_beta_ai_infrastructure | 33.95 |  | 33.5093 | 1.3152 | 34 | 32.26 | 0.0589 | watch_only | none |
| 9 | GOOGL | cloud_ai_capex | 346.53 |  | 346.087 | 0.128 | 348.47 | 341.42 | 1.3274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMCI | ai_server_oem | 24.57 |  | 24.0725 | 2.0666 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 562.94 |  | 551.5116 | 2.0722 | 550 | 536.9 | 0.0853 | buy_precheck_manual_confirm | none |
| 12 | SOXX | semiconductor_index | 528.27 |  | 515.0713 | 2.5625 | 511.83 | 498.665 | 0.0909 | buy_precheck_manual_confirm | none |
| 13 | KLAC | semiconductor_equipment | 215.125 |  | 211.0861 | 1.9134 | 210.82 | 204.71 | 0.2743 | buy_precheck_manual_confirm | none |
| 14 | MU | memory_hbm_storage | 885.78 |  | 854.3089 | 3.6838 | 835.82 | 804.09 | 0.2055 | buy_precheck_manual_confirm | none |
| 15 | APLD | high_beta_ai_infrastructure | 25.32 |  | 24.8779 | 1.7769 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| 16 | ALAB | ai_networking_optical | 305.92 |  | 301.7217 | 1.3914 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | TT | data_center_power_cooling | 473.54 |  | 469.2945 | 0.9047 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 142.29 |  | 140.7127 | 1.121 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 402.93 |  | 398.6322 | 1.0781 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.985 |  | 202.5527 | 1.2008 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 562.94 |  | 551.5116 | 2.0722 | 550 | 536.9 | 0.0853 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 528.27 |  | 515.0713 | 2.5625 | 511.83 | 498.665 | 0.0909 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 215.125 |  | 211.0861 | 1.9134 | 210.82 | 204.71 | 0.2743 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 885.78 |  | 854.3089 | 3.6838 | 835.82 | 804.09 | 0.2055 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 294.81 |  | 294.0314 | 0.2648 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 699.665 |  | 693.8177 | 0.8428 | 693.36 | 686.78 | 0.0214 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46 |  | 45.3751 | 1.3771 | 44.92 | 43.715 | 0.0652 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 746.28 |  | 744.6704 | 0.2161 | 742.66 | 740.8 | 0.0241 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.38 |  | 247.8814 | 0.2011 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.57 |  | 24.0725 | 2.0666 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.755 |  | 20.5009 | 1.2393 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.8 |  | 66.8566 | 2.9069 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 168.275 |  | 163.6405 | 2.8321 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 402.8 |  | 396.3632 | 1.624 | 394.11 | 386.02 | 1.435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 372.61 |  | 368.3099 | 1.1675 | 368.42 | 357.97 | 1.205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 547.285 |  | 530.7183 | 3.1216 | 535.095 | 513.34 | 4.8256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 501.41 |  | 482.992 | 3.8133 | 482.43 | 461.04 | 0.9752 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1786.355 |  | 1744.6115 | 2.3927 | 1741.99 | 1704.935 | 1.0491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 473.54 |  | 469.2945 | 0.9047 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.665 |  | 693.8177 | 0.8428 | 693.36 | 686.78 | 0.0214 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.8 |  | 66.8566 | 2.9069 | 66.9 | 64.92 | 0.0291 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.985 |  | 202.5527 | 1.2008 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.92 |  | 392.961 | -0.0104 | 398.39 | 393.52 | 0.1832 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.81 |  | 332.3463 | -0.4623 | 334.98 | 331.295 | 0.2207 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.53 |  | 346.087 | 0.128 | 348.47 | 341.42 | 1.3274 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 501.41 |  | 482.992 | 3.8133 | 482.43 | 461.04 | 0.9752 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 402.8 |  | 396.3632 | 1.624 | 394.11 | 386.02 | 1.435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.27 |  | 515.0713 | 2.5625 | 511.83 | 498.665 | 0.0909 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 562.94 |  | 551.5116 | 2.0722 | 550 | 536.9 | 0.0853 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.61 |  | 368.3099 | 1.1675 | 368.42 | 357.97 | 1.205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 885.78 |  | 854.3089 | 3.6838 | 835.82 | 804.09 | 0.2055 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 190.77 |  | 185.158 | 3.0309 | 185.03 | 178.09 | 0.3512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 397.36 |  | 388.2044 | 2.3585 | 384 | 368.28 | 3.2716 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46 |  | 45.3751 | 1.3771 | 44.92 | 43.715 | 0.0652 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.57 |  | 24.0725 | 2.0666 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.28 |  | 744.6704 | 0.2161 | 742.66 | 740.8 | 0.0241 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.81 |  | 294.0314 | 0.2648 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.31 |  | 125.2566 | 1.6394 | 125.02 | 121.79 | 2.0187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.56 |  | 71.7299 | 2.5514 | 71.24 | 68.65 | 2.9908 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 295.63 |  | 283.6867 | 4.21 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.93 |  | 398.6322 | 1.0781 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 635.94 |  | 627.1517 | 1.4013 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1060 |  | 1039.1865 | 2.0029 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 473.54 |  | 469.2945 | 0.9047 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.29 |  | 140.7127 | 1.121 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.275 |  | 163.6405 | 2.8321 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 282.24 |  | 271.2248 | 4.0613 | 269.59 | 256.24 | 4.5883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 735.305 |  | 705.0138 | 4.2965 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 383.505 |  | 374.5243 | 2.3979 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.43 |  | 98.8857 | 4.5955 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 305.92 |  | 301.7217 | 1.3914 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1786.355 |  | 1744.6115 | 2.3927 | 1741.99 | 1704.935 | 1.0491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 547.285 |  | 530.7183 | 3.1216 | 535.095 | 513.34 | 4.8256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.5 |  | 309.9777 | 3.3945 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.125 |  | 211.0861 | 1.9134 | 210.82 | 204.71 | 0.2743 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.34 |  | 310.9284 | 4.3134 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 281.19 |  | 268.992 | 4.5347 | 265.71 | 258.355 | 4.7192 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 63.02 |  | 60.82 | 3.6173 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.01 |  | 49.416 | 3.2256 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.48 |  | 133.2073 | 3.9582 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.55 |  | 316.2706 | 2.934 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 517.03 |  | 521.371 | -0.8326 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 298.79 |  | 301.0828 | -0.7615 | 304.36 | 299.62 | 3.4807 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.32 |  | 24.8779 | 1.7769 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.95 |  | 33.5093 | 1.3152 | 34 | 32.26 | 0.0589 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.755 |  | 20.5009 | 1.2393 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1490.16 |  | 1416.2293 | 5.2203 | 1393.96 | 1325.48 | 0.7046 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 479.84 |  | 455.4477 | 5.3557 | 453.35 | 431.78 | 1.1941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 782.8 |  | 743.1852 | 5.3304 | 724.57 | 702.24 | 4.1952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.38 |  | 247.8814 | 0.2011 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 642.71 |  | 635.2222 | 1.1788 | 649.07 | 638.97 | 4.2508 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.25 |  | 256.8046 | 3.6781 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 164.96 |  | 156.7378 | 5.2459 | 151.99 | 145.6 | 1.8126 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
