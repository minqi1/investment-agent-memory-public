# Intraday State

- Generated at: `2026-07-24T02:35:29+08:00`
- Market time ET: `2026-07-23T14:35:30-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 17, 'watch_only': 5, 'below_vwap': 27, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 4, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.54 |  | 692.9661 | -0.2058 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.31 |  | 550.8413 | -0.4595 | 557.38 | 545.965 | 0.0766 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.365 |  | 580.8755 | -0.4322 | 585.98 | 576.635 | 0.0588 | below_vwap | below_vwap |
| SPY | market_regime | 737.58 |  | 738.6218 | -0.141 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1037.44 |  | 1014.8554 | 2.2254 | 1023.33 | 979.08 | 0.1812 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 208.79 |  | 208.5868 | 0.0974 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.83 |  | 476.8111 | 0.2137 | 480 | 472.33 | 0.3076 | watch_only | none |
| 3 | WDC | memory_hbm_storage | 564.51 |  | 564.262 | 0.044 | 576.24 | 556.3 | 0.1984 | watch_only | none |
| 4 | APLD | high_beta_ai_infrastructure | 30.06 |  | 30.0555 | 0.0149 | 31.13 | 29.12 | 0.0998 | watch_only | none |
| 5 | ARM | ai_accelerator | 280.24 |  | 279.661 | 0.207 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | CORZ | high_beta_ai_infrastructure | 24.11 |  | 24.0704 | 0.1645 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 7 | MU | memory_hbm_storage | 994.9 |  | 991.7082 | 0.3218 | 999.04 | 964.86 | 0.5528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | STX | memory_hbm_storage | 924.83 |  | 924.1437 | 0.0743 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | GEV | data_center_power_cooling | 1037.44 |  | 1014.8554 | 2.2254 | 1023.33 | 979.08 | 0.1812 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 578.365 |  | 580.8755 | -0.4322 | 585.98 | 576.635 | 0.0588 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 548.31 |  | 550.8413 | -0.4595 | 557.38 | 545.965 | 0.0766 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1796.15 |  | 1802.8191 | -0.3699 | 1806.11 | 1780.9 | 0.0501 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 291.28 |  | 291.6412 | -0.1239 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 14 | HPE | ai_server_oem | 47.67 |  | 48.3028 | -1.3101 | 48.88 | 47.635 | 0.0629 | below_vwap | below_vwap |
| 15 | SMCI | ai_server_oem | 31.18 |  | 31.6189 | -1.3881 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IREN | high_beta_ai_infrastructure | 40.87 |  | 41.6501 | -1.8731 | 43.21 | 40.51 | 0.0489 | below_vwap | below_vwap |
| 18 | META | cloud_ai_capex | 605.34 |  | 604.4614 | 0.1453 | 614.15 | 605.39 | 0.4576 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | CIEN | ai_networking_optical | 407.25 |  | 408.2176 | -0.237 | 408.58 | 397.9 | 0.3315 | below_vwap | below_vwap |
| 20 | JCI | data_center_power_cooling | 143.595 |  | 143.912 | -0.2203 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1037.44 |  | 1014.8554 | 2.2254 | 1023.33 | 979.08 | 0.1812 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1666.335 |  | 1643.2083 | 1.4074 | 1651.355 | 1560 | 4.4409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | NVDA | ai_accelerator | 208.79 |  | 208.5868 | 0.0974 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 4 | TT | data_center_power_cooling | 477.83 |  | 476.8111 | 0.2137 | 480 | 472.33 | 0.3076 | watch_only | none |
| 5 | WDC | memory_hbm_storage | 564.51 |  | 564.262 | 0.044 | 576.24 | 556.3 | 0.1984 | watch_only | none |
| 6 | CORZ | high_beta_ai_infrastructure | 24.11 |  | 24.0704 | 0.1645 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 7 | APLD | high_beta_ai_infrastructure | 30.06 |  | 30.0555 | 0.0149 | 31.13 | 29.12 | 0.0998 | watch_only | none |
| 8 | TSM | foundry | 415.91 |  | 416.5305 | -0.149 | 420.72 | 412.69 | 0.9617 | below_vwap | below_vwap,spread_too_wide |
| 9 | SMH | semiconductor_index | 578.365 |  | 580.8755 | -0.4322 | 585.98 | 576.635 | 0.0588 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 548.31 |  | 550.8413 | -0.4595 | 557.38 | 545.965 | 0.0766 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 390.83 |  | 392.2043 | -0.3504 | 397.34 | 390.54 | 1.7629 | below_vwap | below_vwap,spread_too_wide |
| 12 | ASML | semiconductor_equipment | 1796.15 |  | 1802.8191 | -0.3699 | 1806.11 | 1780.9 | 0.0501 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 560.285 |  | 565.0728 | -0.8473 | 566.18 | 548.47 | 3.848 | below_vwap | below_vwap,spread_too_wide |
| 14 | ANET | ai_networking_optical | 176.14 |  | 176.6949 | -0.3141 | 177.84 | 173.19 | 3.1225 | below_vwap | below_vwap,spread_too_wide |
| 15 | JCI | data_center_power_cooling | 143.595 |  | 143.912 | -0.2203 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 649.825 |  | 651.7578 | -0.2966 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | KLAC | semiconductor_equipment | 215.375 |  | 215.5315 | -0.0726 | 217.88 | 212.99 | 2.4794 | below_vwap | below_vwap,spread_too_wide |
| 18 | ETN | data_center_power_cooling | 413.26 |  | 413.3342 | -0.018 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | IWM | market_regime | 291.28 |  | 291.6412 | -0.1239 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 20 | LRCX | semiconductor_equipment | 318.86 |  | 320.5566 | -0.5293 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.54 |  | 692.9661 | -0.2058 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.19 |  | 66.5395 | -0.5253 | 68.245 | 66.7 | 0.0302 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.79 |  | 208.5868 | 0.0974 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| MSFT | cloud_ai_capex | 381.41 |  | 382.5649 | -0.3019 | 391.71 | 387.245 | 0.3697 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.14 |  | 321.0132 | -0.272 | 323.25 | 320.82 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.41 |  | 319.561 | -0.0472 | 324.42 | 320.24 | 0.2066 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 537.47 |  | 540.3249 | -0.5284 | 556.12 | 542.33 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 415.91 |  | 416.5305 | -0.149 | 420.72 | 412.69 | 0.9617 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.31 |  | 550.8413 | -0.4595 | 557.38 | 545.965 | 0.0766 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.365 |  | 580.8755 | -0.4322 | 585.98 | 576.635 | 0.0588 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.83 |  | 392.2043 | -0.3504 | 397.34 | 390.54 | 1.7629 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 994.9 |  | 991.7082 | 0.3218 | 999.04 | 964.86 | 0.5528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.02 |  | 209.4359 | -1.1535 | 213.785 | 207.665 | 0.1691 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.38 |  | 443.5916 | -1.4003 | 450.07 | 438.55 | 1.7445 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.67 |  | 48.3028 | -1.3101 | 48.88 | 47.635 | 0.0629 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.18 |  | 31.6189 | -1.3881 | 31.52 | 30.23 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 737.58 |  | 738.6218 | -0.141 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.28 |  | 291.6412 | -0.1239 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.775 |  | 121.75 | -1.6222 | 124.22 | 122.07 | 0.2338 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.7 |  | 82.7472 | -1.2655 | 84.415 | 80.64 | 3.88 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.63 |  | 306.1012 | -1.134 | 311.13 | 303.96 | 1.3052 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.26 |  | 413.3342 | -0.018 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 649.825 |  | 651.7578 | -0.2966 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1037.44 |  | 1014.8554 | 2.2254 | 1023.33 | 979.08 | 0.1812 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 477.83 |  | 476.8111 | 0.2137 | 480 | 472.33 | 0.3076 | watch_only | none |
| JCI | data_center_power_cooling | 143.595 |  | 143.912 | -0.2203 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.14 |  | 176.6949 | -0.3141 | 177.84 | 173.19 | 3.1225 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.445 |  | 317.7431 | -1.3527 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 836.01 |  | 856.7088 | -2.4161 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.25 |  | 408.2176 | -0.237 | 408.58 | 397.9 | 0.3315 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 112.44 |  | 114.5306 | -1.8254 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 322.74 |  | 327.5653 | -1.4731 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.15 |  | 1802.8191 | -0.3699 | 1806.11 | 1780.9 | 0.0501 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 560.285 |  | 565.0728 | -0.8473 | 566.18 | 548.47 | 3.848 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.86 |  | 320.5566 | -0.5293 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.375 |  | 215.5315 | -0.0726 | 217.88 | 212.99 | 2.4794 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.6 |  | 372.1251 | -0.1411 | 376.78 | 363.37 | 5.0161 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 290.19 |  | 294.0267 | -1.3049 | 301.305 | 293.685 | 4.6487 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.89 |  | 65.2161 | -0.5001 | 67.455 | 65.81 | 4.2225 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.245 |  | 54.5033 | -0.4739 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.45 |  | 135.0871 | -0.4716 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.89 |  | 342.8233 | -0.2722 | 347.92 | 341.755 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 505.35 |  | 507.2899 | -0.3824 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.115 |  | 295.7052 | -0.1996 | 299.26 | 295.795 | 0.0678 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.06 |  | 30.0555 | 0.0149 | 31.13 | 29.12 | 0.0998 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 40.87 |  | 41.6501 | -1.8731 | 43.21 | 40.51 | 0.0489 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.11 |  | 24.0704 | 0.1645 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| SNDK | memory_hbm_storage | 1666.335 |  | 1643.2083 | 1.4074 | 1651.355 | 1560 | 4.4409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 564.51 |  | 564.262 | 0.044 | 576.24 | 556.3 | 0.1984 | watch_only | none |
| STX | memory_hbm_storage | 924.83 |  | 924.1437 | 0.0743 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 233.89 |  | 234.3374 | -0.1909 | 238.285 | 235.71 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.34 |  | 604.4614 | 0.1453 | 614.15 | 605.39 | 0.4576 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 280.24 |  | 279.661 | 0.207 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 172.67 |  | 173.5274 | -0.4941 | 177.88 | 168.18 | 0.9672 | below_vwap | below_vwap,spread_too_wide |
