# Intraday State

- Generated at: `2026-07-28T22:16:44+08:00`
- Market time ET: `2026-07-28T10:16:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 37, 'below_vwap': 14, 'watch_only': 2, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 668.83 |  | 671.6179 | -0.4151 | 677.3 | 670.84 | 0.0792 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 483.11 |  | 489.189 | -1.2427 | 497.64 | 485.42 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 521.155 |  | 525.7454 | -0.8731 | 533.01 | 523.325 | 0.0614 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.06 |  | 737.5614 | -0.068 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 394.47 |  | 394.3607 | 0.0277 | 400.09 | 392.355 | 0.0583 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 327.395 |  | 326.9562 | 0.1342 | 330.21 | 324.97 | 0.1985 | watch_only | none |
| 3 | APD | industrial_gases | 297.84 |  | 296.2063 | 0.5515 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 521.53 |  | 518.2252 | 0.6377 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | NVDA | ai_accelerator | 193.99 |  | 194.1709 | -0.0932 | 195.4 | 193.65 | 0.0206 | below_vwap | below_vwap |
| 6 | SPY | market_regime | 737.06 |  | 737.5614 | -0.068 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| 7 | AMZN | cloud_ai_capex | 229.9 |  | 230.392 | -0.2135 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| 8 | TSM | foundry | 383.135 |  | 385.3682 | -0.5795 | 390.46 | 382.495 | 0.1592 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | CORZ | high_beta_ai_infrastructure | 19.89 |  | 20.031 | -0.7041 | 20.97 | 19.755 | 0.1006 | below_vwap | below_vwap |
| 11 | TT | data_center_power_cooling | 463.51 |  | 464.6006 | -0.2347 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ANET | ai_networking_optical | 161.03 |  | 161.7607 | -0.4517 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ETN | data_center_power_cooling | 377.645 |  | 379.0278 | -0.3648 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ALAB | ai_networking_optical | 254.02 |  | 255.9403 | -0.7503 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 118.695 |  | 119.5395 | -0.7065 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 42.56 |  | 43.0422 | -1.1203 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 373.885 |  | 375.3178 | -0.3818 | 378.64 | 371.57 | 0.8131 | below_vwap | below_vwap,spread_too_wide |
| 18 | APLD | high_beta_ai_infrastructure | 26.11 |  | 26.3679 | -0.978 | 27 | 25.42 | 3.1789 | below_vwap | below_vwap,spread_too_wide |
| 19 | SMH | semiconductor_index | 521.155 |  | 525.7454 | -0.8731 | 533.01 | 523.325 | 0.0614 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SOXX | semiconductor_index | 483.11 |  | 489.189 | -1.2427 | 497.64 | 485.42 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 521.53 |  | 518.2252 | 0.6377 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | APD | industrial_gases | 297.84 |  | 296.2063 | 0.5515 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | GOOGL | cloud_ai_capex | 327.395 |  | 326.9562 | 0.1342 | 330.21 | 324.97 | 0.1985 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 394.47 |  | 394.3607 | 0.0277 | 400.09 | 392.355 | 0.0583 | watch_only | none |
| 5 | NVDA | ai_accelerator | 193.99 |  | 194.1709 | -0.0932 | 195.4 | 193.65 | 0.0206 | below_vwap | below_vwap |
| 6 | TSM | foundry | 383.135 |  | 385.3682 | -0.5795 | 390.46 | 382.495 | 0.1592 | below_vwap | below_vwap |
| 7 | AVGO | custom_silicon_networking | 373.885 |  | 375.3178 | -0.3818 | 378.64 | 371.57 | 0.8131 | below_vwap | below_vwap,spread_too_wide |
| 8 | SPY | market_regime | 737.06 |  | 737.5614 | -0.068 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| 9 | TT | data_center_power_cooling | 463.51 |  | 464.6006 | -0.2347 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ANET | ai_networking_optical | 161.03 |  | 161.7607 | -0.4517 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 377.645 |  | 379.0278 | -0.3648 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ALAB | ai_networking_optical | 254.02 |  | 255.9403 | -0.7503 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AMZN | cloud_ai_capex | 229.9 |  | 230.392 | -0.2135 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| 15 | ENTG | semiconductor_materials | 118.695 |  | 119.5395 | -0.7065 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 42.56 |  | 43.0422 | -1.1203 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CORZ | high_beta_ai_infrastructure | 19.89 |  | 20.031 | -0.7041 | 20.97 | 19.755 | 0.1006 | below_vwap | below_vwap |
| 18 | APLD | high_beta_ai_infrastructure | 26.11 |  | 26.3679 | -0.978 | 27 | 25.42 | 3.1789 | below_vwap | below_vwap,spread_too_wide |
| 19 | MU | memory_hbm_storage | 798.81 |  | 819.3183 | -2.5031 | 846.4 | 813.91 | 0.5721 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | SMH | semiconductor_index | 521.155 |  | 525.7454 | -0.8731 | 533.01 | 523.325 | 0.0614 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 668.83 |  | 671.6179 | -0.4151 | 677.3 | 670.84 | 0.0792 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 59.67 |  | 60.4894 | -1.3546 | 62.01 | 60.23 | 0.0335 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 193.99 |  | 194.1709 | -0.0932 | 195.4 | 193.65 | 0.0206 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.47 |  | 394.3607 | 0.0277 | 400.09 | 392.355 | 0.0583 | watch_only | none |
| AAPL | mega_cap_platform | 337.35 |  | 338.8464 | -0.4416 | 342.87 | 337.78 | 0.0267 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 327.395 |  | 326.9562 | 0.1342 | 330.21 | 324.97 | 0.1985 | watch_only | none |
| AMD | ai_accelerator | 448.645 |  | 456.9397 | -1.8153 | 472.485 | 453.76 | 0.1939 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 383.135 |  | 385.3682 | -0.5795 | 390.46 | 382.495 | 0.1592 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 483.11 |  | 489.189 | -1.2427 | 497.64 | 485.42 | 0.0642 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 521.155 |  | 525.7454 | -0.8731 | 533.01 | 523.325 | 0.0614 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 373.885 |  | 375.3178 | -0.3818 | 378.64 | 371.57 | 0.8131 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 798.81 |  | 819.3183 | -2.5031 | 846.4 | 813.91 | 0.5721 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 169.21 |  | 173.2519 | -2.333 | 181.24 | 172.395 | 0.4019 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 365 |  | 371.5151 | -1.7536 | 402 | 374.02 | 4.1918 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.715 |  | 44.3212 | -1.3677 | 46.19 | 44.33 | 0.6405 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 27.36 |  | 27.6988 | -1.2231 | 28.86 | 27.59 | 0.0731 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.06 |  | 737.5614 | -0.068 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 291.115 |  | 291.8613 | -0.2557 | 293.26 | 291.55 | 0.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 114.635 |  | 115.8433 | -1.0431 | 117.17 | 115.25 | 4.6408 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 65.5 |  | 66.1495 | -0.9819 | 68.995 | 65.635 | 4.5802 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 262.56 |  | 267.6499 | -1.9017 | 273.86 | 266.04 | 3.8125 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 377.645 |  | 379.0278 | -0.3648 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 576.13 |  | 582.7533 | -1.1365 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 922.34 |  | 938.1266 | -1.6828 | 955.825 | 935.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 463.51 |  | 464.6006 | -0.2347 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 137.22 |  | 138.0812 | -0.6237 | 139.755 | 137.31 | 0.3207 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ANET | ai_networking_optical | 161.03 |  | 161.7607 | -0.4517 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 231.75 |  | 238.0855 | -2.661 | 256.145 | 236.73 | 4.5049 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 610.575 |  | 627.6258 | -2.7167 | 673.65 | 624.91 | 4.7496 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 333.05 |  | 339.2217 | -1.8194 | 354.09 | 338.14 | 0.5164 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 82.075 |  | 85.2254 | -3.6965 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 254.02 |  | 255.9403 | -0.7503 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1559.99 |  | 1572.5916 | -0.8013 | 1586.01 | 1565.95 | 0.6564 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 470.37 |  | 479.7487 | -1.9549 | 494.87 | 477.03 | 3.0104 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 260.07 |  | 267.3851 | -2.7358 | 276.85 | 267.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 187.71 |  | 190.7618 | -1.5998 | 194.96 | 189.48 | 4.5709 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 303.6 |  | 305.4795 | -0.6153 | 315.21 | 304.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 232.4 |  | 238.3326 | -2.4892 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.66 |  | 47.6049 | -4.0855 | 51.64 | 47.435 | 0.1752 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.56 |  | 43.0422 | -1.1203 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.695 |  | 119.5395 | -0.7065 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 279.99 |  | 284.3567 | -1.5356 | 296.8 | 283.22 | 1.0322 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 521.53 |  | 518.2252 | 0.6377 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.84 |  | 296.2063 | 0.5515 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.11 |  | 26.3679 | -0.978 | 27 | 25.42 | 3.1789 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 32.86 |  | 33.3768 | -1.5485 | 35.08 | 33.52 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.89 |  | 20.031 | -0.7041 | 20.97 | 19.755 | 0.1006 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1067.5 |  | 1114.5399 | -4.2206 | 1185.19 | 1114.57 | 0.9986 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 428.32 |  | 436.5957 | -1.8955 | 465.04 | 435.22 | 0.7891 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 709.19 |  | 724.3402 | -2.0916 | 774.805 | 719.02 | 3.583 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 229.9 |  | 230.392 | -0.2135 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| META | cloud_ai_capex | 592.16 |  | 595.383 | -0.5413 | 600.765 | 594.21 | 0.054 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 242.33 |  | 245.2646 | -1.1965 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.41 |  | 131.5544 | -1.6301 | 136.45 | 131.735 | 5.0228 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
