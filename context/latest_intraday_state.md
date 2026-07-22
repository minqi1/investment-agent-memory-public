# Intraday State

- Generated at: `2026-07-23T02:37:51+08:00`
- Market time ET: `2026-07-22T14:37:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 23, 'manual_confirm_candidate': 7, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 16, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707 |  | 707.4632 | -0.0655 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.7 |  | 553.5516 | 0.7494 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.55 |  | 586.0845 | 0.5913 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.41 |  | 748.5165 | -0.0142 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.73 |  | 211.4941 | 1.0572 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 557.7 |  | 553.5516 | 0.7494 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.55 |  | 586.0845 | 0.5913 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.41 |  | 211.4526 | 0.4528 | 207.06 | 202.18 | 0.1177 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1802.08 |  | 1798.9581 | 0.1735 | 1786.525 | 1767.54 | 0.0583 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 216.16 |  | 216.131 | 0.0134 | 215.465 | 210.975 | 0.0416 | buy_precheck_manual_confirm | none |
| 7 | LIN | industrial_gases | 510.63 |  | 507.3448 | 0.6475 | 507.545 | 505.59 | 0.0607 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 216.16 |  | 216.131 | 0.0134 | 215.465 | 210.975 | 0.0416 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1802.08 |  | 1798.9581 | 0.1735 | 1786.525 | 1767.54 | 0.0583 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 510.63 |  | 507.3448 | 0.6475 | 507.545 | 505.59 | 0.0607 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.7 |  | 553.5516 | 0.7494 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.55 |  | 586.0845 | 0.5913 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 212.41 |  | 211.4526 | 0.4528 | 207.06 | 202.18 | 0.1177 | buy_precheck_manual_confirm | none |
| 7 | TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | NVDA | ai_accelerator | 213.73 |  | 211.4941 | 1.0572 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 9 | JCI | data_center_power_cooling | 143.085 |  | 142.9591 | 0.0881 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 407.975 |  | 407.8697 | 0.0258 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 643.51 |  | 641.2962 | 0.3452 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ONTO | semiconductor_test_packaging | 295.39 |  | 295.3661 | 0.0081 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 298.42 |  | 297.8427 | 0.1938 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AMAT | semiconductor_equipment | 559.85 |  | 558.746 | 0.1976 | 559.22 | 544.305 | 3.0294 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 421.595 |  | 420.9192 | 0.1605 | 419.42 | 414.87 | 0.6025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SNDK | memory_hbm_storage | 1584.9 |  | 1581.2746 | 0.2293 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ANET | ai_networking_optical | 175.185 |  | 174.9317 | 0.1448 | 175.265 | 171.06 | 2.7285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 320.93 |  | 319.4491 | 0.4636 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ALAB | ai_networking_optical | 331.07 |  | 329.8099 | 0.3821 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 554.66 |  | 551.8283 | 0.5131 | 548.755 | 526.6 | 2.0679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.73 |  | 211.4941 | 1.0572 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 557.7 |  | 553.5516 | 0.7494 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.55 |  | 586.0845 | 0.5913 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 212.41 |  | 211.4526 | 0.4528 | 207.06 | 202.18 | 0.1177 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1802.08 |  | 1798.9581 | 0.1735 | 1786.525 | 1767.54 | 0.0583 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 216.16 |  | 216.131 | 0.0134 | 215.465 | 210.975 | 0.0416 | buy_precheck_manual_confirm | none |
| 7 | LIN | industrial_gases | 510.63 |  | 507.3448 | 0.6475 | 507.545 | 505.59 | 0.0607 | buy_precheck_manual_confirm | none |
| 8 | MU | memory_hbm_storage | 966.64 |  | 968.4863 | -0.1906 | 963.41 | 936.99 | 0.419 | below_vwap | below_vwap,spread_too_wide |
| 9 | WDC | memory_hbm_storage | 555.72 |  | 556.17 | -0.0809 | 548.14 | 526.22 | 0.1116 | below_vwap | below_vwap |
| 10 | STX | memory_hbm_storage | 903.89 |  | 909.5669 | -0.6241 | 899.59 | 860.605 | 4.1642 | below_vwap | below_vwap,spread_too_wide |
| 11 | QQQ | market_regime | 707 |  | 707.4632 | -0.0655 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 748.41 |  | 748.5165 | -0.0142 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 13 | TER | semiconductor_test_packaging | 370.62 |  | 371.6625 | -0.2805 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | DELL | ai_server_oem | 440.215 |  | 442.4043 | -0.4949 | 435.98 | 415.79 | 2.183 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMKR | semiconductor_test_packaging | 67.3 |  | 67.472 | -0.255 | 66.73 | 64.98 | 2.4666 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMCI | ai_server_oem | 30.985 |  | 31.1603 | -0.5624 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| 17 | TSM | foundry | 421.595 |  | 420.9192 | 0.1605 | 419.42 | 414.87 | 0.6025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 554.66 |  | 551.8283 | 0.5131 | 548.755 | 526.6 | 2.0679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SNDK | memory_hbm_storage | 1584.9 |  | 1581.2746 | 0.2293 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707 |  | 707.4632 | -0.0655 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.78 |  | 70.8599 | -0.1128 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 213.73 |  | 211.4941 | 1.0572 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.545 |  | 389.8877 | -0.3444 | 400.89 | 392.26 | 0.5173 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 323.99 |  | 324.9876 | -0.307 | 328.865 | 325.74 | 0.0864 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.6 |  | 347.8417 | -0.357 | 348.76 | 346.23 | 0.026 | below_vwap | below_vwap |
| AMD | ai_accelerator | 554.66 |  | 551.8283 | 0.5131 | 548.755 | 526.6 | 2.0679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.595 |  | 420.9192 | 0.1605 | 419.42 | 414.87 | 0.6025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.7 |  | 553.5516 | 0.7494 | 551.02 | 540.105 | 0.0377 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.55 |  | 586.0845 | 0.5913 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.91 |  | 391.7033 | 1.3292 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 966.64 |  | 968.4863 | -0.1906 | 963.41 | 936.99 | 0.419 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 212.41 |  | 211.4526 | 0.4528 | 207.06 | 202.18 | 0.1177 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 440.215 |  | 442.4043 | -0.4949 | 435.98 | 415.79 | 2.183 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.37 |  | 48.9812 | -1.2478 | 48.96 | 47.01 | 0.062 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.985 |  | 31.1603 | -0.5624 | 30.66 | 28.52 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 748.41 |  | 748.5165 | -0.0142 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 294.105 |  | 295.0053 | -0.3052 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 124.94 |  | 126.5561 | -1.277 | 128.79 | 125.83 | 0.7203 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.62 |  | 83.3974 | -0.9321 | 83.22 | 79.6 | 2.917 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.47 |  | 299.4408 | 1.0116 | 297.69 | 293.905 | 1.7688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.975 |  | 407.8697 | 0.0258 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.51 |  | 641.2962 | 0.3452 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 997.5 |  | 1005.1229 | -0.7584 | 1036.605 | 998.94 | 2.9724 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.72 |  | 473.8564 | 0.1823 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.085 |  | 142.9591 | 0.0881 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.185 |  | 174.9317 | 0.1448 | 175.265 | 171.06 | 2.7285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.115 |  | 316.0356 | -0.2913 | 317.93 | 306.89 | 0.6855 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 825.32 |  | 838.4869 | -1.5703 | 840.47 | 814.62 | 1.099 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.85 |  | 405.3331 | -0.6126 | 407.12 | 397.835 | 2.2217 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.5 |  | 114.1665 | -3.2116 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 331.07 |  | 329.8099 | 0.3821 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1802.08 |  | 1798.9581 | 0.1735 | 1786.525 | 1767.54 | 0.0583 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.85 |  | 558.746 | 0.1976 | 559.22 | 544.305 | 3.0294 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.93 |  | 319.4491 | 0.4636 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.16 |  | 216.131 | 0.0134 | 215.465 | 210.975 | 0.0416 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 370.62 |  | 371.6625 | -0.2805 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.39 |  | 295.3661 | 0.0081 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.3 |  | 67.472 | -0.255 | 66.73 | 64.98 | 2.4666 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.415 |  | 55.6592 | -0.4387 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.68 |  | 138.87 | -0.1368 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 347.81 |  | 344.7171 | 0.8972 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.63 |  | 507.3448 | 0.6475 | 507.545 | 505.59 | 0.0607 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 298.42 |  | 297.8427 | 0.1938 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.99 |  | 30.7088 | -2.3408 | 30.78 | 29.46 | 0.1334 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.475 |  | 42.5235 | -2.4657 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.565 |  | 24.0058 | -1.8363 | 24.255 | 23.58 | 0.0849 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1584.9 |  | 1581.2746 | 0.2293 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 555.72 |  | 556.17 | -0.0809 | 548.14 | 526.22 | 0.1116 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 903.89 |  | 909.5669 | -0.6241 | 899.59 | 860.605 | 4.1642 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 243.035 |  | 244.2218 | -0.4859 | 248.43 | 244.47 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.22 |  | 630.4654 | -0.6734 | 647.02 | 632.77 | 0.2331 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 284.615 |  | 285.5899 | -0.3414 | 286.39 | 280.275 | 3.0287 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.385 |  | 166.7389 | -0.2123 | 166.63 | 162.08 | 1.3282 | below_vwap | below_vwap,spread_too_wide |
