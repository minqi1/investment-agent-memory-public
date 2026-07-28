# Intraday State

- Generated at: `2026-07-28T23:27:54+08:00`
- Market time ET: `2026-07-28T11:27:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'watch_only': 11, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_vwap': 4, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.58 |  | 672.1983 | 0.8006 | 677.3 | 670.84 | 0.0059 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 493.62 |  | 488.5889 | 1.0297 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| SMH | semiconductor_index | 531.65 |  | 525.8311 | 1.1066 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| SPY | market_regime | 741.8 |  | 738.2064 | 0.4868 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.73 |  | 194.9574 | 1.4222 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 382.18 |  | 376.5232 | 1.5024 | 378.64 | 371.57 | 0.0288 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.8 |  | 738.2064 | 0.4868 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 677.58 |  | 672.1983 | 0.8006 | 677.3 | 670.84 | 0.0059 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 332.31 |  | 328.0845 | 1.2879 | 330.21 | 324.97 | 0.0512 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.415 |  | 291.7886 | 0.5574 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.33 |  | 116.4499 | 3.332 | 117.17 | 115.25 | 0.241 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.09 |  | 60.5553 | 2.5344 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.8 |  | 738.2064 | 0.4868 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.415 |  | 291.7886 | 0.5574 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 230.51 |  | 229.8757 | 0.2759 | 233.05 | 229.7 | 0.0434 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.285 |  | 338.5405 | 0.2199 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 5 | QQQ | market_regime | 677.58 |  | 672.1983 | 0.8006 | 677.3 | 670.84 | 0.0059 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 20.03 |  | 19.9138 | 0.5835 | 20.97 | 19.755 | 0.0999 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 332.31 |  | 328.0845 | 1.2879 | 330.21 | 324.97 | 0.0512 | buy_precheck_manual_confirm | none |
| 8 | NVDA | ai_accelerator | 197.73 |  | 194.9574 | 1.4222 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 9 | MU | memory_hbm_storage | 821.15 |  | 812.0349 | 1.1225 | 846.4 | 813.91 | 0.0317 | watch_only | none |
| 10 | SMH | semiconductor_index | 531.65 |  | 525.8311 | 1.1066 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| 11 | SOXX | semiconductor_index | 493.62 |  | 488.5889 | 1.0297 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| 12 | KLAC | semiconductor_equipment | 191.67 |  | 189.9241 | 0.9192 | 194.96 | 189.48 | 0.0835 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 399.765 |  | 395.3361 | 1.1203 | 400.09 | 392.355 | 0.065 | watch_only | none |
| 14 | AVGO | custom_silicon_networking | 382.18 |  | 376.5232 | 1.5024 | 378.64 | 371.57 | 0.0288 | buy_precheck_manual_confirm | none |
| 15 | AMAT | semiconductor_equipment | 477.83 |  | 476.706 | 0.2358 | 494.87 | 477.03 | 4.2547 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ASML | semiconductor_equipment | 1582.19 |  | 1571.6566 | 0.6702 | 1586.01 | 1565.95 | 0.7066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | STX | memory_hbm_storage | 728.07 |  | 722.6115 | 0.7554 | 774.805 | 719.02 | 0.4711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SMCI | ai_server_oem | 28.57 |  | 27.7331 | 3.0178 | 28.86 | 27.59 | 0.07 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34.47 |  | 33.4004 | 3.2023 | 35.08 | 33.52 | 0.058 | watch_only | none |
| 20 | ORCL | cloud_ai_capex | 120.33 |  | 116.4499 | 3.332 | 117.17 | 115.25 | 0.241 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.73 |  | 194.9574 | 1.4222 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 382.18 |  | 376.5232 | 1.5024 | 378.64 | 371.57 | 0.0288 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.8 |  | 738.2064 | 0.4868 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 677.58 |  | 672.1983 | 0.8006 | 677.3 | 670.84 | 0.0059 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 332.31 |  | 328.0845 | 1.2879 | 330.21 | 324.97 | 0.0512 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.415 |  | 291.7886 | 0.5574 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.33 |  | 116.4499 | 3.332 | 117.17 | 115.25 | 0.241 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.09 |  | 60.5553 | 2.5344 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 166.6 |  | 162.1802 | 2.7252 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | MU | memory_hbm_storage | 821.15 |  | 812.0349 | 1.1225 | 846.4 | 813.91 | 0.0317 | watch_only | none |
| 11 | SMH | semiconductor_index | 531.65 |  | 525.8311 | 1.1066 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| 12 | SOXX | semiconductor_index | 493.62 |  | 488.5889 | 1.0297 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| 13 | KLAC | semiconductor_equipment | 191.67 |  | 189.9241 | 0.9192 | 194.96 | 189.48 | 0.0835 | watch_only | none |
| 14 | APLD | high_beta_ai_infrastructure | 27.04 |  | 26.3954 | 2.4421 | 27 | 25.42 | 3.8831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MSFT | cloud_ai_capex | 399.765 |  | 395.3361 | 1.1203 | 400.09 | 392.355 | 0.065 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 230.51 |  | 229.8757 | 0.2759 | 233.05 | 229.7 | 0.0434 | watch_only | none |
| 17 | HPE | ai_server_oem | 44.92 |  | 44.2349 | 1.5488 | 46.19 | 44.33 | 0.2226 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.57 |  | 27.7331 | 3.0178 | 28.86 | 27.59 | 0.07 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34.47 |  | 33.4004 | 3.2023 | 35.08 | 33.52 | 0.058 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.285 |  | 338.5405 | 0.2199 | 342.87 | 337.78 | 0.0118 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.58 |  | 672.1983 | 0.8006 | 677.3 | 670.84 | 0.0059 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.09 |  | 60.5553 | 2.5344 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.73 |  | 194.9574 | 1.4222 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 399.765 |  | 395.3361 | 1.1203 | 400.09 | 392.355 | 0.065 | watch_only | none |
| AAPL | mega_cap_platform | 339.285 |  | 338.5405 | 0.2199 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 332.31 |  | 328.0845 | 1.2879 | 330.21 | 324.97 | 0.0512 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 457.79 |  | 452.8907 | 1.0818 | 472.485 | 453.76 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TSM | foundry | 390.22 |  | 385.1254 | 1.3228 | 390.46 | 382.495 | 1.7324 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.62 |  | 488.5889 | 1.0297 | 497.64 | 485.42 | 0.0628 | watch_only | none |
| SMH | semiconductor_index | 531.65 |  | 525.8311 | 1.1066 | 533.01 | 523.325 | 0.0621 | watch_only | none |
| AVGO | custom_silicon_networking | 382.18 |  | 376.5232 | 1.5024 | 378.64 | 371.57 | 0.0288 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 821.15 |  | 812.0349 | 1.1225 | 846.4 | 813.91 | 0.0317 | watch_only | none |
| MRVL | custom_silicon_networking | 177.67 |  | 172.7445 | 2.8513 | 181.24 | 172.395 | 1.4015 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 379.34 |  | 371.9331 | 1.9915 | 402 | 374.02 | 0.8409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.92 |  | 44.2349 | 1.5488 | 46.19 | 44.33 | 0.2226 | watch_only | none |
| SMCI | ai_server_oem | 28.57 |  | 27.7331 | 3.0178 | 28.86 | 27.59 | 0.07 | watch_only | none |
| SPY | market_regime | 741.8 |  | 738.2064 | 0.4868 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.415 |  | 291.7886 | 0.5574 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.33 |  | 116.4499 | 3.332 | 117.17 | 115.25 | 0.241 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.87 |  | 65.9034 | 1.4667 | 68.995 | 65.635 | 1.7646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.71 |  | 265.5936 | 1.1734 | 273.86 | 266.04 | 0.6513 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 384.51 |  | 378.9649 | 1.4632 | 384.565 | 377.43 | 4.7411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 584.88 |  | 579.184 | 0.9835 | 603.25 | 584.69 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 940.78 |  | 933.0839 | 0.8248 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.45 |  | 464.3378 | 0.8856 | 477.73 | 460.77 | 4.4359 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.22 |  | 137.9501 | 0.9205 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.6 |  | 162.1802 | 2.7252 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 238 |  | 235.7055 | 0.9734 | 256.145 | 236.73 | 1.4328 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 636.43 |  | 624.8722 | 1.8496 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 341.04 |  | 335.8906 | 1.533 | 354.09 | 338.14 | 4.5713 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.75 |  | 84.9964 | 3.2397 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.46 |  | 255.6257 | 1.8911 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1582.19 |  | 1571.6566 | 0.6702 | 1586.01 | 1565.95 | 0.7066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 477.83 |  | 476.706 | 0.2358 | 494.87 | 477.03 | 4.2547 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 266.27 |  | 265.5295 | 0.2789 | 276.85 | 267.14 | 1.998 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 191.67 |  | 189.9241 | 0.9192 | 194.96 | 189.48 | 0.0835 | watch_only | none |
| TER | semiconductor_test_packaging | 310.67 |  | 305.8226 | 1.585 | 315.21 | 304.11 | 0.5955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 234.93 |  | 236.8832 | -0.8245 | 248.8 | 236.42 | 0.5576 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 46.53 |  | 47.1073 | -1.2255 | 51.64 | 47.435 | 0.2794 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.465 |  | 42.562 | -0.2279 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.815 |  | 119.3513 | 1.2264 | 121 | 117.72 | 4.0806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 282.13 |  | 281.5467 | 0.2072 | 296.8 | 283.22 | 0.9499 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LIN | industrial_gases | 517.83 |  | 518.6504 | -0.1582 | 518.6 | 511.495 | 4.4358 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.95 |  | 296.3217 | -0.4629 | 297.25 | 293.555 | 4.4177 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.04 |  | 26.3954 | 2.4421 | 27 | 25.42 | 3.8831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.47 |  | 33.4004 | 3.2023 | 35.08 | 33.52 | 0.058 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.03 |  | 19.9138 | 0.5835 | 20.97 | 19.755 | 0.0999 | watch_only | none |
| SNDK | memory_hbm_storage | 1106.94 |  | 1102.0495 | 0.4438 | 1185.19 | 1114.57 | 2.4925 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 442.59 |  | 434.001 | 1.979 | 465.04 | 435.22 | 3.1903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 728.07 |  | 722.6115 | 0.7554 | 774.805 | 719.02 | 0.4711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.51 |  | 229.8757 | 0.2759 | 233.05 | 229.7 | 0.0434 | watch_only | none |
| META | cloud_ai_capex | 593.07 |  | 593.1099 | -0.0067 | 600.765 | 594.21 | 0.1012 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 247.56 |  | 244.675 | 1.1791 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.4 |  | 131.2845 | 1.6114 | 136.45 | 131.735 | 1.7241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
