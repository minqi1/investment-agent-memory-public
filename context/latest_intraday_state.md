# Intraday State

- Generated at: `2026-07-23T01:49:46+08:00`
- Market time ET: `2026-07-22T13:49:47-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_opening_15m_low': 7, 'below_vwap': 16, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.19 |  | 707.4992 | 0.0976 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.63 |  | 553.1512 | 1.1712 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.945 |  | 585.6731 | 0.9001 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.045 |  | 748.5349 | 0.0681 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.95 |  | 211.3155 | 1.2467 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.405 |  | 420.7993 | 0.3816 | 419.42 | 414.87 | 0.322 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 913.315 |  | 909.1081 | 0.4628 | 899.59 | 860.605 | 0.0799 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.63 |  | 553.1512 | 1.1712 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.945 |  | 585.6731 | 0.9001 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.19 |  | 707.4992 | 0.0976 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.045 |  | 748.5349 | 0.0681 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.51 |  | 216.1078 | 0.1861 | 215.465 | 210.975 | 0.0693 | buy_precheck_manual_confirm | none |
| 9 | AMKR | semiconductor_test_packaging | 67.56 |  | 67.4796 | 0.1191 | 66.73 | 64.98 | 0.074 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.15 |  | 70.8599 | 0.4094 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 708.19 |  | 707.4992 | 0.0976 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 749.045 |  | 748.5349 | 0.0681 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.51 |  | 216.1078 | 0.1861 | 215.465 | 210.975 | 0.0693 | buy_precheck_manual_confirm | none |
| 4 | AMKR | semiconductor_test_packaging | 67.56 |  | 67.4796 | 0.1191 | 66.73 | 64.98 | 0.074 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 422.405 |  | 420.7993 | 0.3816 | 419.42 | 414.87 | 0.322 | buy_precheck_manual_confirm | none |
| 6 | STX | memory_hbm_storage | 913.315 |  | 909.1081 | 0.4628 | 899.59 | 860.605 | 0.0799 | buy_precheck_manual_confirm | none |
| 7 | TER | semiconductor_test_packaging | 372.27 |  | 371.6231 | 0.1741 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | NVDA | ai_accelerator | 213.95 |  | 211.3155 | 1.2467 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| 9 | ENTG | semiconductor_materials | 139.2 |  | 138.8511 | 0.2513 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ONTO | semiconductor_test_packaging | 295.92 |  | 295.3654 | 0.1878 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | APD | industrial_gases | 298.56 |  | 297.8025 | 0.2544 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SOXX | semiconductor_index | 559.63 |  | 553.1512 | 1.1712 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 590.945 |  | 585.6731 | 0.9001 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 14 | AMAT | semiconductor_equipment | 559.56 |  | 558.53 | 0.1844 | 559.22 | 544.305 | 2.1285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.805 |  | 473.7177 | 0.4406 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ANET | ai_networking_optical | 175.23 |  | 174.8828 | 0.1985 | 175.265 | 171.06 | 2.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LIN | industrial_gases | 510.02 |  | 507.2786 | 0.5404 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ASML | semiconductor_equipment | 1806.485 |  | 1798.3912 | 0.4501 | 1786.525 | 1767.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 320.91 |  | 319.0912 | 0.57 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | PWR | data_center_power_cooling | 643.81 |  | 640.8042 | 0.4691 | 641.19 | 628.17 | 3.6843 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.95 |  | 211.3155 | 1.2467 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.405 |  | 420.7993 | 0.3816 | 419.42 | 414.87 | 0.322 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 913.315 |  | 909.1081 | 0.4628 | 899.59 | 860.605 | 0.0799 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.63 |  | 553.1512 | 1.1712 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.945 |  | 585.6731 | 0.9001 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.19 |  | 707.4992 | 0.0976 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.045 |  | 748.5349 | 0.0681 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 216.51 |  | 216.1078 | 0.1861 | 215.465 | 210.975 | 0.0693 | buy_precheck_manual_confirm | none |
| 9 | AMKR | semiconductor_test_packaging | 67.56 |  | 67.4796 | 0.1191 | 66.73 | 64.98 | 0.074 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.15 |  | 70.8599 | 0.4094 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 11 | SKHY | memory_hbm_storage | 166.725 |  | 166.8045 | -0.0476 | 166.63 | 162.08 | 1.4875 | below_vwap | below_vwap,spread_too_wide |
| 12 | SMCI | ai_server_oem | 31.18 |  | 31.181 | -0.0032 | 30.66 | 28.52 | 0.0321 | below_vwap | below_vwap |
| 13 | MU | memory_hbm_storage | 974.385 |  | 968.1523 | 0.6438 | 963.41 | 936.99 | 1.1946 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 557.24 |  | 551.5956 | 1.0233 | 548.755 | 526.6 | 2.7762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.805 |  | 473.7177 | 0.4406 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1613.42 |  | 1579.7075 | 2.1341 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 558.035 |  | 556.0393 | 0.3589 | 548.14 | 526.22 | 0.8297 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MRVL | custom_silicon_networking | 213.04 |  | 211.2964 | 0.8252 | 207.06 | 202.18 | 0.7933 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 372.27 |  | 371.6231 | 0.1741 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 397.39 |  | 391.0929 | 1.6101 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.19 |  | 707.4992 | 0.0976 | 705.86 | 703.63 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.15 |  | 70.8599 | 0.4094 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.95 |  | 211.3155 | 1.2467 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.57 |  | 390.19 | -0.6715 | 400.89 | 392.26 | 0.5006 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 323.75 |  | 325.0778 | -0.4085 | 328.865 | 325.74 | 0.0371 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.745 |  | 347.965 | -0.0632 | 348.76 | 346.23 | 0.0115 | below_vwap | below_vwap |
| AMD | ai_accelerator | 557.24 |  | 551.5956 | 1.0233 | 548.755 | 526.6 | 2.7762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.405 |  | 420.7993 | 0.3816 | 419.42 | 414.87 | 0.322 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.63 |  | 553.1512 | 1.1712 | 551.02 | 540.105 | 0.075 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.945 |  | 585.6731 | 0.9001 | 581.9 | 572.01 | 0.0508 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.39 |  | 391.0929 | 1.6101 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 974.385 |  | 968.1523 | 0.6438 | 963.41 | 936.99 | 1.1946 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.04 |  | 211.2964 | 0.8252 | 207.06 | 202.18 | 0.7933 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 444.04 |  | 442.7395 | 0.2937 | 435.98 | 415.79 | 2.9119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.93 |  | 49.0266 | -0.1969 | 48.96 | 47.01 | 0.0409 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.18 |  | 31.181 | -0.0032 | 30.66 | 28.52 | 0.0321 | below_vwap | below_vwap |
| SPY | market_regime | 749.045 |  | 748.5349 | 0.0681 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.51 |  | 295.1077 | -0.2025 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126 |  | 126.6504 | -0.5135 | 128.79 | 125.83 | 0.0635 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.18 |  | 83.5219 | -0.4093 | 83.22 | 79.6 | 2.2121 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.38 |  | 299.1221 | 0.7548 | 297.69 | 293.905 | 1.2078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.47 |  | 407.9238 | -0.1112 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.81 |  | 640.8042 | 0.4691 | 641.19 | 628.17 | 3.6843 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 988.02 |  | 1006.8055 | -1.8659 | 1036.605 | 998.94 | 4.0485 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.805 |  | 473.7177 | 0.4406 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.04 |  | 142.9065 | 0.0934 | 143.27 | 141.04 | 4.8518 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| ANET | ai_networking_optical | 175.23 |  | 174.8828 | 0.1985 | 175.265 | 171.06 | 2.6708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.3 |  | 316.1306 | -0.5791 | 317.93 | 306.89 | 3.0799 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 826.5 |  | 839.9328 | -1.5993 | 840.47 | 814.62 | 4.8433 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.06 |  | 405.6704 | -0.89 | 407.12 | 397.835 | 1.9699 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.98 |  | 114.3828 | -2.9749 | 117.185 | 113.68 | 3.6853 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 333.49 |  | 329.5787 | 1.1868 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.485 |  | 1798.3912 | 0.4501 | 1786.525 | 1767.54 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 559.56 |  | 558.53 | 0.1844 | 559.22 | 544.305 | 2.1285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.91 |  | 319.0912 | 0.57 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.51 |  | 216.1078 | 0.1861 | 215.465 | 210.975 | 0.0693 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 372.27 |  | 371.6231 | 0.1741 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.92 |  | 295.3654 | 0.1878 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.56 |  | 67.4796 | 0.1191 | 66.73 | 64.98 | 0.074 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 55.665 |  | 55.6941 | -0.0523 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.2 |  | 138.8511 | 0.2513 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.5 |  | 344.3997 | 0.9002 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 510.02 |  | 507.2786 | 0.5404 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.56 |  | 297.8025 | 0.2544 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.34 |  | 30.7565 | -1.3542 | 30.78 | 29.46 | 0.1318 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.03 |  | 42.6283 | -1.4034 | 42.29 | 40.305 | 0.0476 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.83 |  | 24.1086 | -1.1557 | 24.255 | 23.58 | 0.0839 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1613.42 |  | 1579.7075 | 2.1341 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 558.035 |  | 556.0393 | 0.3589 | 548.14 | 526.22 | 0.8297 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 913.315 |  | 909.1081 | 0.4628 | 899.59 | 860.605 | 0.0799 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 242.8 |  | 244.3934 | -0.652 | 248.43 | 244.47 | 0.0329 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 627.34 |  | 630.9608 | -0.5739 | 647.02 | 632.77 | 0.1084 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.55 |  | 285.6595 | -0.0383 | 286.39 | 280.275 | 2.8261 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 166.725 |  | 166.8045 | -0.0476 | 166.63 | 162.08 | 1.4875 | below_vwap | below_vwap,spread_too_wide |
