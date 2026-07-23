# Intraday State

- Generated at: `2026-07-24T00:11:39+08:00`
- Market time ET: `2026-07-23T12:11:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 6, 'below_vwap': 30, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.565 |  | 693.0882 | -0.0755 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.28 |  | 550.9986 | -0.3119 | 557.38 | 545.965 | 0.0983 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.25 |  | 581.2618 | -0.3461 | 585.98 | 576.635 | 0.076 | below_vwap | below_vwap |
| SPY | market_regime | 738.585 |  | 738.812 | -0.0307 | 742.515 | 738.54 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 208.81 |  | 208.2274 | 0.2798 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 2 | MU | memory_hbm_storage | 990.57 |  | 988.7967 | 0.1793 | 999.04 | 964.86 | 0.0777 | watch_only | none |
| 3 | SMCI | ai_server_oem | 31.51 |  | 31.4364 | 0.2342 | 31.52 | 30.23 | 0.0635 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 321.31 |  | 321.2164 | 0.0291 | 323.25 | 320.82 | 0.0249 | watch_only | none |
| 5 | ETN | data_center_power_cooling | 413.67 |  | 413.217 | 0.1096 | 415.53 | 406.545 | 0.3263 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 320.59 |  | 319.4686 | 0.351 | 324.42 | 320.24 | 0.1934 | watch_only | none |
| 7 | TT | data_center_power_cooling | 477.675 |  | 476.6526 | 0.2145 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 144.135 |  | 143.9474 | 0.1303 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | WDC | memory_hbm_storage | 565.29 |  | 563.0962 | 0.3896 | 576.24 | 556.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TER | semiconductor_test_packaging | 371.9 |  | 371.5814 | 0.0857 | 376.78 | 363.37 | 4.9045 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | STX | memory_hbm_storage | 927.07 |  | 923.707 | 0.3641 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SMH | semiconductor_index | 579.25 |  | 581.2618 | -0.3461 | 585.98 | 576.635 | 0.076 | below_vwap | below_vwap |
| 13 | SOXX | semiconductor_index | 549.28 |  | 550.9986 | -0.3119 | 557.38 | 545.965 | 0.0983 | below_vwap | below_vwap |
| 14 | ASML | semiconductor_equipment | 1802.16 |  | 1803.8733 | -0.095 | 1806.11 | 1780.9 | 0.1104 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 291.57 |  | 291.7021 | -0.0453 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 16 | SPY | market_regime | 738.585 |  | 738.812 | -0.0307 | 742.515 | 738.54 | 0.0027 | below_vwap | below_vwap |
| 17 | HPE | ai_server_oem | 48.215 |  | 48.3307 | -0.2394 | 48.88 | 47.635 | 0.083 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | IREN | high_beta_ai_infrastructure | 41.33 |  | 41.8824 | -1.3188 | 43.21 | 40.51 | 0.0726 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 176.085 |  | 176.627 | -0.3069 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1661.02 |  | 1627.9967 | 2.0285 | 1651.355 | 1560 | 2.95 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | NVDA | ai_accelerator | 208.81 |  | 208.2274 | 0.2798 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 3 | MU | memory_hbm_storage | 990.57 |  | 988.7967 | 0.1793 | 999.04 | 964.86 | 0.0777 | watch_only | none |
| 4 | ETN | data_center_power_cooling | 413.67 |  | 413.217 | 0.1096 | 415.53 | 406.545 | 0.3263 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 320.59 |  | 319.4686 | 0.351 | 324.42 | 320.24 | 0.1934 | watch_only | none |
| 6 | SMCI | ai_server_oem | 31.51 |  | 31.4364 | 0.2342 | 31.52 | 30.23 | 0.0635 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 321.31 |  | 321.2164 | 0.0291 | 323.25 | 320.82 | 0.0249 | watch_only | none |
| 8 | TSM | foundry | 416.24 |  | 416.5272 | -0.069 | 420.72 | 412.69 | 2.1622 | below_vwap | below_vwap,spread_too_wide |
| 9 | SMH | semiconductor_index | 579.25 |  | 581.2618 | -0.3461 | 585.98 | 576.635 | 0.076 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 549.28 |  | 550.9986 | -0.3119 | 557.38 | 545.965 | 0.0983 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1802.16 |  | 1803.8733 | -0.095 | 1806.11 | 1780.9 | 0.1104 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 564.87 |  | 566.3042 | -0.2533 | 566.18 | 548.47 | 3.9213 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 176.085 |  | 176.627 | -0.3069 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 648.76 |  | 652.6805 | -0.6007 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 215.105 |  | 215.6869 | -0.2698 | 217.88 | 212.99 | 2.3756 | below_vwap | below_vwap,spread_too_wide |
| 16 | AMD | ai_accelerator | 542.42 |  | 546.5517 | -0.756 | 556.12 | 542.33 | 1.7072 | below_vwap | below_vwap,spread_too_wide |
| 17 | VRT | data_center_power_cooling | 304.79 |  | 306.5257 | -0.5662 | 311.13 | 303.96 | 1.9522 | below_vwap | below_vwap,spread_too_wide |
| 18 | GEV | data_center_power_cooling | 1009.29 |  | 1011.1887 | -0.1878 | 1023.33 | 979.08 | 3.5253 | below_vwap | below_vwap,spread_too_wide |
| 19 | IWM | market_regime | 291.57 |  | 291.7021 | -0.0453 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 20 | LRCX | semiconductor_equipment | 319.02 |  | 321.3799 | -0.7343 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.565 |  | 693.0882 | -0.0755 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.43 |  | 66.5518 | -0.183 | 68.245 | 66.7 | 0.0301 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.81 |  | 208.2274 | 0.2798 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| MSFT | cloud_ai_capex | 380.65 |  | 383.1055 | -0.641 | 391.71 | 387.245 | 0.754 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 321.31 |  | 321.2164 | 0.0291 | 323.25 | 320.82 | 0.0249 | watch_only | none |
| GOOGL | cloud_ai_capex | 320.59 |  | 319.4686 | 0.351 | 324.42 | 320.24 | 0.1934 | watch_only | none |
| AMD | ai_accelerator | 542.42 |  | 546.5517 | -0.756 | 556.12 | 542.33 | 1.7072 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 416.24 |  | 416.5272 | -0.069 | 420.72 | 412.69 | 2.1622 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.28 |  | 550.9986 | -0.3119 | 557.38 | 545.965 | 0.0983 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.25 |  | 581.2618 | -0.3461 | 585.98 | 576.635 | 0.076 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 389.49 |  | 392.845 | -0.854 | 397.34 | 390.54 | 1.3402 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 990.57 |  | 988.7967 | 0.1793 | 999.04 | 964.86 | 0.0777 | watch_only | none |
| MRVL | custom_silicon_networking | 208.175 |  | 210.0299 | -0.8831 | 213.785 | 207.665 | 0.759 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.09 |  | 443.9486 | -0.1934 | 450.07 | 438.55 | 1.7355 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.215 |  | 48.3307 | -0.2394 | 48.88 | 47.635 | 0.083 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.51 |  | 31.4364 | 0.2342 | 31.52 | 30.23 | 0.0635 | watch_only | none |
| SPY | market_regime | 738.585 |  | 738.812 | -0.0307 | 742.515 | 738.54 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 291.57 |  | 291.7021 | -0.0453 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.77 |  | 122.2996 | -1.2507 | 124.22 | 122.07 | 0.4223 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.315 |  | 82.9525 | -0.7685 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 304.79 |  | 306.5257 | -0.5662 | 311.13 | 303.96 | 1.9522 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.67 |  | 413.217 | 0.1096 | 415.53 | 406.545 | 0.3263 | watch_only | none |
| PWR | data_center_power_cooling | 648.76 |  | 652.6805 | -0.6007 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1009.29 |  | 1011.1887 | -0.1878 | 1023.33 | 979.08 | 3.5253 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 477.675 |  | 476.6526 | 0.2145 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.135 |  | 143.9474 | 0.1303 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.085 |  | 176.627 | -0.3069 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 315.39 |  | 318.4064 | -0.9474 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 839.99 |  | 859.5519 | -2.2758 | 880.26 | 833 | 4.4048 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 405.975 |  | 407.9673 | -0.4884 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 113.105 |  | 114.8176 | -1.4916 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 325.71 |  | 327.7606 | -0.6256 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1802.16 |  | 1803.8733 | -0.095 | 1806.11 | 1780.9 | 0.1104 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.87 |  | 566.3042 | -0.2533 | 566.18 | 548.47 | 3.9213 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.02 |  | 321.3799 | -0.7343 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.105 |  | 215.6869 | -0.2698 | 217.88 | 212.99 | 2.3756 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.9 |  | 371.5814 | 0.0857 | 376.78 | 363.37 | 4.9045 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 292.745 |  | 295.6971 | -0.9984 | 301.305 | 293.685 | 4.1982 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.485 |  | 65.3246 | -1.2853 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.3 |  | 135.3826 | -0.7997 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.2 |  | 342.8499 | -0.4812 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.09 |  | 507.7089 | -0.1219 | 510.71 | 502.72 | 4.6619 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.47 |  | 296.391 | -0.3107 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.88 |  | 30.0715 | -0.6367 | 31.13 | 29.12 | 0.5355 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.33 |  | 41.8824 | -1.3188 | 43.21 | 40.51 | 0.0726 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.92 |  | 24.0509 | -0.5442 | 24.46 | 23.265 | 0.0836 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1661.02 |  | 1627.9967 | 2.0285 | 1651.355 | 1560 | 2.95 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 565.29 |  | 563.0962 | 0.3896 | 576.24 | 556.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 927.07 |  | 923.707 | 0.3641 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234 |  | 234.3213 | -0.1371 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.96 |  | 603.8597 | -0.3146 | 614.15 | 605.39 | 0.4818 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 278.88 |  | 278.9414 | -0.022 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.67 |  | 173.5552 | -0.5101 | 177.88 | 168.18 | 0.7181 | below_vwap | below_vwap,spread_too_wide |
