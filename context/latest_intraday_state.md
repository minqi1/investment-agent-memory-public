# Intraday State

- Generated at: `2026-07-29T01:37:12+08:00`
- Market time ET: `2026-07-28T13:37:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 6, 'watch_only': 13, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.64 |  | 673.8933 | 0.556 | 677.3 | 670.84 | 0.0546 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 493.49 |  | 489.8774 | 0.7374 | 497.64 | 485.42 | 0.077 | watch_only | none |
| SMH | semiconductor_index | 531.69 |  | 527.257 | 0.8408 | 533.01 | 523.325 | 0.0583 | watch_only | none |
| SPY | market_regime | 741.64 |  | 739.3466 | 0.3102 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.95 |  | 195.9416 | 1.025 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.64 |  | 739.3466 | 0.3102 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 677.64 |  | 673.8933 | 0.556 | 677.3 | 670.84 | 0.0546 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.66 |  | 330.0554 | 1.6981 | 330.21 | 324.97 | 0.2085 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.3 |  | 292.2518 | 0.3587 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 62.14 |  | 61.0508 | 1.784 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.64 |  | 739.3466 | 0.3102 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 677.64 |  | 673.8933 | 0.556 | 677.3 | 670.84 | 0.0546 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 293.3 |  | 292.2518 | 0.3587 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 339.16 |  | 338.8755 | 0.084 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 5 | SOXX | semiconductor_index | 493.49 |  | 489.8774 | 0.7374 | 497.64 | 485.42 | 0.077 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 231.965 |  | 230.3899 | 0.6837 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| 7 | IREN | high_beta_ai_infrastructure | 33.905 |  | 33.7165 | 0.5591 | 35.08 | 33.52 | 0.059 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 191.88 |  | 190.7133 | 0.6117 | 194.96 | 189.48 | 0.2814 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 399.21 |  | 396.1801 | 0.7648 | 400.09 | 392.355 | 0.2029 | watch_only | none |
| 10 | MKSI | semiconductor_materials | 283.475 |  | 282.4444 | 0.3649 | 296.8 | 283.22 | 0.2364 | watch_only | none |
| 11 | NVDA | ai_accelerator | 197.95 |  | 195.9416 | 1.025 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 12 | TT | data_center_power_cooling | 465.62 |  | 465.014 | 0.1303 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ARM | ai_accelerator | 246.08 |  | 245.3785 | 0.2859 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMH | semiconductor_index | 531.69 |  | 527.257 | 0.8408 | 533.01 | 523.325 | 0.0583 | watch_only | none |
| 15 | SMCI | ai_server_oem | 28.37 |  | 27.966 | 1.4445 | 28.86 | 27.59 | 0.0705 | watch_only | none |
| 16 | ETN | data_center_power_cooling | 384.125 |  | 380.4574 | 0.964 | 384.565 | 377.43 | 0.1952 | watch_only | none |
| 17 | ASML | semiconductor_equipment | 1585.18 |  | 1577.1123 | 0.5116 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MRVL | custom_silicon_networking | 176.405 |  | 174.0292 | 1.3652 | 181.24 | 172.395 | 0.2778 | watch_only | none |
| 19 | SKHY | memory_hbm_storage | 132.095 |  | 131.6449 | 0.3419 | 136.45 | 131.735 | 0.757 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MU | memory_hbm_storage | 819.82 |  | 815.264 | 0.5588 | 846.4 | 813.91 | 0.494 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.95 |  | 195.9416 | 1.025 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.64 |  | 739.3466 | 0.3102 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 677.64 |  | 673.8933 | 0.556 | 677.3 | 670.84 | 0.0546 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.66 |  | 330.0554 | 1.6981 | 330.21 | 324.97 | 0.2085 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.3 |  | 292.2518 | 0.3587 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 62.14 |  | 61.0508 | 1.784 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 391.99 |  | 387.4106 | 1.1821 | 390.46 | 382.495 | 2.6531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AVGO | custom_silicon_networking | 380.93 |  | 378.4797 | 0.6474 | 378.64 | 371.57 | 2.4939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 167.68 |  | 164.132 | 2.1617 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ORCL | cloud_ai_capex | 120.94 |  | 118.0511 | 2.4471 | 117.17 | 115.25 | 0.9343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SMH | semiconductor_index | 531.69 |  | 527.257 | 0.8408 | 533.01 | 523.325 | 0.0583 | watch_only | none |
| 12 | SOXX | semiconductor_index | 493.49 |  | 489.8774 | 0.7374 | 497.64 | 485.42 | 0.077 | watch_only | none |
| 13 | ETN | data_center_power_cooling | 384.125 |  | 380.4574 | 0.964 | 384.565 | 377.43 | 0.1952 | watch_only | none |
| 14 | KLAC | semiconductor_equipment | 191.88 |  | 190.7133 | 0.6117 | 194.96 | 189.48 | 0.2814 | watch_only | none |
| 15 | LITE | ai_networking_optical | 645.585 |  | 631.0468 | 2.3038 | 673.65 | 624.91 | 0.2819 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 399.21 |  | 396.1801 | 0.7648 | 400.09 | 392.355 | 0.2029 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.965 |  | 230.3899 | 0.6837 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| 18 | MRVL | custom_silicon_networking | 176.405 |  | 174.0292 | 1.3652 | 181.24 | 172.395 | 0.2778 | watch_only | none |
| 19 | MKSI | semiconductor_materials | 283.475 |  | 282.4444 | 0.3649 | 296.8 | 283.22 | 0.2364 | watch_only | none |
| 20 | SMCI | ai_server_oem | 28.37 |  | 27.966 | 1.4445 | 28.86 | 27.59 | 0.0705 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.64 |  | 673.8933 | 0.556 | 677.3 | 670.84 | 0.0546 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.14 |  | 61.0508 | 1.784 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.95 |  | 195.9416 | 1.025 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 399.21 |  | 396.1801 | 0.7648 | 400.09 | 392.355 | 0.2029 | watch_only | none |
| AAPL | mega_cap_platform | 339.16 |  | 338.8755 | 0.084 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.66 |  | 330.0554 | 1.6981 | 330.21 | 324.97 | 0.2085 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 459.59 |  | 455.3854 | 0.9233 | 472.485 | 453.76 | 3.2181 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.99 |  | 387.4106 | 1.1821 | 390.46 | 382.495 | 2.6531 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.49 |  | 489.8774 | 0.7374 | 497.64 | 485.42 | 0.077 | watch_only | none |
| SMH | semiconductor_index | 531.69 |  | 527.257 | 0.8408 | 533.01 | 523.325 | 0.0583 | watch_only | none |
| AVGO | custom_silicon_networking | 380.93 |  | 378.4797 | 0.6474 | 378.64 | 371.57 | 2.4939 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 819.82 |  | 815.264 | 0.5588 | 846.4 | 813.91 | 0.494 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.405 |  | 174.0292 | 1.3652 | 181.24 | 172.395 | 0.2778 | watch_only | none |
| DELL | ai_server_oem | 384.05 |  | 374.5875 | 2.5261 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.43 |  | 44.4483 | -0.0412 | 46.19 | 44.33 | 1.463 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 28.37 |  | 27.966 | 1.4445 | 28.86 | 27.59 | 0.0705 | watch_only | none |
| SPY | market_regime | 741.64 |  | 739.3466 | 0.3102 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.3 |  | 292.2518 | 0.3587 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.94 |  | 118.0511 | 2.4471 | 117.17 | 115.25 | 0.9343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67 |  | 66.2387 | 1.1493 | 68.995 | 65.635 | 1.2239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.57 |  | 266.3222 | 0.4685 | 273.86 | 266.04 | 0.7176 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 384.125 |  | 380.4574 | 0.964 | 384.565 | 377.43 | 0.1952 | watch_only | none |
| PWR | data_center_power_cooling | 586.03 |  | 581.9475 | 0.7015 | 603.25 | 584.69 | 2.203 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 943.25 |  | 937.5255 | 0.6106 | 955.825 | 935.665 | 2.7554 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 465.62 |  | 465.014 | 0.1303 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139 |  | 138.3692 | 0.4559 | 139.755 | 137.31 | 1.7698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.68 |  | 164.132 | 2.1617 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 241.94 |  | 236.8451 | 2.1512 | 256.145 | 236.73 | 0.8473 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 645.585 |  | 631.0468 | 2.3038 | 673.65 | 624.91 | 0.2819 | watch_only | none |
| CIEN | ai_networking_optical | 344.12 |  | 337.1322 | 2.0727 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.32 |  | 85.6858 | 3.0742 | 92.95 | 84.63 | 4.7441 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 262.8 |  | 258.79 | 1.5495 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1585.18 |  | 1577.1123 | 0.5116 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.99 |  | 476.8435 | -0.179 | 494.87 | 477.03 | 0.2059 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 269.56 |  | 266.2781 | 1.2325 | 276.85 | 267.14 | 3.0309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.88 |  | 190.7133 | 0.6117 | 194.96 | 189.48 | 0.2814 | watch_only | none |
| TER | semiconductor_test_packaging | 311.02 |  | 308.2696 | 0.8922 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 239.27 |  | 236.5485 | 1.1505 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.14 |  | 46.7934 | -1.3963 | 51.64 | 47.435 | 4.0746 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.33 |  | 42.4995 | -0.3988 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.91 |  | 119.4222 | -0.4289 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 283.475 |  | 282.4444 | 0.3649 | 296.8 | 283.22 | 0.2364 | watch_only | none |
| LIN | industrial_gases | 517.68 |  | 518.5422 | -0.1663 | 518.6 | 511.495 | 4.5433 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.5 |  | 295.8647 | -0.1233 | 297.25 | 293.555 | 0.1861 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.355 |  | 26.5329 | -0.6705 | 27 | 25.42 | 0.4933 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.905 |  | 33.7165 | 0.5591 | 35.08 | 33.52 | 0.059 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.45 |  | 20.0203 | 2.1461 | 20.97 | 19.755 | 0.0489 | watch_only | none |
| SNDK | memory_hbm_storage | 1094.55 |  | 1102.1857 | -0.6928 | 1185.19 | 1114.57 | 1.5997 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.91 |  | 438.2137 | 4.2665 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 750.17 |  | 728.3228 | 2.9997 | 774.805 | 719.02 | 3.7791 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.965 |  | 230.3899 | 0.6837 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| META | cloud_ai_capex | 594.2 |  | 593.8419 | 0.0603 | 600.765 | 594.21 | 1.1511 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 246.08 |  | 245.3785 | 0.2859 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.095 |  | 131.6449 | 0.3419 | 136.45 | 131.735 | 0.757 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
