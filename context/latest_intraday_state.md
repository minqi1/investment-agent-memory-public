# Intraday State

- Generated at: `2026-07-24T00:21:30+08:00`
- Market time ET: `2026-07-23T12:21:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 11, 'watch_only': 5, 'below_vwap': 23, 'spread_too_wide_or_missing': 11, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.15 |  | 693.0556 | 0.0136 | 698.65 | 693.24 | 0.0274 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 550.2 |  | 550.8956 | -0.1263 | 557.38 | 545.965 | 0.0727 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.095 |  | 581.1978 | -0.1898 | 585.98 | 576.635 | 0.069 | below_vwap | below_vwap |
| SPY | market_regime | 738.825 |  | 738.8078 | 0.0023 | 742.515 | 738.54 | 0.0311 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 566.52 |  | 566.2691 | 0.0443 | 566.18 | 548.47 | 0.1553 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1664.99 |  | 1629.3954 | 2.1845 | 1651.355 | 1560 | 0.1796 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 31.77 |  | 31.4434 | 1.0387 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 566.52 |  | 566.2691 | 0.0443 | 566.18 | 548.47 | 0.1553 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 738.825 |  | 738.8078 | 0.0023 | 742.515 | 738.54 | 0.0311 | watch_only | none |
| 3 | HPE | ai_server_oem | 48.5 |  | 48.3333 | 0.3449 | 48.88 | 47.635 | 0.0825 | watch_only | none |
| 4 | MU | memory_hbm_storage | 992.28 |  | 988.8651 | 0.3453 | 999.04 | 964.86 | 0.3124 | watch_only | none |
| 5 | NVDA | ai_accelerator | 209.22 |  | 208.2421 | 0.4696 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 320.865 |  | 319.5054 | 0.4255 | 324.42 | 320.24 | 0.1465 | watch_only | none |
| 7 | SMCI | ai_server_oem | 31.77 |  | 31.4434 | 1.0387 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 477.99 |  | 476.707 | 0.2691 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 144.12 |  | 143.9489 | 0.1189 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TSM | foundry | 416.675 |  | 416.5032 | 0.0412 | 420.72 | 412.69 | 2.16 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ANET | ai_networking_optical | 176.67 |  | 176.6261 | 0.0249 | 177.84 | 173.19 | 2.2641 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ETN | data_center_power_cooling | 414.01 |  | 413.2736 | 0.1782 | 415.53 | 406.545 | 0.6715 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ARM | ai_accelerator | 280.095 |  | 278.9445 | 0.4124 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 371.87 |  | 371.6195 | 0.0674 | 376.78 | 363.37 | 4.7705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | DELL | ai_server_oem | 445.05 |  | 443.9568 | 0.2462 | 450.07 | 438.55 | 1.5549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SNDK | memory_hbm_storage | 1664.99 |  | 1629.3954 | 2.1845 | 1651.355 | 1560 | 0.1796 | buy_precheck_manual_confirm | none |
| 17 | GEV | data_center_power_cooling | 1016.485 |  | 1011.3208 | 0.5106 | 1023.33 | 979.08 | 3.0271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | WDC | memory_hbm_storage | 566.95 |  | 563.1613 | 0.6728 | 576.24 | 556.3 | 0.4392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | QQQ | market_regime | 693.15 |  | 693.0556 | 0.0136 | 698.65 | 693.24 | 0.0274 | below_opening_15m_low | below_opening_15m_low |
| 20 | AMZN | cloud_ai_capex | 234.55 |  | 234.3161 | 0.0998 | 238.285 | 235.71 | 0.0512 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 566.52 |  | 566.2691 | 0.0443 | 566.18 | 548.47 | 0.1553 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1664.99 |  | 1629.3954 | 2.1845 | 1651.355 | 1560 | 0.1796 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 31.77 |  | 31.4434 | 1.0387 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 209.22 |  | 208.2421 | 0.4696 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 5 | MU | memory_hbm_storage | 992.28 |  | 988.8651 | 0.3453 | 999.04 | 964.86 | 0.3124 | watch_only | none |
| 6 | SPY | market_regime | 738.825 |  | 738.8078 | 0.0023 | 742.515 | 738.54 | 0.0311 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 320.865 |  | 319.5054 | 0.4255 | 324.42 | 320.24 | 0.1465 | watch_only | none |
| 8 | HPE | ai_server_oem | 48.5 |  | 48.3333 | 0.3449 | 48.88 | 47.635 | 0.0825 | watch_only | none |
| 9 | SMH | semiconductor_index | 580.095 |  | 581.1978 | -0.1898 | 585.98 | 576.635 | 0.069 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 550.2 |  | 550.8956 | -0.1263 | 557.38 | 545.965 | 0.0727 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 391.125 |  | 392.7374 | -0.4106 | 397.34 | 390.54 | 2.2959 | below_vwap | below_vwap,spread_too_wide |
| 12 | ASML | semiconductor_equipment | 1803.12 |  | 1803.8214 | -0.0389 | 1806.11 | 1780.9 | 0.051 | below_vwap | below_vwap |
| 13 | PWR | data_center_power_cooling | 649.04 |  | 652.5357 | -0.5357 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 215.22 |  | 215.6691 | -0.2083 | 217.88 | 212.99 | 2.5137 | below_vwap | below_vwap,spread_too_wide |
| 15 | VRT | data_center_power_cooling | 304.415 |  | 306.4782 | -0.6732 | 311.13 | 303.96 | 0.9986 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.68 |  | 291.6964 | -0.0056 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 320.33 |  | 321.3452 | -0.3159 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 506.82 |  | 507.6964 | -0.1726 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 293.93 |  | 295.6149 | -0.57 | 301.305 | 293.685 | 4.0758 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.15 |  | 693.0556 | 0.0136 | 698.65 | 693.24 | 0.0274 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 66.57 |  | 66.5488 | 0.0318 | 68.245 | 66.7 | 0.03 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 209.22 |  | 208.2421 | 0.4696 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.72 |  | 383.0365 | -0.6048 | 391.71 | 387.245 | 0.7486 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.985 |  | 321.2179 | -0.0725 | 323.25 | 320.82 | 0.0125 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 320.865 |  | 319.5054 | 0.4255 | 324.42 | 320.24 | 0.1465 | watch_only | none |
| AMD | ai_accelerator | 542.21 |  | 546.4428 | -0.7746 | 556.12 | 542.33 | 1.5603 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 416.675 |  | 416.5032 | 0.0412 | 420.72 | 412.69 | 2.16 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.2 |  | 550.8956 | -0.1263 | 557.38 | 545.965 | 0.0727 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.095 |  | 581.1978 | -0.1898 | 585.98 | 576.635 | 0.069 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.125 |  | 392.7374 | -0.4106 | 397.34 | 390.54 | 2.2959 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.28 |  | 988.8651 | 0.3453 | 999.04 | 964.86 | 0.3124 | watch_only | none |
| MRVL | custom_silicon_networking | 208.35 |  | 209.9899 | -0.7809 | 213.785 | 207.665 | 2.2078 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 445.05 |  | 443.9568 | 0.2462 | 450.07 | 438.55 | 1.5549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.5 |  | 48.3333 | 0.3449 | 48.88 | 47.635 | 0.0825 | watch_only | none |
| SMCI | ai_server_oem | 31.77 |  | 31.4434 | 1.0387 | 31.52 | 30.23 | 0.0315 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.825 |  | 738.8078 | 0.0023 | 742.515 | 738.54 | 0.0311 | watch_only | none |
| IWM | market_regime | 291.68 |  | 291.6964 | -0.0056 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.94 |  | 122.2566 | -1.077 | 124.22 | 122.07 | 0.0496 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.775 |  | 82.9385 | -0.1971 | 84.415 | 80.64 | 0.1087 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 304.415 |  | 306.4782 | -0.6732 | 311.13 | 303.96 | 0.9986 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.01 |  | 413.2736 | 0.1782 | 415.53 | 406.545 | 0.6715 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 649.04 |  | 652.5357 | -0.5357 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1016.485 |  | 1011.3208 | 0.5106 | 1023.33 | 979.08 | 3.0271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.99 |  | 476.707 | 0.2691 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.12 |  | 143.9489 | 0.1189 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.67 |  | 176.6261 | 0.0249 | 177.84 | 173.19 | 2.2641 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316.75 |  | 318.3618 | -0.5063 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 844.67 |  | 859.2858 | -1.7009 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 406.95 |  | 407.9425 | -0.2433 | 408.58 | 397.9 | 4.519 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 114.63 |  | 114.7949 | -0.1437 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.535 |  | 327.5869 | -0.3211 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1803.12 |  | 1803.8214 | -0.0389 | 1806.11 | 1780.9 | 0.051 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.52 |  | 566.2691 | 0.0443 | 566.18 | 548.47 | 0.1553 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.33 |  | 321.3452 | -0.3159 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.22 |  | 215.6691 | -0.2083 | 217.88 | 212.99 | 2.5137 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.87 |  | 371.6195 | 0.0674 | 376.78 | 363.37 | 4.7705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.93 |  | 295.6149 | -0.57 | 301.305 | 293.685 | 4.0758 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.85 |  | 65.3222 | -0.7228 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.79 |  | 135.3735 | -0.4311 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.2 |  | 342.8499 | -0.4812 | 347.92 | 341.755 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.82 |  | 507.6964 | -0.1726 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.31 |  | 296.3739 | -0.359 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.97 |  | 30.0673 | -0.3236 | 31.13 | 29.12 | 0.0667 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.53 |  | 41.8689 | -0.8094 | 43.21 | 40.51 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.99 |  | 24.0443 | -0.2258 | 24.46 | 23.265 | 0.1251 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1664.99 |  | 1629.3954 | 2.1845 | 1651.355 | 1560 | 0.1796 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 566.95 |  | 563.1613 | 0.6728 | 576.24 | 556.3 | 0.4392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 928.3 |  | 923.7729 | 0.4901 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234.55 |  | 234.3161 | 0.0998 | 238.285 | 235.71 | 0.0512 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 603.265 |  | 603.8312 | -0.0938 | 614.15 | 605.39 | 0.494 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 280.095 |  | 278.9445 | 0.4124 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 173.23 |  | 173.5449 | -0.1814 | 177.88 | 168.18 | 0.9179 | below_vwap | below_vwap,spread_too_wide |
