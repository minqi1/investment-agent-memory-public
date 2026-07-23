# Intraday State

- Generated at: `2026-07-24T01:05:50+08:00`
- Market time ET: `2026-07-23T13:05:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 14, 'watch_only': 4, 'spread_too_wide_or_missing': 11, 'price_stale_or_missing': 2, 'below_vwap': 24, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.42 |  | 693.1415 | -0.1041 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.55 |  | 550.9986 | -0.4444 | 557.38 | 545.965 | 0.0711 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.755 |  | 581.187 | -0.2464 | 585.98 | 576.635 | 0.0483 | below_vwap | below_vwap |
| SPY | market_regime | 738.23 |  | 738.8097 | -0.0785 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.1 |  | 31.614 | 1.5374 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 991.85 |  | 991.0132 | 0.0844 | 999.04 | 964.86 | 0.1583 | watch_only | none |
| 2 | NVDA | ai_accelerator | 209.68 |  | 208.4592 | 0.5856 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 3 | META | cloud_ai_capex | 606.19 |  | 603.8136 | 0.3936 | 614.15 | 605.39 | 0.1996 | watch_only | none |
| 4 | TT | data_center_power_cooling | 478.41 |  | 476.7657 | 0.3449 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | JCI | data_center_power_cooling | 144.08 |  | 143.9603 | 0.0832 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MKSI | semiconductor_materials | 343.69 |  | 342.8882 | 0.2339 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | CORZ | high_beta_ai_infrastructure | 24.13 |  | 24.0515 | 0.3265 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| 8 | TSM | foundry | 417.29 |  | 416.6765 | 0.1472 | 420.72 | 412.69 | 0.9322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 176.98 |  | 176.7167 | 0.149 | 177.84 | 173.19 | 2.2601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ETN | data_center_power_cooling | 413.99 |  | 413.3715 | 0.1496 | 415.53 | 406.545 | 0.5725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ARM | ai_accelerator | 281 |  | 279.4027 | 0.5717 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TER | semiconductor_test_packaging | 373.6 |  | 372.0665 | 0.4121 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SMCI | ai_server_oem | 32.1 |  | 31.614 | 1.5374 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |
| 14 | WDC | memory_hbm_storage | 566.8 |  | 564.1797 | 0.4645 | 576.24 | 556.3 | 1.9054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | GOOGL | cloud_ai_capex | 319.74 |  | 319.5201 | 0.0688 | 324.42 | 320.24 | 0.0344 | below_opening_15m_low | below_opening_15m_low |
| 16 | AMZN | cloud_ai_capex | 234.535 |  | 234.3435 | 0.0817 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 17 | SMH | semiconductor_index | 579.755 |  | 581.187 | -0.2464 | 585.98 | 576.635 | 0.0483 | below_vwap | below_vwap |
| 18 | SOXX | semiconductor_index | 548.55 |  | 550.9986 | -0.4444 | 557.38 | 545.965 | 0.0711 | below_vwap | below_vwap |
| 19 | GEV | data_center_power_cooling | 1026.13 |  | 1012.1815 | 1.3781 | 1023.33 | 979.08 | 3.4479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 390.655 |  | 392.632 | -0.5035 | 397.34 | 390.54 | 0.041 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.1 |  | 31.614 | 1.5374 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1026.13 |  | 1012.1815 | 1.3781 | 1023.33 | 979.08 | 3.4479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | SNDK | memory_hbm_storage | 1668.73 |  | 1638.0426 | 1.8734 | 1651.355 | 1560 | 4.9139 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | NVDA | ai_accelerator | 209.68 |  | 208.4592 | 0.5856 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 5 | MU | memory_hbm_storage | 991.85 |  | 991.0132 | 0.0844 | 999.04 | 964.86 | 0.1583 | watch_only | none |
| 6 | META | cloud_ai_capex | 606.19 |  | 603.8136 | 0.3936 | 614.15 | 605.39 | 0.1996 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 24.13 |  | 24.0515 | 0.3265 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| 8 | SMH | semiconductor_index | 579.755 |  | 581.187 | -0.2464 | 585.98 | 576.635 | 0.0483 | below_vwap | below_vwap |
| 9 | SOXX | semiconductor_index | 548.55 |  | 550.9986 | -0.4444 | 557.38 | 545.965 | 0.0711 | below_vwap | below_vwap |
| 10 | AVGO | custom_silicon_networking | 390.655 |  | 392.632 | -0.5035 | 397.34 | 390.54 | 0.041 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1802.73 |  | 1804.0521 | -0.0733 | 1806.11 | 1780.9 | 0.0621 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 562.15 |  | 566.3352 | -0.739 | 566.18 | 548.47 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 650 |  | 652.1653 | -0.332 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 215.54 |  | 215.7361 | -0.0909 | 217.88 | 212.99 | 2.4729 | below_vwap | below_vwap,spread_too_wide |
| 15 | VRT | data_center_power_cooling | 304.19 |  | 306.3626 | -0.7092 | 311.13 | 303.96 | 0.8843 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.52 |  | 291.6887 | -0.0578 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 320.32 |  | 321.3564 | -0.3225 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 506.31 |  | 507.6229 | -0.2586 | 510.71 | 502.72 | 4.6948 | below_vwap | below_vwap,spread_too_wide |
| 20 | HPE | ai_server_oem | 48.3 |  | 48.3573 | -0.1184 | 48.88 | 47.635 | 0.0621 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.42 |  | 693.1415 | -0.1041 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.35 |  | 66.579 | -0.344 | 68.245 | 66.7 | 0.0301 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.68 |  | 208.4592 | 0.5856 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.785 |  | 382.8139 | -0.2688 | 391.71 | 387.245 | 0.0236 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.66 |  | 321.1378 | -0.1488 | 323.25 | 320.82 | 0.0374 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.74 |  | 319.5201 | 0.0688 | 324.42 | 320.24 | 0.0344 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 527.77 |  | 542.6138 | -2.7356 | 556.12 | 542.33 | 1.3207 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.29 |  | 416.6765 | 0.1472 | 420.72 | 412.69 | 0.9322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.55 |  | 550.9986 | -0.4444 | 557.38 | 545.965 | 0.0711 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.755 |  | 581.187 | -0.2464 | 585.98 | 576.635 | 0.0483 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.655 |  | 392.632 | -0.5035 | 397.34 | 390.54 | 0.041 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 991.85 |  | 991.0132 | 0.0844 | 999.04 | 964.86 | 0.1583 | watch_only | none |
| MRVL | custom_silicon_networking | 208.29 |  | 209.9355 | -0.7838 | 213.785 | 207.665 | 0.0912 | below_vwap | below_vwap |
| DELL | ai_server_oem | 443.13 |  | 444.0849 | -0.215 | 450.07 | 438.55 | 2.2522 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.3 |  | 48.3573 | -0.1184 | 48.88 | 47.635 | 0.0621 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.1 |  | 31.614 | 1.5374 | 31.52 | 30.23 | 0.0312 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.23 |  | 738.8097 | -0.0785 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.52 |  | 291.6887 | -0.0578 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 121.295 |  | 122.1256 | -0.6801 | 124.22 | 122.07 | 0.0742 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.43 |  | 82.9035 | -0.5712 | 84.415 | 80.64 | 0.0485 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 304.19 |  | 306.3626 | -0.7092 | 311.13 | 303.96 | 0.8843 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.99 |  | 413.3715 | 0.1496 | 415.53 | 406.545 | 0.5725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 650 |  | 652.1653 | -0.332 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1026.13 |  | 1012.1815 | 1.3781 | 1023.33 | 979.08 | 3.4479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.41 |  | 476.7657 | 0.3449 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.08 |  | 143.9603 | 0.0832 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.98 |  | 176.7167 | 0.149 | 177.84 | 173.19 | 2.2601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316.235 |  | 318.2829 | -0.6434 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.4 |  | 858.4482 | -1.287 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.81 |  | 408.1944 | -0.0942 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 113.51 |  | 114.7269 | -1.0607 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.26 |  | 327.796 | -0.1635 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1802.73 |  | 1804.0521 | -0.0733 | 1806.11 | 1780.9 | 0.0621 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 562.15 |  | 566.3352 | -0.739 | 566.18 | 548.47 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 320.32 |  | 321.3564 | -0.3225 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.54 |  | 215.7361 | -0.0909 | 217.88 | 212.99 | 2.4729 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 373.6 |  | 372.0665 | 0.4121 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 292.74 |  | 295.271 | -0.8572 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.14 |  | 65.3115 | -0.2625 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.65 |  | 54.6081 | 0.0768 | 55.76 | 53.78 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.3 |  | 135.4011 | -0.0747 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.69 |  | 342.8882 | 0.2339 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.31 |  | 507.6229 | -0.2586 | 510.71 | 502.72 | 4.6948 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.18 |  | 296.1852 | -0.3394 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.92 |  | 30.0526 | -0.4411 | 31.13 | 29.12 | 0.1003 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.73 |  | 41.7844 | -2.5234 | 43.21 | 40.51 | 0.0737 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.13 |  | 24.0515 | 0.3265 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| SNDK | memory_hbm_storage | 1668.73 |  | 1638.0426 | 1.8734 | 1651.355 | 1560 | 4.9139 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 566.8 |  | 564.1797 | 0.4645 | 576.24 | 556.3 | 1.9054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 921.23 |  | 924.6754 | -0.3726 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.535 |  | 234.3435 | 0.0817 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.19 |  | 603.8136 | 0.3936 | 614.15 | 605.39 | 0.1996 | watch_only | none |
| ARM | ai_accelerator | 281 |  | 279.4027 | 0.5717 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 172.91 |  | 173.6063 | -0.4011 | 177.88 | 168.18 | 0.561 | below_vwap | below_vwap,spread_too_wide |
