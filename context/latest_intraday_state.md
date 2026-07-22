# Intraday State

- Generated at: `2026-07-23T02:41:50+08:00`
- Market time ET: `2026-07-22T14:41:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 27, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 7, 'spread_too_wide_or_missing': 10, 'price_stale_or_missing': 1, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.82 |  | 707.4599 | -0.0904 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.55 |  | 553.6291 | 0.7082 | 551.02 | 540.105 | 0.0413 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.1 |  | 586.1043 | 0.5111 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.26 |  | 748.5148 | -0.034 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.62 |  | 211.5049 | 1 | 207.4 | 205.01 | 0.22 | buy_precheck_manual_confirm | none |
| 2 | TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 | 0.1011 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 557.55 |  | 553.6291 | 0.7082 | 551.02 | 540.105 | 0.0413 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.1 |  | 586.1043 | 0.5111 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.56 |  | 211.456 | 0.5221 | 207.06 | 202.18 | 0.2776 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1801.81 |  | 1798.97 | 0.1579 | 1786.525 | 1767.54 | 0.0394 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.245 |  | 216.1313 | 0.0526 | 215.465 | 210.975 | 0.0509 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 302.295 |  | 299.4597 | 0.9468 | 297.69 | 293.905 | 0.2713 | buy_precheck_manual_confirm | none |
| 9 | PWR | data_center_power_cooling | 643.97 |  | 641.328 | 0.412 | 641.19 | 628.17 | 0.1382 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 | 0.1011 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 216.245 |  | 216.1313 | 0.0526 | 215.465 | 210.975 | 0.0509 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1801.81 |  | 1798.97 | 0.1579 | 1786.525 | 1767.54 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | PWR | data_center_power_cooling | 643.97 |  | 641.328 | 0.412 | 641.19 | 628.17 | 0.1382 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 175.19 |  | 174.9328 | 0.1471 | 175.265 | 171.06 | 0.137 | watch_only | none |
| 6 | JCI | data_center_power_cooling | 143.085 |  | 142.9591 | 0.0881 | 143.27 | 141.04 | 0.0489 | watch_only | none |
| 7 | SOXX | semiconductor_index | 557.55 |  | 553.6291 | 0.7082 | 551.02 | 540.105 | 0.0413 | buy_precheck_manual_confirm | none |
| 8 | SMH | semiconductor_index | 589.1 |  | 586.1043 | 0.5111 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 212.56 |  | 211.456 | 0.5221 | 207.06 | 202.18 | 0.2776 | buy_precheck_manual_confirm | none |
| 10 | APD | industrial_gases | 298.29 |  | 297.8433 | 0.15 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | NVDA | ai_accelerator | 213.62 |  | 211.5049 | 1 | 207.4 | 205.01 | 0.22 | buy_precheck_manual_confirm | none |
| 12 | AMAT | semiconductor_equipment | 560.07 |  | 558.755 | 0.2353 | 559.22 | 544.305 | 3.0657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 421.54 |  | 420.9257 | 0.1459 | 419.42 | 414.87 | 0.4507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 302.295 |  | 299.4597 | 0.9468 | 297.69 | 293.905 | 0.2713 | buy_precheck_manual_confirm | none |
| 15 | LIN | industrial_gases | 510.69 |  | 507.3513 | 0.6581 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MKSI | semiconductor_materials | 347.36 |  | 344.7341 | 0.7617 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | AMD | ai_accelerator | 554.53 |  | 551.8439 | 0.4867 | 548.755 | 526.6 | 2.0684 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 320.67 |  | 319.4549 | 0.3804 | 317.72 | 311.31 | 3.3867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | QQQ | market_regime | 706.82 |  | 707.4599 | -0.0904 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 20 | SPY | market_regime | 748.26 |  | 748.5148 | -0.034 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.62 |  | 211.5049 | 1 | 207.4 | 205.01 | 0.22 | buy_precheck_manual_confirm | none |
| 2 | TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 | 0.1011 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 557.55 |  | 553.6291 | 0.7082 | 551.02 | 540.105 | 0.0413 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.1 |  | 586.1043 | 0.5111 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.56 |  | 211.456 | 0.5221 | 207.06 | 202.18 | 0.2776 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1801.81 |  | 1798.97 | 0.1579 | 1786.525 | 1767.54 | 0.0394 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.245 |  | 216.1313 | 0.0526 | 215.465 | 210.975 | 0.0509 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 302.295 |  | 299.4597 | 0.9468 | 297.69 | 293.905 | 0.2713 | buy_precheck_manual_confirm | none |
| 9 | PWR | data_center_power_cooling | 643.97 |  | 641.328 | 0.412 | 641.19 | 628.17 | 0.1382 | buy_precheck_manual_confirm | none |
| 10 | MU | memory_hbm_storage | 966.02 |  | 968.4717 | -0.2532 | 963.41 | 936.99 | 2.0704 | below_vwap | below_vwap,spread_too_wide |
| 11 | WDC | memory_hbm_storage | 555.8 |  | 556.1683 | -0.0662 | 548.14 | 526.22 | 0.1205 | below_vwap | below_vwap |
| 12 | STX | memory_hbm_storage | 904.13 |  | 909.5613 | -0.5971 | 899.59 | 860.605 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | QQQ | market_regime | 706.82 |  | 707.4599 | -0.0904 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 748.26 |  | 748.5148 | -0.034 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 15 | TER | semiconductor_test_packaging | 370.71 |  | 371.6547 | -0.2542 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | DELL | ai_server_oem | 440.325 |  | 442.3911 | -0.467 | 435.98 | 415.79 | 0.3634 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMKR | semiconductor_test_packaging | 67.31 |  | 67.471 | -0.2387 | 66.73 | 64.98 | 3.7587 | below_vwap | below_vwap,spread_too_wide |
| 18 | SMCI | ai_server_oem | 30.955 |  | 31.1593 | -0.6555 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| 19 | TSM | foundry | 421.54 |  | 420.9257 | 0.1459 | 419.42 | 414.87 | 0.4507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 554.53 |  | 551.8439 | 0.4867 | 548.755 | 526.6 | 2.0684 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.82 |  | 707.4599 | -0.0904 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.79 |  | 70.8598 | -0.0985 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.62 |  | 211.5049 | 1 | 207.4 | 205.01 | 0.22 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.49 |  | 389.8762 | -0.3555 | 400.89 | 392.26 | 0.0386 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.425 |  | 324.9834 | -0.1718 | 328.865 | 325.74 | 0.0092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.61 |  | 347.833 | -0.3516 | 348.76 | 346.23 | 0.1644 | below_vwap | below_vwap |
| AMD | ai_accelerator | 554.53 |  | 551.8439 | 0.4867 | 548.755 | 526.6 | 2.0684 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.54 |  | 420.9257 | 0.1459 | 419.42 | 414.87 | 0.4507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.55 |  | 553.6291 | 0.7082 | 551.02 | 540.105 | 0.0413 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.1 |  | 586.1043 | 0.5111 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.1 |  | 391.747 | 1.3665 | 387.635 | 380.205 | 4.5026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 966.02 |  | 968.4717 | -0.2532 | 963.41 | 936.99 | 2.0704 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 212.56 |  | 211.456 | 0.5221 | 207.06 | 202.18 | 0.2776 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 440.325 |  | 442.3911 | -0.467 | 435.98 | 415.79 | 0.3634 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.35 |  | 48.9747 | -1.2756 | 48.96 | 47.01 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.955 |  | 31.1593 | -0.6555 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 748.26 |  | 748.5148 | -0.034 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.115 |  | 295.0002 | -0.3001 | 296.39 | 295.22 | 0.0136 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.81 |  | 126.5495 | -1.3746 | 128.79 | 125.83 | 3.7817 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.61 |  | 83.3915 | -0.9372 | 83.22 | 79.6 | 2.76 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.295 |  | 299.4597 | 0.9468 | 297.69 | 293.905 | 0.2713 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.62 |  | 407.8684 | -0.0609 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.97 |  | 641.328 | 0.412 | 641.19 | 628.17 | 0.1382 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 999.57 |  | 1005.0254 | -0.5428 | 1036.605 | 998.94 | 2.5471 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 | 0.1011 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 143.085 |  | 142.9591 | 0.0881 | 143.27 | 141.04 | 0.0489 | watch_only | none |
| ANET | ai_networking_optical | 175.19 |  | 174.9328 | 0.1471 | 175.265 | 171.06 | 0.137 | watch_only | none |
| COHR | ai_networking_optical | 315.1 |  | 316.0267 | -0.2932 | 317.93 | 306.89 | 0.311 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 826.27 |  | 838.4425 | -1.4518 | 840.47 | 814.62 | 0.3328 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 403.18 |  | 405.3078 | -0.525 | 407.12 | 397.835 | 2.1107 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.74 |  | 114.1477 | -2.9853 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.64 |  | 329.8319 | 0.8514 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1801.81 |  | 1798.97 | 0.1579 | 1786.525 | 1767.54 | 0.0394 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.07 |  | 558.755 | 0.2353 | 559.22 | 544.305 | 3.0657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.67 |  | 319.4549 | 0.3804 | 317.72 | 311.31 | 3.3867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.245 |  | 216.1313 | 0.0526 | 215.465 | 210.975 | 0.0509 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 370.71 |  | 371.6547 | -0.2542 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.22 |  | 295.3647 | -0.049 | 298.42 | 288.335 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.31 |  | 67.471 | -0.2387 | 66.73 | 64.98 | 3.7587 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.415 |  | 55.6592 | -0.4387 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.71 |  | 138.8622 | -0.1096 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 347.36 |  | 344.7341 | 0.7617 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.69 |  | 507.3513 | 0.6581 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.29 |  | 297.8433 | 0.15 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.94 |  | 30.6998 | -2.4751 | 30.78 | 29.46 | 0.0668 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.33 |  | 42.5108 | -2.7776 | 42.29 | 40.305 | 0.0726 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.58 |  | 24.0033 | -1.7634 | 24.255 | 23.58 | 0.0424 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1594.48 |  | 1581.4016 | 0.827 | 1558.88 | 1518.99 | 4.7012 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 555.8 |  | 556.1683 | -0.0662 | 548.14 | 526.22 | 0.1205 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 904.13 |  | 909.5613 | -0.5971 | 899.59 | 860.605 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 242.95 |  | 244.2148 | -0.5179 | 248.43 | 244.47 | 0.0165 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 625.985 |  | 630.4505 | -0.7083 | 647.02 | 632.77 | 0.4153 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 284.57 |  | 285.5864 | -0.3559 | 286.39 | 280.275 | 2.7023 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.4 |  | 166.7384 | -0.203 | 166.63 | 162.08 | 0.1863 | below_vwap | below_vwap |
