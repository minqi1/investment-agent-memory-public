# Intraday State

- Generated at: `2026-07-23T02:33:50+08:00`
- Market time ET: `2026-07-22T14:33:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 25, 'manual_confirm_candidate': 6, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.54 |  | 707.472 | -0.1317 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 556.975 |  | 553.4778 | 0.6319 | 551.02 | 540.105 | 0.0485 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.105 |  | 586.0349 | 0.5239 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.08 |  | 748.5182 | -0.0585 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.5 |  | 211.4784 | 0.956 | 207.4 | 205.01 | 0.0562 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 556.975 |  | 553.4778 | 0.6319 | 551.02 | 540.105 | 0.0485 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.105 |  | 586.0349 | 0.5239 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1801.8 |  | 1798.9453 | 0.1587 | 1786.525 | 1767.54 | 0.106 | buy_precheck_manual_confirm | none |
| 5 | LRCX | semiconductor_equipment | 320.915 |  | 319.4321 | 0.4642 | 317.72 | 311.31 | 0.0997 | buy_precheck_manual_confirm | none |
| 6 | PWR | data_center_power_cooling | 643.51 |  | 641.2962 | 0.3452 | 641.19 | 628.17 | 0.2595 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1801.8 |  | 1798.9453 | 0.1587 | 1786.525 | 1767.54 | 0.106 | buy_precheck_manual_confirm | none |
| 2 | PWR | data_center_power_cooling | 643.51 |  | 641.2962 | 0.3452 | 641.19 | 628.17 | 0.2595 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 556.975 |  | 553.4778 | 0.6319 | 551.02 | 540.105 | 0.0485 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.105 |  | 586.0349 | 0.5239 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 5 | LRCX | semiconductor_equipment | 320.915 |  | 319.4321 | 0.4642 | 317.72 | 311.31 | 0.0997 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 474.32 |  | 473.8262 | 0.1042 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | NVDA | ai_accelerator | 213.5 |  | 211.4784 | 0.956 | 207.4 | 205.01 | 0.0562 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 143.08 |  | 142.9587 | 0.0849 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ONTO | semiconductor_test_packaging | 295.41 |  | 295.369 | 0.0139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | APD | industrial_gases | 298.3 |  | 297.8402 | 0.1544 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | AMAT | semiconductor_equipment | 560.09 |  | 558.7389 | 0.2418 | 559.22 | 544.305 | 0.3678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TSM | foundry | 421.58 |  | 420.8966 | 0.1624 | 419.42 | 414.87 | 0.4602 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ANET | ai_networking_optical | 174.98 |  | 174.9299 | 0.0287 | 175.265 | 171.06 | 2.8403 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | MKSI | semiconductor_materials | 347.405 |  | 344.6955 | 0.7861 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AMD | ai_accelerator | 553.535 |  | 551.8139 | 0.3119 | 548.755 | 526.6 | 1.8915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SNDK | memory_hbm_storage | 1584.645 |  | 1581.2458 | 0.215 | 1558.88 | 1518.99 | 4.2912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 212.13 |  | 211.4418 | 0.3255 | 207.06 | 202.18 | 0.4431 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | VRT | data_center_power_cooling | 301.69 |  | 299.3859 | 0.7696 | 297.69 | 293.905 | 2.6484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | QQQ | market_regime | 706.54 |  | 707.472 | -0.1317 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 20 | SPY | market_regime | 748.08 |  | 748.5182 | -0.0585 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.5 |  | 211.4784 | 0.956 | 207.4 | 205.01 | 0.0562 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 556.975 |  | 553.4778 | 0.6319 | 551.02 | 540.105 | 0.0485 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.105 |  | 586.0349 | 0.5239 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1801.8 |  | 1798.9453 | 0.1587 | 1786.525 | 1767.54 | 0.106 | buy_precheck_manual_confirm | none |
| 5 | LRCX | semiconductor_equipment | 320.915 |  | 319.4321 | 0.4642 | 317.72 | 311.31 | 0.0997 | buy_precheck_manual_confirm | none |
| 6 | PWR | data_center_power_cooling | 643.51 |  | 641.2962 | 0.3452 | 641.19 | 628.17 | 0.2595 | buy_precheck_manual_confirm | none |
| 7 | MU | memory_hbm_storage | 965.835 |  | 968.5084 | -0.276 | 963.41 | 936.99 | 2.0707 | below_vwap | below_vwap,spread_too_wide |
| 8 | WDC | memory_hbm_storage | 554.62 |  | 556.1757 | -0.2797 | 548.14 | 526.22 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | STX | memory_hbm_storage | 903.87 |  | 909.5867 | -0.6285 | 899.59 | 860.605 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | QQQ | market_regime | 706.54 |  | 707.472 | -0.1317 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 748.08 |  | 748.5182 | -0.0585 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 12 | TER | semiconductor_test_packaging | 370.95 |  | 371.6669 | -0.1929 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 216.01 |  | 216.1327 | -0.0568 | 215.465 | 210.975 | 0.0463 | below_vwap | below_vwap |
| 14 | DELL | ai_server_oem | 439.83 |  | 442.4171 | -0.5848 | 435.98 | 415.79 | 2.4191 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMKR | semiconductor_test_packaging | 67.19 |  | 67.4731 | -0.4196 | 66.73 | 64.98 | 2.5599 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMCI | ai_server_oem | 30.78 |  | 31.1619 | -1.2254 | 30.66 | 28.52 | 0.065 | below_vwap | below_vwap |
| 17 | TSM | foundry | 421.58 |  | 420.8966 | 0.1624 | 419.42 | 414.87 | 0.4602 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 553.535 |  | 551.8139 | 0.3119 | 548.755 | 526.6 | 1.8915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 474.32 |  | 473.8262 | 0.1042 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SNDK | memory_hbm_storage | 1584.645 |  | 1581.2458 | 0.215 | 1558.88 | 1518.99 | 4.2912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.54 |  | 707.472 | -0.1317 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.61 |  | 70.8613 | -0.3547 | 70.43 | 69.81 | 0.0142 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.5 |  | 211.4784 | 0.956 | 207.4 | 205.01 | 0.0562 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.205 |  | 389.9004 | -0.4348 | 400.89 | 392.26 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.975 |  | 325.0022 | -0.3161 | 328.865 | 325.74 | 0.0309 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.275 |  | 347.8557 | -0.4544 | 348.76 | 346.23 | 0.026 | below_vwap | below_vwap |
| AMD | ai_accelerator | 553.535 |  | 551.8139 | 0.3119 | 548.755 | 526.6 | 1.8915 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.58 |  | 420.8966 | 0.1624 | 419.42 | 414.87 | 0.4602 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 556.975 |  | 553.4778 | 0.6319 | 551.02 | 540.105 | 0.0485 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.105 |  | 586.0349 | 0.5239 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.35 |  | 391.6726 | 1.1942 | 387.635 | 380.205 | 0.4239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 965.835 |  | 968.5084 | -0.276 | 963.41 | 936.99 | 2.0707 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 212.13 |  | 211.4418 | 0.3255 | 207.06 | 202.18 | 0.4431 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 439.83 |  | 442.4171 | -0.5848 | 435.98 | 415.79 | 2.4191 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.35 |  | 48.9869 | -1.3002 | 48.96 | 47.01 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.78 |  | 31.1619 | -1.2254 | 30.66 | 28.52 | 0.065 | below_vwap | below_vwap |
| SPY | market_regime | 748.08 |  | 748.5182 | -0.0585 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 294.02 |  | 295.0132 | -0.3367 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.83 |  | 126.5664 | -1.372 | 128.79 | 125.83 | 3.0922 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.34 |  | 83.4057 | -1.2778 | 83.22 | 79.6 | 0.1336 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 301.69 |  | 299.3859 | 0.7696 | 297.69 | 293.905 | 2.6484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.66 |  | 407.8721 | -0.052 | 409.095 | 398.16 | 0.0908 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 643.51 |  | 641.2962 | 0.3452 | 641.19 | 628.17 | 0.2595 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 996.765 |  | 1005.1831 | -0.8375 | 1036.605 | 998.94 | 3.5114 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.32 |  | 473.8262 | 0.1042 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.08 |  | 142.9587 | 0.0849 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.98 |  | 174.9299 | 0.0287 | 175.265 | 171.06 | 2.8403 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.45 |  | 316.0426 | -0.5039 | 317.93 | 306.89 | 0.8364 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 824.36 |  | 838.6105 | -1.6993 | 840.47 | 814.62 | 4.4665 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 401.83 |  | 405.3802 | -0.8758 | 407.12 | 397.835 | 0.3335 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 110.33 |  | 114.1813 | -3.373 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.46 |  | 329.8029 | 0.5025 | 322.67 | 307.545 | 4.7577 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1801.8 |  | 1798.9453 | 0.1587 | 1786.525 | 1767.54 | 0.106 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.09 |  | 558.7389 | 0.2418 | 559.22 | 544.305 | 0.3678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.915 |  | 319.4321 | 0.4642 | 317.72 | 311.31 | 0.0997 | buy_precheck_manual_confirm | none |
| KLAC | semiconductor_equipment | 216.01 |  | 216.1327 | -0.0568 | 215.465 | 210.975 | 0.0463 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 370.95 |  | 371.6669 | -0.1929 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.41 |  | 295.369 | 0.0139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.19 |  | 67.4731 | -0.4196 | 66.73 | 64.98 | 2.5599 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.5 |  | 55.6653 | -0.297 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.63 |  | 138.8725 | -0.1746 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 347.405 |  | 344.6955 | 0.7861 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.11 |  | 507.3339 | 0.5472 | 507.545 | 505.59 | 0.0725 | price_stale_or_missing | price_stale_or_missing,stale_or_missing |
| APD | industrial_gases | 298.3 |  | 297.8402 | 0.1544 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.965 |  | 30.7152 | -2.4425 | 30.78 | 29.46 | 0.0334 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.32 |  | 42.5373 | -2.8618 | 42.29 | 40.305 | 0.0484 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.55 |  | 24.0107 | -1.9189 | 24.255 | 23.58 | 0.0425 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1584.645 |  | 1581.2458 | 0.215 | 1558.88 | 1518.99 | 4.2912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 554.62 |  | 556.1757 | -0.2797 | 548.14 | 526.22 |  | below_vwap | below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 903.87 |  | 909.5867 | -0.6285 | 899.59 | 860.605 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 243.01 |  | 244.2274 | -0.4985 | 248.43 | 244.47 | 0.0082 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.13 |  | 630.6154 | -0.7113 | 647.02 | 632.77 | 0.1453 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.49 |  | 285.5936 | -0.3864 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.085 |  | 166.7401 | -0.3929 | 166.63 | 162.08 | 1.439 | below_vwap | below_vwap,spread_too_wide |
