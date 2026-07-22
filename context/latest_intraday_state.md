# Intraday State

- Generated at: `2026-07-23T00:42:12+08:00`
- Market time ET: `2026-07-22T12:42:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 6, 'watch_only': 1, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 2, 'below_vwap': 14}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.5 |  | 707.1828 | 0.1863 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.3 |  | 552.4851 | 1.0525 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0627 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.785 |  | 748.3785 | 0.1879 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.81 |  | 210.7646 | 1.445 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | WDC | memory_hbm_storage | 559.92 |  | 555.2492 | 0.8412 | 548.14 | 526.22 | 0.3125 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.3 |  | 552.4851 | 1.0525 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0627 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.1 |  | 210.9751 | 1.0072 | 207.06 | 202.18 | 0.1642 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.5 |  | 707.1828 | 0.1863 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.785 |  | 748.3785 | 0.1879 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1800.88 |  | 1796.0661 | 0.268 | 1786.525 | 1767.54 | 0.1033 | buy_precheck_manual_confirm | none |
| 9 | ALAB | ai_networking_optical | 333.06 |  | 328.4732 | 1.3964 | 322.67 | 307.545 | 0.3453 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.68 |  | 31.156 | 1.6818 | 30.66 | 28.52 | 0.0316 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.24 |  | 70.8151 | 0.6 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.785 |  | 748.3785 | 0.1879 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.5 |  | 707.1828 | 0.1863 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1800.88 |  | 1796.0661 | 0.268 | 1786.525 | 1767.54 | 0.1033 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 348.09 |  | 347.9382 | 0.0436 | 348.76 | 346.23 | 0.27 | watch_only | none |
| 5 | SOXX | semiconductor_index | 558.3 |  | 552.4851 | 1.0525 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0627 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 143.295 |  | 142.8712 | 0.2966 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | NVDA | ai_accelerator | 213.81 |  | 210.7646 | 1.445 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 9 | COHR | ai_networking_optical | 317.21 |  | 316.3063 | 0.2857 | 317.93 | 306.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 408.85 |  | 407.7291 | 0.2749 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TT | data_center_power_cooling | 475.2 |  | 472.8991 | 0.4866 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | WDC | memory_hbm_storage | 559.92 |  | 555.2492 | 0.8412 | 548.14 | 526.22 | 0.3125 | buy_precheck_manual_confirm | none |
| 13 | MRVL | custom_silicon_networking | 213.1 |  | 210.9751 | 1.0072 | 207.06 | 202.18 | 0.1642 | buy_precheck_manual_confirm | none |
| 14 | ALAB | ai_networking_optical | 333.06 |  | 328.4732 | 1.3964 | 322.67 | 307.545 | 0.3453 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 175.92 |  | 174.8045 | 0.6382 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | LRCX | semiconductor_equipment | 320.25 |  | 318.7294 | 0.4771 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 644.2 |  | 640.0873 | 0.6425 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 345.37 |  | 343.5443 | 0.5314 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ONTO | semiconductor_test_packaging | 296.29 |  | 295.1654 | 0.381 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | CRWV | gpu_cloud_ai_factory | 83.63 |  | 83.5116 | 0.1418 | 83.22 | 79.6 | 1.7099 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.81 |  | 210.7646 | 1.445 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | WDC | memory_hbm_storage | 559.92 |  | 555.2492 | 0.8412 | 548.14 | 526.22 | 0.3125 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.3 |  | 552.4851 | 1.0525 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0627 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 213.1 |  | 210.9751 | 1.0072 | 207.06 | 202.18 | 0.1642 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 708.5 |  | 707.1828 | 0.1863 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 749.785 |  | 748.3785 | 0.1879 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1800.88 |  | 1796.0661 | 0.268 | 1786.525 | 1767.54 | 0.1033 | buy_precheck_manual_confirm | none |
| 9 | ALAB | ai_networking_optical | 333.06 |  | 328.4732 | 1.3964 | 322.67 | 307.545 | 0.3453 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 31.68 |  | 31.156 | 1.6818 | 30.66 | 28.52 | 0.0316 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.24 |  | 70.8151 | 0.6 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 215.83 |  | 216.0886 | -0.1197 | 215.465 | 210.975 | 2.7012 | below_vwap | below_vwap,spread_too_wide |
| 13 | MU | memory_hbm_storage | 972.805 |  | 966.6162 | 0.6402 | 963.41 | 936.99 | 0.8224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 422.295 |  | 420.5391 | 0.4175 | 419.42 | 414.87 | 0.4073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 554.83 |  | 550.9561 | 0.7031 | 548.755 | 526.6 | 1.9321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TT | data_center_power_cooling | 475.2 |  | 472.8991 | 0.4866 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1606.19 |  | 1574.0901 | 2.0393 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 914.53 |  | 907.5704 | 0.7668 | 899.59 | 860.605 | 0.5194 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 372.775 |  | 371.419 | 0.3651 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 394.605 |  | 389.2189 | 1.3838 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.5 |  | 707.1828 | 0.1863 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.24 |  | 70.8151 | 0.6 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.81 |  | 210.7646 | 1.445 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.62 |  | 390.5451 | -0.4929 | 400.89 | 392.26 | 0.1647 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.36 |  | 325.3704 | -0.3106 | 328.865 | 325.74 | 0.3237 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.09 |  | 347.9382 | 0.0436 | 348.76 | 346.23 | 0.27 | watch_only | none |
| AMD | ai_accelerator | 554.83 |  | 550.9561 | 0.7031 | 548.755 | 526.6 | 1.9321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.295 |  | 420.5391 | 0.4175 | 419.42 | 414.87 | 0.4073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.3 |  | 552.4851 | 1.0525 | 551.02 | 540.105 | 0.0555 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0627 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 394.605 |  | 389.2189 | 1.3838 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 972.805 |  | 966.6162 | 0.6402 | 963.41 | 936.99 | 0.8224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.1 |  | 210.9751 | 1.0072 | 207.06 | 202.18 | 0.1642 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 445.13 |  | 442.6651 | 0.5568 | 435.98 | 415.79 | 1.9702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.8 |  | 49.0432 | -0.4958 | 48.96 | 47.01 | 0.041 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.68 |  | 31.156 | 1.6818 | 30.66 | 28.52 | 0.0316 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.785 |  | 748.3785 | 0.1879 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.71 |  | 295.2349 | -0.1778 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.85 |  | 126.7245 | -0.6901 | 128.79 | 125.83 | 0.1589 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.63 |  | 83.5116 | 0.1418 | 83.22 | 79.6 | 1.7099 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 300 |  | 298.7572 | 0.416 | 297.69 | 293.905 | 1.0533 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.85 |  | 407.7291 | 0.2749 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 644.2 |  | 640.0873 | 0.6425 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 999.15 |  | 1008.8392 | -0.9604 | 1036.605 | 998.94 | 0.7827 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.2 |  | 472.8991 | 0.4866 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.295 |  | 142.8712 | 0.2966 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.92 |  | 174.8045 | 0.6382 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 317.21 |  | 316.3063 | 0.2857 | 317.93 | 306.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 836.185 |  | 841.2536 | -0.6025 | 840.47 | 814.62 | 3.974 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 403.375 |  | 406.1807 | -0.6908 | 407.12 | 397.835 | 2.3055 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.82 |  | 114.7635 | -1.6935 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.06 |  | 328.4732 | 1.3964 | 322.67 | 307.545 | 0.3453 | buy_precheck_manual_confirm | none |
| ASML | semiconductor_equipment | 1800.88 |  | 1796.0661 | 0.268 | 1786.525 | 1767.54 | 0.1033 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 558.37 |  | 558.3707 | -0.0001 | 559.22 | 544.305 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 320.25 |  | 318.7294 | 0.4771 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.83 |  | 216.0886 | -0.1197 | 215.465 | 210.975 | 2.7012 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.775 |  | 371.419 | 0.3651 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 296.29 |  | 295.1654 | 0.381 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.815 |  | 67.4603 | 0.5258 | 66.73 | 64.98 | 1.8875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.635 |  | 138.7514 | -0.0839 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.37 |  | 343.5443 | 0.5314 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.06 |  | 507.0912 | 0.3882 | 507.545 | 505.59 | 4.4651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.61 |  | 297.7608 | -0.0506 | 300.24 | 297.585 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.56 |  | 30.8302 | -0.8764 | 30.78 | 29.46 | 0.0654 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.19 |  | 42.7442 | -1.2966 | 42.29 | 40.305 | 0.0474 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.87 |  | 24.1422 | -1.1277 | 24.255 | 23.58 | 0.0838 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1606.19 |  | 1574.0901 | 2.0393 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.92 |  | 555.2492 | 0.8412 | 548.14 | 526.22 | 0.3125 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 914.53 |  | 907.5704 | 0.7668 | 899.59 | 860.605 | 0.5194 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 244.08 |  | 244.5377 | -0.1872 | 248.43 | 244.47 | 0.4343 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| META | cloud_ai_capex | 628.96 |  | 631.3984 | -0.3862 | 647.02 | 632.77 | 0.4293 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.55 |  | 285.6204 | -0.0247 | 286.39 | 280.275 | 2.9172 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 167.745 |  | 166.6855 | 0.6356 | 166.63 | 162.08 | 0.3577 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
