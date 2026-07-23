# Intraday State

- Generated at: `2026-07-24T00:56:46+08:00`
- Market time ET: `2026-07-23T12:56:48-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 6, 'below_vwap': 25, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 8, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.405 |  | 693.1484 | -0.1072 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.61 |  | 551.0219 | -0.2562 | 557.38 | 545.965 | 0.0837 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.845 |  | 581.2115 | -0.2351 | 585.98 | 576.635 | 0.0724 | below_vwap | below_vwap |
| SPY | market_regime | 738.25 |  | 738.8164 | -0.0767 | 742.515 | 738.54 | 0.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.89 |  | 31.5954 | 0.9326 | 31.52 | 30.23 | 0.0314 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1804.55 |  | 1804.0276 | 0.029 | 1806.11 | 1780.9 | 0.0682 | watch_only | none |
| 2 | TSM | foundry | 417.07 |  | 416.659 | 0.0986 | 420.72 | 412.69 | 0.247 | watch_only | none |
| 3 | NVDA | ai_accelerator | 209.7 |  | 208.4213 | 0.6135 | 210.85 | 208.49 | 0.0191 | watch_only | none |
| 4 | META | cloud_ai_capex | 606.18 |  | 603.7755 | 0.3982 | 614.15 | 605.39 | 0.2573 | watch_only | none |
| 5 | SMCI | ai_server_oem | 31.89 |  | 31.5954 | 0.9326 | 31.52 | 30.23 | 0.0314 | buy_precheck_manual_confirm | none |
| 6 | COHU | semiconductor_test_packaging | 54.65 |  | 54.6081 | 0.0768 | 55.76 | 53.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.0477 | 0.3006 | 24.46 | 23.265 | 0.0829 | watch_only | none |
| 8 | GEV | data_center_power_cooling | 1022.31 |  | 1011.8771 | 1.031 | 1023.33 | 979.08 | 0.1585 | watch_only | none |
| 9 | MU | memory_hbm_storage | 992.54 |  | 990.8386 | 0.1717 | 999.04 | 964.86 | 1.7128 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ANET | ai_networking_optical | 176.84 |  | 176.7106 | 0.0732 | 177.84 | 173.19 | 2.2619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | KLAC | semiconductor_equipment | 216.22 |  | 215.7195 | 0.232 | 217.88 | 212.99 | 2.9599 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 373.905 |  | 372.0306 | 0.5038 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | WDC | memory_hbm_storage | 567.86 |  | 564.0928 | 0.6678 | 576.24 | 556.3 | 1.474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMZN | cloud_ai_capex | 234.61 |  | 234.3377 | 0.1162 | 238.285 | 235.71 | 0.017 | below_opening_15m_low | below_opening_15m_low |
| 15 | ARM | ai_accelerator | 281.8 |  | 279.3373 | 0.8816 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SMH | semiconductor_index | 579.845 |  | 581.2115 | -0.2351 | 585.98 | 576.635 | 0.0724 | below_vwap | below_vwap |
| 17 | SOXX | semiconductor_index | 549.61 |  | 551.0219 | -0.2562 | 557.38 | 545.965 | 0.0837 | below_vwap | below_vwap |
| 18 | AMAT | semiconductor_equipment | 565.45 |  | 566.4057 | -0.1687 | 566.18 | 548.47 | 0.1114 | below_vwap | below_vwap |
| 19 | TT | data_center_power_cooling | 477.41 |  | 476.7565 | 0.1371 | 480 | 472.33 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 20 | IWM | market_regime | 291.47 |  | 291.6899 | -0.0754 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.89 |  | 31.5954 | 0.9326 | 31.52 | 30.23 | 0.0314 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 417.07 |  | 416.659 | 0.0986 | 420.72 | 412.69 | 0.247 | watch_only | none |
| 3 | SNDK | memory_hbm_storage | 1664.625 |  | 1637.2825 | 1.67 | 1651.355 | 1560 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | NVDA | ai_accelerator | 209.7 |  | 208.4213 | 0.6135 | 210.85 | 208.49 | 0.0191 | watch_only | none |
| 5 | ASML | semiconductor_equipment | 1804.55 |  | 1804.0276 | 0.029 | 1806.11 | 1780.9 | 0.0682 | watch_only | none |
| 6 | GEV | data_center_power_cooling | 1022.31 |  | 1011.8771 | 1.031 | 1023.33 | 979.08 | 0.1585 | watch_only | none |
| 7 | META | cloud_ai_capex | 606.18 |  | 603.7755 | 0.3982 | 614.15 | 605.39 | 0.2573 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.0477 | 0.3006 | 24.46 | 23.265 | 0.0829 | watch_only | none |
| 9 | SMH | semiconductor_index | 579.845 |  | 581.2115 | -0.2351 | 585.98 | 576.635 | 0.0724 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 549.61 |  | 551.0219 | -0.2562 | 557.38 | 545.965 | 0.0837 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 390.86 |  | 392.6531 | -0.4567 | 397.34 | 390.54 | 1.5607 | below_vwap | below_vwap,spread_too_wide |
| 12 | AMAT | semiconductor_equipment | 565.45 |  | 566.4057 | -0.1687 | 566.18 | 548.47 | 0.1114 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 143.77 |  | 143.9566 | -0.1297 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 648.265 |  | 652.207 | -0.6044 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | VRT | data_center_power_cooling | 304.05 |  | 306.3824 | -0.7613 | 311.13 | 303.96 | 1.1215 | below_vwap | below_vwap,spread_too_wide |
| 16 | ETN | data_center_power_cooling | 412.94 |  | 413.3559 | -0.1006 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | IWM | market_regime | 291.47 |  | 291.6899 | -0.0754 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 18 | LRCX | semiconductor_equipment | 320.46 |  | 321.3645 | -0.2815 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 506.31 |  | 507.6381 | -0.2616 | 510.71 | 502.72 | 4.7797 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.405 |  | 693.1484 | -0.1072 | 698.65 | 693.24 | 0.0072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.37 |  | 66.5815 | -0.3176 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.7 |  | 208.4213 | 0.6135 | 210.85 | 208.49 | 0.0191 | watch_only | none |
| MSFT | cloud_ai_capex | 381.17 |  | 382.8444 | -0.4374 | 391.71 | 387.245 | 0.021 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.82 |  | 321.1478 | -0.1021 | 323.25 | 320.82 | 0.0187 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 319.33 |  | 319.5282 | -0.062 | 324.42 | 320.24 | 0.166 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 525.36 |  | 544.839 | -3.5752 | 556.12 | 542.33 | 0.8661 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.07 |  | 416.659 | 0.0986 | 420.72 | 412.69 | 0.247 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.61 |  | 551.0219 | -0.2562 | 557.38 | 545.965 | 0.0837 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.845 |  | 581.2115 | -0.2351 | 585.98 | 576.635 | 0.0724 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.86 |  | 392.6531 | -0.4567 | 397.34 | 390.54 | 1.5607 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.54 |  | 990.8386 | 0.1717 | 999.04 | 964.86 | 1.7128 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 208.48 |  | 209.9559 | -0.703 | 213.785 | 207.665 | 1.3766 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.5 |  | 444.0923 | -0.1334 | 450.07 | 438.55 | 1.8985 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.33 |  | 48.3578 | -0.0576 | 48.88 | 47.635 | 0.1035 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.89 |  | 31.5954 | 0.9326 | 31.52 | 30.23 | 0.0314 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.25 |  | 738.8164 | -0.0767 | 742.515 | 738.54 | 0.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.47 |  | 291.6899 | -0.0754 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.98 |  | 122.1514 | -0.959 | 124.22 | 122.07 | 0.4794 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.405 |  | 82.915 | -0.6151 | 84.415 | 80.64 | 0.5582 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.05 |  | 306.3824 | -0.7613 | 311.13 | 303.96 | 1.1215 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.94 |  | 413.3559 | -0.1006 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 648.265 |  | 652.207 | -0.6044 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1022.31 |  | 1011.8771 | 1.031 | 1023.33 | 979.08 | 0.1585 | watch_only | none |
| TT | data_center_power_cooling | 477.41 |  | 476.7565 | 0.1371 | 480 | 472.33 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| JCI | data_center_power_cooling | 143.77 |  | 143.9566 | -0.1297 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.84 |  | 176.7106 | 0.0732 | 177.84 | 173.19 | 2.2619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.65 |  | 318.3224 | -0.8395 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.275 |  | 858.5645 | -1.3149 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.975 |  | 408.1956 | -0.054 | 408.58 | 397.9 | 4.2576 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 113.14 |  | 114.7476 | -1.401 | 118.01 | 108.505 | 0.3005 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 326.71 |  | 327.8017 | -0.333 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1804.55 |  | 1804.0276 | 0.029 | 1806.11 | 1780.9 | 0.0682 | watch_only | none |
| AMAT | semiconductor_equipment | 565.45 |  | 566.4057 | -0.1687 | 566.18 | 548.47 | 0.1114 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 320.46 |  | 321.3645 | -0.2815 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.22 |  | 215.7195 | 0.232 | 217.88 | 212.99 | 2.9599 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373.905 |  | 372.0306 | 0.5038 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.74 |  | 295.3085 | -1.2084 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.98 |  | 65.3182 | -0.5178 | 67.455 | 65.81 | 0.4001 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.65 |  | 54.6081 | 0.0768 | 55.76 | 53.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.125 |  | 135.4011 | -0.2039 | 137.81 | 135.66 | 5.1064 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 345.93 |  | 342.8795 | 0.8897 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.31 |  | 507.6381 | -0.2616 | 510.71 | 502.72 | 4.7797 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.945 |  | 296.2261 | -0.4325 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.785 |  | 30.0562 | -0.9024 | 31.13 | 29.12 | 0.2686 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.87 |  | 41.8046 | -2.2356 | 43.21 | 40.51 | 0.0245 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.12 |  | 24.0477 | 0.3006 | 24.46 | 23.265 | 0.0829 | watch_only | none |
| SNDK | memory_hbm_storage | 1664.625 |  | 1637.2825 | 1.67 | 1651.355 | 1560 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 567.86 |  | 564.0928 | 0.6678 | 576.24 | 556.3 | 1.474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 922.89 |  | 924.7027 | -0.196 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.61 |  | 234.3377 | 0.1162 | 238.285 | 235.71 | 0.017 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 606.18 |  | 603.7755 | 0.3982 | 614.15 | 605.39 | 0.2573 | watch_only | none |
| ARM | ai_accelerator | 281.8 |  | 279.3373 | 0.8816 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 172.93 |  | 173.611 | -0.3923 | 177.88 | 168.18 | 0.5725 | below_vwap | below_vwap,spread_too_wide |
