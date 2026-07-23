# Intraday State

- Generated at: `2026-07-24T01:19:12+08:00`
- Market time ET: `2026-07-23T13:19:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 6, 'spread_too_wide_or_missing': 12, 'price_stale_or_missing': 3, 'below_vwap': 20, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.22 |  | 693.1229 | -0.1303 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.58 |  | 550.9819 | -0.0729 | 557.38 | 545.965 | 0.0908 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.555 |  | 581.1617 | -0.1044 | 585.98 | 576.635 | 0.0672 | below_vwap | below_vwap |
| SPY | market_regime | 738.32 |  | 738.8007 | -0.0651 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 0.2153 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.375 |  | 31.6494 | 2.2925 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 0.2153 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1805.06 |  | 1804.0494 | 0.056 | 1806.11 | 1780.9 | 0.0698 | watch_only | none |
| 3 | KLAC | semiconductor_equipment | 215.81 |  | 215.731 | 0.0366 | 217.88 | 212.99 | 0.0927 | watch_only | none |
| 4 | NVDA | ai_accelerator | 209.94 |  | 208.5046 | 0.6885 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 5 | MU | memory_hbm_storage | 997.215 |  | 991.1338 | 0.6136 | 999.04 | 964.86 | 0.2898 | watch_only | none |
| 6 | APLD | high_beta_ai_infrastructure | 30.12 |  | 30.0509 | 0.2301 | 31.13 | 29.12 | 0.0664 | watch_only | none |
| 7 | TT | data_center_power_cooling | 477.7 |  | 476.7827 | 0.1924 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 144.135 |  | 143.9628 | 0.1196 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 414.43 |  | 413.3889 | 0.2518 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TSM | foundry | 417.785 |  | 416.6862 | 0.2637 | 420.72 | 412.69 | 4.2821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ANET | ai_networking_optical | 176.895 |  | 176.7207 | 0.0986 | 177.84 | 173.19 | 1.8768 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | META | cloud_ai_capex | 605.53 |  | 603.9209 | 0.2664 | 614.15 | 605.39 | 1.8116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TER | semiconductor_test_packaging | 374.795 |  | 372.2234 | 0.6909 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SKHY | memory_hbm_storage | 174.02 |  | 173.6105 | 0.2359 | 177.88 | 168.18 | 0.7413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0543 | 0.3563 | 24.46 | 23.265 | 0.1243 | watch_only | none |
| 16 | SMCI | ai_server_oem | 32.375 |  | 31.6494 | 2.2925 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| 17 | WDC | memory_hbm_storage | 566.87 |  | 564.2179 | 0.47 | 576.24 | 556.3 | 1.72 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | GOOGL | cloud_ai_capex | 320.205 |  | 319.532 | 0.2106 | 324.42 | 320.24 | 0.1343 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMZN | cloud_ai_capex | 234.38 |  | 234.3544 | 0.0109 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low |
| 20 | ARM | ai_accelerator | 282.11 |  | 279.4738 | 0.9433 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 0.2153 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.375 |  | 31.6494 | 2.2925 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1031.73 |  | 1012.7133 | 1.8778 | 1023.33 | 979.08 | 3.0909 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1674.335 |  | 1638.9651 | 2.1581 | 1651.355 | 1560 | 0.4772 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.94 |  | 208.5046 | 0.6885 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | MU | memory_hbm_storage | 997.215 |  | 991.1338 | 0.6136 | 999.04 | 964.86 | 0.2898 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1805.06 |  | 1804.0494 | 0.056 | 1806.11 | 1780.9 | 0.0698 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 215.81 |  | 215.731 | 0.0366 | 217.88 | 212.99 | 0.0927 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0543 | 0.3563 | 24.46 | 23.265 | 0.1243 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 30.12 |  | 30.0509 | 0.2301 | 31.13 | 29.12 | 0.0664 | watch_only | none |
| 11 | SMH | semiconductor_index | 580.555 |  | 581.1617 | -0.1044 | 585.98 | 576.635 | 0.0672 | below_vwap | below_vwap |
| 12 | SOXX | semiconductor_index | 550.58 |  | 550.9819 | -0.0729 | 557.38 | 545.965 | 0.0908 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 391.9 |  | 392.5804 | -0.1733 | 397.34 | 390.54 | 2.863 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMAT | semiconductor_equipment | 563.66 |  | 566.1663 | -0.4427 | 566.18 | 548.47 | 0.1384 | below_vwap | below_vwap |
| 15 | PWR | data_center_power_cooling | 650.735 |  | 652.1104 | -0.2109 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | VRT | data_center_power_cooling | 304.48 |  | 306.3271 | -0.603 | 311.13 | 303.96 | 0.5222 | below_vwap | below_vwap,spread_too_wide |
| 17 | IWM | market_regime | 291.635 |  | 291.6862 | -0.0176 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 18 | LRCX | semiconductor_equipment | 320.43 |  | 321.3156 | -0.2756 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 506.025 |  | 507.5746 | -0.3053 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.22 |  | 693.1229 | -0.1303 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.44 |  | 66.5732 | -0.2002 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.94 |  | 208.5046 | 0.6885 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.09 |  | 382.7714 | -0.4393 | 391.71 | 387.245 | 0.7951 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.315 |  | 321.1224 | -0.2514 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.205 |  | 319.532 | 0.2106 | 324.42 | 320.24 | 0.1343 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 532.89 |  | 541.6043 | -1.609 | 556.12 | 542.33 | 3.3778 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.785 |  | 416.6862 | 0.2637 | 420.72 | 412.69 | 4.2821 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.58 |  | 550.9819 | -0.0729 | 557.38 | 545.965 | 0.0908 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.555 |  | 581.1617 | -0.1044 | 585.98 | 576.635 | 0.0672 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.9 |  | 392.5804 | -0.1733 | 397.34 | 390.54 | 2.863 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 997.215 |  | 991.1338 | 0.6136 | 999.04 | 964.86 | 0.2898 | watch_only | none |
| MRVL | custom_silicon_networking | 208.135 |  | 209.8523 | -0.8183 | 213.785 | 207.665 | 1.5999 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.86 |  | 444.0706 | -0.0474 | 450.07 | 438.55 | 1.8407 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.34 |  | 48.3545 | -0.0299 | 48.88 | 47.635 | 0.1862 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.375 |  | 31.6494 | 2.2925 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.32 |  | 738.8007 | -0.0651 | 742.515 | 738.54 | 0.019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.635 |  | 291.6862 | -0.0176 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.99 |  | 122.0852 | -0.8971 | 124.22 | 122.07 | 0.4876 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.49 |  | 82.8638 | -0.4511 | 84.415 | 80.64 | 0.6304 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.48 |  | 306.3271 | -0.603 | 311.13 | 303.96 | 0.5222 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.43 |  | 413.3889 | 0.2518 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.735 |  | 652.1104 | -0.2109 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1031.73 |  | 1012.7133 | 1.8778 | 1023.33 | 979.08 | 3.0909 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.7 |  | 476.7827 | 0.1924 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.135 |  | 143.9628 | 0.1196 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.895 |  | 176.7207 | 0.0986 | 177.84 | 173.19 | 1.8768 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316 |  | 318.242 | -0.7045 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 846.93 |  | 858.3092 | -1.3258 | 880.26 | 833 | 4.1172 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 408.76 |  | 408.1985 | 0.1376 | 408.58 | 397.9 | 0.2153 | buy_precheck_manual_confirm | none |
| AAOI | ai_networking_optical | 113.77 |  | 114.6883 | -0.8007 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.74 |  | 327.7866 | -0.0142 | 341.68 | 327.43 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.06 |  | 1804.0494 | 0.056 | 1806.11 | 1780.9 | 0.0698 | watch_only | none |
| AMAT | semiconductor_equipment | 563.66 |  | 566.1663 | -0.4427 | 566.18 | 548.47 | 0.1384 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 320.43 |  | 321.3156 | -0.2756 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.81 |  | 215.731 | 0.0366 | 217.88 | 212.99 | 0.0927 | watch_only | none |
| TER | semiconductor_test_packaging | 374.795 |  | 372.2234 | 0.6909 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.59 |  | 295.0222 | -1.1634 | 301.305 | 293.685 | 0.4733 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.07 |  | 65.3068 | -0.3626 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.18 |  | 135.3673 | -0.1384 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.69 |  | 342.8882 | 0.2339 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.025 |  | 507.5746 | -0.3053 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.74 |  | 296.1055 | -0.4611 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.12 |  | 30.0509 | 0.2301 | 31.13 | 29.12 | 0.0664 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 40.94 |  | 41.7457 | -1.93 | 43.21 | 40.51 | 0.0733 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.14 |  | 24.0543 | 0.3563 | 24.46 | 23.265 | 0.1243 | watch_only | none |
| SNDK | memory_hbm_storage | 1674.335 |  | 1638.9651 | 2.1581 | 1651.355 | 1560 | 0.4772 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 566.87 |  | 564.2179 | 0.47 | 576.24 | 556.3 | 1.72 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 924.4 |  | 924.6403 | -0.026 | 933.5 | 908.955 | 1.2343 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 234.38 |  | 234.3544 | 0.0109 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 605.53 |  | 603.9209 | 0.2664 | 614.15 | 605.39 | 1.8116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 282.11 |  | 279.4738 | 0.9433 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 174.02 |  | 173.6105 | 0.2359 | 177.88 | 168.18 | 0.7413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
