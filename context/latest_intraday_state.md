# Intraday State

- Generated at: `2026-07-30T23:41:06+08:00`
- Market time ET: `2026-07-30T11:41:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `56`
- stale_count: `0`
- coverage_price: `54`
- coverage_vwap: `54`
- caution_counts: `{'manual_confirm_candidate': 9, 'below_vwap': 21, 'watch_only': 3, 'spread_too_wide_or_missing': 17, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 679.26 |  | 678.7914 | 0.069 | 677.685 | 673.43 | 0.0427 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 502.31 |  | 500.7034 | 0.3209 | 495.01 | 488.29 | 0.0856 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 535.81 |  | 535.888 | -0.0146 | 530.605 | 524.56 | 0.0541 | below_vwap | below_vwap |
| SPY | market_regime | 735.885 |  | 736.9323 | -0.1421 | 736.77 | 734.67 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 400.1 |  | 399.5683 | 0.1331 | 396.93 | 387.975 | 0.195 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 502.31 |  | 500.7034 | 0.3209 | 495.01 | 488.29 | 0.0856 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 679.26 |  | 678.7914 | 0.069 | 677.685 | 673.43 | 0.0427 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 181.96 |  | 180.3402 | 0.8982 | 178.81 | 175.265 | 0.2308 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 237.39 |  | 236.0085 | 0.5853 | 235.12 | 231.205 | 0.1938 | buy_precheck_manual_confirm | none |
| 6 | DELL | ai_server_oem | 406.59 |  | 405.7976 | 0.1953 | 397.47 | 383.67 | 0.2263 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 27.84 |  | 27.6853 | 0.5589 | 27.29 | 26.68 | 0.0718 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 27.84 |  | 27.7184 | 0.4386 | 27.29 | 25.36 | 0.1078 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 62.39 |  | 62.3496 | 0.0649 | 61.885 | 60.76 | 0.0321 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 679.26 |  | 678.7914 | 0.069 | 677.685 | 673.43 | 0.0427 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 400.1 |  | 399.5683 | 0.1331 | 396.93 | 387.975 | 0.195 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 502.31 |  | 500.7034 | 0.3209 | 495.01 | 488.29 | 0.0856 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 532.91 |  | 532.1971 | 0.134 | 536.38 | 524.49 | 0.0676 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 448.485 |  | 447.0169 | 0.3284 | 451.36 | 432.44 | 0.2386 | watch_only | none |
| 6 | DELL | ai_server_oem | 406.59 |  | 405.7976 | 0.1953 | 397.47 | 383.67 | 0.2263 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 21.805 |  | 21.7983 | 0.0309 | 22.06 | 19.77 | 0.321 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 237.39 |  | 236.0085 | 0.5853 | 235.12 | 231.205 | 0.1938 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 27.84 |  | 27.6853 | 0.5589 | 27.29 | 26.68 | 0.0718 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 27.84 |  | 27.7184 | 0.4386 | 27.29 | 25.36 | 0.1078 | buy_precheck_manual_confirm | none |
| 11 | COHR | ai_networking_optical | 245.23 |  | 245.1913 | 0.0158 | 246.07 | 239.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | CIEN | ai_networking_optical | 363.54 |  | 362.5612 | 0.27 | 362.94 | 355.69 | 1.4744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | COHU | semiconductor_test_packaging | 44.77 |  | 44.6117 | 0.3547 | 44.64 | 43.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | MRVL | custom_silicon_networking | 181.96 |  | 180.3402 | 0.8982 | 178.81 | 175.265 | 0.2308 | buy_precheck_manual_confirm | none |
| 15 | AMAT | semiconductor_equipment | 497.07 |  | 496.3608 | 0.1429 | 493.605 | 476.45 | 4.3636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TER | semiconductor_test_packaging | 355.63 |  | 355.019 | 0.1721 | 353.04 | 345.01 | 0.8408 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ONTO | semiconductor_test_packaging | 248.14 |  | 247.2616 | 0.3553 | 249.235 | 239.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | LITE | ai_networking_optical | 679.4 |  | 677.777 | 0.2395 | 673.79 | 651.04 | 1.8075 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | HPE | ai_server_oem | 46.685 |  | 46.4756 | 0.4505 | 46.415 | 45.48 | 2.7204 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 483.72 |  | 481.3096 | 0.5008 | 472.15 | 457.835 | 3.0389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 400.1 |  | 399.5683 | 0.1331 | 396.93 | 387.975 | 0.195 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 502.31 |  | 500.7034 | 0.3209 | 495.01 | 488.29 | 0.0856 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 679.26 |  | 678.7914 | 0.069 | 677.685 | 673.43 | 0.0427 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 181.96 |  | 180.3402 | 0.8982 | 178.81 | 175.265 | 0.2308 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 406.59 |  | 405.7976 | 0.1953 | 397.47 | 383.67 | 0.2263 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 237.39 |  | 236.0085 | 0.5853 | 235.12 | 231.205 | 0.1938 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 27.84 |  | 27.6853 | 0.5589 | 27.29 | 26.68 | 0.0718 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 27.84 |  | 27.7184 | 0.4386 | 27.29 | 25.36 | 0.1078 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 62.39 |  | 62.3496 | 0.0649 | 61.885 | 60.76 | 0.0321 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 382.94 |  | 384.3783 | -0.3742 | 382.725 | 377.85 | 3.9171 | below_vwap | below_vwap,spread_too_wide |
| 11 | SMH | semiconductor_index | 535.81 |  | 535.888 | -0.0146 | 530.605 | 524.56 | 0.0541 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1656.815 |  | 1657.6354 | -0.0495 | 1645.515 | 1626.61 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | WDC | memory_hbm_storage | 530.92 |  | 532.3777 | -0.2738 | 526.8 | 507.21 | 1.8986 | below_vwap | below_vwap,spread_too_wide |
| 14 | ANET | ai_networking_optical | 169.04 |  | 169.4843 | -0.2621 | 168.42 | 165.88 | 4.076 | below_vwap | below_vwap,spread_too_wide |
| 15 | ORCL | cloud_ai_capex | 125.415 |  | 125.759 | -0.2735 | 124.935 | 121.75 | 3.5881 | below_vwap | below_vwap,spread_too_wide |
| 16 | MU | memory_hbm_storage | 848.86 |  | 831.3497 | 2.1062 | 815.79 | 789.27 | 0.6962 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SKHY | memory_hbm_storage | 145.105 |  | 142.4758 | 1.8454 | 139.35 | 134.52 | 0.6409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 497.07 |  | 496.3608 | 0.1429 | 493.605 | 476.45 | 4.3636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SNDK | memory_hbm_storage | 1243.01 |  | 1215.2503 | 2.2843 | 1195.145 | 1124.35 | 4.0225 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 483.72 |  | 481.3096 | 0.5008 | 472.15 | 457.835 | 3.0389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 679.26 |  | 678.7914 | 0.069 | 677.685 | 673.43 | 0.0427 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.39 |  | 62.3496 | 0.0649 | 61.885 | 60.76 | 0.0321 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 193.18 |  | 194.4688 | -0.6627 | 193.42 | 191.52 | 0.0155 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 448.485 |  | 447.0169 | 0.3284 | 451.36 | 432.44 | 0.2386 | watch_only | none |
| AAPL | mega_cap_platform | 331.73 |  | 331.9738 | -0.0734 | 334.41 | 330.835 | 0.1176 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 332.13 |  | 332.729 | -0.18 | 336.48 | 331.48 | 0.009 | below_vwap | below_vwap |
| AMD | ai_accelerator | 483.72 |  | 481.3096 | 0.5008 | 472.15 | 457.835 | 3.0389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.1 |  | 399.5683 | 0.1331 | 396.93 | 387.975 | 0.195 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 502.31 |  | 500.7034 | 0.3209 | 495.01 | 488.29 | 0.0856 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 535.81 |  | 535.888 | -0.0146 | 530.605 | 524.56 | 0.0541 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.94 |  | 384.3783 | -0.3742 | 382.725 | 377.85 | 3.9171 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.86 |  | 831.3497 | 2.1062 | 815.79 | 789.27 | 0.6962 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 181.96 |  | 180.3402 | 0.8982 | 178.81 | 175.265 | 0.2308 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 406.59 |  | 405.7976 | 0.1953 | 397.47 | 383.67 | 0.2263 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 46.685 |  | 46.4756 | 0.4505 | 46.415 | 45.48 | 2.7204 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SMCI | ai_server_oem | 27.84 |  | 27.6853 | 0.5589 | 27.29 | 26.68 | 0.0718 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 735.885 |  | 736.9323 | -0.1421 | 736.77 | 734.67 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 289.865 |  | 290.2541 | -0.134 | 291.69 | 289.805 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.415 |  | 125.759 | -0.2735 | 124.935 | 121.75 | 3.5881 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.735 |  | 72.4053 | 3.2175 | 70.945 | 67.77 | 1.2578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 228.625 |  | 233.4619 | -2.0718 | 239.7 | 232.81 | 1.2291 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 380.82 |  | 383.5119 | -0.7019 | 385.94 | 380.46 | 3.9835 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 639.43 |  | 646.1034 | -1.0329 | 675.83 | 638.27 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 963.1 |  | 972.8851 | -1.0058 | 976.05 | 951.92 | 0.3188 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 443.01 |  | 452.1538 | -2.0223 | 465.04 | 449.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.945 |  | 143.8515 | -0.6301 | 146.02 | 142.6 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.04 |  | 169.4843 | -0.2621 | 168.42 | 165.88 | 4.076 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 245.23 |  | 245.1913 | 0.0158 | 246.07 | 239.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 679.4 |  | 677.777 | 0.2395 | 673.79 | 651.04 | 1.8075 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 363.54 |  | 362.5612 | 0.27 | 362.94 | 355.69 | 1.4744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.85 |  | 87.957 | 1.0153 | 87.57 | 82.85 | 1.8008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 289.38 |  | 284.5454 | 1.6991 | 283.97 | 274.46 | 4.6133 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1656.815 |  | 1657.6354 | -0.0495 | 1645.515 | 1626.61 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 497.07 |  | 496.3608 | 0.1429 | 493.605 | 476.45 | 4.3636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 300.3 |  | 305.0151 | -1.5459 | 315.605 | 297.09 | 1.3686 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 183.75 |  | 183.9606 | -0.1145 | 186.53 | 179.07 | 2.8354 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 355.63 |  | 355.019 | 0.1721 | 353.04 | 345.01 | 0.8408 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 248.14 |  | 247.2616 | 0.3553 | 249.235 | 239.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 47.715 |  | 47.9295 | -0.4476 | 47.95 | 46.385 | 0.3563 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 44.77 |  | 44.6117 | 0.3547 | 44.64 | 43.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 121.075 |  | 119.5933 | 1.2389 | 118.97 | 116.26 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 290.09 |  | 291.1521 | -0.3648 | 293.47 | 285.6 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 504.78 |  | 507.2136 | -0.4798 | 513.04 | 509.62 | 4.5763 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 300.64 |  | 302.3481 | -0.5649 | 310.51 | 303.35 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.84 |  | 27.7184 | 0.4386 | 27.29 | 25.36 | 0.1078 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 37.175 |  | 36.3166 | 2.3636 | 35.84 | 32.35 | 0.9146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CORZ | high_beta_ai_infrastructure | 21.805 |  | 21.7983 | 0.0309 | 22.06 | 19.77 | 0.321 | watch_only | none |
| SNDK | memory_hbm_storage | 1243.01 |  | 1215.2503 | 2.2843 | 1195.145 | 1124.35 | 4.0225 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 530.92 |  | 532.3777 | -0.2738 | 526.8 | 507.21 | 1.8986 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 852.4 |  | 879.3008 | -3.0593 | 890.57 | 863.14 | 0.3684 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 237.39 |  | 236.0085 | 0.5853 | 235.12 | 231.205 | 0.1938 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 532.91 |  | 532.1971 | 0.134 | 536.38 | 524.49 | 0.0676 | watch_only | none |
| ARM | ai_accelerator | 233.87 |  | 244.9986 | -4.5423 | 268.11 | 241.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 145.105 |  | 142.4758 | 1.8454 | 139.35 | 134.52 | 0.6409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
