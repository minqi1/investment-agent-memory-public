# Intraday State

- Generated at: `2026-07-23T23:40:52+08:00`
- Market time ET: `2026-07-23T11:40:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 18, 'below_vwap': 30, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.12 |  | 693.4472 | -0.4798 | 698.65 | 693.24 | 0.0319 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.61 |  | 551.9155 | -0.7801 | 557.38 | 545.965 | 0.0931 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.135 |  | 581.457 | -0.7433 | 585.98 | 576.635 | 0.0936 | below_vwap | below_vwap |
| SPY | market_regime | 737.38 |  | 739.0397 | -0.2246 | 742.515 | 738.54 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 476.65 |  | 476.6109 | 0.0082 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | LIN | industrial_gases | 508.14 |  | 507.7228 | 0.0822 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MU | memory_hbm_storage | 988.9 |  | 988.5126 | 0.0392 | 999.04 | 964.86 | 0.454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | WDC | memory_hbm_storage | 564.83 |  | 562.9141 | 0.3404 | 576.24 | 556.3 | 0.887 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SNDK | memory_hbm_storage | 1633.765 |  | 1625.0612 | 0.5356 | 1651.355 | 1560 | 0.5992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | TSM | foundry | 413.49 |  | 416.966 | -0.8336 | 420.72 | 412.69 | 0.0846 | below_vwap | below_vwap |
| 7 | SMH | semiconductor_index | 577.135 |  | 581.457 | -0.7433 | 585.98 | 576.635 | 0.0936 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 547.61 |  | 551.9155 | -0.7801 | 557.38 | 545.965 | 0.0931 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 291.23 |  | 291.7323 | -0.1722 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 31.2 |  | 31.4654 | -0.8436 | 31.52 | 30.23 | 0.0641 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 41.63 |  | 41.9853 | -0.8462 | 43.21 | 40.51 | 0.048 | below_vwap | below_vwap |
| 13 | AAPL | mega_cap_platform | 320.98 |  | 321.273 | -0.0912 | 323.25 | 320.82 | 0.0156 | below_vwap | below_vwap |
| 14 | TER | semiconductor_test_packaging | 369.46 |  | 371.9431 | -0.6676 | 376.78 | 363.37 | 0.2301 | below_vwap | below_vwap |
| 15 | ANET | ai_networking_optical | 175.175 |  | 176.7848 | -0.9106 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | SKHY | memory_hbm_storage | 170.77 |  | 173.6936 | -1.6832 | 177.88 | 168.18 | 0.1581 | below_vwap | below_vwap |
| 17 | JCI | data_center_power_cooling | 143.735 |  | 143.9671 | -0.1612 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 647.26 |  | 653.5071 | -0.9559 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 412.975 |  | 413.2712 | -0.0717 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LRCX | semiconductor_equipment | 318.83 |  | 321.5442 | -0.8441 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 413.49 |  | 416.966 | -0.8336 | 420.72 | 412.69 | 0.0846 | below_vwap | below_vwap |
| 2 | SMH | semiconductor_index | 577.135 |  | 581.457 | -0.7433 | 585.98 | 576.635 | 0.0936 | below_vwap | below_vwap |
| 3 | SOXX | semiconductor_index | 547.61 |  | 551.9155 | -0.7801 | 557.38 | 545.965 | 0.0931 | below_vwap | below_vwap |
| 4 | ASML | semiconductor_equipment | 1796.665 |  | 1805.284 | -0.4774 | 1806.11 | 1780.9 | 3.0033 | below_vwap | below_vwap,spread_too_wide |
| 5 | AMAT | semiconductor_equipment | 564.05 |  | 566.6714 | -0.4626 | 566.18 | 548.47 | 1.0371 | below_vwap | below_vwap,spread_too_wide |
| 6 | ANET | ai_networking_optical | 175.175 |  | 176.7848 | -0.9106 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 143.735 |  | 143.9671 | -0.1612 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | PWR | data_center_power_cooling | 647.26 |  | 653.5071 | -0.9559 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 214.46 |  | 215.9245 | -0.6782 | 217.88 | 212.99 | 2.1542 | below_vwap | below_vwap,spread_too_wide |
| 10 | ETN | data_center_power_cooling | 412.975 |  | 413.2712 | -0.0717 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GEV | data_center_power_cooling | 1011.02 |  | 1011.1252 | -0.0104 | 1023.33 | 979.08 | 3.1819 | below_vwap | below_vwap,spread_too_wide |
| 12 | IWM | market_regime | 291.23 |  | 291.7323 | -0.1722 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 318.83 |  | 321.5442 | -0.8441 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ARM | ai_accelerator | 276.78 |  | 279.2867 | -0.8975 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | APD | industrial_gases | 296.315 |  | 296.7758 | -0.1553 | 299.26 | 295.795 | 5.0892 | below_vwap | below_vwap,spread_too_wide |
| 17 | HPE | ai_server_oem | 48.08 |  | 48.4121 | -0.6859 | 48.88 | 47.635 | 4.5341 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 313.85 |  | 318.9017 | -1.5841 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | CIEN | ai_networking_optical | 406.14 |  | 409.0314 | -0.7069 | 408.58 | 397.9 | 4.6339 | below_vwap | below_vwap,spread_too_wide |
| 20 | TER | semiconductor_test_packaging | 369.46 |  | 371.9431 | -0.6676 | 376.78 | 363.37 | 0.2301 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.12 |  | 693.4472 | -0.4798 | 698.65 | 693.24 | 0.0319 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.72 |  | 66.6444 | -1.3871 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.345 |  | 208.2576 | -0.4382 | 210.85 | 208.49 | 0.0241 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 379 |  | 383.7686 | -1.2426 | 391.71 | 387.245 | 0.5699 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.98 |  | 321.273 | -0.0912 | 323.25 | 320.82 | 0.0156 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 318.61 |  | 319.501 | -0.2789 | 324.42 | 320.24 | 0.3327 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.94 |  | 547.3707 | -1.5402 | 556.12 | 542.33 | 1.0799 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 413.49 |  | 416.966 | -0.8336 | 420.72 | 412.69 | 0.0846 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.61 |  | 551.9155 | -0.7801 | 557.38 | 545.965 | 0.0931 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.135 |  | 581.457 | -0.7433 | 585.98 | 576.635 | 0.0936 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 388.85 |  | 393.1836 | -1.1022 | 397.34 | 390.54 | 0.8049 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 988.9 |  | 988.5126 | 0.0392 | 999.04 | 964.86 | 0.454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 206.915 |  | 210.3344 | -1.6257 | 213.785 | 207.665 | 1.0052 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 440.76 |  | 444.1714 | -0.768 | 450.07 | 438.55 | 0.4628 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.08 |  | 48.4121 | -0.6859 | 48.88 | 47.635 | 4.5341 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 31.2 |  | 31.4654 | -0.8436 | 31.52 | 30.23 | 0.0641 | below_vwap | below_vwap |
| SPY | market_regime | 737.38 |  | 739.0397 | -0.2246 | 742.515 | 738.54 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.23 |  | 291.7323 | -0.1722 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.42 |  | 122.6704 | -1.8345 | 124.22 | 122.07 | 0.0664 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.03 |  | 83.067 | -1.2484 | 84.415 | 80.64 | 4.4984 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.49 |  | 307.4713 | -1.6201 | 311.13 | 303.96 | 0.9785 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.975 |  | 413.2712 | -0.0717 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 647.26 |  | 653.5071 | -0.9559 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1011.02 |  | 1011.1252 | -0.0104 | 1023.33 | 979.08 | 3.1819 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.65 |  | 476.6109 | 0.0082 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.735 |  | 143.9671 | -0.1612 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.175 |  | 176.7848 | -0.9106 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 313.85 |  | 318.9017 | -1.5841 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 831.55 |  | 861.8131 | -3.5116 | 880.26 | 833 | 0.6566 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 406.14 |  | 409.0314 | -0.7069 | 408.58 | 397.9 | 4.6339 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.65 |  | 114.9922 | -2.0369 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.235 |  | 328.0837 | -1.1731 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.665 |  | 1805.284 | -0.4774 | 1806.11 | 1780.9 | 3.0033 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 564.05 |  | 566.6714 | -0.4626 | 566.18 | 548.47 | 1.0371 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.83 |  | 321.5442 | -0.8441 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.46 |  | 215.9245 | -0.6782 | 217.88 | 212.99 | 2.1542 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 369.46 |  | 371.9431 | -0.6676 | 376.78 | 363.37 | 0.2301 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 290.885 |  | 295.8891 | -1.6912 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.59 |  | 65.4169 | -1.2641 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.78 |  | 54.9332 | -2.0993 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 133.995 |  | 135.5665 | -1.1592 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.325 |  | 344.4459 | -1.4867 | 347.92 | 341.755 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 508.14 |  | 507.7228 | 0.0822 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.315 |  | 296.7758 | -0.1553 | 299.26 | 295.795 | 5.0892 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30 |  | 30.086 | -0.2858 | 31.13 | 29.12 | 0.1 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.63 |  | 41.9853 | -0.8462 | 43.21 | 40.51 | 0.048 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.03 |  | 24.055 | -0.1039 | 24.46 | 23.265 | 0.1248 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1633.765 |  | 1625.0612 | 0.5356 | 1651.355 | 1560 | 0.5992 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 564.83 |  | 562.9141 | 0.3404 | 576.24 | 556.3 | 0.887 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 922.49 |  | 923.5351 | -0.1132 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 232.905 |  | 234.4921 | -0.6768 | 238.285 | 235.71 | 0.0129 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 597.93 |  | 604.728 | -1.1241 | 614.15 | 605.39 | 0.2609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 276.78 |  | 279.2867 | -0.8975 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 170.77 |  | 173.6936 | -1.6832 | 177.88 | 168.18 | 0.1581 | below_vwap | below_vwap |
