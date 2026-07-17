# Intraday State

- Generated at: `2026-07-17T22:01:09+08:00`
- Market time ET: `2026-07-17T10:01:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_opening_15m_low': 3, 'spread_too_wide_or_missing': 32, 'price_stale_or_missing': 2, 'below_vwap': 3, 'manual_confirm_candidate': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.32 |  | 689.9147 | 0.4936 | 693.36 | 686.78 | 0.0966 | watch_only | none |
| SOXX | semiconductor_index | 512.54 |  | 507.2417 | 1.0445 | 511.83 | 498.665 | 0.1132 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 549.22 |  | 543.6224 | 1.0297 | 550 | 536.9 | 0.0674 | watch_only | none |
| SPY | market_regime | 744.82 |  | 742.3828 | 0.3283 | 742.66 | 740.8 | 0.0416 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 512.54 |  | 507.2417 | 1.0445 | 511.83 | 498.665 | 0.1132 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.66 |  | 293.4578 | 0.4097 | 294.205 | 291.675 | 0.017 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 44.96 |  | 44.3846 | 1.2963 | 44.92 | 43.715 | 0.1557 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 744.82 |  | 742.3828 | 0.3283 | 742.66 | 740.8 | 0.0416 | buy_precheck_manual_confirm | none |
| 5 | STX | memory_hbm_storage | 726.48 |  | 714.1678 | 1.724 | 724.57 | 702.24 | 0.2904 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 247.94 |  | 246.3541 | 0.6437 | 247.72 | 243.725 | 0.2743 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 744.82 |  | 742.3828 | 0.3283 | 742.66 | 740.8 | 0.0416 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.66 |  | 293.4578 | 0.4097 | 294.205 | 291.675 | 0.017 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 247.94 |  | 246.3541 | 0.6437 | 247.72 | 243.725 | 0.2743 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 512.54 |  | 507.2417 | 1.0445 | 511.83 | 498.665 | 0.1132 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 693.32 |  | 689.9147 | 0.4936 | 693.36 | 686.78 | 0.0966 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 346.48 |  | 344.729 | 0.5079 | 348.47 | 341.42 | 0.2309 | watch_only | none |
| 7 | HPE | ai_server_oem | 44.96 |  | 44.3846 | 1.2963 | 44.92 | 43.715 | 0.1557 | buy_precheck_manual_confirm | none |
| 8 | NVDA | ai_accelerator | 201.715 |  | 199.9707 | 0.8723 | 203.41 | 197.98 | 0.0248 | watch_only | none |
| 9 | SMH | semiconductor_index | 549.22 |  | 543.6224 | 1.0297 | 550 | 536.9 | 0.0674 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 209.59 |  | 207.8226 | 0.8504 | 210.82 | 204.71 | 0.1384 | watch_only | none |
| 11 | SMCI | ai_server_oem | 24.04 |  | 23.6979 | 1.4438 | 24.3 | 23.46 | 0.0832 | watch_only | none |
| 12 | CRWV | gpu_cloud_ai_factory | 70.515 |  | 69.6027 | 1.3107 | 71.24 | 68.65 | 0.1418 | watch_only | none |
| 13 | AVGO | custom_silicon_networking | 365.01 |  | 362.417 | 0.7155 | 368.42 | 357.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | APLD | high_beta_ai_infrastructure | 24.84 |  | 24.5018 | 1.3804 | 25.45 | 24.1 | 0.1208 | watch_only | none |
| 15 | STX | memory_hbm_storage | 726.48 |  | 714.1678 | 1.724 | 724.57 | 702.24 | 0.2904 | buy_precheck_manual_confirm | none |
| 16 | MKSI | semiconductor_materials | 312.8 |  | 310.7555 | 0.6579 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AMAT | semiconductor_equipment | 525.16 |  | 522.0822 | 0.5895 | 535.095 | 513.34 | 3.7531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ASML | semiconductor_equipment | 1731.615 |  | 1723.2004 | 0.4883 | 1741.99 | 1704.935 | 0.5636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 468.58 |  | 465.9417 | 0.5662 | 469.08 | 460.78 | 4.456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | IREN | high_beta_ai_infrastructure | 33.645 |  | 32.941 | 2.137 | 34 | 32.26 | 0.0892 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 512.54 |  | 507.2417 | 1.0445 | 511.83 | 498.665 | 0.1132 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.66 |  | 293.4578 | 0.4097 | 294.205 | 291.675 | 0.017 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 44.96 |  | 44.3846 | 1.2963 | 44.92 | 43.715 | 0.1557 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 744.82 |  | 742.3828 | 0.3283 | 742.66 | 740.8 | 0.0416 | buy_precheck_manual_confirm | none |
| 5 | STX | memory_hbm_storage | 726.48 |  | 714.1678 | 1.724 | 724.57 | 702.24 | 0.2904 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 247.94 |  | 246.3541 | 0.6437 | 247.72 | 243.725 | 0.2743 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 394.6 |  | 390.048 | 1.167 | 394.11 | 386.02 | 4.0547 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | MU | memory_hbm_storage | 843.48 |  | 824.0341 | 2.3598 | 835.82 | 804.09 | 1.3326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | VRT | data_center_power_cooling | 282.02 |  | 277.1221 | 1.7674 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 394.35 |  | 388.7691 | 1.4355 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | GEV | data_center_power_cooling | 1031.72 |  | 1005.8665 | 2.5703 | 1001.82 | 982.21 | 4.7474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | PWR | data_center_power_cooling | 620.065 |  | 615.0986 | 0.8074 | 616.75 | 609.05 | 0.7193 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | LRCX | semiconductor_equipment | 306.835 |  | 301.9359 | 1.6226 | 306.51 | 298.89 | 3.9109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | NVDA | ai_accelerator | 201.715 |  | 199.9707 | 0.8723 | 203.41 | 197.98 | 0.0248 | watch_only | none |
| 15 | ARM | ai_accelerator | 254.74 |  | 248.508 | 2.5078 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ENTG | semiconductor_materials | 132.415 |  | 129.5724 | 2.1938 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SMH | semiconductor_index | 549.22 |  | 543.6224 | 1.0297 | 550 | 536.9 | 0.0674 | watch_only | none |
| 18 | TER | semiconductor_test_packaging | 309.54 |  | 302.2288 | 2.4191 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SKHY | memory_hbm_storage | 157.22 |  | 150.4562 | 4.4955 | 151.99 | 145.6 | 1.164 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | KLAC | semiconductor_equipment | 209.59 |  | 207.8226 | 0.8504 | 210.82 | 204.71 | 0.1384 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.32 |  | 689.9147 | 0.4936 | 693.36 | 686.78 | 0.0966 | watch_only | none |
| TQQQ | leveraged_tool | 66.87 |  | 65.7514 | 1.7012 | 66.9 | 64.92 | 0.0449 | watch_only | none |
| NVDA | ai_accelerator | 201.715 |  | 199.9707 | 0.8723 | 203.41 | 197.98 | 0.0248 | watch_only | none |
| MSFT | cloud_ai_capex | 393.11 |  | 395.3442 | -0.5651 | 398.39 | 393.52 | 0.0712 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.94 |  | 333.0531 | -0.6345 | 334.98 | 331.295 | 1.0455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 346.48 |  | 344.729 | 0.5079 | 348.47 | 341.42 | 0.2309 | watch_only | none |
| AMD | ai_accelerator | 475.885 |  | 468.4318 | 1.5911 | 482.43 | 461.04 | 1.1999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.6 |  | 390.048 | 1.167 | 394.11 | 386.02 | 4.0547 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 512.54 |  | 507.2417 | 1.0445 | 511.83 | 498.665 | 0.1132 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 549.22 |  | 543.6224 | 1.0297 | 550 | 536.9 | 0.0674 | watch_only | none |
| AVGO | custom_silicon_networking | 365.01 |  | 362.417 | 0.7155 | 368.42 | 357.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 843.48 |  | 824.0341 | 2.3598 | 835.82 | 804.09 | 1.3326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 184.49 |  | 181.2468 | 1.7894 | 185.03 | 178.09 | 1.6749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 383.54 |  | 375.388 | 2.1716 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.96 |  | 44.3846 | 1.2963 | 44.92 | 43.715 | 0.1557 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.04 |  | 23.6979 | 1.4438 | 24.3 | 23.46 | 0.0832 | watch_only | none |
| SPY | market_regime | 744.82 |  | 742.3828 | 0.3283 | 742.66 | 740.8 | 0.0416 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.66 |  | 293.4578 | 0.4097 | 294.205 | 291.675 | 0.017 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 124.81 |  | 123.5499 | 1.0199 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 70.515 |  | 69.6027 | 1.3107 | 71.24 | 68.65 | 0.1418 | watch_only | none |
| VRT | data_center_power_cooling | 282.02 |  | 277.1221 | 1.7674 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 394.35 |  | 388.7691 | 1.4355 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 620.065 |  | 615.0986 | 0.8074 | 616.75 | 609.05 | 0.7193 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1031.72 |  | 1005.8665 | 2.5703 | 1001.82 | 982.21 | 4.7474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.58 |  | 465.9417 | 0.5662 | 469.08 | 460.78 | 4.456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.48 |  | 138.9625 | 1.092 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 163.17 |  | 160.7124 | 1.5292 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 268.85 |  | 263.8244 | 1.9049 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 691.36 |  | 671.7383 | 2.921 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 374.44 |  | 365.9886 | 2.3092 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 97.6 |  | 94.2661 | 3.5367 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 301.89 |  | 296.9592 | 1.6604 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1731.615 |  | 1723.2004 | 0.4883 | 1741.99 | 1704.935 | 0.5636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 525.16 |  | 522.0822 | 0.5895 | 535.095 | 513.34 | 3.7531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 306.835 |  | 301.9359 | 1.6226 | 306.51 | 298.89 | 3.9109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 209.59 |  | 207.8226 | 0.8504 | 210.82 | 204.71 | 0.1384 | watch_only | none |
| TER | semiconductor_test_packaging | 309.54 |  | 302.2288 | 2.4191 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 264.56 |  | 261.172 | 1.2972 | 265.71 | 258.355 | 4.4111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 59.92 |  | 58.8465 | 1.8243 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 48.2 |  | 47.6531 | 1.1476 | 48.92 | 46.44 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 132.415 |  | 129.5724 | 2.1938 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 312.8 |  | 310.7555 | 0.6579 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 520.58 |  | 523.8644 | -0.627 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.68 |  | 302.0233 | -0.1137 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 24.84 |  | 24.5018 | 1.3804 | 25.45 | 24.1 | 0.1208 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.645 |  | 32.941 | 2.137 | 34 | 32.26 | 0.0892 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.56 |  | 20.1178 | 2.1979 | 20.445 | 19.92 | 0.4864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SNDK | memory_hbm_storage | 1389.55 |  | 1360.688 | 2.1211 | 1393.96 | 1325.48 | 4.531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 446.73 |  | 440.2291 | 1.4767 | 453.35 | 431.78 | 0.4119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 726.48 |  | 714.1678 | 1.724 | 724.57 | 702.24 | 0.2904 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.94 |  | 246.3541 | 0.6437 | 247.72 | 243.725 | 0.2743 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 642.27 |  | 642.3753 | -0.0164 | 649.07 | 638.97 | 0.5901 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 254.74 |  | 248.508 | 2.5078 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 157.22 |  | 150.4562 | 4.4955 | 151.99 | 145.6 | 1.164 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
