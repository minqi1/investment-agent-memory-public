# Intraday State

- Generated at: `2026-07-24T02:39:23+08:00`
- Market time ET: `2026-07-23T14:39:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 20, 'below_vwap': 29, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 1, 'watch_only': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.695 |  | 692.9524 | -0.3258 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.35 |  | 550.82 | -0.63 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.41 |  | 580.8602 | -0.594 | 585.98 | 576.635 | 0.0589 | below_vwap | below_vwap |
| SPY | market_regime | 736.88 |  | 738.6118 | -0.2345 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036 |  | 1015.0156 | 2.0674 | 1023.33 | 979.08 | 0.0917 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 477.91 |  | 476.827 | 0.2271 | 480 | 472.33 | 0.1904 | watch_only | none |
| 2 | ARM | ai_accelerator | 279.79 |  | 279.6618 | 0.0458 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | GEV | data_center_power_cooling | 1036 |  | 1015.0156 | 2.0674 | 1023.33 | 979.08 | 0.0917 | buy_precheck_manual_confirm | none |
| 4 | SNDK | memory_hbm_storage | 1654.67 |  | 1643.3328 | 0.6899 | 1651.355 | 1560 | 4.4722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SMH | semiconductor_index | 577.41 |  | 580.8602 | -0.594 | 585.98 | 576.635 | 0.0589 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 547.35 |  | 550.82 | -0.63 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1792.335 |  | 1802.6902 | -0.5744 | 1806.11 | 1780.9 | 0.0976 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 291.12 |  | 291.638 | -0.1776 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 9 | CRWV | gpu_cloud_ai_factory | 81.37 |  | 82.735 | -1.6499 | 84.415 | 80.64 | 0.086 | below_vwap | below_vwap |
| 10 | SMCI | ai_server_oem | 30.97 |  | 31.6122 | -2.0315 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | IREN | high_beta_ai_infrastructure | 40.69 |  | 41.6455 | -2.2944 | 43.21 | 40.51 | 0.0492 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 175.86 |  | 176.6861 | -0.4676 | 177.84 | 173.19 | 0.182 | below_vwap | below_vwap |
| 14 | WDC | memory_hbm_storage | 563.06 |  | 564.2545 | -0.2117 | 576.24 | 556.3 | 0.2753 | below_vwap | below_vwap |
| 15 | META | cloud_ai_capex | 605.24 |  | 604.4705 | 0.1273 | 614.15 | 605.39 | 0.4825 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | COHR | ai_networking_optical | 313.67 |  | 317.7308 | -1.2781 | 320.13 | 307.04 | 0.1626 | below_vwap | below_vwap |
| 17 | JCI | data_center_power_cooling | 143.55 |  | 143.9097 | -0.2499 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 649.12 |  | 651.7456 | -0.4028 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | KLAC | semiconductor_equipment | 214.61 |  | 215.5256 | -0.4248 | 217.88 | 212.99 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LRCX | semiconductor_equipment | 318.36 |  | 320.5329 | -0.6779 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1036 |  | 1015.0156 | 2.0674 | 1023.33 | 979.08 | 0.0917 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1654.67 |  | 1643.3328 | 0.6899 | 1651.355 | 1560 | 4.4722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TT | data_center_power_cooling | 477.91 |  | 476.827 | 0.2271 | 480 | 472.33 | 0.1904 | watch_only | none |
| 4 | TSM | foundry | 415.17 |  | 416.5099 | -0.3217 | 420.72 | 412.69 | 0.8117 | below_vwap | below_vwap,spread_too_wide |
| 5 | SMH | semiconductor_index | 577.41 |  | 580.8602 | -0.594 | 585.98 | 576.635 | 0.0589 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 547.35 |  | 550.82 | -0.63 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| 7 | MU | memory_hbm_storage | 991.675 |  | 991.722 | -0.0047 | 999.04 | 964.86 | 1.0084 | below_vwap | below_vwap,spread_too_wide |
| 8 | ASML | semiconductor_equipment | 1792.335 |  | 1802.6902 | -0.5744 | 1806.11 | 1780.9 | 0.0976 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 558.87 |  | 565.035 | -1.0911 | 566.18 | 548.47 | 3.21 | below_vwap | below_vwap,spread_too_wide |
| 10 | ANET | ai_networking_optical | 175.86 |  | 176.6861 | -0.4676 | 177.84 | 173.19 | 0.182 | below_vwap | below_vwap |
| 11 | JCI | data_center_power_cooling | 143.55 |  | 143.9097 | -0.2499 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 649.12 |  | 651.7456 | -0.4028 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 214.61 |  | 215.5256 | -0.4248 | 217.88 | 212.99 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ETN | data_center_power_cooling | 412.985 |  | 413.3339 | -0.0844 | 415.53 | 406.545 | 0.6877 | below_vwap | below_vwap,spread_too_wide |
| 15 | IWM | market_regime | 291.12 |  | 291.638 | -0.1776 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 318.36 |  | 320.5329 | -0.6779 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 563.06 |  | 564.2545 | -0.2117 | 576.24 | 556.3 | 0.2753 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 505.56 |  | 507.2824 | -0.3395 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHR | ai_networking_optical | 313.67 |  | 317.7308 | -1.2781 | 320.13 | 307.04 | 0.1626 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.695 |  | 692.9524 | -0.3258 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.96 |  | 66.5363 | -0.8661 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.12 |  | 208.5844 | -0.2227 | 210.85 | 208.49 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 381.355 |  | 382.554 | -0.3134 | 391.71 | 387.245 | 0.1311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.06 |  | 320.9872 | -0.2889 | 323.25 | 320.82 | 0.025 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 318.73 |  | 319.5562 | -0.2586 | 324.42 | 320.24 | 0.0565 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 537.745 |  | 540.2983 | -0.4726 | 556.12 | 542.33 | 3.9015 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.17 |  | 416.5099 | -0.3217 | 420.72 | 412.69 | 0.8117 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.35 |  | 550.82 | -0.63 | 557.38 | 545.965 | 0.0639 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.41 |  | 580.8602 | -0.594 | 585.98 | 576.635 | 0.0589 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.135 |  | 392.1786 | -0.5211 | 397.34 | 390.54 | 1.4277 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 991.675 |  | 991.722 | -0.0047 | 999.04 | 964.86 | 1.0084 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.59 |  | 209.4257 | -1.354 | 213.785 | 207.665 | 0.092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.14 |  | 443.5383 | -1.4426 | 450.07 | 438.55 | 1.7454 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.6 |  | 48.2989 | -1.4471 | 48.88 | 47.635 | 0.084 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 30.97 |  | 31.6122 | -2.0315 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 736.88 |  | 738.6118 | -0.2345 | 742.515 | 738.54 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.12 |  | 291.638 | -0.1776 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.79 |  | 121.7364 | -1.5988 | 124.22 | 122.07 | 0.2337 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.37 |  | 82.735 | -1.6499 | 84.415 | 80.64 | 0.086 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 302.34 |  | 306.0901 | -1.2252 | 311.13 | 303.96 | 0.6946 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.985 |  | 413.3339 | -0.0844 | 415.53 | 406.545 | 0.6877 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 649.12 |  | 651.7456 | -0.4028 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1036 |  | 1015.0156 | 2.0674 | 1023.33 | 979.08 | 0.0917 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 477.91 |  | 476.827 | 0.2271 | 480 | 472.33 | 0.1904 | watch_only | none |
| JCI | data_center_power_cooling | 143.55 |  | 143.9097 | -0.2499 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.86 |  | 176.6861 | -0.4676 | 177.84 | 173.19 | 0.182 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 313.67 |  | 317.7308 | -1.2781 | 320.13 | 307.04 | 0.1626 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 835.035 |  | 856.6455 | -2.5227 | 880.26 | 833 | 0.8287 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 406.735 |  | 408.1806 | -0.3542 | 408.58 | 397.9 | 4.6271 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.55 |  | 114.5218 | -1.7218 | 118.01 | 108.505 | 1.8836 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 322.1 |  | 327.5065 | -1.6508 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1792.335 |  | 1802.6902 | -0.5744 | 1806.11 | 1780.9 | 0.0976 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.87 |  | 565.035 | -1.0911 | 566.18 | 548.47 | 3.21 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.36 |  | 320.5329 | -0.6779 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.61 |  | 215.5256 | -0.4248 | 217.88 | 212.99 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 370.31 |  | 372.1144 | -0.4849 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 289.91 |  | 294.0119 | -1.3952 | 301.305 | 293.685 | 4.2772 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.89 |  | 65.2161 | -0.5001 | 67.455 | 65.81 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.23 |  | 54.4962 | -0.4885 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.28 |  | 135.0757 | -0.5891 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.89 |  | 342.8233 | -0.2722 | 347.92 | 341.755 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.56 |  | 507.2824 | -0.3395 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.23 |  | 295.6936 | -0.1568 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.965 |  | 30.0553 | -0.3005 | 31.13 | 29.12 | 0.0334 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.69 |  | 41.6455 | -2.2944 | 43.21 | 40.51 | 0.0492 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.07 |  | 24.0706 | -0.0024 | 24.46 | 23.265 | 0.0415 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1654.67 |  | 1643.3328 | 0.6899 | 1651.355 | 1560 | 4.4722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 563.06 |  | 564.2545 | -0.2117 | 576.24 | 556.3 | 0.2753 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 922.44 |  | 924.1383 | -0.1838 | 933.5 | 908.955 | 2.23 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.73 |  | 234.3344 | -0.2579 | 238.285 | 235.71 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.24 |  | 604.4705 | 0.1273 | 614.15 | 605.39 | 0.4825 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 279.79 |  | 279.6618 | 0.0458 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 171.07 |  | 173.5131 | -1.408 | 177.88 | 168.18 | 2.9228 | below_vwap | below_vwap,spread_too_wide |
