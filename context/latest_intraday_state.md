# Intraday State

- Generated at: `2026-07-29T02:11:43+08:00`
- Market time ET: `2026-07-28T14:11:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 13, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_vwap': 11, 'below_opening_15m_low': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.94 |  | 674.0134 | 0.2858 | 677.3 | 670.84 | 0.034 | watch_only | none |
| SOXX | semiconductor_index | 490.83 |  | 489.9541 | 0.1788 | 497.64 | 485.42 | 0.0591 | watch_only | none |
| SMH | semiconductor_index | 528.585 |  | 527.3203 | 0.2398 | 533.01 | 523.325 | 0.0378 | watch_only | none |
| SPY | market_regime | 740.73 |  | 739.4735 | 0.1699 | 739.42 | 736.57 | 0.0122 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.86 |  | 196.0066 | 0.4354 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.73 |  | 739.4735 | 0.1699 | 739.42 | 736.57 | 0.0122 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.48 |  | 330.4447 | 1.2212 | 330.21 | 324.97 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.4 |  | 118.29 | 1.7838 | 117.17 | 115.25 | 0.108 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.73 |  | 739.4735 | 0.1699 | 739.42 | 736.57 | 0.0122 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 196.86 |  | 196.0066 | 0.4354 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 3 | MU | memory_hbm_storage | 817.6 |  | 815.3248 | 0.2791 | 846.4 | 813.91 | 0.0917 | watch_only | none |
| 4 | SMH | semiconductor_index | 528.585 |  | 527.3203 | 0.2398 | 533.01 | 523.325 | 0.0378 | watch_only | none |
| 5 | SOXX | semiconductor_index | 490.83 |  | 489.9541 | 0.1788 | 497.64 | 485.42 | 0.0591 | watch_only | none |
| 6 | QQQ | market_regime | 675.94 |  | 674.0134 | 0.2858 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 7 | IWM | market_regime | 292.93 |  | 292.3248 | 0.207 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 190.91 |  | 190.7599 | 0.0787 | 194.96 | 189.48 | 0.0314 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 397.385 |  | 396.3149 | 0.27 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 231.17 |  | 230.4563 | 0.3097 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 11 | AAPL | mega_cap_platform | 339.56 |  | 338.9301 | 0.1859 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 12 | TSM | foundry | 389.96 |  | 387.5625 | 0.6186 | 390.46 | 382.495 | 0.0513 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 334.48 |  | 330.4447 | 1.2212 | 330.21 | 324.97 | 0.012 | buy_precheck_manual_confirm | none |
| 14 | ASML | semiconductor_equipment | 1578.47 |  | 1577.1752 | 0.0821 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 379.38 |  | 378.5504 | 0.2191 | 378.64 | 371.57 | 1.26 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SMCI | ai_server_oem | 28.38 |  | 27.9879 | 1.4009 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 17 | TT | data_center_power_cooling | 466.92 |  | 465.0732 | 0.3971 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 456.88 |  | 455.5236 | 0.2978 | 472.485 | 453.76 | 2.539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 174.9 |  | 174.1616 | 0.424 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 237.87 |  | 236.6762 | 0.5044 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.86 |  | 196.0066 | 0.4354 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.73 |  | 739.4735 | 0.1699 | 739.42 | 736.57 | 0.0122 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.48 |  | 330.4447 | 1.2212 | 330.21 | 324.97 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.4 |  | 118.29 | 1.7838 | 117.17 | 115.25 | 0.108 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 379.38 |  | 378.5504 | 0.2191 | 378.64 | 371.57 | 1.26 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 168.275 |  | 164.4857 | 2.3037 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 139.9 |  | 138.4255 | 1.0652 | 139.755 | 137.31 | 3.2809 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ETN | data_center_power_cooling | 385.26 |  | 381.0017 | 1.1176 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | TSM | foundry | 389.96 |  | 387.5625 | 0.6186 | 390.46 | 382.495 | 0.0513 | watch_only | none |
| 10 | MU | memory_hbm_storage | 817.6 |  | 815.3248 | 0.2791 | 846.4 | 813.91 | 0.0917 | watch_only | none |
| 11 | SMH | semiconductor_index | 528.585 |  | 527.3203 | 0.2398 | 533.01 | 523.325 | 0.0378 | watch_only | none |
| 12 | SOXX | semiconductor_index | 490.83 |  | 489.9541 | 0.1788 | 497.64 | 485.42 | 0.0591 | watch_only | none |
| 13 | QQQ | market_regime | 675.94 |  | 674.0134 | 0.2858 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 14 | IWM | market_regime | 292.93 |  | 292.3248 | 0.207 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 190.91 |  | 190.7599 | 0.0787 | 194.96 | 189.48 | 0.0314 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 397.385 |  | 396.3149 | 0.27 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.17 |  | 230.4563 | 0.3097 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.38 |  | 27.9879 | 1.4009 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 19 | AAPL | mega_cap_platform | 339.56 |  | 338.9301 | 0.1859 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 20 | CORZ | high_beta_ai_infrastructure | 20.53 |  | 20.0429 | 2.4301 | 20.97 | 19.755 | 0.0487 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.94 |  | 674.0134 | 0.2858 | 677.3 | 670.84 | 0.034 | watch_only | none |
| TQQQ | leveraged_tool | 61.66 |  | 61.092 | 0.9298 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 196.86 |  | 196.0066 | 0.4354 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.385 |  | 396.3149 | 0.27 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| AAPL | mega_cap_platform | 339.56 |  | 338.9301 | 0.1859 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.48 |  | 330.4447 | 1.2212 | 330.21 | 324.97 | 0.012 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.88 |  | 455.5236 | 0.2978 | 472.485 | 453.76 | 2.539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 389.96 |  | 387.5625 | 0.6186 | 390.46 | 382.495 | 0.0513 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.83 |  | 489.9541 | 0.1788 | 497.64 | 485.42 | 0.0591 | watch_only | none |
| SMH | semiconductor_index | 528.585 |  | 527.3203 | 0.2398 | 533.01 | 523.325 | 0.0378 | watch_only | none |
| AVGO | custom_silicon_networking | 379.38 |  | 378.5504 | 0.2191 | 378.64 | 371.57 | 1.26 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 817.6 |  | 815.3248 | 0.2791 | 846.4 | 813.91 | 0.0917 | watch_only | none |
| MRVL | custom_silicon_networking | 174.9 |  | 174.1616 | 0.424 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 382.72 |  | 374.9061 | 2.0842 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.37 |  | 44.4412 | -0.1602 | 46.19 | 44.33 | 0.0676 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.38 |  | 27.9879 | 1.4009 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 740.73 |  | 739.4735 | 0.1699 | 739.42 | 736.57 | 0.0122 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.93 |  | 292.3248 | 0.207 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.4 |  | 118.29 | 1.7838 | 117.17 | 115.25 | 0.108 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.315 |  | 66.2553 | 0.0901 | 68.995 | 65.635 | 2.3373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 264.765 |  | 266.2144 | -0.5444 | 273.86 | 266.04 | 1.8998 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 385.26 |  | 381.0017 | 1.1176 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.27 |  | 582.0898 | 0.5463 | 603.25 | 584.69 | 2.5629 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 936.66 |  | 937.5359 | -0.0934 | 955.825 | 935.665 | 0.2712 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 466.92 |  | 465.0732 | 0.3971 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.9 |  | 138.4255 | 1.0652 | 139.755 | 137.31 | 3.2809 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 168.275 |  | 164.4857 | 2.3037 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.135 |  | 237.227 | 1.2258 | 256.145 | 236.73 | 4.4142 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 641.58 |  | 631.6373 | 1.5741 | 673.65 | 624.91 | 0.4317 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 341.1 |  | 337.3376 | 1.1153 | 354.09 | 338.14 | 4.5148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 86.89 |  | 85.7638 | 1.3131 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.92 |  | 258.9968 | 1.1286 | 268.265 | 253.05 | 4.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1578.47 |  | 1577.1752 | 0.0821 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 473.675 |  | 476.5064 | -0.5942 | 494.87 | 477.03 | 0.2533 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 269.95 |  | 266.4292 | 1.3215 | 276.85 | 267.14 | 3.7711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.91 |  | 190.7599 | 0.0787 | 194.96 | 189.48 | 0.0314 | watch_only | none |
| TER | semiconductor_test_packaging | 308.02 |  | 308.4197 | -0.1296 | 315.21 | 304.11 | 2.2499 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 237.87 |  | 236.6762 | 0.5044 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.035 |  | 46.7634 | -1.5577 | 51.64 | 47.435 | 2.0202 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.1 |  | 42.4846 | -0.9053 | 44.155 | 41.78 | 1.0689 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 118.39 |  | 119.3596 | -0.8124 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.25 |  | 282.405 | -0.409 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 514.35 |  | 518.3723 | -0.7759 | 518.6 | 511.495 | 5.1094 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.57 |  | 295.8116 | -0.4197 | 297.25 | 293.555 | 0.1222 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.34 |  | 26.5227 | -0.6887 | 27 | 25.42 | 0.038 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.655 |  | 33.7186 | -0.1887 | 35.08 | 33.52 | 0.0594 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.53 |  | 20.0429 | 2.4301 | 20.97 | 19.755 | 0.0487 | watch_only | none |
| SNDK | memory_hbm_storage | 1077.51 |  | 1100.7912 | -2.115 | 1185.19 | 1114.57 | 1.7383 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.28 |  | 438.9439 | 3.4939 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 751.5 |  | 730.1179 | 2.9286 | 774.805 | 719.02 | 0.4138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.17 |  | 230.4563 | 0.3097 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 593.61 |  | 593.8328 | -0.0375 | 600.765 | 594.21 | 0.1617 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 243.81 |  | 245.302 | -0.6082 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131 |  | 131.6339 | -0.4816 | 136.45 | 131.735 | 1.4122 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
