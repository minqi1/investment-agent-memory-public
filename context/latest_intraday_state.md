# Intraday State

- Generated at: `2026-07-28T23:57:10+08:00`
- Market time ET: `2026-07-28T11:57:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'watch_only': 14, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_vwap': 4, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.48 |  | 673.0648 | 0.8046 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 495.92 |  | 489.1912 | 1.3755 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| SMH | semiconductor_index | 533.93 |  | 526.6683 | 1.3788 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.11 |  | 738.6383 | 0.47 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.22 |  | 195.3495 | 1.4694 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 533.93 |  | 526.6683 | 1.3788 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 383.74 |  | 377.4594 | 1.6639 | 378.64 | 371.57 | 0.0573 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 742.11 |  | 738.6383 | 0.47 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 678.48 |  | 673.0648 | 0.8046 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1592.39 |  | 1574.5767 | 1.1313 | 1586.01 | 1565.95 | 0.1344 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.4 |  | 328.7514 | 1.414 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 293.37 |  | 292.0028 | 0.4682 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 119.9 |  | 117.1291 | 2.3657 | 117.17 | 115.25 | 0.0751 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 27.02 |  | 26.484 | 2.024 | 27 | 25.42 | 0.111 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 62.33 |  | 60.7486 | 2.6033 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 293.37 |  | 292.0028 | 0.4682 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 742.11 |  | 738.6383 | 0.47 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 339.75 |  | 338.6264 | 0.3318 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 4 | SMH | semiconductor_index | 533.93 |  | 526.6683 | 1.3788 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 678.48 |  | 673.0648 | 0.8046 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 397.635 |  | 395.7343 | 0.4803 | 400.09 | 392.355 | 0.0654 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 231.305 |  | 229.9731 | 0.5792 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 8 | ASML | semiconductor_equipment | 1592.39 |  | 1574.5767 | 1.1313 | 1586.01 | 1565.95 | 0.1344 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 198.22 |  | 195.3495 | 1.4694 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 10 | GOOGL | cloud_ai_capex | 333.4 |  | 328.7514 | 1.414 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| 11 | SOXX | semiconductor_index | 495.92 |  | 489.1912 | 1.3755 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| 12 | ONTO | semiconductor_test_packaging | 237.16 |  | 236.4315 | 0.3081 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 192.74 |  | 190.2662 | 1.3002 | 194.96 | 189.48 | 0.0934 | watch_only | none |
| 14 | APLD | high_beta_ai_infrastructure | 27.02 |  | 26.484 | 2.024 | 27 | 25.42 | 0.111 | buy_precheck_manual_confirm | none |
| 15 | PWR | data_center_power_cooling | 586.91 |  | 579.8185 | 1.2231 | 603.25 | 584.69 | 0.3425 | watch_only | none |
| 16 | JCI | data_center_power_cooling | 139.3 |  | 138.0199 | 0.9275 | 139.755 | 137.31 | 0.2584 | watch_only | none |
| 17 | AVGO | custom_silicon_networking | 383.74 |  | 377.4594 | 1.6639 | 378.64 | 371.57 | 0.0573 | buy_precheck_manual_confirm | none |
| 18 | TT | data_center_power_cooling | 468.085 |  | 464.4752 | 0.7772 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ARM | ai_accelerator | 246.685 |  | 244.9759 | 0.6977 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | META | cloud_ai_capex | 594.6 |  | 593.2483 | 0.2278 | 600.765 | 594.21 | 0.3633 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.22 |  | 195.3495 | 1.4694 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 533.93 |  | 526.6683 | 1.3788 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 383.74 |  | 377.4594 | 1.6639 | 378.64 | 371.57 | 0.0573 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 742.11 |  | 738.6383 | 0.47 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 678.48 |  | 673.0648 | 0.8046 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1592.39 |  | 1574.5767 | 1.1313 | 1586.01 | 1565.95 | 0.1344 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.4 |  | 328.7514 | 1.414 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 293.37 |  | 292.0028 | 0.4682 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 119.9 |  | 117.1291 | 2.3657 | 117.17 | 115.25 | 0.0751 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 27.02 |  | 26.484 | 2.024 | 27 | 25.42 | 0.111 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 62.33 |  | 60.7486 | 2.6033 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| 12 | TSM | foundry | 392.28 |  | 386.2096 | 1.5718 | 390.46 | 382.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ANET | ai_networking_optical | 167.17 |  | 163.3827 | 2.318 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ETN | data_center_power_cooling | 386.345 |  | 379.3736 | 1.8376 | 384.565 | 377.43 | 2.9896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SOXX | semiconductor_index | 495.92 |  | 489.1912 | 1.3755 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| 16 | PWR | data_center_power_cooling | 586.91 |  | 579.8185 | 1.2231 | 603.25 | 584.69 | 0.3425 | watch_only | none |
| 17 | JCI | data_center_power_cooling | 139.3 |  | 138.0199 | 0.9275 | 139.755 | 137.31 | 0.2584 | watch_only | none |
| 18 | WDC | memory_hbm_storage | 449.97 |  | 435.0833 | 3.4216 | 465.04 | 435.22 | 0.3022 | watch_only | none |
| 19 | AMD | ai_accelerator | 464.455 |  | 454.0159 | 2.2993 | 472.485 | 453.76 | 0.2691 | watch_only | none |
| 20 | KLAC | semiconductor_equipment | 192.74 |  | 190.2662 | 1.3002 | 194.96 | 189.48 | 0.0934 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.48 |  | 673.0648 | 0.8046 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.33 |  | 60.7486 | 2.6033 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 198.22 |  | 195.3495 | 1.4694 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.635 |  | 395.7343 | 0.4803 | 400.09 | 392.355 | 0.0654 | watch_only | none |
| AAPL | mega_cap_platform | 339.75 |  | 338.6264 | 0.3318 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.4 |  | 328.7514 | 1.414 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 464.455 |  | 454.0159 | 2.2993 | 472.485 | 453.76 | 0.2691 | watch_only | none |
| TSM | foundry | 392.28 |  | 386.2096 | 1.5718 | 390.46 | 382.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.92 |  | 489.1912 | 1.3755 | 497.64 | 485.42 | 0.0948 | watch_only | none |
| SMH | semiconductor_index | 533.93 |  | 526.6683 | 1.3788 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 383.74 |  | 377.4594 | 1.6639 | 378.64 | 371.57 | 0.0573 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 826.82 |  | 813.1689 | 1.6788 | 846.4 | 813.91 | 1.4284 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 178.49 |  | 173.2872 | 3.0024 | 181.24 | 172.395 | 2.6332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 385.93 |  | 373.0314 | 3.4578 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.03 |  | 44.3547 | 1.5225 | 46.19 | 44.33 | 0.1555 | watch_only | none |
| SMCI | ai_server_oem | 28.48 |  | 27.8383 | 2.3049 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 742.11 |  | 738.6383 | 0.47 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.37 |  | 292.0028 | 0.4682 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 119.9 |  | 117.1291 | 2.3657 | 117.17 | 115.25 | 0.0751 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.165 |  | 65.9824 | 1.7922 | 68.995 | 65.635 | 3.3053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.66 |  | 265.9161 | 1.0319 | 273.86 | 266.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 386.345 |  | 379.3736 | 1.8376 | 384.565 | 377.43 | 2.9896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 586.91 |  | 579.8185 | 1.2231 | 603.25 | 584.69 | 0.3425 | watch_only | none |
| GEV | data_center_power_cooling | 950.44 |  | 934.774 | 1.6759 | 955.825 | 935.665 | 0.5639 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.085 |  | 464.4752 | 0.7772 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.3 |  | 138.0199 | 0.9275 | 139.755 | 137.31 | 0.2584 | watch_only | none |
| ANET | ai_networking_optical | 167.17 |  | 163.3827 | 2.318 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.35 |  | 236.0025 | 1.8421 | 256.145 | 236.73 | 0.4285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 643.67 |  | 626.1336 | 2.8008 | 673.65 | 624.91 | 4.9093 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 342.79 |  | 336.1223 | 1.9837 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.01 |  | 85.2384 | 3.2516 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.21 |  | 257.568 | 2.967 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1592.39 |  | 1574.5767 | 1.1313 | 1586.01 | 1565.95 | 0.1344 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 480.275 |  | 477.0104 | 0.6844 | 494.87 | 477.03 | 0.8891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 268.795 |  | 265.7075 | 1.162 | 276.85 | 267.14 | 3.1623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 192.74 |  | 190.2662 | 1.3002 | 194.96 | 189.48 | 0.0934 | watch_only | none |
| TER | semiconductor_test_packaging | 313.72 |  | 306.5304 | 2.3455 | 315.21 | 304.11 | 0.1658 | watch_only | none |
| ONTO | semiconductor_test_packaging | 237.16 |  | 236.4315 | 0.3081 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.71 |  | 47.0565 | -0.7364 | 51.64 | 47.435 | 2.0124 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.525 |  | 42.5491 | -0.0566 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.87 |  | 119.4161 | 0.3801 | 121 | 117.72 | 4.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 284.74 |  | 281.6413 | 1.1002 | 296.8 | 283.22 | 1.1519 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 517.39 |  | 518.5469 | -0.2231 | 518.6 | 511.495 | 4.6232 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.1 |  | 296.0537 | -0.6599 | 297.25 | 293.555 | 0.1836 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 27.02 |  | 26.484 | 2.024 | 27 | 25.42 | 0.111 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.58 |  | 33.5504 | 3.0688 | 35.08 | 33.52 | 0.0578 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.39 |  | 19.9604 | 2.152 | 20.97 | 19.755 | 0.0981 | watch_only | none |
| SNDK | memory_hbm_storage | 1109.3 |  | 1102.2195 | 0.6424 | 1185.19 | 1114.57 | 1.3053 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 449.97 |  | 435.0833 | 3.4216 | 465.04 | 435.22 | 0.3022 | watch_only | none |
| STX | memory_hbm_storage | 741.78 |  | 723.8278 | 2.4802 | 774.805 | 719.02 | 1.6177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.305 |  | 229.9731 | 0.5792 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.6 |  | 593.2483 | 0.2278 | 600.765 | 594.21 | 0.3633 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 246.685 |  | 244.9759 | 0.6977 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.37 |  | 131.4258 | 1.4793 | 136.45 | 131.735 | 0.6223 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
