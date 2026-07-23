# Intraday State

- Generated at: `2026-07-24T00:42:49+08:00`
- Market time ET: `2026-07-23T12:42:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_opening_15m_low': 8, 'below_vwap': 13, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 2, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.25 |  | 693.1472 | 0.1591 | 698.65 | 693.24 | 0.036 | watch_only | none |
| SOXX | semiconductor_index | 553.9 |  | 550.9716 | 0.5315 | 557.38 | 545.965 | 0.0867 | watch_only | none |
| SMH | semiconductor_index | 584.8 |  | 581.2224 | 0.6155 | 585.98 | 576.635 | 0.0821 | watch_only | none |
| SPY | market_regime | 739.21 |  | 738.8418 | 0.0498 | 742.515 | 738.54 | 0.0216 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.8 |  | 1803.9696 | 0.2678 | 1806.11 | 1780.9 | 0.1216 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.345 |  | 31.5486 | 2.5244 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.8 |  | 1803.9696 | 0.2678 | 1806.11 | 1780.9 | 0.1216 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 291.745 |  | 291.7005 | 0.0152 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 3 | QQQ | market_regime | 694.25 |  | 693.1472 | 0.1591 | 698.65 | 693.24 | 0.036 | watch_only | none |
| 4 | SPY | market_regime | 739.21 |  | 738.8418 | 0.0498 | 742.515 | 738.54 | 0.0216 | watch_only | none |
| 5 | SMH | semiconductor_index | 584.8 |  | 581.2224 | 0.6155 | 585.98 | 576.635 | 0.0821 | watch_only | none |
| 6 | SOXX | semiconductor_index | 553.9 |  | 550.9716 | 0.5315 | 557.38 | 545.965 | 0.0867 | watch_only | none |
| 7 | NVDA | ai_accelerator | 210 |  | 208.3641 | 0.7851 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 216.9 |  | 215.6976 | 0.5575 | 217.88 | 212.99 | 0.1706 | watch_only | none |
| 9 | TT | data_center_power_cooling | 477.895 |  | 476.7459 | 0.241 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 144.175 |  | 143.9559 | 0.1522 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 414.21 |  | 413.3513 | 0.2077 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | LRCX | semiconductor_equipment | 322.16 |  | 321.3741 | 0.2445 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | CORZ | high_beta_ai_infrastructure | 24.065 |  | 24.0441 | 0.087 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 14 | AMAT | semiconductor_equipment | 569.38 |  | 566.3957 | 0.5269 | 566.18 | 548.47 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | CIEN | ai_networking_optical | 410.86 |  | 408.1408 | 0.6662 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MRVL | custom_silicon_networking | 210.08 |  | 209.98 | 0.0476 | 213.785 | 207.665 | 0.5188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SKHY | memory_hbm_storage | 174.22 |  | 173.6216 | 0.3447 | 177.88 | 168.18 | 0.8725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ANET | ai_networking_optical | 177.94 |  | 176.6867 | 0.7094 | 177.84 | 173.19 | 1.3993 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TSM | foundry | 418.68 |  | 416.6267 | 0.4928 | 420.72 | 412.69 | 0.9291 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SMCI | ai_server_oem | 32.345 |  | 31.5486 | 2.5244 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.8 |  | 1803.9696 | 0.2678 | 1806.11 | 1780.9 | 0.1216 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.345 |  | 31.5486 | 2.5244 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| 3 | MU | memory_hbm_storage | 1004.79 |  | 990.3701 | 1.456 | 999.04 | 964.86 | 0.5374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | AMAT | semiconductor_equipment | 569.38 |  | 566.3957 | 0.5269 | 566.18 | 548.47 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 177.94 |  | 176.6867 | 0.7094 | 177.84 | 173.19 | 1.3993 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ARM | ai_accelerator | 283.395 |  | 279.2583 | 1.4813 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | CIEN | ai_networking_optical | 410.86 |  | 408.1408 | 0.6662 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SNDK | memory_hbm_storage | 1687.35 |  | 1635.7816 | 3.1525 | 1651.355 | 1560 | 0.6798 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | STX | memory_hbm_storage | 935.77 |  | 924.646 | 1.203 | 933.5 | 908.955 | 3.3972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMH | semiconductor_index | 584.8 |  | 581.2224 | 0.6155 | 585.98 | 576.635 | 0.0821 | watch_only | none |
| 11 | SOXX | semiconductor_index | 553.9 |  | 550.9716 | 0.5315 | 557.38 | 545.965 | 0.0867 | watch_only | none |
| 12 | NVDA | ai_accelerator | 210 |  | 208.3641 | 0.7851 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 13 | KLAC | semiconductor_equipment | 216.9 |  | 215.6976 | 0.5575 | 217.88 | 212.99 | 0.1706 | watch_only | none |
| 14 | IWM | market_regime | 291.745 |  | 291.7005 | 0.0152 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 15 | QQQ | market_regime | 694.25 |  | 693.1472 | 0.1591 | 698.65 | 693.24 | 0.036 | watch_only | none |
| 16 | SPY | market_regime | 739.21 |  | 738.8418 | 0.0498 | 742.515 | 738.54 | 0.0216 | watch_only | none |
| 17 | WDC | memory_hbm_storage | 572.745 |  | 563.8172 | 1.5835 | 576.24 | 556.3 | 0.2165 | watch_only | none |
| 18 | CORZ | high_beta_ai_infrastructure | 24.065 |  | 24.0441 | 0.087 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 66.95 |  | 66.5828 | 0.5514 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| 20 | AVGO | custom_silicon_networking | 392.345 |  | 392.6874 | -0.0872 | 397.34 | 390.54 | 1.1444 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.25 |  | 693.1472 | 0.1591 | 698.65 | 693.24 | 0.036 | watch_only | none |
| TQQQ | leveraged_tool | 66.95 |  | 66.5828 | 0.5514 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| NVDA | ai_accelerator | 210 |  | 208.3641 | 0.7851 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.4 |  | 382.9269 | -0.6599 | 391.71 | 387.245 | 0.623 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.375 |  | 321.1676 | -0.2468 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.54 |  | 319.5472 | -0.0023 | 324.42 | 320.24 | 0.1909 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 545.54 |  | 546.3448 | -0.1473 | 556.12 | 542.33 | 4.7274 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 418.68 |  | 416.6267 | 0.4928 | 420.72 | 412.69 | 0.9291 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.9 |  | 550.9716 | 0.5315 | 557.38 | 545.965 | 0.0867 | watch_only | none |
| SMH | semiconductor_index | 584.8 |  | 581.2224 | 0.6155 | 585.98 | 576.635 | 0.0821 | watch_only | none |
| AVGO | custom_silicon_networking | 392.345 |  | 392.6874 | -0.0872 | 397.34 | 390.54 | 1.1444 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 1004.79 |  | 990.3701 | 1.456 | 999.04 | 964.86 | 0.5374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 210.08 |  | 209.98 | 0.0476 | 213.785 | 207.665 | 0.5188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 447.44 |  | 444.0926 | 0.7538 | 450.07 | 438.55 | 0.3755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.65 |  | 48.3561 | 0.6078 | 48.88 | 47.635 | 0.7811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SMCI | ai_server_oem | 32.345 |  | 31.5486 | 2.5244 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.21 |  | 738.8418 | 0.0498 | 742.515 | 738.54 | 0.0216 | watch_only | none |
| IWM | market_regime | 291.745 |  | 291.7005 | 0.0152 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 120.875 |  | 122.1913 | -1.0773 | 124.22 | 122.07 | 0.0496 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.555 |  | 82.9348 | -0.458 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 305.84 |  | 306.4296 | -0.1924 | 311.13 | 303.96 | 0.412 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.21 |  | 413.3513 | 0.2077 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 651.21 |  | 652.3813 | -0.1795 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1021.355 |  | 1011.6616 | 0.9582 | 1023.33 | 979.08 | 2.7992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.895 |  | 476.7459 | 0.241 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.175 |  | 143.9559 | 0.1522 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.94 |  | 176.6867 | 0.7094 | 177.84 | 173.19 | 1.3993 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 317.855 |  | 318.3547 | -0.157 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 853.12 |  | 858.8414 | -0.6662 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 410.86 |  | 408.1408 | 0.6662 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 114.135 |  | 114.7739 | -0.5567 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.78 |  | 327.7431 | 0.9266 | 341.68 | 327.43 | 4.8945 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1808.8 |  | 1803.9696 | 0.2678 | 1806.11 | 1780.9 | 0.1216 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 569.38 |  | 566.3957 | 0.5269 | 566.18 | 548.47 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 322.16 |  | 321.3741 | 0.2445 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.9 |  | 215.6976 | 0.5575 | 217.88 | 212.99 | 0.1706 | watch_only | none |
| TER | semiconductor_test_packaging | 375.78 |  | 371.8938 | 1.045 | 376.78 | 363.37 | 3.8932 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.91 |  | 295.46 | -0.5246 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.57 |  | 65.3218 | 0.38 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.88 |  | 135.4015 | 0.3534 | 137.81 | 135.66 | 4.3789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 345.93 |  | 342.8795 | 0.8897 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.73 |  | 507.652 | -0.1816 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.455 |  | 296.2834 | -0.2796 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.74 |  | 30.064 | -1.0778 | 31.13 | 29.12 | 0.0672 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.855 |  | 41.8358 | -2.3445 | 43.21 | 40.51 | 0.049 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.065 |  | 24.0441 | 0.087 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| SNDK | memory_hbm_storage | 1687.35 |  | 1635.7816 | 3.1525 | 1651.355 | 1560 | 0.6798 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 572.745 |  | 563.8172 | 1.5835 | 576.24 | 556.3 | 0.2165 | watch_only | none |
| STX | memory_hbm_storage | 935.77 |  | 924.646 | 1.203 | 933.5 | 908.955 | 3.3972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.14 |  | 234.3444 | -0.0872 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 602.6 |  | 603.7978 | -0.1984 | 614.15 | 605.39 | 0.5078 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 283.395 |  | 279.2583 | 1.4813 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 174.22 |  | 173.6216 | 0.3447 | 177.88 | 168.18 | 0.8725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
