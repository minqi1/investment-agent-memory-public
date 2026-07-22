# Intraday State

- Generated at: `2026-07-23T02:01:56+08:00`
- Market time ET: `2026-07-22T14:01:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_opening_15m_low': 8, 'below_vwap': 17, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.64 |  | 707.5056 | 0.019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.6 |  | 553.2424 | 0.9684 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.32 |  | 585.7513 | 0.78 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.68 |  | 748.5384 | 0.0189 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.79 |  | 211.3658 | 1.1469 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 912.25 |  | 909.2853 | 0.3261 | 899.59 | 860.605 | 0.2335 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.6 |  | 553.2424 | 0.9684 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.32 |  | 585.7513 | 0.78 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.285 |  | 211.3518 | 0.9147 | 207.06 | 202.18 | 0.1594 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 707.64 |  | 707.5056 | 0.019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 748.68 |  | 748.5384 | 0.0189 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1803.29 |  | 1798.6267 | 0.2593 | 1786.525 | 1767.54 | 0.1142 | buy_precheck_manual_confirm | none |
| 9 | LIN | industrial_gases | 509.93 |  | 507.3094 | 0.5166 | 507.545 | 505.59 | 0.0569 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 70.985 |  | 70.8649 | 0.1695 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.64 |  | 707.5056 | 0.019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.68 |  | 748.5384 | 0.0189 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1803.29 |  | 1798.6267 | 0.2593 | 1786.525 | 1767.54 | 0.1142 | buy_precheck_manual_confirm | none |
| 4 | STX | memory_hbm_storage | 912.25 |  | 909.2853 | 0.3261 | 899.59 | 860.605 | 0.2335 | buy_precheck_manual_confirm | none |
| 5 | LIN | industrial_gases | 509.93 |  | 507.3094 | 0.5166 | 507.545 | 505.59 | 0.0569 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 590.32 |  | 585.7513 | 0.78 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| 7 | ENTG | semiconductor_materials | 139.23 |  | 138.8636 | 0.2638 | 140.09 | 135.555 | 0.2298 | watch_only | none |
| 8 | SOXX | semiconductor_index | 558.6 |  | 553.2424 | 0.9684 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.35 |  | 174.8931 | 0.2613 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 143.32 |  | 142.9168 | 0.2821 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | NVDA | ai_accelerator | 213.79 |  | 211.3658 | 1.1469 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 12 | ONTO | semiconductor_test_packaging | 295.58 |  | 295.3654 | 0.0726 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 298.53 |  | 297.8161 | 0.2397 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | MRVL | custom_silicon_networking | 213.285 |  | 211.3518 | 0.9147 | 207.06 | 202.18 | 0.1594 | buy_precheck_manual_confirm | none |
| 15 | TSM | foundry | 421.48 |  | 420.8074 | 0.1598 | 419.42 | 414.87 | 1.0677 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | KLAC | semiconductor_equipment | 216.62 |  | 216.1143 | 0.234 | 215.465 | 210.975 | 4.2101 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | PWR | data_center_power_cooling | 643.48 |  | 640.8703 | 0.4072 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | LRCX | semiconductor_equipment | 321.28 |  | 319.1471 | 0.6683 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMAT | semiconductor_equipment | 561.13 |  | 558.5558 | 0.4609 | 559.22 | 544.305 | 3.0064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 475.96 |  | 473.7462 | 0.4673 | 473.865 | 466.83 | 0.6156 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.79 |  | 211.3658 | 1.1469 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 912.25 |  | 909.2853 | 0.3261 | 899.59 | 860.605 | 0.2335 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.6 |  | 553.2424 | 0.9684 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.32 |  | 585.7513 | 0.78 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.285 |  | 211.3518 | 0.9147 | 207.06 | 202.18 | 0.1594 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 707.64 |  | 707.5056 | 0.019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 748.68 |  | 748.5384 | 0.0189 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1803.29 |  | 1798.6267 | 0.2593 | 1786.525 | 1767.54 | 0.1142 | buy_precheck_manual_confirm | none |
| 9 | LIN | industrial_gases | 509.93 |  | 507.3094 | 0.5166 | 507.545 | 505.59 | 0.0569 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 70.985 |  | 70.8649 | 0.1695 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 11 | DELL | ai_server_oem | 441.17 |  | 442.5703 | -0.3164 | 435.98 | 415.79 | 0.3967 | below_vwap | below_vwap,spread_too_wide |
| 12 | AMKR | semiconductor_test_packaging | 67.385 |  | 67.4778 | -0.1375 | 66.73 | 64.98 | 0.1484 | below_vwap | below_vwap |
| 13 | SMCI | ai_server_oem | 30.975 |  | 31.1768 | -0.6471 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| 14 | MU | memory_hbm_storage | 974.39 |  | 968.3229 | 0.6266 | 963.41 | 936.99 | 0.9493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 421.48 |  | 420.8074 | 0.1598 | 419.42 | 414.87 | 1.0677 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 555.615 |  | 551.7036 | 0.709 | 548.755 | 526.6 | 1.9744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 475.96 |  | 473.7462 | 0.4673 | 473.865 | 466.83 | 0.6156 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SNDK | memory_hbm_storage | 1607.5 |  | 1580.1933 | 1.7281 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 557.89 |  | 556.0697 | 0.3274 | 548.14 | 526.22 | 0.8102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 373.38 |  | 371.6403 | 0.4681 | 369.53 | 365 | 4.9306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.64 |  | 707.5056 | 0.019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 70.985 |  | 70.8649 | 0.1695 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.79 |  | 211.3658 | 1.1469 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.23 |  | 390.1203 | -0.7409 | 400.89 | 392.26 | 0.0336 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.92 |  | 325.0625 | -0.3515 | 328.865 | 325.74 | 0.0185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.05 |  | 347.941 | -0.2561 | 348.76 | 346.23 | 0.0202 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555.615 |  | 551.7036 | 0.709 | 548.755 | 526.6 | 1.9744 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.48 |  | 420.8074 | 0.1598 | 419.42 | 414.87 | 1.0677 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.6 |  | 553.2424 | 0.9684 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.32 |  | 585.7513 | 0.78 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.51 |  | 391.1934 | 1.3591 | 387.635 | 380.205 | 0.9735 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 974.39 |  | 968.3229 | 0.6266 | 963.41 | 936.99 | 0.9493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.285 |  | 211.3518 | 0.9147 | 207.06 | 202.18 | 0.1594 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 441.17 |  | 442.5703 | -0.3164 | 435.98 | 415.79 | 0.3967 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.83 |  | 49.0216 | -0.3908 | 48.96 | 47.01 | 0.0614 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.975 |  | 31.1768 | -0.6471 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 748.68 |  | 748.5384 | 0.0189 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.455 |  | 295.096 | -0.2172 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.49 |  | 126.6276 | -0.8984 | 128.79 | 125.83 | 0.0717 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.83 |  | 83.5087 | -0.8128 | 83.22 | 79.6 | 0.1207 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 301.73 |  | 299.2012 | 0.8452 | 297.69 | 293.905 | 2.6514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.8 |  | 407.9172 | -0.0287 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.48 |  | 640.8703 | 0.4072 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 992.54 |  | 1006.1749 | -1.3551 | 1036.605 | 998.94 | 2.0785 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.96 |  | 473.7462 | 0.4673 | 473.865 | 466.83 | 0.6156 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 143.32 |  | 142.9168 | 0.2821 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.35 |  | 174.8931 | 0.2613 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 315.01 |  | 316.1205 | -0.3513 | 317.93 | 306.89 | 2.7396 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 829.08 |  | 839.482 | -1.2391 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.14 |  | 405.5829 | -0.8489 | 407.12 | 397.835 | 1.9222 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.24 |  | 114.3181 | -2.6925 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.3 |  | 329.6029 | 0.8183 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1803.29 |  | 1798.6267 | 0.2593 | 1786.525 | 1767.54 | 0.1142 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 561.13 |  | 558.5558 | 0.4609 | 559.22 | 544.305 | 3.0064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.28 |  | 319.1471 | 0.6683 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.62 |  | 216.1143 | 0.234 | 215.465 | 210.975 | 4.2101 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373.38 |  | 371.6403 | 0.4681 | 369.53 | 365 | 4.9306 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.58 |  | 295.3654 | 0.0726 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.385 |  | 67.4778 | -0.1375 | 66.73 | 64.98 | 0.1484 | below_vwap | below_vwap |
| COHU | semiconductor_test_packaging | 55.6 |  | 55.6847 | -0.1521 | 56.2 | 54.45 | 0.5396 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 139.23 |  | 138.8636 | 0.2638 | 140.09 | 135.555 | 0.2298 | watch_only | none |
| MKSI | semiconductor_materials | 347.5 |  | 344.3997 | 0.9002 | 345.675 | 331.945 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 509.93 |  | 507.3094 | 0.5166 | 507.545 | 505.59 | 0.0569 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 298.53 |  | 297.8161 | 0.2397 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.25 |  | 30.7478 | -1.6189 | 30.78 | 29.46 | 0.0992 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.72 |  | 42.5971 | -2.0592 | 42.29 | 40.305 | 0.0719 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.75 |  | 24.0959 | -1.4353 | 24.255 | 23.58 | 0.0842 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1607.5 |  | 1580.1933 | 1.7281 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 557.89 |  | 556.0697 | 0.3274 | 548.14 | 526.22 | 0.8102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 912.25 |  | 909.2853 | 0.3261 | 899.59 | 860.605 | 0.2335 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 242.59 |  | 244.3329 | -0.7133 | 248.43 | 244.47 | 0.0206 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 625.56 |  | 630.8608 | -0.8403 | 647.02 | 632.77 | 0.2126 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.26 |  | 285.6558 | -0.1386 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.16 |  | 166.8001 | -0.3838 | 166.63 | 162.08 | 2.287 | below_vwap | below_vwap,spread_too_wide |
