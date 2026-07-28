# Intraday State

- Generated at: `2026-07-28T21:43:44+08:00`
- Market time ET: `2026-07-28T09:43:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 50, 'watch_only': 3, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 1, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 671.665 |  | 674.2952 | -0.3901 | 677.3 | 671.64 | 0.0655 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 486.85 |  | 491.5822 | -0.9626 | 497.64 | 486.85 | 0.0801 | below_vwap | below_vwap |
| SMH | semiconductor_index | 524.81 |  | 528.4179 | -0.6828 | 533.01 | 524.69 | 0.0476 | below_vwap | below_vwap |
| SPY | market_regime | 737.22 |  | 738.4199 | -0.1625 | 739.42 | 737.195 | 0.0041 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.22 |  | 515.4308 | 0.5411 | 518.22 | 511.495 | 0.1698 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.22 |  | 515.4308 | 0.5411 | 518.22 | 511.495 | 0.1698 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.24 |  | 395.7584 | 0.1217 | 400.09 | 392.355 | 0.058 | watch_only | none |
| 3 | CORZ | high_beta_ai_infrastructure | 20.1 |  | 20.0832 | 0.0836 | 20.97 | 19.755 | 0.199 | watch_only | none |
| 4 | APLD | high_beta_ai_infrastructure | 26.625 |  | 26.1907 | 1.658 | 26.82 | 25.42 | 0.1878 | watch_only | none |
| 5 | SMH | semiconductor_index | 524.81 |  | 528.4179 | -0.6828 | 533.01 | 524.69 | 0.0476 | below_vwap | below_vwap |
| 6 | SOXX | semiconductor_index | 486.85 |  | 491.5822 | -0.9626 | 497.64 | 486.85 | 0.0801 | below_vwap | below_vwap |
| 7 | SPY | market_regime | 737.22 |  | 738.4199 | -0.1625 | 739.42 | 737.195 | 0.0041 | below_vwap | below_vwap |
| 8 | QQQ | market_regime | 671.665 |  | 674.2952 | -0.3901 | 677.3 | 671.64 | 0.0655 | below_vwap | below_vwap |
| 9 | GOOGL | cloud_ai_capex | 325.365 |  | 327.8259 | -0.7507 | 330.21 | 325.16 | 0.0246 | below_vwap | below_vwap |
| 10 | APD | industrial_gases | 297.25 |  | 294.3511 | 0.9848 | 297.25 | 293.555 | 4.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | IWM | market_regime | 291.78 |  | 292.6714 | -0.3046 | 293.26 | 291.74 | 0.0069 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 230 |  | 231.0535 | -0.4559 | 233.05 | 229.735 | 0.0478 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 33.76 |  | 34.0817 | -0.944 | 35.08 | 33.53 | 0.0889 | below_vwap | below_vwap |
| 15 | STX | memory_hbm_storage | 720.02 |  | 739.1463 | -2.5876 | 774.805 | 720.02 | 0.3042 | below_vwap | below_vwap |
| 16 | LITE | ai_networking_optical | 628.51 |  | 640.1498 | -1.8183 | 673.65 | 626.395 | 0.1846 | below_vwap | below_vwap |
| 17 | TT | data_center_power_cooling | 464.17 |  | 465.519 | -0.2898 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | VRT | data_center_power_cooling | 267.55 |  | 270.6322 | -1.1389 | 273.86 | 266.28 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | MRVL | custom_silicon_networking | 173.23 |  | 176.0606 | -1.6077 | 181.24 | 173.22 | 0.3348 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 161.315 |  | 162.4875 | -0.7216 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.22 |  | 515.4308 | 0.5411 | 518.22 | 511.495 | 0.1698 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 297.25 |  | 294.3511 | 0.9848 | 297.25 | 293.555 | 4.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | MSFT | cloud_ai_capex | 396.24 |  | 395.7584 | 0.1217 | 400.09 | 392.355 | 0.058 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 20.1 |  | 20.0832 | 0.0836 | 20.97 | 19.755 | 0.199 | watch_only | none |
| 5 | APLD | high_beta_ai_infrastructure | 26.625 |  | 26.1907 | 1.658 | 26.82 | 25.42 | 0.1878 | watch_only | none |
| 6 | NVDA | ai_accelerator | 193.93 |  | 194.5113 | -0.2988 | 195.4 | 193.65 | 0.6291 | below_vwap | below_vwap,spread_too_wide |
| 7 | TSM | foundry | 383.54 |  | 386.2816 | -0.7098 | 390.46 | 383.2 | 2.5838 | below_vwap | below_vwap,spread_too_wide |
| 8 | MU | memory_hbm_storage | 818 |  | 831.6901 | -1.6461 | 846.4 | 817.14 | 1.6528 | below_vwap | below_vwap,spread_too_wide |
| 9 | SMH | semiconductor_index | 524.81 |  | 528.4179 | -0.6828 | 533.01 | 524.69 | 0.0476 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 486.85 |  | 491.5822 | -0.9626 | 497.64 | 486.85 | 0.0801 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 372.41 |  | 374.5124 | -0.5614 | 378.64 | 371.79 | 0.3652 | below_vwap | below_vwap,spread_too_wide |
| 12 | SPY | market_regime | 737.22 |  | 738.4199 | -0.1625 | 739.42 | 737.195 | 0.0041 | below_vwap | below_vwap |
| 13 | QQQ | market_regime | 671.665 |  | 674.2952 | -0.3901 | 677.3 | 671.64 | 0.0655 | below_vwap | below_vwap |
| 14 | ASML | semiconductor_equipment | 1571.1 |  | 1576.362 | -0.3338 | 1586.01 | 1566.61 | 0.6199 | below_vwap | below_vwap,spread_too_wide |
| 15 | TT | data_center_power_cooling | 464.17 |  | 465.519 | -0.2898 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | STX | memory_hbm_storage | 720.02 |  | 739.1463 | -2.5876 | 774.805 | 720.02 | 0.3042 | below_vwap | below_vwap |
| 17 | VRT | data_center_power_cooling | 267.55 |  | 270.6322 | -1.1389 | 273.86 | 266.28 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ANET | ai_networking_optical | 161.315 |  | 162.4875 | -0.7216 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 325.365 |  | 327.8259 | -0.7507 | 330.21 | 325.16 | 0.0246 | below_vwap | below_vwap |
| 20 | PWR | data_center_power_cooling | 588.16 |  | 590.8622 | -0.4573 | 603.25 | 585.66 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 671.665 |  | 674.2952 | -0.3901 | 677.3 | 671.64 | 0.0655 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 60.45 |  | 61.2134 | -1.247 | 62.01 | 60.445 | 0.0165 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 193.93 |  | 194.5113 | -0.2988 | 195.4 | 193.65 | 0.6291 | below_vwap | below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 396.24 |  | 395.7584 | 0.1217 | 400.09 | 392.355 | 0.058 | watch_only | none |
| AAPL | mega_cap_platform | 338.89 |  | 339.7809 | -0.2622 | 342.87 | 337.78 | 0.2066 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 325.365 |  | 327.8259 | -0.7507 | 330.21 | 325.16 | 0.0246 | below_vwap | below_vwap |
| AMD | ai_accelerator | 454.6 |  | 461.2599 | -1.4439 | 472.485 | 454.355 | 0.4751 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 383.54 |  | 386.2816 | -0.7098 | 390.46 | 383.2 | 2.5838 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 486.85 |  | 491.5822 | -0.9626 | 497.64 | 486.85 | 0.0801 | below_vwap | below_vwap |
| SMH | semiconductor_index | 524.81 |  | 528.4179 | -0.6828 | 533.01 | 524.69 | 0.0476 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 372.41 |  | 374.5124 | -0.5614 | 378.64 | 371.79 | 0.3652 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 818 |  | 831.6901 | -1.6461 | 846.4 | 817.14 | 1.6528 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 173.23 |  | 176.0606 | -1.6077 | 181.24 | 173.22 | 0.3348 | below_vwap | below_vwap |
| DELL | ai_server_oem | 374.69 |  | 382.4092 | -2.0186 | 402 | 374.69 | 4.852 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 44.48 |  | 44.8238 | -0.7671 | 46.19 | 44.45 | 0.3822 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 27.645 |  | 28.0429 | -1.4189 | 28.86 | 27.59 | 2.098 | below_vwap | below_vwap,spread_too_wide |
| SPY | market_regime | 737.22 |  | 738.4199 | -0.1625 | 739.42 | 737.195 | 0.0041 | below_vwap | below_vwap |
| IWM | market_regime | 291.78 |  | 292.6714 | -0.3046 | 293.26 | 291.74 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 115.31 |  | 116.1522 | -0.7251 | 117.17 | 115.25 |  | below_vwap | below_vwap,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 65.9 |  | 66.8444 | -1.4128 | 68.995 | 65.86 | 4.3096 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 267.55 |  | 270.6322 | -1.1389 | 273.86 | 266.28 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 379.76 |  | 379.8869 | -0.0334 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 588.16 |  | 590.8622 | -0.4573 | 603.25 | 585.66 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 944.02 |  | 946.3003 | -0.241 | 955.825 | 935.665 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 464.17 |  | 465.519 | -0.2898 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 137.52 |  | 138.1007 | -0.4205 | 139.755 | 137.31 | 0.3636 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 161.315 |  | 162.4875 | -0.7216 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 237.985 |  | 244.6089 | -2.708 | 256.145 | 237.91 | 4.5969 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 628.51 |  | 640.1498 | -1.8183 | 673.65 | 626.395 | 0.1846 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 339.73 |  | 345.6339 | -1.7081 | 354.09 | 338.14 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 85.4 |  | 87.6468 | -2.5635 | 92.95 | 85.26 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 255.605 |  | 257.9471 | -0.908 | 268.265 | 254.4 | 3.6071 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1571.1 |  | 1576.362 | -0.3338 | 1586.01 | 1566.61 | 0.6199 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 480.44 |  | 485.9872 | -1.1414 | 494.87 | 479.845 | 0.6765 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 268.08 |  | 270.9259 | -1.0504 | 276.85 | 267.36 | 4.7896 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 190.17 |  | 192.4463 | -1.1828 | 194.96 | 190.055 | 0.3734 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 305.405 |  | 309.0994 | -1.1952 | 315.21 | 305.02 | 1.611 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 239.24 |  | 243.3973 | -1.708 | 248.8 | 238.55 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 47.89 |  | 48.7655 | -1.7953 | 51.64 | 47.435 | 2.0046 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 43.11 |  | 43.7735 | -1.5159 | 44.155 | 43.11 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.56 |  | 119.5626 | -0.8385 | 121 | 118.56 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 286.42 |  | 290.3181 | -1.3427 | 296.8 | 285.86 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.22 |  | 515.4308 | 0.5411 | 518.22 | 511.495 | 0.1698 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 297.25 |  | 294.3511 | 0.9848 | 297.25 | 293.555 | 4.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.625 |  | 26.1907 | 1.658 | 26.82 | 25.42 | 0.1878 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.76 |  | 34.0817 | -0.944 | 35.08 | 33.53 | 0.0889 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.1 |  | 20.0832 | 0.0836 | 20.97 | 19.755 | 0.199 | watch_only | none |
| SNDK | memory_hbm_storage | 1120 |  | 1148.6394 | -2.4933 | 1185.19 | 1120 | 0.2402 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 436.54 |  | 444.7006 | -1.8351 | 465.04 | 436.03 | 0.5246 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 720.02 |  | 739.1463 | -2.5876 | 774.805 | 720.02 | 0.3042 | below_vwap | below_vwap |
| AMZN | cloud_ai_capex | 230 |  | 231.0535 | -0.4559 | 233.05 | 229.735 | 0.0478 | below_vwap | below_vwap |
| META | cloud_ai_capex | 594.23 |  | 597.9919 | -0.6291 | 600.765 | 594.21 | 4.2559 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 245.83 |  | 248.5348 | -1.0883 | 253.38 | 245.08 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 132.265 |  | 134.0522 | -1.3332 | 136.45 | 132.095 | 0.9073 | below_vwap | below_vwap,spread_too_wide |
