# Intraday State

- Generated at: `2026-07-23T01:10:02+08:00`
- Market time ET: `2026-07-22T13:10:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 7, 'below_vwap': 10, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.2 |  | 707.3181 | 0.2661 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 560.66 |  | 552.78 | 1.4255 | 551.02 | 540.105 | 0.066 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.91 |  | 585.0528 | 1.1721 | 581.9 | 572.01 | 0.0574 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.63 |  | 748.4656 | 0.1556 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.055 |  | 210.9895 | 1.4529 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 976.11 |  | 967.1402 | 0.9275 | 963.41 | 936.99 | 0.0625 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 422.83 |  | 420.64 | 0.5206 | 419.42 | 414.87 | 0.2247 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 560.66 |  | 552.78 | 1.4255 | 551.02 | 540.105 | 0.066 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.91 |  | 585.0528 | 1.1721 | 581.9 | 572.01 | 0.0574 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.2 |  | 707.3181 | 0.2661 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.63 |  | 748.4656 | 0.1556 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1810.235 |  | 1796.7743 | 0.7492 | 1786.525 | 1767.54 | 0.0613 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 301.37 |  | 298.8576 | 0.8407 | 297.69 | 293.905 | 0.1161 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 644.105 |  | 640.358 | 0.5851 | 641.19 | 628.17 | 0.1335 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.515 |  | 31.1747 | 1.0917 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 84.045 |  | 83.5188 | 0.63 | 83.22 | 79.6 | 0.0952 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.46 |  | 70.8334 | 0.8845 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.63 |  | 748.4656 | 0.1556 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.2 |  | 707.3181 | 0.2661 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 3 | PWR | data_center_power_cooling | 644.105 |  | 640.358 | 0.5851 | 641.19 | 628.17 | 0.1335 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1810.235 |  | 1796.7743 | 0.7492 | 1786.525 | 1767.54 | 0.0613 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 422.83 |  | 420.64 | 0.5206 | 419.42 | 414.87 | 0.2247 | buy_precheck_manual_confirm | none |
| 6 | CRWV | gpu_cloud_ai_factory | 84.045 |  | 83.5188 | 0.63 | 83.22 | 79.6 | 0.0952 | buy_precheck_manual_confirm | none |
| 7 | MU | memory_hbm_storage | 976.11 |  | 967.1402 | 0.9275 | 963.41 | 936.99 | 0.0625 | buy_precheck_manual_confirm | none |
| 8 | ETN | data_center_power_cooling | 409.13 |  | 407.8756 | 0.3075 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | VRT | data_center_power_cooling | 301.37 |  | 298.8576 | 0.8407 | 297.69 | 293.905 | 0.1161 | buy_precheck_manual_confirm | none |
| 10 | NVDA | ai_accelerator | 214.055 |  | 210.9895 | 1.4529 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | ONTO | semiconductor_test_packaging | 295.5 |  | 295.3356 | 0.0557 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SOXX | semiconductor_index | 560.66 |  | 552.78 | 1.4255 | 551.02 | 540.105 | 0.066 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 591.91 |  | 585.0528 | 1.1721 | 581.9 | 572.01 | 0.0574 | buy_precheck_manual_confirm | none |
| 14 | TT | data_center_power_cooling | 475.39 |  | 473.1129 | 0.4813 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SMCI | ai_server_oem | 31.515 |  | 31.1747 | 1.0917 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 16 | AMAT | semiconductor_equipment | 560.33 |  | 558.3923 | 0.347 | 559.22 | 544.305 | 1.5223 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ANET | ai_networking_optical | 175.33 |  | 174.8334 | 0.2841 | 175.265 | 171.06 | 2.9886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LIN | industrial_gases | 509.36 |  | 507.2072 | 0.4244 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 143.165 |  | 142.8915 | 0.1914 | 143.27 | 141.04 | 4.8476 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ORCL | cloud_ai_capex | 126.74 |  | 126.6883 | 0.0408 | 128.79 | 125.83 | 1.6806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 214.055 |  | 210.9895 | 1.4529 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 976.11 |  | 967.1402 | 0.9275 | 963.41 | 936.99 | 0.0625 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 422.83 |  | 420.64 | 0.5206 | 419.42 | 414.87 | 0.2247 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 560.66 |  | 552.78 | 1.4255 | 551.02 | 540.105 | 0.066 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 591.91 |  | 585.0528 | 1.1721 | 581.9 | 572.01 | 0.0574 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 709.2 |  | 707.3181 | 0.2661 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.63 |  | 748.4656 | 0.1556 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1810.235 |  | 1796.7743 | 0.7492 | 1786.525 | 1767.54 | 0.0613 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 301.37 |  | 298.8576 | 0.8407 | 297.69 | 293.905 | 0.1161 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 644.105 |  | 640.358 | 0.5851 | 641.19 | 628.17 | 0.1335 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.515 |  | 31.1747 | 1.0917 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 84.045 |  | 83.5188 | 0.63 | 83.22 | 79.6 | 0.0952 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.46 |  | 70.8334 | 0.8845 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 14 | AMD | ai_accelerator | 557.39 |  | 551.3174 | 1.1015 | 548.755 | 526.6 | 2.7754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.39 |  | 473.1129 | 0.4813 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1611.36 |  | 1576.568 | 2.2068 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 561.605 |  | 555.5422 | 1.0913 | 548.14 | 526.22 | 4.5156 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 915.79 |  | 908.4404 | 0.809 | 899.59 | 860.605 | 0.3833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 214.22 |  | 211.0973 | 1.4793 | 207.06 | 202.18 | 2.6328 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 373.545 |  | 371.5048 | 0.5492 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.2 |  | 707.3181 | 0.2661 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.46 |  | 70.8334 | 0.8845 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 214.055 |  | 210.9895 | 1.4529 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.875 |  | 390.4433 | -0.4017 | 400.89 | 392.26 | 0.1929 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.92 |  | 325.2251 | -0.4013 | 328.865 | 325.74 | 0.0463 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.9 |  | 347.9444 | -0.0128 | 348.76 | 346.23 | 0.0661 | below_vwap | below_vwap |
| AMD | ai_accelerator | 557.39 |  | 551.3174 | 1.1015 | 548.755 | 526.6 | 2.7754 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.83 |  | 420.64 | 0.5206 | 419.42 | 414.87 | 0.2247 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 560.66 |  | 552.78 | 1.4255 | 551.02 | 540.105 | 0.066 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.91 |  | 585.0528 | 1.1721 | 581.9 | 572.01 | 0.0574 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.8 |  | 389.8852 | 1.7736 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 976.11 |  | 967.1402 | 0.9275 | 963.41 | 936.99 | 0.0625 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 214.22 |  | 211.0973 | 1.4793 | 207.06 | 202.18 | 2.6328 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.3 |  | 442.7187 | 0.1313 | 435.98 | 415.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 48.84 |  | 49.0344 | -0.3965 | 48.96 | 47.01 | 0.041 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.515 |  | 31.1747 | 1.0917 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.63 |  | 748.4656 | 0.1556 | 747.68 | 746.425 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.53 |  | 295.1575 | -0.2126 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.74 |  | 126.6883 | 0.0408 | 128.79 | 125.83 | 1.6806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 84.045 |  | 83.5188 | 0.63 | 83.22 | 79.6 | 0.0952 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 301.37 |  | 298.8576 | 0.8407 | 297.69 | 293.905 | 0.1161 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 409.13 |  | 407.8756 | 0.3075 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 644.105 |  | 640.358 | 0.5851 | 641.19 | 628.17 | 0.1335 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 998.735 |  | 1008.2483 | -0.9435 | 1036.605 | 998.94 | 0.7189 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.39 |  | 473.1129 | 0.4813 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.165 |  | 142.8915 | 0.1914 | 143.27 | 141.04 | 4.8476 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.33 |  | 174.8334 | 0.2841 | 175.265 | 171.06 | 2.9886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.89 |  | 316.1767 | -0.0907 | 317.93 | 306.89 | 2.4945 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 835.32 |  | 840.7858 | -0.6501 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 404.05 |  | 405.9568 | -0.4697 | 407.12 | 397.835 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 113 |  | 114.6805 | -1.4654 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 335.62 |  | 329.1105 | 1.9779 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1810.235 |  | 1796.7743 | 0.7492 | 1786.525 | 1767.54 | 0.0613 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.33 |  | 558.3923 | 0.347 | 559.22 | 544.305 | 1.5223 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.46 |  | 318.907 | 0.8005 | 317.72 | 311.31 | 4.0814 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.92 |  | 216.0644 | 0.396 | 215.465 | 210.975 | 4.0937 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373.545 |  | 371.5048 | 0.5492 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.5 |  | 295.3356 | 0.0557 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.69 |  | 67.4742 | 0.3198 | 66.73 | 64.98 | 1.9648 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.89 |  | 55.6869 | 0.3647 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.295 |  | 138.7403 | 0.3998 | 140.09 | 135.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346.61 |  | 343.6564 | 0.8595 | 345.675 | 331.945 | 0.7097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 509.36 |  | 507.2072 | 0.4244 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.62 |  | 297.7595 | -0.0468 | 300.24 | 297.585 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.41 |  | 30.7864 | -1.2227 | 30.78 | 29.46 | 0.0329 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.08 |  | 42.6979 | -1.4472 | 42.29 | 40.305 | 0.0475 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.91 |  | 24.1317 | -0.9188 | 24.255 | 23.58 | 0.0836 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1611.36 |  | 1576.568 | 2.2068 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 561.605 |  | 555.5422 | 1.0913 | 548.14 | 526.22 | 4.5156 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 915.79 |  | 908.4404 | 0.809 | 899.59 | 860.605 | 0.3833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.52 |  | 244.5056 | -0.4031 | 248.43 | 244.47 | 0.0205 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 630.19 |  | 631.2924 | -0.1746 | 647.02 | 632.77 | 0.6395 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 286.85 |  | 285.6323 | 0.4263 | 286.39 | 280.275 | 2.388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.45 |  | 166.7045 | 1.0471 | 166.63 | 162.08 | 1.0151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
