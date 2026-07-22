# Intraday State

- Generated at: `2026-07-23T03:26:42+08:00`
- Market time ET: `2026-07-22T15:26:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.12 |  | 707.4396 | -0.0452 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.635 |  | 554.2244 | 0.7958 | 551.02 | 540.105 | 0.0304 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.92 |  | 586.6485 | 0.5577 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.755 |  | 748.4828 | -0.0972 | 747.68 | 746.425 | 0.0067 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.3 |  | 211.7026 | 0.7545 | 207.4 | 205.01 | 0.3329 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 423.26 |  | 421.1362 | 0.5043 | 419.42 | 414.87 | 0.1299 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 558.255 |  | 556.292 | 0.3529 | 548.14 | 526.22 | 0.1326 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.635 |  | 554.2244 | 0.7958 | 551.02 | 540.105 | 0.0304 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.92 |  | 586.6485 | 0.5577 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.55 |  | 211.5468 | 0.4742 | 207.06 | 202.18 | 0.3058 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1803.84 |  | 1799.2666 | 0.2542 | 1786.525 | 1767.54 | 0.0449 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 560.64 |  | 558.8765 | 0.3155 | 559.22 | 544.305 | 0.0731 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.355 |  | 174.9723 | 0.2187 | 175.265 | 171.06 | 0.2566 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 560.64 |  | 558.8765 | 0.3155 | 559.22 | 544.305 | 0.0731 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 175.355 |  | 174.9723 | 0.2187 | 175.265 | 171.06 | 0.2566 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1803.84 |  | 1799.2666 | 0.2542 | 1786.525 | 1767.54 | 0.0449 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 423.26 |  | 421.1362 | 0.5043 | 419.42 | 414.87 | 0.1299 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 244.58 |  | 244.2189 | 0.1479 | 248.43 | 244.47 | 0.0327 | watch_only | none |
| 6 | SOXX | semiconductor_index | 558.635 |  | 554.2244 | 0.7958 | 551.02 | 540.105 | 0.0304 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 589.92 |  | 586.6485 | 0.5577 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| 8 | WDC | memory_hbm_storage | 558.255 |  | 556.292 | 0.3529 | 548.14 | 526.22 | 0.1326 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 213.3 |  | 211.7026 | 0.7545 | 207.4 | 205.01 | 0.3329 | buy_precheck_manual_confirm | none |
| 10 | MRVL | custom_silicon_networking | 212.55 |  | 211.5468 | 0.4742 | 207.06 | 202.18 | 0.3058 | buy_precheck_manual_confirm | none |
| 11 | LIN | industrial_gases | 508.51 |  | 507.487 | 0.2016 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ARM | ai_accelerator | 285.77 |  | 285.5794 | 0.0667 | 286.39 | 280.275 | 4.899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | KLAC | semiconductor_equipment | 216.46 |  | 216.1745 | 0.1321 | 215.465 | 210.975 | 4.241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | PWR | data_center_power_cooling | 644.41 |  | 641.7512 | 0.4143 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | MKSI | semiconductor_materials | 347.72 |  | 345.5551 | 0.6265 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | STX | memory_hbm_storage | 910.54 |  | 909.4445 | 0.1205 | 899.59 | 860.605 | 1.1466 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 320.95 |  | 319.5939 | 0.4243 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | MU | memory_hbm_storage | 972.45 |  | 968.5072 | 0.4071 | 963.41 | 936.99 | 1.234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 556.59 |  | 552.8044 | 0.6848 | 548.755 | 526.6 | 2.5207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.3 |  | 211.7026 | 0.7545 | 207.4 | 205.01 | 0.3329 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 423.26 |  | 421.1362 | 0.5043 | 419.42 | 414.87 | 0.1299 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 558.255 |  | 556.292 | 0.3529 | 548.14 | 526.22 | 0.1326 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.635 |  | 554.2244 | 0.7958 | 551.02 | 540.105 | 0.0304 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.92 |  | 586.6485 | 0.5577 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.55 |  | 211.5468 | 0.4742 | 207.06 | 202.18 | 0.3058 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1803.84 |  | 1799.2666 | 0.2542 | 1786.525 | 1767.54 | 0.0449 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 560.64 |  | 558.8765 | 0.3155 | 559.22 | 544.305 | 0.0731 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.355 |  | 174.9723 | 0.2187 | 175.265 | 171.06 | 0.2566 | buy_precheck_manual_confirm | none |
| 10 | QQQ | market_regime | 707.12 |  | 707.4396 | -0.0452 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 747.755 |  | 748.4828 | -0.0972 | 747.68 | 746.425 | 0.0067 | below_vwap | below_vwap |
| 12 | TER | semiconductor_test_packaging | 371.57 |  | 371.6621 | -0.0248 | 369.53 | 365 | 0.1319 | below_vwap | below_vwap |
| 13 | AMKR | semiconductor_test_packaging | 67.28 |  | 67.4626 | -0.2707 | 66.73 | 64.98 | 3.7604 | below_vwap | below_vwap,spread_too_wide |
| 14 | SMCI | ai_server_oem | 30.83 |  | 31.1415 | -1.0003 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 15 | MU | memory_hbm_storage | 972.45 |  | 968.5072 | 0.4071 | 963.41 | 936.99 | 1.234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 556.59 |  | 552.8044 | 0.6848 | 548.755 | 526.6 | 2.5207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SNDK | memory_hbm_storage | 1617.77 |  | 1583.2477 | 2.1805 | 1558.88 | 1518.99 | 1.2363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 910.54 |  | 909.4445 | 0.1205 | 899.59 | 860.605 | 1.1466 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AVGO | custom_silicon_networking | 398.1 |  | 392.1925 | 1.5063 | 387.635 | 380.205 | 0.4396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TQQQ | leveraged_tool | 70.81 |  | 70.8563 | -0.0653 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.12 |  | 707.4396 | -0.0452 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.81 |  | 70.8563 | -0.0653 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.3 |  | 211.7026 | 0.7545 | 207.4 | 205.01 | 0.3329 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.355 |  | 389.7171 | -0.0929 | 400.89 | 392.26 | 0.0616 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.36 |  | 324.9399 | -0.1785 | 328.865 | 325.74 | 0.5827 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 345.435 |  | 347.4817 | -0.589 | 348.76 | 346.23 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 556.59 |  | 552.8044 | 0.6848 | 548.755 | 526.6 | 2.5207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.26 |  | 421.1362 | 0.5043 | 419.42 | 414.87 | 0.1299 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.635 |  | 554.2244 | 0.7958 | 551.02 | 540.105 | 0.0304 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.92 |  | 586.6485 | 0.5577 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.1 |  | 392.1925 | 1.5063 | 387.635 | 380.205 | 0.4396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 972.45 |  | 968.5072 | 0.4071 | 963.41 | 936.99 | 1.234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.55 |  | 211.5468 | 0.4742 | 207.06 | 202.18 | 0.3058 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 443.48 |  | 442.3999 | 0.2441 | 435.98 | 415.79 | 0.5051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.28 |  | 48.907 | -1.2821 | 48.96 | 47.01 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.83 |  | 31.1415 | -1.0003 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 747.755 |  | 748.4828 | -0.0972 | 747.68 | 746.425 | 0.0067 | below_vwap | below_vwap |
| IWM | market_regime | 293.65 |  | 294.8757 | -0.4157 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.42 |  | 126.4545 | -0.0273 | 128.79 | 125.83 | 0.0475 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.205 |  | 83.3395 | -0.1614 | 83.22 | 79.6 | 0.4086 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.835 |  | 299.8201 | 1.0056 | 297.69 | 293.905 | 1.9284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.46 |  | 407.6578 | -0.2938 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.41 |  | 641.7512 | 0.4143 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 992.225 |  | 1003.9001 | -1.163 | 1036.605 | 998.94 | 0.3024 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 473.035 |  | 473.8084 | -0.1632 | 473.865 | 466.83 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.38 |  | 142.8874 | -0.3551 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.355 |  | 174.9723 | 0.2187 | 175.265 | 171.06 | 0.2566 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 315.27 |  | 316.0045 | -0.2324 | 317.93 | 306.89 | 0.1776 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 831.53 |  | 837.8351 | -0.7525 | 840.47 | 814.62 | 4.8104 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 401.16 |  | 404.9121 | -0.9267 | 407.12 | 397.835 | 1.6004 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.81 |  | 113.9058 | -2.7179 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.29 |  | 329.9856 | 0.3953 | 322.67 | 307.545 | 4.7904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1803.84 |  | 1799.2666 | 0.2542 | 1786.525 | 1767.54 | 0.0449 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.64 |  | 558.8765 | 0.3155 | 559.22 | 544.305 | 0.0731 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.95 |  | 319.5939 | 0.4243 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.46 |  | 216.1745 | 0.1321 | 215.465 | 210.975 | 4.241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.57 |  | 371.6621 | -0.0248 | 369.53 | 365 | 0.1319 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.28 |  | 67.4626 | -0.2707 | 66.73 | 64.98 | 3.7604 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.24 |  | 55.591 | -0.6313 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.73 |  | 138.9059 | -0.1266 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 347.72 |  | 345.5551 | 0.6265 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.51 |  | 507.487 | 0.2016 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.46 |  | 297.7517 | -0.4338 | 300.24 | 297.585 | 4.918 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.06 |  | 30.6593 | -1.9547 | 30.78 | 29.46 | 2.6946 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 41.51 |  | 42.4214 | -2.1485 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.57 |  | 23.9762 | -1.6942 | 24.255 | 23.58 | 0.0849 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1617.77 |  | 1583.2477 | 2.1805 | 1558.88 | 1518.99 | 1.2363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.255 |  | 556.292 | 0.3529 | 548.14 | 526.22 | 0.1326 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 910.54 |  | 909.4445 | 0.1205 | 899.59 | 860.605 | 1.1466 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 244.58 |  | 244.2189 | 0.1479 | 248.43 | 244.47 | 0.0327 | watch_only | none |
| META | cloud_ai_capex | 626.86 |  | 630.0638 | -0.5085 | 647.02 | 632.77 | 0.7179 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.77 |  | 285.5794 | 0.0667 | 286.39 | 280.275 | 4.899 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.14 |  | 166.7233 | -0.3499 | 166.63 | 162.08 | 0.7945 | below_vwap | below_vwap,spread_too_wide |
