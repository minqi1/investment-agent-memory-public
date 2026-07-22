# Intraday State

- Generated at: `2026-07-23T03:15:09+08:00`
- Market time ET: `2026-07-22T15:15:10-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 25, 'manual_confirm_candidate': 8, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 12, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.78 |  | 707.4482 | -0.0945 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.945 |  | 554.0367 | 0.7054 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.38 |  | 586.5989 | 0.4741 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.93 |  | 748.4987 | -0.076 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.465 |  | 211.6345 | 0.8649 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 557.945 |  | 554.0367 | 0.7054 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.38 |  | 586.5989 | 0.4741 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1801.53 |  | 1799.188 | 0.1302 | 1786.525 | 1767.54 | 0.0416 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 559.27 |  | 558.8362 | 0.0776 | 559.22 | 544.305 | 0.1591 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 175.325 |  | 174.9593 | 0.209 | 175.265 | 171.06 | 0.1426 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 302.67 |  | 299.7 | 0.991 | 297.69 | 293.905 | 0.261 | buy_precheck_manual_confirm | none |
| 8 | DELL | ai_server_oem | 442.8 |  | 442.3559 | 0.1004 | 435.98 | 415.79 | 0.332 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 175.325 |  | 174.9593 | 0.209 | 175.265 | 171.06 | 0.1426 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 559.27 |  | 558.8362 | 0.0776 | 559.22 | 544.305 | 0.1591 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1801.53 |  | 1799.188 | 0.1302 | 1786.525 | 1767.54 | 0.0416 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 244.51 |  | 244.1945 | 0.1292 | 248.43 | 244.47 | 0.0164 | watch_only | none |
| 5 | SOXX | semiconductor_index | 557.945 |  | 554.0367 | 0.7054 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 589.38 |  | 586.5989 | 0.4741 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 7 | DELL | ai_server_oem | 442.8 |  | 442.3559 | 0.1004 | 435.98 | 415.79 | 0.332 | buy_precheck_manual_confirm | none |
| 8 | LIN | industrial_gases | 509.08 |  | 507.4571 | 0.3198 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.465 |  | 211.6345 | 0.8649 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 10 | LRCX | semiconductor_equipment | 320.24 |  | 319.5696 | 0.2098 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 296.01 |  | 295.3972 | 0.2074 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | VRT | data_center_power_cooling | 302.67 |  | 299.7 | 0.991 | 297.69 | 293.905 | 0.261 | buy_precheck_manual_confirm | none |
| 13 | PWR | data_center_power_cooling | 644.235 |  | 641.6287 | 0.4062 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | MKSI | semiconductor_materials | 347.22 |  | 345.507 | 0.4958 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 556.34 |  | 556.2519 | 0.0158 | 548.14 | 526.22 | 1.7076 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TSM | foundry | 422.69 |  | 421.0597 | 0.3872 | 419.42 | 414.87 | 0.9132 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 211.91 |  | 211.5362 | 0.1767 | 207.06 | 202.18 | 1.4251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ALAB | ai_networking_optical | 330.38 |  | 329.9271 | 0.1373 | 322.67 | 307.545 | 4.6462 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 555.77 |  | 552.4914 | 0.5934 | 548.755 | 526.6 | 0.4354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | QQQ | market_regime | 706.78 |  | 707.4482 | -0.0945 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.465 |  | 211.6345 | 0.8649 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 557.945 |  | 554.0367 | 0.7054 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.38 |  | 586.5989 | 0.4741 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1801.53 |  | 1799.188 | 0.1302 | 1786.525 | 1767.54 | 0.0416 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 559.27 |  | 558.8362 | 0.0776 | 559.22 | 544.305 | 0.1591 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 175.325 |  | 174.9593 | 0.209 | 175.265 | 171.06 | 0.1426 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 302.67 |  | 299.7 | 0.991 | 297.69 | 293.905 | 0.261 | buy_precheck_manual_confirm | none |
| 8 | DELL | ai_server_oem | 442.8 |  | 442.3559 | 0.1004 | 435.98 | 415.79 | 0.332 | buy_precheck_manual_confirm | none |
| 9 | MU | memory_hbm_storage | 966.54 |  | 968.4634 | -0.1986 | 963.41 | 936.99 | 1.2415 | below_vwap | below_vwap,spread_too_wide |
| 10 | STX | memory_hbm_storage | 907.18 |  | 909.4028 | -0.2444 | 899.59 | 860.605 | 1.4121 | below_vwap | below_vwap,spread_too_wide |
| 11 | QQQ | market_regime | 706.78 |  | 707.4482 | -0.0945 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 747.93 |  | 748.4987 | -0.076 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 13 | TER | semiconductor_test_packaging | 371.08 |  | 371.6601 | -0.1561 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 216.105 |  | 216.1599 | -0.0254 | 215.465 | 210.975 | 4.3636 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMKR | semiconductor_test_packaging | 67.32 |  | 67.4666 | -0.2173 | 66.73 | 64.98 | 2.347 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMCI | ai_server_oem | 30.715 |  | 31.1468 | -1.3864 | 30.66 | 28.52 | 0.0326 | below_vwap | below_vwap |
| 17 | TSM | foundry | 422.69 |  | 421.0597 | 0.3872 | 419.42 | 414.87 | 0.9132 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 555.77 |  | 552.4914 | 0.5934 | 548.755 | 526.6 | 0.4354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SNDK | memory_hbm_storage | 1601.525 |  | 1582.4391 | 1.2061 | 1558.88 | 1518.99 | 4.2229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 556.34 |  | 556.2519 | 0.0158 | 548.14 | 526.22 | 1.7076 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.78 |  | 707.4482 | -0.0945 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.72 |  | 70.8592 | -0.1965 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.465 |  | 211.6345 | 0.8649 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.51 |  | 389.7288 | -0.0562 | 400.89 | 392.26 | 0.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.35 |  | 324.9531 | -0.1856 | 328.865 | 325.74 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 345.87 |  | 347.6116 | -0.501 | 348.76 | 346.23 | 0.0289 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 555.77 |  | 552.4914 | 0.5934 | 548.755 | 526.6 | 0.4354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.69 |  | 421.0597 | 0.3872 | 419.42 | 414.87 | 0.9132 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.945 |  | 554.0367 | 0.7054 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.38 |  | 586.5989 | 0.4741 | 581.9 | 572.01 | 0.0458 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.32 |  | 392.0639 | 1.3406 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 966.54 |  | 968.4634 | -0.1986 | 963.41 | 936.99 | 1.2415 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 211.91 |  | 211.5362 | 0.1767 | 207.06 | 202.18 | 1.4251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 442.8 |  | 442.3559 | 0.1004 | 435.98 | 415.79 | 0.332 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 48.325 |  | 48.9271 | -1.2306 | 48.96 | 47.01 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.715 |  | 31.1468 | -1.3864 | 30.66 | 28.52 | 0.0326 | below_vwap | below_vwap |
| SPY | market_regime | 747.93 |  | 748.4987 | -0.076 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.62 |  | 294.918 | -0.4401 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.19 |  | 126.4605 | -0.2139 | 128.79 | 125.83 | 1.9891 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.185 |  | 83.345 | -0.1919 | 83.22 | 79.6 | 4.3998 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.67 |  | 299.7 | 0.991 | 297.69 | 293.905 | 0.261 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 405.93 |  | 407.7027 | -0.4348 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.235 |  | 641.6287 | 0.4062 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 991.7 |  | 1004.2279 | -1.2475 | 1036.605 | 998.94 | 1.6739 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.335 |  | 473.8695 | -0.1128 | 473.865 | 466.83 | 0.0676 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 142.38 |  | 142.9057 | -0.3679 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.325 |  | 174.9593 | 0.209 | 175.265 | 171.06 | 0.1426 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 315.04 |  | 316.0138 | -0.3082 | 317.93 | 306.89 | 2.6409 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 829.78 |  | 837.9322 | -0.9729 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 401.11 |  | 405.0251 | -0.9666 | 407.12 | 397.835 | 1.628 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.68 |  | 113.9807 | -2.8959 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.38 |  | 329.9271 | 0.1373 | 322.67 | 307.545 | 4.6462 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1801.53 |  | 1799.188 | 0.1302 | 1786.525 | 1767.54 | 0.0416 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.27 |  | 558.8362 | 0.0776 | 559.22 | 544.305 | 0.1591 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.24 |  | 319.5696 | 0.2098 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.105 |  | 216.1599 | -0.0254 | 215.465 | 210.975 | 4.3636 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.08 |  | 371.6601 | -0.1561 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.01 |  | 295.3972 | 0.2074 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.32 |  | 67.4666 | -0.2173 | 66.73 | 64.98 | 2.347 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.325 |  | 55.6172 | -0.5254 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.81 |  | 138.8603 | -0.0362 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 347.22 |  | 345.507 | 0.4958 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.08 |  | 507.4571 | 0.3198 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.03 |  | 297.8001 | -0.2586 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.96 |  | 30.6676 | -2.3072 | 30.78 | 29.46 | 0.0334 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.39 |  | 42.4546 | -2.5077 | 42.29 | 40.305 | 0.0242 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.56 |  | 23.9824 | -1.7611 | 24.255 | 23.58 | 0.0849 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1601.525 |  | 1582.4391 | 1.2061 | 1558.88 | 1518.99 | 4.2229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 556.34 |  | 556.2519 | 0.0158 | 548.14 | 526.22 | 1.7076 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 907.18 |  | 909.4028 | -0.2444 | 899.59 | 860.605 | 1.4121 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 244.51 |  | 244.1945 | 0.1292 | 248.43 | 244.47 | 0.0164 | watch_only | none |
| META | cloud_ai_capex | 626.74 |  | 630.2239 | -0.5528 | 647.02 | 632.77 | 0.083 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.43 |  | 285.5797 | -0.0524 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 165.88 |  | 166.7307 | -0.5102 | 166.63 | 162.08 | 1.2057 | below_vwap | below_vwap,spread_too_wide |
