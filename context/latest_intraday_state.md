# Intraday State

- Generated at: `2026-07-23T03:30:34+08:00`
- Market time ET: `2026-07-22T15:30:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 2, 'below_vwap': 16, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.6 |  | 707.4397 | 0.0227 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.175 |  | 554.286 | 0.882 | 551.02 | 540.105 | 0.0447 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.76 |  | 586.6973 | 0.6925 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748 |  | 748.4751 | -0.0635 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.34 |  | 211.7166 | 0.7668 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 912.5 |  | 909.4717 | 0.333 | 899.59 | 860.605 | 0.1381 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 559.175 |  | 554.286 | 0.882 | 551.02 | 540.105 | 0.0447 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.76 |  | 586.6973 | 0.6925 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 707.6 |  | 707.4397 | 0.0227 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 6 | TER | semiconductor_test_packaging | 372.23 |  | 371.6676 | 0.1513 | 369.53 | 365 | 0.1773 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.38 |  | 1799.3064 | 0.3376 | 1786.525 | 1767.54 | 0.0803 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.77 |  | 216.1859 | 0.2702 | 215.465 | 210.975 | 0.0507 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.525 |  | 174.9801 | 0.3114 | 175.265 | 171.06 | 0.2678 | buy_precheck_manual_confirm | none |
| 10 | DELL | ai_server_oem | 443.02 |  | 442.4083 | 0.1383 | 435.98 | 415.79 | 0.1896 | buy_precheck_manual_confirm | none |
| 11 | CRWV | gpu_cloud_ai_factory | 83.36 |  | 83.3395 | 0.0246 | 83.22 | 79.6 | 0.108 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 70.94 |  | 70.8564 | 0.118 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.6 |  | 707.4397 | 0.0227 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 2 | CRWV | gpu_cloud_ai_factory | 83.36 |  | 83.3395 | 0.0246 | 83.22 | 79.6 | 0.108 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.77 |  | 216.1859 | 0.2702 | 215.465 | 210.975 | 0.0507 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 175.525 |  | 174.9801 | 0.3114 | 175.265 | 171.06 | 0.2678 | buy_precheck_manual_confirm | none |
| 5 | STX | memory_hbm_storage | 912.5 |  | 909.4717 | 0.333 | 899.59 | 860.605 | 0.1381 | buy_precheck_manual_confirm | none |
| 6 | TER | semiconductor_test_packaging | 372.23 |  | 371.6676 | 0.1513 | 369.53 | 365 | 0.1773 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.38 |  | 1799.3064 | 0.3376 | 1786.525 | 1767.54 | 0.0803 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 244.61 |  | 244.2259 | 0.1573 | 248.43 | 244.47 | 0.0245 | watch_only | none |
| 9 | NVDA | ai_accelerator | 213.34 |  | 211.7166 | 0.7668 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 10 | DELL | ai_server_oem | 443.02 |  | 442.4083 | 0.1383 | 435.98 | 415.79 | 0.1896 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 590.76 |  | 586.6973 | 0.6925 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| 12 | SOXX | semiconductor_index | 559.175 |  | 554.286 | 0.882 | 551.02 | 540.105 | 0.0447 | buy_precheck_manual_confirm | none |
| 13 | LIN | industrial_gases | 508.47 |  | 507.4898 | 0.1932 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ARM | ai_accelerator | 285.75 |  | 285.5797 | 0.0596 | 286.39 | 280.275 | 0.6649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | ORCL | cloud_ai_capex | 126.46 |  | 126.456 | 0.0032 | 128.79 | 125.83 | 1.8346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | PWR | data_center_power_cooling | 644.74 |  | 641.8131 | 0.456 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 139.19 |  | 138.9149 | 0.198 | 140.09 | 135.555 | 5.0938 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MKSI | semiconductor_materials | 347.17 |  | 345.575 | 0.4616 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 320.965 |  | 319.6149 | 0.4224 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMAT | semiconductor_equipment | 561.865 |  | 558.9456 | 0.5223 | 559.22 | 544.305 | 1.8065 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.34 |  | 211.7166 | 0.7668 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 912.5 |  | 909.4717 | 0.333 | 899.59 | 860.605 | 0.1381 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 559.175 |  | 554.286 | 0.882 | 551.02 | 540.105 | 0.0447 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 590.76 |  | 586.6973 | 0.6925 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 707.6 |  | 707.4397 | 0.0227 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 6 | TER | semiconductor_test_packaging | 372.23 |  | 371.6676 | 0.1513 | 369.53 | 365 | 0.1773 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.38 |  | 1799.3064 | 0.3376 | 1786.525 | 1767.54 | 0.0803 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.77 |  | 216.1859 | 0.2702 | 215.465 | 210.975 | 0.0507 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.525 |  | 174.9801 | 0.3114 | 175.265 | 171.06 | 0.2678 | buy_precheck_manual_confirm | none |
| 10 | DELL | ai_server_oem | 443.02 |  | 442.4083 | 0.1383 | 435.98 | 415.79 | 0.1896 | buy_precheck_manual_confirm | none |
| 11 | CRWV | gpu_cloud_ai_factory | 83.36 |  | 83.3395 | 0.0246 | 83.22 | 79.6 | 0.108 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 70.94 |  | 70.8564 | 0.118 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 13 | SPY | market_regime | 748 |  | 748.4751 | -0.0635 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 14 | AMKR | semiconductor_test_packaging | 67.34 |  | 67.4613 | -0.1799 | 66.73 | 64.98 | 2.5542 | below_vwap | below_vwap,spread_too_wide |
| 15 | SMCI | ai_server_oem | 30.865 |  | 31.1401 | -0.8836 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 16 | MU | memory_hbm_storage | 972.775 |  | 968.5421 | 0.437 | 963.41 | 936.99 | 1.1071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TSM | foundry | 422.8 |  | 421.1669 | 0.3878 | 419.42 | 414.87 | 0.6362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 558.72 |  | 553.0592 | 1.0236 | 548.755 | 526.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1615.95 |  | 1583.5769 | 2.0443 | 1558.88 | 1518.99 | 0.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 559.61 |  | 556.3276 | 0.59 | 548.14 | 526.22 | 0.713 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.6 |  | 707.4397 | 0.0227 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 70.94 |  | 70.8564 | 0.118 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.34 |  | 211.7166 | 0.7668 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.42 |  | 389.7151 | -0.0757 | 400.89 | 392.26 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.39 |  | 324.9373 | -0.1684 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 345.3 |  | 347.4553 | -0.6203 | 348.76 | 346.23 | 0.0898 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 558.72 |  | 553.0592 | 1.0236 | 548.755 | 526.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TSM | foundry | 422.8 |  | 421.1669 | 0.3878 | 419.42 | 414.87 | 0.6362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.175 |  | 554.286 | 0.882 | 551.02 | 540.105 | 0.0447 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.76 |  | 586.6973 | 0.6925 | 581.9 | 572.01 | 0.0542 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.14 |  | 392.2395 | 1.5043 | 387.635 | 380.205 | 0.5702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 972.775 |  | 968.5421 | 0.437 | 963.41 | 936.99 | 1.1071 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.84 |  | 211.5668 | 0.6018 | 207.06 | 202.18 | 0.3665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.02 |  | 442.4083 | 0.1383 | 435.98 | 415.79 | 0.1896 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 48.39 |  | 48.904 | -1.051 | 48.96 | 47.01 | 0.0413 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.865 |  | 31.1401 | -0.8836 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748 |  | 748.4751 | -0.0635 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.79 |  | 294.853 | -0.3605 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.46 |  | 126.456 | 0.0032 | 128.79 | 125.83 | 1.8346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 83.36 |  | 83.3395 | 0.0246 | 83.22 | 79.6 | 0.108 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 302.78 |  | 299.8503 | 0.977 | 297.69 | 293.905 | 2.127 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.07 |  | 407.647 | -0.1415 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.74 |  | 641.8131 | 0.456 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 993.975 |  | 1003.8301 | -0.9817 | 1036.605 | 998.94 | 1.2576 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 472.895 |  | 473.7951 | -0.19 | 473.865 | 466.83 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.415 |  | 142.8813 | -0.3263 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.525 |  | 174.9801 | 0.3114 | 175.265 | 171.06 | 0.2678 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 314.61 |  | 315.9966 | -0.4388 | 317.93 | 306.89 | 3.703 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 831.78 |  | 837.7849 | -0.7168 | 840.47 | 814.62 | 0.2549 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 400.35 |  | 404.8308 | -1.1068 | 407.12 | 397.835 | 1.2889 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.03 |  | 113.878 | -2.5009 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.96 |  | 330.018 | 0.5885 | 322.67 | 307.545 | 4.8078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1805.38 |  | 1799.3064 | 0.3376 | 1786.525 | 1767.54 | 0.0803 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 561.865 |  | 558.9456 | 0.5223 | 559.22 | 544.305 | 1.8065 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.965 |  | 319.6149 | 0.4224 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.77 |  | 216.1859 | 0.2702 | 215.465 | 210.975 | 0.0507 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 372.23 |  | 371.6676 | 0.1513 | 369.53 | 365 | 0.1773 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 296.81 |  | 295.4093 | 0.4742 | 298.42 | 288.335 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 67.34 |  | 67.4613 | -0.1799 | 66.73 | 64.98 | 2.5542 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.36 |  | 55.5749 | -0.3868 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.19 |  | 138.9149 | 0.198 | 140.09 | 135.555 | 5.0938 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 347.17 |  | 345.575 | 0.4616 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.47 |  | 507.4898 | 0.1932 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.655 |  | 297.7394 | -0.3642 | 300.24 | 297.585 | 4.4564 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.06 |  | 30.6545 | -1.9392 | 30.78 | 29.46 | 0.0998 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.48 |  | 42.4152 | -2.2048 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.61 |  | 23.974 | -1.5182 | 24.255 | 23.58 | 0.1271 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1615.95 |  | 1583.5769 | 2.0443 | 1558.88 | 1518.99 | 0.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 559.61 |  | 556.3276 | 0.59 | 548.14 | 526.22 | 0.713 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 912.5 |  | 909.4717 | 0.333 | 899.59 | 860.605 | 0.1381 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 244.61 |  | 244.2259 | 0.1573 | 248.43 | 244.47 | 0.0245 | watch_only | none |
| META | cloud_ai_capex | 627.2 |  | 630.0496 | -0.4523 | 647.02 | 632.77 | 0.7175 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.75 |  | 285.5797 | 0.0596 | 286.39 | 280.275 | 0.6649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.45 |  | 166.7222 | -0.1632 | 166.63 | 162.08 | 0.793 | below_vwap | below_vwap,spread_too_wide |
