# Intraday State

- Generated at: `2026-07-29T03:16:55+08:00`
- Market time ET: `2026-07-28T15:16:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 11, 'manual_confirm_candidate': 9, 'below_vwap': 5, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.13 |  | 674.2761 | 0.4233 | 677.3 | 670.84 | 0.0251 | watch_only | none |
| SOXX | semiconductor_index | 494.42 |  | 490.1027 | 0.8809 | 497.64 | 485.42 | 0.0667 | watch_only | none |
| SMH | semiconductor_index | 532.06 |  | 527.5257 | 0.8595 | 533.01 | 523.325 | 0.0338 | watch_only | none |
| SPY | market_regime | 741.43 |  | 739.6649 | 0.2386 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.54 |  | 196.1505 | 0.7084 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.175 |  | 388.0407 | 1.3231 | 390.46 | 382.495 | 0.1831 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 383.19 |  | 378.7813 | 1.1639 | 378.64 | 371.57 | 0.1148 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.43 |  | 739.6649 | 0.2386 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 169.095 |  | 165.1921 | 2.3626 | 165.975 | 160.51 | 0.2543 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 334.21 |  | 331.1798 | 0.915 | 330.21 | 324.97 | 0.1257 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 140.72 |  | 138.8588 | 1.3403 | 139.755 | 137.31 | 0.0995 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 121.11 |  | 118.7595 | 1.9792 | 117.17 | 115.25 | 0.0743 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.045 |  | 20.16 | 4.3897 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.43 |  | 739.6649 | 0.2386 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 937.88 |  | 937.484 | 0.0422 | 955.825 | 935.665 | 0.0746 | watch_only | none |
| 3 | IWM | market_regime | 293.18 |  | 292.4451 | 0.2513 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | NVDA | ai_accelerator | 197.54 |  | 196.1505 | 0.7084 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 231.14 |  | 230.5381 | 0.2611 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 339.2 |  | 338.9788 | 0.0653 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 7 | QQQ | market_regime | 677.13 |  | 674.2761 | 0.4233 | 677.3 | 670.84 | 0.0251 | watch_only | none |
| 8 | CRWV | gpu_cloud_ai_factory | 66.45 |  | 66.2714 | 0.2694 | 68.995 | 65.635 | 0.1505 | watch_only | none |
| 9 | JCI | data_center_power_cooling | 140.72 |  | 138.8588 | 1.3403 | 139.755 | 137.31 | 0.0995 | buy_precheck_manual_confirm | none |
| 10 | TSM | foundry | 393.175 |  | 388.0407 | 1.3231 | 390.46 | 382.495 | 0.1831 | buy_precheck_manual_confirm | none |
| 11 | AVGO | custom_silicon_networking | 383.19 |  | 378.7813 | 1.1639 | 378.64 | 371.57 | 0.1148 | buy_precheck_manual_confirm | none |
| 12 | GOOGL | cloud_ai_capex | 334.21 |  | 331.1798 | 0.915 | 330.21 | 324.97 | 0.1257 | buy_precheck_manual_confirm | none |
| 13 | ARM | ai_accelerator | 246 |  | 245.2335 | 0.3126 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMH | semiconductor_index | 532.06 |  | 527.5257 | 0.8595 | 533.01 | 523.325 | 0.0338 | watch_only | none |
| 15 | SOXX | semiconductor_index | 494.42 |  | 490.1027 | 0.8809 | 497.64 | 485.42 | 0.0667 | watch_only | none |
| 16 | ENTG | semiconductor_materials | 119.3 |  | 119.1781 | 0.1023 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | HPE | ai_server_oem | 45.15 |  | 44.4989 | 1.4631 | 46.19 | 44.33 | 0.0443 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.425 |  | 28.0156 | 1.4615 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 19 | CORZ | high_beta_ai_infrastructure | 21.045 |  | 20.16 | 4.3897 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |
| 20 | COHU | semiconductor_test_packaging | 42.7 |  | 42.4446 | 0.6017 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.54 |  | 196.1505 | 0.7084 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.175 |  | 388.0407 | 1.3231 | 390.46 | 382.495 | 0.1831 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 383.19 |  | 378.7813 | 1.1639 | 378.64 | 371.57 | 0.1148 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.43 |  | 739.6649 | 0.2386 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 169.095 |  | 165.1921 | 2.3626 | 165.975 | 160.51 | 0.2543 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 334.21 |  | 331.1798 | 0.915 | 330.21 | 324.97 | 0.1257 | buy_precheck_manual_confirm | none |
| 7 | JCI | data_center_power_cooling | 140.72 |  | 138.8588 | 1.3403 | 139.755 | 137.31 | 0.0995 | buy_precheck_manual_confirm | none |
| 8 | ORCL | cloud_ai_capex | 121.11 |  | 118.7595 | 1.9792 | 117.17 | 115.25 | 0.0743 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 21.045 |  | 20.16 | 4.3897 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1590.67 |  | 1577.6593 | 0.8247 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 388.16 |  | 381.5054 | 1.7443 | 384.565 | 377.43 | 3.3749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 317.02 |  | 309.2072 | 2.5267 | 315.21 | 304.11 | 3.2175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SMH | semiconductor_index | 532.06 |  | 527.5257 | 0.8595 | 533.01 | 523.325 | 0.0338 | watch_only | none |
| 14 | SOXX | semiconductor_index | 494.42 |  | 490.1027 | 0.8809 | 497.64 | 485.42 | 0.0667 | watch_only | none |
| 15 | QQQ | market_regime | 677.13 |  | 674.2761 | 0.4233 | 677.3 | 670.84 | 0.0251 | watch_only | none |
| 16 | GEV | data_center_power_cooling | 937.88 |  | 937.484 | 0.0422 | 955.825 | 935.665 | 0.0746 | watch_only | none |
| 17 | IWM | market_regime | 293.18 |  | 292.4451 | 0.2513 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.14 |  | 230.5381 | 0.2611 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| 19 | HPE | ai_server_oem | 45.15 |  | 44.4989 | 1.4631 | 46.19 | 44.33 | 0.0443 | watch_only | none |
| 20 | SMCI | ai_server_oem | 28.425 |  | 28.0156 | 1.4615 | 28.86 | 27.59 | 0.0352 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.13 |  | 674.2761 | 0.4233 | 677.3 | 670.84 | 0.0251 | watch_only | none |
| TQQQ | leveraged_tool | 61.91 |  | 61.1483 | 1.2456 | 62.01 | 60.23 | 0.0323 | watch_only | none |
| NVDA | ai_accelerator | 197.54 |  | 196.1505 | 0.7084 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.265 |  | 396.3665 | -0.5302 | 400.09 | 392.355 | 0.3348 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.2 |  | 338.9788 | 0.0653 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.21 |  | 331.1798 | 0.915 | 330.21 | 324.97 | 0.1257 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 459.46 |  | 455.6643 | 0.833 | 472.485 | 453.76 | 0.8118 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.175 |  | 388.0407 | 1.3231 | 390.46 | 382.495 | 0.1831 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 494.42 |  | 490.1027 | 0.8809 | 497.64 | 485.42 | 0.0667 | watch_only | none |
| SMH | semiconductor_index | 532.06 |  | 527.5257 | 0.8595 | 533.01 | 523.325 | 0.0338 | watch_only | none |
| AVGO | custom_silicon_networking | 383.19 |  | 378.7813 | 1.1639 | 378.64 | 371.57 | 0.1148 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 824.485 |  | 815.9299 | 1.0485 | 846.4 | 813.91 | 0.9169 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.75 |  | 174.2459 | 0.8632 | 181.24 | 172.395 | 1.6387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 390.595 |  | 375.6867 | 3.9683 | 402 | 374.02 | 2.7292 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.15 |  | 44.4989 | 1.4631 | 46.19 | 44.33 | 0.0443 | watch_only | none |
| SMCI | ai_server_oem | 28.425 |  | 28.0156 | 1.4615 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 741.43 |  | 739.6649 | 0.2386 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.18 |  | 292.4451 | 0.2513 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 121.11 |  | 118.7595 | 1.9792 | 117.17 | 115.25 | 0.0743 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.45 |  | 66.2714 | 0.2694 | 68.995 | 65.635 | 0.1505 | watch_only | none |
| VRT | data_center_power_cooling | 268.51 |  | 266.1947 | 0.8698 | 273.86 | 266.04 | 0.432 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 388.16 |  | 381.5054 | 1.7443 | 384.565 | 377.43 | 3.3749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 590.19 |  | 582.7843 | 1.2707 | 603.25 | 584.69 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 937.88 |  | 937.484 | 0.0422 | 955.825 | 935.665 | 0.0746 | watch_only | none |
| TT | data_center_power_cooling | 468.68 |  | 465.605 | 0.6604 | 477.73 | 460.77 | 4.4892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.72 |  | 138.8588 | 1.3403 | 139.755 | 137.31 | 0.0995 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169.095 |  | 165.1921 | 2.3626 | 165.975 | 160.51 | 0.2543 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 243.555 |  | 237.8137 | 2.4142 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 648.55 |  | 632.6329 | 2.516 | 673.65 | 624.91 | 4.12 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 345.15 |  | 337.6079 | 2.234 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.14 |  | 85.8995 | 2.6082 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.955 |  | 259.2787 | 1.0322 | 268.265 | 253.05 | 4.6077 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1590.67 |  | 1577.6593 | 0.8247 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 481.43 |  | 476.5321 | 1.0278 | 494.87 | 477.03 | 0.9596 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 273.11 |  | 266.9815 | 2.2955 | 276.85 | 267.14 | 4.2437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.61 |  | 190.8818 | 1.4293 | 194.96 | 189.48 | 1.7148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 317.02 |  | 309.2072 | 2.5267 | 315.21 | 304.11 | 3.2175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 240.56 |  | 237.1033 | 1.4579 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.35 |  | 46.6685 | -0.6826 | 51.64 | 47.435 | 2.4811 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.7 |  | 42.4446 | 0.6017 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.3 |  | 119.1781 | 0.1023 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 285.68 |  | 282.4469 | 1.1447 | 296.8 | 283.22 | 3.924 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 515.635 |  | 518.0006 | -0.4567 | 518.6 | 511.495 | 0.0815 | below_vwap | below_vwap |
| APD | industrial_gases | 295.35 |  | 295.7324 | -0.1293 | 297.25 | 293.555 | 0.0609 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.41 |  | 26.5099 | -0.3768 | 27 | 25.42 | 1.4767 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.51 |  | 33.7042 | -0.5762 | 35.08 | 33.52 | 0.0298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.045 |  | 20.16 | 4.3897 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1116.8 |  | 1099.7201 | 1.5531 | 1185.19 | 1114.57 | 3.134 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 459.165 |  | 441.0358 | 4.1106 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 747.15 |  | 733.2459 | 1.8962 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.14 |  | 230.5381 | 0.2611 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| META | cloud_ai_capex | 593.58 |  | 593.8508 | -0.0456 | 600.765 | 594.21 | 1.1456 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 246 |  | 245.2335 | 0.3126 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 131.38 |  | 131.5288 | -0.1131 | 136.45 | 131.735 | 0.9438 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
