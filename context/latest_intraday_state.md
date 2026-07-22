# Intraday State

- Generated at: `2026-07-23T00:08:17+08:00`
- Market time ET: `2026-07-22T12:08:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'below_opening_15m_low': 6, 'below_vwap': 10, 'spread_too_wide_or_missing': 30, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.25 |  | 707.022 | 0.3151 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.66 |  | 551.9634 | 1.3944 | 551.02 | 540.105 | 0.0733 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.045 |  | 584.4803 | 1.1232 | 581.9 | 572.01 | 0.0609 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.78 |  | 748.198 | 0.2114 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.53 |  | 210.1606 | 1.6032 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 973.87 |  | 965.5298 | 0.8638 | 963.41 | 936.99 | 0.1776 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 423.33 |  | 420.3621 | 0.706 | 419.42 | 414.87 | 0.2362 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.66 |  | 551.9634 | 1.3944 | 551.02 | 540.105 | 0.0733 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.045 |  | 584.4803 | 1.1232 | 581.9 | 572.01 | 0.0609 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.25 |  | 707.022 | 0.3151 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.78 |  | 748.198 | 0.2114 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 31.95 |  | 31.1092 | 2.7027 | 30.66 | 28.52 | 0.0313 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.48 |  | 70.7498 | 1.0321 | 70.43 | 69.81 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.78 |  | 748.198 | 0.2114 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.25 |  | 707.022 | 0.3151 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 423.33 |  | 420.3621 | 0.706 | 419.42 | 414.87 | 0.2362 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 473.98 |  | 472.5709 | 0.2982 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MU | memory_hbm_storage | 973.87 |  | 965.5298 | 0.8638 | 963.41 | 936.99 | 0.1776 | buy_precheck_manual_confirm | none |
| 6 | ARM | ai_accelerator | 286.03 |  | 285.6239 | 0.1422 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 142.94 |  | 142.841 | 0.0693 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ENTG | semiconductor_materials | 139.03 |  | 138.759 | 0.1953 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | COHU | semiconductor_test_packaging | 55.86 |  | 55.67 | 0.3413 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SOXX | semiconductor_index | 559.66 |  | 551.9634 | 1.3944 | 551.02 | 540.105 | 0.0733 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 591.045 |  | 584.4803 | 1.1232 | 581.9 | 572.01 | 0.0609 | buy_precheck_manual_confirm | none |
| 12 | LIN | industrial_gases | 508.015 |  | 506.9769 | 0.2048 | 507.545 | 505.59 | 4.7459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | PWR | data_center_power_cooling | 642.19 |  | 639.6297 | 0.4003 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TER | semiconductor_test_packaging | 372.27 |  | 371.1172 | 0.3106 | 369.53 | 365 | 0.3788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | KLAC | semiconductor_equipment | 216.34 |  | 216.112 | 0.1055 | 215.465 | 210.975 | 2.2095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LRCX | semiconductor_equipment | 319.43 |  | 318.4583 | 0.3051 | 317.72 | 311.31 | 4.5393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 846.14 |  | 840.8983 | 0.6233 | 840.47 | 814.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | CIEN | ai_networking_optical | 406.575 |  | 406.1763 | 0.0982 | 407.12 | 397.835 | 3.0794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MKSI | semiconductor_materials | 345.36 |  | 343.2446 | 0.6163 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AAOI | ai_networking_optical | 115.29 |  | 114.8427 | 0.3895 | 117.185 | 113.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.53 |  | 210.1606 | 1.6032 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 973.87 |  | 965.5298 | 0.8638 | 963.41 | 936.99 | 0.1776 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 423.33 |  | 420.3621 | 0.706 | 419.42 | 414.87 | 0.2362 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.66 |  | 551.9634 | 1.3944 | 551.02 | 540.105 | 0.0733 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.045 |  | 584.4803 | 1.1232 | 581.9 | 572.01 | 0.0609 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.25 |  | 707.022 | 0.3151 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.78 |  | 748.198 | 0.2114 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 31.95 |  | 31.1092 | 2.7027 | 30.66 | 28.52 | 0.0313 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.48 |  | 70.7498 | 1.0321 | 70.43 | 69.81 | 0.028 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 30.81 |  | 30.8428 | -0.1063 | 30.78 | 29.46 | 0.0974 | below_vwap | below_vwap |
| 11 | IREN | high_beta_ai_infrastructure | 42.55 |  | 42.7692 | -0.5126 | 42.29 | 40.305 | 0.0235 | below_vwap | below_vwap |
| 12 | AMD | ai_accelerator | 555.545 |  | 550.2041 | 0.9707 | 548.755 | 526.6 | 2.7109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TT | data_center_power_cooling | 473.98 |  | 472.5709 | 0.2982 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SNDK | memory_hbm_storage | 1599.3 |  | 1571.247 | 1.7854 | 1558.88 | 1518.99 | 0.6866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | WDC | memory_hbm_storage | 561.705 |  | 554.6369 | 1.2744 | 548.14 | 526.22 | 0.4415 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 918.65 |  | 906.5101 | 1.3392 | 899.59 | 860.605 | 0.602 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 214.29 |  | 210.3698 | 1.8635 | 207.06 | 202.18 | 0.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 372.27 |  | 371.1172 | 0.3106 | 369.53 | 365 | 0.3788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AVGO | custom_silicon_networking | 393.74 |  | 388.5114 | 1.3458 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ASML | semiconductor_equipment | 1807.59 |  | 1795.6315 | 0.666 | 1786.525 | 1767.54 | 0.9958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.25 |  | 707.022 | 0.3151 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.48 |  | 70.7498 | 1.0321 | 70.43 | 69.81 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.53 |  | 210.1606 | 1.6032 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.96 |  | 390.8052 | -0.4721 | 400.89 | 392.26 | 0.27 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.525 |  | 325.5535 | -0.3159 | 328.865 | 325.74 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.85 |  | 347.8766 | -0.0076 | 348.76 | 346.23 | 0.1725 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555.545 |  | 550.2041 | 0.9707 | 548.755 | 526.6 | 2.7109 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.33 |  | 420.3621 | 0.706 | 419.42 | 414.87 | 0.2362 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.66 |  | 551.9634 | 1.3944 | 551.02 | 540.105 | 0.0733 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.045 |  | 584.4803 | 1.1232 | 581.9 | 572.01 | 0.0609 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 393.74 |  | 388.5114 | 1.3458 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 973.87 |  | 965.5298 | 0.8638 | 963.41 | 936.99 | 0.1776 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 214.29 |  | 210.3698 | 1.8635 | 207.06 | 202.18 | 0.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 445.39 |  | 442.3459 | 0.6882 | 435.98 | 415.79 | 2.9031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.92 |  | 49.0344 | -0.2333 | 48.96 | 47.01 | 0.0818 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.95 |  | 31.1092 | 2.7027 | 30.66 | 28.52 | 0.0313 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.78 |  | 748.198 | 0.2114 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.97 |  | 295.2729 | -0.1026 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.05 |  | 126.8441 | -0.626 | 128.79 | 125.83 | 2.1341 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 84.16 |  | 83.4842 | 0.8095 | 83.22 | 79.6 | 1.2239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 300.52 |  | 298.6196 | 0.6364 | 297.69 | 293.905 | 3.9165 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.54 |  | 407.7464 | -0.0506 | 409.095 | 398.16 | 2.2624 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 642.19 |  | 639.6297 | 0.4003 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1002.27 |  | 1009.8361 | -0.7492 | 1036.605 | 998.94 | 0.4849 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.98 |  | 472.5709 | 0.2982 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.94 |  | 142.841 | 0.0693 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.09 |  | 174.6636 | 0.8167 | 175.265 | 171.06 | 2.158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 319.06 |  | 316.0564 | 0.9503 | 317.93 | 306.89 | 1.8147 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 846.14 |  | 840.8983 | 0.6233 | 840.47 | 814.62 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 406.575 |  | 406.1763 | 0.0982 | 407.12 | 397.835 | 3.0794 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 115.29 |  | 114.8427 | 0.3895 | 117.185 | 113.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 335 |  | 328.0407 | 2.1215 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1807.59 |  | 1795.6315 | 0.666 | 1786.525 | 1767.54 | 0.9958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 561.02 |  | 558.2681 | 0.4929 | 559.22 | 544.305 | 0.3957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 319.43 |  | 318.4583 | 0.3051 | 317.72 | 311.31 | 4.5393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.34 |  | 216.112 | 0.1055 | 215.465 | 210.975 | 2.2095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.27 |  | 371.1172 | 0.3106 | 369.53 | 365 | 0.3788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 294.74 |  | 294.89 | -0.0509 | 298.42 | 288.335 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.73 |  | 67.4324 | 0.4414 | 66.73 | 64.98 | 1.7127 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.86 |  | 55.67 | 0.3413 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.03 |  | 138.759 | 0.1953 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 345.36 |  | 343.2446 | 0.6163 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.015 |  | 506.9769 | 0.2048 | 507.545 | 505.59 | 4.7459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.865 |  | 297.8137 | -0.3186 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.81 |  | 30.8428 | -0.1063 | 30.78 | 29.46 | 0.0974 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.55 |  | 42.7692 | -0.5126 | 42.29 | 40.305 | 0.0235 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.97 |  | 24.1544 | -0.7635 | 24.255 | 23.58 | 0.0834 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1599.3 |  | 1571.247 | 1.7854 | 1558.88 | 1518.99 | 0.6866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 561.705 |  | 554.6369 | 1.2744 | 548.14 | 526.22 | 0.4415 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 918.65 |  | 906.5101 | 1.3392 | 899.59 | 860.605 | 0.602 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.79 |  | 244.6531 | -0.3528 | 248.43 | 244.47 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 628.685 |  | 631.7211 | -0.4806 | 647.02 | 632.77 | 0.9544 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 286.03 |  | 285.6239 | 0.1422 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 168.39 |  | 166.6133 | 1.0663 | 166.63 | 162.08 | 0.7008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
