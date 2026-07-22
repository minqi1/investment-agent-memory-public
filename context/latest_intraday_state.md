# Intraday State

- Generated at: `2026-07-23T01:41:41+08:00`
- Market time ET: `2026-07-22T13:41:42-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 7, 'watch_only': 1, 'price_stale_or_missing': 2, 'below_vwap': 11, 'spread_too_wide_or_missing': 21}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.71 |  | 707.4912 | 0.1723 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.8 |  | 553.0801 | 1.215 | 551.02 | 540.105 | 0.0393 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.38 |  | 585.6484 | 0.9787 | 581.9 | 572.01 | 0.0473 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.19 |  | 748.5259 | 0.0887 | 747.68 | 746.425 | 0.008 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.22 |  | 211.2653 | 1.3986 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.71 |  | 420.766 | 0.462 | 419.42 | 414.87 | 0.0757 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 556.54 |  | 551.5427 | 0.9061 | 548.755 | 526.6 | 0.0719 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.8 |  | 553.0801 | 1.215 | 551.02 | 540.105 | 0.0393 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.38 |  | 585.6484 | 0.9787 | 581.9 | 572.01 | 0.0473 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 213.66 |  | 211.2691 | 1.1317 | 207.06 | 202.18 | 0.1123 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 708.71 |  | 707.4912 | 0.1723 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 749.19 |  | 748.5259 | 0.0887 | 747.68 | 746.425 | 0.008 | buy_precheck_manual_confirm | none |
| 9 | AVGO | custom_silicon_networking | 396.9 |  | 390.2672 | 1.6996 | 387.635 | 380.205 | 0.0806 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1808.61 |  | 1798.2162 | 0.578 | 1786.525 | 1767.54 | 0.0581 | buy_precheck_manual_confirm | none |
| 11 | AMAT | semiconductor_equipment | 559.74 |  | 558.4964 | 0.2227 | 559.22 | 544.305 | 0.1929 | buy_precheck_manual_confirm | none |
| 12 | LRCX | semiconductor_equipment | 321.02 |  | 319.0619 | 0.6137 | 317.72 | 311.31 | 0.0716 | buy_precheck_manual_confirm | none |
| 13 | SMCI | ai_server_oem | 31.275 |  | 31.1808 | 0.302 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 71.3 |  | 70.8574 | 0.6247 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.19 |  | 748.5259 | 0.0887 | 747.68 | 746.425 | 0.008 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.71 |  | 707.4912 | 0.1723 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 559.74 |  | 558.4964 | 0.2227 | 559.22 | 544.305 | 0.1929 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 422.71 |  | 420.766 | 0.462 | 419.42 | 414.87 | 0.0757 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 31.275 |  | 31.1808 | 0.302 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1808.61 |  | 1798.2162 | 0.578 | 1786.525 | 1767.54 | 0.0581 | buy_precheck_manual_confirm | none |
| 7 | LRCX | semiconductor_equipment | 321.02 |  | 319.0619 | 0.6137 | 317.72 | 311.31 | 0.0716 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 348.14 |  | 347.9664 | 0.0499 | 348.76 | 346.23 | 0.2413 | watch_only | none |
| 9 | AMD | ai_accelerator | 556.54 |  | 551.5427 | 0.9061 | 548.755 | 526.6 | 0.0719 | buy_precheck_manual_confirm | none |
| 10 | NVDA | ai_accelerator | 214.22 |  | 211.2653 | 1.3986 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| 11 | ANET | ai_networking_optical | 175.235 |  | 174.8772 | 0.2046 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 143.04 |  | 142.9065 | 0.0934 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ONTO | semiconductor_test_packaging | 295.845 |  | 295.3619 | 0.1636 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | APD | industrial_gases | 297.92 |  | 297.7624 | 0.0529 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SOXX | semiconductor_index | 559.8 |  | 553.0801 | 1.215 | 551.02 | 540.105 | 0.0393 | buy_precheck_manual_confirm | none |
| 16 | SMH | semiconductor_index | 591.38 |  | 585.6484 | 0.9787 | 581.9 | 572.01 | 0.0473 | buy_precheck_manual_confirm | none |
| 17 | MRVL | custom_silicon_networking | 213.66 |  | 211.2691 | 1.1317 | 207.06 | 202.18 | 0.1123 | buy_precheck_manual_confirm | none |
| 18 | SKHY | memory_hbm_storage | 167.18 |  | 166.8049 | 0.2249 | 166.63 | 162.08 | 2.4764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 475.75 |  | 473.6955 | 0.4337 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ARM | ai_accelerator | 286.02 |  | 285.6613 | 0.1256 | 286.39 | 280.275 | 2.6117 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.22 |  | 211.2653 | 1.3986 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.71 |  | 420.766 | 0.462 | 419.42 | 414.87 | 0.0757 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 556.54 |  | 551.5427 | 0.9061 | 548.755 | 526.6 | 0.0719 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.8 |  | 553.0801 | 1.215 | 551.02 | 540.105 | 0.0393 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.38 |  | 585.6484 | 0.9787 | 581.9 | 572.01 | 0.0473 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 213.66 |  | 211.2691 | 1.1317 | 207.06 | 202.18 | 0.1123 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 708.71 |  | 707.4912 | 0.1723 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 396.9 |  | 390.2672 | 1.6996 | 387.635 | 380.205 | 0.0806 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 749.19 |  | 748.5259 | 0.0887 | 747.68 | 746.425 | 0.008 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1808.61 |  | 1798.2162 | 0.578 | 1786.525 | 1767.54 | 0.0581 | buy_precheck_manual_confirm | none |
| 11 | AMAT | semiconductor_equipment | 559.74 |  | 558.4964 | 0.2227 | 559.22 | 544.305 | 0.1929 | buy_precheck_manual_confirm | none |
| 12 | LRCX | semiconductor_equipment | 321.02 |  | 319.0619 | 0.6137 | 317.72 | 311.31 | 0.0716 | buy_precheck_manual_confirm | none |
| 13 | SMCI | ai_server_oem | 31.275 |  | 31.1808 | 0.302 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 71.3 |  | 70.8574 | 0.6247 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 15 | HPE | ai_server_oem | 49.01 |  | 49.0272 | -0.0351 | 48.96 | 47.01 | 0.0204 | below_vwap | below_vwap |
| 16 | CRWV | gpu_cloud_ai_factory | 83.52 |  | 83.5235 | -0.0042 | 83.22 | 79.6 | 4.7773 | below_vwap | below_vwap,spread_too_wide |
| 17 | MU | memory_hbm_storage | 977.02 |  | 968.0419 | 0.9274 | 963.41 | 936.99 | 1.2282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TT | data_center_power_cooling | 475.75 |  | 473.6955 | 0.4337 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1620.55 |  | 1579.3404 | 2.6093 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 559.76 |  | 555.9719 | 0.6813 | 548.14 | 526.22 | 1.2148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.71 |  | 707.4912 | 0.1723 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.3 |  | 70.8574 | 0.6247 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 214.22 |  | 211.2653 | 1.3986 | 207.4 | 205.01 | 0.0093 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.09 |  | 390.238 | -0.5504 | 400.89 | 392.26 | 0.0232 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.67 |  | 325.0993 | -0.4397 | 328.865 | 325.74 | 0.0124 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.14 |  | 347.9664 | 0.0499 | 348.76 | 346.23 | 0.2413 | watch_only | none |
| AMD | ai_accelerator | 556.54 |  | 551.5427 | 0.9061 | 548.755 | 526.6 | 0.0719 | buy_precheck_manual_confirm | none |
| TSM | foundry | 422.71 |  | 420.766 | 0.462 | 419.42 | 414.87 | 0.0757 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.8 |  | 553.0801 | 1.215 | 551.02 | 540.105 | 0.0393 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.38 |  | 585.6484 | 0.9787 | 581.9 | 572.01 | 0.0473 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.9 |  | 390.2672 | 1.6996 | 387.635 | 380.205 | 0.0806 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 977.02 |  | 968.0419 | 0.9274 | 963.41 | 936.99 | 1.2282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.66 |  | 211.2691 | 1.1317 | 207.06 | 202.18 | 0.1123 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 443.75 |  | 442.7306 | 0.2303 | 435.98 | 415.79 | 2.0868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 49.01 |  | 49.0272 | -0.0351 | 48.96 | 47.01 | 0.0204 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.275 |  | 31.1808 | 0.302 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.19 |  | 748.5259 | 0.0887 | 747.68 | 746.425 | 0.008 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.515 |  | 295.1177 | -0.2042 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.465 |  | 126.6654 | -0.1582 | 128.79 | 125.83 | 0.0474 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.52 |  | 83.5235 | -0.0042 | 83.22 | 79.6 | 4.7773 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 300.905 |  | 299.0635 | 0.6157 | 297.69 | 293.905 | 1.3459 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.48 |  | 407.9353 | -0.1116 | 409.095 | 398.16 | 0.1914 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 643.55 |  | 640.7476 | 0.4374 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 990.31 |  | 1007.1008 | -1.6672 | 1036.605 | 998.94 | 3.5847 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.75 |  | 473.6955 | 0.4337 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.04 |  | 142.9065 | 0.0934 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.235 |  | 174.8772 | 0.2046 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 314.65 |  | 316.1472 | -0.4736 | 317.93 | 306.89 | 4.4176 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 829.69 |  | 840.1662 | -1.2469 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.535 |  | 405.7144 | -0.7837 | 407.12 | 397.835 | 1.0956 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.5 |  | 114.4102 | -2.5436 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.64 |  | 329.5116 | 1.2529 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1808.61 |  | 1798.2162 | 0.578 | 1786.525 | 1767.54 | 0.0581 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.74 |  | 558.4964 | 0.2227 | 559.22 | 544.305 | 0.1929 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.02 |  | 319.0619 | 0.6137 | 317.72 | 311.31 | 0.0716 | buy_precheck_manual_confirm | none |
| KLAC | semiconductor_equipment | 216.675 |  | 216.1006 | 0.2658 | 215.465 | 210.975 | 4.1583 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373 |  | 371.5885 | 0.3799 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.845 |  | 295.3619 | 0.1636 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.56 |  | 67.4779 | 0.1217 | 66.73 | 64.98 | 4.1297 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.37 |  | 138.8035 | 0.4081 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 348.86 |  | 344.2471 | 1.34 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.69 |  | 507.2558 | 0.4799 | 507.545 | 505.59 | 4.4733 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.92 |  | 297.7624 | 0.0529 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.37 |  | 30.7612 | -1.2716 | 30.78 | 29.46 | 0.0988 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.1 |  | 42.6376 | -1.2608 | 42.29 | 40.305 | 0.0475 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.87 |  | 24.1127 | -1.0064 | 24.255 | 23.58 | 0.0419 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1620.55 |  | 1579.3404 | 2.6093 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.76 |  | 555.9719 | 0.6813 | 548.14 | 526.22 | 1.2148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 915 |  | 909.0272 | 0.6571 | 899.59 | 860.605 | 0.7781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.195 |  | 244.4062 | -0.4956 | 248.43 | 244.47 | 0.0123 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 627.63 |  | 630.9982 | -0.5338 | 647.02 | 632.77 | 1.1472 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 286.02 |  | 285.6613 | 0.1256 | 286.39 | 280.275 | 2.6117 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 167.18 |  | 166.8049 | 0.2249 | 166.63 | 162.08 | 2.4764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
