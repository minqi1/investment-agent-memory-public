# Intraday State

- Generated at: `2026-07-28T22:21:32+08:00`
- Market time ET: `2026-07-28T10:21:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'watch_only': 2, 'price_stale_or_missing': 1, 'below_vwap': 9, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 668.24 |  | 671.4186 | -0.4734 | 677.3 | 670.84 | 0.0329 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 481.18 |  | 488.8127 | -1.5615 | 497.64 | 485.42 | 0.1185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 518.8 |  | 525.4998 | -1.2749 | 533.01 | 523.325 | 0.0559 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.57 |  | 737.5307 | -0.1303 | 739.42 | 736.57 | 0.0489 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 327.35 |  | 326.9723 | 0.1155 | 330.21 | 324.97 | 0.0183 | watch_only | none |
| 2 | MSFT | cloud_ai_capex | 396.975 |  | 394.4653 | 0.6362 | 400.09 | 392.355 | 0.1134 | watch_only | none |
| 3 | APD | industrial_gases | 297.65 |  | 296.2978 | 0.4564 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 521.605 |  | 518.3831 | 0.6215 | 518.6 | 511.495 | 3.7289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SPY | market_regime | 736.57 |  | 737.5307 | -0.1303 | 739.42 | 736.57 | 0.0489 | below_vwap | below_vwap |
| 6 | META | cloud_ai_capex | 594.36 |  | 595.2482 | -0.1492 | 600.765 | 594.21 | 0.0925 | below_vwap | below_vwap |
| 7 | AMZN | cloud_ai_capex | 230.08 |  | 230.3636 | -0.1231 | 233.05 | 229.7 | 0.0522 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | TT | data_center_power_cooling | 462.38 |  | 464.564 | -0.4701 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ANET | ai_networking_optical | 160.98 |  | 161.6381 | -0.4071 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 118.58 |  | 119.4282 | -0.7102 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 373.8 |  | 375.2476 | -0.3858 | 378.64 | 371.57 | 1.0701 | below_vwap | below_vwap,spread_too_wide |
| 13 | APLD | high_beta_ai_infrastructure | 26.04 |  | 26.3433 | -1.1514 | 27 | 25.42 | 2.6114 | below_vwap | below_vwap,spread_too_wide |
| 14 | NVDA | ai_accelerator | 192.97 |  | 194.1048 | -0.5846 | 195.4 | 193.65 | 0.0207 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | MU | memory_hbm_storage | 790.57 |  | 813.8897 | -2.8652 | 846.4 | 813.91 | 0.1214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | SMH | semiconductor_index | 518.8 |  | 525.4998 | -1.2749 | 533.01 | 523.325 | 0.0559 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | SOXX | semiconductor_index | 481.18 |  | 488.8127 | -1.5615 | 497.64 | 485.42 | 0.1185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | QQQ | market_regime | 668.24 |  | 671.4186 | -0.4734 | 677.3 | 670.84 | 0.0329 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | IWM | market_regime | 290.825 |  | 291.8196 | -0.3408 | 293.26 | 291.55 | 0.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMCI | ai_server_oem | 27.24 |  | 27.673 | -1.5647 | 28.86 | 27.59 | 0.0734 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 521.605 |  | 518.3831 | 0.6215 | 518.6 | 511.495 | 3.7289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | APD | industrial_gases | 297.65 |  | 296.2978 | 0.4564 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | GOOGL | cloud_ai_capex | 327.35 |  | 326.9723 | 0.1155 | 330.21 | 324.97 | 0.0183 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 396.975 |  | 394.4653 | 0.6362 | 400.09 | 392.355 | 0.1134 | watch_only | none |
| 5 | AVGO | custom_silicon_networking | 373.8 |  | 375.2476 | -0.3858 | 378.64 | 371.57 | 1.0701 | below_vwap | below_vwap,spread_too_wide |
| 6 | SPY | market_regime | 736.57 |  | 737.5307 | -0.1303 | 739.42 | 736.57 | 0.0489 | below_vwap | below_vwap |
| 7 | TT | data_center_power_cooling | 462.38 |  | 464.564 | -0.4701 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | ANET | ai_networking_optical | 160.98 |  | 161.6381 | -0.4071 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | META | cloud_ai_capex | 594.36 |  | 595.2482 | -0.1492 | 600.765 | 594.21 | 0.0925 | below_vwap | below_vwap |
| 11 | AMZN | cloud_ai_capex | 230.08 |  | 230.3636 | -0.1231 | 233.05 | 229.7 | 0.0522 | below_vwap | below_vwap |
| 12 | ENTG | semiconductor_materials | 118.58 |  | 119.4282 | -0.7102 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | APLD | high_beta_ai_infrastructure | 26.04 |  | 26.3433 | -1.1514 | 27 | 25.42 | 2.6114 | below_vwap | below_vwap,spread_too_wide |
| 14 | NVDA | ai_accelerator | 192.97 |  | 194.1048 | -0.5846 | 195.4 | 193.65 | 0.0207 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | TSM | foundry | 381.73 |  | 385.1829 | -0.8964 | 390.46 | 382.495 | 1.1736 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 16 | MU | memory_hbm_storage | 790.57 |  | 813.8897 | -2.8652 | 846.4 | 813.91 | 0.1214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | SMH | semiconductor_index | 518.8 |  | 525.4998 | -1.2749 | 533.01 | 523.325 | 0.0559 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SOXX | semiconductor_index | 481.18 |  | 488.8127 | -1.5615 | 497.64 | 485.42 | 0.1185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | QQQ | market_regime | 668.24 |  | 671.4186 | -0.4734 | 677.3 | 670.84 | 0.0329 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | ASML | semiconductor_equipment | 1555.91 |  | 1571.142 | -0.9695 | 1586.01 | 1565.95 | 0.6421 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 668.24 |  | 671.4186 | -0.4734 | 677.3 | 670.84 | 0.0329 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 59.48 |  | 60.4341 | -1.5788 | 62.01 | 60.23 | 0.0168 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 192.97 |  | 194.1048 | -0.5846 | 195.4 | 193.65 | 0.0207 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 396.975 |  | 394.4653 | 0.6362 | 400.09 | 392.355 | 0.1134 | watch_only | none |
| AAPL | mega_cap_platform | 337.48 |  | 338.7736 | -0.3818 | 342.87 | 337.78 | 0.0119 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 327.35 |  | 326.9723 | 0.1155 | 330.21 | 324.97 | 0.0183 | watch_only | none |
| AMD | ai_accelerator | 443.36 |  | 455.346 | -2.6323 | 472.485 | 453.76 | 4.299 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 381.73 |  | 385.1829 | -0.8964 | 390.46 | 382.495 | 1.1736 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 481.18 |  | 488.8127 | -1.5615 | 497.64 | 485.42 | 0.1185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 518.8 |  | 525.4998 | -1.2749 | 533.01 | 523.325 | 0.0559 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 373.8 |  | 375.2476 | -0.3858 | 378.64 | 371.57 | 1.0701 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 790.57 |  | 813.8897 | -2.8652 | 846.4 | 813.91 | 0.1214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 167.49 |  | 172.9533 | -3.1588 | 181.24 | 172.395 | 0.806 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 363.1 |  | 370.8134 | -2.0801 | 402 | 374.02 | 3.9438 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.5 |  | 44.254 | -1.7037 | 46.19 | 44.33 | 0.1609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.24 |  | 27.673 | -1.5647 | 28.86 | 27.59 | 0.0734 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.57 |  | 737.5307 | -0.1303 | 739.42 | 736.57 | 0.0489 | below_vwap | below_vwap |
| IWM | market_regime | 290.825 |  | 291.8196 | -0.3408 | 293.26 | 291.55 | 0.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 114.92 |  | 115.7704 | -0.7346 | 117.17 | 115.25 | 4.8033 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 64.88 |  | 66.0363 | -1.751 | 68.995 | 65.635 | 3.545 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 259.945 |  | 267.1938 | -2.7129 | 273.86 | 266.04 | 1.5965 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 376.19 |  | 378.8723 | -0.708 | 384.565 | 377.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 572.8 |  | 580.952 | -1.4032 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 916.635 |  | 936.8378 | -2.1565 | 955.825 | 935.665 | 4.4096 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 462.38 |  | 464.564 | -0.4701 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 136.96 |  | 138.064 | -0.7996 | 139.755 | 137.31 | 4.8481 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 160.98 |  | 161.6381 | -0.4071 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 229.23 |  | 237.7964 | -3.6024 | 256.145 | 236.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 604.4 |  | 626.1324 | -3.4709 | 673.65 | 624.91 | 1.5354 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 331.9 |  | 338.8319 | -2.0458 | 354.09 | 338.14 | 4.9563 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 81.69 |  | 84.9939 | -3.8872 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 252.14 |  | 255.7818 | -1.4238 | 268.265 | 253.05 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1555.91 |  | 1571.142 | -0.9695 | 1586.01 | 1565.95 | 0.6421 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 467.72 |  | 478.8259 | -2.3194 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 259.84 |  | 266.6321 | -2.5474 | 276.85 | 267.14 | 4.4373 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 187.29 |  | 190.4152 | -1.6412 | 194.96 | 189.48 | 2.0343 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 302.74 |  | 305.3746 | -0.8627 | 315.21 | 304.11 | 1.2783 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 231.85 |  | 238.2177 | -2.6731 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.31 |  | 47.5107 | -4.6319 | 51.64 | 47.435 | 0.2207 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 41.765 |  | 42.9067 | -2.6609 | 44.155 | 41.78 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.58 |  | 119.4282 | -0.7102 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 278.57 |  | 283.8227 | -1.8507 | 296.8 | 283.22 | 0.4451 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 521.605 |  | 518.3831 | 0.6215 | 518.6 | 511.495 | 3.7289 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.65 |  | 296.2978 | 0.4564 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.04 |  | 26.3433 | -1.1514 | 27 | 25.42 | 2.6114 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 32.69 |  | 33.3177 | -1.8841 | 35.08 | 33.52 | 0.0306 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.7 |  | 20.0137 | -1.5676 | 20.97 | 19.755 | 0.1015 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1056.04 |  | 1108.8635 | -4.7638 | 1185.19 | 1114.57 | 4.5453 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 422.75 |  | 435.2937 | -2.8817 | 465.04 | 435.22 | 2.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 704.04 |  | 722.9669 | -2.618 | 774.805 | 719.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 230.08 |  | 230.3636 | -0.1231 | 233.05 | 229.7 | 0.0522 | below_vwap | below_vwap |
| META | cloud_ai_capex | 594.36 |  | 595.2482 | -0.1492 | 600.765 | 594.21 | 0.0925 | below_vwap | below_vwap |
| ARM | ai_accelerator | 241.45 |  | 245.085 | -1.4832 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 128.79 |  | 131.4066 | -1.9912 | 136.45 | 131.735 | 0.9628 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
