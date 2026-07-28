# Intraday State

- Generated at: `2026-07-29T03:47:34+08:00`
- Market time ET: `2026-07-28T15:47:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 21, 'manual_confirm_candidate': 4, 'below_vwap': 7, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 1, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676 |  | 674.4262 | 0.2333 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| SOXX | semiconductor_index | 493.46 |  | 490.3592 | 0.6324 | 497.64 | 485.42 | 0.079 | watch_only | none |
| SMH | semiconductor_index | 530.95 |  | 527.8272 | 0.5916 | 533.01 | 523.325 | 0.032 | watch_only | none |
| SPY | market_regime | 741.005 |  | 739.8453 | 0.1567 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.06 |  | 196.2565 | 0.4094 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.64 |  | 388.9596 | 1.2033 | 390.46 | 382.495 | 0.0559 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.005 |  | 739.8453 | 0.1567 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.59 |  | 139.0966 | 1.0736 | 139.755 | 137.31 | 0.0711 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.005 |  | 739.8453 | 0.1567 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 676 |  | 674.4262 | 0.2333 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| 3 | IWM | market_regime | 293.02 |  | 292.4889 | 0.1816 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 4 | NVDA | ai_accelerator | 197.06 |  | 196.2565 | 0.4094 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 230.96 |  | 230.5706 | 0.1689 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 339.36 |  | 339.0167 | 0.1013 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 7 | APLD | high_beta_ai_infrastructure | 26.61 |  | 26.539 | 0.2676 | 27 | 25.42 | 0.0752 | watch_only | none |
| 8 | AMD | ai_accelerator | 456.7 |  | 456.1034 | 0.1308 | 472.485 | 453.76 | 0.2649 | watch_only | none |
| 9 | MU | memory_hbm_storage | 820.57 |  | 816.5909 | 0.4873 | 846.4 | 813.91 | 0.1194 | watch_only | none |
| 10 | SMH | semiconductor_index | 530.95 |  | 527.8272 | 0.5916 | 533.01 | 523.325 | 0.032 | watch_only | none |
| 11 | SOXX | semiconductor_index | 493.46 |  | 490.3592 | 0.6324 | 497.64 | 485.42 | 0.079 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 140.59 |  | 139.0966 | 1.0736 | 139.755 | 137.31 | 0.0711 | buy_precheck_manual_confirm | none |
| 13 | AMAT | semiconductor_equipment | 479.105 |  | 476.965 | 0.4487 | 494.87 | 477.03 | 0.3381 | watch_only | none |
| 14 | TSM | foundry | 393.64 |  | 388.9596 | 1.2033 | 390.46 | 382.495 | 0.0559 | buy_precheck_manual_confirm | none |
| 15 | PWR | data_center_power_cooling | 588.39 |  | 583.4658 | 0.844 | 603.25 | 584.69 | 0.0969 | watch_only | none |
| 16 | HPE | ai_server_oem | 45.255 |  | 44.6849 | 1.2759 | 46.19 | 44.33 | 0.0221 | watch_only | none |
| 17 | SMCI | ai_server_oem | 28.39 |  | 28.0509 | 1.2089 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 18 | IREN | high_beta_ai_infrastructure | 34.055 |  | 33.7378 | 0.9402 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| 19 | CRWV | gpu_cloud_ai_factory | 67.215 |  | 66.3161 | 1.3555 | 68.995 | 65.635 | 0.0744 | watch_only | none |
| 20 | ASML | semiconductor_equipment | 1585.915 |  | 1578.7969 | 0.4509 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.06 |  | 196.2565 | 0.4094 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.64 |  | 388.9596 | 1.2033 | 390.46 | 382.495 | 0.0559 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.005 |  | 739.8453 | 0.1567 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 140.59 |  | 139.0966 | 1.0736 | 139.755 | 137.31 | 0.0711 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 383.795 |  | 379.2072 | 1.2098 | 378.64 | 371.57 | 1.6285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 168.955 |  | 165.3181 | 2.1999 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | GOOGL | cloud_ai_capex | 334.025 |  | 331.6159 | 0.7265 | 330.21 | 324.97 | 0.3712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ETN | data_center_power_cooling | 386.505 |  | 381.7451 | 1.2469 | 384.565 | 377.43 | 2.4967 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ORCL | cloud_ai_capex | 120.58 |  | 118.9783 | 1.3462 | 117.17 | 115.25 | 2.0153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | TER | semiconductor_test_packaging | 320.37 |  | 310.6649 | 3.124 | 315.21 | 304.11 | 4.2857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | MU | memory_hbm_storage | 820.57 |  | 816.5909 | 0.4873 | 846.4 | 813.91 | 0.1194 | watch_only | none |
| 12 | SMH | semiconductor_index | 530.95 |  | 527.8272 | 0.5916 | 533.01 | 523.325 | 0.032 | watch_only | none |
| 13 | SOXX | semiconductor_index | 493.46 |  | 490.3592 | 0.6324 | 497.64 | 485.42 | 0.079 | watch_only | none |
| 14 | QQQ | market_regime | 676 |  | 674.4262 | 0.2333 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 588.39 |  | 583.4658 | 0.844 | 603.25 | 584.69 | 0.0969 | watch_only | none |
| 16 | WDC | memory_hbm_storage | 460.09 |  | 442.884 | 3.885 | 465.04 | 435.22 | 0.0891 | watch_only | none |
| 17 | IWM | market_regime | 293.02 |  | 292.4889 | 0.1816 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 18 | AMAT | semiconductor_equipment | 479.105 |  | 476.965 | 0.4487 | 494.87 | 477.03 | 0.3381 | watch_only | none |
| 19 | AMD | ai_accelerator | 456.7 |  | 456.1034 | 0.1308 | 472.485 | 453.76 | 0.2649 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 230.96 |  | 230.5706 | 0.1689 | 233.05 | 229.7 | 0.013 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676 |  | 674.4262 | 0.2333 | 677.3 | 670.84 | 0.0281 | watch_only | none |
| TQQQ | leveraged_tool | 61.66 |  | 61.1859 | 0.7748 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.06 |  | 196.2565 | 0.4094 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.05 |  | 396.1188 | -0.7747 | 400.09 | 392.355 | 0.7887 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 339.36 |  | 339.0167 | 0.1013 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.025 |  | 331.6159 | 0.7265 | 330.21 | 324.97 | 0.3712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 456.7 |  | 456.1034 | 0.1308 | 472.485 | 453.76 | 0.2649 | watch_only | none |
| TSM | foundry | 393.64 |  | 388.9596 | 1.2033 | 390.46 | 382.495 | 0.0559 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.46 |  | 490.3592 | 0.6324 | 497.64 | 485.42 | 0.079 | watch_only | none |
| SMH | semiconductor_index | 530.95 |  | 527.8272 | 0.5916 | 533.01 | 523.325 | 0.032 | watch_only | none |
| AVGO | custom_silicon_networking | 383.795 |  | 379.2072 | 1.2098 | 378.64 | 371.57 | 1.6285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 820.57 |  | 816.5909 | 0.4873 | 846.4 | 813.91 | 0.1194 | watch_only | none |
| MRVL | custom_silicon_networking | 175.065 |  | 174.3753 | 0.3955 | 181.24 | 172.395 | 1.3081 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 389.835 |  | 376.6944 | 3.4884 | 402 | 374.02 | 0.136 | watch_only | none |
| HPE | ai_server_oem | 45.255 |  | 44.6849 | 1.2759 | 46.19 | 44.33 | 0.0221 | watch_only | none |
| SMCI | ai_server_oem | 28.39 |  | 28.0509 | 1.2089 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 741.005 |  | 739.8453 | 0.1567 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.02 |  | 292.4889 | 0.1816 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.58 |  | 118.9783 | 1.3462 | 117.17 | 115.25 | 2.0153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67.215 |  | 66.3161 | 1.3555 | 68.995 | 65.635 | 0.0744 | watch_only | none |
| VRT | data_center_power_cooling | 268.975 |  | 266.4086 | 0.9633 | 273.86 | 266.04 | 4.8406 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.505 |  | 381.7451 | 1.2469 | 384.565 | 377.43 | 2.4967 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 588.39 |  | 583.4658 | 0.844 | 603.25 | 584.69 | 0.0969 | watch_only | none |
| GEV | data_center_power_cooling | 940.42 |  | 937.707 | 0.2893 | 955.825 | 935.665 | 0.3892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.45 |  | 466.0342 | 0.5184 | 477.73 | 460.77 | 4.6088 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.59 |  | 139.0966 | 1.0736 | 139.755 | 137.31 | 0.0711 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 168.955 |  | 165.3181 | 2.1999 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 244.385 |  | 238.548 | 2.4469 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 653.17 |  | 634.374 | 2.9629 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 349.55 |  | 338.1635 | 3.3672 | 354.09 | 338.14 | 0.1144 | watch_only | none |
| AAOI | ai_networking_optical | 88.16 |  | 86.1288 | 2.3584 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 262.105 |  | 259.8148 | 0.8815 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1585.915 |  | 1578.7969 | 0.4509 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 479.105 |  | 476.965 | 0.4487 | 494.87 | 477.03 | 0.3381 | watch_only | none |
| LRCX | semiconductor_equipment | 271.23 |  | 267.3311 | 1.4585 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 193.635 |  | 191.2632 | 1.24 | 194.96 | 189.48 | 0.4235 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 320.37 |  | 310.6649 | 3.124 | 315.21 | 304.11 | 4.2857 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 240.4 |  | 237.3019 | 1.3055 | 248.8 | 236.42 | 4.8586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.97 |  | 46.6395 | -1.4356 | 51.64 | 47.435 | 2.3059 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.35 |  | 42.4933 | -0.3372 | 44.155 | 41.78 | 0.2597 | below_vwap | below_vwap |
| ENTG | semiconductor_materials | 118.96 |  | 119.2087 | -0.2086 | 121 | 117.72 | 0.1681 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 285.35 |  | 282.7283 | 0.9273 | 296.8 | 283.22 | 0.2698 | watch_only | none |
| LIN | industrial_gases | 513.765 |  | 517.71 | -0.762 | 518.6 | 511.495 | 0.1869 | below_vwap | below_vwap |
| APD | industrial_gases | 294.68 |  | 295.6714 | -0.3353 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.61 |  | 26.539 | 0.2676 | 27 | 25.42 | 0.0752 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.055 |  | 33.7378 | 0.9402 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.79 |  | 20.2066 | 2.8874 | 20.97 | 19.755 | 0.0962 | watch_only | none |
| SNDK | memory_hbm_storage | 1107.94 |  | 1101.1125 | 0.6201 | 1185.19 | 1114.57 | 0.7934 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 460.09 |  | 442.884 | 3.885 | 465.04 | 435.22 | 0.0891 | watch_only | none |
| STX | memory_hbm_storage | 744.89 |  | 734.4127 | 1.4266 | 774.805 | 719.02 | 0.6417 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.96 |  | 230.5706 | 0.1689 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594.06 |  | 593.8219 | 0.0401 | 600.765 | 594.21 | 0.0353 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 244.75 |  | 245.3158 | -0.2306 | 253.38 | 243.72 | 0.3636 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 131.26 |  | 131.5621 | -0.2297 | 136.45 | 131.735 | 0.3885 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
