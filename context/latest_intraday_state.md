# Intraday State

- Generated at: `2026-07-23T01:37:44+08:00`
- Market time ET: `2026-07-22T13:37:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'below_opening_15m_low': 7, 'watch_only': 2, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 3, 'below_vwap': 11}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.56 |  | 707.4816 | 0.1524 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.79 |  | 553.0637 | 1.2162 | 551.02 | 540.105 | 0.0679 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.69 |  | 585.6266 | 0.8646 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.08 |  | 748.5161 | 0.0753 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.06 |  | 211.2273 | 1.3411 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.79 |  | 553.0637 | 1.2162 | 551.02 | 540.105 | 0.0679 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.69 |  | 585.6266 | 0.8646 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.56 |  | 707.4816 | 0.1524 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 749.08 |  | 748.5161 | 0.0753 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.064 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 71.245 |  | 70.8546 | 0.5509 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.08 |  | 748.5161 | 0.0753 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.56 |  | 707.4816 | 0.1524 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 347.99 |  | 347.9611 | 0.0083 | 348.76 | 346.23 | 0.0144 | watch_only | none |
| 4 | SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.064 | buy_precheck_manual_confirm | none |
| 5 | APD | industrial_gases | 298 |  | 297.7616 | 0.0801 | 300.24 | 297.585 | 0.1544 | watch_only | none |
| 6 | NVDA | ai_accelerator | 214.06 |  | 211.2273 | 1.3411 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 7 | ARM | ai_accelerator | 286.02 |  | 285.6613 | 0.1256 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 143.1 |  | 142.906 | 0.1358 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ONTO | semiconductor_test_packaging | 295.845 |  | 295.3619 | 0.1636 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SOXX | semiconductor_index | 559.79 |  | 553.0637 | 1.2162 | 551.02 | 540.105 | 0.0679 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 590.69 |  | 585.6266 | 0.8646 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 12 | AMAT | semiconductor_equipment | 559.925 |  | 558.4846 | 0.2579 | 559.22 | 544.305 | 2.3646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SKHY | memory_hbm_storage | 166.91 |  | 166.8042 | 0.0634 | 166.63 | 162.08 | 2.4804 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | PWR | data_center_power_cooling | 643.33 |  | 640.6651 | 0.416 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TT | data_center_power_cooling | 475.715 |  | 473.6842 | 0.4287 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 216.465 |  | 216.0966 | 0.1705 | 215.465 | 210.975 | 4.1762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ANET | ai_networking_optical | 174.975 |  | 174.8694 | 0.0604 | 175.265 | 171.06 | 2.909 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ENTG | semiconductor_materials | 139.27 |  | 138.7774 | 0.355 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TER | semiconductor_test_packaging | 372.72 |  | 371.5843 | 0.3056 | 369.53 | 365 | 4.9394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMKR | semiconductor_test_packaging | 67.53 |  | 67.4778 | 0.0774 | 66.73 | 64.98 | 1.9251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.06 |  | 211.2273 | 1.3411 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.79 |  | 553.0637 | 1.2162 | 551.02 | 540.105 | 0.0679 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.69 |  | 585.6266 | 0.8646 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.56 |  | 707.4816 | 0.1524 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 749.08 |  | 748.5161 | 0.0753 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.064 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 71.245 |  | 70.8546 | 0.5509 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 8 | MU | memory_hbm_storage | 976.98 |  | 967.98 | 0.9298 | 963.41 | 936.99 | 1.2283 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | TSM | foundry | 422.26 |  | 420.7373 | 0.3619 | 419.42 | 414.87 | 0.9591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | AMD | ai_accelerator | 556.53 |  | 551.5221 | 0.908 | 548.755 | 526.6 | 2.7797 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TT | data_center_power_cooling | 475.715 |  | 473.6842 | 0.4287 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SNDK | memory_hbm_storage | 1621 |  | 1579.1336 | 2.6512 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | WDC | memory_hbm_storage | 559.785 |  | 555.9172 | 0.6958 | 548.14 | 526.22 | 0.3894 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | STX | memory_hbm_storage | 913.4 |  | 908.852 | 0.5004 | 899.59 | 860.605 | 0.9864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MRVL | custom_silicon_networking | 213.625 |  | 211.2349 | 1.1315 | 207.06 | 202.18 | 0.5477 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TER | semiconductor_test_packaging | 372.72 |  | 371.5843 | 0.3056 | 369.53 | 365 | 4.9394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 396.85 |  | 390.2076 | 1.7023 | 387.635 | 380.205 | 0.7534 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ASML | semiconductor_equipment | 1809.435 |  | 1798.0773 | 0.6317 | 1786.525 | 1767.54 | 1.4507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | KLAC | semiconductor_equipment | 216.465 |  | 216.0966 | 0.1705 | 215.465 | 210.975 | 4.1762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMAT | semiconductor_equipment | 559.925 |  | 558.4846 | 0.2579 | 559.22 | 544.305 | 2.3646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.56 |  | 707.4816 | 0.1524 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.245 |  | 70.8546 | 0.5509 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 214.06 |  | 211.2273 | 1.3411 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.705 |  | 390.259 | -0.6544 | 400.89 | 392.26 | 0.4926 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 323.79 |  | 325.1274 | -0.4113 | 328.865 | 325.74 | 0.2162 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.99 |  | 347.9611 | 0.0083 | 348.76 | 346.23 | 0.0144 | watch_only | none |
| AMD | ai_accelerator | 556.53 |  | 551.5221 | 0.908 | 548.755 | 526.6 | 2.7797 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.26 |  | 420.7373 | 0.3619 | 419.42 | 414.87 | 0.9591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.79 |  | 553.0637 | 1.2162 | 551.02 | 540.105 | 0.0679 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.69 |  | 585.6266 | 0.8646 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.85 |  | 390.2076 | 1.7023 | 387.635 | 380.205 | 0.7534 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 976.98 |  | 967.98 | 0.9298 | 963.41 | 936.99 | 1.2283 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.625 |  | 211.2349 | 1.1315 | 207.06 | 202.18 | 0.5477 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.05 |  | 442.7177 | 0.0751 | 435.98 | 415.79 | 1.5867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.88 |  | 49.0277 | -0.3013 | 48.96 | 47.01 | 0.0409 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.23 |  | 31.1803 | 0.1594 | 30.66 | 28.52 | 0.064 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.08 |  | 748.5161 | 0.0753 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.42 |  | 295.128 | -0.2399 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.255 |  | 126.667 | -0.3253 | 128.79 | 125.83 | 0.4039 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.205 |  | 83.5244 | -0.3823 | 83.22 | 79.6 | 4.7713 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.075 |  | 299.0274 | 0.6848 | 297.69 | 293.905 | 0.5447 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.38 |  | 407.9369 | -0.1365 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.33 |  | 640.6651 | 0.416 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 990.81 |  | 1007.2829 | -1.6354 | 1036.605 | 998.94 | 2.1276 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.715 |  | 473.6842 | 0.4287 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.1 |  | 142.906 | 0.1358 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 174.975 |  | 174.8694 | 0.0604 | 175.265 | 171.06 | 2.909 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.58 |  | 316.1512 | -0.497 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 829.36 |  | 840.2233 | -1.2929 | 840.47 | 814.62 | 4.1393 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.09 |  | 405.728 | -0.8967 | 407.12 | 397.835 | 0.5646 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.38 |  | 114.4404 | -2.6743 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.2 |  | 329.484 | 1.1278 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1809.435 |  | 1798.0773 | 0.6317 | 1786.525 | 1767.54 | 1.4507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 559.925 |  | 558.4846 | 0.2579 | 559.22 | 544.305 | 2.3646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.96 |  | 319.0453 | 0.6001 | 317.72 | 311.31 | 0.4206 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.465 |  | 216.0966 | 0.1705 | 215.465 | 210.975 | 4.1762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.72 |  | 371.5843 | 0.3056 | 369.53 | 365 | 4.9394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.845 |  | 295.3619 | 0.1636 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.53 |  | 67.4778 | 0.0774 | 66.73 | 64.98 | 1.9251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 | 0.4118 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| ENTG | semiconductor_materials | 139.27 |  | 138.7774 | 0.355 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346.9 |  | 344.0931 | 0.8157 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.44 |  | 507.2507 | 0.4316 | 507.545 | 505.59 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| APD | industrial_gases | 298 |  | 297.7616 | 0.0801 | 300.24 | 297.585 | 0.1544 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 30.34 |  | 30.7639 | -1.378 | 30.78 | 29.46 | 0.0659 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.13 |  | 42.6427 | -1.2023 | 42.29 | 40.305 | 0.0475 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.82 |  | 24.116 | -1.2274 | 24.255 | 23.58 | 0.1259 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1621 |  | 1579.1336 | 2.6512 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.785 |  | 555.9172 | 0.6958 | 548.14 | 526.22 | 0.3894 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 913.4 |  | 908.852 | 0.5004 | 899.59 | 860.605 | 0.9864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.01 |  | 244.4151 | -0.5749 | 248.43 | 244.47 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 627.235 |  | 631.0345 | -0.6021 | 647.02 | 632.77 | 1.1479 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 286.02 |  | 285.6613 | 0.1256 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 166.91 |  | 166.8042 | 0.0634 | 166.63 | 162.08 | 2.4804 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
