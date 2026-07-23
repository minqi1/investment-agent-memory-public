# Intraday State

- Generated at: `2026-07-24T00:47:34+08:00`
- Market time ET: `2026-07-23T12:47:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 14, 'watch_only': 5, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 1, 'below_vwap': 17, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.87 |  | 693.159 | -0.0417 | 698.65 | 693.24 | 0.013 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 551.03 |  | 551.0396 | -0.0017 | 557.38 | 545.965 | 0.0617 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.85 |  | 581.2272 | -0.0649 | 585.98 | 576.635 | 0.0844 | below_vwap | below_vwap |
| SPY | market_regime | 738.4 |  | 738.8415 | -0.0598 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.19 |  | 31.5693 | 1.9661 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1805.65 |  | 1804.0046 | 0.0912 | 1806.11 | 1780.9 | 0.1163 | watch_only | none |
| 2 | HPE | ai_server_oem | 48.45 |  | 48.3577 | 0.1909 | 48.88 | 47.635 | 0.1238 | watch_only | none |
| 3 | NVDA | ai_accelerator | 209.55 |  | 208.3877 | 0.5578 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 4 | TT | data_center_power_cooling | 477.41 |  | 476.7565 | 0.1371 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | JCI | data_center_power_cooling | 144.085 |  | 143.9579 | 0.0883 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ETN | data_center_power_cooling | 413.96 |  | 413.3525 | 0.147 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | COHU | semiconductor_test_packaging | 54.72 |  | 54.6067 | 0.2075 | 55.76 | 53.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | MU | memory_hbm_storage | 998.56 |  | 990.6283 | 0.8007 | 999.04 | 964.86 | 0.1482 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.09 |  | 24.0453 | 0.1859 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 10 | AMAT | semiconductor_equipment | 567.75 |  | 566.4135 | 0.2359 | 566.18 | 548.47 | 1.8512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 417.62 |  | 416.6487 | 0.2331 | 420.72 | 412.69 | 0.9315 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | CIEN | ai_networking_optical | 409.25 |  | 408.189 | 0.2599 | 408.58 | 397.9 | 4.1368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ANET | ai_networking_optical | 176.96 |  | 176.7069 | 0.1433 | 177.84 | 173.19 | 1.8196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | KLAC | semiconductor_equipment | 216.44 |  | 215.7093 | 0.3388 | 217.88 | 212.99 | 3.0632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | ALAB | ai_networking_optical | 329.12 |  | 327.8072 | 0.4005 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | DELL | ai_server_oem | 444.33 |  | 444.096 | 0.0527 | 450.07 | 438.55 | 1.895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SMCI | ai_server_oem | 32.19 |  | 31.5693 | 1.9661 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |
| 18 | ARM | ai_accelerator | 281.09 |  | 279.302 | 0.6402 | 283 | 276.24 | 4.2228 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 374.77 |  | 371.97 | 0.7527 | 376.78 | 363.37 | 4.0612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 930.4 |  | 924.6777 | 0.6188 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.19 |  | 31.5693 | 1.9661 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 567.75 |  | 566.4135 | 0.2359 | 566.18 | 548.47 | 1.8512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | CIEN | ai_networking_optical | 409.25 |  | 408.189 | 0.2599 | 408.58 | 397.9 | 4.1368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1678.8 |  | 1636.4356 | 2.5888 | 1651.355 | 1560 | 1.1669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.55 |  | 208.3877 | 0.5578 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | MU | memory_hbm_storage | 998.56 |  | 990.6283 | 0.8007 | 999.04 | 964.86 | 0.1482 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1805.65 |  | 1804.0046 | 0.0912 | 1806.11 | 1780.9 | 0.1163 | watch_only | none |
| 8 | HPE | ai_server_oem | 48.45 |  | 48.3577 | 0.1909 | 48.88 | 47.635 | 0.1238 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.09 |  | 24.0453 | 0.1859 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| 10 | SMH | semiconductor_index | 580.85 |  | 581.2272 | -0.0649 | 585.98 | 576.635 | 0.0844 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 551.03 |  | 551.0396 | -0.0017 | 557.38 | 545.965 | 0.0617 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 391.175 |  | 392.6767 | -0.3824 | 397.34 | 390.54 | 1.7562 | below_vwap | below_vwap,spread_too_wide |
| 13 | PWR | data_center_power_cooling | 649.515 |  | 652.3387 | -0.4329 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | VRT | data_center_power_cooling | 304.065 |  | 306.3935 | -0.76 | 311.13 | 303.96 | 1.1346 | below_vwap | below_vwap,spread_too_wide |
| 15 | IWM | market_regime | 291.5 |  | 291.6994 | -0.0684 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 320.98 |  | 321.3728 | -0.1222 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 506.84 |  | 507.651 | -0.1598 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | COHR | ai_networking_optical | 316.2 |  | 318.3438 | -0.6734 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | MRVL | custom_silicon_networking | 209.315 |  | 209.9775 | -0.3155 | 213.785 | 207.665 | 0.8408 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.87 |  | 693.159 | -0.0417 | 698.65 | 693.24 | 0.013 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.57 |  | 66.5848 | -0.0223 | 68.245 | 66.7 | 0.03 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.55 |  | 208.3877 | 0.5578 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.275 |  | 382.9002 | -0.6856 | 391.71 | 387.245 | 0.6127 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.57 |  | 321.1607 | -0.1839 | 323.25 | 320.82 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.09 |  | 319.542 | -0.1414 | 324.42 | 320.24 | 0.1536 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 537.95 |  | 546.1299 | -1.4978 | 556.12 | 542.33 | 4.6473 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.62 |  | 416.6487 | 0.2331 | 420.72 | 412.69 | 0.9315 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.03 |  | 551.0396 | -0.0017 | 557.38 | 545.965 | 0.0617 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.85 |  | 581.2272 | -0.0649 | 585.98 | 576.635 | 0.0844 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.175 |  | 392.6767 | -0.3824 | 397.34 | 390.54 | 1.7562 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 998.56 |  | 990.6283 | 0.8007 | 999.04 | 964.86 | 0.1482 | watch_only | none |
| MRVL | custom_silicon_networking | 209.315 |  | 209.9775 | -0.3155 | 213.785 | 207.665 | 0.8408 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 444.33 |  | 444.096 | 0.0527 | 450.07 | 438.55 | 1.895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.45 |  | 48.3577 | 0.1909 | 48.88 | 47.635 | 0.1238 | watch_only | none |
| SMCI | ai_server_oem | 32.19 |  | 31.5693 | 1.9661 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.4 |  | 738.8415 | -0.0598 | 742.515 | 738.54 | 0.0041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.5 |  | 291.6994 | -0.0684 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.54 |  | 122.1801 | -1.3424 | 124.22 | 122.07 | 0.0332 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.25 |  | 82.9263 | -0.8156 | 84.415 | 80.64 | 0.1459 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 304.065 |  | 306.3935 | -0.76 | 311.13 | 303.96 | 1.1346 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.96 |  | 413.3525 | 0.147 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 649.515 |  | 652.3387 | -0.4329 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1021.55 |  | 1011.8084 | 0.9628 | 1023.33 | 979.08 | 2.8956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.41 |  | 476.7565 | 0.1371 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.085 |  | 143.9579 | 0.0883 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.96 |  | 176.7069 | 0.1433 | 177.84 | 173.19 | 1.8196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316.2 |  | 318.3438 | -0.6734 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.73 |  | 858.742 | -1.2823 | 880.26 | 833 | 4.0945 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 409.25 |  | 408.189 | 0.2599 | 408.58 | 397.9 | 4.1368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 114.27 |  | 114.7736 | -0.4387 | 118.01 | 108.505 | 0.3063 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 329.12 |  | 327.8072 | 0.4005 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1805.65 |  | 1804.0046 | 0.0912 | 1806.11 | 1780.9 | 0.1163 | watch_only | none |
| AMAT | semiconductor_equipment | 567.75 |  | 566.4135 | 0.2359 | 566.18 | 548.47 | 1.8512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.98 |  | 321.3728 | -0.1222 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.44 |  | 215.7093 | 0.3388 | 217.88 | 212.99 | 3.0632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 374.77 |  | 371.97 | 0.7527 | 376.78 | 363.37 | 4.0612 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.095 |  | 295.4132 | -0.7847 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.57 |  | 65.3218 | 0.38 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.72 |  | 54.6067 | 0.2075 | 55.76 | 53.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.39 |  | 135.4055 | -0.0115 | 137.81 | 135.66 | 4.8083 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 345.93 |  | 342.8795 | 0.8897 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.84 |  | 507.651 | -0.1598 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.455 |  | 296.2834 | -0.2796 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.72 |  | 30.0608 | -1.1337 | 31.13 | 29.12 | 0.1682 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.75 |  | 41.825 | -2.5703 | 43.21 | 40.51 | 0.0736 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.09 |  | 24.0453 | 0.1859 | 24.46 | 23.265 | 0.0415 | watch_only | none |
| SNDK | memory_hbm_storage | 1678.8 |  | 1636.4356 | 2.5888 | 1651.355 | 1560 | 1.1669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 570.71 |  | 563.9622 | 1.1965 | 576.24 | 556.3 | 1.0759 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 930.4 |  | 924.6777 | 0.6188 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234.075 |  | 234.3391 | -0.1127 | 238.285 | 235.71 | 0.0214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 603.01 |  | 603.779 | -0.1274 | 614.15 | 605.39 | 0.2305 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 281.09 |  | 279.302 | 0.6402 | 283 | 276.24 | 4.2228 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.28 |  | 173.6259 | -0.1992 | 177.88 | 168.18 | 0.958 | below_vwap | below_vwap,spread_too_wide |
