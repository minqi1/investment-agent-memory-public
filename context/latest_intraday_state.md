# Intraday State

- Generated at: `2026-07-29T01:52:31+08:00`
- Market time ET: `2026-07-28T13:52:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 1, 'below_vwap': 11, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.28 |  | 673.9749 | 0.342 | 677.3 | 670.84 | 0.0192 | watch_only | none |
| SOXX | semiconductor_index | 490.65 |  | 489.8906 | 0.155 | 497.64 | 485.42 | 0.051 | watch_only | none |
| SMH | semiconductor_index | 528.87 |  | 527.2819 | 0.3012 | 533.01 | 523.325 | 0.0529 | watch_only | none |
| SPY | market_regime | 740.92 |  | 739.4164 | 0.2033 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.06 |  | 195.9734 | 0.5545 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.37 |  | 378.5282 | 0.2224 | 378.64 | 371.57 | 0.0554 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.92 |  | 739.4164 | 0.2033 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.555 |  | 330.2799 | 1.5972 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.37 |  | 378.5282 | 0.2224 | 378.64 | 371.57 | 0.0554 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.92 |  | 739.4164 | 0.2033 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 528.87 |  | 527.2819 | 0.3012 | 533.01 | 523.325 | 0.0529 | watch_only | none |
| 4 | SOXX | semiconductor_index | 490.65 |  | 489.8906 | 0.155 | 497.64 | 485.42 | 0.051 | watch_only | none |
| 5 | QQQ | market_regime | 676.28 |  | 673.9749 | 0.342 | 677.3 | 670.84 | 0.0192 | watch_only | none |
| 6 | IWM | market_regime | 293.05 |  | 292.2896 | 0.2602 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 7 | KLAC | semiconductor_equipment | 191.1 |  | 190.7343 | 0.1917 | 194.96 | 189.48 | 0.0314 | watch_only | none |
| 8 | NVDA | ai_accelerator | 197.06 |  | 195.9734 | 0.5545 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 9 | IREN | high_beta_ai_infrastructure | 33.81 |  | 33.719 | 0.2699 | 35.08 | 33.52 | 0.0887 | watch_only | none |
| 10 | AAPL | mega_cap_platform | 339.74 |  | 338.9009 | 0.2476 | 342.87 | 337.78 | 0.0206 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 399.16 |  | 396.2574 | 0.7325 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 12 | AMZN | cloud_ai_capex | 231.25 |  | 230.4322 | 0.3549 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 13 | MRVL | custom_silicon_networking | 175.26 |  | 174.116 | 0.657 | 181.24 | 172.395 | 0.2453 | watch_only | none |
| 14 | TT | data_center_power_cooling | 465.385 |  | 464.9925 | 0.0844 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 309.18 |  | 308.3643 | 0.2645 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SMCI | ai_server_oem | 28.315 |  | 27.9774 | 1.2068 | 28.86 | 27.59 | 0.0706 | watch_only | none |
| 17 | LRCX | semiconductor_equipment | 268.74 |  | 266.3781 | 0.8867 | 276.85 | 267.14 | 0.3051 | watch_only | none |
| 18 | JCI | data_center_power_cooling | 138.44 |  | 138.374 | 0.0477 | 139.755 | 137.31 | 4.3557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | GOOGL | cloud_ai_capex | 335.555 |  | 330.2799 | 1.5972 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 20 | TSM | foundry | 390.02 |  | 387.4831 | 0.6547 | 390.46 | 382.495 | 1.5615 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.06 |  | 195.9734 | 0.5545 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.37 |  | 378.5282 | 0.2224 | 378.64 | 371.57 | 0.0554 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.92 |  | 739.4164 | 0.2033 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.555 |  | 330.2799 | 1.5972 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 167.11 |  | 164.2281 | 1.7548 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ORCL | cloud_ai_capex | 120.4 |  | 118.1459 | 1.9079 | 117.17 | 115.25 | 4.5681 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SMH | semiconductor_index | 528.87 |  | 527.2819 | 0.3012 | 533.01 | 523.325 | 0.0529 | watch_only | none |
| 8 | SOXX | semiconductor_index | 490.65 |  | 489.8906 | 0.155 | 497.64 | 485.42 | 0.051 | watch_only | none |
| 9 | QQQ | market_regime | 676.28 |  | 673.9749 | 0.342 | 677.3 | 670.84 | 0.0192 | watch_only | none |
| 10 | IWM | market_regime | 293.05 |  | 292.2896 | 0.2602 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 11 | KLAC | semiconductor_equipment | 191.1 |  | 190.7343 | 0.1917 | 194.96 | 189.48 | 0.0314 | watch_only | none |
| 12 | LRCX | semiconductor_equipment | 268.74 |  | 266.3781 | 0.8867 | 276.85 | 267.14 | 0.3051 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 399.16 |  | 396.2574 | 0.7325 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 14 | AMZN | cloud_ai_capex | 231.25 |  | 230.4322 | 0.3549 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 15 | MRVL | custom_silicon_networking | 175.26 |  | 174.116 | 0.657 | 181.24 | 172.395 | 0.2453 | watch_only | none |
| 16 | SMCI | ai_server_oem | 28.315 |  | 27.9774 | 1.2068 | 28.86 | 27.59 | 0.0706 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 33.81 |  | 33.719 | 0.2699 | 35.08 | 33.52 | 0.0887 | watch_only | none |
| 18 | AAPL | mega_cap_platform | 339.74 |  | 338.9009 | 0.2476 | 342.87 | 337.78 | 0.0206 | watch_only | none |
| 19 | CORZ | high_beta_ai_infrastructure | 20.54 |  | 20.0312 | 2.5399 | 20.97 | 19.755 | 0.0974 | watch_only | none |
| 20 | TQQQ | leveraged_tool | 61.77 |  | 61.0715 | 1.1437 | 62.01 | 60.23 | 0.0162 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.28 |  | 673.9749 | 0.342 | 677.3 | 670.84 | 0.0192 | watch_only | none |
| TQQQ | leveraged_tool | 61.77 |  | 61.0715 | 1.1437 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.06 |  | 195.9734 | 0.5545 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 399.16 |  | 396.2574 | 0.7325 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| AAPL | mega_cap_platform | 339.74 |  | 338.9009 | 0.2476 | 342.87 | 337.78 | 0.0206 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.555 |  | 330.2799 | 1.5972 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 457.53 |  | 455.469 | 0.4525 | 472.485 | 453.76 | 2.7845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 390.02 |  | 387.4831 | 0.6547 | 390.46 | 382.495 | 1.5615 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.65 |  | 489.8906 | 0.155 | 497.64 | 485.42 | 0.051 | watch_only | none |
| SMH | semiconductor_index | 528.87 |  | 527.2819 | 0.3012 | 533.01 | 523.325 | 0.0529 | watch_only | none |
| AVGO | custom_silicon_networking | 379.37 |  | 378.5282 | 0.2224 | 378.64 | 371.57 | 0.0554 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 814.69 |  | 815.2627 | -0.0703 | 846.4 | 813.91 | 0.7352 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 175.26 |  | 174.116 | 0.657 | 181.24 | 172.395 | 0.2453 | watch_only | none |
| DELL | ai_server_oem | 383.35 |  | 374.7134 | 2.3049 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.33 |  | 44.4463 | -0.2617 | 46.19 | 44.33 | 0.1128 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.315 |  | 27.9774 | 1.2068 | 28.86 | 27.59 | 0.0706 | watch_only | none |
| SPY | market_regime | 740.92 |  | 739.4164 | 0.2033 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.05 |  | 292.2896 | 0.2602 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.4 |  | 118.1459 | 1.9079 | 117.17 | 115.25 | 4.5681 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.535 |  | 66.2527 | 0.4262 | 68.995 | 65.635 | 1.8637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 264.91 |  | 266.3001 | -0.522 | 273.86 | 266.04 | 0.2605 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 384.24 |  | 380.8523 | 0.8895 | 384.565 | 377.43 | 2.4308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 583.975 |  | 582.0197 | 0.3359 | 603.25 | 584.69 | 1.5686 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 936.75 |  | 937.5667 | -0.0871 | 955.825 | 935.665 | 0.2114 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 465.385 |  | 464.9925 | 0.0844 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 138.44 |  | 138.374 | 0.0477 | 139.755 | 137.31 | 4.3557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.11 |  | 164.2281 | 1.7548 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 241.9 |  | 237.0385 | 2.0509 | 256.145 | 236.73 | 0.5622 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 640.98 |  | 631.3588 | 1.5239 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 340.74 |  | 337.2282 | 1.0414 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.62 |  | 85.7311 | 2.2033 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.145 |  | 258.901 | 0.8667 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1575.39 |  | 1577.1647 | -0.1125 | 1586.01 | 1565.95 | 1.081 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 472.02 |  | 476.6725 | -0.976 | 494.87 | 477.03 | 0.1504 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 268.74 |  | 266.3781 | 0.8867 | 276.85 | 267.14 | 0.3051 | watch_only | none |
| KLAC | semiconductor_equipment | 191.1 |  | 190.7343 | 0.1917 | 194.96 | 189.48 | 0.0314 | watch_only | none |
| TER | semiconductor_test_packaging | 309.18 |  | 308.3643 | 0.2645 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 237.5 |  | 236.5863 | 0.3862 | 248.8 | 236.42 | 0.8505 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.95 |  | 46.7761 | -1.766 | 51.64 | 47.435 | 4.5702 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.935 |  | 42.4893 | -1.3047 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.17 |  | 119.4005 | -1.0306 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.82 |  | 282.4433 | -0.2207 | 296.8 | 283.22 | 0.2803 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LIN | industrial_gases | 516.13 |  | 518.5074 | -0.4585 | 518.6 | 511.495 | 4.8321 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.99 |  | 295.8471 | -0.2897 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.28 |  | 26.5292 | -0.9392 | 27 | 25.42 | 0.0761 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.81 |  | 33.719 | 0.2699 | 35.08 | 33.52 | 0.0887 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.54 |  | 20.0312 | 2.5399 | 20.97 | 19.755 | 0.0974 | watch_only | none |
| SNDK | memory_hbm_storage | 1074.67 |  | 1101.4528 | -2.4316 | 1185.19 | 1114.57 | 1.4777 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 451.64 |  | 438.6042 | 2.9721 | 465.04 | 435.22 | 4.7405 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 745.41 |  | 728.9159 | 2.2628 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.25 |  | 230.4322 | 0.3549 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 593.29 |  | 593.8457 | -0.0936 | 600.765 | 594.21 | 1.5018 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.45 |  | 245.3508 | -0.3672 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131.33 |  | 131.6432 | -0.2379 | 136.45 | 131.735 | 3.0077 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
