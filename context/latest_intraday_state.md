# Intraday State

- Generated at: `2026-07-24T00:31:05+08:00`
- Market time ET: `2026-07-23T12:31:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'below_opening_15m_low': 6, 'below_vwap': 11, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 3, 'spread_too_wide_or_missing': 19}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.37 |  | 693.0864 | 0.1852 | 698.65 | 693.24 | 0.0302 | watch_only | none |
| SOXX | semiconductor_index | 553.18 |  | 550.8999 | 0.4139 | 557.38 | 545.965 | 0.038 | watch_only | none |
| SMH | semiconductor_index | 582.375 |  | 581.2048 | 0.2013 | 585.98 | 576.635 | 0.0687 | watch_only | none |
| SPY | market_regime | 739.455 |  | 738.8274 | 0.0849 | 742.515 | 738.54 | 0.027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 1004.01 |  | 989.2657 | 1.4904 | 999.04 | 964.86 | 0.238 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1808.02 |  | 1803.8917 | 0.2289 | 1806.11 | 1780.9 | 0.0548 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.15 |  | 31.4672 | 2.17 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.02 |  | 1803.8917 | 0.2289 | 1806.11 | 1780.9 | 0.0548 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 582.375 |  | 581.2048 | 0.2013 | 585.98 | 576.635 | 0.0687 | watch_only | none |
| 3 | IWM | market_regime | 291.86 |  | 291.6996 | 0.055 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| 4 | QQQ | market_regime | 694.37 |  | 693.0864 | 0.1852 | 698.65 | 693.24 | 0.0302 | watch_only | none |
| 5 | SPY | market_regime | 739.455 |  | 738.8274 | 0.0849 | 742.515 | 738.54 | 0.027 | watch_only | none |
| 6 | MRVL | custom_silicon_networking | 210.04 |  | 209.9826 | 0.0273 | 213.785 | 207.665 | 0.1428 | watch_only | none |
| 7 | SOXX | semiconductor_index | 553.18 |  | 550.8999 | 0.4139 | 557.38 | 545.965 | 0.038 | watch_only | none |
| 8 | NVDA | ai_accelerator | 209.65 |  | 208.2767 | 0.6594 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 9 | GOOGL | cloud_ai_capex | 320.89 |  | 319.5285 | 0.4261 | 324.42 | 320.24 | 0.1247 | watch_only | none |
| 10 | TSM | foundry | 418.12 |  | 416.5267 | 0.3825 | 420.72 | 412.69 | 0.1698 | watch_only | none |
| 11 | CRWV | gpu_cloud_ai_factory | 83.28 |  | 82.9395 | 0.4105 | 84.415 | 80.64 | 0.0961 | watch_only | none |
| 12 | KLAC | semiconductor_equipment | 216.52 |  | 215.6739 | 0.3923 | 217.88 | 212.99 | 0.1986 | watch_only | none |
| 13 | MU | memory_hbm_storage | 1004.01 |  | 989.2657 | 1.4904 | 999.04 | 964.86 | 0.238 | buy_precheck_manual_confirm | none |
| 14 | CIEN | ai_networking_optical | 409.375 |  | 407.95 | 0.3493 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TT | data_center_power_cooling | 478.05 |  | 476.7241 | 0.2781 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 144.17 |  | 143.9524 | 0.1511 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | LRCX | semiconductor_equipment | 322.08 |  | 321.3554 | 0.2255 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ALAB | ai_networking_optical | 328.44 |  | 327.6036 | 0.2553 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | CORZ | high_beta_ai_infrastructure | 24.055 |  | 24.0425 | 0.0521 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| 20 | HPE | ai_server_oem | 48.74 |  | 48.3396 | 0.8282 | 48.88 | 47.635 | 0.0821 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 1004.01 |  | 989.2657 | 1.4904 | 999.04 | 964.86 | 0.238 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1808.02 |  | 1803.8917 | 0.2289 | 1806.11 | 1780.9 | 0.0548 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.15 |  | 31.4672 | 2.17 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |
| 4 | AMAT | semiconductor_equipment | 570 |  | 566.3039 | 0.6527 | 566.18 | 548.47 | 4.8789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GEV | data_center_power_cooling | 1023.41 |  | 1011.5487 | 1.1726 | 1023.33 | 979.08 | 4.7879 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | TSM | foundry | 418.12 |  | 416.5267 | 0.3825 | 420.72 | 412.69 | 0.1698 | watch_only | none |
| 7 | CIEN | ai_networking_optical | 409.375 |  | 407.95 | 0.3493 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SNDK | memory_hbm_storage | 1688 |  | 1631.494 | 3.4635 | 1651.355 | 1560 | 4.0705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | STX | memory_hbm_storage | 935.82 |  | 924.3226 | 1.2439 | 933.5 | 908.955 | 0.5589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMH | semiconductor_index | 582.375 |  | 581.2048 | 0.2013 | 585.98 | 576.635 | 0.0687 | watch_only | none |
| 11 | SOXX | semiconductor_index | 553.18 |  | 550.8999 | 0.4139 | 557.38 | 545.965 | 0.038 | watch_only | none |
| 12 | NVDA | ai_accelerator | 209.65 |  | 208.2767 | 0.6594 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 13 | KLAC | semiconductor_equipment | 216.52 |  | 215.6739 | 0.3923 | 217.88 | 212.99 | 0.1986 | watch_only | none |
| 14 | IWM | market_regime | 291.86 |  | 291.6996 | 0.055 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| 15 | QQQ | market_regime | 694.37 |  | 693.0864 | 0.1852 | 698.65 | 693.24 | 0.0302 | watch_only | none |
| 16 | SPY | market_regime | 739.455 |  | 738.8274 | 0.0849 | 742.515 | 738.54 | 0.027 | watch_only | none |
| 17 | GOOGL | cloud_ai_capex | 320.89 |  | 319.5285 | 0.4261 | 324.42 | 320.24 | 0.1247 | watch_only | none |
| 18 | HPE | ai_server_oem | 48.74 |  | 48.3396 | 0.8282 | 48.88 | 47.635 | 0.0821 | watch_only | none |
| 19 | MRVL | custom_silicon_networking | 210.04 |  | 209.9826 | 0.0273 | 213.785 | 207.665 | 0.1428 | watch_only | none |
| 20 | CRWV | gpu_cloud_ai_factory | 83.28 |  | 82.9395 | 0.4105 | 84.415 | 80.64 | 0.0961 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.37 |  | 693.0864 | 0.1852 | 698.65 | 693.24 | 0.0302 | watch_only | none |
| TQQQ | leveraged_tool | 66.995 |  | 66.5656 | 0.645 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| NVDA | ai_accelerator | 209.65 |  | 208.2767 | 0.6594 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.59 |  | 382.9948 | -0.6279 | 391.71 | 387.245 | 0.1655 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.33 |  | 321.2044 | -0.2722 | 323.25 | 320.82 | 0.0718 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.89 |  | 319.5285 | 0.4261 | 324.42 | 320.24 | 0.1247 | watch_only | none |
| AMD | ai_accelerator | 545.255 |  | 546.3597 | -0.2022 | 556.12 | 542.33 | 1.5387 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 418.12 |  | 416.5267 | 0.3825 | 420.72 | 412.69 | 0.1698 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.18 |  | 550.8999 | 0.4139 | 557.38 | 545.965 | 0.038 | watch_only | none |
| SMH | semiconductor_index | 582.375 |  | 581.2048 | 0.2013 | 585.98 | 576.635 | 0.0687 | watch_only | none |
| AVGO | custom_silicon_networking | 391.465 |  | 392.6985 | -0.3141 | 397.34 | 390.54 | 1.8367 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 1004.01 |  | 989.2657 | 1.4904 | 999.04 | 964.86 | 0.238 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 210.04 |  | 209.9826 | 0.0273 | 213.785 | 207.665 | 0.1428 | watch_only | none |
| DELL | ai_server_oem | 446.44 |  | 444.0003 | 0.5495 | 450.07 | 438.55 | 1.3283 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.74 |  | 48.3396 | 0.8282 | 48.88 | 47.635 | 0.0821 | watch_only | none |
| SMCI | ai_server_oem | 32.15 |  | 31.4672 | 2.17 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.455 |  | 738.8274 | 0.0849 | 742.515 | 738.54 | 0.027 | watch_only | none |
| IWM | market_regime | 291.86 |  | 291.6996 | 0.055 | 293.01 | 290.365 | 0.0103 | watch_only | none |
| ORCL | cloud_ai_capex | 121.24 |  | 122.2181 | -0.8003 | 124.22 | 122.07 | 0.0907 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.28 |  | 82.9395 | 0.4105 | 84.415 | 80.64 | 0.0961 | watch_only | none |
| VRT | data_center_power_cooling | 305.75 |  | 306.4591 | -0.2314 | 311.13 | 303.96 | 0.5724 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 415.015 |  | 413.2996 | 0.415 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.59 |  | 652.4548 | -0.2858 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1023.41 |  | 1011.5487 | 1.1726 | 1023.33 | 979.08 | 4.7879 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.05 |  | 476.7241 | 0.2781 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.17 |  | 143.9524 | 0.1511 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.44 |  | 176.6395 | 0.4532 | 177.84 | 173.19 | 1.7471 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 319.56 |  | 318.3427 | 0.3824 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 848.685 |  | 859.1255 | -1.2152 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 409.375 |  | 407.95 | 0.3493 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 114.71 |  | 114.7878 | -0.0677 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 328.44 |  | 327.6036 | 0.2553 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1808.02 |  | 1803.8917 | 0.2289 | 1806.11 | 1780.9 | 0.0548 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 570 |  | 566.3039 | 0.6527 | 566.18 | 548.47 | 4.8789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 322.08 |  | 321.3554 | 0.2255 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.52 |  | 215.6739 | 0.3923 | 217.88 | 212.99 | 0.1986 | watch_only | none |
| TER | semiconductor_test_packaging | 376.375 |  | 371.751 | 1.2438 | 376.78 | 363.37 | 4.0066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 294.12 |  | 295.5533 | -0.485 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.965 |  | 65.3197 | -0.543 | 67.455 | 65.81 | 3.956 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.975 |  | 135.384 | 0.4365 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 344.3 |  | 342.8588 | 0.4203 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.59 |  | 507.6773 | -0.2142 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.52 |  | 296.3077 | -0.2658 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.05 |  | 30.0667 | -0.0557 | 31.13 | 29.12 | 0.0998 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.58 |  | 41.8621 | -0.674 | 43.21 | 40.51 | 0.0722 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.055 |  | 24.0425 | 0.0521 | 24.46 | 23.265 | 0.0831 | watch_only | none |
| SNDK | memory_hbm_storage | 1688 |  | 1631.494 | 3.4635 | 1651.355 | 1560 | 4.0705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 575.13 |  | 563.4488 | 2.0732 | 576.24 | 556.3 | 1.2189 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 935.82 |  | 924.3226 | 1.2439 | 933.5 | 908.955 | 0.5589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.78 |  | 234.334 | 0.1903 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 604.27 |  | 603.8388 | 0.0714 | 614.15 | 605.39 | 0.5312 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 280.73 |  | 278.9861 | 0.6251 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 174.595 |  | 173.5513 | 0.6014 | 177.88 | 168.18 | 1.5923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
