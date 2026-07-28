# Intraday State

- Generated at: `2026-07-28T22:06:57+08:00`
- Market time ET: `2026-07-28T10:06:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 22, 'spread_too_wide_or_missing': 14, 'below_opening_15m_low': 14, 'price_stale_or_missing': 1, 'watch_only': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 671.64 |  | 671.9211 | -0.0418 | 677.3 | 670.84 | 0.0878 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 490.42 |  | 489.4781 | 0.1924 | 497.64 | 485.42 | 0.0856 | watch_only | none |
| SMH | semiconductor_index | 526.94 |  | 525.9613 | 0.1861 | 533.01 | 523.325 | 0.1025 | watch_only | none |
| SPY | market_regime | 737.78 |  | 737.6242 | 0.0211 | 739.42 | 736.57 | 0.0217 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 526.94 |  | 525.9613 | 0.1861 | 533.01 | 523.325 | 0.1025 | watch_only | none |
| 2 | SOXX | semiconductor_index | 490.42 |  | 489.4781 | 0.1924 | 497.64 | 485.42 | 0.0856 | watch_only | none |
| 3 | SPY | market_regime | 737.78 |  | 737.6242 | 0.0211 | 739.42 | 736.57 | 0.0217 | watch_only | none |
| 4 | CORZ | high_beta_ai_infrastructure | 20.05 |  | 20.0405 | 0.0473 | 20.97 | 19.755 | 0.0998 | watch_only | none |
| 5 | ORCL | cloud_ai_capex | 116.325 |  | 115.9035 | 0.3637 | 117.17 | 115.25 | 0.0774 | watch_only | none |
| 6 | JCI | data_center_power_cooling | 138.16 |  | 138.1321 | 0.0202 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | NVDA | ai_accelerator | 194.82 |  | 194.1406 | 0.35 | 195.4 | 193.65 | 0.6929 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | TSM | foundry | 386.83 |  | 385.6418 | 0.3081 | 390.46 | 382.495 | 0.9823 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ETN | data_center_power_cooling | 380.275 |  | 379.043 | 0.325 | 384.565 | 377.43 | 0.497 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | APD | industrial_gases | 297.13 |  | 295.688 | 0.4877 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 120.38 |  | 119.5529 | 0.6918 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | CRWV | gpu_cloud_ai_factory | 66.24 |  | 66.2069 | 0.05 | 68.995 | 65.635 | 3.2609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | LIN | industrial_gases | 520.69 |  | 518.0286 | 0.5137 | 518.6 | 511.495 | 3.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | HPE | ai_server_oem | 44.555 |  | 44.3722 | 0.4121 | 46.19 | 44.33 | 0.4264 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | IREN | high_beta_ai_infrastructure | 33.495 |  | 33.4157 | 0.2373 | 35.08 | 33.52 | 0.0597 | below_opening_15m_low | below_opening_15m_low |
| 16 | ANET | ai_networking_optical | 163.31 |  | 161.7079 | 0.9908 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | TER | semiconductor_test_packaging | 308.6 |  | 305.4588 | 1.0284 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 379.775 |  | 375.1739 | 1.2264 | 378.64 | 371.57 | 0.6346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | QQQ | market_regime | 671.64 |  | 671.9211 | -0.0418 | 677.3 | 670.84 | 0.0878 | below_vwap | below_vwap |
| 20 | IWM | market_regime | 291.69 |  | 291.9354 | -0.0841 | 293.26 | 291.55 | 0.0069 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.775 |  | 375.1739 | 1.2264 | 378.64 | 371.57 | 0.6346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | LIN | industrial_gases | 520.69 |  | 518.0286 | 0.5137 | 518.6 | 511.495 | 3.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | SMH | semiconductor_index | 526.94 |  | 525.9613 | 0.1861 | 533.01 | 523.325 | 0.1025 | watch_only | none |
| 4 | SOXX | semiconductor_index | 490.42 |  | 489.4781 | 0.1924 | 497.64 | 485.42 | 0.0856 | watch_only | none |
| 5 | SPY | market_regime | 737.78 |  | 737.6242 | 0.0211 | 739.42 | 736.57 | 0.0217 | watch_only | none |
| 6 | ORCL | cloud_ai_capex | 116.325 |  | 115.9035 | 0.3637 | 117.17 | 115.25 | 0.0774 | watch_only | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.05 |  | 20.0405 | 0.0473 | 20.97 | 19.755 | 0.0998 | watch_only | none |
| 8 | MU | memory_hbm_storage | 821.54 |  | 821.9736 | -0.0527 | 846.4 | 813.91 | 3.7734 | below_vwap | below_vwap,spread_too_wide |
| 9 | QQQ | market_regime | 671.64 |  | 671.9211 | -0.0418 | 677.3 | 670.84 | 0.0878 | below_vwap | below_vwap |
| 10 | ASML | semiconductor_equipment | 1573.41 |  | 1573.845 | -0.0276 | 1586.01 | 1565.95 | 0.2371 | below_vwap | below_vwap |
| 11 | TT | data_center_power_cooling | 463.08 |  | 464.6656 | -0.3412 | 477.73 | 460.77 | 0.5118 | below_vwap | below_vwap,spread_too_wide |
| 12 | STX | memory_hbm_storage | 723.46 |  | 725.1352 | -0.231 | 774.805 | 719.02 | 2.0706 | below_vwap | below_vwap,spread_too_wide |
| 13 | VRT | data_center_power_cooling | 267.4 |  | 268.4788 | -0.4018 | 273.86 | 266.04 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GOOGL | cloud_ai_capex | 326.93 |  | 326.9487 | -0.0057 | 330.21 | 324.97 | 0.2998 | below_vwap | below_vwap |
| 15 | WDC | memory_hbm_storage | 436.02 |  | 438.0768 | -0.4695 | 465.04 | 435.22 | 0.4495 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.69 |  | 291.9354 | -0.0841 | 293.26 | 291.55 | 0.0069 | below_vwap | below_vwap |
| 17 | AMAT | semiconductor_equipment | 478.765 |  | 480.8825 | -0.4403 | 494.87 | 477.03 | 1.3827 | below_vwap | below_vwap,spread_too_wide |
| 18 | AMD | ai_accelerator | 457.71 |  | 457.8467 | -0.0299 | 472.485 | 453.76 | 3.2772 | below_vwap | below_vwap,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 190.81 |  | 191.1864 | -0.1969 | 194.96 | 189.48 | 0.1048 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 671.64 |  | 671.9211 | -0.0418 | 677.3 | 670.84 | 0.0878 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 60.51 |  | 60.5728 | -0.1036 | 62.01 | 60.23 | 0.0331 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 194.82 |  | 194.1406 | 0.35 | 195.4 | 193.65 | 0.6929 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 393.45 |  | 394.4291 | -0.2482 | 400.09 | 392.355 | 0.3635 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 336.025 |  | 339.1281 | -0.915 | 342.87 | 337.78 | 0.0446 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 326.93 |  | 326.9487 | -0.0057 | 330.21 | 324.97 | 0.2998 | below_vwap | below_vwap |
| AMD | ai_accelerator | 457.71 |  | 457.8467 | -0.0299 | 472.485 | 453.76 | 3.2772 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 386.83 |  | 385.6418 | 0.3081 | 390.46 | 382.495 | 0.9823 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.42 |  | 489.4781 | 0.1924 | 497.64 | 485.42 | 0.0856 | watch_only | none |
| SMH | semiconductor_index | 526.94 |  | 525.9613 | 0.1861 | 533.01 | 523.325 | 0.1025 | watch_only | none |
| AVGO | custom_silicon_networking | 379.775 |  | 375.1739 | 1.2264 | 378.64 | 371.57 | 0.6346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 821.54 |  | 821.9736 | -0.0527 | 846.4 | 813.91 | 3.7734 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 173.48 |  | 173.8256 | -0.1988 | 181.24 | 172.395 | 0.6802 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 369.89 |  | 372.1798 | -0.6152 | 402 | 374.02 | 0.3298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 44.555 |  | 44.3722 | 0.4121 | 46.19 | 44.33 | 0.4264 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SMCI | ai_server_oem | 27.635 |  | 27.7354 | -0.3621 | 28.86 | 27.59 | 0.0724 | below_vwap | below_vwap |
| SPY | market_regime | 737.78 |  | 737.6242 | 0.0211 | 739.42 | 736.57 | 0.0217 | watch_only | none |
| IWM | market_regime | 291.69 |  | 291.9354 | -0.0841 | 293.26 | 291.55 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 116.325 |  | 115.9035 | 0.3637 | 117.17 | 115.25 | 0.0774 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 66.24 |  | 66.2069 | 0.05 | 68.995 | 65.635 | 3.2609 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.4 |  | 268.4788 | -0.4018 | 273.86 | 266.04 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 380.275 |  | 379.043 | 0.325 | 384.565 | 377.43 | 0.497 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 583.03 |  | 585.1076 | -0.3551 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 933.83 |  | 940.2493 | -0.6827 | 955.825 | 935.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 463.08 |  | 464.6656 | -0.3412 | 477.73 | 460.77 | 0.5118 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 138.16 |  | 138.1321 | 0.0202 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 163.31 |  | 161.7079 | 0.9908 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 235 |  | 238.725 | -1.5604 | 256.145 | 236.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 620.9 |  | 631.054 | -1.6091 | 673.65 | 624.91 | 0.6168 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 338.29 |  | 340.6651 | -0.6972 | 354.09 | 338.14 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 84.46 |  | 85.4542 | -1.1635 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 261.69 |  | 255.6877 | 2.3475 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1573.41 |  | 1573.845 | -0.0276 | 1586.01 | 1565.95 | 0.2371 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 478.765 |  | 480.8825 | -0.4403 | 494.87 | 477.03 | 1.3827 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 264.8 |  | 268.298 | -1.3038 | 276.85 | 267.14 | 4.1239 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 190.81 |  | 191.1864 | -0.1969 | 194.96 | 189.48 | 0.1048 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 308.6 |  | 305.4588 | 1.0284 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 236.56 |  | 238.5875 | -0.8498 | 248.8 | 236.42 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.58 |  | 47.8768 | -2.7087 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.615 |  | 43.1701 | -1.2859 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.38 |  | 119.5529 | 0.6918 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 283.27 |  | 284.9526 | -0.5905 | 296.8 | 283.22 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 520.69 |  | 518.0286 | 0.5137 | 518.6 | 511.495 | 3.9006 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.13 |  | 295.688 | 0.4877 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.745 |  | 26.3368 | 1.5499 | 27 | 25.42 | 0.673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.495 |  | 33.4157 | 0.2373 | 35.08 | 33.52 | 0.0597 | below_opening_15m_low | below_opening_15m_low |
| CORZ | high_beta_ai_infrastructure | 20.05 |  | 20.0405 | 0.0473 | 20.97 | 19.755 | 0.0998 | watch_only | none |
| SNDK | memory_hbm_storage | 1112 |  | 1121.3725 | -0.8358 | 1185.19 | 1114.57 | 0.3939 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 436.02 |  | 438.0768 | -0.4695 | 465.04 | 435.22 | 0.4495 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 723.46 |  | 725.1352 | -0.231 | 774.805 | 719.02 | 2.0706 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 229.58 |  | 230.4816 | -0.3912 | 233.05 | 229.7 | 0.0348 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 593.47 |  | 595.9033 | -0.4083 | 600.765 | 594.21 | 0.3303 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 244.71 |  | 245.5923 | -0.3592 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131.05 |  | 131.8201 | -0.5842 | 136.45 | 131.735 | 0.992 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
