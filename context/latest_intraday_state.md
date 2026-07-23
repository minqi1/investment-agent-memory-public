# Intraday State

- Generated at: `2026-07-24T02:27:39+08:00`
- Market time ET: `2026-07-23T14:27:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 18, 'below_vwap': 30, 'price_stale_or_missing': 2, 'watch_only': 2, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.045 |  | 692.9917 | -0.2809 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.05 |  | 550.875 | -0.6943 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.08 |  | 580.8975 | -0.6572 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| SPY | market_regime | 737.11 |  | 738.6468 | -0.2081 | 742.515 | 738.54 | 0.0095 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 992.45 |  | 991.6996 | 0.0757 | 999.04 | 964.86 | 0.0736 | watch_only | none |
| 2 | TT | data_center_power_cooling | 477.62 |  | 476.8025 | 0.1715 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | CORZ | high_beta_ai_infrastructure | 24.11 |  | 24.0703 | 0.1651 | 24.46 | 23.265 | 0.083 | watch_only | none |
| 4 | META | cloud_ai_capex | 605.51 |  | 604.4373 | 0.1775 | 614.15 | 605.39 | 0.7993 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GOOGL | cloud_ai_capex | 319.6 |  | 319.5612 | 0.0121 | 324.42 | 320.24 | 0.1033 | below_opening_15m_low | below_opening_15m_low |
| 6 | SMH | semiconductor_index | 577.08 |  | 580.8975 | -0.6572 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.05 |  | 550.875 | -0.6943 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| 8 | NVDA | ai_accelerator | 208.555 |  | 208.5862 | -0.015 | 210.85 | 208.49 | 0.0192 | below_vwap | below_vwap |
| 9 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 | 0.3178 | price_stale_or_missing | price_stale_or_missing,stale_or_missing |
| 10 | KLAC | semiconductor_equipment | 214.53 |  | 215.5469 | -0.4718 | 217.88 | 212.99 | 0.0559 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 291.14 |  | 291.6448 | -0.1731 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 12 | HPE | ai_server_oem | 47.715 |  | 48.3171 | -1.2462 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| 13 | SMCI | ai_server_oem | 30.995 |  | 31.6329 | -2.0167 | 31.52 | 30.23 | 0.0645 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | IREN | high_beta_ai_infrastructure | 40.81 |  | 41.6641 | -2.05 | 43.21 | 40.51 | 0.0735 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 143.72 |  | 143.9175 | -0.1372 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 650.135 |  | 651.765 | -0.2501 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 413.07 |  | 413.3415 | -0.0657 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 318.14 |  | 320.6211 | -0.7739 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 279.44 |  | 279.6631 | -0.0798 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1035 |  | 1014.6391 | 2.0067 | 1023.33 | 979.08 | 0.5217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | SNDK | memory_hbm_storage | 1664.85 |  | 1643.0165 | 1.3289 | 1651.355 | 1560 | 4.4448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | MU | memory_hbm_storage | 992.45 |  | 991.6996 | 0.0757 | 999.04 | 964.86 | 0.0736 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 24.11 |  | 24.0703 | 0.1651 | 24.46 | 23.265 | 0.083 | watch_only | none |
| 5 | TSM | foundry | 414.785 |  | 416.5692 | -0.4283 | 420.72 | 412.69 | 0.9644 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 577.08 |  | 580.8975 | -0.6572 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 547.05 |  | 550.875 | -0.6943 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| 8 | NVDA | ai_accelerator | 208.555 |  | 208.5862 | -0.015 | 210.85 | 208.49 | 0.0192 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1790.9 |  | 1802.9601 | -0.6689 | 1806.11 | 1780.9 | 0.7499 | below_vwap | below_vwap,spread_too_wide |
| 10 | AMAT | semiconductor_equipment | 557.865 |  | 565.2481 | -1.3062 | 566.18 | 548.47 | 0.3603 | below_vwap | below_vwap,spread_too_wide |
| 11 | ANET | ai_networking_optical | 175.97 |  | 176.7243 | -0.4268 | 177.84 | 173.19 | 1.0059 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.72 |  | 143.9175 | -0.1372 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 650.135 |  | 651.765 | -0.2501 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 214.53 |  | 215.5469 | -0.4718 | 217.88 | 212.99 | 0.0559 | below_vwap | below_vwap |
| 15 | ETN | data_center_power_cooling | 413.07 |  | 413.3415 | -0.0657 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | IWM | market_regime | 291.14 |  | 291.6448 | -0.1731 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 318.14 |  | 320.6211 | -0.7739 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ARM | ai_accelerator | 279.44 |  | 279.6631 | -0.0798 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 563.305 |  | 564.2694 | -0.1709 | 576.24 | 556.3 | 1.3687 | below_vwap | below_vwap,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.045 |  | 692.9917 | -0.2809 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.97 |  | 66.5423 | -0.8601 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.555 |  | 208.5862 | -0.015 | 210.85 | 208.49 | 0.0192 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 381.4 |  | 382.5757 | -0.3073 | 391.71 | 387.245 | 0.4012 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.07 |  | 321.0273 | -0.2982 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.6 |  | 319.5612 | 0.0121 | 324.42 | 320.24 | 0.1033 | below_opening_15m_low | below_opening_15m_low |
| AMD | ai_accelerator | 535.39 |  | 540.3926 | -0.9257 | 556.12 | 542.33 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 414.785 |  | 416.5692 | -0.4283 | 420.72 | 412.69 | 0.9644 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.05 |  | 550.875 | -0.6943 | 557.38 | 545.965 | 0.0658 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.08 |  | 580.8975 | -0.6572 | 585.98 | 576.635 | 0.0572 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.015 |  | 392.2303 | -0.5648 | 397.34 | 390.54 | 1.4102 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.45 |  | 991.6996 | 0.0757 | 999.04 | 964.86 | 0.0736 | watch_only | none |
| MRVL | custom_silicon_networking | 206.42 |  | 209.4911 | -1.466 | 213.785 | 207.665 | 0.1647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 437.77 |  | 443.6868 | -1.3335 | 450.07 | 438.55 | 0.297 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 47.715 |  | 48.3171 | -1.2462 | 48.88 | 47.635 | 0.0419 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.995 |  | 31.6329 | -2.0167 | 31.52 | 30.23 | 0.0645 | below_vwap | below_vwap |
| SPY | market_regime | 737.11 |  | 738.6468 | -0.2081 | 742.515 | 738.54 | 0.0095 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.14 |  | 291.6448 | -0.1731 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.59 |  | 121.8004 | -1.8148 | 124.22 | 122.07 | 0.5352 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 81.79 |  | 82.7627 | -1.1753 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.7 |  | 306.1143 | -1.1154 | 311.13 | 303.96 | 0.5649 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.07 |  | 413.3415 | -0.0657 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 650.135 |  | 651.765 | -0.2501 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1035 |  | 1014.6391 | 2.0067 | 1023.33 | 979.08 | 0.5217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.62 |  | 476.8025 | 0.1715 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.72 |  | 143.9175 | -0.1372 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.97 |  | 176.7243 | -0.4268 | 177.84 | 173.19 | 1.0059 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 313.265 |  | 317.7947 | -1.4254 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.7 |  | 856.8346 | -2.4666 | 880.26 | 833 | 0.4176 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 407.96 |  | 408.2384 | -0.0682 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 112.445 |  | 114.5426 | -1.8313 | 118.01 | 108.505 | 0.2846 | below_vwap | below_vwap |
| ALAB | ai_networking_optical | 323.05 |  | 327.6373 | -1.4001 | 341.68 | 327.43 | 4.2811 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1790.9 |  | 1802.9601 | -0.6689 | 1806.11 | 1780.9 | 0.7499 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 557.865 |  | 565.2481 | -1.3062 | 566.18 | 548.47 | 0.3603 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.14 |  | 320.6211 | -0.7739 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.53 |  | 215.5469 | -0.4718 | 217.88 | 212.99 | 0.0559 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 370.33 |  | 372.1517 | -0.4895 | 376.78 | 363.37 | 3.8236 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 289.465 |  | 294.0605 | -1.5628 | 301.305 | 293.685 | 0.5631 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.89 |  | 65.2161 | -0.5001 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.18 |  | 54.5255 | -0.6337 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.18 |  | 135.1242 | -0.6987 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 | 0.3178 | price_stale_or_missing | price_stale_or_missing,stale_or_missing |
| LIN | industrial_gases | 505.185 |  | 507.3391 | -0.4246 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.18 |  | 295.7262 | -0.1847 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.03 |  | 30.056 | -0.0865 | 31.13 | 29.12 | 0.0666 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.81 |  | 41.6641 | -2.05 | 43.21 | 40.51 | 0.0735 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.11 |  | 24.0703 | 0.1651 | 24.46 | 23.265 | 0.083 | watch_only | none |
| SNDK | memory_hbm_storage | 1664.85 |  | 1643.0165 | 1.3289 | 1651.355 | 1560 | 4.4448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 563.305 |  | 564.2694 | -0.1709 | 576.24 | 556.3 | 1.3687 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 920.195 |  | 924.2138 | -0.4348 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 233.675 |  | 234.3427 | -0.2849 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 605.51 |  | 604.4373 | 0.1775 | 614.15 | 605.39 | 0.7993 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.44 |  | 279.6631 | -0.0798 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.53 |  | 173.54 | -0.582 | 177.88 | 168.18 | 1.4258 | below_vwap | below_vwap,spread_too_wide |
