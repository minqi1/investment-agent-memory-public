# Intraday State

- Generated at: `2026-07-29T02:57:43+08:00`
- Market time ET: `2026-07-28T14:57:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 18, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.64 |  | 674.1833 | 0.3644 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| SOXX | semiconductor_index | 491.39 |  | 489.9899 | 0.2857 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| SMH | semiconductor_index | 529.62 |  | 527.3865 | 0.4235 | 533.01 | 523.325 | 0.0227 | watch_only | none |
| SPY | market_regime | 741.51 |  | 739.599 | 0.2584 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.07 |  | 196.0907 | 0.4994 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.69 |  | 387.7881 | 1.0062 | 390.46 | 382.495 | 0.0357 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 381.31 |  | 378.6375 | 0.7058 | 378.64 | 371.57 | 0.1652 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.51 |  | 739.599 | 0.2584 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.315 |  | 330.9891 | 1.307 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.51 |  | 739.599 | 0.2584 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 491.39 |  | 489.9899 | 0.2857 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| 3 | ASML | semiconductor_equipment | 1582.185 |  | 1577.3592 | 0.3059 | 1586.01 | 1565.95 | 0.1138 | watch_only | none |
| 4 | IWM | market_regime | 293.09 |  | 292.3966 | 0.2371 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 5 | META | cloud_ai_capex | 594.265 |  | 593.8254 | 0.074 | 600.765 | 594.21 | 0.0825 | watch_only | none |
| 6 | NVDA | ai_accelerator | 197.07 |  | 196.0907 | 0.4994 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 396.82 |  | 396.4119 | 0.1029 | 400.09 | 392.355 | 0.0428 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 231.19 |  | 230.5145 | 0.293 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 9 | AVGO | custom_silicon_networking | 381.31 |  | 378.6375 | 0.7058 | 378.64 | 371.57 | 0.1652 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 339.43 |  | 338.9591 | 0.1389 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 11 | VRT | data_center_power_cooling | 266.42 |  | 266.1384 | 0.1058 | 273.86 | 266.04 | 0.1989 | watch_only | none |
| 12 | SMH | semiconductor_index | 529.62 |  | 527.3865 | 0.4235 | 533.01 | 523.325 | 0.0227 | watch_only | none |
| 13 | QQQ | market_regime | 676.64 |  | 674.1833 | 0.3644 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| 14 | TSM | foundry | 391.69 |  | 387.7881 | 1.0062 | 390.46 | 382.495 | 0.0357 | buy_precheck_manual_confirm | none |
| 15 | KLAC | semiconductor_equipment | 191.615 |  | 190.7897 | 0.4326 | 194.96 | 189.48 | 0.0261 | watch_only | none |
| 16 | HPE | ai_server_oem | 44.61 |  | 44.4424 | 0.3771 | 46.19 | 44.33 | 0.0448 | watch_only | none |
| 17 | SMCI | ai_server_oem | 28.2 |  | 28.0052 | 0.6958 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 18 | PWR | data_center_power_cooling | 586.14 |  | 582.4792 | 0.6285 | 603.25 | 584.69 | 0.2337 | watch_only | none |
| 19 | MRVL | custom_silicon_networking | 174.465 |  | 174.2076 | 0.1478 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | GOOGL | cloud_ai_capex | 335.315 |  | 330.9891 | 1.307 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.07 |  | 196.0907 | 0.4994 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.69 |  | 387.7881 | 1.0062 | 390.46 | 382.495 | 0.0357 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 381.31 |  | 378.6375 | 0.7058 | 378.64 | 371.57 | 0.1652 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.51 |  | 739.599 | 0.2584 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.315 |  | 330.9891 | 1.307 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 168.32 |  | 165.0814 | 1.9618 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 140.09 |  | 138.6321 | 1.0517 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ETN | data_center_power_cooling | 384.94 |  | 381.3159 | 0.9504 | 384.565 | 377.43 | 2.6861 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ORCL | cloud_ai_capex | 121.18 |  | 118.6036 | 2.1723 | 117.17 | 115.25 | 0.7427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMH | semiconductor_index | 529.62 |  | 527.3865 | 0.4235 | 533.01 | 523.325 | 0.0227 | watch_only | none |
| 11 | SOXX | semiconductor_index | 491.39 |  | 489.9899 | 0.2857 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| 12 | QQQ | market_regime | 676.64 |  | 674.1833 | 0.3644 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| 13 | ASML | semiconductor_equipment | 1582.185 |  | 1577.3592 | 0.3059 | 1586.01 | 1565.95 | 0.1138 | watch_only | none |
| 14 | VRT | data_center_power_cooling | 266.42 |  | 266.1384 | 0.1058 | 273.86 | 266.04 | 0.1989 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 586.14 |  | 582.4792 | 0.6285 | 603.25 | 584.69 | 0.2337 | watch_only | none |
| 16 | IWM | market_regime | 293.09 |  | 292.3966 | 0.2371 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 17 | KLAC | semiconductor_equipment | 191.615 |  | 190.7897 | 0.4326 | 194.96 | 189.48 | 0.0261 | watch_only | none |
| 18 | META | cloud_ai_capex | 594.265 |  | 593.8254 | 0.074 | 600.765 | 594.21 | 0.0825 | watch_only | none |
| 19 | TER | semiconductor_test_packaging | 312.37 |  | 308.7573 | 1.1701 | 315.21 | 304.11 | 0.0832 | watch_only | none |
| 20 | MSFT | cloud_ai_capex | 396.82 |  | 396.4119 | 0.1029 | 400.09 | 392.355 | 0.0428 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.64 |  | 674.1833 | 0.3644 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| TQQQ | leveraged_tool | 61.83 |  | 61.1238 | 1.1553 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.07 |  | 196.0907 | 0.4994 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.82 |  | 396.4119 | 0.1029 | 400.09 | 392.355 | 0.0428 | watch_only | none |
| AAPL | mega_cap_platform | 339.43 |  | 338.9591 | 0.1389 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.315 |  | 330.9891 | 1.307 | 330.21 | 324.97 | 0.0179 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.385 |  | 455.5437 | 0.1847 | 472.485 | 453.76 | 2.6863 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.69 |  | 387.7881 | 1.0062 | 390.46 | 382.495 | 0.0357 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.39 |  | 489.9899 | 0.2857 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| SMH | semiconductor_index | 529.62 |  | 527.3865 | 0.4235 | 533.01 | 523.325 | 0.0227 | watch_only | none |
| AVGO | custom_silicon_networking | 381.31 |  | 378.6375 | 0.7058 | 378.64 | 371.57 | 0.1652 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 821.66 |  | 815.5534 | 0.7488 | 846.4 | 813.91 | 1.3388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 174.465 |  | 174.2076 | 0.1478 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 386.71 |  | 375.3143 | 3.0363 | 402 | 374.02 | 0.2793 | watch_only | none |
| HPE | ai_server_oem | 44.61 |  | 44.4424 | 0.3771 | 46.19 | 44.33 | 0.0448 | watch_only | none |
| SMCI | ai_server_oem | 28.2 |  | 28.0052 | 0.6958 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| SPY | market_regime | 741.51 |  | 739.599 | 0.2584 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.09 |  | 292.3966 | 0.2371 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 121.18 |  | 118.6036 | 2.1723 | 117.17 | 115.25 | 0.7427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.34 |  | 66.2604 | 0.1201 | 68.995 | 65.635 | 4.1453 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.42 |  | 266.1384 | 0.1058 | 273.86 | 266.04 | 0.1989 | watch_only | none |
| ETN | data_center_power_cooling | 384.94 |  | 381.3159 | 0.9504 | 384.565 | 377.43 | 2.6861 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 586.14 |  | 582.4792 | 0.6285 | 603.25 | 584.69 | 0.2337 | watch_only | none |
| GEV | data_center_power_cooling | 935.13 |  | 937.5375 | -0.2568 | 955.825 | 935.665 | 1.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 467.48 |  | 465.2947 | 0.4697 | 477.73 | 460.77 | 4.8344 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.09 |  | 138.6321 | 1.0517 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.32 |  | 165.0814 | 1.9618 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 241.18 |  | 237.5176 | 1.5419 | 256.145 | 236.73 | 4.706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 642.95 |  | 632.3515 | 1.676 | 673.65 | 624.91 | 4.7749 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.93 |  | 337.4721 | 1.0247 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.3 |  | 85.8485 | 1.6907 | 92.95 | 84.63 | 3.9977 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 260.91 |  | 259.1065 | 0.696 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1582.185 |  | 1577.3592 | 0.3059 | 1586.01 | 1565.95 | 0.1138 | watch_only | none |
| AMAT | semiconductor_equipment | 476.32 |  | 476.3284 | -0.0018 | 494.87 | 477.03 | 4.7069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.53 |  | 266.6954 | 1.4378 | 276.85 | 267.14 | 4.4357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.615 |  | 190.7897 | 0.4326 | 194.96 | 189.48 | 0.0261 | watch_only | none |
| TER | semiconductor_test_packaging | 312.37 |  | 308.7573 | 1.1701 | 315.21 | 304.11 | 0.0832 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.445 |  | 236.8219 | 0.6854 | 248.8 | 236.42 | 0.3774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.41 |  | 46.6836 | -2.7281 | 51.64 | 47.435 | 0.8148 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.995 |  | 42.4376 | -1.043 | 44.155 | 41.78 | 0.4762 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 118.685 |  | 119.1598 | -0.3984 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 282.42 |  | 282.3579 | 0.022 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.46 |  | 518.0811 | -0.3129 | 518.6 | 511.495 | 4.7361 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.51 |  | 295.745 | -0.0795 | 297.25 | 293.555 | 0.1184 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.18 |  | 26.5135 | -1.2578 | 27 | 25.42 | 2.903 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.485 |  | 33.7075 | -0.6601 | 35.08 | 33.52 | 0.0299 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.91 |  | 20.1139 | 3.9577 | 20.97 | 19.755 | 0.0478 | watch_only | none |
| SNDK | memory_hbm_storage | 1087.055 |  | 1099.2917 | -1.1131 | 1185.19 | 1114.57 | 3.0173 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 455.99 |  | 440.1748 | 3.5929 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 748.01 |  | 732.4568 | 2.1234 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.19 |  | 230.5145 | 0.293 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594.265 |  | 593.8254 | 0.074 | 600.765 | 594.21 | 0.0825 | watch_only | none |
| ARM | ai_accelerator | 245 |  | 245.2096 | -0.0855 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.89 |  | 131.5281 | -0.4851 | 136.45 | 131.735 | 0.6723 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
