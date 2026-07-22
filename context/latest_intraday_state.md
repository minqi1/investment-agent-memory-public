# Intraday State

- Generated at: `2026-07-23T02:50:14+08:00`
- Market time ET: `2026-07-22T14:50:15-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `56`
- stale_count: `0`
- coverage_price: `54`
- coverage_vwap: `54`
- caution_counts: `{'below_vwap': 19, 'manual_confirm_candidate': 11, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 16, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.29 |  | 707.4553 | -0.0234 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.27 |  | 553.7004 | 0.8253 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.91 |  | 586.1333 | 0.6443 | 581.9 | 572.01 | 0.0288 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.4 |  | 748.512 | -0.015 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.84 |  | 211.5284 | 1.0928 | 207.4 | 205.01 | 0.0935 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.965 |  | 420.9407 | 0.2433 | 419.42 | 414.87 | 0.1185 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.01 |  | 473.8859 | 0.2372 | 473.865 | 466.83 | 0.1747 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.27 |  | 553.7004 | 0.8253 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.91 |  | 586.1333 | 0.6443 | 581.9 | 572.01 | 0.0288 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 213.01 |  | 211.472 | 0.7273 | 207.06 | 202.18 | 0.2347 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1804.19 |  | 1799.0181 | 0.2875 | 1786.525 | 1767.54 | 0.0205 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.46 |  | 216.1347 | 0.1505 | 215.465 | 210.975 | 0.0739 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.72 |  | 558.7627 | 0.3503 | 559.22 | 544.305 | 0.1338 | buy_precheck_manual_confirm | none |
| 10 | SKHY | memory_hbm_storage | 166.82 |  | 166.7384 | 0.0489 | 166.63 | 162.08 | 0.1619 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 70.885 |  | 70.859 | 0.0366 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 421.965 |  | 420.9407 | 0.2433 | 419.42 | 414.87 | 0.1185 | buy_precheck_manual_confirm | none |
| 2 | TT | data_center_power_cooling | 475.01 |  | 473.8859 | 0.2372 | 473.865 | 466.83 | 0.1747 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.46 |  | 216.1347 | 0.1505 | 215.465 | 210.975 | 0.0739 | buy_precheck_manual_confirm | none |
| 4 | SKHY | memory_hbm_storage | 166.82 |  | 166.7384 | 0.0489 | 166.63 | 162.08 | 0.1619 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1804.19 |  | 1799.0181 | 0.2875 | 1786.525 | 1767.54 | 0.0205 | buy_precheck_manual_confirm | none |
| 6 | AMAT | semiconductor_equipment | 560.72 |  | 558.7627 | 0.3503 | 559.22 | 544.305 | 0.1338 | buy_precheck_manual_confirm | none |
| 7 | APD | industrial_gases | 298.13 |  | 297.8453 | 0.0956 | 300.24 | 297.585 | 0.0973 | watch_only | none |
| 8 | SMH | semiconductor_index | 589.91 |  | 586.1333 | 0.6443 | 581.9 | 572.01 | 0.0288 | buy_precheck_manual_confirm | none |
| 9 | ANET | ai_networking_optical | 175.25 |  | 174.9359 | 0.1796 | 175.265 | 171.06 | 0.194 | watch_only | none |
| 10 | MRVL | custom_silicon_networking | 213.01 |  | 211.472 | 0.7273 | 207.06 | 202.18 | 0.2347 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 558.27 |  | 553.7004 | 0.8253 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| 12 | TER | semiconductor_test_packaging | 371.72 |  | 371.6485 | 0.0192 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | NVDA | ai_accelerator | 213.84 |  | 211.5284 | 1.0928 | 207.4 | 205.01 | 0.0935 | buy_precheck_manual_confirm | none |
| 14 | ETN | data_center_power_cooling | 408.08 |  | 407.868 | 0.052 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 139.01 |  | 138.8576 | 0.1097 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ONTO | semiconductor_test_packaging | 296.05 |  | 295.3671 | 0.2312 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | LIN | industrial_gases | 510.06 |  | 507.3999 | 0.5243 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 143.06 |  | 142.9602 | 0.0698 | 143.27 | 141.04 | 5.0468 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | COHR | ai_networking_optical | 316.07 |  | 316.0239 | 0.0146 | 317.93 | 306.89 | 2.3444 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | PWR | data_center_power_cooling | 643.96 |  | 641.4002 | 0.3991 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.84 |  | 211.5284 | 1.0928 | 207.4 | 205.01 | 0.0935 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.965 |  | 420.9407 | 0.2433 | 419.42 | 414.87 | 0.1185 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.01 |  | 473.8859 | 0.2372 | 473.865 | 466.83 | 0.1747 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 558.27 |  | 553.7004 | 0.8253 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.91 |  | 586.1333 | 0.6443 | 581.9 | 572.01 | 0.0288 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 213.01 |  | 211.472 | 0.7273 | 207.06 | 202.18 | 0.2347 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1804.19 |  | 1799.0181 | 0.2875 | 1786.525 | 1767.54 | 0.0205 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.46 |  | 216.1347 | 0.1505 | 215.465 | 210.975 | 0.0739 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 560.72 |  | 558.7627 | 0.3503 | 559.22 | 544.305 | 0.1338 | buy_precheck_manual_confirm | none |
| 10 | SKHY | memory_hbm_storage | 166.82 |  | 166.7384 | 0.0489 | 166.63 | 162.08 | 0.1619 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 70.885 |  | 70.859 | 0.0366 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 12 | MU | memory_hbm_storage | 967.505 |  | 968.4563 | -0.0982 | 963.41 | 936.99 | 1.2403 | below_vwap | below_vwap,spread_too_wide |
| 13 | STX | memory_hbm_storage | 905.72 |  | 909.5557 | -0.4217 | 899.59 | 860.605 | 1.9123 | below_vwap | below_vwap,spread_too_wide |
| 14 | QQQ | market_regime | 707.29 |  | 707.4553 | -0.0234 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 15 | SPY | market_regime | 748.4 |  | 748.512 | -0.015 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| 16 | DELL | ai_server_oem | 440.25 |  | 442.3685 | -0.4789 | 435.98 | 415.79 | 4.7791 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMKR | semiconductor_test_packaging | 67.36 |  | 67.4708 | -0.1643 | 66.73 | 64.98 | 0.1781 | below_vwap | below_vwap |
| 18 | SMCI | ai_server_oem | 31.065 |  | 31.1579 | -0.2982 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| 19 | AMD | ai_accelerator | 556.075 |  | 551.9117 | 0.7543 | 548.755 | 526.6 | 2.782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SNDK | memory_hbm_storage | 1605.45 |  | 1581.588 | 1.5087 | 1558.88 | 1518.99 | 4.088 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.29 |  | 707.4553 | -0.0234 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.885 |  | 70.859 | 0.0366 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.84 |  | 211.5284 | 1.0928 | 207.4 | 205.01 | 0.0935 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.63 |  | 389.8498 | -0.3129 | 400.89 | 392.26 | 0.157 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.58 |  | 324.9803 | -0.1232 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.04 |  | 347.8195 | -0.2241 | 348.76 | 346.23 | 0.0231 | below_vwap | below_vwap |
| AMD | ai_accelerator | 556.075 |  | 551.9117 | 0.7543 | 548.755 | 526.6 | 2.782 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.965 |  | 420.9407 | 0.2433 | 419.42 | 414.87 | 0.1185 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.27 |  | 553.7004 | 0.8253 | 551.02 | 540.105 | 0.0627 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.91 |  | 586.1333 | 0.6443 | 581.9 | 572.01 | 0.0288 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.53 |  | 391.8058 | 1.461 | 387.635 | 380.205 | 0.6817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 967.505 |  | 968.4563 | -0.0982 | 963.41 | 936.99 | 1.2403 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 213.01 |  | 211.472 | 0.7273 | 207.06 | 202.18 | 0.2347 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 440.25 |  | 442.3685 | -0.4789 | 435.98 | 415.79 | 4.7791 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.31 |  | 48.9636 | -1.3348 | 48.96 | 47.01 | 0.0414 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.065 |  | 31.1579 | -0.2982 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 748.4 |  | 748.512 | -0.015 | 747.68 | 746.425 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.1 |  | 294.9823 | -0.2991 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.025 |  | 126.5312 | -1.1904 | 128.79 | 125.83 | 3.0954 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.605 |  | 83.3753 | -0.9238 | 83.22 | 79.6 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 303.12 |  | 299.5433 | 1.194 | 297.69 | 293.905 | 0.9237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.08 |  | 407.868 | 0.052 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.96 |  | 641.4002 | 0.3991 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 998.71 |  | 1004.9462 | -0.6205 | 1036.605 | 998.94 | 2.1107 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.01 |  | 473.8859 | 0.2372 | 473.865 | 466.83 | 0.1747 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 143.06 |  | 142.9602 | 0.0698 | 143.27 | 141.04 | 5.0468 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.25 |  | 174.9359 | 0.1796 | 175.265 | 171.06 | 0.194 | watch_only | none |
| COHR | ai_networking_optical | 316.07 |  | 316.0239 | 0.0146 | 317.93 | 306.89 | 2.3444 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 827.735 |  | 838.34 | -1.265 | 840.47 | 814.62 | 1.0873 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 403.23 |  | 405.2574 | -0.5003 | 407.12 | 397.835 | 1.979 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.15 |  | 114.0971 | -2.583 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.94 |  | 329.8826 | 0.6237 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1804.19 |  | 1799.0181 | 0.2875 | 1786.525 | 1767.54 | 0.0205 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.72 |  | 558.7627 | 0.3503 | 559.22 | 544.305 | 0.1338 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.965 |  | 319.4786 | 0.4653 | 317.72 | 311.31 | 4.1001 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.46 |  | 216.1347 | 0.1505 | 215.465 | 210.975 | 0.0739 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 371.72 |  | 371.6485 | 0.0192 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.05 |  | 295.3671 | 0.2312 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.36 |  | 67.4708 | -0.1643 | 66.73 | 64.98 | 0.1781 | below_vwap | below_vwap |
| COHU | semiconductor_test_packaging | 55.425 |  | 55.6536 | -0.4107 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.01 |  | 138.8576 | 0.1097 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 348.03 |  | 345.1786 | 0.8261 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.06 |  | 507.3999 | 0.5243 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.13 |  | 297.8453 | 0.0956 | 300.24 | 297.585 | 0.0973 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 30.16 |  | 30.6935 | -1.738 | 30.78 | 29.46 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.67 |  | 42.4901 | -1.9301 | 42.29 | 40.305 | 0.024 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.68 |  | 23.9987 | -1.3281 | 24.255 | 23.58 | 0.0422 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1605.45 |  | 1581.588 | 1.5087 | 1558.88 | 1518.99 | 4.088 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 557.52 |  | 556.1558 | 0.2453 | 548.14 | 526.22 | 1.704 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 905.72 |  | 909.5557 | -0.4217 | 899.59 | 860.605 | 1.9123 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 242.82 |  | 244.2037 | -0.5666 | 248.43 | 244.47 | 0.0124 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.05 |  | 630.4152 | -0.6924 | 647.02 | 632.77 | 0.0623 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.67 |  | 285.5847 | -0.3203 | 286.39 | 280.275 | 2.7541 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.82 |  | 166.7384 | 0.0489 | 166.63 | 162.08 | 0.1619 | buy_precheck_manual_confirm | none |
