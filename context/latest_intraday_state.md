# Intraday State

- Generated at: `2026-07-23T02:45:55+08:00`
- Market time ET: `2026-07-22T14:45:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 25, 'manual_confirm_candidate': 7, 'below_opening_15m_low': 7, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.91 |  | 707.458 | -0.0775 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.83 |  | 553.6713 | 0.7511 | 551.02 | 540.105 | 0.0466 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.48 |  | 586.1263 | 0.5722 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.33 |  | 748.513 | -0.0245 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.67 |  | 211.5165 | 1.0181 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.75 |  | 420.9367 | 0.1932 | 419.42 | 414.87 | 0.1873 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 556.24 |  | 556.1485 | 0.0164 | 548.14 | 526.22 | 0.1294 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.83 |  | 553.6713 | 0.7511 | 551.02 | 540.105 | 0.0466 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.48 |  | 586.1263 | 0.5722 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.7 |  | 211.4574 | 0.5877 | 207.06 | 202.18 | 0.1693 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 302.59 |  | 299.4863 | 1.0363 | 297.69 | 293.905 | 0.0958 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 421.75 |  | 420.9367 | 0.1932 | 419.42 | 414.87 | 0.1873 | buy_precheck_manual_confirm | none |
| 2 | WDC | memory_hbm_storage | 556.24 |  | 556.1485 | 0.0164 | 548.14 | 526.22 | 0.1294 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 557.83 |  | 553.6713 | 0.7511 | 551.02 | 540.105 | 0.0466 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.48 |  | 586.1263 | 0.5722 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 175.15 |  | 174.9355 | 0.1226 | 175.265 | 171.06 | 0.1941 | watch_only | none |
| 6 | MRVL | custom_silicon_networking | 212.7 |  | 211.4574 | 0.5877 | 207.06 | 202.18 | 0.1693 | buy_precheck_manual_confirm | none |
| 7 | TT | data_center_power_cooling | 475.03 |  | 473.8784 | 0.243 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | NVDA | ai_accelerator | 213.67 |  | 211.5165 | 1.0181 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 9 | JCI | data_center_power_cooling | 143.05 |  | 142.9595 | 0.0633 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ONTO | semiconductor_test_packaging | 295.59 |  | 295.3645 | 0.0763 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | APD | industrial_gases | 298.13 |  | 297.8453 | 0.0956 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | VRT | data_center_power_cooling | 302.59 |  | 299.4863 | 1.0363 | 297.69 | 293.905 | 0.0958 | buy_precheck_manual_confirm | none |
| 13 | KLAC | semiconductor_equipment | 216.165 |  | 216.1325 | 0.015 | 215.465 | 210.975 | 4.3439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMAT | semiconductor_equipment | 560.02 |  | 558.7558 | 0.2263 | 559.22 | 544.305 | 2.991 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | LIN | industrial_gases | 510.36 |  | 507.3673 | 0.5899 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 643.62 |  | 641.3726 | 0.3504 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ASML | semiconductor_equipment | 1802.57 |  | 1799.0009 | 0.1984 | 1786.525 | 1767.54 | 2.6701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ALAB | ai_networking_optical | 331.78 |  | 329.8646 | 0.5807 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMD | ai_accelerator | 555.16 |  | 551.8751 | 0.5952 | 548.755 | 526.6 | 2.0661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | LRCX | semiconductor_equipment | 320.74 |  | 319.4644 | 0.3993 | 317.72 | 311.31 | 4.1467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.67 |  | 211.5165 | 1.0181 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.75 |  | 420.9367 | 0.1932 | 419.42 | 414.87 | 0.1873 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 556.24 |  | 556.1485 | 0.0164 | 548.14 | 526.22 | 0.1294 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.83 |  | 553.6713 | 0.7511 | 551.02 | 540.105 | 0.0466 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.48 |  | 586.1263 | 0.5722 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.7 |  | 211.4574 | 0.5877 | 207.06 | 202.18 | 0.1693 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 302.59 |  | 299.4863 | 1.0363 | 297.69 | 293.905 | 0.0958 | buy_precheck_manual_confirm | none |
| 8 | MU | memory_hbm_storage | 967 |  | 968.4618 | -0.1509 | 963.41 | 936.99 | 2.0683 | below_vwap | below_vwap,spread_too_wide |
| 9 | STX | memory_hbm_storage | 903.08 |  | 909.5584 | -0.7123 | 899.59 | 860.605 | 2.0463 | below_vwap | below_vwap,spread_too_wide |
| 10 | QQQ | market_regime | 706.91 |  | 707.458 | -0.0775 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 748.33 |  | 748.513 | -0.0245 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 12 | TER | semiconductor_test_packaging | 371.26 |  | 371.6522 | -0.1055 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | SKHY | memory_hbm_storage | 166.65 |  | 166.738 | -0.0528 | 166.63 | 162.08 | 0.294 | below_vwap | below_vwap |
| 14 | DELL | ai_server_oem | 440.08 |  | 442.3799 | -0.5199 | 435.98 | 415.79 | 2.3518 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMKR | semiconductor_test_packaging | 67.31 |  | 67.471 | -0.2387 | 66.73 | 64.98 | 2.3325 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMCI | ai_server_oem | 31.02 |  | 31.1584 | -0.4442 | 30.66 | 28.52 | 0.0645 | below_vwap | below_vwap |
| 17 | AMD | ai_accelerator | 555.16 |  | 551.8751 | 0.5952 | 548.755 | 526.6 | 2.0661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 475.03 |  | 473.8784 | 0.243 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1596.29 |  | 1581.5197 | 0.9339 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 397.085 |  | 391.7807 | 1.3539 | 387.635 | 380.205 | 0.758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.91 |  | 707.458 | -0.0775 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.78 |  | 70.8592 | -0.1118 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.67 |  | 211.5165 | 1.0181 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.68 |  | 389.8596 | -0.3026 | 400.89 | 392.26 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.42 |  | 324.9821 | -0.173 | 328.865 | 325.74 | 0.0062 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.5 |  | 347.8254 | -0.381 | 348.76 | 346.23 | 0.0375 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555.16 |  | 551.8751 | 0.5952 | 548.755 | 526.6 | 2.0661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.75 |  | 420.9367 | 0.1932 | 419.42 | 414.87 | 0.1873 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.83 |  | 553.6713 | 0.7511 | 551.02 | 540.105 | 0.0466 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.48 |  | 586.1263 | 0.5722 | 581.9 | 572.01 | 0.0204 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.085 |  | 391.7807 | 1.3539 | 387.635 | 380.205 | 0.758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 967 |  | 968.4618 | -0.1509 | 963.41 | 936.99 | 2.0683 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 212.7 |  | 211.4574 | 0.5877 | 207.06 | 202.18 | 0.1693 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 440.08 |  | 442.3799 | -0.5199 | 435.98 | 415.79 | 2.3518 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.34 |  | 48.97 | -1.2864 | 48.96 | 47.01 | 0.0207 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.02 |  | 31.1584 | -0.4442 | 30.66 | 28.52 | 0.0645 | below_vwap | below_vwap |
| SPY | market_regime | 748.33 |  | 748.513 | -0.0245 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.11 |  | 294.9906 | -0.2985 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.79 |  | 126.5419 | -1.3845 | 128.79 | 125.83 | 0.0321 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.55 |  | 83.3827 | -0.9987 | 83.22 | 79.6 | 2.9679 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.59 |  | 299.4863 | 1.0363 | 297.69 | 293.905 | 0.0958 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.76 |  | 407.867 | -0.0262 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.62 |  | 641.3726 | 0.3504 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1001.76 |  | 1005.0045 | -0.3228 | 1036.605 | 998.94 | 1.6052 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.03 |  | 473.8784 | 0.243 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.05 |  | 142.9595 | 0.0633 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.15 |  | 174.9355 | 0.1226 | 175.265 | 171.06 | 0.1941 | watch_only | none |
| COHR | ai_networking_optical | 315.33 |  | 316.0249 | -0.2199 | 317.93 | 306.89 | 2.3499 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 826.86 |  | 838.4284 | -1.3798 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.67 |  | 405.2923 | -0.647 | 407.12 | 397.835 | 0.1167 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 110.91 |  | 114.123 | -2.8154 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.78 |  | 329.8646 | 0.5807 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1802.57 |  | 1799.0009 | 0.1984 | 1786.525 | 1767.54 | 2.6701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.02 |  | 558.7558 | 0.2263 | 559.22 | 544.305 | 2.991 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.74 |  | 319.4644 | 0.3993 | 317.72 | 311.31 | 4.1467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.165 |  | 216.1325 | 0.015 | 215.465 | 210.975 | 4.3439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.26 |  | 371.6522 | -0.1055 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.59 |  | 295.3645 | 0.0763 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.31 |  | 67.471 | -0.2387 | 66.73 | 64.98 | 2.3325 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.425 |  | 55.6536 | -0.4107 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.72 |  | 138.8565 | -0.0983 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 347.66 |  | 344.7953 | 0.8308 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.36 |  | 507.3673 | 0.5899 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.13 |  | 297.8453 | 0.0956 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.05 |  | 30.6964 | -2.1059 | 30.78 | 29.46 | 0.0666 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.53 |  | 42.5012 | -2.2851 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.65 |  | 24.0011 | -1.4627 | 24.255 | 23.58 | 0.0423 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1596.29 |  | 1581.5197 | 0.9339 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 556.24 |  | 556.1485 | 0.0164 | 548.14 | 526.22 | 0.1294 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 903.08 |  | 909.5584 | -0.7123 | 899.59 | 860.605 | 2.0463 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 242.91 |  | 244.2106 | -0.5326 | 248.43 | 244.47 | 0.1317 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 625.71 |  | 630.4307 | -0.7488 | 647.02 | 632.77 | 0.4155 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 284.67 |  | 285.5847 | -0.3203 | 286.39 | 280.275 | 2.9332 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.65 |  | 166.738 | -0.0528 | 166.63 | 162.08 | 0.294 | below_vwap | below_vwap |
