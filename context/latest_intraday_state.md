# Intraday State

- Generated at: `2026-07-23T03:49:56+08:00`
- Market time ET: `2026-07-22T15:49:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 24, 'manual_confirm_candidate': 8, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 13, 'price_stale_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.67 |  | 707.3831 | -0.1008 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.62 |  | 554.6693 | 0.532 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.99 |  | 586.776 | 0.3773 | 581.9 | 572.01 | 0.017 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.885 |  | 748.4019 | -0.0691 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.49 |  | 211.7855 | 0.3327 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.66 |  | 421.219 | 0.3421 | 419.42 | 414.87 | 0.0497 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 557.62 |  | 554.6693 | 0.532 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 588.99 |  | 586.776 | 0.3773 | 581.9 | 572.01 | 0.017 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1808.21 |  | 1799.5458 | 0.4815 | 1786.525 | 1767.54 | 0.0509 | buy_precheck_manual_confirm | none |
| 6 | AMAT | semiconductor_equipment | 559.37 |  | 558.9712 | 0.0713 | 559.22 | 544.305 | 0.1019 | buy_precheck_manual_confirm | none |
| 7 | ANET | ai_networking_optical | 175.38 |  | 175.0374 | 0.1957 | 175.265 | 171.06 | 0.3421 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 303.3 |  | 300.0487 | 1.0836 | 297.69 | 293.905 | 0.1088 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 559.37 |  | 558.9712 | 0.0713 | 559.22 | 544.305 | 0.1019 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.66 |  | 421.219 | 0.3421 | 419.42 | 414.87 | 0.0497 | buy_precheck_manual_confirm | none |
| 3 | ANET | ai_networking_optical | 175.38 |  | 175.0374 | 0.1957 | 175.265 | 171.06 | 0.3421 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 212.49 |  | 211.7855 | 0.3327 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 5 | ETN | data_center_power_cooling | 407.995 |  | 407.6572 | 0.0829 | 409.095 | 398.16 | 0.1348 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 244.635 |  | 244.2645 | 0.1517 | 248.43 | 244.47 | 0.0736 | watch_only | none |
| 7 | SOXX | semiconductor_index | 557.62 |  | 554.6693 | 0.532 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 8 | SMH | semiconductor_index | 588.99 |  | 586.776 | 0.3773 | 581.9 | 572.01 | 0.017 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1808.21 |  | 1799.5458 | 0.4815 | 1786.525 | 1767.54 | 0.0509 | buy_precheck_manual_confirm | none |
| 10 | TT | data_center_power_cooling | 474.565 |  | 473.7934 | 0.1629 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 296.135 |  | 295.4338 | 0.2373 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | AMD | ai_accelerator | 554.65 |  | 553.6767 | 0.1758 | 548.755 | 526.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | VRT | data_center_power_cooling | 303.3 |  | 300.0487 | 1.0836 | 297.69 | 293.905 | 0.1088 | buy_precheck_manual_confirm | none |
| 14 | LIN | industrial_gases | 508.46 |  | 507.5959 | 0.1702 | 507.545 | 505.59 | 4.6631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | LRCX | semiconductor_equipment | 319.77 |  | 319.6309 | 0.0435 | 317.72 | 311.31 | 4.4626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 910.29 |  | 909.5855 | 0.0775 | 899.59 | 860.605 | 1.0162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 211.73 |  | 211.5893 | 0.0665 | 207.06 | 202.18 | 1.9648 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | PWR | data_center_power_cooling | 645.1 |  | 642.1662 | 0.4569 | 641.19 | 628.17 | 3.4584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AAPL | mega_cap_platform | 325.3 |  | 324.8702 | 0.1323 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low |
| 20 | MU | memory_hbm_storage | 972.665 |  | 969.0141 | 0.3768 | 963.41 | 936.99 | 0.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.49 |  | 211.7855 | 0.3327 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.66 |  | 421.219 | 0.3421 | 419.42 | 414.87 | 0.0497 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 557.62 |  | 554.6693 | 0.532 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 588.99 |  | 586.776 | 0.3773 | 581.9 | 572.01 | 0.017 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1808.21 |  | 1799.5458 | 0.4815 | 1786.525 | 1767.54 | 0.0509 | buy_precheck_manual_confirm | none |
| 6 | AMAT | semiconductor_equipment | 559.37 |  | 558.9712 | 0.0713 | 559.22 | 544.305 | 0.1019 | buy_precheck_manual_confirm | none |
| 7 | ANET | ai_networking_optical | 175.38 |  | 175.0374 | 0.1957 | 175.265 | 171.06 | 0.3421 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 303.3 |  | 300.0487 | 1.0836 | 297.69 | 293.905 | 0.1088 | buy_precheck_manual_confirm | none |
| 9 | QQQ | market_regime | 706.67 |  | 707.3831 | -0.1008 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 747.885 |  | 748.4019 | -0.0691 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 11 | TER | semiconductor_test_packaging | 371.2 |  | 371.6356 | -0.1172 | 369.53 | 365 | 1.8615 | below_vwap | below_vwap,spread_too_wide |
| 12 | SKHY | memory_hbm_storage | 166.68 |  | 166.7196 | -0.0238 | 166.63 | 162.08 | 0.276 | below_vwap | below_vwap |
| 13 | ALAB | ai_networking_optical | 328.9 |  | 329.9765 | -0.3262 | 322.67 | 307.545 | 4.9894 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMKR | semiconductor_test_packaging | 67.155 |  | 67.4298 | -0.4075 | 66.73 | 64.98 | 3.6185 | below_vwap | below_vwap,spread_too_wide |
| 15 | SMCI | ai_server_oem | 30.75 |  | 31.1164 | -1.1774 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| 16 | MU | memory_hbm_storage | 972.665 |  | 969.0141 | 0.3768 | 963.41 | 936.99 | 0.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 554.65 |  | 553.6767 | 0.1758 | 548.755 | 526.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TT | data_center_power_cooling | 474.565 |  | 473.7934 | 0.1629 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1600.725 |  | 1584.9807 | 0.9933 | 1558.88 | 1518.99 | 3.6309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 559.13 |  | 556.5484 | 0.4639 | 548.14 | 526.22 | 4.7091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.67 |  | 707.3831 | -0.1008 | 705.86 | 703.63 | 0.0042 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.68 |  | 70.8487 | -0.2382 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 212.49 |  | 211.7855 | 0.3327 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.82 |  | 389.6446 | -0.2116 | 400.89 | 392.26 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 325.3 |  | 324.8702 | 0.1323 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low |
| GOOGL | cloud_ai_capex | 344.66 |  | 347.1249 | -0.7101 | 348.76 | 346.23 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 554.65 |  | 553.6767 | 0.1758 | 548.755 | 526.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TSM | foundry | 422.66 |  | 421.219 | 0.3421 | 419.42 | 414.87 | 0.0497 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.62 |  | 554.6693 | 0.532 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.99 |  | 586.776 | 0.3773 | 581.9 | 572.01 | 0.017 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.15 |  | 392.7069 | 1.386 | 387.635 | 380.205 | 0.5526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 972.665 |  | 969.0141 | 0.3768 | 963.41 | 936.99 | 0.8153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 211.73 |  | 211.5893 | 0.0665 | 207.06 | 202.18 | 1.9648 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 444.03 |  | 442.5199 | 0.3413 | 435.98 | 415.79 | 2.3895 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.475 |  | 48.8778 | -0.8241 | 48.96 | 47.01 | 0.0206 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.75 |  | 31.1164 | -1.1774 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| SPY | market_regime | 747.885 |  | 748.4019 | -0.0691 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.62 |  | 294.7397 | -0.3799 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.05 |  | 126.4321 | -0.3022 | 128.79 | 125.83 | 2.1975 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.08 |  | 83.3298 | -0.2998 | 83.22 | 79.6 | 0.0963 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 303.3 |  | 300.0487 | 1.0836 | 297.69 | 293.905 | 0.1088 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.995 |  | 407.6572 | 0.0829 | 409.095 | 398.16 | 0.1348 | watch_only | none |
| PWR | data_center_power_cooling | 645.1 |  | 642.1662 | 0.4569 | 641.19 | 628.17 | 3.4584 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 991.335 |  | 1003.1064 | -1.1735 | 1036.605 | 998.94 | 1.1843 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.565 |  | 473.7934 | 0.1629 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.72 |  | 142.8346 | -0.0803 | 143.27 | 141.04 | 0.0911 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 175.38 |  | 175.0374 | 0.1957 | 175.265 | 171.06 | 0.3421 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 313.34 |  | 315.8084 | -0.7816 | 317.93 | 306.89 | 3.0989 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 820.41 |  | 836.0883 | -1.8752 | 840.47 | 814.62 | 1.9588 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 398.95 |  | 404.2863 | -1.3199 | 407.12 | 397.835 | 1.0352 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.58 |  | 113.752 | -2.7885 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 328.9 |  | 329.9765 | -0.3262 | 322.67 | 307.545 | 4.9894 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1808.21 |  | 1799.5458 | 0.4815 | 1786.525 | 1767.54 | 0.0509 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.37 |  | 558.9712 | 0.0713 | 559.22 | 544.305 | 0.1019 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 319.77 |  | 319.6309 | 0.0435 | 317.72 | 311.31 | 4.4626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 215.38 |  | 216.1132 | -0.3393 | 215.465 | 210.975 | 4.6244 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.2 |  | 371.6356 | -0.1172 | 369.53 | 365 | 1.8615 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 296.135 |  | 295.4338 | 0.2373 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.155 |  | 67.4298 | -0.4075 | 66.73 | 64.98 | 3.6185 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.07 |  | 55.5209 | -0.8122 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.54 |  | 138.8481 | -0.2219 | 140.09 | 135.555 | 0.1299 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 345.3 |  | 345.6107 | -0.0899 | 345.675 | 331.945 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 508.46 |  | 507.5959 | 0.1702 | 507.545 | 505.59 | 4.6631 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.605 |  | 297.6511 | -0.3515 | 300.24 | 297.585 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.12 |  | 30.6364 | -1.6857 | 30.78 | 29.46 | 0.1328 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.445 |  | 42.3696 | -2.1822 | 42.29 | 40.305 | 0.0241 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.635 |  | 23.9514 | -1.3212 | 24.255 | 23.58 | 0.0423 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1600.725 |  | 1584.9807 | 0.9933 | 1558.88 | 1518.99 | 3.6309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 559.13 |  | 556.5484 | 0.4639 | 548.14 | 526.22 | 4.7091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 910.29 |  | 909.5855 | 0.0775 | 899.59 | 860.605 | 1.0162 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 244.635 |  | 244.2645 | 0.1517 | 248.43 | 244.47 | 0.0736 | watch_only | none |
| META | cloud_ai_capex | 624.815 |  | 629.8046 | -0.7922 | 647.02 | 632.77 | 1.7989 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 284.91 |  | 285.5669 | -0.23 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.68 |  | 166.7196 | -0.0238 | 166.63 | 162.08 | 0.276 | below_vwap | below_vwap |
