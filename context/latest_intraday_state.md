# Intraday State

- Generated at: `2026-07-23T02:21:52+08:00`
- Market time ET: `2026-07-22T14:21:53-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 22, 'manual_confirm_candidate': 5, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.835 |  | 707.485 | -0.0919 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.93 |  | 553.3638 | 0.8252 | 551.02 | 540.105 | 0.0341 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.54 |  | 585.9409 | 0.6143 | 581.9 | 572.01 | 0.0509 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.41 |  | 748.5256 | -0.0154 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.685 |  | 211.4395 | 1.062 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 557.93 |  | 553.3638 | 0.8252 | 551.02 | 540.105 | 0.0341 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.54 |  | 585.9409 | 0.6143 | 581.9 | 572.01 | 0.0509 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.34 |  | 211.4153 | 0.4374 | 207.06 | 202.18 | 0.2213 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 396.64 |  | 391.5487 | 1.3003 | 387.635 | 380.205 | 0.2471 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 589.54 |  | 585.9409 | 0.6143 | 581.9 | 572.01 | 0.0509 | buy_precheck_manual_confirm | none |
| 2 | MRVL | custom_silicon_networking | 212.34 |  | 211.4153 | 0.4374 | 207.06 | 202.18 | 0.2213 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.34 |  | 473.8087 | 0.1121 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | SOXX | semiconductor_index | 557.93 |  | 553.3638 | 0.8252 | 551.02 | 540.105 | 0.0341 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 175.34 |  | 174.9229 | 0.2384 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | NVDA | ai_accelerator | 213.685 |  | 211.4395 | 1.062 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 143.15 |  | 142.9527 | 0.138 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ONTO | semiconductor_test_packaging | 295.43 |  | 295.3687 | 0.0207 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | APD | industrial_gases | 298.2 |  | 297.8263 | 0.1255 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | MU | memory_hbm_storage | 970.41 |  | 968.5108 | 0.1961 | 963.41 | 936.99 | 3.0709 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 422.1 |  | 420.8596 | 0.2947 | 419.42 | 414.87 | 0.3743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | AVGO | custom_silicon_networking | 396.64 |  | 391.5487 | 1.3003 | 387.635 | 380.205 | 0.2471 | buy_precheck_manual_confirm | none |
| 13 | WDC | memory_hbm_storage | 557 |  | 556.1848 | 0.1466 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 216.355 |  | 216.1321 | 0.1031 | 215.465 | 210.975 | 4.2754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 553.61 |  | 551.7906 | 0.3297 | 548.755 | 526.6 | 1.8912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 912.74 |  | 909.5965 | 0.3456 | 899.59 | 860.605 | 0.9378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1801.13 |  | 1798.8602 | 0.1262 | 1786.525 | 1767.54 | 2.6095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 321.245 |  | 319.3631 | 0.5893 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMAT | semiconductor_equipment | 560.65 |  | 558.6667 | 0.355 | 559.22 | 544.305 | 3.0928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SNDK | memory_hbm_storage | 1592.43 |  | 1581.0872 | 0.7174 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.685 |  | 211.4395 | 1.062 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 557.93 |  | 553.3638 | 0.8252 | 551.02 | 540.105 | 0.0341 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.54 |  | 585.9409 | 0.6143 | 581.9 | 572.01 | 0.0509 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.34 |  | 211.4153 | 0.4374 | 207.06 | 202.18 | 0.2213 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 396.64 |  | 391.5487 | 1.3003 | 387.635 | 380.205 | 0.2471 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 706.835 |  | 707.485 | -0.0919 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| 7 | SPY | market_regime | 748.41 |  | 748.5256 | -0.0154 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 8 | TER | semiconductor_test_packaging | 371.39 |  | 371.671 | -0.0756 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | DELL | ai_server_oem | 439.9 |  | 442.4529 | -0.577 | 435.98 | 415.79 | 0.1432 | below_vwap | below_vwap |
| 10 | AMKR | semiconductor_test_packaging | 67.265 |  | 67.4757 | -0.3123 | 66.73 | 64.98 | 3.8653 | below_vwap | below_vwap,spread_too_wide |
| 11 | SMCI | ai_server_oem | 30.9 |  | 31.166 | -0.8535 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 970.41 |  | 968.5108 | 0.1961 | 963.41 | 936.99 | 3.0709 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 422.1 |  | 420.8596 | 0.2947 | 419.42 | 414.87 | 0.3743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 553.61 |  | 551.7906 | 0.3297 | 548.755 | 526.6 | 1.8912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 474.34 |  | 473.8087 | 0.1121 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1592.43 |  | 1581.0872 | 0.7174 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 557 |  | 556.1848 | 0.1466 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 912.74 |  | 909.5965 | 0.3456 | 899.59 | 860.605 | 0.9378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TQQQ | leveraged_tool | 70.83 |  | 70.8646 | -0.0488 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| 20 | ASML | semiconductor_equipment | 1801.13 |  | 1798.8602 | 0.1262 | 1786.525 | 1767.54 | 2.6095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.835 |  | 707.485 | -0.0919 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.83 |  | 70.8646 | -0.0488 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.685 |  | 211.4395 | 1.062 | 207.4 | 205.01 | 0.0468 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.88 |  | 389.9838 | -0.5395 | 400.89 | 392.26 | 0.0361 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.87 |  | 325.0278 | -0.3562 | 328.865 | 325.74 | 0.0185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.415 |  | 347.876 | -0.42 | 348.76 | 346.23 | 0.0087 | below_vwap | below_vwap |
| AMD | ai_accelerator | 553.61 |  | 551.7906 | 0.3297 | 548.755 | 526.6 | 1.8912 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.1 |  | 420.8596 | 0.2947 | 419.42 | 414.87 | 0.3743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.93 |  | 553.3638 | 0.8252 | 551.02 | 540.105 | 0.0341 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.54 |  | 585.9409 | 0.6143 | 581.9 | 572.01 | 0.0509 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.64 |  | 391.5487 | 1.3003 | 387.635 | 380.205 | 0.2471 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 970.41 |  | 968.5108 | 0.1961 | 963.41 | 936.99 | 3.0709 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.34 |  | 211.4153 | 0.4374 | 207.06 | 202.18 | 0.2213 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 439.9 |  | 442.4529 | -0.577 | 435.98 | 415.79 | 0.1432 | below_vwap | below_vwap |
| HPE | ai_server_oem | 48.49 |  | 49.0065 | -1.054 | 48.96 | 47.01 | 0.0412 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.9 |  | 31.166 | -0.8535 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748.41 |  | 748.5256 | -0.0154 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 294.24 |  | 295.0377 | -0.2704 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.01 |  | 126.5891 | -1.2475 | 128.79 | 125.83 | 0.056 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.485 |  | 83.4528 | -1.1597 | 83.22 | 79.6 | 2.4247 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.55 |  | 299.3074 | 0.7493 | 297.69 | 293.905 | 1.2005 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.6 |  | 407.8828 | -0.0693 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.93 |  | 641.1851 | 0.4281 | 641.19 | 628.17 | 3.637 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 993.06 |  | 1005.4176 | -1.2291 | 1036.605 | 998.94 | 3.315 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.34 |  | 473.8087 | 0.1121 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.15 |  | 142.9527 | 0.138 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.34 |  | 174.9229 | 0.2384 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 314.76 |  | 316.0863 | -0.4196 | 317.93 | 306.89 | 2.7068 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 826.72 |  | 838.8388 | -1.4447 | 840.47 | 814.62 | 4.0171 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.47 |  | 405.4282 | -0.7296 | 407.12 | 397.835 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 111.35 |  | 114.2286 | -2.52 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.71 |  | 329.7308 | 0.6002 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1801.13 |  | 1798.8602 | 0.1262 | 1786.525 | 1767.54 | 2.6095 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.65 |  | 558.6667 | 0.355 | 559.22 | 544.305 | 3.0928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.245 |  | 319.3631 | 0.5893 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.355 |  | 216.1321 | 0.1031 | 215.465 | 210.975 | 4.2754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.39 |  | 371.671 | -0.0756 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.43 |  | 295.3687 | 0.0207 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.265 |  | 67.4757 | -0.3123 | 66.73 | 64.98 | 3.8653 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.425 |  | 55.6716 | -0.4429 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.68 |  | 138.8754 | -0.1407 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 348.3 |  | 344.5055 | 1.1014 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.11 |  | 507.3339 | 0.5472 | 507.545 | 505.59 | 4.2226 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 298.2 |  | 297.8263 | 0.1255 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.15 |  | 30.728 | -1.8812 | 30.78 | 29.46 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.7 |  | 42.5599 | -2.0204 | 42.29 | 40.305 | 0.0719 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.67 |  | 24.0228 | -1.4686 | 24.255 | 23.58 | 0.0845 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1592.43 |  | 1581.0872 | 0.7174 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 557 |  | 556.1848 | 0.1466 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 912.74 |  | 909.5965 | 0.3456 | 899.59 | 860.605 | 0.9378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 242.83 |  | 244.2485 | -0.5808 | 248.43 | 244.47 | 0.0082 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.28 |  | 630.7117 | -0.7026 | 647.02 | 632.77 | 0.0734 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.67 |  | 285.6061 | -0.3278 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.185 |  | 166.7421 | -0.3341 | 166.63 | 162.08 | 0.6739 | below_vwap | below_vwap,spread_too_wide |
