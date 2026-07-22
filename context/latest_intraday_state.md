# Intraday State

- Generated at: `2026-07-23T00:03:23+08:00`
- Market time ET: `2026-07-22T12:03:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_opening_15m_low': 6, 'below_vwap': 10, 'spread_too_wide_or_missing': 28, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.06 |  | 707.0016 | 0.2912 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.2 |  | 551.8834 | 1.3258 | 551.02 | 540.105 | 0.0805 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.1 |  | 584.328 | 1.1589 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.6 |  | 748.1593 | 0.1926 | 747.68 | 746.425 | 0.0307 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.62 |  | 210.0871 | 1.6816 | 207.4 | 205.01 | 0.0983 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 423.58 |  | 420.3409 | 0.7706 | 419.42 | 414.87 | 0.3423 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 561.7 |  | 554.556 | 1.2882 | 548.14 | 526.22 | 0.2795 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.2 |  | 551.8834 | 1.3258 | 551.02 | 540.105 | 0.0805 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.1 |  | 584.328 | 1.1589 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.06 |  | 707.0016 | 0.2912 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.6 |  | 748.1593 | 0.1926 | 747.68 | 746.425 | 0.0307 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 31.76 |  | 31.0882 | 2.161 | 30.66 | 28.52 | 0.0315 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 83.57 |  | 83.4803 | 0.1074 | 83.22 | 79.6 | 0.1077 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.42 |  | 70.7462 | 0.9524 | 70.43 | 69.81 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.6 |  | 748.1593 | 0.1926 | 747.68 | 746.425 | 0.0307 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.06 |  | 707.0016 | 0.2912 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 3 | CRWV | gpu_cloud_ai_factory | 83.57 |  | 83.4803 | 0.1074 | 83.22 | 79.6 | 0.1077 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 423.58 |  | 420.3409 | 0.7706 | 419.42 | 414.87 | 0.3423 | buy_precheck_manual_confirm | none |
| 5 | ENTG | semiconductor_materials | 138.945 |  | 138.7417 | 0.1465 | 140.09 | 135.555 | 0.1727 | watch_only | none |
| 6 | TT | data_center_power_cooling | 473.98 |  | 472.5709 | 0.2982 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SOXX | semiconductor_index | 559.2 |  | 551.8834 | 1.3258 | 551.02 | 540.105 | 0.0805 | buy_precheck_manual_confirm | none |
| 8 | ARM | ai_accelerator | 285.725 |  | 285.6143 | 0.0388 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | LRCX | semiconductor_equipment | 319.33 |  | 318.4527 | 0.2755 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 142.905 |  | 142.8387 | 0.0464 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MKSI | semiconductor_materials | 344.165 |  | 343.1908 | 0.2839 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | COHU | semiconductor_test_packaging | 55.86 |  | 55.67 | 0.3413 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SMH | semiconductor_index | 591.1 |  | 584.328 | 1.1589 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| 14 | AAOI | ai_networking_optical | 115.01 |  | 114.839 | 0.1489 | 117.185 | 113.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 561.7 |  | 554.556 | 1.2882 | 548.14 | 526.22 | 0.2795 | buy_precheck_manual_confirm | none |
| 16 | KLAC | semiconductor_equipment | 216.165 |  | 216.1105 | 0.0252 | 215.465 | 210.975 | 0.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LIN | industrial_gases | 507.655 |  | 506.9717 | 0.1348 | 507.545 | 505.59 | 4.8576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | PWR | data_center_power_cooling | 642.17 |  | 639.6002 | 0.4018 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TER | semiconductor_test_packaging | 371.45 |  | 371.1123 | 0.091 | 369.53 | 365 | 0.568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | LITE | ai_networking_optical | 844.1 |  | 840.8668 | 0.3845 | 840.47 | 814.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.62 |  | 210.0871 | 1.6816 | 207.4 | 205.01 | 0.0983 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 423.58 |  | 420.3409 | 0.7706 | 419.42 | 414.87 | 0.3423 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 561.7 |  | 554.556 | 1.2882 | 548.14 | 526.22 | 0.2795 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.2 |  | 551.8834 | 1.3258 | 551.02 | 540.105 | 0.0805 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.1 |  | 584.328 | 1.1589 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.06 |  | 707.0016 | 0.2912 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.6 |  | 748.1593 | 0.1926 | 747.68 | 746.425 | 0.0307 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 31.76 |  | 31.0882 | 2.161 | 30.66 | 28.52 | 0.0315 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 83.57 |  | 83.4803 | 0.1074 | 83.22 | 79.6 | 0.1077 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.42 |  | 70.7462 | 0.9524 | 70.43 | 69.81 | 0.028 | buy_precheck_manual_confirm | none |
| 11 | MU | memory_hbm_storage | 974.65 |  | 965.3649 | 0.9618 | 963.41 | 936.99 | 2.4912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | IREN | high_beta_ai_infrastructure | 42.45 |  | 42.7722 | -0.7534 | 42.29 | 40.305 | 0.0471 | below_vwap | below_vwap |
| 13 | AMD | ai_accelerator | 555.91 |  | 550.1189 | 1.0527 | 548.755 | 526.6 | 2.7091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TT | data_center_power_cooling | 473.98 |  | 472.5709 | 0.2982 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SNDK | memory_hbm_storage | 1601.01 |  | 1571.0376 | 1.9078 | 1558.88 | 1518.99 | 0.6302 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 917.58 |  | 906.1794 | 1.2581 | 899.59 | 860.605 | 0.5166 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 214.17 |  | 210.2929 | 1.8437 | 207.06 | 202.18 | 0.9385 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 371.45 |  | 371.1123 | 0.091 | 369.53 | 365 | 0.568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AVGO | custom_silicon_networking | 393.2 |  | 388.4602 | 1.2202 | 387.635 | 380.205 | 2.0041 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1806.26 |  | 1795.4995 | 0.5993 | 1786.525 | 1767.54 | 1.6327 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.06 |  | 707.0016 | 0.2912 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.42 |  | 70.7462 | 0.9524 | 70.43 | 69.81 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.62 |  | 210.0871 | 1.6816 | 207.4 | 205.01 | 0.0983 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.23 |  | 390.8435 | -0.4128 | 400.89 | 392.26 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.51 |  | 325.5712 | -0.326 | 328.865 | 325.74 | 0.0092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.87 |  | 347.8771 | -0.002 | 348.76 | 346.23 | 0.1983 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555.91 |  | 550.1189 | 1.0527 | 548.755 | 526.6 | 2.7091 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.58 |  | 420.3409 | 0.7706 | 419.42 | 414.87 | 0.3423 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.2 |  | 551.8834 | 1.3258 | 551.02 | 540.105 | 0.0805 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.1 |  | 584.328 | 1.1589 | 581.9 | 572.01 | 0.0491 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 393.2 |  | 388.4602 | 1.2202 | 387.635 | 380.205 | 2.0041 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 974.65 |  | 965.3649 | 0.9618 | 963.41 | 936.99 | 2.4912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 214.17 |  | 210.2929 | 1.8437 | 207.06 | 202.18 | 0.9385 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 442.77 |  | 442.3029 | 0.1056 | 435.98 | 415.79 | 1.6465 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.815 |  | 49.0366 | -0.4518 | 48.96 | 47.01 | 0.0819 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.76 |  | 31.0882 | 2.161 | 30.66 | 28.52 | 0.0315 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.6 |  | 748.1593 | 0.1926 | 747.68 | 746.425 | 0.0307 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.65 |  | 295.2776 | -0.2125 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.87 |  | 126.8705 | -0.7886 | 128.79 | 125.83 | 0.0874 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.57 |  | 83.4803 | 0.1074 | 83.22 | 79.6 | 0.1077 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 300.12 |  | 298.6082 | 0.5063 | 297.69 | 293.905 | 1.7326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 406.95 |  | 407.7514 | -0.1966 | 409.095 | 398.16 | 0.1573 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 642.17 |  | 639.6002 | 0.4018 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1001.495 |  | 1009.9923 | -0.8413 | 1036.605 | 998.94 | 2.4963 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.98 |  | 472.5709 | 0.2982 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.905 |  | 142.8387 | 0.0464 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.2 |  | 174.6396 | 0.8935 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 318.49 |  | 315.9986 | 0.7884 | 317.93 | 306.89 | 2.1508 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 844.1 |  | 840.8668 | 0.3845 | 840.47 | 814.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 406.5 |  | 406.1703 | 0.0812 | 407.12 | 397.835 | 3.08 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 115.01 |  | 114.839 | 0.1489 | 117.185 | 113.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 334.45 |  | 327.9868 | 1.9706 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.26 |  | 1795.4995 | 0.5993 | 1786.525 | 1767.54 | 1.6327 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.85 |  | 558.2231 | 0.4706 | 559.22 | 544.305 | 2.605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 319.33 |  | 318.4527 | 0.2755 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.165 |  | 216.1105 | 0.0252 | 215.465 | 210.975 | 0.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.45 |  | 371.1123 | 0.091 | 369.53 | 365 | 0.568 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 294.55 |  | 294.8967 | -0.1176 | 298.42 | 288.335 | 4.4712 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.73 |  | 67.4324 | 0.4414 | 66.73 | 64.98 | 1.8013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.86 |  | 55.67 | 0.3413 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.945 |  | 138.7417 | 0.1465 | 140.09 | 135.555 | 0.1727 | watch_only | none |
| MKSI | semiconductor_materials | 344.165 |  | 343.1908 | 0.2839 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 507.655 |  | 506.9717 | 0.1348 | 507.545 | 505.59 | 4.8576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.66 |  | 297.8163 | -0.3883 | 300.24 | 297.585 | 4.5709 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.74 |  | 30.8437 | -0.3362 | 30.78 | 29.46 | 0.0976 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.45 |  | 42.7722 | -0.7534 | 42.29 | 40.305 | 0.0471 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.87 |  | 24.1566 | -1.1865 | 24.255 | 23.58 | 0.0419 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1601.01 |  | 1571.0376 | 1.9078 | 1558.88 | 1518.99 | 0.6302 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 561.7 |  | 554.556 | 1.2882 | 548.14 | 526.22 | 0.2795 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 917.58 |  | 906.1794 | 1.2581 | 899.59 | 860.605 | 0.5166 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.845 |  | 244.6642 | -0.3348 | 248.43 | 244.47 | 0.123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 628.45 |  | 631.7449 | -0.5215 | 647.02 | 632.77 | 0.1114 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.725 |  | 285.6143 | 0.0388 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 168.38 |  | 166.6083 | 1.0634 | 166.63 | 162.08 | 0.7008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
