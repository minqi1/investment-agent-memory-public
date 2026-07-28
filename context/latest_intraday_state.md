# Intraday State

- Generated at: `2026-07-29T00:58:53+08:00`
- Market time ET: `2026-07-28T12:58:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'spread_too_wide_or_missing': 29, 'watch_only': 11, 'price_stale_or_missing': 1, 'below_vwap': 4, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.94 |  | 673.7045 | 0.7771 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 495.98 |  | 489.758 | 1.2704 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| SMH | semiconductor_index | 533.67 |  | 527.0413 | 1.2577 | 533.01 | 523.325 | 0.045 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.585 |  | 739.135 | 0.4668 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 533.67 |  | 527.0413 | 1.2577 | 533.01 | 523.325 | 0.045 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 383.685 |  | 378.2698 | 1.4316 | 378.64 | 371.57 | 0.2815 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.585 |  | 739.135 | 0.4668 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.94 |  | 673.7045 | 0.7771 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.4 |  | 329.4966 | 1.4882 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 139.775 |  | 138.2535 | 1.1005 | 139.755 | 137.31 | 0.279 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.625 |  | 292.1403 | 0.5082 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 121.495 |  | 117.8226 | 3.1169 | 117.17 | 115.25 | 0.0576 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 62.48 |  | 60.964 | 2.4867 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 678.94 |  | 673.7045 | 0.7771 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.625 |  | 292.1403 | 0.5082 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.585 |  | 739.135 | 0.4668 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 339.57 |  | 338.8501 | 0.2125 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 5 | SMH | semiconductor_index | 533.67 |  | 527.0413 | 1.2577 | 533.01 | 523.325 | 0.045 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 398.68 |  | 396.0549 | 0.6628 | 400.09 | 392.355 | 0.0251 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 231.605 |  | 230.2005 | 0.6101 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 8 | JCI | data_center_power_cooling | 139.775 |  | 138.2535 | 1.1005 | 139.755 | 137.31 | 0.279 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 334.4 |  | 329.4966 | 1.4882 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 383.685 |  | 378.2698 | 1.4316 | 378.64 | 371.57 | 0.2815 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 495.98 |  | 489.758 | 1.2704 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| 12 | HPE | ai_server_oem | 44.95 |  | 44.4412 | 1.1449 | 46.19 | 44.33 | 0.0667 | watch_only | none |
| 13 | ASML | semiconductor_equipment | 1587.35 |  | 1576.6067 | 0.6814 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SKHY | memory_hbm_storage | 133.37 |  | 131.6063 | 1.3401 | 136.45 | 131.735 | 0.2849 | watch_only | none |
| 15 | TT | data_center_power_cooling | 468.07 |  | 464.7858 | 0.7066 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | META | cloud_ai_capex | 594.53 |  | 593.8699 | 0.1111 | 600.765 | 594.21 | 1.1892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ENTG | semiconductor_materials | 120.06 |  | 119.4389 | 0.52 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | APLD | high_beta_ai_infrastructure | 26.82 |  | 26.5394 | 1.0572 | 27 | 25.42 | 0.2983 | watch_only | none |
| 19 | ORCL | cloud_ai_capex | 121.495 |  | 117.8226 | 3.1169 | 117.17 | 115.25 | 0.0576 | buy_precheck_manual_confirm | none |
| 20 | TER | semiconductor_test_packaging | 313.595 |  | 307.8209 | 1.8758 | 315.21 | 304.11 | 0.1307 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 533.67 |  | 527.0413 | 1.2577 | 533.01 | 523.325 | 0.045 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 383.685 |  | 378.2698 | 1.4316 | 378.64 | 371.57 | 0.2815 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.585 |  | 739.135 | 0.4668 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.94 |  | 673.7045 | 0.7771 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.4 |  | 329.4966 | 1.4882 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 139.775 |  | 138.2535 | 1.1005 | 139.755 | 137.31 | 0.279 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.625 |  | 292.1403 | 0.5082 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 121.495 |  | 117.8226 | 3.1169 | 117.17 | 115.25 | 0.0576 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 62.48 |  | 60.964 | 2.4867 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| 10 | NVDA | ai_accelerator | 198.13 |  | 195.7544 | 1.2135 | 195.4 | 193.65 | 1.0347 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 392.985 |  | 387.118 | 1.5156 | 390.46 | 382.495 | 2.6464 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ASML | semiconductor_equipment | 1587.35 |  | 1576.6067 | 0.6814 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ANET | ai_networking_optical | 168.42 |  | 163.8955 | 2.7606 | 165.975 | 160.51 | 4.0613 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ETN | data_center_power_cooling | 385.94 |  | 380.2827 | 1.4877 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SOXX | semiconductor_index | 495.98 |  | 489.758 | 1.2704 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| 16 | SKHY | memory_hbm_storage | 133.37 |  | 131.6063 | 1.3401 | 136.45 | 131.735 | 0.2849 | watch_only | none |
| 17 | TER | semiconductor_test_packaging | 313.595 |  | 307.8209 | 1.8758 | 315.21 | 304.11 | 0.1307 | watch_only | none |
| 18 | MSFT | cloud_ai_capex | 398.68 |  | 396.0549 | 0.6628 | 400.09 | 392.355 | 0.0251 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 231.605 |  | 230.2005 | 0.6101 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 20 | HPE | ai_server_oem | 44.95 |  | 44.4412 | 1.1449 | 46.19 | 44.33 | 0.0667 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.94 |  | 673.7045 | 0.7771 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.48 |  | 60.964 | 2.4867 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 198.13 |  | 195.7544 | 1.2135 | 195.4 | 193.65 | 1.0347 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 398.68 |  | 396.0549 | 0.6628 | 400.09 | 392.355 | 0.0251 | watch_only | none |
| AAPL | mega_cap_platform | 339.57 |  | 338.8501 | 0.2125 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.4 |  | 329.4966 | 1.4882 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 462.08 |  | 455.1091 | 1.5317 | 472.485 | 453.76 | 0.409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.985 |  | 387.118 | 1.5156 | 390.46 | 382.495 | 2.6464 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.98 |  | 489.758 | 1.2704 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| SMH | semiconductor_index | 533.67 |  | 527.0413 | 1.2577 | 533.01 | 523.325 | 0.045 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 383.685 |  | 378.2698 | 1.4316 | 378.64 | 371.57 | 0.2815 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 826.44 |  | 814.6899 | 1.4423 | 846.4 | 813.91 | 0.6885 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 178.32 |  | 173.8905 | 2.5473 | 181.24 | 172.395 | 0.7571 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 387.04 |  | 374.2591 | 3.415 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.95 |  | 44.4412 | 1.1449 | 46.19 | 44.33 | 0.0667 | watch_only | none |
| SMCI | ai_server_oem | 28.61 |  | 27.9192 | 2.4742 | 28.86 | 27.59 | 0.035 | watch_only | none |
| SPY | market_regime | 742.585 |  | 739.135 | 0.4668 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.625 |  | 292.1403 | 0.5082 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 121.495 |  | 117.8226 | 3.1169 | 117.17 | 115.25 | 0.0576 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.84 |  | 66.1351 | 2.578 | 68.995 | 65.635 | 4.2158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.43 |  | 266.211 | 1.2092 | 273.86 | 266.04 | 0.5679 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.94 |  | 380.2827 | 1.4877 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 588.6 |  | 581.4077 | 1.237 | 603.25 | 584.69 | 5.0527 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 950 |  | 937.0229 | 1.3849 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.07 |  | 464.7858 | 0.7066 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.775 |  | 138.2535 | 1.1005 | 139.755 | 137.31 | 0.279 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 168.42 |  | 163.8955 | 2.7606 | 165.975 | 160.51 | 4.0613 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 244.05 |  | 236.4017 | 3.2353 | 256.145 | 236.73 | 5.0768 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 654.345 |  | 629.6062 | 3.9293 | 673.65 | 624.91 | 1.192 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 344.95 |  | 336.7805 | 2.4258 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 89.085 |  | 85.5704 | 4.1073 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.87 |  | 258.611 | 2.8069 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1587.35 |  | 1576.6067 | 0.6814 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 479.32 |  | 476.9875 | 0.489 | 494.87 | 477.03 | 1.5188 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 270.745 |  | 266.0878 | 1.7502 | 276.85 | 267.14 | 3.4645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.09 |  | 190.5834 | 1.3152 | 194.96 | 189.48 | 1.5226 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 313.595 |  | 307.8209 | 1.8758 | 315.21 | 304.11 | 0.1307 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.36 |  | 236.4978 | 0.7874 | 248.8 | 236.42 | 4.1869 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.41 |  | 46.8252 | -0.8867 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.48 |  | 42.5159 | -0.0845 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.06 |  | 119.4389 | 0.52 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 286.44 |  | 282.1914 | 1.5056 | 296.8 | 283.22 | 0.3945 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 518.005 |  | 518.5643 | -0.1079 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.75 |  | 295.904 | -0.0521 | 297.25 | 293.555 | 4.4937 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.82 |  | 26.5394 | 1.0572 | 27 | 25.42 | 0.2983 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.515 |  | 33.6925 | 2.4412 | 35.08 | 33.52 | 0.029 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.41 |  | 20.0066 | 2.0165 | 20.97 | 19.755 | 0.098 | watch_only | none |
| SNDK | memory_hbm_storage | 1104.28 |  | 1102.7254 | 0.141 | 1185.19 | 1114.57 | 1.2252 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 460.515 |  | 437.2291 | 5.3258 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 753.705 |  | 725.7418 | 3.8531 | 774.805 | 719.02 | 4.1807 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.605 |  | 230.2005 | 0.6101 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.53 |  | 593.8699 | 0.1111 | 600.765 | 594.21 | 1.1892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 248.74 |  | 245.2354 | 1.4291 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.37 |  | 131.6063 | 1.3401 | 136.45 | 131.735 | 0.2849 | watch_only | none |
