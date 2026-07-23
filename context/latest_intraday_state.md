# Intraday State

- Generated at: `2026-07-24T01:01:19+08:00`
- Market time ET: `2026-07-23T13:01:20-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 5, 'spread_too_wide_or_missing': 12, 'price_stale_or_missing': 3, 'below_vwap': 21, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.845 |  | 693.1431 | -0.043 | 698.65 | 693.24 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.06 |  | 551.0185 | -0.174 | 557.38 | 545.965 | 0.0873 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.63 |  | 581.1952 | -0.0972 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| SPY | market_regime | 738.87 |  | 738.8114 | 0.0079 | 742.515 | 738.54 | 0.0041 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.42 |  | 1804.0458 | 0.2425 | 1806.11 | 1780.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.18 |  | 31.6022 | 1.8283 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.42 |  | 1804.0458 | 0.2425 | 1806.11 | 1780.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 291.765 |  | 291.6886 | 0.0262 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 3 | SPY | market_regime | 738.87 |  | 738.8114 | 0.0079 | 742.515 | 738.54 | 0.0041 | watch_only | none |
| 4 | ETN | data_center_power_cooling | 414.03 |  | 413.3581 | 0.1625 | 415.53 | 406.545 | 0.3212 | watch_only | none |
| 5 | NVDA | ai_accelerator | 209.91 |  | 208.4396 | 0.7054 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | TT | data_center_power_cooling | 478.41 |  | 476.7657 | 0.3449 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 144.155 |  | 143.9587 | 0.1364 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | TSM | foundry | 417.8 |  | 416.6663 | 0.2721 | 420.72 | 412.69 | 0.4787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ANET | ai_networking_optical | 177.12 |  | 176.7145 | 0.2295 | 177.84 | 173.19 | 2.2584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ARM | ai_accelerator | 281.475 |  | 279.3569 | 0.7582 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | META | cloud_ai_capex | 605.43 |  | 603.7954 | 0.2707 | 614.15 | 605.39 | 0.3518 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 374.675 |  | 372.0353 | 0.7095 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | CORZ | high_beta_ai_infrastructure | 24.22 |  | 24.049 | 0.7109 | 24.46 | 23.265 | 0.1239 | watch_only | none |
| 14 | MU | memory_hbm_storage | 994.735 |  | 990.9192 | 0.3851 | 999.04 | 964.86 | 0.5579 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | KLAC | semiconductor_equipment | 216.515 |  | 215.7309 | 0.3634 | 217.88 | 212.99 | 3.0945 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SMCI | ai_server_oem | 32.18 |  | 31.6022 | 1.8283 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |
| 17 | WDC | memory_hbm_storage | 568.325 |  | 564.1166 | 0.746 | 576.24 | 556.3 | 1.1666 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | GOOGL | cloud_ai_capex | 319.825 |  | 319.5211 | 0.0951 | 324.42 | 320.24 | 0.1313 | below_opening_15m_low | below_opening_15m_low |
| 19 | AMZN | cloud_ai_capex | 234.61 |  | 234.34 | 0.1152 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low |
| 20 | SMH | semiconductor_index | 580.63 |  | 581.1952 | -0.0972 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.42 |  | 1804.0458 | 0.2425 | 1806.11 | 1780.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.18 |  | 31.6022 | 1.8283 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1027 |  | 1011.9064 | 1.4916 | 1023.33 | 979.08 | 2.9211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | SNDK | memory_hbm_storage | 1667.78 |  | 1637.832 | 1.8285 | 1651.355 | 1560 | 1.6465 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | NVDA | ai_accelerator | 209.91 |  | 208.4396 | 0.7054 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 6 | ETN | data_center_power_cooling | 414.03 |  | 413.3581 | 0.1625 | 415.53 | 406.545 | 0.3212 | watch_only | none |
| 7 | IWM | market_regime | 291.765 |  | 291.6886 | 0.0262 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 8 | SPY | market_regime | 738.87 |  | 738.8114 | 0.0079 | 742.515 | 738.54 | 0.0041 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.22 |  | 24.049 | 0.7109 | 24.46 | 23.265 | 0.1239 | watch_only | none |
| 10 | SMH | semiconductor_index | 580.63 |  | 581.1952 | -0.0972 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 550.06 |  | 551.0185 | -0.174 | 557.38 | 545.965 | 0.0873 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 391.31 |  | 392.648 | -0.3408 | 397.34 | 390.54 | 2.8673 | below_vwap | below_vwap,spread_too_wide |
| 13 | AMAT | semiconductor_equipment | 564.97 |  | 566.3646 | -0.2462 | 566.18 | 548.47 | 4.0144 | below_vwap | below_vwap,spread_too_wide |
| 14 | PWR | data_center_power_cooling | 650.51 |  | 652.1837 | -0.2566 | 656.38 | 642.37 | 0.2536 | below_vwap | below_vwap |
| 15 | VRT | data_center_power_cooling | 304.56 |  | 306.3678 | -0.5901 | 311.13 | 303.96 | 1.2477 | below_vwap | below_vwap,spread_too_wide |
| 16 | LRCX | semiconductor_equipment | 320.9 |  | 321.3596 | -0.143 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 506.29 |  | 507.6364 | -0.2652 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | HPE | ai_server_oem | 48.31 |  | 48.3574 | -0.0981 | 48.88 | 47.635 | 0.1035 | below_vwap | below_vwap |
| 20 | COHR | ai_networking_optical | 316.33 |  | 318.2956 | -0.6176 | 320.13 | 307.04 | 4.2772 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.845 |  | 693.1431 | -0.043 | 698.65 | 693.24 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.53 |  | 66.58 | -0.075 | 68.245 | 66.7 | 0.015 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.91 |  | 208.4396 | 0.7054 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 381.335 |  | 382.8295 | -0.3904 | 391.71 | 387.245 | 0.1128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.735 |  | 321.1409 | -0.1264 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.825 |  | 319.5211 | 0.0951 | 324.42 | 320.24 | 0.1313 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 529.8 |  | 543.4309 | -2.5083 | 556.12 | 542.33 | 1.4402 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.8 |  | 416.6663 | 0.2721 | 420.72 | 412.69 | 0.4787 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.06 |  | 551.0185 | -0.174 | 557.38 | 545.965 | 0.0873 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.63 |  | 581.1952 | -0.0972 | 585.98 | 576.635 | 0.0878 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 391.31 |  | 392.648 | -0.3408 | 397.34 | 390.54 | 2.8673 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 994.735 |  | 990.9192 | 0.3851 | 999.04 | 964.86 | 0.5579 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 208.705 |  | 209.946 | -0.5911 | 213.785 | 207.665 | 0.4169 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.89 |  | 444.0896 | -0.045 | 450.07 | 438.55 | 1.8315 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.31 |  | 48.3574 | -0.0981 | 48.88 | 47.635 | 0.1035 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 32.18 |  | 31.6022 | 1.8283 | 31.52 | 30.23 | 0.0622 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.87 |  | 738.8114 | 0.0079 | 742.515 | 738.54 | 0.0041 | watch_only | none |
| IWM | market_regime | 291.765 |  | 291.6886 | 0.0262 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 121.29 |  | 122.1358 | -0.6925 | 124.22 | 122.07 | 0.1896 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.39 |  | 82.9103 | -0.6276 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 304.56 |  | 306.3678 | -0.5901 | 311.13 | 303.96 | 1.2477 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.03 |  | 413.3581 | 0.1625 | 415.53 | 406.545 | 0.3212 | watch_only | none |
| PWR | data_center_power_cooling | 650.51 |  | 652.1837 | -0.2566 | 656.38 | 642.37 | 0.2536 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1027 |  | 1011.9064 | 1.4916 | 1023.33 | 979.08 | 2.9211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.41 |  | 476.7657 | 0.3449 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.155 |  | 143.9587 | 0.1364 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.12 |  | 176.7145 | 0.2295 | 177.84 | 173.19 | 2.2584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316.33 |  | 318.2956 | -0.6176 | 320.13 | 307.04 | 4.2772 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 846.605 |  | 858.4754 | -1.3827 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.79 |  | 408.196 | -0.0995 | 408.58 | 397.9 | 0.255 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 113.765 |  | 114.7336 | -0.8442 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.71 |  | 327.8017 | -0.333 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1808.42 |  | 1804.0458 | 0.2425 | 1806.11 | 1780.9 | 0.0852 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 564.97 |  | 566.3646 | -0.2462 | 566.18 | 548.47 | 4.0144 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.9 |  | 321.3596 | -0.143 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.515 |  | 215.7309 | 0.3634 | 217.88 | 212.99 | 3.0945 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 374.675 |  | 372.0353 | 0.7095 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.74 |  | 295.3085 | -1.2084 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.035 |  | 65.3123 | -0.4246 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.65 |  | 54.6081 | 0.0768 | 55.76 | 53.78 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.28 |  | 135.4003 | -0.0889 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.93 |  | 342.8795 | 0.8897 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.29 |  | 507.6364 | -0.2652 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.02 |  | 296.1885 | -0.3945 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.85 |  | 30.0546 | -0.6808 | 31.13 | 29.12 | 0.067 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.82 |  | 41.7995 | -2.3434 | 43.21 | 40.51 | 0.049 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.22 |  | 24.049 | 0.7109 | 24.46 | 23.265 | 0.1239 | watch_only | none |
| SNDK | memory_hbm_storage | 1667.78 |  | 1637.832 | 1.8285 | 1651.355 | 1560 | 1.6465 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 568.325 |  | 564.1166 | 0.746 | 576.24 | 556.3 | 1.1666 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 924.155 |  | 924.6979 | -0.0587 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.61 |  | 234.34 | 0.1152 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 605.43 |  | 603.7954 | 0.2707 | 614.15 | 605.39 | 0.3518 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.475 |  | 279.3569 | 0.7582 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 173.39 |  | 173.6092 | -0.1263 | 177.88 | 168.18 | 2.8952 | below_vwap | below_vwap,spread_too_wide |
