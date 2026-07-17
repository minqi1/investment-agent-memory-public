# Intraday State

- Generated at: `2026-07-18T02:44:09+08:00`
- Market time ET: `2026-07-17T14:44:10-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'below_vwap': 14, 'watch_only': 3, 'spread_too_wide_or_missing': 27, 'price_stale_or_missing': 2, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.37 |  | 695.555 | 0.1172 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 522.27 |  | 518.4622 | 0.7345 | 511.83 | 498.665 | 0.0938 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.07 |  | 555.1086 | 0.1732 | 550 | 536.9 | 0.0234 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.28 |  | 744.8992 | -0.2174 | 742.66 | 740.8 | 0.0108 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.07 |  | 555.1086 | 0.1732 | 550 | 536.9 | 0.0234 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 522.27 |  | 518.4622 | 0.7345 | 511.83 | 498.665 | 0.0938 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1053.98 |  | 1045.1374 | 0.8461 | 1001.82 | 982.21 | 0.2192 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 696.37 |  | 695.555 | 0.1172 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.18 |  | 45.6673 | 1.1227 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.52 |  | 24.3105 | 0.8617 | 24.3 | 23.46 | 0.0816 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6613 | 1.5427 | 20.445 | 19.92 | 0.0477 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 67.8 |  | 67.2134 | 0.8728 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.37 |  | 695.555 | 0.1172 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.07 |  | 555.1086 | 0.1732 | 550 | 536.9 | 0.0234 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 394.425 |  | 393.3972 | 0.2613 | 398.39 | 393.52 | 0.142 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 333.03 |  | 332.0096 | 0.3073 | 334.98 | 331.295 | 0.1261 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 25.165 |  | 25.0909 | 0.2955 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| 6 | SOXX | semiconductor_index | 522.27 |  | 518.4622 | 0.7345 | 511.83 | 498.665 | 0.0938 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.52 |  | 24.3105 | 0.8617 | 24.3 | 23.46 | 0.0816 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 46.18 |  | 45.6673 | 1.1227 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 9 | GEV | data_center_power_cooling | 1053.98 |  | 1045.1374 | 0.8461 | 1001.82 | 982.21 | 0.2192 | buy_precheck_manual_confirm | none |
| 10 | KLAC | semiconductor_equipment | 212.35 |  | 212.2033 | 0.0691 | 210.82 | 204.71 | 4.8693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ETN | data_center_power_cooling | 400.46 |  | 399.772 | 0.1721 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 278.02 |  | 277.6685 | 0.1266 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ASML | semiconductor_equipment | 1760.29 |  | 1757.0161 | 0.1863 | 1741.99 | 1704.935 | 2.8115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | PWR | data_center_power_cooling | 633.235 |  | 630.079 | 0.5009 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6613 | 1.5427 | 20.445 | 19.92 | 0.0477 | buy_precheck_manual_confirm | none |
| 16 | META | cloud_ai_capex | 646.32 |  | 642.3975 | 0.6106 | 649.07 | 638.97 | 1.2037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 372.16 |  | 370.2496 | 0.516 | 368.42 | 357.97 | 2.2087 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ORCL | cloud_ai_capex | 126.5 |  | 126.027 | 0.3753 | 125.02 | 121.79 | 3.1383 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MU | memory_hbm_storage | 870.27 |  | 864.3036 | 0.6903 | 835.82 | 804.09 | 1.1663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SPY | market_regime | 743.28 |  | 744.8992 | -0.2174 | 742.66 | 740.8 | 0.0108 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.07 |  | 555.1086 | 0.1732 | 550 | 536.9 | 0.0234 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 522.27 |  | 518.4622 | 0.7345 | 511.83 | 498.665 | 0.0938 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1053.98 |  | 1045.1374 | 0.8461 | 1001.82 | 982.21 | 0.2192 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 696.37 |  | 695.555 | 0.1172 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.18 |  | 45.6673 | 1.1227 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 24.52 |  | 24.3105 | 0.8617 | 24.3 | 23.46 | 0.0816 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6613 | 1.5427 | 20.445 | 19.92 | 0.0477 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 67.8 |  | 67.2134 | 0.8728 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 396.32 |  | 398.0824 | -0.4427 | 394.11 | 386.02 | 0.3684 | below_vwap | below_vwap,spread_too_wide |
| 10 | TT | data_center_power_cooling | 469.23 |  | 469.7843 | -0.118 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | CIEN | ai_networking_optical | 376.37 |  | 377.8345 | -0.3876 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | LRCX | semiconductor_equipment | 311.72 |  | 312.1238 | -0.1294 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | SPY | market_regime | 743.28 |  | 744.8992 | -0.2174 | 742.66 | 740.8 | 0.0108 | below_vwap | below_vwap |
| 14 | SNDK | memory_hbm_storage | 1412.36 |  | 1428.1264 | -1.104 | 1393.96 | 1325.48 | 4.2659 | below_vwap | below_vwap,spread_too_wide |
| 15 | ANET | ai_networking_optical | 168.42 |  | 166.1583 | 1.3611 | 163.275 | 157.34 | 4.7144 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 372.16 |  | 370.2496 | 0.516 | 368.42 | 357.97 | 2.2087 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 494.85 |  | 486.7779 | 1.6583 | 482.43 | 461.04 | 2.8392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ASML | semiconductor_equipment | 1760.29 |  | 1757.0161 | 0.1863 | 1741.99 | 1704.935 | 2.8115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | KLAC | semiconductor_equipment | 212.35 |  | 212.2033 | 0.0691 | 210.82 | 204.71 | 4.8693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MU | memory_hbm_storage | 870.27 |  | 864.3036 | 0.6903 | 835.82 | 804.09 | 1.1663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.37 |  | 695.555 | 0.1172 | 693.36 | 686.78 | 0.0072 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.8 |  | 67.2134 | 0.8728 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.95 |  | 203.2424 | -0.1439 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.425 |  | 393.3972 | 0.2613 | 398.39 | 393.52 | 0.142 | watch_only | none |
| AAPL | mega_cap_platform | 333.03 |  | 332.0096 | 0.3073 | 334.98 | 331.295 | 0.1261 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.67 |  | 345.8205 | -0.3327 | 348.47 | 341.42 | 0.119 | below_vwap | below_vwap |
| AMD | ai_accelerator | 494.85 |  | 486.7779 | 1.6583 | 482.43 | 461.04 | 2.8392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.32 |  | 398.0824 | -0.4427 | 394.11 | 386.02 | 0.3684 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 522.27 |  | 518.4622 | 0.7345 | 511.83 | 498.665 | 0.0938 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.07 |  | 555.1086 | 0.1732 | 550 | 536.9 | 0.0234 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.16 |  | 370.2496 | 0.516 | 368.42 | 357.97 | 2.2087 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 870.27 |  | 864.3036 | 0.6903 | 835.82 | 804.09 | 1.1663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 188.83 |  | 187.1669 | 0.8886 | 185.03 | 178.09 | 0.6196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 400.49 |  | 393.0165 | 1.9016 | 384 | 368.28 | 2.6842 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.18 |  | 45.6673 | 1.1227 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.52 |  | 24.3105 | 0.8617 | 24.3 | 23.46 | 0.0816 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.28 |  | 744.8992 | -0.2174 | 742.66 | 740.8 | 0.0108 | below_vwap | below_vwap |
| IWM | market_regime | 293.43 |  | 294.1625 | -0.249 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.5 |  | 126.027 | 0.3753 | 125.02 | 121.79 | 3.1383 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.375 |  | 72.2184 | 1.6015 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 291.38 |  | 287.3309 | 1.4092 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.46 |  | 399.772 | 0.1721 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 633.235 |  | 630.079 | 0.5009 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1053.98 |  | 1045.1374 | 0.8461 | 1001.82 | 982.21 | 0.2192 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 469.23 |  | 469.7843 | -0.118 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.835 |  | 140.9586 | -0.0877 | 140.765 | 137.165 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ANET | ai_networking_optical | 168.42 |  | 166.1583 | 1.3611 | 163.275 | 157.34 | 4.7144 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.34 |  | 274.0241 | 1.2101 | 269.59 | 256.24 | 3.3317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 733.03 |  | 717.734 | 2.1311 | 694.98 | 653.305 | 2.431 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 376.37 |  | 377.8345 | -0.3876 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.245 |  | 100.556 | 1.6797 | 97.585 | 91.92 | 4.3425 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 304.1 |  | 305.2069 | -0.3627 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1760.29 |  | 1757.0161 | 0.1863 | 1741.99 | 1704.935 | 2.8115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.9 |  | 535.2448 | -0.6249 | 535.095 | 513.34 | 0.2237 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 311.72 |  | 312.1238 | -0.1294 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.35 |  | 212.2033 | 0.0691 | 210.82 | 204.71 | 4.8693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 323.095 |  | 320.0002 | 0.9671 | 308.03 | 297.18 | 4.6055 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 278.02 |  | 277.6685 | 0.1266 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.31 |  | 61.5075 | 1.3047 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.89 |  | 49.911 | 1.9616 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.03 |  | 134.825 | 1.6355 | 129.93 | 126.945 | 4.1597 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 323.415 |  | 318.8227 | 1.4404 | 315.89 | 307.13 | 3.899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.425 |  | 519.8678 | -0.8546 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.38 |  | 298.933 | -0.854 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.165 |  | 25.0909 | 0.2955 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.58 |  | 33.7898 | -0.621 | 34 | 32.26 | 0.0596 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.98 |  | 20.6613 | 1.5427 | 20.445 | 19.92 | 0.0477 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1412.36 |  | 1428.1264 | -1.104 | 1393.96 | 1325.48 | 4.2659 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.78 |  | 467.1636 | 2.9147 | 453.35 | 431.78 | 4.4095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 787.265 |  | 760.8463 | 3.4723 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.545 |  | 248.0033 | -0.1848 | 247.72 | 243.725 | 0.0121 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.32 |  | 642.3975 | 0.6106 | 649.07 | 638.97 | 1.2037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.7 |  | 261.173 | 2.1162 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 161.015 |  | 158.8251 | 1.3788 | 151.99 | 145.6 | 3.0618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
