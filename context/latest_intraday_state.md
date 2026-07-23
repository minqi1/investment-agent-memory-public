# Intraday State

- Generated at: `2026-07-24T00:35:01+08:00`
- Market time ET: `2026-07-23T12:35:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 20, 'below_vwap': 14, 'price_stale_or_missing': 2, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.15 |  | 693.1035 | 0.151 | 698.65 | 693.24 | 0.0086 | watch_only | none |
| SOXX | semiconductor_index | 552.67 |  | 550.9032 | 0.3207 | 557.38 | 545.965 | 0.0905 | watch_only | none |
| SMH | semiconductor_index | 582.195 |  | 581.2107 | 0.1693 | 585.98 | 576.635 | 0.0739 | watch_only | none |
| SPY | market_regime | 739.27 |  | 738.8317 | 0.0593 | 742.515 | 738.54 | 0.0243 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 568.09 |  | 566.3276 | 0.3112 | 566.18 | 548.47 | 0.1655 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.24 |  | 31.4884 | 2.3868 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 568.09 |  | 566.3276 | 0.3112 | 566.18 | 548.47 | 0.1655 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 582.195 |  | 581.2107 | 0.1693 | 585.98 | 576.635 | 0.0739 | watch_only | none |
| 3 | SOXX | semiconductor_index | 552.67 |  | 550.9032 | 0.3207 | 557.38 | 545.965 | 0.0905 | watch_only | none |
| 4 | ASML | semiconductor_equipment | 1805.13 |  | 1803.904 | 0.068 | 1806.11 | 1780.9 | 0.1064 | watch_only | none |
| 5 | QQQ | market_regime | 694.15 |  | 693.1035 | 0.151 | 698.65 | 693.24 | 0.0086 | watch_only | none |
| 6 | SPY | market_regime | 739.27 |  | 738.8317 | 0.0593 | 742.515 | 738.54 | 0.0243 | watch_only | none |
| 7 | TSM | foundry | 417.96 |  | 416.5421 | 0.3404 | 420.72 | 412.69 | 0.2584 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 216.205 |  | 215.6782 | 0.2443 | 217.88 | 212.99 | 0.1526 | watch_only | none |
| 9 | NVDA | ai_accelerator | 209.74 |  | 208.2987 | 0.692 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 10 | HPE | ai_server_oem | 48.66 |  | 48.3413 | 0.6594 | 48.88 | 47.635 | 0.0617 | watch_only | none |
| 11 | TT | data_center_power_cooling | 478.05 |  | 476.7241 | 0.2781 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 144.04 |  | 143.9541 | 0.0597 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ETN | data_center_power_cooling | 414.61 |  | 413.3043 | 0.3159 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | LRCX | semiconductor_equipment | 321.53 |  | 321.3559 | 0.0542 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | COHR | ai_networking_optical | 318.54 |  | 318.3464 | 0.0608 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ARM | ai_accelerator | 281 |  | 279.0253 | 0.7077 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MKSI | semiconductor_materials | 344.3 |  | 342.8588 | 0.4203 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 135.93 |  | 135.396 | 0.3944 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ALAB | ai_networking_optical | 329.41 |  | 327.6293 | 0.5435 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SKHY | memory_hbm_storage | 173.9 |  | 173.5574 | 0.1974 | 177.88 | 168.18 | 2.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 568.09 |  | 566.3276 | 0.3112 | 566.18 | 548.47 | 0.1655 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.24 |  | 31.4884 | 2.3868 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |
| 3 | MU | memory_hbm_storage | 1003.38 |  | 989.4611 | 1.4067 | 999.04 | 964.86 | 1.6424 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | TSM | foundry | 417.96 |  | 416.5421 | 0.3404 | 420.72 | 412.69 | 0.2584 | watch_only | none |
| 5 | CIEN | ai_networking_optical | 409.62 |  | 407.9734 | 0.4036 | 408.58 | 397.9 | 4.055 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SNDK | memory_hbm_storage | 1683.66 |  | 1632.2648 | 3.1487 | 1651.355 | 1560 | 0.4051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SMH | semiconductor_index | 582.195 |  | 581.2107 | 0.1693 | 585.98 | 576.635 | 0.0739 | watch_only | none |
| 8 | SOXX | semiconductor_index | 552.67 |  | 550.9032 | 0.3207 | 557.38 | 545.965 | 0.0905 | watch_only | none |
| 9 | NVDA | ai_accelerator | 209.74 |  | 208.2987 | 0.692 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 10 | ASML | semiconductor_equipment | 1805.13 |  | 1803.904 | 0.068 | 1806.11 | 1780.9 | 0.1064 | watch_only | none |
| 11 | KLAC | semiconductor_equipment | 216.205 |  | 215.6782 | 0.2443 | 217.88 | 212.99 | 0.1526 | watch_only | none |
| 12 | QQQ | market_regime | 694.15 |  | 693.1035 | 0.151 | 698.65 | 693.24 | 0.0086 | watch_only | none |
| 13 | SPY | market_regime | 739.27 |  | 738.8317 | 0.0593 | 742.515 | 738.54 | 0.0243 | watch_only | none |
| 14 | HPE | ai_server_oem | 48.66 |  | 48.3413 | 0.6594 | 48.88 | 47.635 | 0.0617 | watch_only | none |
| 15 | TQQQ | leveraged_tool | 66.92 |  | 66.5699 | 0.5259 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| 16 | AVGO | custom_silicon_networking | 392.085 |  | 392.6846 | -0.1527 | 397.34 | 390.54 | 2.0251 | below_vwap | below_vwap,spread_too_wide |
| 17 | PWR | data_center_power_cooling | 650.87 |  | 652.4166 | -0.2371 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AMD | ai_accelerator | 544.65 |  | 546.3255 | -0.3067 | 556.12 | 542.33 | 1.5019 | below_vwap | below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 305.04 |  | 306.4438 | -0.4581 | 311.13 | 303.96 | 0.3508 | below_vwap | below_vwap,spread_too_wide |
| 20 | IWM | market_regime | 291.66 |  | 291.6998 | -0.0136 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.15 |  | 693.1035 | 0.151 | 698.65 | 693.24 | 0.0086 | watch_only | none |
| TQQQ | leveraged_tool | 66.92 |  | 66.5699 | 0.5259 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| NVDA | ai_accelerator | 209.74 |  | 208.2987 | 0.692 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.58 |  | 382.9756 | -0.6255 | 391.71 | 387.245 | 0.0447 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.18 |  | 321.1924 | -0.3152 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.98 |  | 319.5429 | 0.4497 | 324.42 | 320.24 | 0.62 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 544.65 |  | 546.3255 | -0.3067 | 556.12 | 542.33 | 1.5019 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 417.96 |  | 416.5421 | 0.3404 | 420.72 | 412.69 | 0.2584 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.67 |  | 550.9032 | 0.3207 | 557.38 | 545.965 | 0.0905 | watch_only | none |
| SMH | semiconductor_index | 582.195 |  | 581.2107 | 0.1693 | 585.98 | 576.635 | 0.0739 | watch_only | none |
| AVGO | custom_silicon_networking | 392.085 |  | 392.6846 | -0.1527 | 397.34 | 390.54 | 2.0251 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 1003.38 |  | 989.4611 | 1.4067 | 999.04 | 964.86 | 1.6424 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.45 |  | 209.9771 | -0.251 | 213.785 | 207.665 | 2.1342 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 446.265 |  | 444.0355 | 0.5021 | 450.07 | 438.55 | 1.2325 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.66 |  | 48.3413 | 0.6594 | 48.88 | 47.635 | 0.0617 | watch_only | none |
| SMCI | ai_server_oem | 32.24 |  | 31.4884 | 2.3868 | 31.52 | 30.23 | 0.031 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.27 |  | 738.8317 | 0.0593 | 742.515 | 738.54 | 0.0243 | watch_only | none |
| IWM | market_regime | 291.66 |  | 291.6998 | -0.0136 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 121.11 |  | 122.2088 | -0.8991 | 124.22 | 122.07 | 0.1073 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.84 |  | 82.941 | -0.1218 | 84.415 | 80.64 | 0.0845 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 305.04 |  | 306.4438 | -0.4581 | 311.13 | 303.96 | 0.3508 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.61 |  | 413.3043 | 0.3159 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.87 |  | 652.4166 | -0.2371 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1022.5 |  | 1011.6019 | 1.0773 | 1023.33 | 979.08 | 4.7922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.05 |  | 476.7241 | 0.2781 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.04 |  | 143.9541 | 0.0597 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.45 |  | 176.6501 | 0.4528 | 177.84 | 173.19 | 2.2542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 318.54 |  | 318.3464 | 0.0608 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 845.81 |  | 858.9932 | -1.5347 | 880.26 | 833 | 4.1688 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 409.62 |  | 407.9734 | 0.4036 | 408.58 | 397.9 | 4.055 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 114.23 |  | 114.7852 | -0.4837 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 329.41 |  | 327.6293 | 0.5435 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1805.13 |  | 1803.904 | 0.068 | 1806.11 | 1780.9 | 0.1064 | watch_only | none |
| AMAT | semiconductor_equipment | 568.09 |  | 566.3276 | 0.3112 | 566.18 | 548.47 | 0.1655 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.53 |  | 321.3559 | 0.0542 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.205 |  | 215.6782 | 0.2443 | 217.88 | 212.99 | 0.1526 | watch_only | none |
| TER | semiconductor_test_packaging | 376.05 |  | 371.7925 | 1.1451 | 376.78 | 363.37 | 3.8479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.26 |  | 295.513 | -0.7624 | 301.305 | 293.685 | 0.4092 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.41 |  | 65.3202 | 0.1375 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.93 |  | 135.396 | 0.3944 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 344.3 |  | 342.8588 | 0.4203 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.73 |  | 507.6666 | -0.1845 | 510.71 | 502.72 | 4.7027 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.59 |  | 296.2862 | -0.235 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.905 |  | 30.0663 | -0.5366 | 31.13 | 29.12 | 0.1338 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.15 |  | 41.8549 | -1.6841 | 43.21 | 40.51 | 0.0486 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.01 |  | 24.0425 | -0.135 | 24.46 | 23.265 | 0.1249 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1683.66 |  | 1632.2648 | 3.1487 | 1651.355 | 1560 | 0.4051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 572.67 |  | 563.6001 | 1.6093 | 576.24 | 556.3 | 0.6094 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 933.19 |  | 924.3861 | 0.9524 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234.765 |  | 234.3477 | 0.1781 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 604.22 |  | 603.8706 | 0.0579 | 614.15 | 605.39 | 0.8689 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 281 |  | 279.0253 | 0.7077 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 173.9 |  | 173.5574 | 0.1974 | 177.88 | 168.18 | 2.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
