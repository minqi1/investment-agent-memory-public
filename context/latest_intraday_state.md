# Intraday State

- Generated at: `2026-07-28T22:40:53+08:00`
- Market time ET: `2026-07-28T10:40:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 35, 'manual_confirm_candidate': 1, 'watch_only': 3, 'below_vwap': 13, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.55 |  | 671.2069 | -0.0979 | 677.3 | 670.84 | 0.0597 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 485.415 |  | 488.0817 | -0.5464 | 497.64 | 485.42 | 0.0989 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 523.99 |  | 524.8473 | -0.1633 | 533.01 | 523.325 | 0.0401 | below_vwap | below_vwap |
| SPY | market_regime | 737.51 |  | 737.5501 | -0.0054 | 739.42 | 736.57 | 0.0081 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 195.71 |  | 194.1214 | 0.8184 | 195.4 | 193.65 | 0.0562 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 327.37 |  | 327.146 | 0.0685 | 330.21 | 324.97 | 0.058 | watch_only | none |
| 2 | APD | industrial_gases | 296.975 |  | 296.4551 | 0.1754 | 297.25 | 293.555 | 0.2323 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 395.025 |  | 394.6804 | 0.0873 | 400.09 | 392.355 | 0.3038 | watch_only | none |
| 4 | NVDA | ai_accelerator | 195.71 |  | 194.1214 | 0.8184 | 195.4 | 193.65 | 0.0562 | buy_precheck_manual_confirm | none |
| 5 | LIN | industrial_gases | 519.695 |  | 518.6531 | 0.2009 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | AVGO | custom_silicon_networking | 376.01 |  | 375.2795 | 0.1947 | 378.64 | 371.57 | 0.9361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 162.64 |  | 161.675 | 0.5969 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SMH | semiconductor_index | 523.99 |  | 524.8473 | -0.1633 | 533.01 | 523.325 | 0.0401 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 737.51 |  | 737.5501 | -0.0054 | 739.42 | 736.57 | 0.0081 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | SMCI | ai_server_oem | 27.61 |  | 27.6341 | -0.0873 | 28.86 | 27.59 | 0.0724 | below_vwap | below_vwap |
| 12 | TT | data_center_power_cooling | 462.86 |  | 464.0641 | -0.2595 | 477.73 | 460.77 | 0.2528 | below_vwap | below_vwap |
| 13 | STX | memory_hbm_storage | 719.16 |  | 721.7054 | -0.3527 | 774.805 | 719.02 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 118.16 |  | 119.088 | -0.7793 | 121 | 117.72 | 0.2539 | below_vwap | below_vwap |
| 15 | ALAB | ai_networking_optical | 254.15 |  | 255.2857 | -0.4449 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | APLD | high_beta_ai_infrastructure | 26.225 |  | 26.296 | -0.2698 | 27 | 25.42 | 0.1525 | below_vwap | below_vwap |
| 17 | COHU | semiconductor_test_packaging | 42.295 |  | 42.668 | -0.8743 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | TSM | foundry | 382.55 |  | 384.666 | -0.5501 | 390.46 | 382.495 | 1.856 | below_vwap | below_vwap,spread_too_wide |
| 19 | ASML | semiconductor_equipment | 1569.84 |  | 1570.22 | -0.0242 | 1586.01 | 1565.95 | 0.3726 | below_vwap | below_vwap,spread_too_wide |
| 20 | ORCL | cloud_ai_capex | 115.48 |  | 115.7019 | -0.1918 | 117.17 | 115.25 | 4.2258 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 195.71 |  | 194.1214 | 0.8184 | 195.4 | 193.65 | 0.0562 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 519.695 |  | 518.6531 | 0.2009 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | GOOGL | cloud_ai_capex | 327.37 |  | 327.146 | 0.0685 | 330.21 | 324.97 | 0.058 | watch_only | none |
| 4 | APD | industrial_gases | 296.975 |  | 296.4551 | 0.1754 | 297.25 | 293.555 | 0.2323 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 395.025 |  | 394.6804 | 0.0873 | 400.09 | 392.355 | 0.3038 | watch_only | none |
| 6 | TSM | foundry | 382.55 |  | 384.666 | -0.5501 | 390.46 | 382.495 | 1.856 | below_vwap | below_vwap,spread_too_wide |
| 7 | SMH | semiconductor_index | 523.99 |  | 524.8473 | -0.1633 | 533.01 | 523.325 | 0.0401 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 737.51 |  | 737.5501 | -0.0054 | 739.42 | 736.57 | 0.0081 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1569.84 |  | 1570.22 | -0.0242 | 1586.01 | 1565.95 | 0.3726 | below_vwap | below_vwap,spread_too_wide |
| 10 | TT | data_center_power_cooling | 462.86 |  | 464.0641 | -0.2595 | 477.73 | 460.77 | 0.2528 | below_vwap | below_vwap |
| 11 | STX | memory_hbm_storage | 719.16 |  | 721.7054 | -0.3527 | 774.805 | 719.02 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ALAB | ai_networking_optical | 254.15 |  | 255.2857 | -0.4449 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ORCL | cloud_ai_capex | 115.48 |  | 115.7019 | -0.1918 | 117.17 | 115.25 | 4.2258 | below_vwap | below_vwap,spread_too_wide |
| 15 | ENTG | semiconductor_materials | 118.16 |  | 119.088 | -0.7793 | 121 | 117.72 | 0.2539 | below_vwap | below_vwap |
| 16 | SMCI | ai_server_oem | 27.61 |  | 27.6341 | -0.0873 | 28.86 | 27.59 | 0.0724 | below_vwap | below_vwap |
| 17 | COHU | semiconductor_test_packaging | 42.295 |  | 42.668 | -0.8743 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 376.01 |  | 375.2795 | 0.1947 | 378.64 | 371.57 | 0.9361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | APLD | high_beta_ai_infrastructure | 26.225 |  | 26.296 | -0.2698 | 27 | 25.42 | 0.1525 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 162.64 |  | 161.675 | 0.5969 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.55 |  | 671.2069 | -0.0979 | 677.3 | 670.84 | 0.0597 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 60.21 |  | 60.3783 | -0.2788 | 62.01 | 60.23 | 0.0332 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 195.71 |  | 194.1214 | 0.8184 | 195.4 | 193.65 | 0.0562 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 395.025 |  | 394.6804 | 0.0873 | 400.09 | 392.355 | 0.3038 | watch_only | none |
| AAPL | mega_cap_platform | 337.44 |  | 338.6407 | -0.3546 | 342.87 | 337.78 | 0.0652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 327.37 |  | 327.146 | 0.0685 | 330.21 | 324.97 | 0.058 | watch_only | none |
| AMD | ai_accelerator | 450.24 |  | 453.2958 | -0.6741 | 472.485 | 453.76 | 2.6941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 382.55 |  | 384.666 | -0.5501 | 390.46 | 382.495 | 1.856 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 485.415 |  | 488.0817 | -0.5464 | 497.64 | 485.42 | 0.0989 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 523.99 |  | 524.8473 | -0.1633 | 533.01 | 523.325 | 0.0401 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 376.01 |  | 375.2795 | 0.1947 | 378.64 | 371.57 | 0.9361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 809.23 |  | 811.1493 | -0.2366 | 846.4 | 813.91 | 0.7241 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 170.42 |  | 171.5778 | -0.6748 | 181.24 | 172.395 | 1.0562 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 369.445 |  | 370.5733 | -0.3045 | 402 | 374.02 | 3.7813 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.89 |  | 44.0197 | -0.2946 | 46.19 | 44.33 | 0.1823 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.61 |  | 27.6341 | -0.0873 | 28.86 | 27.59 | 0.0724 | below_vwap | below_vwap |
| SPY | market_regime | 737.51 |  | 737.5501 | -0.0054 | 739.42 | 736.57 | 0.0081 | below_vwap | below_vwap |
| IWM | market_regime | 290.83 |  | 291.6344 | -0.2758 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.48 |  | 115.7019 | -0.1918 | 117.17 | 115.25 | 4.2258 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 64.875 |  | 65.9067 | -1.5655 | 68.995 | 65.635 | 4.2235 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 260.6 |  | 265.8339 | -1.9688 | 273.86 | 266.04 | 3.5649 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 376.43 |  | 378.5619 | -0.5631 | 384.565 | 377.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 573.75 |  | 579.1765 | -0.9369 | 603.25 | 584.69 | 1.0649 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 922.28 |  | 933.4835 | -1.2002 | 955.825 | 935.665 | 0.772 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 462.86 |  | 464.0641 | -0.2595 | 477.73 | 460.77 | 0.2528 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 137.03 |  | 137.8089 | -0.5652 | 139.755 | 137.31 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 162.64 |  | 161.675 | 0.5969 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 231.07 |  | 235.9484 | -2.0676 | 256.145 | 236.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 616.49 |  | 623.304 | -1.0932 | 673.65 | 624.91 | 3.2442 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 332.74 |  | 335.5642 | -0.8416 | 354.09 | 338.14 | 0.3516 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 83.86 |  | 84.7175 | -1.0122 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 254.15 |  | 255.2857 | -0.4449 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1569.84 |  | 1570.22 | -0.0242 | 1586.01 | 1565.95 | 0.3726 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 472.13 |  | 477.6475 | -1.1551 | 494.87 | 477.03 | 5.1066 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 261.89 |  | 265.7867 | -1.4661 | 276.85 | 267.14 | 0.1795 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 188.53 |  | 189.893 | -0.7178 | 194.96 | 189.48 | 0.7797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 303.78 |  | 305.0825 | -0.4269 | 315.21 | 304.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 232.06 |  | 237.9192 | -2.4627 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.43 |  | 47.2605 | -1.7573 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.295 |  | 42.668 | -0.8743 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.16 |  | 119.088 | -0.7793 | 121 | 117.72 | 0.2539 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 278.57 |  | 282.3271 | -1.3308 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 519.695 |  | 518.6531 | 0.2009 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.975 |  | 296.4551 | 0.1754 | 297.25 | 293.555 | 0.2323 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 26.225 |  | 26.296 | -0.2698 | 27 | 25.42 | 0.1525 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.07 |  | 33.2513 | -0.5451 | 35.08 | 33.52 | 0.0605 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.745 |  | 19.9414 | -0.9847 | 20.97 | 19.755 | 0.1519 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1095.71 |  | 1103.4631 | -0.7026 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 427.65 |  | 433.4397 | -1.3357 | 465.04 | 435.22 | 2.7359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 719.16 |  | 721.7054 | -0.3527 | 774.805 | 719.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 228.285 |  | 230.1408 | -0.8064 | 233.05 | 229.7 | 0.3461 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 590.57 |  | 594.8088 | -0.7126 | 600.765 | 594.21 | 1.358 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 242.02 |  | 244.6277 | -1.066 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.865 |  | 131.2431 | -0.2881 | 136.45 | 131.735 | 0.2292 | below_opening_15m_low | below_opening_15m_low,below_vwap |
