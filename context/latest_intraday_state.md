# Intraday State

- Generated at: `2026-07-23T02:05:55+08:00`
- Market time ET: `2026-07-22T14:05:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'below_opening_15m_low': 8, 'below_vwap': 18, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.51 |  | 707.504 | 0.0008 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.76 |  | 553.2557 | 0.9949 | 551.02 | 540.105 | 0.0591 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.91 |  | 585.8124 | 0.6995 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.4 |  | 748.5369 | -0.0183 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.76 |  | 211.3804 | 1.1257 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | WDC | memory_hbm_storage | 556.86 |  | 556.0793 | 0.1404 | 548.14 | 526.22 | 0.1544 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.76 |  | 553.2557 | 0.9949 | 551.02 | 540.105 | 0.0591 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.91 |  | 585.8124 | 0.6995 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 707.51 |  | 707.504 | 0.0008 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.45 |  | 1798.6631 | 0.2661 | 1786.525 | 1767.54 | 0.1026 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.095 |  | 299.2112 | 0.6296 | 297.69 | 293.905 | 0.1993 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 70.92 |  | 70.8648 | 0.0779 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.51 |  | 707.504 | 0.0008 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1803.45 |  | 1798.6631 | 0.2661 | 1786.525 | 1767.54 | 0.1026 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.91 |  | 585.8124 | 0.6995 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 4 | WDC | memory_hbm_storage | 556.86 |  | 556.0793 | 0.1404 | 548.14 | 526.22 | 0.1544 | buy_precheck_manual_confirm | none |
| 5 | VRT | data_center_power_cooling | 301.095 |  | 299.2112 | 0.6296 | 297.69 | 293.905 | 0.1993 | buy_precheck_manual_confirm | none |
| 6 | SOXX | semiconductor_index | 558.76 |  | 553.2557 | 0.9949 | 551.02 | 540.105 | 0.0591 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 143.325 |  | 142.9246 | 0.2802 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | NVDA | ai_accelerator | 213.76 |  | 211.3804 | 1.1257 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 9 | ONTO | semiconductor_test_packaging | 295.38 |  | 295.3656 | 0.0049 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | APD | industrial_gases | 298.03 |  | 297.8189 | 0.0709 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TT | data_center_power_cooling | 475.45 |  | 473.7571 | 0.3573 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ANET | ai_networking_optical | 175.35 |  | 174.8931 | 0.2613 | 175.265 | 171.06 | 2.6233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | PWR | data_center_power_cooling | 642.35 |  | 640.9216 | 0.2229 | 641.19 | 628.17 | 3.9963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 421.12 |  | 420.8084 | 0.0741 | 419.42 | 414.87 | 0.4512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | KLAC | semiconductor_equipment | 216.38 |  | 216.1192 | 0.1207 | 215.465 | 210.975 | 4.2333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LIN | industrial_gases | 509.72 |  | 507.327 | 0.4717 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 139.03 |  | 138.8661 | 0.118 | 140.09 | 135.555 | 0.4747 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 911.16 |  | 909.318 | 0.2026 | 899.59 | 860.605 | 2.6999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 372.67 |  | 371.6699 | 0.2691 | 369.53 | 365 | 4.94 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMAT | semiconductor_equipment | 560.61 |  | 558.5738 | 0.3645 | 559.22 | 544.305 | 0.3585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.76 |  | 211.3804 | 1.1257 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | WDC | memory_hbm_storage | 556.86 |  | 556.0793 | 0.1404 | 548.14 | 526.22 | 0.1544 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.76 |  | 553.2557 | 0.9949 | 551.02 | 540.105 | 0.0591 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.91 |  | 585.8124 | 0.6995 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 707.51 |  | 707.504 | 0.0008 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.45 |  | 1798.6631 | 0.2661 | 1786.525 | 1767.54 | 0.1026 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.095 |  | 299.2112 | 0.6296 | 297.69 | 293.905 | 0.1993 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 70.92 |  | 70.8648 | 0.0779 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 748.4 |  | 748.5369 | -0.0183 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |
| 10 | DELL | ai_server_oem | 440.975 |  | 442.525 | -0.3503 | 435.98 | 415.79 | 1.2041 | below_vwap | below_vwap,spread_too_wide |
| 11 | AMKR | semiconductor_test_packaging | 67.385 |  | 67.4778 | -0.1375 | 66.73 | 64.98 | 2.226 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMCI | ai_server_oem | 30.9 |  | 31.1741 | -0.8794 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 13 | MU | memory_hbm_storage | 974.535 |  | 968.3684 | 0.6368 | 963.41 | 936.99 | 1.0969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 421.12 |  | 420.8084 | 0.0741 | 419.42 | 414.87 | 0.4512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 555.84 |  | 551.7111 | 0.7484 | 548.755 | 526.6 | 0.9157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 475.45 |  | 473.7571 | 0.3573 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1601.61 |  | 1580.4182 | 1.3409 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 911.16 |  | 909.318 | 0.2026 | 899.59 | 860.605 | 2.6999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 212.86 |  | 211.3692 | 0.7053 | 207.06 | 202.18 | 0.9537 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 372.67 |  | 371.6699 | 0.2691 | 369.53 | 365 | 4.94 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.51 |  | 707.504 | 0.0008 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 70.92 |  | 70.8648 | 0.0779 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.76 |  | 211.3804 | 1.1257 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.4 |  | 390.0902 | -0.6896 | 400.89 | 392.26 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.77 |  | 325.0538 | -0.395 | 328.865 | 325.74 | 0.1946 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.09 |  | 347.9139 | -0.2368 | 348.76 | 346.23 | 0.1008 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555.84 |  | 551.7111 | 0.7484 | 548.755 | 526.6 | 0.9157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.12 |  | 420.8084 | 0.0741 | 419.42 | 414.87 | 0.4512 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.76 |  | 553.2557 | 0.9949 | 551.02 | 540.105 | 0.0591 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.91 |  | 585.8124 | 0.6995 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.63 |  | 391.2476 | 1.3757 | 387.635 | 380.205 | 0.8799 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 974.535 |  | 968.3684 | 0.6368 | 963.41 | 936.99 | 1.0969 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.86 |  | 211.3692 | 0.7053 | 207.06 | 202.18 | 0.9537 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 440.975 |  | 442.525 | -0.3503 | 435.98 | 415.79 | 1.2041 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.77 |  | 49.0186 | -0.5072 | 48.96 | 47.01 | 0.082 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.9 |  | 31.1741 | -0.8794 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748.4 |  | 748.5369 | -0.0183 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 294.325 |  | 295.0896 | -0.2591 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.365 |  | 126.6198 | -0.991 | 128.79 | 125.83 | 0.1675 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.715 |  | 83.4944 | -0.9334 | 83.22 | 79.6 | 0.0725 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 301.095 |  | 299.2112 | 0.6296 | 297.69 | 293.905 | 0.1993 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.36 |  | 407.9092 | -0.1346 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 642.35 |  | 640.9216 | 0.2229 | 641.19 | 628.17 | 3.9963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 990.63 |  | 1005.7772 | -1.506 | 1036.605 | 998.94 | 3.9924 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.45 |  | 473.7571 | 0.3573 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.325 |  | 142.9246 | 0.2802 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.35 |  | 174.8931 | 0.2613 | 175.265 | 171.06 | 2.6233 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.35 |  | 316.1058 | -0.5554 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 827.14 |  | 839.3355 | -1.453 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.09 |  | 405.5671 | -0.8573 | 407.12 | 397.835 | 1.8976 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.01 |  | 114.3057 | -2.8833 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.145 |  | 329.6258 | 0.7643 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1803.45 |  | 1798.6631 | 0.2661 | 1786.525 | 1767.54 | 0.1026 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.61 |  | 558.5738 | 0.3645 | 559.22 | 544.305 | 0.3585 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.13 |  | 319.174 | 0.6128 | 317.72 | 311.31 | 3.9735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.38 |  | 216.1192 | 0.1207 | 215.465 | 210.975 | 4.2333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.67 |  | 371.6699 | 0.2691 | 369.53 | 365 | 4.94 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.38 |  | 295.3656 | 0.0049 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.385 |  | 67.4778 | -0.1375 | 66.73 | 64.98 | 2.226 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.6 |  | 55.6847 | -0.1521 | 56.2 | 54.45 | 0.7194 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 139.03 |  | 138.8661 | 0.118 | 140.09 | 135.555 | 0.4747 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 348.115 |  | 344.4688 | 1.0585 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.72 |  | 507.327 | 0.4717 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.03 |  | 297.8189 | 0.0709 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.28 |  | 30.7426 | -1.5047 | 30.78 | 29.46 | 0.0991 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.7 |  | 42.5863 | -2.0813 | 42.29 | 40.305 | 0.048 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.69 |  | 24.0503 | -1.4982 | 24.255 | 23.58 | 0.1266 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1601.61 |  | 1580.4182 | 1.3409 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 556.86 |  | 556.0793 | 0.1404 | 548.14 | 526.22 | 0.1544 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 911.16 |  | 909.318 | 0.2026 | 899.59 | 860.605 | 2.6999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 242.71 |  | 244.3067 | -0.6536 | 248.43 | 244.47 | 0.0165 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.34 |  | 630.8222 | -0.7105 | 647.02 | 632.77 | 0.8286 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.22 |  | 285.6532 | -0.1517 | 286.39 | 280.275 | 3.2045 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.04 |  | 166.7846 | -0.4464 | 166.63 | 162.08 | 1.8369 | below_vwap | below_vwap,spread_too_wide |
