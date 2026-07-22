# Intraday State

- Generated at: `2026-07-23T03:22:51+08:00`
- Market time ET: `2026-07-22T15:22:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 20, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 16, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.91 |  | 707.4413 | -0.0751 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.39 |  | 554.1589 | 0.7635 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.95 |  | 586.6307 | 0.5658 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.89 |  | 748.4884 | -0.0799 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.32 |  | 211.679 | 0.7752 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 969.845 |  | 968.4581 | 0.1432 | 963.41 | 936.99 | 0.2 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.39 |  | 554.1589 | 0.7635 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.95 |  | 586.6307 | 0.5658 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.125 |  | 211.5392 | 0.2769 | 207.06 | 202.18 | 0.2499 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.61 |  | 1799.2371 | 0.243 | 1786.525 | 1767.54 | 0.0959 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.485 |  | 216.1694 | 0.146 | 215.465 | 210.975 | 0.0601 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 559.98 |  | 558.8646 | 0.1996 | 559.22 | 544.305 | 0.2911 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.42 |  | 174.9673 | 0.2587 | 175.265 | 171.06 | 0.1197 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 175.42 |  | 174.9673 | 0.2587 | 175.265 | 171.06 | 0.1197 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 216.485 |  | 216.1694 | 0.146 | 215.465 | 210.975 | 0.0601 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 559.98 |  | 558.8646 | 0.1996 | 559.22 | 544.305 | 0.2911 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 969.845 |  | 968.4581 | 0.1432 | 963.41 | 936.99 | 0.2 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1803.61 |  | 1799.2371 | 0.243 | 1786.525 | 1767.54 | 0.0959 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 244.48 |  | 244.2124 | 0.1096 | 248.43 | 244.47 | 0.0245 | watch_only | none |
| 7 | SOXX | semiconductor_index | 558.39 |  | 554.1589 | 0.7635 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| 8 | SMH | semiconductor_index | 589.95 |  | 586.6307 | 0.5658 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 212.125 |  | 211.5392 | 0.2769 | 207.06 | 202.18 | 0.2499 | buy_precheck_manual_confirm | none |
| 10 | NVDA | ai_accelerator | 213.32 |  | 211.679 | 0.7752 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 11 | LIN | industrial_gases | 508.8 |  | 507.4766 | 0.2608 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ENTG | semiconductor_materials | 139.14 |  | 138.9001 | 0.1727 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TER | semiconductor_test_packaging | 372.24 |  | 371.6612 | 0.1557 | 369.53 | 365 | 5.0451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | MKSI | semiconductor_materials | 347.66 |  | 345.5443 | 0.6123 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | STX | memory_hbm_storage | 910.64 |  | 909.4185 | 0.1343 | 899.59 | 860.605 | 1.2288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | PWR | data_center_power_cooling | 643.99 |  | 641.7043 | 0.3562 | 641.19 | 628.17 | 3.6383 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TSM | foundry | 422.9 |  | 421.0926 | 0.4292 | 419.42 | 414.87 | 0.9695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 556.125 |  | 552.6619 | 0.6266 | 548.755 | 526.6 | 0.4172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | DELL | ai_server_oem | 442.91 |  | 442.3851 | 0.1187 | 435.98 | 415.79 | 0.7202 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.32 |  | 211.679 | 0.7752 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 969.845 |  | 968.4581 | 0.1432 | 963.41 | 936.99 | 0.2 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.39 |  | 554.1589 | 0.7635 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.95 |  | 586.6307 | 0.5658 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.125 |  | 211.5392 | 0.2769 | 207.06 | 202.18 | 0.2499 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.61 |  | 1799.2371 | 0.243 | 1786.525 | 1767.54 | 0.0959 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.485 |  | 216.1694 | 0.146 | 215.465 | 210.975 | 0.0601 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 559.98 |  | 558.8646 | 0.1996 | 559.22 | 544.305 | 0.2911 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.42 |  | 174.9673 | 0.2587 | 175.265 | 171.06 | 0.1197 | buy_precheck_manual_confirm | none |
| 10 | QQQ | market_regime | 706.91 |  | 707.4413 | -0.0751 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 747.89 |  | 748.4884 | -0.0799 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 12 | AMKR | semiconductor_test_packaging | 67.465 |  | 67.4653 | -0.0005 | 66.73 | 64.98 | 2.2827 | below_vwap | below_vwap,spread_too_wide |
| 13 | SMCI | ai_server_oem | 30.69 |  | 31.1432 | -1.4552 | 30.66 | 28.52 | 0.0326 | below_vwap | below_vwap |
| 14 | TSM | foundry | 422.9 |  | 421.0926 | 0.4292 | 419.42 | 414.87 | 0.9695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 556.125 |  | 552.6619 | 0.6266 | 548.755 | 526.6 | 0.4172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SNDK | memory_hbm_storage | 1609.98 |  | 1582.8178 | 1.7161 | 1558.88 | 1518.99 | 3.3143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | WDC | memory_hbm_storage | 558.335 |  | 556.2753 | 0.3703 | 548.14 | 526.22 | 1.7015 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 910.64 |  | 909.4185 | 0.1343 | 899.59 | 860.605 | 1.2288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 372.24 |  | 371.6612 | 0.1557 | 369.53 | 365 | 5.0451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 397.395 |  | 392.1232 | 1.3444 | 387.635 | 380.205 | 0.5763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.91 |  | 707.4413 | -0.0751 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.77 |  | 70.8568 | -0.1225 | 70.43 | 69.81 | 0.0283 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.32 |  | 211.679 | 0.7752 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.4 |  | 389.7212 | -0.0824 | 400.89 | 392.26 | 0.0128 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.38 |  | 324.9444 | -0.1737 | 328.865 | 325.74 | 0.3761 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 345.48 |  | 347.5317 | -0.5904 | 348.76 | 346.23 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 556.125 |  | 552.6619 | 0.6266 | 548.755 | 526.6 | 0.4172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.9 |  | 421.0926 | 0.4292 | 419.42 | 414.87 | 0.9695 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.39 |  | 554.1589 | 0.7635 | 551.02 | 540.105 | 0.0519 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.95 |  | 586.6307 | 0.5658 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.395 |  | 392.1232 | 1.3444 | 387.635 | 380.205 | 0.5763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 969.845 |  | 968.4581 | 0.1432 | 963.41 | 936.99 | 0.2 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 212.125 |  | 211.5392 | 0.2769 | 207.06 | 202.18 | 0.2499 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 442.91 |  | 442.3851 | 0.1187 | 435.98 | 415.79 | 0.7202 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.255 |  | 48.911 | -1.3412 | 48.96 | 47.01 | 0.0207 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.69 |  | 31.1432 | -1.4552 | 30.66 | 28.52 | 0.0326 | below_vwap | below_vwap |
| SPY | market_regime | 747.89 |  | 748.4884 | -0.0799 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.67 |  | 294.8843 | -0.4118 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.23 |  | 126.4567 | -0.1793 | 128.79 | 125.83 | 3.7392 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.16 |  | 83.3416 | -0.2179 | 83.22 | 79.6 | 0.5051 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.26 |  | 299.7835 | 1.1597 | 297.69 | 293.905 | 0.4518 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.635 |  | 407.6711 | -0.2542 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.99 |  | 641.7043 | 0.3562 | 641.19 | 628.17 | 3.6383 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 992.84 |  | 1003.9938 | -1.1109 | 1036.605 | 998.94 | 1.9137 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.49 |  | 473.86 | -0.0781 | 473.865 | 466.83 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.565 |  | 142.8949 | -0.2309 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.42 |  | 174.9673 | 0.2587 | 175.265 | 171.06 | 0.1197 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 315.27 |  | 316.0045 | -0.2324 | 317.93 | 306.89 | 0.295 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 830.91 |  | 837.8742 | -0.8312 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 400.81 |  | 404.9723 | -1.0278 | 407.12 | 397.835 | 1.6492 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.65 |  | 113.9155 | -2.8666 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.385 |  | 329.9543 | 0.4336 | 322.67 | 307.545 | 4.8011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1803.61 |  | 1799.2371 | 0.243 | 1786.525 | 1767.54 | 0.0959 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.98 |  | 558.8646 | 0.1996 | 559.22 | 544.305 | 0.2911 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.835 |  | 319.5856 | 0.3909 | 317.72 | 311.31 | 4.1049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.485 |  | 216.1694 | 0.146 | 215.465 | 210.975 | 0.0601 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 372.24 |  | 371.6612 | 0.1557 | 369.53 | 365 | 5.0451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.465 |  | 67.4653 | -0.0005 | 66.73 | 64.98 | 2.2827 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.31 |  | 55.597 | -0.5163 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.14 |  | 138.9001 | 0.1727 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.66 |  | 345.5443 | 0.6123 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.8 |  | 507.4766 | 0.2608 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.6 |  | 297.7807 | -0.3965 | 300.24 | 297.585 | 4.5111 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.01 |  | 30.6612 | -2.1239 | 30.78 | 29.46 | 0.0666 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.52 |  | 42.4294 | -2.1434 | 42.29 | 40.305 | 0.0241 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.56 |  | 23.9772 | -1.7402 | 24.255 | 23.58 | 0.0424 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1609.98 |  | 1582.8178 | 1.7161 | 1558.88 | 1518.99 | 3.3143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.335 |  | 556.2753 | 0.3703 | 548.14 | 526.22 | 1.7015 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 910.64 |  | 909.4185 | 0.1343 | 899.59 | 860.605 | 1.2288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 244.48 |  | 244.2124 | 0.1096 | 248.43 | 244.47 | 0.0245 | watch_only | none |
| META | cloud_ai_capex | 626.42 |  | 630.0878 | -0.5821 | 647.02 | 632.77 | 0.273 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.54 |  | 285.5777 | -0.0132 | 286.39 | 280.275 | 0.3257 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 166.21 |  | 166.7242 | -0.3084 | 166.63 | 162.08 | 0.4873 | below_vwap | below_vwap,spread_too_wide |
