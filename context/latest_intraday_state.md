# Intraday State

- Generated at: `2026-07-29T01:14:13+08:00`
- Market time ET: `2026-07-28T13:14:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 18, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.97 |  | 673.7967 | 0.471 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| SOXX | semiconductor_index | 492.72 |  | 489.8136 | 0.5934 | 497.64 | 485.42 | 0.0568 | watch_only | none |
| SMH | semiconductor_index | 530.61 |  | 527.1686 | 0.6528 | 533.01 | 523.325 | 0.0735 | watch_only | none |
| SPY | market_regime | 741.26 |  | 739.2521 | 0.2716 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.68 |  | 195.8426 | 0.9382 | 195.4 | 193.65 | 0.0051 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 381.17 |  | 378.3469 | 0.7462 | 378.64 | 371.57 | 0.0761 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.26 |  | 739.2521 | 0.2716 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.22 |  | 329.7434 | 1.3576 | 330.21 | 324.97 | 0.0479 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.26 |  | 739.2521 | 0.2716 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 381.17 |  | 378.3469 | 0.7462 | 378.64 | 371.57 | 0.0761 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 293.03 |  | 292.2098 | 0.2807 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.11 |  | 338.8667 | 0.0718 | 342.87 | 337.78 | 0.0177 | watch_only | none |
| 5 | KLAC | semiconductor_equipment | 191.15 |  | 190.6387 | 0.2682 | 194.96 | 189.48 | 0.1988 | watch_only | none |
| 6 | SMH | semiconductor_index | 530.61 |  | 527.1686 | 0.6528 | 533.01 | 523.325 | 0.0735 | watch_only | none |
| 7 | SOXX | semiconductor_index | 492.72 |  | 489.8136 | 0.5934 | 497.64 | 485.42 | 0.0568 | watch_only | none |
| 8 | QQQ | market_regime | 676.97 |  | 673.7967 | 0.471 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 231.87 |  | 230.2729 | 0.6936 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 397.865 |  | 396.1169 | 0.4413 | 400.09 | 392.355 | 0.2488 | watch_only | none |
| 11 | NVDA | ai_accelerator | 197.68 |  | 195.8426 | 0.9382 | 195.4 | 193.65 | 0.0051 | buy_precheck_manual_confirm | none |
| 12 | GOOGL | cloud_ai_capex | 334.22 |  | 329.7434 | 1.3576 | 330.21 | 324.97 | 0.0479 | buy_precheck_manual_confirm | none |
| 13 | ASML | semiconductor_equipment | 1580.61 |  | 1576.8719 | 0.2371 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ARM | ai_accelerator | 245.93 |  | 245.3088 | 0.2532 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | IREN | high_beta_ai_infrastructure | 33.99 |  | 33.7065 | 0.8412 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.28 |  | 20.0133 | 1.3326 | 20.97 | 19.755 | 0.0493 | watch_only | none |
| 17 | TER | semiconductor_test_packaging | 311.44 |  | 308.039 | 1.1041 | 315.21 | 304.11 | 0.2569 | watch_only | none |
| 18 | MRVL | custom_silicon_networking | 176.285 |  | 173.9527 | 1.3408 | 181.24 | 172.395 | 0.3233 | watch_only | none |
| 19 | ONTO | semiconductor_test_packaging | 236.92 |  | 236.5328 | 0.1637 | 248.8 | 236.42 | 0.4094 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 456.65 |  | 437.7088 | 4.3274 | 465.04 | 435.22 | 0.1073 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.68 |  | 195.8426 | 0.9382 | 195.4 | 193.65 | 0.0051 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 381.17 |  | 378.3469 | 0.7462 | 378.64 | 371.57 | 0.0761 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.26 |  | 739.2521 | 0.2716 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.22 |  | 329.7434 | 1.3576 | 330.21 | 324.97 | 0.0479 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 391.59 |  | 387.2297 | 1.126 | 390.46 | 382.495 | 2.6558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.41 |  | 164.0187 | 2.0676 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ORCL | cloud_ai_capex | 120.68 |  | 117.9436 | 2.3201 | 117.17 | 115.25 | 1.1269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SMH | semiconductor_index | 530.61 |  | 527.1686 | 0.6528 | 533.01 | 523.325 | 0.0735 | watch_only | none |
| 9 | SOXX | semiconductor_index | 492.72 |  | 489.8136 | 0.5934 | 497.64 | 485.42 | 0.0568 | watch_only | none |
| 10 | QQQ | market_regime | 676.97 |  | 673.7967 | 0.471 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| 11 | STX | memory_hbm_storage | 754.5 |  | 727.1294 | 3.7642 | 774.805 | 719.02 | 0.2876 | watch_only | none |
| 12 | WDC | memory_hbm_storage | 456.65 |  | 437.7088 | 4.3274 | 465.04 | 435.22 | 0.1073 | watch_only | none |
| 13 | IWM | market_regime | 293.03 |  | 292.2098 | 0.2807 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| 14 | KLAC | semiconductor_equipment | 191.15 |  | 190.6387 | 0.2682 | 194.96 | 189.48 | 0.1988 | watch_only | none |
| 15 | LITE | ai_networking_optical | 647.33 |  | 630.2966 | 2.7025 | 673.65 | 624.91 | 0.1236 | watch_only | none |
| 16 | TER | semiconductor_test_packaging | 311.44 |  | 308.039 | 1.1041 | 315.21 | 304.11 | 0.2569 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 397.865 |  | 396.1169 | 0.4413 | 400.09 | 392.355 | 0.2488 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.87 |  | 230.2729 | 0.6936 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 19 | MRVL | custom_silicon_networking | 176.285 |  | 173.9527 | 1.3408 | 181.24 | 172.395 | 0.3233 | watch_only | none |
| 20 | SMCI | ai_server_oem | 28.4 |  | 27.9388 | 1.6508 | 28.86 | 27.59 | 0.0704 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.97 |  | 673.7967 | 0.471 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| TQQQ | leveraged_tool | 61.99 |  | 61.0071 | 1.611 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.68 |  | 195.8426 | 0.9382 | 195.4 | 193.65 | 0.0051 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.865 |  | 396.1169 | 0.4413 | 400.09 | 392.355 | 0.2488 | watch_only | none |
| AAPL | mega_cap_platform | 339.11 |  | 338.8667 | 0.0718 | 342.87 | 337.78 | 0.0177 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.22 |  | 329.7434 | 1.3576 | 330.21 | 324.97 | 0.0479 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.19 |  | 455.2542 | 0.6449 | 472.485 | 453.76 | 3.0359 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.59 |  | 387.2297 | 1.126 | 390.46 | 382.495 | 2.6558 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 492.72 |  | 489.8136 | 0.5934 | 497.64 | 485.42 | 0.0568 | watch_only | none |
| SMH | semiconductor_index | 530.61 |  | 527.1686 | 0.6528 | 533.01 | 523.325 | 0.0735 | watch_only | none |
| AVGO | custom_silicon_networking | 381.17 |  | 378.3469 | 0.7462 | 378.64 | 371.57 | 0.0761 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.49 |  | 814.9496 | 0.5571 | 846.4 | 813.91 | 0.41 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.285 |  | 173.9527 | 1.3408 | 181.24 | 172.395 | 0.3233 | watch_only | none |
| DELL | ai_server_oem | 382.865 |  | 374.4001 | 2.2609 | 402 | 374.02 | 0.3604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.425 |  | 44.4498 | -0.0558 | 46.19 | 44.33 | 0.09 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.4 |  | 27.9388 | 1.6508 | 28.86 | 27.59 | 0.0704 | watch_only | none |
| SPY | market_regime | 741.26 |  | 739.2521 | 0.2716 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.03 |  | 292.2098 | 0.2807 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| ORCL | cloud_ai_capex | 120.68 |  | 117.9436 | 2.3201 | 117.17 | 115.25 | 1.1269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67.66 |  | 66.2054 | 2.1971 | 68.995 | 65.635 | 0.0887 | watch_only | none |
| VRT | data_center_power_cooling | 267.3 |  | 266.2665 | 0.3881 | 273.86 | 266.04 | 1.0213 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 383.78 |  | 380.3615 | 0.8988 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.21 |  | 581.7252 | 0.5991 | 603.25 | 584.69 | 1.9207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 944.785 |  | 937.2458 | 0.8044 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 467.155 |  | 464.9452 | 0.4753 | 477.73 | 460.77 | 4.917 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 139.245 |  | 138.3269 | 0.6637 | 139.755 | 137.31 | 1.9103 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.41 |  | 164.0187 | 2.0676 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.73 |  | 236.6472 | 1.7253 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 647.33 |  | 630.2966 | 2.7025 | 673.65 | 624.91 | 0.1236 | watch_only | none |
| CIEN | ai_networking_optical | 343.24 |  | 337.0181 | 1.8462 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.91 |  | 85.6092 | 2.6876 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.885 |  | 258.705 | 1.2292 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1580.61 |  | 1576.8719 | 0.2371 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.38 |  | 476.9891 | -0.3373 | 494.87 | 477.03 | 2.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 269.07 |  | 266.2062 | 1.0758 | 276.85 | 267.14 | 4.0621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.15 |  | 190.6387 | 0.2682 | 194.96 | 189.48 | 0.1988 | watch_only | none |
| TER | semiconductor_test_packaging | 311.44 |  | 308.039 | 1.1041 | 315.21 | 304.11 | 0.2569 | watch_only | none |
| ONTO | semiconductor_test_packaging | 236.92 |  | 236.5328 | 0.1637 | 248.8 | 236.42 | 0.4094 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.87 |  | 46.8145 | -2.0176 | 51.64 | 47.435 | 1.8531 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.17 |  | 42.5087 | -0.7968 | 44.155 | 41.78 | 0.498 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 118.92 |  | 119.4424 | -0.4374 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 283.5 |  | 282.3352 | 0.4126 | 296.8 | 283.22 | 0.5714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 518.51 |  | 518.5616 | -0.01 | 518.6 | 511.495 | 4.3066 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.6 |  | 295.8733 | -0.0924 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.26 |  | 26.5392 | -1.0519 | 27 | 25.42 | 0.1142 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.99 |  | 33.7065 | 0.8412 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.28 |  | 20.0133 | 1.3326 | 20.97 | 19.755 | 0.0493 | watch_only | none |
| SNDK | memory_hbm_storage | 1090.14 |  | 1102.4489 | -1.1165 | 1185.19 | 1114.57 | 1.9007 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.65 |  | 437.7088 | 4.3274 | 465.04 | 435.22 | 0.1073 | watch_only | none |
| STX | memory_hbm_storage | 754.5 |  | 727.1294 | 3.7642 | 774.805 | 719.02 | 0.2876 | watch_only | none |
| AMZN | cloud_ai_capex | 231.87 |  | 230.2729 | 0.6936 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 592.76 |  | 593.8469 | -0.183 | 600.765 | 594.21 | 2.0244 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 245.93 |  | 245.3088 | 0.2532 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.17 |  | 131.6315 | 0.4091 | 136.45 | 131.735 | 0.7263 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
