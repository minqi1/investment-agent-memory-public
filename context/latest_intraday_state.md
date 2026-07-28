# Intraday State

- Generated at: `2026-07-29T01:18:02+08:00`
- Market time ET: `2026-07-28T13:18:02-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 20, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_vwap': 6, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.24 |  | 673.8219 | 0.5073 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| SOXX | semiconductor_index | 493.08 |  | 489.823 | 0.6649 | 497.64 | 485.42 | 0.073 | watch_only | none |
| SMH | semiconductor_index | 531.06 |  | 527.1802 | 0.736 | 533.01 | 523.325 | 0.0433 | watch_only | none |
| SPY | market_regime | 741.35 |  | 739.2601 | 0.2827 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.85 |  | 195.8554 | 1.0184 | 195.4 | 193.65 | 0.1213 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.64 |  | 387.2463 | 1.1346 | 390.46 | 382.495 | 0.0613 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.35 |  | 739.2601 | 0.2827 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.46 |  | 329.7848 | 1.4177 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.54 |  | 117.95 | 2.1958 | 117.17 | 115.25 | 0.0747 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.35 |  | 739.2601 | 0.2827 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.09 |  | 292.2122 | 0.3004 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 339.08 |  | 338.8687 | 0.0624 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 4 | ARM | ai_accelerator | 246.16 |  | 245.3214 | 0.3419 | 253.38 | 243.72 | 0.1869 | watch_only | none |
| 5 | SMH | semiconductor_index | 531.06 |  | 527.1802 | 0.736 | 533.01 | 523.325 | 0.0433 | watch_only | none |
| 6 | SOXX | semiconductor_index | 493.08 |  | 489.823 | 0.6649 | 497.64 | 485.42 | 0.073 | watch_only | none |
| 7 | QQQ | market_regime | 677.24 |  | 673.8219 | 0.5073 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| 8 | TSM | foundry | 391.64 |  | 387.2463 | 1.1346 | 390.46 | 382.495 | 0.0613 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 467.33 |  | 464.9594 | 0.5098 | 477.73 | 460.77 | 0.1284 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 231.86 |  | 230.2813 | 0.6856 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 11 | MU | memory_hbm_storage | 819.24 |  | 814.9967 | 0.5206 | 846.4 | 813.91 | 0.21 | watch_only | none |
| 12 | GEV | data_center_power_cooling | 943.86 |  | 937.2931 | 0.7006 | 955.825 | 935.665 | 0.268 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 397.88 |  | 396.1224 | 0.4437 | 400.09 | 392.355 | 0.2815 | watch_only | none |
| 14 | MKSI | semiconductor_materials | 284.01 |  | 282.3406 | 0.5913 | 296.8 | 283.22 | 0.1831 | watch_only | none |
| 15 | NVDA | ai_accelerator | 197.85 |  | 195.8554 | 1.0184 | 195.4 | 193.65 | 0.1213 | buy_precheck_manual_confirm | none |
| 16 | GOOGL | cloud_ai_capex | 334.46 |  | 329.7848 | 1.4177 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| 17 | ONTO | semiconductor_test_packaging | 236.92 |  | 236.5328 | 0.1637 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | IREN | high_beta_ai_infrastructure | 34.11 |  | 33.7077 | 1.1936 | 35.08 | 33.52 | 0.0586 | watch_only | none |
| 19 | LIN | industrial_gases | 518.6 |  | 518.5612 | 0.0075 | 518.6 | 511.495 | 4.3232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1581.58 |  | 1576.8854 | 0.2977 | 1586.01 | 1565.95 | 1.281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.85 |  | 195.8554 | 1.0184 | 195.4 | 193.65 | 0.1213 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.64 |  | 387.2463 | 1.1346 | 390.46 | 382.495 | 0.0613 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.35 |  | 739.2601 | 0.2827 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.46 |  | 329.7848 | 1.4177 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.54 |  | 117.95 | 2.1958 | 117.17 | 115.25 | 0.0747 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 380.875 |  | 378.3618 | 0.6642 | 378.64 | 371.57 | 2.5546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 167.37 |  | 164.0363 | 2.0323 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | LIN | industrial_gases | 518.6 |  | 518.5612 | 0.0075 | 518.6 | 511.495 | 4.3232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MU | memory_hbm_storage | 819.24 |  | 814.9967 | 0.5206 | 846.4 | 813.91 | 0.21 | watch_only | none |
| 10 | SMH | semiconductor_index | 531.06 |  | 527.1802 | 0.736 | 533.01 | 523.325 | 0.0433 | watch_only | none |
| 11 | SOXX | semiconductor_index | 493.08 |  | 489.823 | 0.6649 | 497.64 | 485.42 | 0.073 | watch_only | none |
| 12 | QQQ | market_regime | 677.24 |  | 673.8219 | 0.5073 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| 13 | TT | data_center_power_cooling | 467.33 |  | 464.9594 | 0.5098 | 477.73 | 460.77 | 0.1284 | watch_only | none |
| 14 | GEV | data_center_power_cooling | 943.86 |  | 937.2931 | 0.7006 | 955.825 | 935.665 | 0.268 | watch_only | none |
| 15 | IWM | market_regime | 293.09 |  | 292.2122 | 0.3004 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 16 | LITE | ai_networking_optical | 646.14 |  | 630.4082 | 2.4955 | 673.65 | 624.91 | 0.099 | watch_only | none |
| 17 | ARM | ai_accelerator | 246.16 |  | 245.3214 | 0.3419 | 253.38 | 243.72 | 0.1869 | watch_only | none |
| 18 | TER | semiconductor_test_packaging | 311.52 |  | 308.0595 | 1.1233 | 315.21 | 304.11 | 0.3146 | watch_only | none |
| 19 | MSFT | cloud_ai_capex | 397.88 |  | 396.1224 | 0.4437 | 400.09 | 392.355 | 0.2815 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 231.86 |  | 230.2813 | 0.6856 | 233.05 | 229.7 | 0.0173 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.24 |  | 673.8219 | 0.5073 | 677.3 | 670.84 | 0.0266 | watch_only | none |
| TQQQ | leveraged_tool | 62 |  | 61.0124 | 1.6187 | 62.01 | 60.23 | 0.0323 | watch_only | none |
| NVDA | ai_accelerator | 197.85 |  | 195.8554 | 1.0184 | 195.4 | 193.65 | 0.1213 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.88 |  | 396.1224 | 0.4437 | 400.09 | 392.355 | 0.2815 | watch_only | none |
| AAPL | mega_cap_platform | 339.08 |  | 338.8687 | 0.0624 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.46 |  | 329.7848 | 1.4177 | 330.21 | 324.97 | 0.0299 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 457.88 |  | 455.2677 | 0.5738 | 472.485 | 453.76 | 2.8239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.64 |  | 387.2463 | 1.1346 | 390.46 | 382.495 | 0.0613 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.08 |  | 489.823 | 0.6649 | 497.64 | 485.42 | 0.073 | watch_only | none |
| SMH | semiconductor_index | 531.06 |  | 527.1802 | 0.736 | 533.01 | 523.325 | 0.0433 | watch_only | none |
| AVGO | custom_silicon_networking | 380.875 |  | 378.3618 | 0.6642 | 378.64 | 371.57 | 2.5546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 819.24 |  | 814.9967 | 0.5206 | 846.4 | 813.91 | 0.21 | watch_only | none |
| MRVL | custom_silicon_networking | 176.5 |  | 173.9597 | 1.4603 | 181.24 | 172.395 | 0.3399 | watch_only | none |
| DELL | ai_server_oem | 383.89 |  | 374.4209 | 2.529 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.44 |  | 44.4499 | -0.0222 | 46.19 | 44.33 | 0.045 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.455 |  | 27.9408 | 1.8403 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 741.35 |  | 739.2601 | 0.2827 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.09 |  | 292.2122 | 0.3004 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.54 |  | 117.95 | 2.1958 | 117.17 | 115.25 | 0.0747 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.61 |  | 66.2099 | 2.1146 | 68.995 | 65.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 267.27 |  | 266.27 | 0.3755 | 273.86 | 266.04 | 1.332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 383.81 |  | 380.3756 | 0.9029 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.08 |  | 581.7542 | 0.5717 | 603.25 | 584.69 | 1.8955 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 943.86 |  | 937.2931 | 0.7006 | 955.825 | 935.665 | 0.268 | watch_only | none |
| TT | data_center_power_cooling | 467.33 |  | 464.9594 | 0.5098 | 477.73 | 460.77 | 0.1284 | watch_only | none |
| JCI | data_center_power_cooling | 139.33 |  | 138.3305 | 0.7225 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.37 |  | 164.0363 | 2.0323 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 241.1 |  | 236.6603 | 1.876 | 256.145 | 236.73 | 0.112 | watch_only | none |
| LITE | ai_networking_optical | 646.14 |  | 630.4082 | 2.4955 | 673.65 | 624.91 | 0.099 | watch_only | none |
| CIEN | ai_networking_optical | 343.36 |  | 337.0373 | 1.876 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.775 |  | 85.6115 | 2.5271 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.885 |  | 258.705 | 1.2292 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1581.58 |  | 1576.8854 | 0.2977 | 1586.01 | 1565.95 | 1.281 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 475.78 |  | 476.9775 | -0.2511 | 494.87 | 477.03 | 0.8029 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 269.315 |  | 266.2084 | 1.167 | 276.85 | 267.14 | 2.718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.35 |  | 190.642 | 0.3714 | 194.96 | 189.48 | 0.6376 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 311.52 |  | 308.0595 | 1.1233 | 315.21 | 304.11 | 0.3146 | watch_only | none |
| ONTO | semiconductor_test_packaging | 236.92 |  | 236.5328 | 0.1637 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.9 |  | 46.8099 | -1.9439 | 51.64 | 47.435 | 0.0654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.08 |  | 42.5074 | -1.0054 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.92 |  | 119.4412 | -0.4363 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 284.01 |  | 282.3406 | 0.5913 | 296.8 | 283.22 | 0.1831 | watch_only | none |
| LIN | industrial_gases | 518.6 |  | 518.5612 | 0.0075 | 518.6 | 511.495 | 4.3232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.61 |  | 295.8727 | -0.0888 | 297.25 | 293.555 | 4.1643 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.37 |  | 26.5384 | -0.6346 | 27 | 25.42 | 3.4509 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 34.11 |  | 33.7077 | 1.1936 | 35.08 | 33.52 | 0.0586 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.35 |  | 20.0151 | 1.6732 | 20.97 | 19.755 | 0.0983 | watch_only | none |
| SNDK | memory_hbm_storage | 1092.29 |  | 1102.3657 | -0.914 | 1185.19 | 1114.57 | 2.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.585 |  | 437.7346 | 4.3064 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 752.53 |  | 727.296 | 3.4696 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.86 |  | 230.2813 | 0.6856 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.67 |  | 593.8391 | -0.0285 | 600.765 | 594.21 | 0.9955 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 246.16 |  | 245.3214 | 0.3419 | 253.38 | 243.72 | 0.1869 | watch_only | none |
| SKHY | memory_hbm_storage | 132.11 |  | 131.6331 | 0.3623 | 136.45 | 131.735 | 0.7267 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
