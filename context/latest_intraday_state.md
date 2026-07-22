# Intraday State

- Generated at: `2026-07-23T02:17:54+08:00`
- Market time ET: `2026-07-22T14:17:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `52`
- stale_count: `4`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 20, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.94 |  | 707.495 | -0.0784 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.56 |  | 553.3241 | 0.7655 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.63 |  | 585.907 | 0.6354 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.16 |  | 748.5283 | -0.0492 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.68 |  | 211.4245 | 1.0668 | 207.4 | 205.01 | 0.0515 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.995 |  | 420.846 | 0.273 | 419.42 | 414.87 | 0.1114 | buy_precheck_manual_confirm | none |
| 3 | SNDK | memory_hbm_storage | 1591.485 |  | 1580.805 | 0.6756 | 1558.88 | 1518.99 | 0.1068 | buy_precheck_manual_confirm | none |
| 4 | WDC | memory_hbm_storage | 556.725 |  | 556.1855 | 0.097 | 548.14 | 526.22 | 0.097 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 557.56 |  | 553.3241 | 0.7655 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 589.63 |  | 585.907 | 0.6354 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 212.31 |  | 211.4097 | 0.4259 | 207.06 | 202.18 | 0.2402 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.18 |  | 216.1313 | 0.0225 | 215.465 | 210.975 | 0.0648 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 301.55 |  | 299.2803 | 0.7584 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 216.18 |  | 216.1313 | 0.0225 | 215.465 | 210.975 | 0.0648 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.995 |  | 420.846 | 0.273 | 419.42 | 414.87 | 0.1114 | buy_precheck_manual_confirm | none |
| 3 | WDC | memory_hbm_storage | 556.725 |  | 556.1855 | 0.097 | 548.14 | 526.22 | 0.097 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.56 |  | 553.3241 | 0.7655 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.63 |  | 585.907 | 0.6354 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 6 | VRT | data_center_power_cooling | 301.55 |  | 299.2803 | 0.7584 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| 7 | SNDK | memory_hbm_storage | 1591.485 |  | 1580.805 | 0.6756 | 1558.88 | 1518.99 | 0.1068 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 212.31 |  | 211.4097 | 0.4259 | 207.06 | 202.18 | 0.2402 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 474.32 |  | 473.7821 | 0.1135 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | NVDA | ai_accelerator | 213.68 |  | 211.4245 | 1.0668 | 207.4 | 205.01 | 0.0515 | buy_precheck_manual_confirm | none |
| 11 | ANET | ai_networking_optical | 175.15 |  | 174.92 | 0.1315 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 143.19 |  | 142.9461 | 0.1706 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 297.94 |  | 297.8226 | 0.0394 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AMAT | semiconductor_equipment | 560.23 |  | 558.6481 | 0.2832 | 559.22 | 544.305 | 3.0184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MU | memory_hbm_storage | 969.61 |  | 968.4773 | 0.117 | 963.41 | 936.99 | 1.4439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | PWR | data_center_power_cooling | 642.425 |  | 641.0152 | 0.2199 | 641.19 | 628.17 | 3.7218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | STX | memory_hbm_storage | 910.3 |  | 909.542 | 0.0833 | 899.59 | 860.605 | 1.2479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ASML | semiconductor_equipment | 1800.845 |  | 1798.7994 | 0.1137 | 1786.525 | 1767.54 | 2.7754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LRCX | semiconductor_equipment | 321.2 |  | 319.3289 | 0.586 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | LIN | industrial_gases | 510.11 |  | 507.3339 | 0.5472 | 507.545 | 505.59 | 4.354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.68 |  | 211.4245 | 1.0668 | 207.4 | 205.01 | 0.0515 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.995 |  | 420.846 | 0.273 | 419.42 | 414.87 | 0.1114 | buy_precheck_manual_confirm | none |
| 3 | SNDK | memory_hbm_storage | 1591.485 |  | 1580.805 | 0.6756 | 1558.88 | 1518.99 | 0.1068 | buy_precheck_manual_confirm | none |
| 4 | WDC | memory_hbm_storage | 556.725 |  | 556.1855 | 0.097 | 548.14 | 526.22 | 0.097 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 557.56 |  | 553.3241 | 0.7655 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 589.63 |  | 585.907 | 0.6354 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 212.31 |  | 211.4097 | 0.4259 | 207.06 | 202.18 | 0.2402 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.18 |  | 216.1313 | 0.0225 | 215.465 | 210.975 | 0.0648 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 301.55 |  | 299.2803 | 0.7584 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| 10 | QQQ | market_regime | 706.94 |  | 707.495 | -0.0784 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 748.16 |  | 748.5283 | -0.0492 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |
| 12 | TER | semiconductor_test_packaging | 371.015 |  | 371.6892 | -0.1814 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | DELL | ai_server_oem | 439.77 |  | 442.473 | -0.6109 | 435.98 | 415.79 | 0.4389 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMKR | semiconductor_test_packaging | 67.24 |  | 67.4762 | -0.35 | 66.73 | 64.98 | 3.6734 | below_vwap | below_vwap,spread_too_wide |
| 15 | SMCI | ai_server_oem | 30.91 |  | 31.1672 | -0.8253 | 30.66 | 28.52 | 0.0647 | below_vwap | below_vwap |
| 16 | MU | memory_hbm_storage | 969.61 |  | 968.4773 | 0.117 | 963.41 | 936.99 | 1.4439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMD | ai_accelerator | 553.825 |  | 551.7824 | 0.3702 | 548.755 | 526.6 | 1.8905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 474.32 |  | 473.7821 | 0.1135 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | STX | memory_hbm_storage | 910.3 |  | 909.542 | 0.0833 | 899.59 | 860.605 | 1.2479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 396.47 |  | 391.4061 | 1.2938 | 387.635 | 380.205 | 0.9433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.94 |  | 707.495 | -0.0784 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.76 |  | 70.8649 | -0.148 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.68 |  | 211.4245 | 1.0668 | 207.4 | 205.01 | 0.0515 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.56 |  | 390.0029 | -0.6264 | 400.89 | 392.26 | 0.2761 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.95 |  | 325.0331 | -0.3332 | 328.865 | 325.74 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.41 |  | 347.8858 | -0.4242 | 348.76 | 346.23 | 0.0173 | below_vwap | below_vwap |
| AMD | ai_accelerator | 553.825 |  | 551.7824 | 0.3702 | 548.755 | 526.6 | 1.8905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.995 |  | 420.846 | 0.273 | 419.42 | 414.87 | 0.1114 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.56 |  | 553.3241 | 0.7655 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.63 |  | 585.907 | 0.6354 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.47 |  | 391.4061 | 1.2938 | 387.635 | 380.205 | 0.9433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 969.61 |  | 968.4773 | 0.117 | 963.41 | 936.99 | 1.4439 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.31 |  | 211.4097 | 0.4259 | 207.06 | 202.18 | 0.2402 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 439.77 |  | 442.473 | -0.6109 | 435.98 | 415.79 | 0.4389 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.47 |  | 49.0092 | -1.1001 | 48.96 | 47.01 | 0.0413 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.91 |  | 31.1672 | -0.8253 | 30.66 | 28.52 | 0.0647 | below_vwap | below_vwap |
| SPY | market_regime | 748.16 |  | 748.5283 | -0.0492 | 747.68 | 746.425 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 294.08 |  | 295.0568 | -0.3311 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125 |  | 126.5962 | -1.2608 | 128.79 | 125.83 | 3.016 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.355 |  | 83.4702 | -1.336 | 83.22 | 79.6 | 3.4849 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.55 |  | 299.2803 | 0.7584 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.28 |  | 407.8889 | -0.1493 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 642.425 |  | 641.0152 | 0.2199 | 641.19 | 628.17 | 3.7218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 992.22 |  | 1005.5171 | -1.3224 | 1036.605 | 998.94 | 4.0314 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.32 |  | 473.7821 | 0.1135 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.19 |  | 142.9461 | 0.1706 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.15 |  | 174.92 | 0.1315 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 314.47 |  | 316.09 | -0.5125 | 317.93 | 306.89 | 0.5915 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 825.72 |  | 838.97 | -1.5793 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 401.89 |  | 405.451 | -0.8783 | 407.12 | 397.835 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 111.33 |  | 114.2483 | -2.5544 | 117.185 | 113.68 | 4.0959 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 331.44 |  | 329.6978 | 0.5284 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1800.845 |  | 1798.7994 | 0.1137 | 1786.525 | 1767.54 | 2.7754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.23 |  | 558.6481 | 0.2832 | 559.22 | 544.305 | 3.0184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.2 |  | 319.3289 | 0.586 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.18 |  | 216.1313 | 0.0225 | 215.465 | 210.975 | 0.0648 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 371.015 |  | 371.6892 | -0.1814 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.06 |  | 295.3682 | 0.2342 | 298.42 | 288.335 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 67.24 |  | 67.4762 | -0.35 | 66.73 | 64.98 | 3.6734 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.59 |  | 55.6828 | -0.1667 | 56.2 | 54.45 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.76 |  | 138.8771 | -0.0844 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 348.115 |  | 344.4688 | 1.0585 | 345.675 | 331.945 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 510.11 |  | 507.3339 | 0.5472 | 507.545 | 505.59 | 4.354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.94 |  | 297.8226 | 0.0394 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.08 |  | 30.7335 | -2.1262 | 30.78 | 29.46 | 0.0665 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.5 |  | 42.5654 | -2.5029 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.57 |  | 24.0285 | -1.9081 | 24.255 | 23.58 | 0.0849 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1591.485 |  | 1580.805 | 0.6756 | 1558.88 | 1518.99 | 0.1068 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 556.725 |  | 556.1855 | 0.097 | 548.14 | 526.22 | 0.097 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 910.3 |  | 909.542 | 0.0833 | 899.59 | 860.605 | 1.2479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 242.82 |  | 244.2633 | -0.5909 | 248.43 | 244.47 | 0.0494 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.07 |  | 630.7475 | -0.7416 | 647.02 | 632.77 | 0.3035 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.6 |  | 285.6201 | -0.3571 | 286.39 | 280.275 | 0.123 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 166.18 |  | 166.747 | -0.34 | 166.63 | 162.08 | 0.674 | below_vwap | below_vwap,spread_too_wide |
