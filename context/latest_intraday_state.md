# Intraday State

- Generated at: `2026-07-23T02:54:22+08:00`
- Market time ET: `2026-07-22T14:54:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 22, 'manual_confirm_candidate': 10, 'below_opening_15m_low': 9, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 12, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.035 |  | 707.4528 | -0.0591 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.4 |  | 553.7745 | 0.8353 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.94 |  | 586.2585 | 0.628 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.36 |  | 748.5081 | -0.0198 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.735 |  | 211.5457 | 1.0349 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.92 |  | 420.9485 | 0.2308 | 419.42 | 414.87 | 0.1256 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 556.99 |  | 552.012 | 0.9018 | 548.755 | 526.6 | 0.2047 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.4 |  | 553.7745 | 0.8353 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.94 |  | 586.2585 | 0.628 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.58 |  | 211.4819 | 0.5193 | 207.06 | 202.18 | 0.1176 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.05 |  | 1799.052 | 0.3334 | 1786.525 | 1767.54 | 0.0537 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.6 |  | 216.1374 | 0.214 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.62 |  | 558.7768 | 0.3299 | 559.22 | 544.305 | 0.2176 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 302.34 |  | 299.5884 | 0.9185 | 297.69 | 293.905 | 0.1455 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 421.92 |  | 420.9485 | 0.2308 | 419.42 | 414.87 | 0.1256 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 216.6 |  | 216.1374 | 0.214 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 560.62 |  | 558.7768 | 0.3299 | 559.22 | 544.305 | 0.2176 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1805.05 |  | 1799.052 | 0.3334 | 1786.525 | 1767.54 | 0.0537 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.94 |  | 586.2585 | 0.628 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 175.225 |  | 174.9377 | 0.1642 | 175.265 | 171.06 | 0.1826 | watch_only | none |
| 7 | MRVL | custom_silicon_networking | 212.58 |  | 211.4819 | 0.5193 | 207.06 | 202.18 | 0.1176 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 474.83 |  | 473.9028 | 0.1956 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SOXX | semiconductor_index | 558.4 |  | 553.7745 | 0.8353 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| 10 | NVDA | ai_accelerator | 213.735 |  | 211.5457 | 1.0349 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | ENTG | semiconductor_materials | 138.93 |  | 138.8564 | 0.053 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 296.05 |  | 295.3671 | 0.2312 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | VRT | data_center_power_cooling | 302.34 |  | 299.5884 | 0.9185 | 297.69 | 293.905 | 0.1455 | buy_precheck_manual_confirm | none |
| 14 | AMD | ai_accelerator | 556.99 |  | 552.012 | 0.9018 | 548.755 | 526.6 | 0.2047 | buy_precheck_manual_confirm | none |
| 15 | TER | semiconductor_test_packaging | 372.245 |  | 371.6503 | 0.16 | 369.53 | 365 | 5.0101 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LIN | industrial_gases | 510.06 |  | 507.3999 | 0.5243 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 644.04 |  | 641.4158 | 0.4091 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 556.97 |  | 556.1617 | 0.1453 | 548.14 | 526.22 | 1.0701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ALAB | ai_networking_optical | 331.34 |  | 329.8923 | 0.4388 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | LRCX | semiconductor_equipment | 321.07 |  | 319.4928 | 0.4937 | 317.72 | 311.31 | 4.0676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.735 |  | 211.5457 | 1.0349 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.92 |  | 420.9485 | 0.2308 | 419.42 | 414.87 | 0.1256 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 556.99 |  | 552.012 | 0.9018 | 548.755 | 526.6 | 0.2047 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.4 |  | 553.7745 | 0.8353 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.94 |  | 586.2585 | 0.628 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.58 |  | 211.4819 | 0.5193 | 207.06 | 202.18 | 0.1176 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.05 |  | 1799.052 | 0.3334 | 1786.525 | 1767.54 | 0.0537 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.6 |  | 216.1374 | 0.214 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.62 |  | 558.7768 | 0.3299 | 559.22 | 544.305 | 0.2176 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 302.34 |  | 299.5884 | 0.9185 | 297.69 | 293.905 | 0.1455 | buy_precheck_manual_confirm | none |
| 11 | MU | memory_hbm_storage | 967.79 |  | 968.4437 | -0.0675 | 963.41 | 936.99 | 0.7936 | below_vwap | below_vwap,spread_too_wide |
| 12 | STX | memory_hbm_storage | 904.73 |  | 909.5342 | -0.5282 | 899.59 | 860.605 | 1.9221 | below_vwap | below_vwap,spread_too_wide |
| 13 | QQQ | market_regime | 707.035 |  | 707.4528 | -0.0591 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 748.36 |  | 748.5081 | -0.0198 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 15 | DELL | ai_server_oem | 441.5 |  | 442.3606 | -0.1946 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | AMKR | semiconductor_test_packaging | 67.32 |  | 67.4706 | -0.2232 | 66.73 | 64.98 | 2.2282 | below_vwap | below_vwap,spread_too_wide |
| 17 | SMCI | ai_server_oem | 30.86 |  | 31.1568 | -0.9525 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 18 | TT | data_center_power_cooling | 474.83 |  | 473.9028 | 0.1956 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1604 |  | 1581.6674 | 1.412 | 1558.88 | 1518.99 | 3.8485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 556.97 |  | 556.1617 | 0.1453 | 548.14 | 526.22 | 1.0701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.035 |  | 707.4528 | -0.0591 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.85 |  | 70.8589 | -0.0125 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.735 |  | 211.5457 | 1.0349 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.42 |  | 389.7767 | -0.3481 | 400.89 | 392.26 | 0.1879 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.43 |  | 324.9747 | -0.1676 | 328.865 | 325.74 | 0.1325 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.7 |  | 347.8116 | -0.3196 | 348.76 | 346.23 | 0.0865 | below_vwap | below_vwap |
| AMD | ai_accelerator | 556.99 |  | 552.012 | 0.9018 | 548.755 | 526.6 | 0.2047 | buy_precheck_manual_confirm | none |
| TSM | foundry | 421.92 |  | 420.9485 | 0.2308 | 419.42 | 414.87 | 0.1256 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.4 |  | 553.7745 | 0.8353 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.94 |  | 586.2585 | 0.628 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.4 |  | 391.8379 | 1.4195 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 967.79 |  | 968.4437 | -0.0675 | 963.41 | 936.99 | 0.7936 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 212.58 |  | 211.4819 | 0.5193 | 207.06 | 202.18 | 0.1176 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 441.5 |  | 442.3606 | -0.1946 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.39 |  | 48.9453 | -1.1345 | 48.96 | 47.01 | 0.0827 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.86 |  | 31.1568 | -0.9525 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748.36 |  | 748.5081 | -0.0198 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 294.03 |  | 294.9668 | -0.3176 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.84 |  | 126.5178 | -1.3261 | 128.79 | 125.83 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.6 |  | 83.3596 | -0.9113 | 83.22 | 79.6 | 3.8136 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.34 |  | 299.5884 | 0.9185 | 297.69 | 293.905 | 0.1455 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.63 |  | 407.8534 | -0.3 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.04 |  | 641.4158 | 0.4091 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 997.455 |  | 1004.8335 | -0.7343 | 1036.605 | 998.94 | 2.361 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.83 |  | 473.9028 | 0.1956 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.86 |  | 142.9592 | -0.0694 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.225 |  | 174.9377 | 0.1642 | 175.265 | 171.06 | 0.1826 | watch_only | none |
| COHR | ai_networking_optical | 315.59 |  | 316.0223 | -0.1368 | 317.93 | 306.89 | 0.469 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 827.625 |  | 838.2674 | -1.2696 | 840.47 | 814.62 | 0.2223 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 403.16 |  | 405.2216 | -0.5087 | 407.12 | 397.835 | 2.0935 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.845 |  | 114.0705 | -2.8276 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.34 |  | 329.8923 | 0.4388 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1805.05 |  | 1799.052 | 0.3334 | 1786.525 | 1767.54 | 0.0537 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.62 |  | 558.7768 | 0.3299 | 559.22 | 544.305 | 0.2176 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.07 |  | 319.4928 | 0.4937 | 317.72 | 311.31 | 4.0676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.6 |  | 216.1374 | 0.214 | 215.465 | 210.975 | 0.1154 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 372.245 |  | 371.6503 | 0.16 | 369.53 | 365 | 5.0101 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.05 |  | 295.3671 | 0.2312 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.32 |  | 67.4706 | -0.2232 | 66.73 | 64.98 | 2.2282 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.445 |  | 55.646 | -0.3611 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.93 |  | 138.8564 | 0.053 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.975 |  | 345.2048 | 0.8025 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.06 |  | 507.3999 | 0.5243 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.3 |  | 297.8414 | -0.1818 | 300.24 | 297.585 | 0.1177 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.065 |  | 30.6885 | -2.0316 | 30.78 | 29.46 | 0.0665 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.45 |  | 42.4831 | -2.4318 | 42.29 | 40.305 | 0.0483 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.62 |  | 23.9972 | -1.572 | 24.255 | 23.58 | 0.0847 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1604 |  | 1581.6674 | 1.412 | 1558.88 | 1518.99 | 3.8485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 556.97 |  | 556.1617 | 0.1453 | 548.14 | 526.22 | 1.0701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 904.73 |  | 909.5342 | -0.5282 | 899.59 | 860.605 | 1.9221 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 242.86 |  | 244.1904 | -0.5448 | 248.43 | 244.47 | 0.0288 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626 |  | 630.3727 | -0.6937 | 647.02 | 632.77 | 0.4505 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 284.67 |  | 285.5847 | -0.3203 | 286.39 | 280.275 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| SKHY | memory_hbm_storage | 166.33 |  | 166.7374 | -0.2443 | 166.63 | 162.08 | 1.3287 | below_vwap | below_vwap,spread_too_wide |
