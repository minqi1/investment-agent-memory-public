# Intraday State

- Generated at: `2026-07-23T03:03:29+08:00`
- Market time ET: `2026-07-22T15:03:30-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 22, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 10, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.19 |  | 707.4519 | -0.037 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.67 |  | 553.8625 | 0.868 | 551.02 | 540.105 | 0.0412 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.29 |  | 586.4847 | 0.6488 | 581.9 | 572.01 | 0.044 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.21 |  | 748.5057 | -0.0395 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.81 |  | 211.582 | 1.053 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 969.11 |  | 968.454 | 0.0677 | 963.41 | 936.99 | 0.1734 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 557.4 |  | 556.1988 | 0.216 | 548.14 | 526.22 | 0.1399 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.67 |  | 553.8625 | 0.868 | 551.02 | 540.105 | 0.0412 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.29 |  | 586.4847 | 0.6488 | 581.9 | 572.01 | 0.044 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.26 |  | 1799.1196 | 0.2301 | 1786.525 | 1767.54 | 0.0272 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.34 |  | 216.1481 | 0.0888 | 215.465 | 210.975 | 0.1479 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 560.52 |  | 558.8082 | 0.3063 | 559.22 | 544.305 | 0.0803 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 302.45 |  | 299.6503 | 0.9343 | 297.69 | 293.905 | 0.1289 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 560.52 |  | 558.8082 | 0.3063 | 559.22 | 544.305 | 0.0803 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 216.34 |  | 216.1481 | 0.0888 | 215.465 | 210.975 | 0.1479 | buy_precheck_manual_confirm | none |
| 3 | MU | memory_hbm_storage | 969.11 |  | 968.454 | 0.0677 | 963.41 | 936.99 | 0.1734 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1803.26 |  | 1799.1196 | 0.2301 | 1786.525 | 1767.54 | 0.0272 | buy_precheck_manual_confirm | none |
| 5 | WDC | memory_hbm_storage | 557.4 |  | 556.1988 | 0.216 | 548.14 | 526.22 | 0.1399 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 590.29 |  | 586.4847 | 0.6488 | 581.9 | 572.01 | 0.044 | buy_precheck_manual_confirm | none |
| 7 | SOXX | semiconductor_index | 558.67 |  | 553.8625 | 0.868 | 551.02 | 540.105 | 0.0412 | buy_precheck_manual_confirm | none |
| 8 | PWR | data_center_power_cooling | 643.34 |  | 641.5468 | 0.2795 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.81 |  | 211.582 | 1.053 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| 10 | ENTG | semiconductor_materials | 139.11 |  | 138.8594 | 0.1804 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | VRT | data_center_power_cooling | 302.45 |  | 299.6503 | 0.9343 | 297.69 | 293.905 | 0.1289 | buy_precheck_manual_confirm | none |
| 12 | ANET | ai_networking_optical | 175.36 |  | 174.9511 | 0.2337 | 175.265 | 171.06 | 2.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | LIN | industrial_gases | 509.23 |  | 507.4343 | 0.3539 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 371.91 |  | 371.6653 | 0.0658 | 369.53 | 365 | 5.1195 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MKSI | semiconductor_materials | 347.65 |  | 345.4356 | 0.6411 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 296.58 |  | 295.3907 | 0.4026 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ALAB | ai_networking_optical | 330.53 |  | 329.9025 | 0.1902 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 321.02 |  | 319.5424 | 0.4624 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TSM | foundry | 422.52 |  | 421.0212 | 0.356 | 419.42 | 414.87 | 0.9585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | QQQ | market_regime | 707.19 |  | 707.4519 | -0.037 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.81 |  | 211.582 | 1.053 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 969.11 |  | 968.454 | 0.0677 | 963.41 | 936.99 | 0.1734 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 557.4 |  | 556.1988 | 0.216 | 548.14 | 526.22 | 0.1399 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.67 |  | 553.8625 | 0.868 | 551.02 | 540.105 | 0.0412 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.29 |  | 586.4847 | 0.6488 | 581.9 | 572.01 | 0.044 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.26 |  | 1799.1196 | 0.2301 | 1786.525 | 1767.54 | 0.0272 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.34 |  | 216.1481 | 0.0888 | 215.465 | 210.975 | 0.1479 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 560.52 |  | 558.8082 | 0.3063 | 559.22 | 544.305 | 0.0803 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 302.45 |  | 299.6503 | 0.9343 | 297.69 | 293.905 | 0.1289 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 906.18 |  | 909.4849 | -0.3634 | 899.59 | 860.605 | 2.142 | below_vwap | below_vwap,spread_too_wide |
| 11 | QQQ | market_regime | 707.19 |  | 707.4519 | -0.037 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 748.21 |  | 748.5057 | -0.0395 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 13 | SKHY | memory_hbm_storage | 166.665 |  | 166.7375 | -0.0435 | 166.63 | 162.08 | 0.714 | below_vwap | below_vwap,spread_too_wide |
| 14 | DELL | ai_server_oem | 441.62 |  | 442.3532 | -0.1657 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AMKR | semiconductor_test_packaging | 67.36 |  | 67.47 | -0.163 | 66.73 | 64.98 | 3.9044 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMCI | ai_server_oem | 30.725 |  | 31.1504 | -1.3657 | 30.66 | 28.52 | 0.0651 | below_vwap | below_vwap |
| 17 | TSM | foundry | 422.52 |  | 421.0212 | 0.356 | 419.42 | 414.87 | 0.9585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 557.165 |  | 552.2822 | 0.8841 | 548.755 | 526.6 | 2.7766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SNDK | memory_hbm_storage | 1608.34 |  | 1581.9233 | 1.6699 | 1558.88 | 1518.99 | 3.8201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 212.88 |  | 211.5134 | 0.6461 | 207.06 | 202.18 | 1.0851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.19 |  | 707.4519 | -0.037 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.845 |  | 70.8595 | -0.0204 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.81 |  | 211.582 | 1.053 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.92 |  | 389.7456 | -0.2118 | 400.89 | 392.26 | 0.2546 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.355 |  | 324.9614 | -0.1866 | 328.865 | 325.74 | 0.3361 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 345.67 |  | 347.7412 | -0.5956 | 348.76 | 346.23 | 0.0752 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 557.165 |  | 552.2822 | 0.8841 | 548.755 | 526.6 | 2.7766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.52 |  | 421.0212 | 0.356 | 419.42 | 414.87 | 0.9585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.67 |  | 553.8625 | 0.868 | 551.02 | 540.105 | 0.0412 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.29 |  | 586.4847 | 0.6488 | 581.9 | 572.01 | 0.044 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.9 |  | 391.9089 | 1.5287 | 387.635 | 380.205 | 0.5152 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 969.11 |  | 968.454 | 0.0677 | 963.41 | 936.99 | 0.1734 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 212.88 |  | 211.5134 | 0.6461 | 207.06 | 202.18 | 1.0851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 441.62 |  | 442.3532 | -0.1657 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.41 |  | 48.9364 | -1.0757 | 48.96 | 47.01 | 0.0413 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.725 |  | 31.1504 | -1.3657 | 30.66 | 28.52 | 0.0651 | below_vwap | below_vwap |
| SPY | market_regime | 748.21 |  | 748.5057 | -0.0395 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.805 |  | 294.9491 | -0.3879 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.91 |  | 126.4994 | -1.2564 | 128.79 | 125.83 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.965 |  | 83.3443 | -0.4551 | 83.22 | 79.6 | 0.1085 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 302.45 |  | 299.6503 | 0.9343 | 297.69 | 293.905 | 0.1289 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.62 |  | 407.8071 | -0.2911 | 409.095 | 398.16 | 0.15 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 643.34 |  | 641.5468 | 0.2795 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 995.14 |  | 1004.6148 | -0.9431 | 1036.605 | 998.94 | 1.2561 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 472.92 |  | 473.8962 | -0.206 | 473.865 | 466.83 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.605 |  | 142.9457 | -0.2384 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.36 |  | 174.9511 | 0.2337 | 175.265 | 171.06 | 2.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.88 |  | 316.0271 | -0.0466 | 317.93 | 306.89 | 3.4918 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 827.435 |  | 838.1562 | -1.2791 | 840.47 | 814.62 | 0.2538 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 402.88 |  | 405.1336 | -0.5563 | 407.12 | 397.835 | 0.139 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.13 |  | 114.0438 | -2.555 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.53 |  | 329.9025 | 0.1902 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1803.26 |  | 1799.1196 | 0.2301 | 1786.525 | 1767.54 | 0.0272 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.52 |  | 558.8082 | 0.3063 | 559.22 | 544.305 | 0.0803 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.02 |  | 319.5424 | 0.4624 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.34 |  | 216.1481 | 0.0888 | 215.465 | 210.975 | 0.1479 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 371.91 |  | 371.6653 | 0.0658 | 369.53 | 365 | 5.1195 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.58 |  | 295.3907 | 0.4026 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.36 |  | 67.47 | -0.163 | 66.73 | 64.98 | 3.9044 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.55 |  | 55.6406 | -0.1629 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.11 |  | 138.8594 | 0.1804 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.65 |  | 345.4356 | 0.6411 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.23 |  | 507.4343 | 0.3539 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.97 |  | 297.8301 | -0.2888 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.06 |  | 30.6793 | -2.0187 | 30.78 | 29.46 | 0.0665 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.53 |  | 42.469 | -2.2111 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.6 |  | 23.9892 | -1.6225 | 24.255 | 23.58 | 0.0847 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1608.34 |  | 1581.9233 | 1.6699 | 1558.88 | 1518.99 | 3.8201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 557.4 |  | 556.1988 | 0.216 | 548.14 | 526.22 | 0.1399 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 906.18 |  | 909.4849 | -0.3634 | 899.59 | 860.605 | 2.142 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 244.075 |  | 244.1679 | -0.038 | 248.43 | 244.47 | 0.0328 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.065 |  | 630.3187 | -0.6748 | 647.02 | 632.77 | 0.2396 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.25 |  | 285.5844 | -0.1171 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.665 |  | 166.7375 | -0.0435 | 166.63 | 162.08 | 0.714 | below_vwap | below_vwap,spread_too_wide |
