# Intraday State

- Generated at: `2026-07-23T01:45:44+08:00`
- Market time ET: `2026-07-22T13:45:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 7, 'below_vwap': 13, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.525 |  | 707.4951 | 0.1456 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.88 |  | 553.1039 | 1.2251 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.13 |  | 585.6587 | 0.9342 | 581.9 | 572.01 | 0.0338 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.13 |  | 748.5309 | 0.08 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.84 |  | 211.2927 | 1.2056 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1620.535 |  | 1579.4988 | 2.598 | 1558.88 | 1518.99 | 0.3425 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 559.065 |  | 556.0165 | 0.5483 | 548.14 | 526.22 | 0.1073 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.88 |  | 553.1039 | 1.2251 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.13 |  | 585.6587 | 0.9342 | 581.9 | 572.01 | 0.0338 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.525 |  | 707.4951 | 0.1456 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.13 |  | 748.5309 | 0.08 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.735 |  | 216.104 | 0.292 | 215.465 | 210.975 | 0.0554 | buy_precheck_manual_confirm | none |
| 9 | DELL | ai_server_oem | 443.92 |  | 442.7369 | 0.2672 | 435.98 | 415.79 | 0.1532 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.245 |  | 31.1808 | 0.2058 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.23 |  | 70.8588 | 0.5238 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.13 |  | 748.5309 | 0.08 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.525 |  | 707.4951 | 0.1456 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.735 |  | 216.104 | 0.292 | 215.465 | 210.975 | 0.0554 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 31.245 |  | 31.1808 | 0.2058 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 5 | DELL | ai_server_oem | 443.92 |  | 442.7369 | 0.2672 | 435.98 | 415.79 | 0.1532 | buy_precheck_manual_confirm | none |
| 6 | WDC | memory_hbm_storage | 559.065 |  | 556.0165 | 0.5483 | 548.14 | 526.22 | 0.1073 | buy_precheck_manual_confirm | none |
| 7 | NVDA | ai_accelerator | 213.84 |  | 211.2927 | 1.2056 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 8 | ENTG | semiconductor_materials | 139.295 |  | 138.8318 | 0.3336 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ONTO | semiconductor_test_packaging | 295.92 |  | 295.3654 | 0.1878 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | APD | industrial_gases | 298.2 |  | 297.7762 | 0.1423 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 559.88 |  | 553.1039 | 1.2251 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| 12 | SMH | semiconductor_index | 591.13 |  | 585.6587 | 0.9342 | 581.9 | 572.01 | 0.0338 | buy_precheck_manual_confirm | none |
| 13 | AMAT | semiconductor_equipment | 559.81 |  | 558.5107 | 0.2326 | 559.22 | 544.305 | 2.3651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SKHY | memory_hbm_storage | 166.87 |  | 166.8051 | 0.0389 | 166.63 | 162.08 | 2.481 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | ANET | ai_networking_optical | 175.29 |  | 174.8811 | 0.2338 | 175.265 | 171.06 | 2.6699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 475.655 |  | 473.7109 | 0.4104 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ARM | ai_accelerator | 285.67 |  | 285.6618 | 0.0029 | 286.39 | 280.275 | 2.8249 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LIN | industrial_gases | 509.72 |  | 507.261 | 0.4848 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 143.04 |  | 142.9065 | 0.0934 | 143.27 | 141.04 | 4.9147 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | PWR | data_center_power_cooling | 643.575 |  | 640.7617 | 0.4391 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.84 |  | 211.2927 | 1.2056 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1620.535 |  | 1579.4988 | 2.598 | 1558.88 | 1518.99 | 0.3425 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 559.065 |  | 556.0165 | 0.5483 | 548.14 | 526.22 | 0.1073 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.88 |  | 553.1039 | 1.2251 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.13 |  | 585.6587 | 0.9342 | 581.9 | 572.01 | 0.0338 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.525 |  | 707.4951 | 0.1456 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.13 |  | 748.5309 | 0.08 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.735 |  | 216.104 | 0.292 | 215.465 | 210.975 | 0.0554 | buy_precheck_manual_confirm | none |
| 9 | DELL | ai_server_oem | 443.92 |  | 442.7369 | 0.2672 | 435.98 | 415.79 | 0.1532 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.245 |  | 31.1808 | 0.2058 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.23 |  | 70.8588 | 0.5238 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 49.01 |  | 49.0269 | -0.0345 | 48.96 | 47.01 | 0.0408 | below_vwap | below_vwap |
| 13 | CRWV | gpu_cloud_ai_factory | 83.48 |  | 83.5235 | -0.0521 | 83.22 | 79.6 | 0.3713 | below_vwap | below_vwap,spread_too_wide |
| 14 | MU | memory_hbm_storage | 976.79 |  | 968.0752 | 0.9002 | 963.41 | 936.99 | 0.9593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 422.635 |  | 420.7911 | 0.4382 | 419.42 | 414.87 | 1.0647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 556.62 |  | 551.5633 | 0.9168 | 548.755 | 526.6 | 0.7743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 475.655 |  | 473.7109 | 0.4104 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 914.31 |  | 909.088 | 0.5744 | 899.59 | 860.605 | 0.864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 213.525 |  | 211.2817 | 1.0618 | 207.06 | 202.18 | 0.5479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 373.15 |  | 371.6067 | 0.4153 | 369.53 | 365 | 4.7729 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.525 |  | 707.4951 | 0.1456 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.23 |  | 70.8588 | 0.5238 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.84 |  | 211.2927 | 1.2056 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.76 |  | 390.2148 | -0.6291 | 400.89 | 392.26 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.89 |  | 325.0827 | -0.3669 | 328.865 | 325.74 | 0.2316 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.88 |  | 347.9664 | -0.0248 | 348.76 | 346.23 | 0.1696 | below_vwap | below_vwap |
| AMD | ai_accelerator | 556.62 |  | 551.5633 | 0.9168 | 548.755 | 526.6 | 0.7743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.635 |  | 420.7911 | 0.4382 | 419.42 | 414.87 | 1.0647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.88 |  | 553.1039 | 1.2251 | 551.02 | 540.105 | 0.0518 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.13 |  | 585.6587 | 0.9342 | 581.9 | 572.01 | 0.0338 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.79 |  | 390.3455 | 1.651 | 387.635 | 380.205 | 0.6931 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 976.79 |  | 968.0752 | 0.9002 | 963.41 | 936.99 | 0.9593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.525 |  | 211.2817 | 1.0618 | 207.06 | 202.18 | 0.5479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.92 |  | 442.7369 | 0.2672 | 435.98 | 415.79 | 0.1532 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 49.01 |  | 49.0269 | -0.0345 | 48.96 | 47.01 | 0.0408 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.245 |  | 31.1808 | 0.2058 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.13 |  | 748.5309 | 0.08 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.49 |  | 295.1109 | -0.2104 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.12 |  | 126.6621 | -0.428 | 128.79 | 125.83 | 2.0932 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.48 |  | 83.5235 | -0.0521 | 83.22 | 79.6 | 0.3713 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.16 |  | 299.09 | 0.6921 | 297.69 | 293.905 | 1.2153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.34 |  | 407.9246 | -0.1433 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.575 |  | 640.7617 | 0.4391 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 989.19 |  | 1006.9695 | -1.7656 | 1036.605 | 998.94 | 3.6201 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.655 |  | 473.7109 | 0.4104 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.04 |  | 142.9065 | 0.0934 | 143.27 | 141.04 | 4.9147 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.29 |  | 174.8811 | 0.2338 | 175.265 | 171.06 | 2.6699 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.485 |  | 316.1435 | -0.5246 | 317.93 | 306.89 | 3.0431 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 828.11 |  | 840.0323 | -1.4193 | 840.47 | 814.62 | 0.4975 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.55 |  | 405.6836 | -0.7724 | 407.12 | 397.835 | 1.9675 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.17 |  | 114.4043 | -2.8271 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.72 |  | 329.5576 | 1.263 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1809.105 |  | 1798.2819 | 0.6019 | 1786.525 | 1767.54 | 1.4587 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 559.81 |  | 558.5107 | 0.2326 | 559.22 | 544.305 | 2.3651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.08 |  | 319.076 | 0.6281 | 317.72 | 311.31 | 3.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.735 |  | 216.104 | 0.292 | 215.465 | 210.975 | 0.0554 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 373.15 |  | 371.6067 | 0.4153 | 369.53 | 365 | 4.7729 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.92 |  | 295.3654 | 0.1878 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.55 |  | 67.4782 | 0.1064 | 66.73 | 64.98 | 1.9245 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.665 |  | 55.6941 | -0.0523 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.295 |  | 138.8318 | 0.3336 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 348.16 |  | 344.2749 | 1.1285 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.72 |  | 507.261 | 0.4848 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.2 |  | 297.7762 | 0.1423 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.38 |  | 30.7598 | -1.2348 | 30.78 | 29.46 | 0.0658 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.03 |  | 42.6325 | -1.4131 | 42.29 | 40.305 | 0.0476 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.82 |  | 24.1097 | -1.2017 | 24.255 | 23.58 | 0.042 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1620.535 |  | 1579.4988 | 2.598 | 1558.88 | 1518.99 | 0.3425 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 559.065 |  | 556.0165 | 0.5483 | 548.14 | 526.22 | 0.1073 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 914.31 |  | 909.088 | 0.5744 | 899.59 | 860.605 | 0.864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.02 |  | 244.4018 | -0.5654 | 248.43 | 244.47 | 0.0206 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 627.195 |  | 630.9852 | -0.6007 | 647.02 | 632.77 | 1.148 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.67 |  | 285.6618 | 0.0029 | 286.39 | 280.275 | 2.8249 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.87 |  | 166.8051 | 0.0389 | 166.63 | 162.08 | 2.481 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
