# Intraday State

- Generated at: `2026-07-29T00:47:24+08:00`
- Market time ET: `2026-07-28T12:47:25-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 6, 'watch_only': 14, 'spread_too_wide_or_missing': 29, 'price_stale_or_missing': 2, 'below_vwap': 2, 'below_opening_15m_low': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.35 |  | 673.6286 | 0.5524 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 493.68 |  | 489.6422 | 0.8246 | 497.64 | 485.42 | 0.0689 | watch_only | none |
| SMH | semiconductor_index | 531.33 |  | 526.9689 | 0.8276 | 533.01 | 523.325 | 0.0376 | watch_only | none |
| SPY | market_regime | 741.45 |  | 739.0678 | 0.3223 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.465 |  | 195.7132 | 0.8951 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 382.52 |  | 378.1616 | 1.1525 | 378.64 | 371.57 | 0.0575 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.45 |  | 739.0678 | 0.3223 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 677.35 |  | 673.6286 | 0.5524 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.515 |  | 329.3884 | 1.2528 | 330.21 | 324.97 | 0.1499 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 62.04 |  | 60.9312 | 1.8197 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.45 |  | 739.0678 | 0.3223 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 677.35 |  | 673.6286 | 0.5524 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 292.88 |  | 292.109 | 0.264 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.05 |  | 338.8319 | 0.0644 | 342.87 | 337.78 | 0.0354 | watch_only | none |
| 5 | AMZN | cloud_ai_capex | 231.25 |  | 230.1701 | 0.4692 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 6 | PWR | data_center_power_cooling | 585.59 |  | 581.2964 | 0.7386 | 603.25 | 584.69 | 0.1759 | watch_only | none |
| 7 | KLAC | semiconductor_equipment | 191.83 |  | 190.5436 | 0.6751 | 194.96 | 189.48 | 0.1616 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 398.04 |  | 396.0181 | 0.5105 | 400.09 | 392.355 | 0.2512 | watch_only | none |
| 9 | NVDA | ai_accelerator | 197.465 |  | 195.7132 | 0.8951 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 10 | AVGO | custom_silicon_networking | 382.52 |  | 378.1616 | 1.1525 | 378.64 | 371.57 | 0.0575 | buy_precheck_manual_confirm | none |
| 11 | GOOGL | cloud_ai_capex | 333.515 |  | 329.3884 | 1.2528 | 330.21 | 324.97 | 0.1499 | buy_precheck_manual_confirm | none |
| 12 | LIN | industrial_gases | 519.035 |  | 518.5617 | 0.0913 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | APD | industrial_gases | 296.015 |  | 295.9067 | 0.0366 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SMH | semiconductor_index | 531.33 |  | 526.9689 | 0.8276 | 533.01 | 523.325 | 0.0376 | watch_only | none |
| 15 | SOXX | semiconductor_index | 493.68 |  | 489.6422 | 0.8246 | 497.64 | 485.42 | 0.0689 | watch_only | none |
| 16 | HPE | ai_server_oem | 44.85 |  | 44.4244 | 0.9579 | 46.19 | 44.33 | 0.0669 | watch_only | none |
| 17 | SMCI | ai_server_oem | 28.31 |  | 27.9047 | 1.4523 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 18 | IREN | high_beta_ai_infrastructure | 34.08 |  | 33.6805 | 1.1862 | 35.08 | 33.52 | 0.088 | watch_only | none |
| 19 | CORZ | high_beta_ai_infrastructure | 20.22 |  | 19.9986 | 1.1069 | 20.97 | 19.755 | 0.0495 | watch_only | none |
| 20 | SKHY | memory_hbm_storage | 132.83 |  | 131.5881 | 0.9438 | 136.45 | 131.735 | 0.2334 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.465 |  | 195.7132 | 0.8951 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 382.52 |  | 378.1616 | 1.1525 | 378.64 | 371.57 | 0.0575 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.45 |  | 739.0678 | 0.3223 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 677.35 |  | 673.6286 | 0.5524 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.515 |  | 329.3884 | 1.2528 | 330.21 | 324.97 | 0.1499 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 62.04 |  | 60.9312 | 1.8197 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 391.48 |  | 386.9966 | 1.1585 | 390.46 | 382.495 | 1.0345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 167.46 |  | 163.825 | 2.2189 | 165.975 | 160.51 | 4.5026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ETN | data_center_power_cooling | 385.2 |  | 380.0163 | 1.3641 | 384.565 | 377.43 | 4.1485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | LIN | industrial_gases | 519.035 |  | 518.5617 | 0.0913 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ORCL | cloud_ai_capex | 120.58 |  | 117.7274 | 2.4231 | 117.17 | 115.25 | 1.1611 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SMH | semiconductor_index | 531.33 |  | 526.9689 | 0.8276 | 533.01 | 523.325 | 0.0376 | watch_only | none |
| 13 | SOXX | semiconductor_index | 493.68 |  | 489.6422 | 0.8246 | 497.64 | 485.42 | 0.0689 | watch_only | none |
| 14 | PWR | data_center_power_cooling | 585.59 |  | 581.2964 | 0.7386 | 603.25 | 584.69 | 0.1759 | watch_only | none |
| 15 | IWM | market_regime | 292.88 |  | 292.109 | 0.264 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 16 | SKHY | memory_hbm_storage | 132.83 |  | 131.5881 | 0.9438 | 136.45 | 131.735 | 0.2334 | watch_only | none |
| 17 | KLAC | semiconductor_equipment | 191.83 |  | 190.5436 | 0.6751 | 194.96 | 189.48 | 0.1616 | watch_only | none |
| 18 | LITE | ai_networking_optical | 648.78 |  | 628.9493 | 3.153 | 673.65 | 624.91 | 0.1603 | watch_only | none |
| 19 | MSFT | cloud_ai_capex | 398.04 |  | 396.0181 | 0.5105 | 400.09 | 392.355 | 0.2512 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 231.25 |  | 230.1701 | 0.4692 | 233.05 | 229.7 | 0.0173 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.35 |  | 673.6286 | 0.5524 | 677.3 | 670.84 | 0.0251 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.04 |  | 60.9312 | 1.8197 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.465 |  | 195.7132 | 0.8951 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.04 |  | 396.0181 | 0.5105 | 400.09 | 392.355 | 0.2512 | watch_only | none |
| AAPL | mega_cap_platform | 339.05 |  | 338.8319 | 0.0644 | 342.87 | 337.78 | 0.0354 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.515 |  | 329.3884 | 1.2528 | 330.21 | 324.97 | 0.1499 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 459.395 |  | 454.9459 | 0.9779 | 472.485 | 453.76 | 3.226 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.48 |  | 386.9966 | 1.1585 | 390.46 | 382.495 | 1.0345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.68 |  | 489.6422 | 0.8246 | 497.64 | 485.42 | 0.0689 | watch_only | none |
| SMH | semiconductor_index | 531.33 |  | 526.9689 | 0.8276 | 533.01 | 523.325 | 0.0376 | watch_only | none |
| AVGO | custom_silicon_networking | 382.52 |  | 378.1616 | 1.1525 | 378.64 | 371.57 | 0.0575 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 820.475 |  | 814.4464 | 0.7402 | 846.4 | 813.91 | 1.3736 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 177.455 |  | 173.8319 | 2.0843 | 181.24 | 172.395 | 0.5635 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 384.56 |  | 374.1154 | 2.7918 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.85 |  | 44.4244 | 0.9579 | 46.19 | 44.33 | 0.0669 | watch_only | none |
| SMCI | ai_server_oem | 28.31 |  | 27.9047 | 1.4523 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.45 |  | 739.0678 | 0.3223 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.88 |  | 292.109 | 0.264 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.58 |  | 117.7274 | 2.4231 | 117.17 | 115.25 | 1.1611 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.98 |  | 66.0969 | 1.3361 | 68.995 | 65.635 | 1.5378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.175 |  | 266.1644 | 0.3797 | 273.86 | 266.04 | 0.3518 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.2 |  | 380.0163 | 1.3641 | 384.565 | 377.43 | 4.1485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 585.59 |  | 581.2964 | 0.7386 | 603.25 | 584.69 | 0.1759 | watch_only | none |
| GEV | data_center_power_cooling | 945.055 |  | 936.7592 | 0.8856 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 467.495 |  | 464.7568 | 0.5892 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.245 |  | 138.2306 | 0.7338 | 139.755 | 137.31 | 3.9714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.46 |  | 163.825 | 2.2189 | 165.975 | 160.51 | 4.5026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 240.47 |  | 236.2217 | 1.7984 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 648.78 |  | 628.9493 | 3.153 | 673.65 | 624.91 | 0.1603 | watch_only | none |
| CIEN | ai_networking_optical | 342.2 |  | 336.6808 | 1.6393 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 88.46 |  | 85.5076 | 3.4528 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 266.18 |  | 258.5908 | 2.9348 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1582.34 |  | 1576.2518 | 0.3862 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 476.36 |  | 476.9762 | -0.1292 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 268.78 |  | 266.0039 | 1.0436 | 276.85 | 267.14 | 4.1261 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.83 |  | 190.5436 | 0.6751 | 194.96 | 189.48 | 0.1616 | watch_only | none |
| TER | semiconductor_test_packaging | 311.81 |  | 307.7183 | 1.3297 | 315.21 | 304.11 | 3.0275 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 237.14 |  | 236.4827 | 0.2779 | 248.8 | 236.42 | 4.6386 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.06 |  | 46.8318 | -1.6479 | 51.64 | 47.435 | 4.4724 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.03 |  | 42.5236 | -1.1607 | 44.155 | 41.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 119.22 |  | 119.4313 | -0.1769 | 121 | 117.72 | 4.8901 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 285.34 |  | 282.0641 | 1.1614 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 519.035 |  | 518.5617 | 0.0913 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.015 |  | 295.9067 | 0.0366 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.63 |  | 26.5356 | 0.3558 | 27 | 25.42 | 2.178 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.08 |  | 33.6805 | 1.1862 | 35.08 | 33.52 | 0.088 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.22 |  | 19.9986 | 1.1069 | 20.97 | 19.755 | 0.0495 | watch_only | none |
| SNDK | memory_hbm_storage | 1097.795 |  | 1102.6993 | -0.4448 | 1185.19 | 1114.57 | 0.9109 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.47 |  | 436.9175 | 4.4751 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 743.545 |  | 725.3518 | 2.5082 | 774.805 | 719.02 | 4.9856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.25 |  | 230.1701 | 0.4692 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.5 |  | 593.8218 | 0.1142 | 600.765 | 594.21 | 0.5517 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 246.99 |  | 245.1685 | 0.743 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.83 |  | 131.5881 | 0.9438 | 136.45 | 131.735 | 0.2334 | watch_only | none |
