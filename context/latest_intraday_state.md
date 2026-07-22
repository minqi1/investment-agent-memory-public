# Intraday State

- Generated at: `2026-07-23T02:09:54+08:00`
- Market time ET: `2026-07-22T14:09:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'below_opening_15m_low': 8, 'below_vwap': 17, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.53 |  | 707.504 | 0.0037 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.27 |  | 553.2739 | 1.0837 | 551.02 | 540.105 | 0.0375 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.61 |  | 585.8388 | 0.8144 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.49 |  | 748.5348 | -0.006 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.72 |  | 211.3936 | 1.1005 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.27 |  | 553.2739 | 1.0837 | 551.02 | 540.105 | 0.0375 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.61 |  | 585.8388 | 0.8144 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 707.53 |  | 707.504 | 0.0037 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 396.355 |  | 391.2662 | 1.3006 | 387.635 | 380.205 | 0.111 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1804.69 |  | 1798.753 | 0.3301 | 1786.525 | 1767.54 | 0.0986 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.5 |  | 299.2329 | 0.7576 | 297.69 | 293.905 | 0.1095 | buy_precheck_manual_confirm | none |
| 8 | AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.01 |  | 70.8653 | 0.2042 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.53 |  | 707.504 | 0.0037 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1804.69 |  | 1798.753 | 0.3301 | 1786.525 | 1767.54 | 0.0986 | buy_precheck_manual_confirm | none |
| 3 | AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| 4 | VRT | data_center_power_cooling | 301.5 |  | 299.2329 | 0.7576 | 297.69 | 293.905 | 0.1095 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 474.72 |  | 473.7601 | 0.2026 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | SOXX | semiconductor_index | 559.27 |  | 553.2739 | 1.0837 | 551.02 | 540.105 | 0.0375 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 590.61 |  | 585.8388 | 0.8144 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 8 | PWR | data_center_power_cooling | 642.78 |  | 640.9615 | 0.2837 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.72 |  | 211.3936 | 1.1005 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 10 | JCI | data_center_power_cooling | 143.24 |  | 142.9385 | 0.2109 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 139.32 |  | 138.8703 | 0.3238 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 296.06 |  | 295.3682 | 0.2342 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 298.19 |  | 297.8224 | 0.1234 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 396.355 |  | 391.2662 | 1.3006 | 387.635 | 380.205 | 0.111 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 175.45 |  | 174.9119 | 0.3076 | 175.265 | 171.06 | 2.5591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TSM | foundry | 422.08 |  | 420.8232 | 0.2986 | 419.42 | 414.87 | 0.4288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | KLAC | semiconductor_equipment | 216.525 |  | 216.1232 | 0.1859 | 215.465 | 210.975 | 4.2489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LIN | industrial_gases | 509.77 |  | 507.331 | 0.4808 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TER | semiconductor_test_packaging | 372.6 |  | 371.6839 | 0.2465 | 369.53 | 365 | 4.9678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 558.71 |  | 556.1113 | 0.4673 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.72 |  | 211.3936 | 1.1005 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.27 |  | 553.2739 | 1.0837 | 551.02 | 540.105 | 0.0375 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.61 |  | 585.8388 | 0.8144 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 707.53 |  | 707.504 | 0.0037 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 396.355 |  | 391.2662 | 1.3006 | 387.635 | 380.205 | 0.111 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1804.69 |  | 1798.753 | 0.3301 | 1786.525 | 1767.54 | 0.0986 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.5 |  | 299.2329 | 0.7576 | 297.69 | 293.905 | 0.1095 | buy_precheck_manual_confirm | none |
| 8 | AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.01 |  | 70.8653 | 0.2042 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 10 | SPY | market_regime | 748.49 |  | 748.5348 | -0.006 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 11 | DELL | ai_server_oem | 441.2 |  | 442.5156 | -0.2973 | 435.98 | 415.79 | 2.9306 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMCI | ai_server_oem | 30.88 |  | 31.1726 | -0.9386 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 13 | MU | memory_hbm_storage | 974.1 |  | 968.4281 | 0.5857 | 963.41 | 936.99 | 1.2319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 422.08 |  | 420.8232 | 0.2986 | 419.42 | 414.87 | 0.4288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 556.59 |  | 551.7544 | 0.8764 | 548.755 | 526.6 | 2.7794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 474.72 |  | 473.7601 | 0.2026 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1600.88 |  | 1580.6542 | 1.2796 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 558.71 |  | 556.1113 | 0.4673 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | STX | memory_hbm_storage | 913.275 |  | 909.3449 | 0.4322 | 899.59 | 860.605 | 0.692 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MRVL | custom_silicon_networking | 212.91 |  | 211.3927 | 0.7177 | 207.06 | 202.18 | 2.649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.53 |  | 707.504 | 0.0037 | 705.86 | 703.63 | 0.0057 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.01 |  | 70.8653 | 0.2042 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.72 |  | 211.3936 | 1.1005 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.275 |  | 390.0597 | -0.7139 | 400.89 | 392.26 | 0.1394 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.95 |  | 325.0457 | -0.3371 | 328.865 | 325.74 | 0.2377 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.22 |  | 347.9029 | -0.1963 | 348.76 | 346.23 | 0.1037 | below_vwap | below_vwap |
| AMD | ai_accelerator | 556.59 |  | 551.7544 | 0.8764 | 548.755 | 526.6 | 2.7794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.08 |  | 420.8232 | 0.2986 | 419.42 | 414.87 | 0.4288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.27 |  | 553.2739 | 1.0837 | 551.02 | 540.105 | 0.0375 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.61 |  | 585.8388 | 0.8144 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.355 |  | 391.2662 | 1.3006 | 387.635 | 380.205 | 0.111 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 974.1 |  | 968.4281 | 0.5857 | 963.41 | 936.99 | 1.2319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.91 |  | 211.3927 | 0.7177 | 207.06 | 202.18 | 2.649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 441.2 |  | 442.5156 | -0.2973 | 435.98 | 415.79 | 2.9306 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.66 |  | 49.0159 | -0.726 | 48.96 | 47.01 | 0.0411 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.88 |  | 31.1726 | -0.9386 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748.49 |  | 748.5348 | -0.006 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.21 |  | 295.0859 | -0.2968 | 296.39 | 295.22 | 0.0136 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.28 |  | 126.6163 | -1.0554 | 128.79 | 125.83 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.65 |  | 83.4884 | -1.0042 | 83.22 | 79.6 | 3.775 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.5 |  | 299.2329 | 0.7576 | 297.69 | 293.905 | 0.1095 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.32 |  | 407.9017 | -0.1426 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 642.78 |  | 640.9615 | 0.2837 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 993.28 |  | 1005.6581 | -1.2308 | 1036.605 | 998.94 | 4.0271 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.72 |  | 473.7601 | 0.2026 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.24 |  | 142.9385 | 0.2109 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.45 |  | 174.9119 | 0.3076 | 175.265 | 171.06 | 2.5591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.53 |  | 316.1054 | -0.182 | 317.93 | 306.89 | 2.7097 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 828.365 |  | 839.0889 | -1.278 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.82 |  | 405.5304 | -0.6684 | 407.12 | 397.835 | 2.1871 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.92 |  | 114.2733 | -2.0593 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.51 |  | 329.6506 | 0.8674 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1804.69 |  | 1798.753 | 0.3301 | 1786.525 | 1767.54 | 0.0986 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 561.61 |  | 558.6159 | 0.536 | 559.22 | 544.305 | 2.694 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.38 |  | 319.1921 | 0.6854 | 317.72 | 311.31 | 3.9206 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.525 |  | 216.1232 | 0.1859 | 215.465 | 210.975 | 4.2489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.6 |  | 371.6839 | 0.2465 | 369.53 | 365 | 4.9678 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.06 |  | 295.3682 | 0.2342 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 55.59 |  | 55.6828 | -0.1667 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.32 |  | 138.8703 | 0.3238 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 348.115 |  | 344.4688 | 1.0585 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.77 |  | 507.331 | 0.4808 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.19 |  | 297.8224 | 0.1234 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.21 |  | 30.739 | -1.7208 | 30.78 | 29.46 | 0.0662 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.595 |  | 42.581 | -2.3157 | 42.29 | 40.305 | 0.0721 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.69 |  | 24.0459 | -1.4801 | 24.255 | 23.58 | 0.0844 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1600.88 |  | 1580.6542 | 1.2796 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 558.71 |  | 556.1113 | 0.4673 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 913.275 |  | 909.3449 | 0.4322 | 899.59 | 860.605 | 0.692 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 242.82 |  | 244.2929 | -0.6029 | 248.43 | 244.47 | 0.0124 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.26 |  | 630.7981 | -0.7194 | 647.02 | 632.77 | 0.4503 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 284.96 |  | 285.6481 | -0.2409 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.35 |  | 166.7825 | -0.2593 | 166.63 | 162.08 | 1.8335 | below_vwap | below_vwap,spread_too_wide |
