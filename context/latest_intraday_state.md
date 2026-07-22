# Intraday State

- Generated at: `2026-07-23T03:19:01+08:00`
- Market time ET: `2026-07-22T15:19:02-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 20, 'manual_confirm_candidate': 8, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.16 |  | 707.4426 | -0.04 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.68 |  | 554.0895 | 0.8285 | 551.02 | 540.105 | 0.0483 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.11 |  | 586.6135 | 0.5961 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.08 |  | 748.4923 | -0.0551 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.49 |  | 211.6612 | 0.864 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 556.6 |  | 552.6169 | 0.7208 | 548.755 | 526.6 | 0.3288 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 558.27 |  | 556.262 | 0.361 | 548.14 | 526.22 | 0.3135 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.68 |  | 554.0895 | 0.8285 | 551.02 | 540.105 | 0.0483 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.11 |  | 586.6135 | 0.5961 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.01 |  | 211.5367 | 0.2238 | 207.06 | 202.18 | 0.2594 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1802.145 |  | 1799.1944 | 0.164 | 1786.525 | 1767.54 | 0.0855 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 560.955 |  | 558.8532 | 0.3761 | 559.22 | 544.305 | 0.1123 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1802.145 |  | 1799.1944 | 0.164 | 1786.525 | 1767.54 | 0.0855 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 560.955 |  | 558.8532 | 0.3761 | 559.22 | 544.305 | 0.1123 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.11 |  | 586.6135 | 0.5961 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.01 |  | 211.5367 | 0.2238 | 207.06 | 202.18 | 0.2594 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 556.6 |  | 552.6169 | 0.7208 | 548.755 | 526.6 | 0.3288 | buy_precheck_manual_confirm | none |
| 6 | ENTG | semiconductor_materials | 139.25 |  | 138.8788 | 0.2673 | 140.09 | 135.555 | 0.1939 | watch_only | none |
| 7 | WDC | memory_hbm_storage | 558.27 |  | 556.262 | 0.361 | 548.14 | 526.22 | 0.3135 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 474.14 |  | 473.864 | 0.0582 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SOXX | semiconductor_index | 558.68 |  | 554.0895 | 0.8285 | 551.02 | 540.105 | 0.0483 | buy_precheck_manual_confirm | none |
| 10 | LIN | industrial_gases | 509.01 |  | 507.4608 | 0.3053 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | NVDA | ai_accelerator | 213.49 |  | 211.6612 | 0.864 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 12 | ANET | ai_networking_optical | 175.5 |  | 174.9613 | 0.3079 | 175.265 | 171.06 | 2.4387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | MU | memory_hbm_storage | 969.36 |  | 968.4482 | 0.0942 | 963.41 | 936.99 | 1.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TER | semiconductor_test_packaging | 372.01 |  | 371.6585 | 0.0946 | 369.53 | 365 | 5.1074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | KLAC | semiconductor_equipment | 216.68 |  | 216.1641 | 0.2387 | 215.465 | 210.975 | 4.5505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MKSI | semiconductor_materials | 347.615 |  | 345.5246 | 0.605 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ALAB | ai_networking_optical | 330.05 |  | 329.9309 | 0.0361 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | STX | memory_hbm_storage | 911.99 |  | 909.4042 | 0.2843 | 899.59 | 860.605 | 1.0855 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TSM | foundry | 422.74 |  | 421.075 | 0.3954 | 419.42 | 414.87 | 1.0645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.49 |  | 211.6612 | 0.864 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 556.6 |  | 552.6169 | 0.7208 | 548.755 | 526.6 | 0.3288 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 558.27 |  | 556.262 | 0.361 | 548.14 | 526.22 | 0.3135 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.68 |  | 554.0895 | 0.8285 | 551.02 | 540.105 | 0.0483 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.11 |  | 586.6135 | 0.5961 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.01 |  | 211.5367 | 0.2238 | 207.06 | 202.18 | 0.2594 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1802.145 |  | 1799.1944 | 0.164 | 1786.525 | 1767.54 | 0.0855 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 560.955 |  | 558.8532 | 0.3761 | 559.22 | 544.305 | 0.1123 | buy_precheck_manual_confirm | none |
| 9 | QQQ | market_regime | 707.16 |  | 707.4426 | -0.04 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 748.08 |  | 748.4923 | -0.0551 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |
| 11 | AMKR | semiconductor_test_packaging | 67.465 |  | 67.4653 | -0.0005 | 66.73 | 64.98 | 2.0307 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMCI | ai_server_oem | 30.75 |  | 31.1453 | -1.2693 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| 13 | CRWV | gpu_cloud_ai_factory | 83.305 |  | 83.3422 | -0.0446 | 83.22 | 79.6 | 0.3361 | below_vwap | below_vwap |
| 14 | MU | memory_hbm_storage | 969.36 |  | 968.4482 | 0.0942 | 963.41 | 936.99 | 1.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 422.74 |  | 421.075 | 0.3954 | 419.42 | 414.87 | 1.0645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 474.14 |  | 473.864 | 0.0582 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1611.185 |  | 1582.6599 | 1.8024 | 1558.88 | 1518.99 | 0.4227 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 911.99 |  | 909.4042 | 0.2843 | 899.59 | 860.605 | 1.0855 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 372.01 |  | 371.6585 | 0.0946 | 369.53 | 365 | 5.1074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 397.59 |  | 392.1011 | 1.3999 | 387.635 | 380.205 | 0.6313 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.16 |  | 707.4426 | -0.04 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.84 |  | 70.8585 | -0.0261 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.49 |  | 211.6612 | 0.864 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.445 |  | 389.726 | -0.0721 | 400.89 | 392.26 | 0.0308 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.48 |  | 324.9482 | -0.1441 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 345.46 |  | 347.5763 | -0.6089 | 348.76 | 346.23 | 0.0608 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 556.6 |  | 552.6169 | 0.7208 | 548.755 | 526.6 | 0.3288 | buy_precheck_manual_confirm | none |
| TSM | foundry | 422.74 |  | 421.075 | 0.3954 | 419.42 | 414.87 | 1.0645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.68 |  | 554.0895 | 0.8285 | 551.02 | 540.105 | 0.0483 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.11 |  | 586.6135 | 0.5961 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.59 |  | 392.1011 | 1.3999 | 387.635 | 380.205 | 0.6313 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 969.36 |  | 968.4482 | 0.0942 | 963.41 | 936.99 | 1.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.01 |  | 211.5367 | 0.2238 | 207.06 | 202.18 | 0.2594 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 443.53 |  | 442.3763 | 0.2608 | 435.98 | 415.79 | 0.6584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.43 |  | 48.9171 | -0.9958 | 48.96 | 47.01 | 0.0413 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.75 |  | 31.1453 | -1.2693 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| SPY | market_regime | 748.08 |  | 748.4923 | -0.0551 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 293.74 |  | 294.8969 | -0.3923 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.23 |  | 126.4585 | -0.1807 | 128.79 | 125.83 | 1.9567 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.305 |  | 83.3422 | -0.0446 | 83.22 | 79.6 | 0.3361 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 303.48 |  | 299.7206 | 1.2543 | 297.69 | 293.905 | 0.4745 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.755 |  | 407.6846 | -0.228 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.49 |  | 641.6415 | 0.4439 | 641.19 | 628.17 | 3.5796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 994.71 |  | 1004.0669 | -0.9319 | 1036.605 | 998.94 | 1.9101 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.14 |  | 473.864 | 0.0582 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.36 |  | 142.8985 | -0.3768 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.5 |  | 174.9613 | 0.3079 | 175.265 | 171.06 | 2.4387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.85 |  | 316.0067 | -0.0496 | 317.93 | 306.89 | 3.3529 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 831.38 |  | 837.9005 | -0.7782 | 840.47 | 814.62 | 4.7812 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 401.305 |  | 404.9879 | -0.9094 | 407.12 | 397.835 | 1.8814 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.71 |  | 113.9288 | -2.8252 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.05 |  | 329.9309 | 0.0361 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1802.145 |  | 1799.1944 | 0.164 | 1786.525 | 1767.54 | 0.0855 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.955 |  | 558.8532 | 0.3761 | 559.22 | 544.305 | 0.1123 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.185 |  | 319.5752 | 0.5037 | 317.72 | 311.31 | 4.0818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.68 |  | 216.1641 | 0.2387 | 215.465 | 210.975 | 4.5505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.01 |  | 371.6585 | 0.0946 | 369.53 | 365 | 5.1074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.465 |  | 67.4653 | -0.0005 | 66.73 | 64.98 | 2.0307 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.31 |  | 55.597 | -0.5163 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.25 |  | 138.8788 | 0.2673 | 140.09 | 135.555 | 0.1939 | watch_only | none |
| MKSI | semiconductor_materials | 347.615 |  | 345.5246 | 0.605 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.01 |  | 507.4608 | 0.3053 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.44 |  | 297.7902 | -0.4534 | 300.24 | 297.585 | 0.2969 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.07 |  | 30.6638 | -1.9365 | 30.78 | 29.46 | 0.0333 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.45 |  | 42.4351 | -2.3215 | 42.29 | 40.305 | 0.0241 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.6 |  | 23.9785 | -1.5784 | 24.255 | 23.58 | 0.0847 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1611.185 |  | 1582.6599 | 1.8024 | 1558.88 | 1518.99 | 0.4227 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.27 |  | 556.262 | 0.361 | 548.14 | 526.22 | 0.3135 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 911.99 |  | 909.4042 | 0.2843 | 899.59 | 860.605 | 1.0855 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 244.42 |  | 244.1991 | 0.0905 | 248.43 | 244.47 | 0.0818 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 626.135 |  | 630.1256 | -0.6333 | 647.02 | 632.77 | 0.2859 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.16 |  | 285.5778 | -0.1463 | 286.39 | 280.275 | 2.7634 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.09 |  | 166.7257 | -0.3813 | 166.63 | 162.08 | 1.439 | below_vwap | below_vwap,spread_too_wide |
