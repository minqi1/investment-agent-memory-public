# Intraday State

- Generated at: `2026-07-23T02:25:55+08:00`
- Market time ET: `2026-07-22T14:25:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 23, 'manual_confirm_candidate': 5, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.87 |  | 707.4825 | -0.0866 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.02 |  | 553.385 | 0.8376 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.53 |  | 585.9693 | 0.6077 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.24 |  | 748.5231 | -0.0378 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.6 |  | 211.449 | 1.0173 | 207.4 | 205.01 | 0.1639 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.02 |  | 553.385 | 0.8376 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.53 |  | 585.9693 | 0.6077 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.33 |  | 211.4211 | 0.4299 | 207.06 | 202.18 | 0.3061 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 216.165 |  | 216.1344 | 0.0141 | 215.465 | 210.975 | 0.037 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 216.165 |  | 216.1344 | 0.0141 | 215.465 | 210.975 | 0.037 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 589.53 |  | 585.9693 | 0.6077 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 3 | MRVL | custom_silicon_networking | 212.33 |  | 211.4211 | 0.4299 | 207.06 | 202.18 | 0.3061 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 474.935 |  | 473.812 | 0.237 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | SOXX | semiconductor_index | 558.02 |  | 553.385 | 0.8376 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 143.27 |  | 142.956 | 0.2197 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ONTO | semiconductor_test_packaging | 295.41 |  | 295.369 | 0.0139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | NVDA | ai_accelerator | 213.6 |  | 211.449 | 1.0173 | 207.4 | 205.01 | 0.1639 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.58 |  | 558.6982 | 0.3368 | 559.22 | 544.305 | 2.9345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | MU | memory_hbm_storage | 970.285 |  | 968.5252 | 0.1817 | 963.41 | 936.99 | 1.0492 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 421.745 |  | 420.8697 | 0.208 | 419.42 | 414.87 | 0.4149 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | WDC | memory_hbm_storage | 556.995 |  | 556.1888 | 0.145 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ANET | ai_networking_optical | 175.24 |  | 174.9242 | 0.1805 | 175.265 | 171.06 | 3.4353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | APD | industrial_gases | 298.3 |  | 297.828 | 0.1585 | 300.24 | 297.585 | 4.2977 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 553.61 |  | 551.7906 | 0.3297 | 548.755 | 526.6 | 0.4046 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ASML | semiconductor_equipment | 1802.5 |  | 1798.8833 | 0.2011 | 1786.525 | 1767.54 | 0.9026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | PWR | data_center_power_cooling | 644.385 |  | 641.2597 | 0.4874 | 641.19 | 628.17 | 3.6345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 321.195 |  | 319.4 | 0.562 | 317.72 | 311.31 | 4.0443 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | VRT | data_center_power_cooling | 301.58 |  | 299.3383 | 0.7489 | 297.69 | 293.905 | 2.6527 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MKSI | semiconductor_materials | 348.19 |  | 344.576 | 1.0488 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.6 |  | 211.449 | 1.0173 | 207.4 | 205.01 | 0.1639 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.02 |  | 553.385 | 0.8376 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.53 |  | 585.9693 | 0.6077 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.33 |  | 211.4211 | 0.4299 | 207.06 | 202.18 | 0.3061 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 216.165 |  | 216.1344 | 0.0141 | 215.465 | 210.975 | 0.037 | buy_precheck_manual_confirm | none |
| 6 | STX | memory_hbm_storage | 907.52 |  | 909.605 | -0.2292 | 899.59 | 860.605 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | QQQ | market_regime | 706.87 |  | 707.4825 | -0.0866 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 748.24 |  | 748.5231 | -0.0378 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 9 | TER | semiconductor_test_packaging | 371.42 |  | 371.6677 | -0.0667 | 369.53 | 365 | 0.665 | below_vwap | below_vwap,spread_too_wide |
| 10 | DELL | ai_server_oem | 439.985 |  | 442.4348 | -0.5537 | 435.98 | 415.79 | 0.5341 | below_vwap | below_vwap,spread_too_wide |
| 11 | AMKR | semiconductor_test_packaging | 67.32 |  | 67.4751 | -0.2299 | 66.73 | 64.98 | 2.4064 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMCI | ai_server_oem | 30.975 |  | 31.1644 | -0.6079 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| 13 | MU | memory_hbm_storage | 970.285 |  | 968.5252 | 0.1817 | 963.41 | 936.99 | 1.0492 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 421.745 |  | 420.8697 | 0.208 | 419.42 | 414.87 | 0.4149 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 553.61 |  | 551.7906 | 0.3297 | 548.755 | 526.6 | 0.4046 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 474.935 |  | 473.812 | 0.237 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1598.175 |  | 1581.17 | 1.0755 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 556.995 |  | 556.1888 | 0.145 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 396.75 |  | 391.5667 | 1.3237 | 387.635 | 380.205 | 1.0032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TQQQ | leveraged_tool | 70.76 |  | 70.8642 | -0.1471 | 70.43 | 69.81 | 0.0283 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.87 |  | 707.4825 | -0.0866 | 705.86 | 703.63 | 0.0099 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.76 |  | 70.8642 | -0.1471 | 70.43 | 69.81 | 0.0283 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.6 |  | 211.449 | 1.0173 | 207.4 | 205.01 | 0.1639 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.74 |  | 389.9437 | -0.5651 | 400.89 | 392.26 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.915 |  | 325.0223 | -0.3407 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.325 |  | 347.8692 | -0.4439 | 348.76 | 346.23 | 0.026 | below_vwap | below_vwap |
| AMD | ai_accelerator | 553.61 |  | 551.7906 | 0.3297 | 548.755 | 526.6 | 0.4046 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.745 |  | 420.8697 | 0.208 | 419.42 | 414.87 | 0.4149 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.02 |  | 553.385 | 0.8376 | 551.02 | 540.105 | 0.0358 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.53 |  | 585.9693 | 0.6077 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.75 |  | 391.5667 | 1.3237 | 387.635 | 380.205 | 1.0032 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 970.285 |  | 968.5252 | 0.1817 | 963.41 | 936.99 | 1.0492 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.33 |  | 211.4211 | 0.4299 | 207.06 | 202.18 | 0.3061 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 439.985 |  | 442.4348 | -0.5537 | 435.98 | 415.79 | 0.5341 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.5 |  | 49.0027 | -1.0258 | 48.96 | 47.01 | 0.0412 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.975 |  | 31.1644 | -0.6079 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 748.24 |  | 748.5231 | -0.0378 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 294.29 |  | 295.0228 | -0.2484 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.87 |  | 126.5833 | -1.3535 | 128.79 | 125.83 | 3.0992 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.57 |  | 83.4476 | -1.0517 | 83.22 | 79.6 | 3.0156 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.58 |  | 299.3383 | 0.7489 | 297.69 | 293.905 | 2.6527 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.675 |  | 407.8821 | -0.0508 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.385 |  | 641.2597 | 0.4874 | 641.19 | 628.17 | 3.6345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 992.74 |  | 1005.3359 | -1.2529 | 1036.605 | 998.94 | 1.4173 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.935 |  | 473.812 | 0.237 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.27 |  | 142.956 | 0.2197 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.24 |  | 174.9242 | 0.1805 | 175.265 | 171.06 | 3.4353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.605 |  | 316.0772 | -0.4658 | 317.93 | 306.89 | 2.8734 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 826.2 |  | 838.7988 | -1.502 | 840.47 | 814.62 | 4.8414 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.285 |  | 405.421 | -0.7735 | 407.12 | 397.835 | 0.4698 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.36 |  | 114.2105 | -2.4958 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.235 |  | 329.7688 | 0.4446 | 322.67 | 307.545 | 4.6372 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1802.5 |  | 1798.8833 | 0.2011 | 1786.525 | 1767.54 | 0.9026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.58 |  | 558.6982 | 0.3368 | 559.22 | 544.305 | 2.9345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.195 |  | 319.4 | 0.562 | 317.72 | 311.31 | 4.0443 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.165 |  | 216.1344 | 0.0141 | 215.465 | 210.975 | 0.037 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 371.42 |  | 371.6677 | -0.0667 | 369.53 | 365 | 0.665 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 295.41 |  | 295.369 | 0.0139 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.32 |  | 67.4751 | -0.2299 | 66.73 | 64.98 | 2.4064 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.425 |  | 55.6716 | -0.4429 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.77 |  | 138.8735 | -0.0745 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 348.19 |  | 344.576 | 1.0488 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.11 |  | 507.3339 | 0.5472 | 507.545 | 505.59 | 4.2246 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| APD | industrial_gases | 298.3 |  | 297.828 | 0.1585 | 300.24 | 297.585 | 4.2977 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 30.11 |  | 30.7248 | -2.0008 | 30.78 | 29.46 | 0.0664 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.55 |  | 42.5542 | -2.3598 | 42.29 | 40.305 | 0.0481 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.62 |  | 24.0222 | -1.6742 | 24.255 | 23.58 | 0.0423 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1598.175 |  | 1581.17 | 1.0755 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 556.995 |  | 556.1888 | 0.145 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 907.52 |  | 909.605 | -0.2292 | 899.59 | 860.605 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 242.7 |  | 244.2397 | -0.6304 | 248.43 | 244.47 | 0.0824 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.07 |  | 630.695 | -0.7333 | 647.02 | 632.77 | 0.0623 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.86 |  | 285.6044 | -0.2607 | 286.39 | 280.275 | 2.9664 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.47 |  | 166.7402 | -0.1621 | 166.63 | 162.08 | 0.2463 | below_vwap | below_vwap |
