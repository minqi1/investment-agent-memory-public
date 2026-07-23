# Intraday State

- Generated at: `2026-07-24T00:26:34+08:00`
- Market time ET: `2026-07-23T12:26:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'below_opening_15m_low': 6, 'below_vwap': 14, 'spread_too_wide_or_missing': 16, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.04 |  | 693.0709 | 0.1398 | 698.65 | 693.24 | 0.0245 | watch_only | none |
| SOXX | semiconductor_index | 551.8 |  | 550.8928 | 0.1647 | 557.38 | 545.965 | 0.0924 | watch_only | none |
| SMH | semiconductor_index | 581.515 |  | 581.1989 | 0.0544 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| SPY | market_regime | 739.39 |  | 738.8193 | 0.0772 | 742.515 | 738.54 | 0.0392 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 568.75 |  | 566.2782 | 0.4365 | 566.18 | 548.47 | 0.2092 | buy_precheck_manual_confirm | none |
| 2 | CIEN | ai_networking_optical | 409.13 |  | 407.9468 | 0.29 | 408.58 | 397.9 | 0.2298 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 31.965 |  | 31.4544 | 1.6232 | 31.52 | 30.23 | 0.0626 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 409.13 |  | 407.9468 | 0.29 | 408.58 | 397.9 | 0.2298 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 581.515 |  | 581.1989 | 0.0544 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| 3 | SOXX | semiconductor_index | 551.8 |  | 550.8928 | 0.1647 | 557.38 | 545.965 | 0.0924 | watch_only | none |
| 4 | ASML | semiconductor_equipment | 1806.01 |  | 1803.8395 | 0.1203 | 1806.11 | 1780.9 | 0.0847 | watch_only | none |
| 5 | IWM | market_regime | 291.92 |  | 291.698 | 0.0761 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| 6 | QQQ | market_regime | 694.04 |  | 693.0709 | 0.1398 | 698.65 | 693.24 | 0.0245 | watch_only | none |
| 7 | SPY | market_regime | 739.39 |  | 738.8193 | 0.0772 | 742.515 | 738.54 | 0.0392 | watch_only | none |
| 8 | CRWV | gpu_cloud_ai_factory | 83.125 |  | 82.9373 | 0.2264 | 84.415 | 80.64 | 0.0842 | watch_only | none |
| 9 | AMAT | semiconductor_equipment | 568.75 |  | 566.2782 | 0.4365 | 566.18 | 548.47 | 0.2092 | buy_precheck_manual_confirm | none |
| 10 | SKHY | memory_hbm_storage | 173.85 |  | 173.5429 | 0.177 | 177.88 | 168.18 | 0.2301 | watch_only | none |
| 11 | NVDA | ai_accelerator | 209.52 |  | 208.2614 | 0.6044 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| 12 | MU | memory_hbm_storage | 995.92 |  | 988.9521 | 0.7046 | 999.04 | 964.86 | 0.0372 | watch_only | none |
| 13 | HPE | ai_server_oem | 48.66 |  | 48.3365 | 0.6693 | 48.88 | 47.635 | 0.0822 | watch_only | none |
| 14 | ARM | ai_accelerator | 281.02 |  | 278.9776 | 0.7321 | 283 | 276.24 | 0.1708 | watch_only | none |
| 15 | GOOGL | cloud_ai_capex | 320.84 |  | 319.5211 | 0.4128 | 324.42 | 320.24 | 0.2774 | watch_only | none |
| 16 | TT | data_center_power_cooling | 478.245 |  | 476.721 | 0.3197 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 144.34 |  | 143.9515 | 0.2699 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 414.5 |  | 413.2833 | 0.2944 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 321.74 |  | 321.3457 | 0.1227 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | COHR | ai_networking_optical | 318.77 |  | 318.3398 | 0.1351 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 568.75 |  | 566.2782 | 0.4365 | 566.18 | 548.47 | 0.2092 | buy_precheck_manual_confirm | none |
| 2 | CIEN | ai_networking_optical | 409.13 |  | 407.9468 | 0.29 | 408.58 | 397.9 | 0.2298 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 31.965 |  | 31.4544 | 1.6232 | 31.52 | 30.23 | 0.0626 | buy_precheck_manual_confirm | none |
| 4 | SNDK | memory_hbm_storage | 1677.14 |  | 1630.602 | 2.854 | 1651.355 | 1560 | 3.8232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | STX | memory_hbm_storage | 933.62 |  | 924.0412 | 1.0366 | 933.5 | 908.955 | 4.0605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SMH | semiconductor_index | 581.515 |  | 581.1989 | 0.0544 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| 7 | SOXX | semiconductor_index | 551.8 |  | 550.8928 | 0.1647 | 557.38 | 545.965 | 0.0924 | watch_only | none |
| 8 | NVDA | ai_accelerator | 209.52 |  | 208.2614 | 0.6044 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| 9 | MU | memory_hbm_storage | 995.92 |  | 988.9521 | 0.7046 | 999.04 | 964.86 | 0.0372 | watch_only | none |
| 10 | ASML | semiconductor_equipment | 1806.01 |  | 1803.8395 | 0.1203 | 1806.11 | 1780.9 | 0.0847 | watch_only | none |
| 11 | IWM | market_regime | 291.92 |  | 291.698 | 0.0761 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| 12 | QQQ | market_regime | 694.04 |  | 693.0709 | 0.1398 | 698.65 | 693.24 | 0.0245 | watch_only | none |
| 13 | ARM | ai_accelerator | 281.02 |  | 278.9776 | 0.7321 | 283 | 276.24 | 0.1708 | watch_only | none |
| 14 | SPY | market_regime | 739.39 |  | 738.8193 | 0.0772 | 742.515 | 738.54 | 0.0392 | watch_only | none |
| 15 | GOOGL | cloud_ai_capex | 320.84 |  | 319.5211 | 0.4128 | 324.42 | 320.24 | 0.2774 | watch_only | none |
| 16 | HPE | ai_server_oem | 48.66 |  | 48.3365 | 0.6693 | 48.88 | 47.635 | 0.0822 | watch_only | none |
| 17 | SKHY | memory_hbm_storage | 173.85 |  | 173.5429 | 0.177 | 177.88 | 168.18 | 0.2301 | watch_only | none |
| 18 | CRWV | gpu_cloud_ai_factory | 83.125 |  | 82.9373 | 0.2264 | 84.415 | 80.64 | 0.0842 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 66.86 |  | 66.5572 | 0.455 | 68.245 | 66.7 | 0.015 | watch_only | none |
| 20 | AVGO | custom_silicon_networking | 391.39 |  | 392.7139 | -0.3371 | 397.34 | 390.54 | 1.464 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.04 |  | 693.0709 | 0.1398 | 698.65 | 693.24 | 0.0245 | watch_only | none |
| TQQQ | leveraged_tool | 66.86 |  | 66.5572 | 0.455 | 68.245 | 66.7 | 0.015 | watch_only | none |
| NVDA | ai_accelerator | 209.52 |  | 208.2614 | 0.6044 | 210.85 | 208.49 | 0.0095 | watch_only | none |
| MSFT | cloud_ai_capex | 380.69 |  | 383.0144 | -0.6069 | 391.71 | 387.245 | 0.725 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 321.13 |  | 321.2171 | -0.0271 | 323.25 | 320.82 | 0.0405 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 320.84 |  | 319.5211 | 0.4128 | 324.42 | 320.24 | 0.2774 | watch_only | none |
| AMD | ai_accelerator | 544.08 |  | 546.3741 | -0.4199 | 556.12 | 542.33 | 1.1598 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 417.66 |  | 416.5105 | 0.276 | 420.72 | 412.69 | 3.3233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.8 |  | 550.8928 | 0.1647 | 557.38 | 545.965 | 0.0924 | watch_only | none |
| SMH | semiconductor_index | 581.515 |  | 581.1989 | 0.0544 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| AVGO | custom_silicon_networking | 391.39 |  | 392.7139 | -0.3371 | 397.34 | 390.54 | 1.464 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 995.92 |  | 988.9521 | 0.7046 | 999.04 | 964.86 | 0.0372 | watch_only | none |
| MRVL | custom_silicon_networking | 209.45 |  | 209.9842 | -0.2544 | 213.785 | 207.665 | 0.1767 | below_vwap | below_vwap |
| DELL | ai_server_oem | 444.86 |  | 443.9787 | 0.1985 | 450.07 | 438.55 | 0.4271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.66 |  | 48.3365 | 0.6693 | 48.88 | 47.635 | 0.0822 | watch_only | none |
| SMCI | ai_server_oem | 31.965 |  | 31.4544 | 1.6232 | 31.52 | 30.23 | 0.0626 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.39 |  | 738.8193 | 0.0772 | 742.515 | 738.54 | 0.0392 | watch_only | none |
| IWM | market_regime | 291.92 |  | 291.698 | 0.0761 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| ORCL | cloud_ai_capex | 121.205 |  | 122.2374 | -0.8446 | 124.22 | 122.07 | 0.0578 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.125 |  | 82.9373 | 0.2264 | 84.415 | 80.64 | 0.0842 | watch_only | none |
| VRT | data_center_power_cooling | 305.46 |  | 306.4654 | -0.328 | 311.13 | 303.96 | 0.9952 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.5 |  | 413.2833 | 0.2944 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.28 |  | 652.4855 | -0.338 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1021.15 |  | 1011.401 | 0.9639 | 1023.33 | 979.08 | 2.6186 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.245 |  | 476.721 | 0.3197 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.34 |  | 143.9515 | 0.2699 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.29 |  | 176.6307 | 0.3733 | 177.84 | 173.19 | 2.2562 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 318.77 |  | 318.3398 | 0.1351 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 846.45 |  | 859.1489 | -1.4781 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 409.13 |  | 407.9468 | 0.29 | 408.58 | 397.9 | 0.2298 | buy_precheck_manual_confirm | none |
| AAOI | ai_networking_optical | 114.37 |  | 114.7922 | -0.3678 | 118.01 | 108.505 | 0.3585 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 328.17 |  | 327.5931 | 0.1761 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.01 |  | 1803.8395 | 0.1203 | 1806.11 | 1780.9 | 0.0847 | watch_only | none |
| AMAT | semiconductor_equipment | 568.75 |  | 566.2782 | 0.4365 | 566.18 | 548.47 | 0.2092 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.74 |  | 321.3457 | 0.1227 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.09 |  | 215.6696 | 0.1949 | 217.88 | 212.99 | 2.9108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 375.08 |  | 371.6566 | 0.9211 | 376.78 | 363.37 | 4.0418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 294.66 |  | 295.5904 | -0.3148 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.965 |  | 65.3197 | -0.543 | 67.455 | 65.81 | 1.293 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.86 |  | 135.3758 | 0.3577 | 137.81 | 135.66 | 4.4237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 341.2 |  | 342.8499 | -0.4812 | 347.92 | 341.755 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.43 |  | 507.6882 | -0.2478 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.26 |  | 296.3339 | -0.3624 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.01 |  | 30.0669 | -0.1891 | 31.13 | 29.12 | 1.6328 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.45 |  | 41.8666 | -0.995 | 43.21 | 40.51 | 0.0483 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.03 |  | 24.0427 | -0.0528 | 24.46 | 23.265 | 0.1248 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1677.14 |  | 1630.602 | 2.854 | 1651.355 | 1560 | 3.8232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 572.85 |  | 563.3032 | 1.6948 | 576.24 | 556.3 | 0.6721 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 933.62 |  | 924.0412 | 1.0366 | 933.5 | 908.955 | 4.0605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.69 |  | 234.3253 | 0.1556 | 238.285 | 235.71 | 0.0511 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 603.96 |  | 603.83 | 0.0215 | 614.15 | 605.39 | 0.5083 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 281.02 |  | 278.9776 | 0.7321 | 283 | 276.24 | 0.1708 | watch_only | none |
| SKHY | memory_hbm_storage | 173.85 |  | 173.5429 | 0.177 | 177.88 | 168.18 | 0.2301 | watch_only | none |
