# Intraday State

- Generated at: `2026-07-22T02:39:08+08:00`
- Market time ET: `2026-07-21T14:39:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'watch_only': 4, 'below_vwap': 11, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 1, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.23 |  | 707.1657 | 0.2919 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 553.65 |  | 549.2125 | 0.808 | 550.77 | 545.11 | 0.056 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.61 |  | 581.0165 | 0.6185 | 582.03 | 576.57 | 0.0308 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.14 |  | 747.1352 | 0.1345 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 584.61 |  | 581.0165 | 0.6185 | 582.03 | 576.57 | 0.0308 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 553.65 |  | 549.2125 | 0.808 | 550.77 | 545.11 | 0.056 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.23 |  | 707.1657 | 0.2919 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.14 |  | 747.1352 | 0.1345 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | LITE | ai_networking_optical | 836.94 |  | 825.1238 | 1.4321 | 823.31 | 800.37 | 0.2784 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 296.07 |  | 294.6661 | 0.4764 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 142.22 |  | 141.8623 | 0.2521 | 142.15 | 140.105 | 0.1688 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0198 | 0.23 | 23.32 | 22.79 | 0.0831 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 327.44 |  | 326.274 | 0.3574 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 10 | AAOI | ai_networking_optical | 118.81 |  | 116.4556 | 2.0218 | 109.39 | 107.58 | 0.2946 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 25.315 |  | 24.9427 | 1.4927 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 30.36 |  | 30.2915 | 0.2262 | 29.735 | 28.785 | 0.0988 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.49 |  | 70.8097 | 0.9607 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 709.23 |  | 707.1657 | 0.2919 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 748.14 |  | 747.1352 | 0.1345 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 142.22 |  | 141.8623 | 0.2521 | 142.15 | 140.105 | 0.1688 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 584.61 |  | 581.0165 | 0.6185 | 582.03 | 576.57 | 0.0308 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 206.765 |  | 206.0526 | 0.3457 | 208.61 | 206.275 | 0.0145 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 385.85 |  | 384.897 | 0.2476 | 390.11 | 382.13 | 0.1477 | watch_only | none |
| 7 | IWM | market_regime | 296.07 |  | 294.6661 | 0.4764 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 470.75 |  | 469.9353 | 0.1734 | 475.98 | 467.01 | 0.0892 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 327.44 |  | 326.274 | 0.3574 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0198 | 0.23 | 23.32 | 22.79 | 0.0831 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 30.36 |  | 30.2915 | 0.2262 | 29.735 | 28.785 | 0.0988 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 217.73 |  | 216.9175 | 0.3745 | 220.76 | 214.41 | 0.0367 | watch_only | none |
| 13 | SOXX | semiconductor_index | 553.65 |  | 549.2125 | 0.808 | 550.77 | 545.11 | 0.056 | buy_precheck_manual_confirm | none |
| 14 | LRCX | semiconductor_equipment | 320.68 |  | 320.4862 | 0.0605 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 640.41 |  | 638.6583 | 0.2743 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | DELL | ai_server_oem | 403.86 |  | 403.5334 | 0.0809 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | CIEN | ai_networking_optical | 406.98 |  | 405.6394 | 0.3305 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMAT | semiconductor_equipment | 566.71 |  | 564.7423 | 0.3484 | 564.91 | 552.71 | 0.3706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SMCI | ai_server_oem | 25.315 |  | 24.9427 | 1.4927 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 20 | LITE | ai_networking_optical | 836.94 |  | 825.1238 | 1.4321 | 823.31 | 800.37 | 0.2784 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 584.61 |  | 581.0165 | 0.6185 | 582.03 | 576.57 | 0.0308 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 553.65 |  | 549.2125 | 0.808 | 550.77 | 545.11 | 0.056 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 709.23 |  | 707.1657 | 0.2919 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 748.14 |  | 747.1352 | 0.1345 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | LITE | ai_networking_optical | 836.94 |  | 825.1238 | 1.4321 | 823.31 | 800.37 | 0.2784 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 296.07 |  | 294.6661 | 0.4764 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 142.22 |  | 141.8623 | 0.2521 | 142.15 | 140.105 | 0.1688 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0198 | 0.23 | 23.32 | 22.79 | 0.0831 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 327.44 |  | 326.274 | 0.3574 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| 10 | AAOI | ai_networking_optical | 118.81 |  | 116.4556 | 2.0218 | 109.39 | 107.58 | 0.2946 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 25.315 |  | 24.9427 | 1.4927 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 30.36 |  | 30.2915 | 0.2262 | 29.735 | 28.785 | 0.0988 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 71.49 |  | 70.8097 | 0.9607 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| 14 | ASML | semiconductor_equipment | 1805.425 |  | 1809.5313 | -0.2269 | 1804.54 | 1786.51 | 0.1069 | below_vwap | below_vwap |
| 15 | TSM | foundry | 423.905 |  | 420.527 | 0.8033 | 418.76 | 415.025 | 0.4978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 544.07 |  | 534.9601 | 1.7029 | 532.365 | 524.72 | 0.5679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MU | memory_hbm_storage | 973.36 |  | 952.8402 | 2.1535 | 944.99 | 923 | 0.4387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 406.98 |  | 405.6394 | 0.3305 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMAT | semiconductor_equipment | 566.71 |  | 564.7423 | 0.3484 | 564.91 | 552.71 | 0.3706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 893.33 |  | 878.6372 | 1.6722 | 866.73 | 845.78 | 1.3892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.23 |  | 707.1657 | 0.2919 | 707.09 | 704.52 | 0.0056 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.49 |  | 70.8097 | 0.9607 | 70.84 | 70.09 | 0.028 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.765 |  | 206.0526 | 0.3457 | 208.61 | 206.275 | 0.0145 | watch_only | none |
| MSFT | cloud_ai_capex | 398.18 |  | 399.1268 | -0.2372 | 401.45 | 396.36 | 0.0377 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.44 |  | 326.274 | 0.3574 | 325.59 | 322.63 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 348.535 |  | 349.1517 | -0.1766 | 350.985 | 347.69 | 0.0402 | below_vwap | below_vwap |
| AMD | ai_accelerator | 544.07 |  | 534.9601 | 1.7029 | 532.365 | 524.72 | 0.5679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 423.905 |  | 420.527 | 0.8033 | 418.76 | 415.025 | 0.4978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.65 |  | 549.2125 | 0.808 | 550.77 | 545.11 | 0.056 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 584.61 |  | 581.0165 | 0.6185 | 582.03 | 576.57 | 0.0308 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.85 |  | 384.897 | 0.2476 | 390.11 | 382.13 | 0.1477 | watch_only | none |
| MU | memory_hbm_storage | 973.36 |  | 952.8402 | 2.1535 | 944.99 | 923 | 0.4387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 208.55 |  | 207.7474 | 0.3863 | 208.61 | 205.31 | 0.5131 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.86 |  | 403.5334 | 0.0809 | 405.78 | 397.185 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.415 |  | 46.5367 | -0.2615 | 46.685 | 45.835 | 0.1077 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.315 |  | 24.9427 | 1.4927 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.14 |  | 747.1352 | 0.1345 | 746.6 | 744.3 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.07 |  | 294.6661 | 0.4764 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.915 |  | 125.7053 | 0.9623 | 126.01 | 122.48 | 0.5043 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.69 |  | 78.5641 | 0.1603 | 76.615 | 74.55 | 2.1604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 304.65 |  | 301.9615 | 0.8903 | 305.09 | 299.13 | 2.1566 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 403.94 |  | 405.9129 | -0.486 | 411.01 | 404.21 | 4.6269 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 640.41 |  | 638.6583 | 0.2743 | 645.815 | 635.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1087.05 |  | 1095.6107 | -0.7814 | 1140.63 | 1103.815 | 2.4084 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.75 |  | 469.9353 | 0.1734 | 475.98 | 467.01 | 0.0892 | watch_only | none |
| JCI | data_center_power_cooling | 142.22 |  | 141.8623 | 0.2521 | 142.15 | 140.105 | 0.1688 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 174.12 |  | 175.0999 | -0.5596 | 176.06 | 172.32 | 4.83 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 317.52 |  | 312.8739 | 1.485 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 836.94 |  | 825.1238 | 1.4321 | 823.31 | 800.37 | 0.2784 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 406.98 |  | 405.6394 | 0.3305 | 401.91 | 397.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 118.81 |  | 116.4556 | 2.0218 | 109.39 | 107.58 | 0.2946 | buy_precheck_manual_confirm | none |
| ALAB | ai_networking_optical | 322.2 |  | 325.5056 | -1.0155 | 329.97 | 323.92 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.425 |  | 1809.5313 | -0.2269 | 1804.54 | 1786.51 | 0.1069 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.71 |  | 564.7423 | 0.3484 | 564.91 | 552.71 | 0.3706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.68 |  | 320.4862 | 0.0605 | 328.135 | 317.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 217.73 |  | 216.9175 | 0.3745 | 220.76 | 214.41 | 0.0367 | watch_only | none |
| TER | semiconductor_test_packaging | 378.535 |  | 371.6104 | 1.8634 | 365.97 | 356.39 | 4.063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 300.27 |  | 297.2871 | 1.0034 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.75 |  | 66.1566 | 0.897 | 66.54 | 65 | 4.0449 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 56.18 |  | 55.1659 | 1.8383 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 141.14 |  | 141.5306 | -0.276 | 142.09 | 139.41 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.07 |  | 340.0912 | 1.464 | 340.205 | 336.3 | 4.4774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 506.43 |  | 506.3913 | 0.0077 | 512.83 | 507.675 | 0.0316 | below_opening_15m_low | below_opening_15m_low |
| APD | industrial_gases | 298.81 |  | 299.3128 | -0.168 | 301.84 | 296.5 | 4.7053 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.36 |  | 30.2915 | 0.2262 | 29.735 | 28.785 | 0.0988 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 40.93 |  | 41.7929 | -2.0646 | 41.65 | 40.435 | 0.0489 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.075 |  | 24.0198 | 0.23 | 23.32 | 22.79 | 0.0831 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1563.92 |  | 1543.1583 | 1.3454 | 1540.85 | 1490.29 | 0.415 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 548.93 |  | 540.8533 | 1.4933 | 533.56 | 517.335 | 1.2242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 893.33 |  | 878.6372 | 1.6722 | 866.73 | 845.78 | 1.3892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.625 |  | 247.8537 | -0.0923 | 248.915 | 247.32 | 0.0606 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.79 |  | 647.3669 | -0.0891 | 655.425 | 643.54 | 0.555 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 290.845 |  | 286.7495 | 1.4282 | 286.39 | 275.86 | 1.2653 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 171.22 |  | 167.2285 | 2.3868 | 165.88 | 160.77 | 1.1973 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
