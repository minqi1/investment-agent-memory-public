# Intraday State

- Generated at: `2026-07-24T01:23:06+08:00`
- Market time ET: `2026-07-23T13:23:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 11, 'watch_only': 6, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 2, 'below_vwap': 21, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.1 |  | 693.1227 | -0.0033 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.88 |  | 550.9802 | -0.0182 | 557.38 | 545.965 | 0.0617 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.24 |  | 581.1602 | -0.1583 | 585.98 | 576.635 | 0.0776 | below_vwap | below_vwap |
| SPY | market_regime | 738.62 |  | 738.7978 | -0.0241 | 742.515 | 738.54 | 0.0122 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 408.71 |  | 408.2027 | 0.1243 | 408.58 | 397.9 | 0.3034 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.355 |  | 31.6587 | 2.1993 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 408.71 |  | 408.2027 | 0.1243 | 408.58 | 397.9 | 0.3034 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1804.61 |  | 1804.0548 | 0.0308 | 1806.11 | 1780.9 | 0.1668 | watch_only | none |
| 3 | NVDA | ai_accelerator | 209.95 |  | 208.5145 | 0.6885 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 320.68 |  | 319.5356 | 0.3581 | 324.42 | 320.24 | 0.0655 | watch_only | none |
| 5 | META | cloud_ai_capex | 606.38 |  | 603.9302 | 0.4056 | 614.15 | 605.39 | 0.1253 | watch_only | none |
| 6 | JCI | data_center_power_cooling | 144.36 |  | 143.9644 | 0.2748 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ETN | data_center_power_cooling | 414.38 |  | 413.3917 | 0.2391 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | MKSI | semiconductor_materials | 343.45 |  | 342.8978 | 0.161 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | TSM | foundry | 417.62 |  | 416.6907 | 0.223 | 420.72 | 412.69 | 3.8791 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | APLD | high_beta_ai_infrastructure | 30.23 |  | 30.0525 | 0.5908 | 31.13 | 29.12 | 0.1654 | watch_only | none |
| 11 | TT | data_center_power_cooling | 478.6 |  | 476.8087 | 0.3757 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ANET | ai_networking_optical | 177.05 |  | 176.722 | 0.1856 | 177.84 | 173.19 | 2.2592 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | WDC | memory_hbm_storage | 567.03 |  | 564.2327 | 0.4958 | 576.24 | 556.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 374.86 |  | 372.229 | 0.7068 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 174.105 |  | 173.6142 | 0.2827 | 177.88 | 168.18 | 0.6203 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 925.72 |  | 924.6516 | 0.1155 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MU | memory_hbm_storage | 996.69 |  | 991.2909 | 0.5446 | 999.04 | 964.86 | 1.7949 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SMCI | ai_server_oem | 32.355 |  | 31.6587 | 2.1993 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| 19 | AMZN | cloud_ai_capex | 234.535 |  | 234.3552 | 0.0767 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 20 | ARM | ai_accelerator | 282.9 |  | 279.5309 | 1.2053 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 408.71 |  | 408.2027 | 0.1243 | 408.58 | 397.9 | 0.3034 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.355 |  | 31.6587 | 2.1993 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1033.885 |  | 1012.8082 | 2.081 | 1023.33 | 979.08 | 4.0507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1678.53 |  | 1639.8176 | 2.3608 | 1651.355 | 1560 | 4.4086 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.95 |  | 208.5145 | 0.6885 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | ASML | semiconductor_equipment | 1804.61 |  | 1804.0548 | 0.0308 | 1806.11 | 1780.9 | 0.1668 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 320.68 |  | 319.5356 | 0.3581 | 324.42 | 320.24 | 0.0655 | watch_only | none |
| 8 | META | cloud_ai_capex | 606.38 |  | 603.9302 | 0.4056 | 614.15 | 605.39 | 0.1253 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.27 |  | 24.0558 | 0.8902 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 30.23 |  | 30.0525 | 0.5908 | 31.13 | 29.12 | 0.1654 | watch_only | none |
| 11 | SMH | semiconductor_index | 580.24 |  | 581.1602 | -0.1583 | 585.98 | 576.635 | 0.0776 | below_vwap | below_vwap |
| 12 | SOXX | semiconductor_index | 550.88 |  | 550.9802 | -0.0182 | 557.38 | 545.965 | 0.0617 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 391.895 |  | 392.5784 | -0.1741 | 397.34 | 390.54 | 2.863 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMAT | semiconductor_equipment | 562.93 |  | 566.1423 | -0.5674 | 566.18 | 548.47 | 0.1919 | below_vwap | below_vwap |
| 15 | PWR | data_center_power_cooling | 650.9 |  | 652.1065 | -0.185 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 215.58 |  | 215.732 | -0.0705 | 217.88 | 212.99 | 0.0928 | below_vwap | below_vwap |
| 17 | VRT | data_center_power_cooling | 304.48 |  | 306.3271 | -0.603 | 311.13 | 303.96 | 1.2283 | below_vwap | below_vwap,spread_too_wide |
| 18 | IWM | market_regime | 291.61 |  | 291.6859 | -0.026 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 19 | LRCX | semiconductor_equipment | 321.1 |  | 321.3122 | -0.066 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | SPY | market_regime | 738.62 |  | 738.7978 | -0.0241 | 742.515 | 738.54 | 0.0122 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.1 |  | 693.1227 | -0.0033 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.65 |  | 66.5736 | 0.1147 | 68.245 | 66.7 | 0.015 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 209.95 |  | 208.5145 | 0.6885 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.29 |  | 382.7594 | -0.3839 | 391.71 | 387.245 | 0.0446 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.53 |  | 321.1181 | -0.1831 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.68 |  | 319.5356 | 0.3581 | 324.42 | 320.24 | 0.0655 | watch_only | none |
| AMD | ai_accelerator | 533.91 |  | 541.4717 | -1.3965 | 556.12 | 542.33 | 2.8095 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.62 |  | 416.6907 | 0.223 | 420.72 | 412.69 | 3.8791 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.88 |  | 550.9802 | -0.0182 | 557.38 | 545.965 | 0.0617 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.24 |  | 581.1602 | -0.1583 | 585.98 | 576.635 | 0.0776 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.895 |  | 392.5784 | -0.1741 | 397.34 | 390.54 | 2.863 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 996.69 |  | 991.2909 | 0.5446 | 999.04 | 964.86 | 1.7949 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 208.35 |  | 209.8437 | -0.7118 | 213.785 | 207.665 | 2.8798 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 442.59 |  | 444.064 | -0.3319 | 450.07 | 438.55 | 2.6639 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.32 |  | 48.3544 | -0.0712 | 48.88 | 47.635 | 0.1242 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.355 |  | 31.6587 | 2.1993 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.62 |  | 738.7978 | -0.0241 | 742.515 | 738.54 | 0.0122 | below_vwap | below_vwap |
| IWM | market_regime | 291.61 |  | 291.6859 | -0.026 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.95 |  | 122.0758 | -0.9223 | 124.22 | 122.07 | 0.4713 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.545 |  | 82.8609 | -0.3812 | 84.415 | 80.64 | 0.7269 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.48 |  | 306.3271 | -0.603 | 311.13 | 303.96 | 1.2283 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.38 |  | 413.3917 | 0.2391 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.9 |  | 652.1065 | -0.185 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1033.885 |  | 1012.8082 | 2.081 | 1023.33 | 979.08 | 4.0507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.6 |  | 476.8087 | 0.3757 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.36 |  | 143.9644 | 0.2748 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.05 |  | 176.722 | 0.1856 | 177.84 | 173.19 | 2.2592 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.68 |  | 318.2278 | -0.8006 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.31 |  | 858.2692 | -1.2769 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 408.71 |  | 408.2027 | 0.1243 | 408.58 | 397.9 | 0.3034 | buy_precheck_manual_confirm | none |
| AAOI | ai_networking_optical | 113.96 |  | 114.6826 | -0.6301 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.74 |  | 327.7866 | -0.0142 | 341.68 | 327.43 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1804.61 |  | 1804.0548 | 0.0308 | 1806.11 | 1780.9 | 0.1668 | watch_only | none |
| AMAT | semiconductor_equipment | 562.93 |  | 566.1423 | -0.5674 | 566.18 | 548.47 | 0.1919 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 321.1 |  | 321.3122 | -0.066 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.58 |  | 215.732 | -0.0705 | 217.88 | 212.99 | 0.0928 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 374.86 |  | 372.229 | 0.7068 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.24 |  | 294.9403 | -1.2546 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.21 |  | 65.306 | -0.147 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.18 |  | 135.3673 | -0.1384 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.45 |  | 342.8978 | 0.161 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.075 |  | 507.5676 | -0.2941 | 510.71 | 502.72 | 4.8254 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.275 |  | 296.0933 | -0.6141 | 299.26 | 295.795 | 0.3976 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.23 |  | 30.0525 | 0.5908 | 31.13 | 29.12 | 0.1654 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.15 |  | 41.7414 | -1.4169 | 43.21 | 40.51 | 0.0729 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.27 |  | 24.0558 | 0.8902 | 24.46 | 23.265 | 0.0824 | watch_only | none |
| SNDK | memory_hbm_storage | 1678.53 |  | 1639.8176 | 2.3608 | 1651.355 | 1560 | 4.4086 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 567.03 |  | 564.2327 | 0.4958 | 576.24 | 556.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 925.72 |  | 924.6516 | 0.1155 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234.535 |  | 234.3552 | 0.0767 | 238.285 | 235.71 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.38 |  | 603.9302 | 0.4056 | 614.15 | 605.39 | 0.1253 | watch_only | none |
| ARM | ai_accelerator | 282.9 |  | 279.5309 | 1.2053 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 174.105 |  | 173.6142 | 0.2827 | 177.88 | 168.18 | 0.6203 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
