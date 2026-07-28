# Intraday State

- Generated at: `2026-07-29T03:55:15+08:00`
- Market time ET: `2026-07-28T15:55:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 17, 'manual_confirm_candidate': 7, 'below_vwap': 3, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 1, 'below_opening_15m_low': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.05 |  | 674.4698 | 0.3826 | 677.3 | 670.84 | 0.0044 | watch_only | none |
| SOXX | semiconductor_index | 495.34 |  | 490.6148 | 0.9631 | 497.64 | 485.42 | 0.0828 | watch_only | none |
| SMH | semiconductor_index | 533.25 |  | 528.0552 | 0.9838 | 533.01 | 523.325 | 0.0394 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 741.65 |  | 739.9175 | 0.2341 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198 |  | 196.293 | 0.8696 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 394.8 |  | 389.3157 | 1.4087 | 390.46 | 382.495 | 0.0633 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 533.25 |  | 528.0552 | 0.9838 | 533.01 | 523.325 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.65 |  | 739.9175 | 0.2341 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.86 |  | 331.7441 | 0.6378 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.585 |  | 139.2137 | 0.9851 | 139.755 | 137.31 | 0.0285 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.66 |  | 292.5188 | 0.3901 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.65 |  | 739.9175 | 0.2341 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.66 |  | 292.5188 | 0.3901 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 230.9 |  | 230.5833 | 0.1374 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 333.86 |  | 331.7441 | 0.6378 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 339.85 |  | 339.0396 | 0.239 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 6 | QQQ | market_regime | 677.05 |  | 674.4698 | 0.3826 | 677.3 | 670.84 | 0.0044 | watch_only | none |
| 7 | SMH | semiconductor_index | 533.25 |  | 528.0552 | 0.9838 | 533.01 | 523.325 | 0.0394 | buy_precheck_manual_confirm | none |
| 8 | GEV | data_center_power_cooling | 942.4 |  | 937.8417 | 0.486 | 955.825 | 935.665 | 0.1379 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 33.94 |  | 33.7436 | 0.5821 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| 10 | JCI | data_center_power_cooling | 140.585 |  | 139.2137 | 0.9851 | 139.755 | 137.31 | 0.0285 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 26.68 |  | 26.5394 | 0.5298 | 27 | 25.42 | 0.0375 | watch_only | none |
| 12 | NVDA | ai_accelerator | 198 |  | 196.293 | 0.8696 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 13 | TSM | foundry | 394.8 |  | 389.3157 | 1.4087 | 390.46 | 382.495 | 0.0633 | buy_precheck_manual_confirm | none |
| 14 | SOXX | semiconductor_index | 495.34 |  | 490.6148 | 0.9631 | 497.64 | 485.42 | 0.0828 | watch_only | none |
| 15 | VRT | data_center_power_cooling | 270.02 |  | 266.5062 | 1.3185 | 273.86 | 266.04 | 0.1222 | watch_only | none |
| 16 | COHU | semiconductor_test_packaging | 42.5 |  | 42.4785 | 0.0506 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ASML | semiconductor_equipment | 1590.65 |  | 1579.0584 | 0.7341 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SMCI | ai_server_oem | 28.485 |  | 28.0643 | 1.4991 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| 19 | CRWV | gpu_cloud_ai_factory | 67.25 |  | 66.3382 | 1.3745 | 68.995 | 65.635 | 0.0892 | watch_only | none |
| 20 | STX | memory_hbm_storage | 745.29 |  | 734.8117 | 1.426 | 774.805 | 719.02 | 0.1919 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198 |  | 196.293 | 0.8696 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 394.8 |  | 389.3157 | 1.4087 | 390.46 | 382.495 | 0.0633 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 533.25 |  | 528.0552 | 0.9838 | 533.01 | 523.325 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.65 |  | 739.9175 | 0.2341 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.86 |  | 331.7441 | 0.6378 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.585 |  | 139.2137 | 0.9851 | 139.755 | 137.31 | 0.0285 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.66 |  | 292.5188 | 0.3901 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 385.26 |  | 379.4067 | 1.5428 | 378.64 | 371.57 | 1.7702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1590.65 |  | 1579.0584 | 0.7341 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ANET | ai_networking_optical | 169.38 |  | 165.447 | 2.3772 | 165.975 | 160.51 | 4.7467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ETN | data_center_power_cooling | 387.28 |  | 381.9137 | 1.4051 | 384.565 | 377.43 | 2.657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ORCL | cloud_ai_capex | 120.33 |  | 119.0303 | 1.0919 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TER | semiconductor_test_packaging | 323.76 |  | 311.4916 | 3.9386 | 315.21 | 304.11 | 4.7165 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SOXX | semiconductor_index | 495.34 |  | 490.6148 | 0.9631 | 497.64 | 485.42 | 0.0828 | watch_only | none |
| 15 | QQQ | market_regime | 677.05 |  | 674.4698 | 0.3826 | 677.3 | 670.84 | 0.0044 | watch_only | none |
| 16 | STX | memory_hbm_storage | 745.29 |  | 734.8117 | 1.426 | 774.805 | 719.02 | 0.1919 | watch_only | none |
| 17 | VRT | data_center_power_cooling | 270.02 |  | 266.5062 | 1.3185 | 273.86 | 266.04 | 0.1222 | watch_only | none |
| 18 | GEV | data_center_power_cooling | 942.4 |  | 937.8417 | 0.486 | 955.825 | 935.665 | 0.1379 | watch_only | none |
| 19 | WDC | memory_hbm_storage | 461.68 |  | 443.5555 | 4.0862 | 465.04 | 435.22 | 0.0542 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 230.9 |  | 230.5833 | 0.1374 | 233.05 | 229.7 | 0.013 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.05 |  | 674.4698 | 0.3826 | 677.3 | 670.84 | 0.0044 | watch_only | none |
| TQQQ | leveraged_tool | 61.96 |  | 61.1989 | 1.2437 | 62.01 | 60.23 | 0.0323 | watch_only | none |
| NVDA | ai_accelerator | 198 |  | 196.293 | 0.8696 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.41 |  | 396.0359 | -0.663 | 400.09 | 392.355 | 0.2694 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 339.85 |  | 339.0396 | 0.239 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.86 |  | 331.7441 | 0.6378 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.08 |  | 456.1356 | 0.4263 | 472.485 | 453.76 | 2.3009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 394.8 |  | 389.3157 | 1.4087 | 390.46 | 382.495 | 0.0633 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.34 |  | 490.6148 | 0.9631 | 497.64 | 485.42 | 0.0828 | watch_only | none |
| SMH | semiconductor_index | 533.25 |  | 528.0552 | 0.9838 | 533.01 | 523.325 | 0.0394 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.26 |  | 379.4067 | 1.5428 | 378.64 | 371.57 | 1.7702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 822.19 |  | 816.7188 | 0.6699 | 846.4 | 813.91 | 2.5298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.45 |  | 174.4177 | 1.1652 | 181.24 | 172.395 | 0.1814 | watch_only | none |
| DELL | ai_server_oem | 393.04 |  | 377.1803 | 4.2048 | 402 | 374.02 | 2.0023 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.53 |  | 44.7326 | 1.7825 | 46.19 | 44.33 | 0.0659 | watch_only | none |
| SMCI | ai_server_oem | 28.485 |  | 28.0643 | 1.4991 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 741.65 |  | 739.9175 | 0.2341 | 739.42 | 736.57 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.66 |  | 292.5188 | 0.3901 | 293.26 | 291.55 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.33 |  | 119.0303 | 1.0919 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 67.25 |  | 66.3382 | 1.3745 | 68.995 | 65.635 | 0.0892 | watch_only | none |
| VRT | data_center_power_cooling | 270.02 |  | 266.5062 | 1.3185 | 273.86 | 266.04 | 0.1222 | watch_only | none |
| ETN | data_center_power_cooling | 387.28 |  | 381.9137 | 1.4051 | 384.565 | 377.43 | 2.657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 588.785 |  | 583.6287 | 0.8835 | 603.25 | 584.69 | 5.0018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 942.4 |  | 937.8417 | 0.486 | 955.825 | 935.665 | 0.1379 | watch_only | none |
| TT | data_center_power_cooling | 470.525 |  | 466.2811 | 0.9102 | 477.73 | 460.77 | 4.0614 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.585 |  | 139.2137 | 0.9851 | 139.755 | 137.31 | 0.0285 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169.38 |  | 165.447 | 2.3772 | 165.975 | 160.51 | 4.7467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 244.59 |  | 238.7541 | 2.4443 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 653.64 |  | 635.2223 | 2.8994 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 349.95 |  | 338.6716 | 3.3302 | 354.09 | 338.14 | 3.5291 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.375 |  | 86.2237 | 2.495 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 264.54 |  | 260.0392 | 1.7308 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1590.65 |  | 1579.0584 | 0.7341 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 480.795 |  | 477.0735 | 0.7801 | 494.87 | 477.03 | 0.4742 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 271.72 |  | 267.4895 | 1.5816 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 194.92 |  | 191.3968 | 1.8408 | 194.96 | 189.48 | 3.2321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 323.76 |  | 311.4916 | 3.9386 | 315.21 | 304.11 | 4.7165 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 241.65 |  | 237.4717 | 1.7595 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.11 |  | 46.6109 | -1.0747 | 51.64 | 47.435 | 2.6025 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.5 |  | 42.4785 | 0.0506 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 119.62 |  | 119.1924 | 0.3587 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 286.12 |  | 282.8096 | 1.1706 | 296.8 | 283.22 | 0.1782 | watch_only | none |
| LIN | industrial_gases | 511.015 |  | 517.5124 | -1.2555 | 518.6 | 511.495 | 4.8316 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.66 |  | 295.5526 | -0.6404 | 297.25 | 293.555 | 4.8526 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.68 |  | 26.5394 | 0.5298 | 27 | 25.42 | 0.0375 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.94 |  | 33.7436 | 0.5821 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.815 |  | 20.2309 | 2.8873 | 20.97 | 19.755 | 0.0961 | watch_only | none |
| SNDK | memory_hbm_storage | 1102.67 |  | 1101.2702 | 0.1271 | 1185.19 | 1114.57 | 0.0907 | below_opening_15m_low | below_opening_15m_low |
| WDC | memory_hbm_storage | 461.68 |  | 443.5555 | 4.0862 | 465.04 | 435.22 | 0.0542 | watch_only | none |
| STX | memory_hbm_storage | 745.29 |  | 734.8117 | 1.426 | 774.805 | 719.02 | 0.1919 | watch_only | none |
| AMZN | cloud_ai_capex | 230.9 |  | 230.5833 | 0.1374 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594 |  | 593.8351 | 0.0278 | 600.765 | 594.21 | 0.2189 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 246.035 |  | 245.2839 | 0.3062 | 253.38 | 243.72 | 0.4633 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 130.02 |  | 131.5025 | -1.1274 | 136.45 | 131.735 | 0.6999 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
