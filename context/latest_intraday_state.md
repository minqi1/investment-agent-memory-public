# Intraday State

- Generated at: `2026-07-24T03:14:20+08:00`
- Market time ET: `2026-07-23T15:14:21-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 25, 'below_vwap': 23, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 3, 'manual_confirm_candidate': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.45 |  | 692.8085 | -0.4848 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545.44 |  | 550.6708 | -0.9499 | 557.38 | 545.965 | 0.066 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.9 |  | 580.5436 | -0.7999 | 585.98 | 576.635 | 0.0469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.68 |  | 738.4886 | -0.2449 | 742.515 | 738.54 | 0.0081 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1033.23 |  | 1016.4548 | 1.6504 | 1023.33 | 979.08 | 0.1791 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 215.78 |  | 215.4618 | 0.1477 | 217.88 | 212.99 | 0.139 | watch_only | none |
| 2 | META | cloud_ai_capex | 605.64 |  | 604.6185 | 0.169 | 614.15 | 605.39 | 0.0182 | watch_only | none |
| 3 | TT | data_center_power_cooling | 478.17 |  | 476.8757 | 0.2714 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ETN | data_center_power_cooling | 413.67 |  | 413.3334 | 0.0814 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.89 |  | 295.6885 | 0.0681 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1033.23 |  | 1016.4548 | 1.6504 | 1023.33 | 979.08 | 0.1791 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1792.7 |  | 1801.6667 | -0.4977 | 1806.11 | 1780.9 | 0.0407 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.275 |  | 291.6104 | -0.115 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 9 | CRWV | gpu_cloud_ai_factory | 80.655 |  | 82.5713 | -2.3208 | 84.415 | 80.64 | 0.0372 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 30.985 |  | 31.5798 | -1.8834 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 143.27 |  | 143.8086 | -0.3745 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 317.65 |  | 320.2841 | -0.8224 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ARM | ai_accelerator | 279.04 |  | 279.5651 | -0.1878 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | LIN | industrial_gases | 506.025 |  | 507.1954 | -0.2308 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | TER | semiconductor_test_packaging | 368.555 |  | 371.8859 | -0.8957 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | AAOI | ai_networking_optical | 111.27 |  | 114.4056 | -2.7408 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | TSM | foundry | 414.46 |  | 416.3738 | -0.4596 | 420.72 | 412.69 | 0.6321 | below_vwap | below_vwap,spread_too_wide |
| 19 | MU | memory_hbm_storage | 980.15 |  | 991.1433 | -1.1092 | 999.04 | 964.86 | 1.0713 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 557.28 |  | 564.1515 | -1.218 | 566.18 | 548.47 | 3.4973 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1033.23 |  | 1016.4548 | 1.6504 | 1023.33 | 979.08 | 0.1791 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 215.78 |  | 215.4618 | 0.1477 | 217.88 | 212.99 | 0.139 | watch_only | none |
| 3 | META | cloud_ai_capex | 605.64 |  | 604.6185 | 0.169 | 614.15 | 605.39 | 0.0182 | watch_only | none |
| 4 | TSM | foundry | 414.46 |  | 416.3738 | -0.4596 | 420.72 | 412.69 | 0.6321 | below_vwap | below_vwap,spread_too_wide |
| 5 | MU | memory_hbm_storage | 980.15 |  | 991.1433 | -1.1092 | 999.04 | 964.86 | 1.0713 | below_vwap | below_vwap,spread_too_wide |
| 6 | ASML | semiconductor_equipment | 1792.7 |  | 1801.6667 | -0.4977 | 1806.11 | 1780.9 | 0.0407 | below_vwap | below_vwap |
| 7 | AMAT | semiconductor_equipment | 557.28 |  | 564.1515 | -1.218 | 566.18 | 548.47 | 3.4973 | below_vwap | below_vwap,spread_too_wide |
| 8 | ANET | ai_networking_optical | 175.3 |  | 176.6403 | -0.7588 | 177.84 | 173.19 | 3.1375 | below_vwap | below_vwap,spread_too_wide |
| 9 | JCI | data_center_power_cooling | 143.27 |  | 143.8086 | -0.3745 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 648.17 |  | 651.605 | -0.5272 | 656.38 | 642.37 | 1.5181 | below_vwap | below_vwap,spread_too_wide |
| 11 | IWM | market_regime | 291.275 |  | 291.6104 | -0.115 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 12 | LRCX | semiconductor_equipment | 317.65 |  | 320.2841 | -0.8224 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ARM | ai_accelerator | 279.04 |  | 279.5651 | -0.1878 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | WDC | memory_hbm_storage | 558.01 |  | 564.1168 | -1.0825 | 576.24 | 556.3 | 3.758 | below_vwap | below_vwap,spread_too_wide |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LIN | industrial_gases | 506.025 |  | 507.1954 | -0.2308 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | COHR | ai_networking_optical | 311.36 |  | 317.3865 | -1.8988 | 320.13 | 307.04 | 4.5189 | below_vwap | below_vwap,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 404.03 |  | 407.8956 | -0.9477 | 408.58 | 397.9 | 3.9007 | below_vwap | below_vwap,spread_too_wide |
| 19 | TER | semiconductor_test_packaging | 368.555 |  | 371.8859 | -0.8957 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CRWV | gpu_cloud_ai_factory | 80.655 |  | 82.5713 | -2.3208 | 84.415 | 80.64 | 0.0372 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 689.45 |  | 692.8085 | -0.4848 | 698.65 | 693.24 | 0.0058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.55 |  | 66.502 | -1.4315 | 68.245 | 66.7 | 0.0153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.33 |  | 208.5211 | -0.5712 | 210.85 | 208.49 | 0.1688 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.885 |  | 382.4929 | -0.4204 | 391.71 | 387.245 | 0.21 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.625 |  | 320.944 | -0.0994 | 323.25 | 320.82 | 0.0062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.28 |  | 319.5166 | -0.387 | 324.42 | 320.24 | 0.0346 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 534.8 |  | 539.982 | -0.9597 | 556.12 | 542.33 | 0.3254 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 414.46 |  | 416.3738 | -0.4596 | 420.72 | 412.69 | 0.6321 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.44 |  | 550.6708 | -0.9499 | 557.38 | 545.965 | 0.066 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.9 |  | 580.5436 | -0.7999 | 585.98 | 576.635 | 0.0469 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 390.04 |  | 392.0079 | -0.502 | 397.34 | 390.54 | 1.5357 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 980.15 |  | 991.1433 | -1.1092 | 999.04 | 964.86 | 1.0713 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.16 |  | 209.2855 | -1.4934 | 213.785 | 207.665 | 0.1116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 435.62 |  | 443.2715 | -1.7261 | 450.07 | 438.55 | 1.5885 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.495 |  | 48.2501 | -1.5651 | 48.88 | 47.635 | 0.0211 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.985 |  | 31.5798 | -1.8834 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 736.68 |  | 738.4886 | -0.2449 | 742.515 | 738.54 | 0.0081 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.275 |  | 291.6104 | -0.115 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.86 |  | 121.6664 | -1.4848 | 124.22 | 122.07 | 0.0334 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.655 |  | 82.5713 | -2.3208 | 84.415 | 80.64 | 0.0372 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 302.01 |  | 305.8316 | -1.2496 | 311.13 | 303.96 | 0.1192 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 413.67 |  | 413.3334 | 0.0814 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 648.17 |  | 651.605 | -0.5272 | 656.38 | 642.37 | 1.5181 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1033.23 |  | 1016.4548 | 1.6504 | 1023.33 | 979.08 | 0.1791 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 478.17 |  | 476.8757 | 0.2714 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.27 |  | 143.8086 | -0.3745 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.3 |  | 176.6403 | -0.7588 | 177.84 | 173.19 | 3.1375 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.36 |  | 317.3865 | -1.8988 | 320.13 | 307.04 | 4.5189 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 829.02 |  | 855.0969 | -3.0496 | 880.26 | 833 | 2.9227 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.03 |  | 407.8956 | -0.9477 | 408.58 | 397.9 | 3.9007 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.27 |  | 114.4056 | -2.7408 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.64 |  | 326.7759 | -2.1837 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1792.7 |  | 1801.6667 | -0.4977 | 1806.11 | 1780.9 | 0.0407 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 557.28 |  | 564.1515 | -1.218 | 566.18 | 548.47 | 3.4973 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.65 |  | 320.2841 | -0.8224 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.78 |  | 215.4618 | 0.1477 | 217.88 | 212.99 | 0.139 | watch_only | none |
| TER | semiconductor_test_packaging | 368.555 |  | 371.8859 | -0.8957 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.01 |  | 293.7366 | -1.6091 | 301.305 | 293.685 | 0.3114 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMKR | semiconductor_test_packaging | 64.88 |  | 65.1872 | -0.4712 | 67.455 | 65.81 | 0.0771 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.21 |  | 134.9669 | -0.5608 | 137.81 | 135.66 | 0.3055 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MKSI | semiconductor_materials | 339.94 |  | 342.6457 | -0.7897 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 506.025 |  | 507.1954 | -0.2308 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.89 |  | 295.6885 | 0.0681 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.69 |  | 30.0499 | -1.1976 | 31.13 | 29.12 | 0.0674 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.41 |  | 41.5546 | -2.7545 | 43.21 | 40.51 | 0.0495 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.94 |  | 24.07 | -0.5401 | 24.46 | 23.265 | 0.0835 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1612.28 |  | 1642.3911 | -1.8334 | 1651.355 | 1560 | 3.5577 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 558.01 |  | 564.1168 | -1.0825 | 576.24 | 556.3 | 3.758 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 916.78 |  | 923.697 | -0.7488 | 933.5 | 908.955 | 1.5456 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.64 |  | 234.3025 | -0.2828 | 238.285 | 235.71 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.64 |  | 604.6185 | 0.169 | 614.15 | 605.39 | 0.0182 | watch_only | none |
| ARM | ai_accelerator | 279.04 |  | 279.5651 | -0.1878 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 167.56 |  | 173.1856 | -3.2483 | 177.88 | 168.18 | 4.3984 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
