# Intraday State

- Generated at: `2026-07-28T22:25:24+08:00`
- Market time ET: `2026-07-28T10:25:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'watch_only': 3, 'below_vwap': 11, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 669.72 |  | 671.2938 | -0.2344 | 677.3 | 670.84 | 0.0896 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 483.35 |  | 488.5698 | -1.0684 | 497.64 | 485.42 | 0.0807 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 521.25 |  | 525.0858 | -0.7305 | 533.01 | 523.325 | 0.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.23 |  | 737.5106 | -0.038 | 739.42 | 736.57 | 0.0109 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 375.62 |  | 375.2067 | 0.1102 | 378.64 | 371.57 | 0.1145 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 327.375 |  | 326.9991 | 0.1149 | 330.21 | 324.97 | 0.1985 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 396.01 |  | 394.5337 | 0.3742 | 400.09 | 392.355 | 0.0758 | watch_only | none |
| 4 | TER | semiconductor_test_packaging | 305.78 |  | 305.3419 | 0.1435 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 297.7 |  | 296.339 | 0.4593 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | LIN | industrial_gases | 521.48 |  | 518.4538 | 0.5837 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SPY | market_regime | 737.23 |  | 737.5106 | -0.038 | 739.42 | 736.57 | 0.0109 | below_vwap | below_vwap |
| 8 | AMZN | cloud_ai_capex | 229.93 |  | 230.3408 | -0.1783 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | TT | data_center_power_cooling | 463.365 |  | 464.5314 | -0.2511 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ANET | ai_networking_optical | 161.23 |  | 161.5895 | -0.2225 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ALAB | ai_networking_optical | 254.22 |  | 255.6965 | -0.5774 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ENTG | semiconductor_materials | 119.02 |  | 119.3824 | -0.3036 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | COHU | semiconductor_test_packaging | 41.94 |  | 42.8248 | -2.0662 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TSM | foundry | 382.62 |  | 385.0762 | -0.6378 | 390.46 | 382.495 | 1.5681 | below_vwap | below_vwap,spread_too_wide |
| 16 | META | cloud_ai_capex | 594.24 |  | 595.1857 | -0.1589 | 600.765 | 594.21 | 0.7371 | below_vwap | below_vwap,spread_too_wide |
| 17 | APLD | high_beta_ai_infrastructure | 25.855 |  | 26.3279 | -1.796 | 27 | 25.42 | 1.0443 | below_vwap | below_vwap,spread_too_wide |
| 18 | NVDA | ai_accelerator | 193.435 |  | 194.0273 | -0.3053 | 195.4 | 193.65 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 521.25 |  | 525.0858 | -0.7305 | 533.01 | 523.325 | 0.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SOXX | semiconductor_index | 483.35 |  | 488.5698 | -1.0684 | 497.64 | 485.42 | 0.0807 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 521.48 |  | 518.4538 | 0.5837 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 2 | APD | industrial_gases | 297.7 |  | 296.339 | 0.4593 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | AVGO | custom_silicon_networking | 375.62 |  | 375.2067 | 0.1102 | 378.64 | 371.57 | 0.1145 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 327.375 |  | 326.9991 | 0.1149 | 330.21 | 324.97 | 0.1985 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 396.01 |  | 394.5337 | 0.3742 | 400.09 | 392.355 | 0.0758 | watch_only | none |
| 6 | TSM | foundry | 382.62 |  | 385.0762 | -0.6378 | 390.46 | 382.495 | 1.5681 | below_vwap | below_vwap,spread_too_wide |
| 7 | SPY | market_regime | 737.23 |  | 737.5106 | -0.038 | 739.42 | 736.57 | 0.0109 | below_vwap | below_vwap |
| 8 | TT | data_center_power_cooling | 463.365 |  | 464.5314 | -0.2511 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 161.23 |  | 161.5895 | -0.2225 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ALAB | ai_networking_optical | 254.22 |  | 255.6965 | -0.5774 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | META | cloud_ai_capex | 594.24 |  | 595.1857 | -0.1589 | 600.765 | 594.21 | 0.7371 | below_vwap | below_vwap,spread_too_wide |
| 13 | AMZN | cloud_ai_capex | 229.93 |  | 230.3408 | -0.1783 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| 14 | ENTG | semiconductor_materials | 119.02 |  | 119.3824 | -0.3036 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 41.94 |  | 42.8248 | -2.0662 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | APLD | high_beta_ai_infrastructure | 25.855 |  | 26.3279 | -1.796 | 27 | 25.42 | 1.0443 | below_vwap | below_vwap,spread_too_wide |
| 17 | TER | semiconductor_test_packaging | 305.78 |  | 305.3419 | 0.1435 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | NVDA | ai_accelerator | 193.435 |  | 194.0273 | -0.3053 | 195.4 | 193.65 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | MU | memory_hbm_storage | 796.43 |  | 812.3451 | -1.9592 | 846.4 | 813.91 | 2.0404 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | SMH | semiconductor_index | 521.25 |  | 525.0858 | -0.7305 | 533.01 | 523.325 | 0.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 669.72 |  | 671.2938 | -0.2344 | 677.3 | 670.84 | 0.0896 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 59.98 |  | 60.4091 | -0.7103 | 62.01 | 60.23 | 0.0167 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 193.435 |  | 194.0273 | -0.3053 | 195.4 | 193.65 | 0.0155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 396.01 |  | 394.5337 | 0.3742 | 400.09 | 392.355 | 0.0758 | watch_only | none |
| AAPL | mega_cap_platform | 337.695 |  | 338.7318 | -0.3061 | 342.87 | 337.78 | 0.3879 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 327.375 |  | 326.9991 | 0.1149 | 330.21 | 324.97 | 0.1985 | watch_only | none |
| AMD | ai_accelerator | 445.38 |  | 454.2684 | -1.9566 | 472.485 | 453.76 | 1.5492 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 382.62 |  | 385.0762 | -0.6378 | 390.46 | 382.495 | 1.5681 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 483.35 |  | 488.5698 | -1.0684 | 497.64 | 485.42 | 0.0807 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 521.25 |  | 525.0858 | -0.7305 | 533.01 | 523.325 | 0.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.62 |  | 375.2067 | 0.1102 | 378.64 | 371.57 | 0.1145 | watch_only | none |
| MU | memory_hbm_storage | 796.43 |  | 812.3451 | -1.9592 | 846.4 | 813.91 | 2.0404 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 168.7 |  | 172.7003 | -2.3163 | 181.24 | 172.395 | 1.3159 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 366.71 |  | 370.6175 | -1.0543 | 402 | 374.02 | 4.4313 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 43.53 |  | 44.1645 | -1.4367 | 46.19 | 44.33 | 4.6635 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 27.29 |  | 27.66 | -1.3376 | 28.86 | 27.59 | 0.0733 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.23 |  | 737.5106 | -0.038 | 739.42 | 736.57 | 0.0109 | below_vwap | below_vwap |
| IWM | market_regime | 290.83 |  | 291.7612 | -0.3192 | 293.26 | 291.55 | 0.0138 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.02 |  | 115.7437 | -0.6253 | 117.17 | 115.25 | 0.5303 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 64.91 |  | 65.9809 | -1.623 | 68.995 | 65.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 261 |  | 266.7818 | -2.1672 | 273.86 | 266.04 | 0.4751 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 376.94 |  | 378.8141 | -0.4947 | 384.565 | 377.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 572.015 |  | 580.5559 | -1.4712 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 917.81 |  | 935.2108 | -1.8606 | 955.825 | 935.665 | 4.7766 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 463.365 |  | 464.5314 | -0.2511 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 137.16 |  | 138.0135 | -0.6184 | 139.755 | 137.31 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 161.23 |  | 161.5895 | -0.2225 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 228.985 |  | 237.4369 | -3.5597 | 256.145 | 236.73 | 0.6332 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 603.3 |  | 625.0818 | -3.4846 | 673.65 | 624.91 | 1.7073 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 332 |  | 336.3502 | -1.2934 | 354.09 | 338.14 | 3.5572 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 81.9 |  | 84.8928 | -3.5254 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 254.22 |  | 255.6965 | -0.5774 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1563.97 |  | 1570.4114 | -0.4102 | 1586.01 | 1565.95 | 0.5953 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 472.23 |  | 478.4154 | -1.2929 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 262.46 |  | 266.414 | -1.4842 | 276.85 | 267.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 188.925 |  | 190.1742 | -0.6569 | 194.96 | 189.48 | 0.7252 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 305.78 |  | 305.3419 | 0.1435 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 232.79 |  | 238.1384 | -2.2459 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.635 |  | 47.4244 | -3.7731 | 51.64 | 47.435 | 0.2191 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 41.94 |  | 42.8248 | -2.0662 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.02 |  | 119.3824 | -0.3036 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 278.3 |  | 283.1458 | -1.7114 | 296.8 | 283.22 | 0.3881 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 521.48 |  | 518.4538 | 0.5837 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.7 |  | 296.339 | 0.4593 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.855 |  | 26.3279 | -1.796 | 27 | 25.42 | 1.0443 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 32.82 |  | 33.2872 | -1.4034 | 35.08 | 33.52 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.72 |  | 19.9896 | -1.3487 | 20.97 | 19.755 | 0.1014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1074.78 |  | 1106.1056 | -2.8321 | 1185.19 | 1114.57 | 4.6521 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 425.415 |  | 434.7475 | -2.1466 | 465.04 | 435.22 | 1.1753 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 709.085 |  | 722.4381 | -1.8483 | 774.805 | 719.02 | 0.2595 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 229.93 |  | 230.3408 | -0.1783 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| META | cloud_ai_capex | 594.24 |  | 595.1857 | -0.1589 | 600.765 | 594.21 | 0.7371 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 242.97 |  | 244.8352 | -0.7618 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.22 |  | 131.3484 | -0.8591 | 136.45 | 131.735 | 1.5359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
