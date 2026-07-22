# Intraday State

- Generated at: `2026-07-23T00:50:04+08:00`
- Market time ET: `2026-07-22T12:50:05-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_opening_15m_low': 7, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 3, 'below_vwap': 13}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.32 |  | 707.2033 | 0.1579 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 557.09 |  | 552.5483 | 0.822 | 551.02 | 540.105 | 0.0772 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.355 |  | 584.8356 | 0.7728 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.57 |  | 748.4125 | 0.1547 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.39 |  | 210.8204 | 1.2189 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 972.055 |  | 966.731 | 0.5507 | 963.41 | 936.99 | 0.2212 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 422.13 |  | 420.5627 | 0.3727 | 419.42 | 414.87 | 0.3056 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.09 |  | 552.5483 | 0.822 | 551.02 | 540.105 | 0.0772 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.355 |  | 584.8356 | 0.7728 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.32 |  | 707.2033 | 0.1579 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.57 |  | 748.4125 | 0.1547 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1800.28 |  | 1796.1242 | 0.2314 | 1786.525 | 1767.54 | 0.0933 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.51 |  | 31.1649 | 1.1072 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.18 |  | 70.8195 | 0.509 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 708.32 |  | 707.2033 | 0.1579 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 749.57 |  | 748.4125 | 0.1547 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1800.28 |  | 1796.1242 | 0.2314 | 1786.525 | 1767.54 | 0.0933 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 422.13 |  | 420.5627 | 0.3727 | 419.42 | 414.87 | 0.3056 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.355 |  | 584.8356 | 0.7728 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 6 | MU | memory_hbm_storage | 972.055 |  | 966.731 | 0.5507 | 963.41 | 936.99 | 0.2212 | buy_precheck_manual_confirm | none |
| 7 | SOXX | semiconductor_index | 557.09 |  | 552.5483 | 0.822 | 551.02 | 540.105 | 0.0772 | buy_precheck_manual_confirm | none |
| 8 | TER | semiconductor_test_packaging | 371.815 |  | 371.4252 | 0.1049 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.39 |  | 210.8204 | 1.2189 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 10 | ARM | ai_accelerator | 285.68 |  | 285.6165 | 0.0222 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ANET | ai_networking_optical | 175.08 |  | 174.8144 | 0.1519 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 408.95 |  | 407.7723 | 0.2888 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 297.83 |  | 297.7593 | 0.0237 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMCI | ai_server_oem | 31.51 |  | 31.1649 | 1.1072 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 15 | PWR | data_center_power_cooling | 643.32 |  | 640.1909 | 0.4888 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TT | data_center_power_cooling | 475.62 |  | 472.985 | 0.5571 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 348.455 |  | 347.9404 | 0.1479 | 348.76 | 346.23 | 0.5051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LRCX | semiconductor_equipment | 319.02 |  | 318.7721 | 0.0778 | 317.72 | 311.31 | 4.7771 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | JCI | data_center_power_cooling | 143.17 |  | 142.8778 | 0.2045 | 143.27 | 141.04 | 4.9033 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CRWV | gpu_cloud_ai_factory | 83.64 |  | 83.5124 | 0.1528 | 83.22 | 79.6 | 1.8173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.39 |  | 210.8204 | 1.2189 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 972.055 |  | 966.731 | 0.5507 | 963.41 | 936.99 | 0.2212 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 422.13 |  | 420.5627 | 0.3727 | 419.42 | 414.87 | 0.3056 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.09 |  | 552.5483 | 0.822 | 551.02 | 540.105 | 0.0772 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.355 |  | 584.8356 | 0.7728 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.32 |  | 707.2033 | 0.1579 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.57 |  | 748.4125 | 0.1547 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1800.28 |  | 1796.1242 | 0.2314 | 1786.525 | 1767.54 | 0.0933 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.51 |  | 31.1649 | 1.1072 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 71.18 |  | 70.8195 | 0.509 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 11 | KLAC | semiconductor_equipment | 215.565 |  | 216.0702 | -0.2338 | 215.465 | 210.975 | 4.7039 | below_vwap | below_vwap,spread_too_wide |
| 12 | AMD | ai_accelerator | 554.69 |  | 551.0159 | 0.6668 | 548.755 | 526.6 | 1.9326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TT | data_center_power_cooling | 475.62 |  | 472.985 | 0.5571 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SNDK | memory_hbm_storage | 1601.155 |  | 1574.6239 | 1.6849 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 559.71 |  | 555.3447 | 0.7861 | 548.14 | 526.22 | 4.9901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 913.94 |  | 907.9865 | 0.6557 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MRVL | custom_silicon_networking | 212.61 |  | 210.9971 | 0.7644 | 207.06 | 202.18 | 0.7337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 371.815 |  | 371.4252 | 0.1049 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 395.24 |  | 389.4086 | 1.4975 | 387.635 | 380.205 | 4.5238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SKHY | memory_hbm_storage | 167.395 |  | 166.6917 | 0.4219 | 166.63 | 162.08 | 0.8363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.32 |  | 707.2033 | 0.1579 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.18 |  | 70.8195 | 0.509 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.39 |  | 210.8204 | 1.2189 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.625 |  | 390.5106 | -0.4829 | 400.89 | 392.26 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.395 |  | 325.3387 | -0.2901 | 328.865 | 325.74 | 0.0647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.455 |  | 347.9404 | 0.1479 | 348.76 | 346.23 | 0.5051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 554.69 |  | 551.0159 | 0.6668 | 548.755 | 526.6 | 1.9326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.13 |  | 420.5627 | 0.3727 | 419.42 | 414.87 | 0.3056 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.09 |  | 552.5483 | 0.822 | 551.02 | 540.105 | 0.0772 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.355 |  | 584.8356 | 0.7728 | 581.9 | 572.01 | 0.0526 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 395.24 |  | 389.4086 | 1.4975 | 387.635 | 380.205 | 4.5238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 972.055 |  | 966.731 | 0.5507 | 963.41 | 936.99 | 0.2212 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 212.61 |  | 210.9971 | 0.7644 | 207.06 | 202.18 | 0.7337 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.525 |  | 442.6917 | 0.1882 | 435.98 | 415.79 | 2.6898 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.78 |  | 49.0405 | -0.5313 | 48.96 | 47.01 | 0.082 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.51 |  | 31.1649 | 1.1072 | 30.66 | 28.52 | 0.0317 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.57 |  | 748.4125 | 0.1547 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.485 |  | 295.2225 | -0.2498 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.06 |  | 126.6972 | -0.5029 | 128.79 | 125.83 | 2.0149 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.64 |  | 83.5124 | 0.1528 | 83.22 | 79.6 | 1.8173 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.97 |  | 298.766 | 0.403 | 297.69 | 293.905 | 2.6669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.95 |  | 407.7723 | 0.2888 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.32 |  | 640.1909 | 0.4888 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 994.9 |  | 1008.6785 | -1.366 | 1036.605 | 998.94 | 2.3369 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.62 |  | 472.985 | 0.5571 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.17 |  | 142.8778 | 0.2045 | 143.27 | 141.04 | 4.9033 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 175.08 |  | 174.8144 | 0.1519 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 314.5 |  | 316.249 | -0.553 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 834.64 |  | 841.1243 | -0.7709 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 403.17 |  | 406.0955 | -0.7204 | 407.12 | 397.835 | 2.3067 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.16 |  | 114.7454 | -2.2532 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.76 |  | 328.6414 | 1.2532 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1800.28 |  | 1796.1242 | 0.2314 | 1786.525 | 1767.54 | 0.0933 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 557.91 |  | 558.3657 | -0.0816 | 559.22 | 544.305 | 1.9448 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.02 |  | 318.7721 | 0.0778 | 317.72 | 311.31 | 4.7771 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 215.565 |  | 216.0702 | -0.2338 | 215.465 | 210.975 | 4.7039 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.815 |  | 371.4252 | 0.1049 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.28 |  | 295.2958 | -0.0053 | 298.42 | 288.335 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.56 |  | 67.4612 | 0.1464 | 66.73 | 64.98 | 4.1741 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.12 |  | 138.7195 | -0.4322 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.37 |  | 343.5443 | 0.5314 | 345.675 | 331.945 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 509.52 |  | 507.1298 | 0.4713 | 507.545 | 505.59 | 4.4905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.83 |  | 297.7593 | 0.0237 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.39 |  | 30.819 | -1.3921 | 30.78 | 29.46 | 0.1316 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.065 |  | 42.7252 | -1.5451 | 42.29 | 40.305 | 0.0238 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.765 |  | 24.1405 | -1.5553 | 24.255 | 23.58 | 0.0842 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1601.155 |  | 1574.6239 | 1.6849 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.71 |  | 555.3447 | 0.7861 | 548.14 | 526.22 | 4.9901 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 913.94 |  | 907.9865 | 0.6557 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 244.13 |  | 244.5313 | -0.1641 | 248.43 | 244.47 | 0.0205 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 629.455 |  | 631.3698 | -0.3033 | 647.02 | 632.77 | 0.2733 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.68 |  | 285.6165 | 0.0222 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 167.395 |  | 166.6917 | 0.4219 | 166.63 | 162.08 | 0.8363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
