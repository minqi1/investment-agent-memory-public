# Intraday State

- Generated at: `2026-07-29T03:28:24+08:00`
- Market time ET: `2026-07-28T15:28:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 12, 'manual_confirm_candidate': 10, 'below_vwap': 4, 'spread_too_wide_or_missing': 27, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.22 |  | 674.3208 | 0.4299 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| SOXX | semiconductor_index | 496.65 |  | 490.1991 | 1.316 | 497.64 | 485.42 | 0.0524 | watch_only | none |
| SMH | semiconductor_index | 533.6 |  | 527.6619 | 1.1254 | 533.01 | 523.325 | 0.0431 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 741.425 |  | 739.7445 | 0.2272 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.72 |  | 196.1932 | 0.7782 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 394.12 |  | 388.4296 | 1.465 | 390.46 | 382.495 | 0.0812 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 533.6 |  | 527.6619 | 1.1254 | 533.01 | 523.325 | 0.0431 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 384.21 |  | 378.984 | 1.3789 | 378.64 | 371.57 | 0.1145 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 741.425 |  | 739.7445 | 0.2272 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1592.8 |  | 1578.1475 | 0.9285 | 1586.01 | 1565.95 | 0.1074 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 334.18 |  | 331.3137 | 0.8651 | 330.21 | 324.97 | 0.0209 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 140.88 |  | 138.9397 | 1.3965 | 139.755 | 137.31 | 0.0852 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 293.37 |  | 292.4596 | 0.3113 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1821 | 4.1023 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.425 |  | 739.7445 | 0.2272 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.37 |  | 292.4596 | 0.3113 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 197.72 |  | 196.1932 | 0.7782 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 230.86 |  | 230.5465 | 0.136 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.21 |  | 338.9852 | 0.0663 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 6 | QQQ | market_regime | 677.22 |  | 674.3208 | 0.4299 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| 7 | SMH | semiconductor_index | 533.6 |  | 527.6619 | 1.1254 | 533.01 | 523.325 | 0.0431 | buy_precheck_manual_confirm | none |
| 8 | ASML | semiconductor_equipment | 1592.8 |  | 1578.1475 | 0.9285 | 1586.01 | 1565.95 | 0.1074 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 394.12 |  | 388.4296 | 1.465 | 390.46 | 382.495 | 0.0812 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 384.21 |  | 378.984 | 1.3789 | 378.64 | 371.57 | 0.1145 | buy_precheck_manual_confirm | none |
| 11 | GOOGL | cloud_ai_capex | 334.18 |  | 331.3137 | 0.8651 | 330.21 | 324.97 | 0.0209 | buy_precheck_manual_confirm | none |
| 12 | JCI | data_center_power_cooling | 140.88 |  | 138.9397 | 1.3965 | 139.755 | 137.31 | 0.0852 | buy_precheck_manual_confirm | none |
| 13 | MU | memory_hbm_storage | 826.68 |  | 816.1662 | 1.2882 | 846.4 | 813.91 | 0.0605 | watch_only | none |
| 14 | SOXX | semiconductor_index | 496.65 |  | 490.1991 | 1.316 | 497.64 | 485.42 | 0.0524 | watch_only | none |
| 15 | HPE | ai_server_oem | 45.18 |  | 44.5768 | 1.3531 | 46.19 | 44.33 | 0.0664 | watch_only | none |
| 16 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1821 | 4.1023 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |
| 17 | IREN | high_beta_ai_infrastructure | 34.07 |  | 33.707 | 1.0768 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| 18 | VRT | data_center_power_cooling | 269.07 |  | 266.2598 | 1.0554 | 273.86 | 266.04 | 0.1672 | watch_only | none |
| 19 | APLD | high_beta_ai_infrastructure | 26.88 |  | 26.52 | 1.3576 | 27 | 25.42 | 0.1488 | watch_only | none |
| 20 | GEV | data_center_power_cooling | 940.04 |  | 937.5186 | 0.2689 | 955.825 | 935.665 | 0.3979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.72 |  | 196.1932 | 0.7782 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 394.12 |  | 388.4296 | 1.465 | 390.46 | 382.495 | 0.0812 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 533.6 |  | 527.6619 | 1.1254 | 533.01 | 523.325 | 0.0431 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 384.21 |  | 378.984 | 1.3789 | 378.64 | 371.57 | 0.1145 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 741.425 |  | 739.7445 | 0.2272 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1592.8 |  | 1578.1475 | 0.9285 | 1586.01 | 1565.95 | 0.1074 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 334.18 |  | 331.3137 | 0.8651 | 330.21 | 324.97 | 0.0209 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 140.88 |  | 138.9397 | 1.3965 | 139.755 | 137.31 | 0.0852 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 293.37 |  | 292.4596 | 0.3113 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1821 | 4.1023 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |
| 11 | ANET | ai_networking_optical | 169.145 |  | 165.2183 | 2.3766 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 387.465 |  | 381.5922 | 1.539 | 384.565 | 377.43 | 3.4764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | KLAC | semiconductor_equipment | 195.3 |  | 191.0467 | 2.2263 | 194.96 | 189.48 | 0.7578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 120.97 |  | 118.8616 | 1.7738 | 117.17 | 115.25 | 1.645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 321.1 |  | 309.7671 | 3.6585 | 315.21 | 304.11 | 1.5353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MU | memory_hbm_storage | 826.68 |  | 816.1662 | 1.2882 | 846.4 | 813.91 | 0.0605 | watch_only | none |
| 17 | SOXX | semiconductor_index | 496.65 |  | 490.1991 | 1.316 | 497.64 | 485.42 | 0.0524 | watch_only | none |
| 18 | QQQ | market_regime | 677.22 |  | 674.3208 | 0.4299 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| 19 | VRT | data_center_power_cooling | 269.07 |  | 266.2598 | 1.0554 | 273.86 | 266.04 | 0.1672 | watch_only | none |
| 20 | WDC | memory_hbm_storage | 460.6 |  | 441.5843 | 4.3063 | 465.04 | 435.22 | 0.1954 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.22 |  | 674.3208 | 0.4299 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| TQQQ | leveraged_tool | 61.98 |  | 61.1585 | 1.3433 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.72 |  | 196.1932 | 0.7782 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.81 |  | 396.2937 | -0.8791 | 400.09 | 392.355 | 0.3997 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 339.21 |  | 338.9852 | 0.0663 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.18 |  | 331.3137 | 0.8651 | 330.21 | 324.97 | 0.0209 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 463.315 |  | 455.8518 | 1.6372 | 472.485 | 453.76 | 4.1613 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.12 |  | 388.4296 | 1.465 | 390.46 | 382.495 | 0.0812 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 496.65 |  | 490.1991 | 1.316 | 497.64 | 485.42 | 0.0524 | watch_only | none |
| SMH | semiconductor_index | 533.6 |  | 527.6619 | 1.1254 | 533.01 | 523.325 | 0.0431 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 384.21 |  | 378.984 | 1.3789 | 378.64 | 371.57 | 0.1145 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 826.68 |  | 816.1662 | 1.2882 | 846.4 | 813.91 | 0.0605 | watch_only | none |
| MRVL | custom_silicon_networking | 176.74 |  | 174.2979 | 1.4011 | 181.24 | 172.395 | 5.0187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 392.12 |  | 376.1208 | 4.2537 | 402 | 374.02 | 2.1167 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.18 |  | 44.5768 | 1.3531 | 46.19 | 44.33 | 0.0664 | watch_only | none |
| SMCI | ai_server_oem | 28.5 |  | 28.0259 | 1.6917 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 741.425 |  | 739.7445 | 0.2272 | 739.42 | 736.57 | 0.0067 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.37 |  | 292.4596 | 0.3113 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.97 |  | 118.8616 | 1.7738 | 117.17 | 115.25 | 1.645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.945 |  | 66.283 | 0.9987 | 68.995 | 65.635 | 2.9875 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.07 |  | 266.2598 | 1.0554 | 273.86 | 266.04 | 0.1672 | watch_only | none |
| ETN | data_center_power_cooling | 387.465 |  | 381.5922 | 1.539 | 384.565 | 377.43 | 3.4764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 591.49 |  | 583.0194 | 1.4529 | 603.25 | 584.69 | 4.5749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 940.04 |  | 937.5186 | 0.2689 | 955.825 | 935.665 | 0.3979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.66 |  | 465.7816 | 0.618 | 477.73 | 460.77 | 5.0186 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.88 |  | 138.9397 | 1.3965 | 139.755 | 137.31 | 0.0852 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169.145 |  | 165.2183 | 2.3766 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 244.54 |  | 238.1124 | 2.6994 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 655.53 |  | 633.149 | 3.5349 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 347.88 |  | 337.7944 | 2.9857 | 354.09 | 338.14 | 4.1566 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.65 |  | 85.9926 | 3.0903 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 264.36 |  | 259.4969 | 1.8741 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1592.8 |  | 1578.1475 | 0.9285 | 1586.01 | 1565.95 | 0.1074 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 481.155 |  | 476.7273 | 0.9288 | 494.87 | 477.03 | 0.6879 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 273.77 |  | 267.1362 | 2.4833 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 195.3 |  | 191.0467 | 2.2263 | 194.96 | 189.48 | 0.7578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 321.1 |  | 309.7671 | 3.6585 | 315.21 | 304.11 | 1.5353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 242.07 |  | 237.1877 | 2.0584 | 248.8 | 236.42 | 0.9088 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.21 |  | 46.6637 | -0.9722 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.83 |  | 42.4648 | 0.86 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.89 |  | 119.1993 | 0.5795 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 287.68 |  | 282.5446 | 1.8176 | 296.8 | 283.22 | 4.9326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.79 |  | 517.9217 | -0.6047 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.83 |  | 295.7201 | -0.301 | 297.25 | 293.555 | 0.0814 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.88 |  | 26.52 | 1.3576 | 27 | 25.42 | 0.1488 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.07 |  | 33.707 | 1.0768 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 21.01 |  | 20.1821 | 4.1023 | 20.97 | 19.755 | 0.0476 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1116.195 |  | 1100.4382 | 1.4319 | 1185.19 | 1114.57 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 460.6 |  | 441.5843 | 4.3063 | 465.04 | 435.22 | 0.1954 | watch_only | none |
| STX | memory_hbm_storage | 749.82 |  | 733.7455 | 2.1907 | 774.805 | 719.02 | 0.9829 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.86 |  | 230.5465 | 0.136 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| META | cloud_ai_capex | 593.49 |  | 593.8468 | -0.0601 | 600.765 | 594.21 | 1.1239 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 247.595 |  | 245.2821 | 0.943 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.635 |  | 131.5366 | 0.8351 | 136.45 | 131.735 | 1.44 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
