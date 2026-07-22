# Intraday State

- Generated at: `2026-07-23T01:57:55+08:00`
- Market time ET: `2026-07-22T13:57:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'below_opening_15m_low': 8, 'below_vwap': 17, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.52 |  | 707.5064 | 0.0019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.77 |  | 553.2046 | 1.006 | 551.02 | 540.105 | 0.0394 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.26 |  | 585.7156 | 0.7759 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.57 |  | 748.5379 | 0.0043 | 747.68 | 746.425 | 0.0013 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.645 |  | 211.3526 | 1.0846 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.77 |  | 553.2046 | 1.006 | 551.02 | 540.105 | 0.0394 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.26 |  | 585.7156 | 0.7759 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 707.52 |  | 707.5064 | 0.0019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.57 |  | 748.5379 | 0.0043 | 747.68 | 746.425 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | AMAT | semiconductor_equipment | 559.71 |  | 558.5401 | 0.2095 | 559.22 | 544.305 | 0.2841 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.29 |  | 299.1728 | 0.7077 | 297.69 | 293.905 | 0.0697 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 70.91 |  | 70.8644 | 0.0643 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.52 |  | 707.5064 | 0.0019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.57 |  | 748.5379 | 0.0043 | 747.68 | 746.425 | 0.0013 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 559.71 |  | 558.5401 | 0.2095 | 559.22 | 544.305 | 0.2841 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 143.19 |  | 142.9126 | 0.1941 | 143.27 | 141.04 | 0.0489 | watch_only | none |
| 5 | SMH | semiconductor_index | 590.26 |  | 585.7156 | 0.7759 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| 6 | VRT | data_center_power_cooling | 301.29 |  | 299.1728 | 0.7077 | 297.69 | 293.905 | 0.0697 | buy_precheck_manual_confirm | none |
| 7 | SOXX | semiconductor_index | 558.77 |  | 553.2046 | 1.006 | 551.02 | 540.105 | 0.0394 | buy_precheck_manual_confirm | none |
| 8 | TER | semiconductor_test_packaging | 372.37 |  | 371.6288 | 0.1994 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.645 |  | 211.3526 | 1.0846 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 10 | ENTG | semiconductor_materials | 139.14 |  | 138.8565 | 0.2041 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 295.44 |  | 295.3645 | 0.0256 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | APD | industrial_gases | 298.22 |  | 297.8059 | 0.1391 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 421.62 |  | 420.8039 | 0.1939 | 419.42 | 414.87 | 1.0673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TT | data_center_power_cooling | 475.87 |  | 473.7254 | 0.4527 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 216.24 |  | 216.1113 | 0.0596 | 215.465 | 210.975 | 4.273 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LIN | industrial_gases | 509.98 |  | 507.2866 | 0.5309 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 643.48 |  | 640.8703 | 0.4072 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 911.47 |  | 909.2125 | 0.2483 | 899.59 | 860.605 | 0.3807 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | LRCX | semiconductor_equipment | 320.84 |  | 319.1158 | 0.5403 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ANET | ai_networking_optical | 175.535 |  | 174.8883 | 0.3698 | 175.265 | 171.06 | 2.7573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.645 |  | 211.3526 | 1.0846 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.77 |  | 553.2046 | 1.006 | 551.02 | 540.105 | 0.0394 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.26 |  | 585.7156 | 0.7759 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 707.52 |  | 707.5064 | 0.0019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 748.57 |  | 748.5379 | 0.0043 | 747.68 | 746.425 | 0.0013 | buy_precheck_manual_confirm | none |
| 6 | AMAT | semiconductor_equipment | 559.71 |  | 558.5401 | 0.2095 | 559.22 | 544.305 | 0.2841 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.29 |  | 299.1728 | 0.7077 | 297.69 | 293.905 | 0.0697 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 70.91 |  | 70.8644 | 0.0643 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 9 | DELL | ai_server_oem | 440.85 |  | 442.6952 | -0.4168 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | AMKR | semiconductor_test_packaging | 67.34 |  | 67.4788 | -0.2056 | 66.73 | 64.98 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | SMCI | ai_server_oem | 31.015 |  | 31.1779 | -0.5223 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 973.235 |  | 968.2643 | 0.5134 | 963.41 | 936.99 | 1.0111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 421.62 |  | 420.8039 | 0.1939 | 419.42 | 414.87 | 1.0673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 555 |  | 551.6776 | 0.6022 | 548.755 | 526.6 | 2.7874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.87 |  | 473.7254 | 0.4527 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1602.9 |  | 1579.9989 | 1.4494 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 556.535 |  | 556.0641 | 0.0847 | 548.14 | 526.22 | 0.8122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 911.47 |  | 909.2125 | 0.2483 | 899.59 | 860.605 | 0.3807 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 212.95 |  | 211.3358 | 0.7638 | 207.06 | 202.18 | 0.8922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 372.37 |  | 371.6288 | 0.1994 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.52 |  | 707.5064 | 0.0019 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 70.91 |  | 70.8644 | 0.0643 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.645 |  | 211.3526 | 1.0846 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.345 |  | 390.1478 | -0.7184 | 400.89 | 392.26 | 0.0181 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.88 |  | 325.0678 | -0.3654 | 328.865 | 325.74 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.125 |  | 347.948 | -0.2365 | 348.76 | 346.23 | 0.0086 | below_vwap | below_vwap |
| AMD | ai_accelerator | 555 |  | 551.6776 | 0.6022 | 548.755 | 526.6 | 2.7874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.62 |  | 420.8039 | 0.1939 | 419.42 | 414.87 | 1.0673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.77 |  | 553.2046 | 1.006 | 551.02 | 540.105 | 0.0394 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.26 |  | 585.7156 | 0.7759 | 581.9 | 572.01 | 0.0576 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.8 |  | 391.1546 | 1.4433 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 973.235 |  | 968.2643 | 0.5134 | 963.41 | 936.99 | 1.0111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.95 |  | 211.3358 | 0.7638 | 207.06 | 202.18 | 0.8922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 440.85 |  | 442.6952 | -0.4168 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.82 |  | 49.0238 | -0.4157 | 48.96 | 47.01 | 0.041 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.015 |  | 31.1779 | -0.5223 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 748.57 |  | 748.5379 | 0.0043 | 747.68 | 746.425 | 0.0013 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.435 |  | 295.0982 | -0.2248 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.6 |  | 126.6326 | -0.8154 | 128.79 | 125.83 | 0.0637 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.82 |  | 83.5129 | -0.8296 | 83.22 | 79.6 | 0.1087 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 301.29 |  | 299.1728 | 0.7077 | 297.69 | 293.905 | 0.0697 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.5 |  | 407.9187 | -0.1026 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.48 |  | 640.8703 | 0.4072 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 990.38 |  | 1006.4262 | -1.5944 | 1036.605 | 998.94 | 0.2767 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 475.87 |  | 473.7254 | 0.4527 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.19 |  | 142.9126 | 0.1941 | 143.27 | 141.04 | 0.0489 | watch_only | none |
| ANET | ai_networking_optical | 175.535 |  | 174.8883 | 0.3698 | 175.265 | 171.06 | 2.7573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.36 |  | 316.1225 | -0.5575 | 317.93 | 306.89 | 2.8439 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 825.8 |  | 839.5828 | -1.6416 | 840.47 | 814.62 | 3.875 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 401.81 |  | 405.5948 | -0.9332 | 407.12 | 397.835 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 110.95 |  | 114.3258 | -2.9528 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.29 |  | 329.5973 | 0.817 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1806.115 |  | 1798.5836 | 0.4187 | 1786.525 | 1767.54 | 1.645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 559.71 |  | 558.5401 | 0.2095 | 559.22 | 544.305 | 0.2841 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.84 |  | 319.1158 | 0.5403 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.24 |  | 216.1113 | 0.0596 | 215.465 | 210.975 | 4.273 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.37 |  | 371.6288 | 0.1994 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.44 |  | 295.3645 | 0.0256 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.34 |  | 67.4788 | -0.2056 | 66.73 | 64.98 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.545 |  | 55.691 | -0.2621 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 139.14 |  | 138.8565 | 0.2041 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 347.5 |  | 344.3997 | 0.9002 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.98 |  | 507.2866 | 0.5309 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.22 |  | 297.8059 | 0.1391 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.22 |  | 30.7503 | -1.7245 | 30.78 | 29.46 | 0.0993 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.63 |  | 42.6074 | -2.2939 | 42.29 | 40.305 | 0.048 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.71 |  | 24.0981 | -1.6104 | 24.255 | 23.58 | 0.0844 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1602.9 |  | 1579.9989 | 1.4494 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 556.535 |  | 556.0641 | 0.0847 | 548.14 | 526.22 | 0.8122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 911.47 |  | 909.2125 | 0.2483 | 899.59 | 860.605 | 0.3807 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 242.625 |  | 244.3599 | -0.71 | 248.43 | 244.47 | 0.0124 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 625.455 |  | 630.8969 | -0.8626 | 647.02 | 632.77 | 0.0767 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.26 |  | 285.6558 | -0.1386 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.555 |  | 166.8025 | -0.1484 | 166.63 | 162.08 | 2.2815 | below_vwap | below_vwap,spread_too_wide |
