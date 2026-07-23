# Intraday State

- Generated at: `2026-07-23T22:08:49+08:00`
- Market time ET: `2026-07-23T10:08:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 7, 'watch_only': 11, 'below_opening_15m_low': 3, 'spread_too_wide_or_missing': 28, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.18 |  | 696.2027 | -0.0033 | 698.65 | 693.24 | 0.0847 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 556.53 |  | 553.5564 | 0.5372 | 557.38 | 545.965 | 0.124 | watch_only | none |
| SMH | semiconductor_index | 585.57 |  | 582.3112 | 0.5596 | 585.98 | 576.635 | 0.1042 | watch_only | none |
| SPY | market_regime | 740.525 |  | 740.6217 | -0.0131 | 742.515 | 738.54 | 0.0108 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1811.255 |  | 1800.7988 | 0.5806 | 1806.11 | 1780.9 | 0.2059 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 178.59 |  | 177.4537 | 0.6403 | 177.84 | 173.19 | 0.3136 | buy_precheck_manual_confirm | none |
| 3 | LRCX | semiconductor_equipment | 323.09 |  | 320.5024 | 0.8074 | 322.4 | 317.27 | 0.2538 | buy_precheck_manual_confirm | none |
| 4 | HPE | ai_server_oem | 49.015 |  | 48.5458 | 0.9665 | 48.88 | 47.635 | 0.1224 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 32.09 |  | 31.4539 | 2.0223 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |
| 6 | AAOI | ai_networking_optical | 118.17 |  | 116.3032 | 1.6051 | 118.01 | 108.505 | 0.3385 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 209.75 |  | 209.3535 | 0.1894 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 2 | ASML | semiconductor_equipment | 1811.255 |  | 1800.7988 | 0.5806 | 1806.11 | 1780.9 | 0.2059 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 292.24 |  | 291.8953 | 0.1181 | 293.01 | 290.365 | 0.0068 | watch_only | none |
| 4 | ANET | ai_networking_optical | 178.59 |  | 177.4537 | 0.6403 | 177.84 | 173.19 | 0.3136 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 321.38 |  | 321.1294 | 0.078 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| 6 | DELL | ai_server_oem | 444.13 |  | 443.6447 | 0.1094 | 450.07 | 438.55 | 0.1711 | watch_only | none |
| 7 | SMH | semiconductor_index | 585.57 |  | 582.3112 | 0.5596 | 585.98 | 576.635 | 0.1042 | watch_only | none |
| 8 | SOXX | semiconductor_index | 556.53 |  | 553.5564 | 0.5372 | 557.38 | 545.965 | 0.124 | watch_only | none |
| 9 | HPE | ai_server_oem | 49.015 |  | 48.5458 | 0.9665 | 48.88 | 47.635 | 0.1224 | buy_precheck_manual_confirm | none |
| 10 | ARM | ai_accelerator | 281.3 |  | 280.178 | 0.4005 | 283 | 276.24 | 0.3271 | watch_only | none |
| 11 | LRCX | semiconductor_equipment | 323.09 |  | 320.5024 | 0.8074 | 322.4 | 317.27 | 0.2538 | buy_precheck_manual_confirm | none |
| 12 | APD | industrial_gases | 297.39 |  | 297.3165 | 0.0247 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 137.38 |  | 137.0565 | 0.236 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ETN | data_center_power_cooling | 415.99 |  | 413.3391 | 0.6413 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | IREN | high_beta_ai_infrastructure | 42.93 |  | 42.3383 | 1.3976 | 43.21 | 40.51 | 0.0932 | watch_only | none |
| 16 | ONTO | semiconductor_test_packaging | 301.89 |  | 299.7648 | 0.7089 | 301.305 | 293.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 395.5 |  | 394.2461 | 0.3181 | 397.34 | 390.54 | 2.5284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | JCI | data_center_power_cooling | 144.05 |  | 144.0362 | 0.0096 | 145.035 | 141.815 | 4.9636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | KLAC | semiconductor_equipment | 216.5 |  | 216.0251 | 0.2198 | 217.88 | 212.99 | 4.1755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 552.03 |  | 550.5001 | 0.2779 | 556.12 | 542.33 | 1.8586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1811.255 |  | 1800.7988 | 0.5806 | 1806.11 | 1780.9 | 0.2059 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 178.59 |  | 177.4537 | 0.6403 | 177.84 | 173.19 | 0.3136 | buy_precheck_manual_confirm | none |
| 3 | LRCX | semiconductor_equipment | 323.09 |  | 320.5024 | 0.8074 | 322.4 | 317.27 | 0.2538 | buy_precheck_manual_confirm | none |
| 4 | HPE | ai_server_oem | 49.015 |  | 48.5458 | 0.9665 | 48.88 | 47.635 | 0.1224 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 32.09 |  | 31.4539 | 2.0223 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |
| 6 | AAOI | ai_networking_optical | 118.17 |  | 116.3032 | 1.6051 | 118.01 | 108.505 | 0.3385 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 570.27 |  | 562.3153 | 1.4146 | 566.18 | 548.47 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | PWR | data_center_power_cooling | 657.35 |  | 654.0646 | 0.5023 | 656.38 | 642.37 | 0.8337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | VRT | data_center_power_cooling | 312.28 |  | 308.6406 | 1.1792 | 311.13 | 303.96 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 415.99 |  | 413.3391 | 0.6413 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 301.89 |  | 299.7648 | 0.7089 | 301.305 | 293.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | COHR | ai_networking_optical | 324.76 |  | 319.1897 | 1.7451 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | CIEN | ai_networking_optical | 411.895 |  | 407.5668 | 1.062 | 408.58 | 397.9 | 0.942 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TER | semiconductor_test_packaging | 376.8 |  | 372.889 | 1.0488 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 55.76 |  | 55.2317 | 0.9566 | 55.76 | 54.445 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CRWV | gpu_cloud_ai_factory | 84.88 |  | 83.3182 | 1.8746 | 84.415 | 80.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SMH | semiconductor_index | 585.57 |  | 582.3112 | 0.5596 | 585.98 | 576.635 | 0.1042 | watch_only | none |
| 18 | SOXX | semiconductor_index | 556.53 |  | 553.5564 | 0.5372 | 557.38 | 545.965 | 0.124 | watch_only | none |
| 19 | NVDA | ai_accelerator | 209.75 |  | 209.3535 | 0.1894 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 20 | IWM | market_regime | 292.24 |  | 291.8953 | 0.1181 | 293.01 | 290.365 | 0.0068 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.18 |  | 696.2027 | -0.0033 | 698.65 | 693.24 | 0.0847 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.55 |  | 67.4557 | 0.1398 | 68.245 | 66.7 | 0.0296 | watch_only | none |
| NVDA | ai_accelerator | 209.75 |  | 209.3535 | 0.1894 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 386.71 |  | 388.8669 | -0.5547 | 391.71 | 387.245 | 0.0776 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.38 |  | 321.1294 | 0.078 | 323.25 | 320.82 | 0.0187 | watch_only | none |
| GOOGL | cloud_ai_capex | 319.8 |  | 321.1511 | -0.4207 | 324.42 | 320.24 | 0.3502 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 552.03 |  | 550.5001 | 0.2779 | 556.12 | 542.33 | 1.8586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 420.18 |  | 418.0079 | 0.5196 | 420.72 | 412.69 | 0.4974 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 556.53 |  | 553.5564 | 0.5372 | 557.38 | 545.965 | 0.124 | watch_only | none |
| SMH | semiconductor_index | 585.57 |  | 582.3112 | 0.5596 | 585.98 | 576.635 | 0.1042 | watch_only | none |
| AVGO | custom_silicon_networking | 395.5 |  | 394.2461 | 0.3181 | 397.34 | 390.54 | 2.5284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 995.57 |  | 986.0583 | 0.9646 | 999.04 | 964.86 | 0.7302 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.7 |  | 212.105 | 0.752 | 213.785 | 207.665 | 4.5297 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 444.13 |  | 443.6447 | 0.1094 | 450.07 | 438.55 | 0.1711 | watch_only | none |
| HPE | ai_server_oem | 49.015 |  | 48.5458 | 0.9665 | 48.88 | 47.635 | 0.1224 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 32.09 |  | 31.4539 | 2.0223 | 31.52 | 30.23 | 0.0623 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 740.525 |  | 740.6217 | -0.0131 | 742.515 | 738.54 | 0.0108 | below_vwap | below_vwap |
| IWM | market_regime | 292.24 |  | 291.8953 | 0.1181 | 293.01 | 290.365 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 123.87 |  | 123.4457 | 0.3437 | 124.22 | 122.07 | 2.9709 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 84.88 |  | 83.3182 | 1.8746 | 84.415 | 80.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 312.28 |  | 308.6406 | 1.1792 | 311.13 | 303.96 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 415.99 |  | 413.3391 | 0.6413 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 657.35 |  | 654.0646 | 0.5023 | 656.38 | 642.37 | 0.8337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1022.02 |  | 1007.7347 | 1.4176 | 1023.33 | 979.08 | 3.0988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.575 |  | 476.7419 | -0.035 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 144.05 |  | 144.0362 | 0.0096 | 145.035 | 141.815 | 4.9636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 178.59 |  | 177.4537 | 0.6403 | 177.84 | 173.19 | 0.3136 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 324.76 |  | 319.1897 | 1.7451 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 870.24 |  | 873.3198 | -0.3527 | 880.26 | 833 | 4.5539 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 411.895 |  | 407.5668 | 1.062 | 408.58 | 397.9 | 0.942 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 118.17 |  | 116.3032 | 1.6051 | 118.01 | 108.505 | 0.3385 | buy_precheck_manual_confirm | none |
| ALAB | ai_networking_optical | 339.34 |  | 335.9571 | 1.007 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1811.255 |  | 1800.7988 | 0.5806 | 1806.11 | 1780.9 | 0.2059 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 570.27 |  | 562.3153 | 1.4146 | 566.18 | 548.47 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 323.09 |  | 320.5024 | 0.8074 | 322.4 | 317.27 | 0.2538 | buy_precheck_manual_confirm | none |
| KLAC | semiconductor_equipment | 216.5 |  | 216.0251 | 0.2198 | 217.88 | 212.99 | 4.1755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 376.8 |  | 372.889 | 1.0488 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.89 |  | 299.7648 | 0.7089 | 301.305 | 293.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.95 |  | 66.6955 | 0.3815 | 67.455 | 65.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.76 |  | 55.2317 | 0.9566 | 55.76 | 54.445 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.38 |  | 137.0565 | 0.236 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.28 |  | 345.2119 | 0.5991 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 507.09 |  | 506.9664 | 0.0244 | 510.71 | 502.72 | 4.6027 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.39 |  | 297.3165 | 0.0247 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 31.01 |  | 30.4496 | 1.8403 | 31.13 | 29.12 | 0.129 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 42.93 |  | 42.3383 | 1.3976 | 43.21 | 40.51 | 0.0932 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 24.365 |  | 24.1068 | 1.071 | 24.46 | 23.265 | 0.1231 | watch_only | none |
| SNDK | memory_hbm_storage | 1640.17 |  | 1618.6483 | 1.3296 | 1651.355 | 1560 | 2.4388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 560.11 |  | 566.8573 | -1.1903 | 576.24 | 556.3 | 3.7493 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 930.07 |  | 926.697 | 0.364 | 933.5 | 908.955 | 4.605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 235.15 |  | 236.4892 | -0.5663 | 238.285 | 235.71 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 608.52 |  | 610.2019 | -0.2756 | 614.15 | 605.39 | 0.2646 | below_vwap | below_vwap |
| ARM | ai_accelerator | 281.3 |  | 280.178 | 0.4005 | 283 | 276.24 | 0.3271 | watch_only | none |
| SKHY | memory_hbm_storage | 175.71 |  | 174.0544 | 0.9512 | 177.88 | 168.18 | 1.0017 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
