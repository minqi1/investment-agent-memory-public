# Intraday State

- Generated at: `2026-07-29T00:51:16+08:00`
- Market time ET: `2026-07-28T12:51:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'watch_only': 10, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1, 'below_vwap': 3, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.245 |  | 673.6411 | 0.6834 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 495.05 |  | 489.6895 | 1.0947 | 497.64 | 485.42 | 0.0626 | watch_only | none |
| SMH | semiconductor_index | 532.78 |  | 526.9836 | 1.0999 | 533.01 | 523.325 | 0.0206 | watch_only | none |
| SPY | market_regime | 742.19 |  | 739.0827 | 0.4204 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.795 |  | 195.7241 | 1.0581 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 383.34 |  | 378.1902 | 1.3617 | 378.64 | 371.57 | 0.0704 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.19 |  | 739.0827 | 0.4204 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.245 |  | 673.6411 | 0.6834 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.93 |  | 329.4267 | 1.367 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.33 |  | 292.1181 | 0.4149 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.37 |  | 60.9394 | 2.3476 | 62.01 | 60.23 | 0.0321 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 678.245 |  | 673.6411 | 0.6834 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.33 |  | 292.1181 | 0.4149 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.19 |  | 739.0827 | 0.4204 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 339.4 |  | 338.8353 | 0.1667 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 398.63 |  | 396.0303 | 0.6564 | 400.09 | 392.355 | 0.1029 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 231.77 |  | 230.1862 | 0.688 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 7 | APLD | high_beta_ai_infrastructure | 26.715 |  | 26.5362 | 0.674 | 27 | 25.42 | 0.0749 | watch_only | none |
| 8 | NVDA | ai_accelerator | 197.795 |  | 195.7241 | 1.0581 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 9 | AVGO | custom_silicon_networking | 383.34 |  | 378.1902 | 1.3617 | 378.64 | 371.57 | 0.0704 | buy_precheck_manual_confirm | none |
| 10 | GOOGL | cloud_ai_capex | 333.93 |  | 329.4267 | 1.367 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 532.78 |  | 526.9836 | 1.0999 | 533.01 | 523.325 | 0.0206 | watch_only | none |
| 12 | SOXX | semiconductor_index | 495.05 |  | 489.6895 | 1.0947 | 497.64 | 485.42 | 0.0626 | watch_only | none |
| 13 | HPE | ai_server_oem | 44.91 |  | 44.4286 | 1.0835 | 46.19 | 44.33 | 0.0668 | watch_only | none |
| 14 | LIN | industrial_gases | 519.02 |  | 518.5662 | 0.0875 | 518.6 | 511.495 | 4.2638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CORZ | high_beta_ai_infrastructure | 20.29 |  | 20.0006 | 1.4469 | 20.97 | 19.755 | 0.0986 | watch_only | none |
| 16 | ASML | semiconductor_equipment | 1583.73 |  | 1576.3415 | 0.4687 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | VRT | data_center_power_cooling | 268.27 |  | 266.175 | 0.7871 | 273.86 | 266.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMAT | semiconductor_equipment | 477.81 |  | 476.9605 | 0.1781 | 494.87 | 477.03 | 2.0782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | META | cloud_ai_capex | 594.44 |  | 593.8237 | 0.1038 | 600.765 | 594.21 | 0.7738 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ENTG | semiconductor_materials | 119.78 |  | 119.4334 | 0.2902 | 121 | 117.72 | 4.2995 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.795 |  | 195.7241 | 1.0581 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 383.34 |  | 378.1902 | 1.3617 | 378.64 | 371.57 | 0.0704 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.19 |  | 739.0827 | 0.4204 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.245 |  | 673.6411 | 0.6834 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.93 |  | 329.4267 | 1.367 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.33 |  | 292.1181 | 0.4149 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.37 |  | 60.9394 | 2.3476 | 62.01 | 60.23 | 0.0321 | buy_precheck_manual_confirm | none |
| 8 | TSM | foundry | 392.17 |  | 387.0358 | 1.3265 | 390.46 | 382.495 | 0.8542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 167.88 |  | 163.8508 | 2.459 | 165.975 | 160.51 | 1.0543 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ETN | data_center_power_cooling | 385.435 |  | 380.1319 | 1.3951 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | LIN | industrial_gases | 519.02 |  | 518.5662 | 0.0875 | 518.6 | 511.495 | 4.2638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ORCL | cloud_ai_capex | 120.93 |  | 117.7683 | 2.6847 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SMH | semiconductor_index | 532.78 |  | 526.9836 | 1.0999 | 533.01 | 523.325 | 0.0206 | watch_only | none |
| 14 | SOXX | semiconductor_index | 495.05 |  | 489.6895 | 1.0947 | 497.64 | 485.42 | 0.0626 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 398.63 |  | 396.0303 | 0.6564 | 400.09 | 392.355 | 0.1029 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 231.77 |  | 230.1862 | 0.688 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 17 | HPE | ai_server_oem | 44.91 |  | 44.4286 | 1.0835 | 46.19 | 44.33 | 0.0668 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.49 |  | 27.9082 | 2.0846 | 28.86 | 27.59 | 0.0702 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34.285 |  | 33.6833 | 1.7864 | 35.08 | 33.52 | 0.0875 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.4 |  | 338.8353 | 0.1667 | 342.87 | 337.78 | 0.0118 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.245 |  | 673.6411 | 0.6834 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.37 |  | 60.9394 | 2.3476 | 62.01 | 60.23 | 0.0321 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.795 |  | 195.7241 | 1.0581 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.63 |  | 396.0303 | 0.6564 | 400.09 | 392.355 | 0.1029 | watch_only | none |
| AAPL | mega_cap_platform | 339.4 |  | 338.8353 | 0.1667 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.93 |  | 329.4267 | 1.367 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 459.96 |  | 454.9751 | 1.0956 | 472.485 | 453.76 | 3.6308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.17 |  | 387.0358 | 1.3265 | 390.46 | 382.495 | 0.8542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.05 |  | 489.6895 | 1.0947 | 497.64 | 485.42 | 0.0626 | watch_only | none |
| SMH | semiconductor_index | 532.78 |  | 526.9836 | 1.0999 | 533.01 | 523.325 | 0.0206 | watch_only | none |
| AVGO | custom_silicon_networking | 383.34 |  | 378.1902 | 1.3617 | 378.64 | 371.57 | 0.0704 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 823.4 |  | 814.5204 | 1.0902 | 846.4 | 813.91 | 0.6182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 177.77 |  | 173.8441 | 2.2583 | 181.24 | 172.395 | 4.3314 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 385.24 |  | 374.1488 | 2.9644 | 402 | 374.02 | 4.2727 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.91 |  | 44.4286 | 1.0835 | 46.19 | 44.33 | 0.0668 | watch_only | none |
| SMCI | ai_server_oem | 28.49 |  | 27.9082 | 2.0846 | 28.86 | 27.59 | 0.0702 | watch_only | none |
| SPY | market_regime | 742.19 |  | 739.0827 | 0.4204 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.33 |  | 292.1181 | 0.4149 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.93 |  | 117.7683 | 2.6847 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 67.41 |  | 66.1043 | 1.9752 | 68.995 | 65.635 | 0.7417 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.27 |  | 266.175 | 0.7871 | 273.86 | 266.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 385.435 |  | 380.1319 | 1.3951 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 586.19 |  | 581.3159 | 0.8385 | 603.25 | 584.69 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 946.82 |  | 936.845 | 1.0647 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 467.36 |  | 464.7776 | 0.5556 | 477.73 | 460.77 | 4.8014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.63 |  | 138.2435 | 1.003 | 139.755 | 137.31 | 2.213 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.88 |  | 163.8508 | 2.459 | 165.975 | 160.51 | 1.0543 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 241.24 |  | 236.2364 | 2.1181 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 651.64 |  | 629.2222 | 3.5628 | 673.65 | 624.91 | 4.6774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 343.05 |  | 336.7146 | 1.8815 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.64 |  | 85.5306 | 3.6355 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.87 |  | 258.611 | 2.8069 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1583.73 |  | 1576.3415 | 0.4687 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 477.81 |  | 476.9605 | 0.1781 | 494.87 | 477.03 | 2.0782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 270.31 |  | 266.0201 | 1.6126 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 192.93 |  | 190.5525 | 1.2477 | 194.96 | 189.48 | 3.5246 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 312.76 |  | 307.7439 | 1.63 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 237.62 |  | 236.4864 | 0.4794 | 248.8 | 236.42 | 4.1747 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.94 |  | 46.8281 | -1.8965 | 51.64 | 47.435 | 4.31 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.41 |  | 42.5209 | -0.2607 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.78 |  | 119.4334 | 0.2902 | 121 | 117.72 | 4.2995 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 286.02 |  | 282.0995 | 1.3898 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 519.02 |  | 518.5662 | 0.0875 | 518.6 | 511.495 | 4.2638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.86 |  | 295.9065 | -0.0157 | 297.25 | 293.555 | 0.1048 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.715 |  | 26.5362 | 0.674 | 27 | 25.42 | 0.0749 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.285 |  | 33.6833 | 1.7864 | 35.08 | 33.52 | 0.0875 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.29 |  | 20.0006 | 1.4469 | 20.97 | 19.755 | 0.0986 | watch_only | none |
| SNDK | memory_hbm_storage | 1103.01 |  | 1102.6803 | 0.0299 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 459.065 |  | 437.0652 | 5.0335 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 749.34 |  | 725.5221 | 3.2829 | 774.805 | 719.02 | 4.5146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.77 |  | 230.1862 | 0.688 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.44 |  | 593.8237 | 0.1038 | 600.765 | 594.21 | 0.7738 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 247.94 |  | 245.1801 | 1.1257 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.27 |  | 131.5959 | 1.2721 | 136.45 | 131.735 | 1.2306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
