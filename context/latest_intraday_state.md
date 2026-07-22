# Intraday State

- Generated at: `2026-07-23T03:42:09+08:00`
- Market time ET: `2026-07-22T15:42:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 23, 'manual_confirm_candidate': 8, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 12, 'price_stale_or_missing': 1, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.28 |  | 707.4182 | -0.1609 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557 |  | 554.5813 | 0.4361 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.75 |  | 586.7319 | 0.3439 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.49 |  | 748.4392 | -0.1268 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.665 |  | 211.7655 | 0.4248 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 554.43 |  | 553.6309 | 0.1443 | 548.755 | 526.6 | 0.2796 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 911.32 |  | 909.5473 | 0.1949 | 899.59 | 860.605 | 0.1295 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557 |  | 554.5813 | 0.4361 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 588.75 |  | 586.7319 | 0.3439 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 398.16 |  | 392.4866 | 1.4455 | 387.635 | 380.205 | 0.0427 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1804.94 |  | 1799.413 | 0.3072 | 1786.525 | 1767.54 | 0.0521 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 303.05 |  | 299.9763 | 1.0247 | 297.69 | 293.905 | 0.0759 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | STX | memory_hbm_storage | 911.32 |  | 909.5473 | 0.1949 | 899.59 | 860.605 | 0.1295 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 588.75 |  | 586.7319 | 0.3439 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1804.94 |  | 1799.413 | 0.3072 | 1786.525 | 1767.54 | 0.0521 | buy_precheck_manual_confirm | none |
| 4 | AMD | ai_accelerator | 554.43 |  | 553.6309 | 0.1443 | 548.755 | 526.6 | 0.2796 | buy_precheck_manual_confirm | none |
| 5 | ETN | data_center_power_cooling | 407.78 |  | 407.6454 | 0.033 | 409.095 | 398.16 | 0.1054 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 244.71 |  | 244.2464 | 0.1898 | 248.43 | 244.47 | 0.0327 | watch_only | none |
| 7 | SOXX | semiconductor_index | 557 |  | 554.5813 | 0.4361 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 8 | NVDA | ai_accelerator | 212.665 |  | 211.7655 | 0.4248 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 9 | ENTG | semiconductor_materials | 138.88 |  | 138.8695 | 0.0075 | 140.09 | 135.555 | 0.252 | watch_only | none |
| 10 | TT | data_center_power_cooling | 474.27 |  | 473.7777 | 0.1039 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | LIN | industrial_gases | 508.94 |  | 507.5479 | 0.2743 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | MKSI | semiconductor_materials | 346.005 |  | 345.6102 | 0.1142 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 319.695 |  | 319.64 | 0.0172 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 296.31 |  | 295.4318 | 0.2973 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 398.16 |  | 392.4866 | 1.4455 | 387.635 | 380.205 | 0.0427 | buy_precheck_manual_confirm | none |
| 16 | VRT | data_center_power_cooling | 303.05 |  | 299.9763 | 1.0247 | 297.69 | 293.905 | 0.0759 | buy_precheck_manual_confirm | none |
| 17 | ANET | ai_networking_optical | 175.44 |  | 175.0045 | 0.2489 | 175.265 | 171.06 | 2.736 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TSM | foundry | 421.54 |  | 421.1934 | 0.0823 | 419.42 | 414.87 | 0.4484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 645.3 |  | 641.9372 | 0.5239 | 641.19 | 628.17 | 3.4372 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MU | memory_hbm_storage | 973.38 |  | 968.9149 | 0.4608 | 963.41 | 936.99 | 0.6678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.665 |  | 211.7655 | 0.4248 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 554.43 |  | 553.6309 | 0.1443 | 548.755 | 526.6 | 0.2796 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 911.32 |  | 909.5473 | 0.1949 | 899.59 | 860.605 | 0.1295 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557 |  | 554.5813 | 0.4361 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 588.75 |  | 586.7319 | 0.3439 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 398.16 |  | 392.4866 | 1.4455 | 387.635 | 380.205 | 0.0427 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1804.94 |  | 1799.413 | 0.3072 | 1786.525 | 1767.54 | 0.0521 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 303.05 |  | 299.9763 | 1.0247 | 297.69 | 293.905 | 0.0759 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 211.41 |  | 211.5889 | -0.0846 | 207.06 | 202.18 | 0.123 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 706.28 |  | 707.4182 | -0.1609 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| 11 | TER | semiconductor_test_packaging | 371.405 |  | 371.6539 | -0.067 | 369.53 | 365 | 0.3204 | below_vwap | below_vwap |
| 12 | KLAC | semiconductor_equipment | 215.575 |  | 216.1476 | -0.2649 | 215.465 | 210.975 | 0.0557 | below_vwap | below_vwap |
| 13 | ALAB | ai_networking_optical | 328.85 |  | 330.014 | -0.3527 | 322.67 | 307.545 | 0.1977 | below_vwap | below_vwap |
| 14 | AMKR | semiconductor_test_packaging | 67.15 |  | 67.447 | -0.4403 | 66.73 | 64.98 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | CRWV | gpu_cloud_ai_factory | 83.23 |  | 83.3311 | -0.1214 | 83.22 | 79.6 | 0.6128 | below_vwap | below_vwap,spread_too_wide |
| 16 | MU | memory_hbm_storage | 973.38 |  | 968.9149 | 0.4608 | 963.41 | 936.99 | 0.6678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TSM | foundry | 421.54 |  | 421.1934 | 0.0823 | 419.42 | 414.87 | 0.4484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 474.27 |  | 473.7777 | 0.1039 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1605.27 |  | 1584.6342 | 1.3022 | 1558.88 | 1518.99 | 3.5477 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 558.51 |  | 556.4437 | 0.3713 | 548.14 | 526.22 | 1.0295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.28 |  | 707.4182 | -0.1609 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.57 |  | 70.8516 | -0.3974 | 70.43 | 69.81 | 0.0142 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 212.665 |  | 211.7655 | 0.4248 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.41 |  | 389.6691 | -0.3231 | 400.89 | 392.26 | 0.018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.25 |  | 324.9211 | -0.2065 | 328.865 | 325.74 | 0.0062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 344.99 |  | 347.3168 | -0.6699 | 348.76 | 346.23 | 0.0174 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 554.43 |  | 553.6309 | 0.1443 | 548.755 | 526.6 | 0.2796 | buy_precheck_manual_confirm | none |
| TSM | foundry | 421.54 |  | 421.1934 | 0.0823 | 419.42 | 414.87 | 0.4484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557 |  | 554.5813 | 0.4361 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.75 |  | 586.7319 | 0.3439 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.16 |  | 392.4866 | 1.4455 | 387.635 | 380.205 | 0.0427 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 973.38 |  | 968.9149 | 0.4608 | 963.41 | 936.99 | 0.6678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 211.41 |  | 211.5889 | -0.0846 | 207.06 | 202.18 | 0.123 | below_vwap | below_vwap |
| DELL | ai_server_oem | 442.93 |  | 442.5017 | 0.0968 | 435.98 | 415.79 | 1.831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.36 |  | 48.8901 | -1.0843 | 48.96 | 47.01 | 0.0207 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.34 |  | 31.1254 | -2.5232 | 30.66 | 28.52 | 0.033 | below_vwap | below_vwap |
| SPY | market_regime | 747.49 |  | 748.4392 | -0.1268 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.465 |  | 294.7757 | -0.4446 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.76 |  | 126.4414 | -0.5389 | 128.79 | 125.83 | 2.2106 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.23 |  | 83.3311 | -0.1214 | 83.22 | 79.6 | 0.6128 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.05 |  | 299.9763 | 1.0247 | 297.69 | 293.905 | 0.0759 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.78 |  | 407.6454 | 0.033 | 409.095 | 398.16 | 0.1054 | watch_only | none |
| PWR | data_center_power_cooling | 645.3 |  | 641.9372 | 0.5239 | 641.19 | 628.17 | 3.4372 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 988.98 |  | 1003.5723 | -1.454 | 1036.605 | 998.94 | 0.3165 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 474.27 |  | 473.7777 | 0.1039 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.655 |  | 142.8426 | -0.1314 | 143.27 | 141.04 | 0.0561 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 175.44 |  | 175.0045 | 0.2489 | 175.265 | 171.06 | 2.736 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 313.395 |  | 315.8583 | -0.7799 | 317.93 | 306.89 | 3.3823 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 831.435 |  | 837.6357 | -0.7403 | 840.47 | 814.62 | 2.0314 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 400.45 |  | 404.5077 | -1.0031 | 407.12 | 397.835 | 0.1898 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.14 |  | 113.8095 | -2.3456 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 328.85 |  | 330.014 | -0.3527 | 322.67 | 307.545 | 0.1977 | below_vwap | below_vwap |
| ASML | semiconductor_equipment | 1804.94 |  | 1799.413 | 0.3072 | 1786.525 | 1767.54 | 0.0521 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 558.405 |  | 558.9811 | -0.1031 | 559.22 | 544.305 | 0.1074 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.695 |  | 319.64 | 0.0172 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.575 |  | 216.1476 | -0.2649 | 215.465 | 210.975 | 0.0557 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 371.405 |  | 371.6539 | -0.067 | 369.53 | 365 | 0.3204 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.31 |  | 295.4318 | 0.2973 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.15 |  | 67.447 | -0.4403 | 66.73 | 64.98 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.035 |  | 55.5498 | -0.9268 | 56.2 | 54.45 | 0.0727 | below_vwap | below_vwap |
| ENTG | semiconductor_materials | 138.88 |  | 138.8695 | 0.0075 | 140.09 | 135.555 | 0.252 | watch_only | none |
| MKSI | semiconductor_materials | 346.005 |  | 345.6102 | 0.1142 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.94 |  | 507.5479 | 0.2743 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.95 |  | 297.6912 | -0.249 | 300.24 | 297.585 | 4.7079 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.15 |  | 30.6437 | -1.6111 | 30.78 | 29.46 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.42 |  | 42.3898 | -2.2877 | 42.29 | 40.305 | 0.0241 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.59 |  | 23.9619 | -1.552 | 24.255 | 23.58 | 0.0848 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1605.27 |  | 1584.6342 | 1.3022 | 1558.88 | 1518.99 | 3.5477 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.51 |  | 556.4437 | 0.3713 | 548.14 | 526.22 | 1.0295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 911.32 |  | 909.5473 | 0.1949 | 899.59 | 860.605 | 0.1295 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 244.71 |  | 244.2464 | 0.1898 | 248.43 | 244.47 | 0.0327 | watch_only | none |
| META | cloud_ai_capex | 625.93 |  | 629.9514 | -0.6384 | 647.02 | 632.77 | 0.4889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.1 |  | 285.5752 | -0.1664 | 286.39 | 280.275 | 0.712 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.27 |  | 166.7163 | -0.2677 | 166.63 | 162.08 | 1.1968 | below_vwap | below_vwap,spread_too_wide |
