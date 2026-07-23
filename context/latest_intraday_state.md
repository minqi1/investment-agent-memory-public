# Intraday State

- Generated at: `2026-07-24T01:35:32+08:00`
- Market time ET: `2026-07-23T13:35:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 16, 'watch_only': 3, 'spread_too_wide_or_missing': 16, 'price_stale_or_missing': 2, 'below_vwap': 18, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.28 |  | 693.1134 | -0.1202 | 698.65 | 693.24 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.97 |  | 550.9771 | -0.3643 | 557.38 | 545.965 | 0.0455 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.45 |  | 581.1502 | -0.2926 | 585.98 | 576.635 | 0.0639 | below_vwap | below_vwap |
| SPY | market_regime | 738.1 |  | 738.7914 | -0.0936 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.42 |  | 31.6807 | 2.3336 | 31.52 | 30.23 | 0.0617 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | HPE | ai_server_oem | 48.44 |  | 48.3551 | 0.1755 | 48.88 | 47.635 | 0.0826 | watch_only | none |
| 2 | NVDA | ai_accelerator | 209.67 |  | 208.5539 | 0.5352 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 3 | TT | data_center_power_cooling | 476.92 |  | 476.813 | 0.0224 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ETN | data_center_power_cooling | 413.605 |  | 413.4025 | 0.049 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TER | semiconductor_test_packaging | 373.3 |  | 372.2862 | 0.2723 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TSM | foundry | 417.56 |  | 416.7091 | 0.2042 | 420.72 | 412.69 | 1.4178 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | WDC | memory_hbm_storage | 565.98 |  | 564.2735 | 0.3024 | 576.24 | 556.3 | 0.5495 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | CIEN | ai_networking_optical | 411 |  | 408.2505 | 0.6735 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | META | cloud_ai_capex | 605.77 |  | 604.0456 | 0.2855 | 614.15 | 605.39 | 1.489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SKHY | memory_hbm_storage | 173.705 |  | 173.6196 | 0.0492 | 177.88 | 168.18 | 0.7484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | MU | memory_hbm_storage | 997.54 |  | 991.5159 | 0.6076 | 999.04 | 964.86 | 1.0025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ANET | ai_networking_optical | 177.47 |  | 176.7306 | 0.4184 | 177.84 | 173.19 | 2.2539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SMCI | ai_server_oem | 32.42 |  | 31.6807 | 2.3336 | 31.52 | 30.23 | 0.0617 | buy_precheck_manual_confirm | none |
| 15 | ARM | ai_accelerator | 281.53 |  | 279.6091 | 0.687 | 283 | 276.24 | 4.7952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | GOOGL | cloud_ai_capex | 320.015 |  | 319.553 | 0.1446 | 324.42 | 320.24 | 0.0812 | below_opening_15m_low | below_opening_15m_low |
| 17 | STX | memory_hbm_storage | 926.52 |  | 924.6868 | 0.1982 | 933.5 | 908.955 | 5.063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CORZ | high_beta_ai_infrastructure | 24.26 |  | 24.0627 | 0.8199 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| 19 | SMH | semiconductor_index | 579.45 |  | 581.1502 | -0.2926 | 585.98 | 576.635 | 0.0639 | below_vwap | below_vwap |
| 20 | SOXX | semiconductor_index | 548.97 |  | 550.9771 | -0.3643 | 557.38 | 545.965 | 0.0455 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.42 |  | 31.6807 | 2.3336 | 31.52 | 30.23 | 0.0617 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1028.81 |  | 1013.0503 | 1.5557 | 1023.33 | 979.08 | 2.083 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | CIEN | ai_networking_optical | 411 |  | 408.2505 | 0.6735 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | SNDK | memory_hbm_storage | 1671.62 |  | 1640.5839 | 1.8918 | 1651.355 | 1560 | 3.2902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.67 |  | 208.5539 | 0.5352 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | HPE | ai_server_oem | 48.44 |  | 48.3551 | 0.1755 | 48.88 | 47.635 | 0.0826 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 24.26 |  | 24.0627 | 0.8199 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| 8 | SMH | semiconductor_index | 579.45 |  | 581.1502 | -0.2926 | 585.98 | 576.635 | 0.0639 | below_vwap | below_vwap |
| 9 | SOXX | semiconductor_index | 548.97 |  | 550.9771 | -0.3643 | 557.38 | 545.965 | 0.0455 | below_vwap | below_vwap |
| 10 | AVGO | custom_silicon_networking | 391.685 |  | 392.5638 | -0.2239 | 397.34 | 390.54 | 2.8645 | below_vwap | below_vwap,spread_too_wide |
| 11 | ASML | semiconductor_equipment | 1800.41 |  | 1804.0453 | -0.2015 | 1806.11 | 1780.9 | 0.14 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 561.05 |  | 566.0828 | -0.8891 | 566.18 | 548.47 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 143.84 |  | 143.9657 | -0.0873 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 649.54 |  | 652.068 | -0.3877 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 214.8 |  | 215.7271 | -0.4298 | 217.88 | 212.99 | 2.1881 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.29 |  | 291.6814 | -0.1342 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 319.54 |  | 321.2747 | -0.54 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 505.955 |  | 507.5465 | -0.3136 | 510.71 | 502.72 | 0.0257 | below_vwap | below_vwap |
| 20 | COHR | ai_networking_optical | 315.66 |  | 318.1806 | -0.7922 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.28 |  | 693.1134 | -0.1202 | 698.65 | 693.24 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.37 |  | 66.573 | -0.3049 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.67 |  | 208.5539 | 0.5352 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.44 |  | 382.705 | -0.3305 | 391.71 | 387.245 | 0.3828 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.76 |  | 321.1127 | -0.1098 | 323.25 | 320.82 | 0.0842 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.015 |  | 319.553 | 0.1446 | 324.42 | 320.24 | 0.0812 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 533.815 |  | 541.09 | -1.3445 | 556.12 | 542.33 | 1.7834 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.56 |  | 416.7091 | 0.2042 | 420.72 | 412.69 | 1.4178 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.97 |  | 550.9771 | -0.3643 | 557.38 | 545.965 | 0.0455 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.45 |  | 581.1502 | -0.2926 | 585.98 | 576.635 | 0.0639 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.685 |  | 392.5638 | -0.2239 | 397.34 | 390.54 | 2.8645 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 997.54 |  | 991.5159 | 0.6076 | 999.04 | 964.86 | 1.0025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 207.29 |  | 209.7932 | -1.1932 | 213.785 | 207.665 | 0.164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 443.58 |  | 444.0473 | -0.1052 | 450.07 | 438.55 | 0.4103 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.44 |  | 48.3551 | 0.1755 | 48.88 | 47.635 | 0.0826 | watch_only | none |
| SMCI | ai_server_oem | 32.42 |  | 31.6807 | 2.3336 | 31.52 | 30.23 | 0.0617 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.1 |  | 738.7914 | -0.0936 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.29 |  | 291.6814 | -0.1342 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.34 |  | 122.0327 | -1.3871 | 124.22 | 122.07 | 0.2825 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.6 |  | 82.8546 | -0.3073 | 84.415 | 80.64 | 0.8475 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.69 |  | 306.3094 | -0.8551 | 311.13 | 303.96 | 0.1383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 413.605 |  | 413.4025 | 0.049 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 649.54 |  | 652.068 | -0.3877 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.81 |  | 1013.0503 | 1.5557 | 1023.33 | 979.08 | 2.083 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.92 |  | 476.813 | 0.0224 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.84 |  | 143.9657 | -0.0873 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.47 |  | 176.7306 | 0.4184 | 177.84 | 173.19 | 2.2539 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.66 |  | 318.1806 | -0.7922 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 845.19 |  | 858.1824 | -1.5139 | 880.26 | 833 | 4.1411 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 411 |  | 408.2505 | 0.6735 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 113.96 |  | 114.6688 | -0.6181 | 118.01 | 108.505 | 4.7034 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 327.12 |  | 327.7813 | -0.2017 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1800.41 |  | 1804.0453 | -0.2015 | 1806.11 | 1780.9 | 0.14 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 561.05 |  | 566.0828 | -0.8891 | 566.18 | 548.47 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 319.54 |  | 321.2747 | -0.54 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.8 |  | 215.7271 | -0.4298 | 217.88 | 212.99 | 2.1881 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 373.3 |  | 372.2862 | 0.2723 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.31 |  | 294.7853 | -1.5181 | 301.305 | 293.685 | 0.4099 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.985 |  | 65.3045 | -0.4892 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.73 |  | 135.3484 | -0.4569 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 505.955 |  | 507.5465 | -0.3136 | 510.71 | 502.72 | 0.0257 | below_vwap | below_vwap |
| APD | industrial_gases | 294.59 |  | 295.9936 | -0.4742 | 299.26 | 295.795 | 0.1018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.27 |  | 30.0575 | 0.7071 | 31.13 | 29.12 | 2.3456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 41.2 |  | 41.7277 | -1.2647 | 43.21 | 40.51 | 0.0485 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.26 |  | 24.0627 | 0.8199 | 24.46 | 23.265 | 0.0412 | watch_only | none |
| SNDK | memory_hbm_storage | 1671.62 |  | 1640.5839 | 1.8918 | 1651.355 | 1560 | 3.2902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 565.98 |  | 564.2735 | 0.3024 | 576.24 | 556.3 | 0.5495 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 926.52 |  | 924.6868 | 0.1982 | 933.5 | 908.955 | 5.063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.305 |  | 234.3561 | -0.0218 | 238.285 | 235.71 | 0.0683 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.77 |  | 604.0456 | 0.2855 | 614.15 | 605.39 | 1.489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.53 |  | 279.6091 | 0.687 | 283 | 276.24 | 4.7952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.705 |  | 173.6196 | 0.0492 | 177.88 | 168.18 | 0.7484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
