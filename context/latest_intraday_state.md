# Intraday State

- Generated at: `2026-07-29T03:01:32+08:00`
- Market time ET: `2026-07-28T15:01:33-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 15, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.2 |  | 674.2001 | 0.445 | 677.3 | 670.84 | 0.0517 | watch_only | none |
| SOXX | semiconductor_index | 492.81 |  | 489.9944 | 0.5746 | 497.64 | 485.42 | 0.069 | watch_only | none |
| SMH | semiconductor_index | 530.955 |  | 527.4039 | 0.6733 | 533.01 | 523.325 | 0.0245 | watch_only | none |
| SPY | market_regime | 741.64 |  | 739.6078 | 0.2748 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.38 |  | 196.1039 | 0.6507 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.64 |  | 739.6078 | 0.2748 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 335.31 |  | 331.0317 | 1.2924 | 330.21 | 324.97 | 0.0925 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 121.82 |  | 118.6264 | 2.6922 | 117.17 | 115.25 | 0.0575 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.1286 | 4.5775 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.64 |  | 739.6078 | 0.2748 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.02 |  | 292.4034 | 0.2109 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 3 | NVDA | ai_accelerator | 197.38 |  | 196.1039 | 0.6507 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 396.82 |  | 396.418 | 0.1014 | 400.09 | 392.355 | 0.1436 | watch_only | none |
| 5 | AMZN | cloud_ai_capex | 231.24 |  | 230.5193 | 0.3126 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 339.415 |  | 338.9633 | 0.1333 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 7 | SMH | semiconductor_index | 530.955 |  | 527.4039 | 0.6733 | 533.01 | 523.325 | 0.0245 | watch_only | none |
| 8 | SOXX | semiconductor_index | 492.81 |  | 489.9944 | 0.5746 | 497.64 | 485.42 | 0.069 | watch_only | none |
| 9 | QQQ | market_regime | 677.2 |  | 674.2001 | 0.445 | 677.3 | 670.84 | 0.0517 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 192.31 |  | 190.7969 | 0.793 | 194.96 | 189.48 | 0.0936 | watch_only | none |
| 11 | PWR | data_center_power_cooling | 586.85 |  | 582.5446 | 0.7391 | 603.25 | 584.69 | 0.2607 | watch_only | none |
| 12 | AMAT | semiconductor_equipment | 478.18 |  | 476.3362 | 0.3871 | 494.87 | 477.03 | 0.3032 | watch_only | none |
| 13 | MU | memory_hbm_storage | 824.915 |  | 815.6029 | 1.1417 | 846.4 | 813.91 | 0.0473 | watch_only | none |
| 14 | ARM | ai_accelerator | 245.535 |  | 245.2096 | 0.1327 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | GOOGL | cloud_ai_capex | 335.31 |  | 331.0317 | 1.2924 | 330.21 | 324.97 | 0.0925 | buy_precheck_manual_confirm | none |
| 16 | HPE | ai_server_oem | 44.96 |  | 44.4474 | 1.1533 | 46.19 | 44.33 | 0.089 | watch_only | none |
| 17 | SMCI | ai_server_oem | 28.335 |  | 28.0062 | 1.1741 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 18 | ASML | semiconductor_equipment | 1585.04 |  | 1577.3811 | 0.4855 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | VRT | data_center_power_cooling | 266.86 |  | 266.1418 | 0.2699 | 273.86 | 266.04 | 2.6456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.1286 | 4.5775 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.38 |  | 196.1039 | 0.6507 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.64 |  | 739.6078 | 0.2748 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 335.31 |  | 331.0317 | 1.2924 | 330.21 | 324.97 | 0.0925 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 121.82 |  | 118.6264 | 2.6922 | 117.17 | 115.25 | 0.0575 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.1286 | 4.5775 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 392.7 |  | 387.8151 | 1.2596 | 390.46 | 382.495 | 0.9651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AVGO | custom_silicon_networking | 382.35 |  | 378.6525 | 0.9765 | 378.64 | 371.57 | 2.0792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 168.98 |  | 165.1103 | 2.3437 | 165.975 | 160.51 | 3.3436 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | JCI | data_center_power_cooling | 140.44 |  | 138.6605 | 1.2834 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 385.26 |  | 381.3243 | 1.0321 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MU | memory_hbm_storage | 824.915 |  | 815.6029 | 1.1417 | 846.4 | 813.91 | 0.0473 | watch_only | none |
| 12 | SMH | semiconductor_index | 530.955 |  | 527.4039 | 0.6733 | 533.01 | 523.325 | 0.0245 | watch_only | none |
| 13 | SOXX | semiconductor_index | 492.81 |  | 489.9944 | 0.5746 | 497.64 | 485.42 | 0.069 | watch_only | none |
| 14 | QQQ | market_regime | 677.2 |  | 674.2001 | 0.445 | 677.3 | 670.84 | 0.0517 | watch_only | none |
| 15 | STX | memory_hbm_storage | 749.9 |  | 732.6288 | 2.3574 | 774.805 | 719.02 | 0.1627 | watch_only | none |
| 16 | PWR | data_center_power_cooling | 586.85 |  | 582.5446 | 0.7391 | 603.25 | 584.69 | 0.2607 | watch_only | none |
| 17 | IWM | market_regime | 293.02 |  | 292.4034 | 0.2109 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 18 | AMAT | semiconductor_equipment | 478.18 |  | 476.3362 | 0.3871 | 494.87 | 477.03 | 0.3032 | watch_only | none |
| 19 | KLAC | semiconductor_equipment | 192.31 |  | 190.7969 | 0.793 | 194.96 | 189.48 | 0.0936 | watch_only | none |
| 20 | MSFT | cloud_ai_capex | 396.82 |  | 396.418 | 0.1014 | 400.09 | 392.355 | 0.1436 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.2 |  | 674.2001 | 0.445 | 677.3 | 670.84 | 0.0517 | watch_only | none |
| TQQQ | leveraged_tool | 62 |  | 61.1307 | 1.422 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.38 |  | 196.1039 | 0.6507 | 195.4 | 193.65 | 0.0253 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.82 |  | 396.418 | 0.1014 | 400.09 | 392.355 | 0.1436 | watch_only | none |
| AAPL | mega_cap_platform | 339.415 |  | 338.9633 | 0.1333 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.31 |  | 331.0317 | 1.2924 | 330.21 | 324.97 | 0.0925 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.35 |  | 455.5568 | 0.6131 | 472.485 | 453.76 | 1.7956 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.7 |  | 387.8151 | 1.2596 | 390.46 | 382.495 | 0.9651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 492.81 |  | 489.9944 | 0.5746 | 497.64 | 485.42 | 0.069 | watch_only | none |
| SMH | semiconductor_index | 530.955 |  | 527.4039 | 0.6733 | 533.01 | 523.325 | 0.0245 | watch_only | none |
| AVGO | custom_silicon_networking | 382.35 |  | 378.6525 | 0.9765 | 378.64 | 371.57 | 2.0792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 824.915 |  | 815.6029 | 1.1417 | 846.4 | 813.91 | 0.0473 | watch_only | none |
| MRVL | custom_silicon_networking | 175.07 |  | 174.2107 | 0.4933 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 387.67 |  | 375.3534 | 3.2813 | 402 | 374.02 | 3.1083 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.96 |  | 44.4474 | 1.1533 | 46.19 | 44.33 | 0.089 | watch_only | none |
| SMCI | ai_server_oem | 28.335 |  | 28.0062 | 1.1741 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.64 |  | 739.6078 | 0.2748 | 739.42 | 736.57 | 0.0189 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.02 |  | 292.4034 | 0.2109 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 121.82 |  | 118.6264 | 2.6922 | 117.17 | 115.25 | 0.0575 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.56 |  | 66.261 | 0.4513 | 68.995 | 65.635 | 2.9748 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.86 |  | 266.1418 | 0.2699 | 273.86 | 266.04 | 2.6456 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.26 |  | 381.3243 | 1.0321 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 586.85 |  | 582.5446 | 0.7391 | 603.25 | 584.69 | 0.2607 | watch_only | none |
| GEV | data_center_power_cooling | 936.055 |  | 937.5181 | -0.1561 | 955.825 | 935.665 | 0.0662 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 467.83 |  | 465.3393 | 0.5352 | 477.73 | 460.77 | 4.8308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.44 |  | 138.6605 | 1.2834 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.98 |  | 165.1103 | 2.3437 | 165.975 | 160.51 | 3.3436 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 241.45 |  | 237.5596 | 1.6376 | 256.145 | 236.73 | 4.7877 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 645 |  | 632.3758 | 1.9963 | 673.65 | 624.91 | 4.5566 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 342.13 |  | 337.4911 | 1.3745 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.43 |  | 85.8499 | 1.8405 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.58 |  | 259.1421 | 0.9408 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1585.04 |  | 1577.3811 | 0.4855 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 478.18 |  | 476.3362 | 0.3871 | 494.87 | 477.03 | 0.3032 | watch_only | none |
| LRCX | semiconductor_equipment | 271.47 |  | 266.7257 | 1.7787 | 276.85 | 267.14 | 1.4698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 192.31 |  | 190.7969 | 0.793 | 194.96 | 189.48 | 0.0936 | watch_only | none |
| TER | semiconductor_test_packaging | 314.61 |  | 308.8212 | 1.8745 | 315.21 | 304.11 | 4.504 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 238.41 |  | 236.8408 | 0.6625 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.03 |  | 46.6758 | -1.3835 | 51.64 | 47.435 | 4.4102 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.31 |  | 42.4355 | -0.2959 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.33 |  | 119.159 | 0.1435 | 121 | 117.72 | 4.7934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 283.35 |  | 282.3622 | 0.3498 | 296.8 | 283.22 | 4.5668 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 516.17 |  | 518.0701 | -0.3668 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.205 |  | 295.7432 | -0.182 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.29 |  | 26.5122 | -0.8382 | 27 | 25.42 | 0.1521 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.68 |  | 33.707 | -0.08 | 35.08 | 33.52 | 0.0594 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.05 |  | 20.1286 | 4.5775 | 20.97 | 19.755 | 0.0475 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1096.755 |  | 1099.2163 | -0.2239 | 1185.19 | 1114.57 | 1.9676 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 457.27 |  | 440.3481 | 3.8428 | 465.04 | 435.22 | 0.9775 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 749.9 |  | 732.6288 | 2.3574 | 774.805 | 719.02 | 0.1627 | watch_only | none |
| AMZN | cloud_ai_capex | 231.24 |  | 230.5193 | 0.3126 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.99 |  | 593.8334 | 0.1948 | 600.765 | 594.21 | 0.3563 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 245.535 |  | 245.2096 | 0.1327 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 131.21 |  | 131.5257 | -0.24 | 136.45 | 131.735 | 3.2772 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
