# Intraday State

- Generated at: `2026-07-29T02:34:44+08:00`
- Market time ET: `2026-07-28T14:34:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1, 'below_vwap': 8, 'below_opening_15m_low': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.345 |  | 674.108 | 0.3318 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.59 |  | 489.9654 | 0.3316 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| SMH | semiconductor_index | 529.55 |  | 527.3379 | 0.4195 | 533.01 | 523.325 | 0.0321 | watch_only | none |
| SPY | market_regime | 740.86 |  | 739.5167 | 0.1816 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.02 |  | 196.0439 | 0.4979 | 195.4 | 193.65 | 0.2386 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.11 |  | 378.5786 | 0.4045 | 378.64 | 371.57 | 0.0658 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.86 |  | 739.5167 | 0.1816 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.83 |  | 330.695 | 1.2504 | 330.21 | 324.97 | 0.0329 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.565 |  | 118.4643 | 1.7733 | 117.17 | 115.25 | 0.3152 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.86 |  | 739.5167 | 0.1816 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.11 |  | 378.5786 | 0.4045 | 378.64 | 371.57 | 0.0658 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 491.59 |  | 489.9654 | 0.3316 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| 4 | QQQ | market_regime | 676.345 |  | 674.108 | 0.3318 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 5 | IWM | market_regime | 292.86 |  | 292.3579 | 0.1717 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 6 | MSFT | cloud_ai_capex | 397.46 |  | 396.3549 | 0.2788 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 339.395 |  | 338.9619 | 0.1278 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 8 | KLAC | semiconductor_equipment | 191.17 |  | 190.7604 | 0.2147 | 194.96 | 189.48 | 0.1831 | watch_only | none |
| 9 | NVDA | ai_accelerator | 197.02 |  | 196.0439 | 0.4979 | 195.4 | 193.65 | 0.2386 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 231.12 |  | 230.4753 | 0.2797 | 233.05 | 229.7 | 0.1558 | watch_only | none |
| 11 | HPE | ai_server_oem | 44.48 |  | 44.4395 | 0.0912 | 46.19 | 44.33 | 0.2473 | watch_only | none |
| 12 | MU | memory_hbm_storage | 819.92 |  | 815.3269 | 0.5633 | 846.4 | 813.91 | 0.0781 | watch_only | none |
| 13 | SMH | semiconductor_index | 529.55 |  | 527.3379 | 0.4195 | 533.01 | 523.325 | 0.0321 | watch_only | none |
| 14 | GOOGL | cloud_ai_capex | 334.83 |  | 330.695 | 1.2504 | 330.21 | 324.97 | 0.0329 | buy_precheck_manual_confirm | none |
| 15 | JCI | data_center_power_cooling | 139.7 |  | 138.5124 | 0.8574 | 139.755 | 137.31 | 0.0787 | watch_only | none |
| 16 | SMCI | ai_server_oem | 28.27 |  | 27.9968 | 0.9758 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 17 | ASML | semiconductor_equipment | 1583.935 |  | 1577.247 | 0.424 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TT | data_center_power_cooling | 466.435 |  | 465.1736 | 0.2712 | 477.73 | 460.77 | 4.9482 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | GEV | data_center_power_cooling | 937.87 |  | 937.547 | 0.0345 | 955.825 | 935.665 | 0.7688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 456.89 |  | 455.5279 | 0.299 | 472.485 | 453.76 | 2.7096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.02 |  | 196.0439 | 0.4979 | 195.4 | 193.65 | 0.2386 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.11 |  | 378.5786 | 0.4045 | 378.64 | 371.57 | 0.0658 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.86 |  | 739.5167 | 0.1816 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.83 |  | 330.695 | 1.2504 | 330.21 | 324.97 | 0.0329 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.565 |  | 118.4643 | 1.7733 | 117.17 | 115.25 | 0.3152 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 391.8 |  | 387.6712 | 1.065 | 390.46 | 382.495 | 1.608 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 168.005 |  | 164.7138 | 1.9981 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ETN | data_center_power_cooling | 384.85 |  | 381.1682 | 0.9659 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | MU | memory_hbm_storage | 819.92 |  | 815.3269 | 0.5633 | 846.4 | 813.91 | 0.0781 | watch_only | none |
| 10 | SMH | semiconductor_index | 529.55 |  | 527.3379 | 0.4195 | 533.01 | 523.325 | 0.0321 | watch_only | none |
| 11 | SOXX | semiconductor_index | 491.59 |  | 489.9654 | 0.3316 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| 12 | QQQ | market_regime | 676.345 |  | 674.108 | 0.3318 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 13 | JCI | data_center_power_cooling | 139.7 |  | 138.5124 | 0.8574 | 139.755 | 137.31 | 0.0787 | watch_only | none |
| 14 | IWM | market_regime | 292.86 |  | 292.3579 | 0.1717 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 191.17 |  | 190.7604 | 0.2147 | 194.96 | 189.48 | 0.1831 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 397.46 |  | 396.3549 | 0.2788 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.12 |  | 230.4753 | 0.2797 | 233.05 | 229.7 | 0.1558 | watch_only | none |
| 18 | HPE | ai_server_oem | 44.48 |  | 44.4395 | 0.0912 | 46.19 | 44.33 | 0.2473 | watch_only | none |
| 19 | SMCI | ai_server_oem | 28.27 |  | 27.9968 | 0.9758 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.395 |  | 338.9619 | 0.1278 | 342.87 | 337.78 | 0.0147 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.345 |  | 674.108 | 0.3318 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.73 |  | 61.1015 | 1.0286 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.02 |  | 196.0439 | 0.4979 | 195.4 | 193.65 | 0.2386 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.46 |  | 396.3549 | 0.2788 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| AAPL | mega_cap_platform | 339.395 |  | 338.9619 | 0.1278 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.83 |  | 330.695 | 1.2504 | 330.21 | 324.97 | 0.0329 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.89 |  | 455.5279 | 0.299 | 472.485 | 453.76 | 2.7096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.8 |  | 387.6712 | 1.065 | 390.46 | 382.495 | 1.608 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.59 |  | 489.9654 | 0.3316 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| SMH | semiconductor_index | 529.55 |  | 527.3379 | 0.4195 | 533.01 | 523.325 | 0.0321 | watch_only | none |
| AVGO | custom_silicon_networking | 380.11 |  | 378.5786 | 0.4045 | 378.64 | 371.57 | 0.0658 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.92 |  | 815.3269 | 0.5633 | 846.4 | 813.91 | 0.0781 | watch_only | none |
| MRVL | custom_silicon_networking | 175.45 |  | 174.185 | 0.7262 | 181.24 | 172.395 | 0.8435 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 384.965 |  | 375.0298 | 2.6492 | 402 | 374.02 | 3.7432 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.48 |  | 44.4395 | 0.0912 | 46.19 | 44.33 | 0.2473 | watch_only | none |
| SMCI | ai_server_oem | 28.27 |  | 27.9968 | 0.9758 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 740.86 |  | 739.5167 | 0.1816 | 739.42 | 736.57 | 0.0297 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.86 |  | 292.3579 | 0.1717 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.565 |  | 118.4643 | 1.7733 | 117.17 | 115.25 | 0.3152 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.36 |  | 66.2548 | 0.1588 | 68.995 | 65.635 | 2.1851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.19 |  | 266.1436 | -0.3583 | 273.86 | 266.04 | 0.4374 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 384.85 |  | 381.1682 | 0.9659 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.12 |  | 582.245 | 0.4938 | 603.25 | 584.69 | 1.9346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 937.87 |  | 937.547 | 0.0345 | 955.825 | 935.665 | 0.7688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.435 |  | 465.1736 | 0.2712 | 477.73 | 460.77 | 4.9482 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.7 |  | 138.5124 | 0.8574 | 139.755 | 137.31 | 0.0787 | watch_only | none |
| ANET | ai_networking_optical | 168.005 |  | 164.7138 | 1.9981 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.8 |  | 237.3381 | 1.4586 | 256.145 | 236.73 | 4.593 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 642.37 |  | 631.9254 | 1.6528 | 673.65 | 624.91 | 4.3106 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 339.83 |  | 337.3964 | 0.7213 | 354.09 | 338.14 | 0.5356 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.18 |  | 85.797 | 1.612 | 92.95 | 84.63 | 4.2785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 260.27 |  | 259.064 | 0.4655 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1583.935 |  | 1577.247 | 0.424 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.685 |  | 476.3775 | -0.1454 | 494.87 | 477.03 | 1.7322 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 271.15 |  | 266.6195 | 1.6993 | 276.85 | 267.14 | 4.4256 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.17 |  | 190.7604 | 0.2147 | 194.96 | 189.48 | 0.1831 | watch_only | none |
| TER | semiconductor_test_packaging | 312.01 |  | 308.4378 | 1.1581 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 238.69 |  | 236.7378 | 0.8246 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.61 |  | 46.7205 | -2.3769 | 51.64 | 47.435 | 1.2717 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.06 |  | 42.4546 | -0.9295 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.69 |  | 119.191 | -0.4204 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 282.13 |  | 282.3705 | -0.0852 | 296.8 | 283.22 | 0.3899 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 513.755 |  | 518.2321 | -0.8639 | 518.6 | 511.495 | 5.0394 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.81 |  | 295.7722 | -0.3253 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.47 |  | 26.5171 | -0.1777 | 27 | 25.42 | 0.0756 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.525 |  | 33.7123 | -0.5556 | 35.08 | 33.52 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.47 |  | 20.0553 | 2.0679 | 20.97 | 19.755 | 0.0489 | watch_only | none |
| SNDK | memory_hbm_storage | 1081.455 |  | 1100.1745 | -1.7015 | 1185.19 | 1114.57 | 1.9973 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.88 |  | 439.6546 | 3.9179 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 752.03 |  | 731.2619 | 2.84 | 774.805 | 719.02 | 4.3602 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.12 |  | 230.4753 | 0.2797 | 233.05 | 229.7 | 0.1558 | watch_only | none |
| META | cloud_ai_capex | 593.74 |  | 593.8474 | -0.0181 | 600.765 | 594.21 | 1.0863 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.52 |  | 245.2387 | -0.2931 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.94 |  | 131.5762 | -1.2435 | 136.45 | 131.735 | 3.8864 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
