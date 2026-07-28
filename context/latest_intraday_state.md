# Intraday State

- Generated at: `2026-07-28T22:11:12+08:00`
- Market time ET: `2026-07-28T10:11:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 32, 'watch_only': 2, 'below_vwap': 18, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 669.78 |  | 671.881 | -0.3127 | 677.3 | 670.84 | 0.0448 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 485.64 |  | 489.4049 | -0.7693 | 497.64 | 485.42 | 0.1071 | below_vwap | below_vwap |
| SMH | semiconductor_index | 522.8 |  | 525.8824 | -0.5861 | 533.01 | 523.325 | 0.0536 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.2 |  | 737.6155 | -0.0563 | 739.42 | 736.57 | 0.0353 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 521.28 |  | 518.0899 | 0.6157 | 518.6 | 511.495 | 0.0748 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 194.34 |  | 194.1607 | 0.0923 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| 2 | GOOGL | cloud_ai_capex | 327.52 |  | 326.952 | 0.1737 | 330.21 | 324.97 | 0.0305 | watch_only | none |
| 3 | LIN | industrial_gases | 521.28 |  | 518.0899 | 0.6157 | 518.6 | 511.495 | 0.0748 | buy_precheck_manual_confirm | none |
| 4 | ALAB | ai_networking_optical | 257.27 |  | 255.898 | 0.5361 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 297.145 |  | 295.767 | 0.4659 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | SOXX | semiconductor_index | 485.64 |  | 489.4049 | -0.7693 | 497.64 | 485.42 | 0.1071 | below_vwap | below_vwap |
| 7 | SPY | market_regime | 737.2 |  | 737.6155 | -0.0563 | 739.42 | 736.57 | 0.0353 | below_vwap | below_vwap |
| 8 | META | cloud_ai_capex | 594.21 |  | 595.6971 | -0.2496 | 600.765 | 594.21 | 0.1245 | below_vwap | below_vwap |
| 9 | AMZN | cloud_ai_capex | 229.88 |  | 230.4443 | -0.2449 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | APLD | high_beta_ai_infrastructure | 26.31 |  | 26.3557 | -0.1734 | 27 | 25.42 | 0.114 | below_vwap | below_vwap |
| 12 | MSFT | cloud_ai_capex | 393.89 |  | 394.3944 | -0.1279 | 400.09 | 392.355 | 0.2336 | below_vwap | below_vwap |
| 13 | TT | data_center_power_cooling | 464.53 |  | 464.612 | -0.0176 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ANET | ai_networking_optical | 161.52 |  | 161.7626 | -0.15 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 138.01 |  | 138.1302 | -0.0871 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 19.95 |  | 20.0388 | -0.4433 | 20.97 | 19.755 | 0.1504 | below_vwap | below_vwap |
| 17 | COHU | semiconductor_test_packaging | 42.48 |  | 43.1249 | -1.4955 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | TSM | foundry | 384.72 |  | 385.6445 | -0.2397 | 390.46 | 382.495 | 0.8292 | below_vwap | below_vwap,spread_too_wide |
| 19 | AVGO | custom_silicon_networking | 375.33 |  | 375.3666 | -0.0098 | 378.64 | 371.57 | 4.7905 | below_vwap | below_vwap,spread_too_wide |
| 20 | ETN | data_center_power_cooling | 377.99 |  | 379.0581 | -0.2818 | 384.565 | 377.43 | 4.217 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 521.28 |  | 518.0899 | 0.6157 | 518.6 | 511.495 | 0.0748 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 194.34 |  | 194.1607 | 0.0923 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| 3 | GOOGL | cloud_ai_capex | 327.52 |  | 326.952 | 0.1737 | 330.21 | 324.97 | 0.0305 | watch_only | none |
| 4 | TSM | foundry | 384.72 |  | 385.6445 | -0.2397 | 390.46 | 382.495 | 0.8292 | below_vwap | below_vwap,spread_too_wide |
| 5 | SOXX | semiconductor_index | 485.64 |  | 489.4049 | -0.7693 | 497.64 | 485.42 | 0.1071 | below_vwap | below_vwap |
| 6 | AVGO | custom_silicon_networking | 375.33 |  | 375.3666 | -0.0098 | 378.64 | 371.57 | 4.7905 | below_vwap | below_vwap,spread_too_wide |
| 7 | SPY | market_regime | 737.2 |  | 737.6155 | -0.0563 | 739.42 | 736.57 | 0.0353 | below_vwap | below_vwap |
| 8 | TT | data_center_power_cooling | 464.53 |  | 464.612 | -0.0176 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 161.52 |  | 161.7626 | -0.15 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 138.01 |  | 138.1302 | -0.0871 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 377.99 |  | 379.0581 | -0.2818 | 384.565 | 377.43 | 4.217 | below_vwap | below_vwap,spread_too_wide |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | ORCL | cloud_ai_capex | 115.33 |  | 115.902 | -0.4936 | 117.17 | 115.25 | 3.6417 | below_vwap | below_vwap,spread_too_wide |
| 14 | META | cloud_ai_capex | 594.21 |  | 595.6971 | -0.2496 | 600.765 | 594.21 | 0.1245 | below_vwap | below_vwap |
| 15 | TER | semiconductor_test_packaging | 304.85 |  | 305.4801 | -0.2063 | 315.21 | 304.11 | 0.5314 | below_vwap | below_vwap,spread_too_wide |
| 16 | MSFT | cloud_ai_capex | 393.89 |  | 394.3944 | -0.1279 | 400.09 | 392.355 | 0.2336 | below_vwap | below_vwap |
| 17 | AMZN | cloud_ai_capex | 229.88 |  | 230.4443 | -0.2449 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| 18 | ENTG | semiconductor_materials | 119.3 |  | 119.5872 | -0.2402 | 121 | 117.72 | 0.3856 | below_vwap | below_vwap,spread_too_wide |
| 19 | COHU | semiconductor_test_packaging | 42.48 |  | 43.1249 | -1.4955 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | CORZ | high_beta_ai_infrastructure | 19.95 |  | 20.0388 | -0.4433 | 20.97 | 19.755 | 0.1504 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 669.78 |  | 671.881 | -0.3127 | 677.3 | 670.84 | 0.0448 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 59.93 |  | 60.5563 | -1.0343 | 62.01 | 60.23 | 0.0167 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 194.34 |  | 194.1607 | 0.0923 | 195.4 | 193.65 | 0.0154 | watch_only | none |
| MSFT | cloud_ai_capex | 393.89 |  | 394.3944 | -0.1279 | 400.09 | 392.355 | 0.2336 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 336.635 |  | 339.0315 | -0.7069 | 342.87 | 337.78 | 0.8704 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 327.52 |  | 326.952 | 0.1737 | 330.21 | 324.97 | 0.0305 | watch_only | none |
| AMD | ai_accelerator | 452.32 |  | 457.6913 | -1.1736 | 472.485 | 453.76 | 0.8313 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 384.72 |  | 385.6445 | -0.2397 | 390.46 | 382.495 | 0.8292 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1555000 |  | 1782642.2481 | -12.7699 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 485.64 |  | 489.4049 | -0.7693 | 497.64 | 485.42 | 0.1071 | below_vwap | below_vwap |
| SMH | semiconductor_index | 522.8 |  | 525.8824 | -0.5861 | 533.01 | 523.325 | 0.0536 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.33 |  | 375.3666 | -0.0098 | 378.64 | 371.57 | 4.7905 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 809.21 |  | 821.3019 | -1.4723 | 846.4 | 813.91 | 0.1508 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 170.585 |  | 173.6535 | -1.767 | 181.24 | 172.395 | 2.3507 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 365.9 |  | 372.03 | -1.6477 | 402 | 374.02 | 1.4785 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 44.09 |  | 44.3649 | -0.6196 | 46.19 | 44.33 | 0.1588 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.445 |  | 27.7201 | -0.9924 | 28.86 | 27.59 | 0.1093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.2 |  | 737.6155 | -0.0563 | 739.42 | 736.57 | 0.0353 | below_vwap | below_vwap |
| IWM | market_regime | 291.495 |  | 291.9231 | -0.1466 | 293.26 | 291.55 | 0.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.33 |  | 115.902 | -0.4936 | 117.17 | 115.25 | 3.6417 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 65.5 |  | 66.1922 | -1.0457 | 68.995 | 65.635 | 1.4809 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 263.48 |  | 268.0175 | -1.693 | 273.86 | 266.04 | 1.1576 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 377.99 |  | 379.0581 | -0.2818 | 384.565 | 377.43 | 4.217 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 579.78 |  | 584.5265 | -0.812 | 603.25 | 584.69 | 3.8739 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 927.76 |  | 939.5127 | -1.2509 | 955.825 | 935.665 | 0.2102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 464.53 |  | 464.612 | -0.0176 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 138.01 |  | 138.1302 | -0.0871 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 161.52 |  | 161.7626 | -0.15 | 165.975 | 160.51 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 232.75 |  | 238.4308 | -2.3826 | 256.145 | 236.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 609.77 |  | 629.2369 | -3.0937 | 673.65 | 624.91 | 0.2263 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 332.32 |  | 340.3232 | -2.3517 | 354.09 | 338.14 | 0.2708 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 82.92 |  | 85.3734 | -2.8738 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 257.27 |  | 255.898 | 0.5361 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1565.85 |  | 1573.5666 | -0.4904 | 1586.01 | 1565.95 | 0.6916 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 473.77 |  | 480.6614 | -1.4337 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 262.085 |  | 267.8531 | -2.1535 | 276.85 | 267.14 | 1.9078 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 189.06 |  | 191.0321 | -1.0323 | 194.96 | 189.48 | 0.1904 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 304.85 |  | 305.4801 | -0.2063 | 315.21 | 304.11 | 0.5314 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 235.7 |  | 238.5586 | -1.1983 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.395 |  | 47.7374 | -2.8121 | 51.64 | 47.435 | 1.9183 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.48 |  | 43.1249 | -1.4955 | 44.155 | 42.4 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.3 |  | 119.5872 | -0.2402 | 121 | 117.72 | 0.3856 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 282.25 |  | 284.7311 | -0.8714 | 296.8 | 283.22 | 2.0868 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 521.28 |  | 518.0899 | 0.6157 | 518.6 | 511.495 | 0.0748 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 297.145 |  | 295.767 | 0.4659 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.31 |  | 26.3557 | -0.1734 | 27 | 25.42 | 0.114 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.115 |  | 33.4142 | -0.8955 | 35.08 | 33.52 | 0.0604 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.95 |  | 20.0388 | -0.4433 | 20.97 | 19.755 | 0.1504 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1080.48 |  | 1118.5145 | -3.4004 | 1185.19 | 1114.57 | 0.4628 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 427.98 |  | 437.4673 | -2.1687 | 465.04 | 435.22 | 3.2198 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 714.02 |  | 724.9206 | -1.5037 | 774.805 | 719.02 | 0.2171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 229.88 |  | 230.4443 | -0.2449 | 233.05 | 229.7 | 0.0261 | below_vwap | below_vwap |
| META | cloud_ai_capex | 594.21 |  | 595.6971 | -0.2496 | 600.765 | 594.21 | 0.1245 | below_vwap | below_vwap |
| ARM | ai_accelerator | 243.45 |  | 245.4248 | -0.8046 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.435 |  | 131.7411 | -1.7505 | 136.45 | 131.735 | 5.0218 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
