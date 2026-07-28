# Intraday State

- Generated at: `2026-07-29T01:48:42+08:00`
- Market time ET: `2026-07-28T13:48:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 15, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 1, 'below_vwap': 11, 'below_opening_15m_low': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.06 |  | 673.9592 | 0.3117 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.05 |  | 489.888 | 0.2372 | 497.64 | 485.42 | 0.0692 | watch_only | none |
| SMH | semiconductor_index | 528.35 |  | 527.2775 | 0.2034 | 533.01 | 523.325 | 0.036 | watch_only | none |
| SPY | market_regime | 740.76 |  | 739.3966 | 0.1844 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197 |  | 195.966 | 0.5276 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.42 |  | 378.5118 | 0.2399 | 378.64 | 371.57 | 0.1344 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.76 |  | 739.3966 | 0.1844 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.985 |  | 330.2315 | 1.4394 | 330.21 | 324.97 | 0.2567 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.42 |  | 378.5118 | 0.2399 | 378.64 | 371.57 | 0.1344 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.76 |  | 739.3966 | 0.1844 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 528.35 |  | 527.2775 | 0.2034 | 533.01 | 523.325 | 0.036 | watch_only | none |
| 4 | SOXX | semiconductor_index | 491.05 |  | 489.888 | 0.2372 | 497.64 | 485.42 | 0.0692 | watch_only | none |
| 5 | QQQ | market_regime | 676.06 |  | 673.9592 | 0.3117 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 6 | IWM | market_regime | 292.87 |  | 292.2801 | 0.2018 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 7 | KLAC | semiconductor_equipment | 190.83 |  | 190.7315 | 0.0517 | 194.96 | 189.48 | 0.11 | watch_only | none |
| 8 | NVDA | ai_accelerator | 197 |  | 195.966 | 0.5276 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 231.14 |  | 230.4235 | 0.311 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 10 | ASML | semiconductor_equipment | 1578.46 |  | 1577.167 | 0.082 | 1586.01 | 1565.95 | 0.2173 | watch_only | none |
| 11 | AAPL | mega_cap_platform | 339.73 |  | 338.8914 | 0.2474 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 12 | TSM | foundry | 389.28 |  | 387.4607 | 0.4696 | 390.46 | 382.495 | 0.0796 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 398.96 |  | 396.2275 | 0.6896 | 400.09 | 392.355 | 0.0451 | watch_only | none |
| 14 | MRVL | custom_silicon_networking | 175.41 |  | 174.1076 | 0.7481 | 181.24 | 172.395 | 0.0741 | watch_only | none |
| 15 | TER | semiconductor_test_packaging | 309.58 |  | 308.3481 | 0.3995 | 315.21 | 304.11 | 0.2035 | watch_only | none |
| 16 | GOOGL | cloud_ai_capex | 334.985 |  | 330.2315 | 1.4394 | 330.21 | 324.97 | 0.2567 | buy_precheck_manual_confirm | none |
| 17 | SMCI | ai_server_oem | 28.2 |  | 27.9752 | 0.8034 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 18 | ALAB | ai_networking_optical | 260.855 |  | 258.8785 | 0.7635 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ONTO | semiconductor_test_packaging | 238.005 |  | 236.5687 | 0.6072 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 457.205 |  | 455.4484 | 0.3857 | 472.485 | 453.76 | 2.7624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197 |  | 195.966 | 0.5276 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.42 |  | 378.5118 | 0.2399 | 378.64 | 371.57 | 0.1344 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.76 |  | 739.3966 | 0.1844 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.985 |  | 330.2315 | 1.4394 | 330.21 | 324.97 | 0.2567 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 167.09 |  | 164.203 | 1.7582 | 165.975 | 160.51 | 4.9075 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ORCL | cloud_ai_capex | 120.44 |  | 118.1349 | 1.9513 | 117.17 | 115.25 | 1.3119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | TSM | foundry | 389.28 |  | 387.4607 | 0.4696 | 390.46 | 382.495 | 0.0796 | watch_only | none |
| 8 | SMH | semiconductor_index | 528.35 |  | 527.2775 | 0.2034 | 533.01 | 523.325 | 0.036 | watch_only | none |
| 9 | SOXX | semiconductor_index | 491.05 |  | 489.888 | 0.2372 | 497.64 | 485.42 | 0.0692 | watch_only | none |
| 10 | QQQ | market_regime | 676.06 |  | 673.9592 | 0.3117 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 11 | ASML | semiconductor_equipment | 1578.46 |  | 1577.167 | 0.082 | 1586.01 | 1565.95 | 0.2173 | watch_only | none |
| 12 | IWM | market_regime | 292.87 |  | 292.2801 | 0.2018 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 13 | KLAC | semiconductor_equipment | 190.83 |  | 190.7315 | 0.0517 | 194.96 | 189.48 | 0.11 | watch_only | none |
| 14 | TER | semiconductor_test_packaging | 309.58 |  | 308.3481 | 0.3995 | 315.21 | 304.11 | 0.2035 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 398.96 |  | 396.2275 | 0.6896 | 400.09 | 392.355 | 0.0451 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 231.14 |  | 230.4235 | 0.311 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 17 | MRVL | custom_silicon_networking | 175.41 |  | 174.1076 | 0.7481 | 181.24 | 172.395 | 0.0741 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.2 |  | 27.9752 | 0.8034 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 19 | AAPL | mega_cap_platform | 339.73 |  | 338.8914 | 0.2474 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 20 | CORZ | high_beta_ai_infrastructure | 20.38 |  | 20.0239 | 1.7782 | 20.97 | 19.755 | 0.0981 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.06 |  | 673.9592 | 0.3117 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.67 |  | 61.0669 | 0.9875 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197 |  | 195.966 | 0.5276 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.96 |  | 396.2275 | 0.6896 | 400.09 | 392.355 | 0.0451 | watch_only | none |
| AAPL | mega_cap_platform | 339.73 |  | 338.8914 | 0.2474 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.985 |  | 330.2315 | 1.4394 | 330.21 | 324.97 | 0.2567 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 457.205 |  | 455.4484 | 0.3857 | 472.485 | 453.76 | 2.7624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 389.28 |  | 387.4607 | 0.4696 | 390.46 | 382.495 | 0.0796 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.05 |  | 489.888 | 0.2372 | 497.64 | 485.42 | 0.0692 | watch_only | none |
| SMH | semiconductor_index | 528.35 |  | 527.2775 | 0.2034 | 533.01 | 523.325 | 0.036 | watch_only | none |
| AVGO | custom_silicon_networking | 379.42 |  | 378.5118 | 0.2399 | 378.64 | 371.57 | 0.1344 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 811.57 |  | 815.2754 | -0.4545 | 846.4 | 813.91 | 0.0986 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 175.41 |  | 174.1076 | 0.7481 | 181.24 | 172.395 | 0.0741 | watch_only | none |
| DELL | ai_server_oem | 383.06 |  | 374.6759 | 2.2377 | 402 | 374.02 | 4.7904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.315 |  | 44.4471 | -0.2972 | 46.19 | 44.33 | 0.0451 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 28.2 |  | 27.9752 | 0.8034 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| SPY | market_regime | 740.76 |  | 739.3966 | 0.1844 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.87 |  | 292.2801 | 0.2018 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.44 |  | 118.1349 | 1.9513 | 117.17 | 115.25 | 1.3119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.49 |  | 66.2502 | 0.3619 | 68.995 | 65.635 | 1.895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.115 |  | 266.3152 | -0.4507 | 273.86 | 266.04 | 0.2527 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 383.98 |  | 380.8106 | 0.8323 | 384.565 | 377.43 | 4.5679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 583.69 |  | 581.993 | 0.2916 | 603.25 | 584.69 | 0.3632 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 936.28 |  | 937.5732 | -0.1379 | 955.825 | 935.665 | 0.2766 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 464.08 |  | 464.995 | -0.1968 | 477.73 | 460.77 | 0.1681 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 138.305 |  | 138.3742 | -0.05 | 139.755 | 137.31 | 1.2942 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 167.09 |  | 164.203 | 1.7582 | 165.975 | 160.51 | 4.9075 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 242.62 |  | 236.9753 | 2.382 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 641.07 |  | 631.2972 | 1.548 | 673.65 | 624.91 | 4.0963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.86 |  | 337.213 | 1.0815 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.46 |  | 85.7183 | 2.0319 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.855 |  | 258.8785 | 0.7635 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1578.46 |  | 1577.167 | 0.082 | 1586.01 | 1565.95 | 0.2173 | watch_only | none |
| AMAT | semiconductor_equipment | 471.95 |  | 476.7372 | -1.0042 | 494.87 | 477.03 | 0.178 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 267.96 |  | 266.3585 | 0.6013 | 276.85 | 267.14 | 2.4892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.83 |  | 190.7315 | 0.0517 | 194.96 | 189.48 | 0.11 | watch_only | none |
| TER | semiconductor_test_packaging | 309.58 |  | 308.3481 | 0.3995 | 315.21 | 304.11 | 0.2035 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.005 |  | 236.5687 | 0.6072 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.86 |  | 46.7861 | -1.9795 | 51.64 | 47.435 | 0.0654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 41.99 |  | 42.4921 | -1.1816 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.27 |  | 119.4081 | -0.9531 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 282.13 |  | 282.4514 | -0.1138 | 296.8 | 283.22 | 0.6451 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.74 |  | 518.5186 | -0.343 | 518.6 | 511.495 | 0.0755 | below_vwap | below_vwap |
| APD | industrial_gases | 295.34 |  | 295.8525 | -0.1732 | 297.25 | 293.555 | 0.0643 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.15 |  | 26.53 | -1.4323 | 27 | 25.42 | 0.6501 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.71 |  | 33.7185 | -0.0253 | 35.08 | 33.52 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.38 |  | 20.0239 | 1.7782 | 20.97 | 19.755 | 0.0981 | watch_only | none |
| SNDK | memory_hbm_storage | 1073.9 |  | 1101.5723 | -2.5121 | 1185.19 | 1114.57 | 3.0729 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 453.445 |  | 438.549 | 3.3967 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 745.43 |  | 728.8283 | 2.2779 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.14 |  | 230.4235 | 0.311 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.45 |  | 593.8465 | -0.0668 | 600.765 | 594.21 | 0.1365 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 243.9 |  | 245.3607 | -0.5953 | 253.38 | 243.72 | 1.1972 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 131.08 |  | 131.6441 | -0.4285 | 136.45 | 131.735 | 3.0134 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
