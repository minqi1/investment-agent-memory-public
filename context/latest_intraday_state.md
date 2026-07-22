# Intraday State

- Generated at: `2026-07-23T02:13:53+08:00`
- Market time ET: `2026-07-22T14:13:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 19, 'manual_confirm_candidate': 8, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.08 |  | 707.5025 | -0.0597 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.8 |  | 553.2933 | 0.9953 | 551.02 | 540.105 | 0.0626 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.92 |  | 585.8698 | 0.6913 | 581.9 | 572.01 | 0.0525 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.11 |  | 748.5332 | -0.0565 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.645 |  | 211.4158 | 1.0544 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 555.93 |  | 551.7694 | 0.7541 | 548.755 | 526.6 | 0.3004 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 557.52 |  | 556.1831 | 0.2404 | 548.14 | 526.22 | 0.1525 | buy_precheck_manual_confirm | none |
| 4 | STX | memory_hbm_storage | 910.995 |  | 909.5073 | 0.1636 | 899.59 | 860.605 | 0.2788 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 558.8 |  | 553.2933 | 0.9953 | 551.02 | 540.105 | 0.0626 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 589.92 |  | 585.8698 | 0.6913 | 581.9 | 572.01 | 0.0525 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.38 |  | 299.2519 | 0.7111 | 297.69 | 293.905 | 0.0962 | buy_precheck_manual_confirm | none |
| 8 | AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 910.995 |  | 909.5073 | 0.1636 | 899.59 | 860.605 | 0.2788 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.92 |  | 585.8698 | 0.6913 | 581.9 | 572.01 | 0.0525 | buy_precheck_manual_confirm | none |
| 4 | WDC | memory_hbm_storage | 557.52 |  | 556.1831 | 0.2404 | 548.14 | 526.22 | 0.1525 | buy_precheck_manual_confirm | none |
| 5 | VRT | data_center_power_cooling | 301.38 |  | 299.2519 | 0.7111 | 297.69 | 293.905 | 0.0962 | buy_precheck_manual_confirm | none |
| 6 | AMD | ai_accelerator | 555.93 |  | 551.7694 | 0.7541 | 548.755 | 526.6 | 0.3004 | buy_precheck_manual_confirm | none |
| 7 | TT | data_center_power_cooling | 474.72 |  | 473.7601 | 0.2026 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SOXX | semiconductor_index | 558.8 |  | 553.2933 | 0.9953 | 551.02 | 540.105 | 0.0626 | buy_precheck_manual_confirm | none |
| 9 | TER | semiconductor_test_packaging | 371.875 |  | 371.6938 | 0.0487 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | NVDA | ai_accelerator | 213.645 |  | 211.4158 | 1.0544 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | JCI | data_center_power_cooling | 143.22 |  | 142.9424 | 0.1942 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 296.06 |  | 295.3682 | 0.2342 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 297.91 |  | 297.8226 | 0.0294 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | MU | memory_hbm_storage | 969.62 |  | 968.4537 | 0.1204 | 963.41 | 936.99 | 0.5157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 642.16 |  | 640.9877 | 0.1829 | 641.19 | 628.17 | 3.9928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TSM | foundry | 421.67 |  | 420.8363 | 0.1981 | 419.42 | 414.87 | 0.4506 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | KLAC | semiconductor_equipment | 216.51 |  | 216.1293 | 0.1762 | 215.465 | 210.975 | 4.2723 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ANET | ai_networking_optical | 175.13 |  | 174.9194 | 0.1204 | 175.265 | 171.06 | 2.6894 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LIN | industrial_gases | 509.77 |  | 507.331 | 0.4808 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 139.01 |  | 138.876 | 0.0965 | 140.09 | 135.555 | 0.3669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.645 |  | 211.4158 | 1.0544 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 555.93 |  | 551.7694 | 0.7541 | 548.755 | 526.6 | 0.3004 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 557.52 |  | 556.1831 | 0.2404 | 548.14 | 526.22 | 0.1525 | buy_precheck_manual_confirm | none |
| 4 | STX | memory_hbm_storage | 910.995 |  | 909.5073 | 0.1636 | 899.59 | 860.605 | 0.2788 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 558.8 |  | 553.2933 | 0.9953 | 551.02 | 540.105 | 0.0626 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 589.92 |  | 585.8698 | 0.6913 | 581.9 | 572.01 | 0.0525 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.38 |  | 299.2519 | 0.7111 | 297.69 | 293.905 | 0.0962 | buy_precheck_manual_confirm | none |
| 8 | AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| 9 | QQQ | market_regime | 707.08 |  | 707.5025 | -0.0597 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 748.11 |  | 748.5332 | -0.0565 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 11 | DELL | ai_server_oem | 440.26 |  | 442.4868 | -0.5032 | 435.98 | 415.79 | 0.5292 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMCI | ai_server_oem | 30.84 |  | 31.1687 | -1.0546 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 13 | MU | memory_hbm_storage | 969.62 |  | 968.4537 | 0.1204 | 963.41 | 936.99 | 0.5157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 421.67 |  | 420.8363 | 0.1981 | 419.42 | 414.87 | 0.4506 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 474.72 |  | 473.7601 | 0.2026 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1591 |  | 1580.7058 | 0.6512 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MRVL | custom_silicon_networking | 212.38 |  | 211.401 | 0.4631 | 207.06 | 202.18 | 1.6339 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 371.875 |  | 371.6938 | 0.0487 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 396.52 |  | 391.337 | 1.3244 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TQQQ | leveraged_tool | 70.86 |  | 70.8654 | -0.0076 | 70.43 | 69.81 | 0.0282 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.08 |  | 707.5025 | -0.0597 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.86 |  | 70.8654 | -0.0076 | 70.43 | 69.81 | 0.0282 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.645 |  | 211.4158 | 1.0544 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.235 |  | 390.0291 | -0.7164 | 400.89 | 392.26 | 0.3331 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.855 |  | 325.0388 | -0.3642 | 328.865 | 325.74 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.69 |  | 347.8963 | -0.3467 | 348.76 | 346.23 | 0.0144 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555.93 |  | 551.7694 | 0.7541 | 548.755 | 526.6 | 0.3004 | buy_precheck_manual_confirm | none |
| TSM | foundry | 421.67 |  | 420.8363 | 0.1981 | 419.42 | 414.87 | 0.4506 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.8 |  | 553.2933 | 0.9953 | 551.02 | 540.105 | 0.0626 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.92 |  | 585.8698 | 0.6913 | 581.9 | 572.01 | 0.0525 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.52 |  | 391.337 | 1.3244 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 969.62 |  | 968.4537 | 0.1204 | 963.41 | 936.99 | 0.5157 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.38 |  | 211.401 | 0.4631 | 207.06 | 202.18 | 1.6339 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 440.26 |  | 442.4868 | -0.5032 | 435.98 | 415.79 | 0.5292 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.55 |  | 49.0131 | -0.9448 | 48.96 | 47.01 | 0.0412 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.84 |  | 31.1687 | -1.0546 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748.11 |  | 748.5332 | -0.0565 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.97 |  | 295.0794 | -0.376 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.065 |  | 126.6045 | -1.216 | 128.79 | 125.83 | 3.0064 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.505 |  | 83.4789 | -1.1666 | 83.22 | 79.6 | 0.0848 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 301.38 |  | 299.2519 | 0.7111 | 297.69 | 293.905 | 0.0962 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.31 |  | 407.8963 | -0.1437 | 409.095 | 398.16 | 0.0663 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 642.16 |  | 640.9877 | 0.1829 | 641.19 | 628.17 | 3.9928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 992.14 |  | 1005.6123 | -1.3397 | 1036.605 | 998.94 | 0.9434 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.72 |  | 473.7601 | 0.2026 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.22 |  | 142.9424 | 0.1942 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.13 |  | 174.9194 | 0.1204 | 175.265 | 171.06 | 2.6894 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.03 |  | 316.1 | -0.3385 | 317.93 | 306.89 | 2.8251 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 825.795 |  | 839.0578 | -1.5807 | 840.47 | 814.62 | 4.8438 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.71 |  | 405.487 | -0.6849 | 407.12 | 397.835 | 1.8326 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.495 |  | 114.2592 | -2.4192 | 117.185 | 113.68 | 4.4755 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 332.23 |  | 329.6762 | 0.7747 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1802.96 |  | 1798.7807 | 0.2323 | 1786.525 | 1767.54 | 2.6623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.76 |  | 558.6403 | 0.3794 | 559.22 | 544.305 | 3.0922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.83 |  | 319.2748 | 0.8003 | 317.72 | 311.31 | 3.8623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.51 |  | 216.1293 | 0.1762 | 215.465 | 210.975 | 4.2723 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.875 |  | 371.6938 | 0.0487 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.06 |  | 295.3682 | 0.2342 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.62 |  | 67.4781 | 0.2103 | 66.73 | 64.98 | 0.1035 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 55.59 |  | 55.6828 | -0.1667 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.01 |  | 138.876 | 0.0965 | 140.09 | 135.555 | 0.3669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 348.115 |  | 344.4688 | 1.0585 | 345.675 | 331.945 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 509.77 |  | 507.331 | 0.4808 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.91 |  | 297.8226 | 0.0294 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.16 |  | 30.7365 | -1.8756 | 30.78 | 29.46 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.56 |  | 42.57 | -2.3725 | 42.29 | 40.305 | 0.0722 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.66 |  | 24.0418 | -1.588 | 24.255 | 23.58 | 0.0845 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1591 |  | 1580.7058 | 0.6512 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 557.52 |  | 556.1831 | 0.2404 | 548.14 | 526.22 | 0.1525 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 910.995 |  | 909.5073 | 0.1636 | 899.59 | 860.605 | 0.2788 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 242.73 |  | 244.2805 | -0.6347 | 248.43 | 244.47 | 0.0082 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.245 |  | 630.7772 | -0.7185 | 647.02 | 632.77 | 0.2204 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.6 |  | 285.6242 | -0.3586 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 165.475 |  | 166.7784 | -0.7815 | 166.63 | 162.08 | 1.6317 | below_vwap | below_vwap,spread_too_wide |
