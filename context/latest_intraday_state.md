# Intraday State

- Generated at: `2026-07-23T00:28:43+08:00`
- Market time ET: `2026-07-22T12:28:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 8, 'watch_only': 1, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 1, 'below_vwap': 11}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.89 |  | 707.1227 | 0.2499 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.65 |  | 552.3712 | 1.1367 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.235 |  | 584.7469 | 0.9385 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.76 |  | 748.3297 | 0.1911 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.8 |  | 210.5845 | 1.527 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 423.03 |  | 420.4691 | 0.6091 | 419.42 | 414.87 | 0.1584 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.65 |  | 552.3712 | 1.1367 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.235 |  | 584.7469 | 0.9385 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.93 |  | 210.8549 | 0.9841 | 207.06 | 202.18 | 0.1597 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.89 |  | 707.1227 | 0.2499 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.76 |  | 748.3297 | 0.1911 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 394.65 |  | 388.8603 | 1.4889 | 387.635 | 380.205 | 0.0684 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1801.2 |  | 1795.9046 | 0.2949 | 1786.525 | 1767.54 | 0.1227 | buy_precheck_manual_confirm | none |
| 10 | LITE | ai_networking_optical | 844.24 |  | 841.2806 | 0.3518 | 840.47 | 814.62 | 0.2748 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.98 |  | 31.14 | 2.6974 | 30.66 | 28.52 | 0.0313 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.35 |  | 70.7987 | 0.7787 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.76 |  | 748.3297 | 0.1911 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.89 |  | 707.1227 | 0.2499 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1801.2 |  | 1795.9046 | 0.2949 | 1786.525 | 1767.54 | 0.1227 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 348.53 |  | 347.9224 | 0.1746 | 348.76 | 346.23 | 0.0344 | watch_only | none |
| 5 | LITE | ai_networking_optical | 844.24 |  | 841.2806 | 0.3518 | 840.47 | 814.62 | 0.2748 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 423.03 |  | 420.4691 | 0.6091 | 419.42 | 414.87 | 0.1584 | buy_precheck_manual_confirm | none |
| 7 | TT | data_center_power_cooling | 473.955 |  | 472.7078 | 0.2638 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SOXX | semiconductor_index | 558.65 |  | 552.3712 | 1.1367 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| 9 | SMH | semiconductor_index | 590.235 |  | 584.7469 | 0.9385 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| 10 | TER | semiconductor_test_packaging | 371.705 |  | 371.2796 | 0.1146 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 142.945 |  | 142.8618 | 0.0582 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 295.96 |  | 295.017 | 0.3197 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 394.65 |  | 388.8603 | 1.4889 | 387.635 | 380.205 | 0.0684 | buy_precheck_manual_confirm | none |
| 14 | MRVL | custom_silicon_networking | 212.93 |  | 210.8549 | 0.9841 | 207.06 | 202.18 | 0.1597 | buy_precheck_manual_confirm | none |
| 15 | AMAT | semiconductor_equipment | 558.9 |  | 558.3498 | 0.0985 | 559.22 | 544.305 | 0.4258 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LRCX | semiconductor_equipment | 319.5 |  | 318.6021 | 0.2818 | 317.72 | 311.31 | 3.0235 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | VRT | data_center_power_cooling | 299.67 |  | 298.7153 | 0.3196 | 297.69 | 293.905 | 0.9978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | COHR | ai_networking_optical | 317.05 |  | 316.2442 | 0.2548 | 317.93 | 306.89 | 2.0155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MKSI | semiconductor_materials | 344.78 |  | 343.4239 | 0.3949 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.8 |  | 210.5845 | 1.527 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 423.03 |  | 420.4691 | 0.6091 | 419.42 | 414.87 | 0.1584 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.65 |  | 552.3712 | 1.1367 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.235 |  | 584.7469 | 0.9385 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.93 |  | 210.8549 | 0.9841 | 207.06 | 202.18 | 0.1597 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.89 |  | 707.1227 | 0.2499 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 394.65 |  | 388.8603 | 1.4889 | 387.635 | 380.205 | 0.0684 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 749.76 |  | 748.3297 | 0.1911 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1801.2 |  | 1795.9046 | 0.2949 | 1786.525 | 1767.54 | 0.1227 | buy_precheck_manual_confirm | none |
| 10 | LITE | ai_networking_optical | 844.24 |  | 841.2806 | 0.3518 | 840.47 | 814.62 | 0.2748 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.98 |  | 31.14 | 2.6974 | 30.66 | 28.52 | 0.0313 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.35 |  | 70.7987 | 0.7787 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 13 | KLAC | semiconductor_equipment | 215.58 |  | 216.0896 | -0.2358 | 215.465 | 210.975 | 4.6711 | below_vwap | below_vwap,spread_too_wide |
| 14 | HPE | ai_server_oem | 49.015 |  | 49.0417 | -0.0544 | 48.96 | 47.01 | 0.0612 | below_vwap | below_vwap |
| 15 | MU | memory_hbm_storage | 974.57 |  | 966.3701 | 0.8485 | 963.41 | 936.99 | 0.513 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | IREN | high_beta_ai_infrastructure | 42.33 |  | 42.7543 | -0.9923 | 42.29 | 40.305 | 0.0472 | below_vwap | below_vwap |
| 17 | AMD | ai_accelerator | 555.92 |  | 550.7346 | 0.9415 | 548.755 | 526.6 | 2.423 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 473.955 |  | 472.7078 | 0.2638 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1612.64 |  | 1573.3945 | 2.4943 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 560.93 |  | 555.1042 | 1.0495 | 548.14 | 526.22 | 4.6851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.89 |  | 707.1227 | 0.2499 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.35 |  | 70.7987 | 0.7787 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.8 |  | 210.5845 | 1.527 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.86 |  | 390.6201 | -0.4506 | 400.89 | 392.26 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.85 |  | 325.5038 | -0.2009 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.53 |  | 347.9224 | 0.1746 | 348.76 | 346.23 | 0.0344 | watch_only | none |
| AMD | ai_accelerator | 555.92 |  | 550.7346 | 0.9415 | 548.755 | 526.6 | 2.423 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.03 |  | 420.4691 | 0.6091 | 419.42 | 414.87 | 0.1584 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.65 |  | 552.3712 | 1.1367 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.235 |  | 584.7469 | 0.9385 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 394.65 |  | 388.8603 | 1.4889 | 387.635 | 380.205 | 0.0684 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 974.57 |  | 966.3701 | 0.8485 | 963.41 | 936.99 | 0.513 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.93 |  | 210.8549 | 0.9841 | 207.06 | 202.18 | 0.1597 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 444.75 |  | 442.6114 | 0.4832 | 435.98 | 415.79 | 2.154 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 49.015 |  | 49.0417 | -0.0544 | 48.96 | 47.01 | 0.0612 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.98 |  | 31.14 | 2.6974 | 30.66 | 28.52 | 0.0313 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.76 |  | 748.3297 | 0.1911 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.68 |  | 295.2446 | -0.1912 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.75 |  | 126.7617 | -0.7981 | 128.79 | 125.83 | 0.159 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.73 |  | 83.4981 | 0.2778 | 83.22 | 79.6 | 1.5287 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.67 |  | 298.7153 | 0.3196 | 297.69 | 293.905 | 0.9978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.16 |  | 407.7127 | -0.1356 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 642.595 |  | 639.9338 | 0.4159 | 641.19 | 628.17 | 0.6427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 999.91 |  | 1009.0687 | -0.9076 | 1036.605 | 998.94 | 2.4172 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.955 |  | 472.7078 | 0.2638 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.945 |  | 142.8618 | 0.0582 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.02 |  | 174.7486 | 0.7276 | 175.265 | 171.06 | 3.8802 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 317.05 |  | 316.2442 | 0.2548 | 317.93 | 306.89 | 2.0155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 844.24 |  | 841.2806 | 0.3518 | 840.47 | 814.62 | 0.2748 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 406.17 |  | 406.1902 | -0.005 | 407.12 | 397.835 | 0.4973 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.92 |  | 114.7941 | -1.6326 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.48 |  | 328.2575 | 1.2864 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1801.2 |  | 1795.9046 | 0.2949 | 1786.525 | 1767.54 | 0.1227 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 558.9 |  | 558.3498 | 0.0985 | 559.22 | 544.305 | 0.4258 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 319.5 |  | 318.6021 | 0.2818 | 317.72 | 311.31 | 3.0235 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 215.58 |  | 216.0896 | -0.2358 | 215.465 | 210.975 | 4.6711 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.705 |  | 371.2796 | 0.1146 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.96 |  | 295.017 | 0.3197 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.54 |  | 67.4559 | 0.1247 | 66.73 | 64.98 | 1.984 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.75 |  | 138.7592 | -0.0066 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 344.78 |  | 343.4239 | 0.3949 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.99 |  | 507.0416 | 0.3843 | 507.545 | 505.59 | 4.56 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.39 |  | 297.7733 | -0.1287 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.68 |  | 30.8369 | -0.5087 | 30.78 | 29.46 | 0.0978 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.33 |  | 42.7543 | -0.9923 | 42.29 | 40.305 | 0.0472 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.89 |  | 24.1465 | -1.0622 | 24.255 | 23.58 | 0.0837 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1612.64 |  | 1573.3945 | 2.4943 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 560.93 |  | 555.1042 | 1.0495 | 548.14 | 526.22 | 4.6851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 915.205 |  | 907.2964 | 0.8717 | 899.59 | 860.605 | 0.6217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.93 |  | 244.5573 | -0.2565 | 248.43 | 244.47 | 0.2788 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 629.06 |  | 631.5835 | -0.3996 | 647.02 | 632.77 | 0.1955 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.93 |  | 285.636 | -0.2472 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 168.37 |  | 166.6681 | 1.0211 | 166.63 | 162.08 | 0.689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
