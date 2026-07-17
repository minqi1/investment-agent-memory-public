# Intraday State

- Generated at: `2026-07-18T03:16:28+08:00`
- Market time ET: `2026-07-17T15:16:29-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 27, 'manual_confirm_candidate': 6, 'watch_only': 3, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.97 |  | 695.6543 | -0.0984 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 519.35 |  | 518.6842 | 0.1284 | 511.83 | 498.665 | 0.0905 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 553.31 |  | 555.2198 | -0.344 | 550 | 536.9 | 0.0181 | below_vwap | below_vwap |
| SPY | market_regime | 742.605 |  | 744.8382 | -0.2998 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 370.61 |  | 370.3959 | 0.0578 | 368.42 | 357.97 | 0.1106 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 519.35 |  | 518.6842 | 0.1284 | 511.83 | 498.665 | 0.0905 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 45.94 |  | 45.7017 | 0.5214 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.395 |  | 24.3216 | 0.3017 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.765 |  | 20.6774 | 0.4239 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 67.37 |  | 67.2458 | 0.1847 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 370.61 |  | 370.3959 | 0.0578 | 368.42 | 357.97 | 0.1106 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 519.35 |  | 518.6842 | 0.1284 | 511.83 | 498.665 | 0.0905 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 24.395 |  | 24.3216 | 0.3017 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.825 |  | 393.5619 | 0.3209 | 398.39 | 393.52 | 0.1292 | watch_only | none |
| 5 | HPE | ai_server_oem | 45.94 |  | 45.7017 | 0.5214 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 20.765 |  | 20.6774 | 0.4239 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.235 |  | 25.1016 | 0.5315 | 25.45 | 24.1 | 0.0793 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 333.65 |  | 332.2826 | 0.4115 | 334.98 | 331.295 | 0.2218 | watch_only | none |
| 9 | GEV | data_center_power_cooling | 1048.32 |  | 1045.5732 | 0.2627 | 1001.82 | 982.21 | 4.1943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ENTG | semiconductor_materials | 135.81 |  | 135.1251 | 0.5069 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TER | semiconductor_test_packaging | 320.94 |  | 320.3052 | 0.1982 | 308.03 | 297.18 | 4.1784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | AMKR | semiconductor_test_packaging | 61.885 |  | 61.604 | 0.4562 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | QQQ | market_regime | 694.97 |  | 695.6543 | -0.0984 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| 14 | TQQQ | leveraged_tool | 67.37 |  | 67.2458 | 0.1847 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 15 | SMH | semiconductor_index | 553.31 |  | 555.2198 | -0.344 | 550 | 536.9 | 0.0181 | below_vwap | below_vwap |
| 16 | IWM | market_regime | 293.17 |  | 294.1228 | -0.3239 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| 17 | COHR | ai_networking_optical | 276.18 |  | 274.1907 | 0.7255 | 269.59 | 256.24 | 4.87 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ANET | ai_networking_optical | 167.75 |  | 166.3019 | 0.8708 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SPY | market_regime | 742.605 |  | 744.8382 | -0.2998 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 20 | GOOGL | cloud_ai_capex | 345.1 |  | 345.7792 | -0.1964 | 348.47 | 341.42 | 0.1101 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 370.61 |  | 370.3959 | 0.0578 | 368.42 | 357.97 | 0.1106 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 519.35 |  | 518.6842 | 0.1284 | 511.83 | 498.665 | 0.0905 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 45.94 |  | 45.7017 | 0.5214 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.395 |  | 24.3216 | 0.3017 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.765 |  | 20.6774 | 0.4239 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 67.37 |  | 67.2458 | 0.1847 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 394.995 |  | 397.9423 | -0.7406 | 394.11 | 386.02 | 2.0253 | below_vwap | below_vwap,spread_too_wide |
| 8 | SMH | semiconductor_index | 553.31 |  | 555.2198 | -0.344 | 550 | 536.9 | 0.0181 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1746.96 |  | 1757.0544 | -0.5745 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | KLAC | semiconductor_equipment | 211.1 |  | 212.2251 | -0.5301 | 210.82 | 204.71 | 4.1971 | below_vwap | below_vwap,spread_too_wide |
| 11 | MU | memory_hbm_storage | 863.29 |  | 864.7179 | -0.1651 | 835.82 | 804.09 | 0.3278 | below_vwap | below_vwap |
| 12 | ETN | data_center_power_cooling | 398.915 |  | 399.7341 | -0.2049 | 389.4 | 382.38 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 630.18 |  | 630.2999 | -0.019 | 616.75 | 609.05 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | QQQ | market_regime | 694.97 |  | 695.6543 | -0.0984 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 309.86 |  | 312.1111 | -0.7212 | 306.51 | 298.89 | 3.3047 | below_vwap | below_vwap,spread_too_wide |
| 16 | ONTO | semiconductor_test_packaging | 277.11 |  | 277.7622 | -0.2348 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1402.74 |  | 1427.5899 | -1.7407 | 1393.96 | 1325.48 | 3.8361 | below_vwap | below_vwap,spread_too_wide |
| 18 | SKHY | memory_hbm_storage | 156.02 |  | 158.9366 | -1.8351 | 151.99 | 145.6 | 1.2434 | below_vwap | below_vwap,spread_too_wide |
| 19 | MRVL | custom_silicon_networking | 187.09 |  | 187.2657 | -0.0938 | 185.03 | 178.09 | 0.2673 | below_vwap | below_vwap |
| 20 | ORCL | cloud_ai_capex | 125.67 |  | 126.0369 | -0.2911 | 125.02 | 121.79 | 1.6074 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.97 |  | 695.6543 | -0.0984 | 693.36 | 686.78 | 0.0058 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.37 |  | 67.2458 | 0.1847 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 201.92 |  | 203.217 | -0.6383 | 203.41 | 197.98 | 0.6933 | below_vwap | below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 394.825 |  | 393.5619 | 0.3209 | 398.39 | 393.52 | 0.1292 | watch_only | none |
| AAPL | mega_cap_platform | 333.65 |  | 332.2826 | 0.4115 | 334.98 | 331.295 | 0.2218 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.1 |  | 345.7792 | -0.1964 | 348.47 | 341.42 | 0.1101 | below_vwap | below_vwap |
| AMD | ai_accelerator | 492.89 |  | 487.0675 | 1.1954 | 482.43 | 461.04 | 2.5219 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.995 |  | 397.9423 | -0.7406 | 394.11 | 386.02 | 2.0253 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 519.35 |  | 518.6842 | 0.1284 | 511.83 | 498.665 | 0.0905 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 553.31 |  | 555.2198 | -0.344 | 550 | 536.9 | 0.0181 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 370.61 |  | 370.3959 | 0.0578 | 368.42 | 357.97 | 0.1106 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 863.29 |  | 864.7179 | -0.1651 | 835.82 | 804.09 | 0.3278 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 187.09 |  | 187.2657 | -0.0938 | 185.03 | 178.09 | 0.2673 | below_vwap | below_vwap |
| DELL | ai_server_oem | 398.13 |  | 393.47 | 1.1843 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.94 |  | 45.7017 | 0.5214 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.395 |  | 24.3216 | 0.3017 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.605 |  | 744.8382 | -0.2998 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.17 |  | 294.1228 | -0.3239 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.67 |  | 126.0369 | -0.2911 | 125.02 | 121.79 | 1.6074 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.83 |  | 72.2787 | 0.7628 | 71.24 | 68.65 | 4.5311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.075 |  | 287.6017 | 0.86 | 280.565 | 273.17 | 3.9852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 398.915 |  | 399.7341 | -0.2049 | 389.4 | 382.38 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 630.18 |  | 630.2999 | -0.019 | 616.75 | 609.05 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1048.32 |  | 1045.5732 | 0.2627 | 1001.82 | 982.21 | 4.1943 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.3 |  | 469.7264 | -0.3037 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.71 |  | 140.9252 | -0.1527 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.75 |  | 166.3019 | 0.8708 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.18 |  | 274.1907 | 0.7255 | 269.59 | 256.24 | 4.87 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 732.84 |  | 719.025 | 1.9213 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 374.975 |  | 377.7451 | -0.7333 | 375.52 | 359.81 | 4.0723 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 101.83 |  | 100.6457 | 1.1767 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 298.97 |  | 304.7586 | -1.8994 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1746.96 |  | 1757.0544 | -0.5745 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 526.81 |  | 534.6327 | -1.4632 | 535.095 | 513.34 | 4.4703 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 309.86 |  | 312.1111 | -0.7212 | 306.51 | 298.89 | 3.3047 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 211.1 |  | 212.2251 | -0.5301 | 210.82 | 204.71 | 4.1971 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 320.94 |  | 320.3052 | 0.1982 | 308.03 | 297.18 | 4.1784 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 277.11 |  | 277.7622 | -0.2348 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.885 |  | 61.604 | 0.4562 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.74 |  | 49.9665 | 1.548 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.81 |  | 135.1251 | 0.5069 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 323.51 |  | 319.1329 | 1.3716 | 315.89 | 307.13 | 3.7248 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.57 |  | 518.5672 | -0.9637 | 526.74 | 522.205 | 0.0389 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 295.73 |  | 298.8331 | -1.0384 | 304.36 | 299.62 | 0.1927 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 25.235 |  | 25.1016 | 0.5315 | 25.45 | 24.1 | 0.0793 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.33 |  | 33.772 | -1.3088 | 34 | 32.26 | 0.03 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.765 |  | 20.6774 | 0.4239 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1402.74 |  | 1427.5899 | -1.7407 | 1393.96 | 1325.48 | 3.8361 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 478.84 |  | 467.7048 | 2.3808 | 453.35 | 431.78 | 4.8075 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 786.75 |  | 764.1943 | 2.9516 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.36 |  | 247.9825 | -0.251 | 247.72 | 243.725 | 0.0162 | below_vwap | below_vwap |
| META | cloud_ai_capex | 641.72 |  | 642.5761 | -0.1332 | 649.07 | 638.97 | 0.6 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 265.79 |  | 261.5287 | 1.6294 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 156.02 |  | 158.9366 | -1.8351 | 151.99 | 145.6 | 1.2434 | below_vwap | below_vwap,spread_too_wide |
