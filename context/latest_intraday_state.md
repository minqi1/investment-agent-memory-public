# Intraday State

- Generated at: `2026-07-24T00:06:48+08:00`
- Market time ET: `2026-07-23T12:06:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 19, 'watch_only': 3, 'below_vwap': 28, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.46 |  | 693.1171 | -0.2391 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 548.84 |  | 551.0762 | -0.4058 | 557.38 | 545.965 | 0.0856 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.39 |  | 581.2748 | -0.4963 | 585.98 | 576.635 | 0.0709 | below_vwap | below_vwap |
| SPY | market_regime | 737.61 |  | 738.8224 | -0.1641 | 742.515 | 738.54 | 0.0583 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 208.93 |  | 208.2055 | 0.348 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 2 | SMCI | ai_server_oem | 31.455 |  | 31.4366 | 0.0587 | 31.52 | 30.23 | 0.0636 | watch_only | none |
| 3 | MU | memory_hbm_storage | 994.625 |  | 988.7638 | 0.5928 | 999.04 | 964.86 | 0.0694 | watch_only | none |
| 4 | TT | data_center_power_cooling | 477.675 |  | 476.6526 | 0.2145 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | DELL | ai_server_oem | 444.34 |  | 443.9611 | 0.0853 | 450.07 | 438.55 | 2.0007 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | STX | memory_hbm_storage | 925.13 |  | 923.6882 | 0.1561 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | WDC | memory_hbm_storage | 567.19 |  | 563.0247 | 0.7398 | 576.24 | 556.3 | 1.8054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SMH | semiconductor_index | 578.39 |  | 581.2748 | -0.4963 | 585.98 | 576.635 | 0.0709 | below_vwap | below_vwap |
| 9 | SOXX | semiconductor_index | 548.84 |  | 551.0762 | -0.4058 | 557.38 | 545.965 | 0.0856 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 291.2 |  | 291.7077 | -0.1741 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| 11 | LRCX | semiconductor_equipment | 319.09 |  | 321.3945 | -0.717 | 322.4 | 317.27 | 0.1128 | below_vwap | below_vwap |
| 12 | HPE | ai_server_oem | 48.02 |  | 48.3364 | -0.6547 | 48.88 | 47.635 | 0.1249 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 41.11 |  | 41.8938 | -1.8709 | 43.21 | 40.51 | 0.0486 | below_vwap | below_vwap |
| 15 | ASML | semiconductor_equipment | 1796.865 |  | 1803.9229 | -0.3913 | 1806.11 | 1780.9 | 0.1937 | below_vwap | below_vwap |
| 16 | ANET | ai_networking_optical | 175.27 |  | 176.6357 | -0.7732 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 143.79 |  | 143.9472 | -0.1092 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 646.66 |  | 652.9556 | -0.9642 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 412.96 |  | 413.216 | -0.0619 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ARM | ai_accelerator | 277.66 |  | 278.967 | -0.4685 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1659.65 |  | 1627.3188 | 1.9868 | 1651.355 | 1560 | 4.76 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | NVDA | ai_accelerator | 208.93 |  | 208.2055 | 0.348 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| 3 | MU | memory_hbm_storage | 994.625 |  | 988.7638 | 0.5928 | 999.04 | 964.86 | 0.0694 | watch_only | none |
| 4 | SMCI | ai_server_oem | 31.455 |  | 31.4366 | 0.0587 | 31.52 | 30.23 | 0.0636 | watch_only | none |
| 5 | TSM | foundry | 415.23 |  | 416.5434 | -0.3153 | 420.72 | 412.69 | 0.9609 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 578.39 |  | 581.2748 | -0.4963 | 585.98 | 576.635 | 0.0709 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 548.84 |  | 551.0762 | -0.4058 | 557.38 | 545.965 | 0.0856 | below_vwap | below_vwap |
| 8 | ASML | semiconductor_equipment | 1796.865 |  | 1803.9229 | -0.3913 | 1806.11 | 1780.9 | 0.1937 | below_vwap | below_vwap |
| 9 | AMAT | semiconductor_equipment | 563.15 |  | 566.3264 | -0.5609 | 566.18 | 548.47 | 0.4546 | below_vwap | below_vwap,spread_too_wide |
| 10 | ANET | ai_networking_optical | 175.27 |  | 176.6357 | -0.7732 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 143.79 |  | 143.9472 | -0.1092 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 646.66 |  | 652.9556 | -0.9642 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 214.295 |  | 215.7031 | -0.6528 | 217.88 | 212.99 | 2.1092 | below_vwap | below_vwap,spread_too_wide |
| 14 | ETN | data_center_power_cooling | 412.96 |  | 413.216 | -0.0619 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | GEV | data_center_power_cooling | 1009.29 |  | 1011.1887 | -0.1878 | 1023.33 | 979.08 | 2.1371 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.2 |  | 291.7077 | -0.1741 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 319.09 |  | 321.3945 | -0.717 | 322.4 | 317.27 | 0.1128 | below_vwap | below_vwap |
| 18 | ARM | ai_accelerator | 277.66 |  | 278.967 | -0.4685 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 506.88 |  | 507.7186 | -0.1652 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.46 |  | 693.1171 | -0.2391 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.085 |  | 66.5587 | -0.7116 | 68.245 | 66.7 | 0.0454 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.93 |  | 208.2055 | 0.348 | 210.85 | 208.49 | 0.0144 | watch_only | none |
| MSFT | cloud_ai_capex | 380.2 |  | 383.1314 | -0.7651 | 391.71 | 387.245 | 0.647 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.435 |  | 321.22 | -0.2444 | 323.25 | 320.82 | 0.0125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.415 |  | 319.4475 | -0.0102 | 324.42 | 320.24 | 0.1628 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 540.7 |  | 546.6362 | -1.0859 | 556.12 | 542.33 | 1.3372 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.23 |  | 416.5434 | -0.3153 | 420.72 | 412.69 | 0.9609 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 548.84 |  | 551.0762 | -0.4058 | 557.38 | 545.965 | 0.0856 | below_vwap | below_vwap |
| SMH | semiconductor_index | 578.39 |  | 581.2748 | -0.4963 | 585.98 | 576.635 | 0.0709 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 388.83 |  | 392.876 | -1.0298 | 397.34 | 390.54 | 1.3425 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 994.625 |  | 988.7638 | 0.5928 | 999.04 | 964.86 | 0.0694 | watch_only | none |
| MRVL | custom_silicon_networking | 207.255 |  | 210.0505 | -1.3309 | 213.785 | 207.665 | 2.2195 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 444.34 |  | 443.9611 | 0.0853 | 450.07 | 438.55 | 2.0007 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.02 |  | 48.3364 | -0.6547 | 48.88 | 47.635 | 0.1249 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.455 |  | 31.4366 | 0.0587 | 31.52 | 30.23 | 0.0636 | watch_only | none |
| SPY | market_regime | 737.61 |  | 738.8224 | -0.1641 | 742.515 | 738.54 | 0.0583 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.2 |  | 291.7077 | -0.1741 | 293.01 | 290.365 | 0.0137 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.61 |  | 122.3477 | -1.4203 | 124.22 | 122.07 | 0.2239 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.97 |  | 82.9675 | -1.2023 | 84.415 | 80.64 | 4.3919 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.41 |  | 306.5752 | -1.0324 | 311.13 | 303.96 | 0.1417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 412.96 |  | 413.216 | -0.0619 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 646.66 |  | 652.9556 | -0.9642 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1009.29 |  | 1011.1887 | -0.1878 | 1023.33 | 979.08 | 2.1371 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 477.675 |  | 476.6526 | 0.2145 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.79 |  | 143.9472 | -0.1092 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.27 |  | 176.6357 | -0.7732 | 177.84 | 173.19 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 314.85 |  | 318.5184 | -1.1517 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 834.725 |  | 859.7478 | -2.9105 | 880.26 | 833 | 1.4316 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 404.89 |  | 408.1202 | -0.7915 | 408.58 | 397.9 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 113.11 |  | 114.8314 | -1.4991 | 118.01 | 108.505 | 4.6592 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 326.795 |  | 327.7702 | -0.2975 | 341.68 | 327.43 | 4.5564 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1796.865 |  | 1803.9229 | -0.3913 | 1806.11 | 1780.9 | 0.1937 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 563.15 |  | 566.3264 | -0.5609 | 566.18 | 548.47 | 0.4546 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.09 |  | 321.3945 | -0.717 | 322.4 | 317.27 | 0.1128 | below_vwap | below_vwap |
| KLAC | semiconductor_equipment | 214.295 |  | 215.7031 | -0.6528 | 217.88 | 212.99 | 2.1092 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.71 |  | 371.5931 | -0.2377 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 292.83 |  | 295.7194 | -0.9771 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.49 |  | 65.329 | -1.2842 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.37 |  | 54.6094 | -0.4384 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.25 |  | 135.3898 | -0.8419 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.06 |  | 342.8981 | -0.536 | 347.92 | 341.755 | 4.014 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 506.88 |  | 507.7186 | -0.1652 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.175 |  | 296.4668 | -0.4357 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.71 |  | 30.0737 | -1.2094 | 31.13 | 29.12 | 0.0673 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.11 |  | 41.8938 | -1.8709 | 43.21 | 40.51 | 0.0486 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.95 |  | 24.0562 | -0.4415 | 24.46 | 23.265 | 0.167 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1659.65 |  | 1627.3188 | 1.9868 | 1651.355 | 1560 | 4.76 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 567.19 |  | 563.0247 | 0.7398 | 576.24 | 556.3 | 1.8054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 925.13 |  | 923.6882 | 0.1561 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 233.46 |  | 234.3282 | -0.3705 | 238.285 | 235.71 | 0.03 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 601.45 |  | 603.9157 | -0.4083 | 614.15 | 605.39 | 1.8239 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 277.66 |  | 278.967 | -0.4685 | 283 | 276.24 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 172.7 |  | 173.5644 | -0.498 | 177.88 | 168.18 | 0.6948 | below_vwap | below_vwap,spread_too_wide |
