# Intraday State

- Generated at: `2026-07-29T03:59:06+08:00`
- Market time ET: `2026-07-28T15:59:07-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 21, 'manual_confirm_candidate': 7, 'below_vwap': 6, 'below_opening_15m_low': 6, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 15}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.95 |  | 674.5074 | 0.2139 | 677.3 | 670.84 | 0.0148 | watch_only | none |
| SOXX | semiconductor_index | 492.09 |  | 490.7343 | 0.2763 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| SMH | semiconductor_index | 530.25 |  | 528.1111 | 0.405 | 533.01 | 523.325 | 0.0585 | watch_only | none |
| SPY | market_regime | 741.12 |  | 739.9641 | 0.1562 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.42 |  | 196.3359 | 0.5522 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.865 |  | 389.4599 | 1.1311 | 390.46 | 382.495 | 0.0254 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 381.78 |  | 379.5151 | 0.5968 | 378.64 | 371.57 | 0.0786 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.12 |  | 739.9641 | 0.1562 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.71 |  | 331.8088 | 0.573 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.65 |  | 139.3788 | 0.9121 | 139.755 | 137.31 | 0.0284 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.46 |  | 292.548 | 0.3117 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.12 |  | 739.9641 | 0.1562 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.46 |  | 292.548 | 0.3117 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 492.09 |  | 490.7343 | 0.2763 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| 4 | QQQ | market_regime | 675.95 |  | 674.5074 | 0.2139 | 677.3 | 670.84 | 0.0148 | watch_only | none |
| 5 | ASML | semiconductor_equipment | 1584.49 |  | 1579.1967 | 0.3352 | 1586.01 | 1565.95 | 0.0429 | watch_only | none |
| 6 | AMAT | semiconductor_equipment | 477.495 |  | 477.1047 | 0.0818 | 494.87 | 477.03 | 0.0817 | watch_only | none |
| 7 | NVDA | ai_accelerator | 197.42 |  | 196.3359 | 0.5522 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 230.91 |  | 230.6003 | 0.1343 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| 9 | AVGO | custom_silicon_networking | 381.78 |  | 379.5151 | 0.5968 | 378.64 | 371.57 | 0.0786 | buy_precheck_manual_confirm | none |
| 10 | GOOGL | cloud_ai_capex | 333.71 |  | 331.8088 | 0.573 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| 11 | SMH | semiconductor_index | 530.25 |  | 528.1111 | 0.405 | 533.01 | 523.325 | 0.0585 | watch_only | none |
| 12 | KLAC | semiconductor_equipment | 192.84 |  | 191.4989 | 0.7003 | 194.96 | 189.48 | 0.1037 | watch_only | none |
| 13 | IREN | high_beta_ai_infrastructure | 33.95 |  | 33.7479 | 0.5989 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| 14 | AAPL | mega_cap_platform | 340.4 |  | 339.076 | 0.3905 | 342.87 | 337.78 | 0.0617 | watch_only | none |
| 15 | GEV | data_center_power_cooling | 942.065 |  | 937.9621 | 0.4374 | 955.825 | 935.665 | 0.2123 | watch_only | none |
| 16 | JCI | data_center_power_cooling | 140.65 |  | 139.3788 | 0.9121 | 139.755 | 137.31 | 0.0284 | buy_precheck_manual_confirm | none |
| 17 | APLD | high_beta_ai_infrastructure | 26.64 |  | 26.5419 | 0.3696 | 27 | 25.42 | 0.0751 | watch_only | none |
| 18 | MKSI | semiconductor_materials | 284.97 |  | 282.905 | 0.7299 | 296.8 | 283.22 | 0.3018 | watch_only | none |
| 19 | TSM | foundry | 393.865 |  | 389.4599 | 1.1311 | 390.46 | 382.495 | 0.0254 | buy_precheck_manual_confirm | none |
| 20 | ALAB | ai_networking_optical | 260.46 |  | 260.1191 | 0.131 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.42 |  | 196.3359 | 0.5522 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.865 |  | 389.4599 | 1.1311 | 390.46 | 382.495 | 0.0254 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 381.78 |  | 379.5151 | 0.5968 | 378.64 | 371.57 | 0.0786 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.12 |  | 739.9641 | 0.1562 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.71 |  | 331.8088 | 0.573 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.65 |  | 139.3788 | 0.9121 | 139.755 | 137.31 | 0.0284 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.46 |  | 292.548 | 0.3117 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 169.09 |  | 165.5285 | 2.1516 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 386.695 |  | 382.0958 | 1.2037 | 384.565 | 377.43 | 2.511 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ORCL | cloud_ai_capex | 120.23 |  | 119.0671 | 0.9766 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TER | semiconductor_test_packaging | 321.68 |  | 311.8834 | 3.1411 | 315.21 | 304.11 | 4.6661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SMH | semiconductor_index | 530.25 |  | 528.1111 | 0.405 | 533.01 | 523.325 | 0.0585 | watch_only | none |
| 13 | SOXX | semiconductor_index | 492.09 |  | 490.7343 | 0.2763 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| 14 | QQQ | market_regime | 675.95 |  | 674.5074 | 0.2139 | 677.3 | 670.84 | 0.0148 | watch_only | none |
| 15 | ASML | semiconductor_equipment | 1584.49 |  | 1579.1967 | 0.3352 | 1586.01 | 1565.95 | 0.0429 | watch_only | none |
| 16 | TT | data_center_power_cooling | 470.625 |  | 466.5522 | 0.873 | 477.73 | 460.77 | 0.0659 | watch_only | none |
| 17 | VRT | data_center_power_cooling | 269.29 |  | 266.5563 | 1.0256 | 273.86 | 266.04 | 0.2228 | watch_only | none |
| 18 | GEV | data_center_power_cooling | 942.065 |  | 937.9621 | 0.4374 | 955.825 | 935.665 | 0.2123 | watch_only | none |
| 19 | WDC | memory_hbm_storage | 463.02 |  | 444.5465 | 4.1556 | 465.04 | 435.22 | 0.067 | watch_only | none |
| 20 | AMAT | semiconductor_equipment | 477.495 |  | 477.1047 | 0.0818 | 494.87 | 477.03 | 0.0817 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.95 |  | 674.5074 | 0.2139 | 677.3 | 670.84 | 0.0148 | watch_only | none |
| TQQQ | leveraged_tool | 61.655 |  | 61.214 | 0.7204 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.42 |  | 196.3359 | 0.5522 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.38 |  | 395.9768 | -0.6558 | 400.09 | 392.355 | 0.0229 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 340.4 |  | 339.076 | 0.3905 | 342.87 | 337.78 | 0.0617 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.71 |  | 331.8088 | 0.573 | 330.21 | 324.97 | 0.03 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 453.02 |  | 456.0854 | -0.6721 | 472.485 | 453.76 | 4.715 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 393.865 |  | 389.4599 | 1.1311 | 390.46 | 382.495 | 0.0254 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 492.09 |  | 490.7343 | 0.2763 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| SMH | semiconductor_index | 530.25 |  | 528.1111 | 0.405 | 533.01 | 523.325 | 0.0585 | watch_only | none |
| AVGO | custom_silicon_networking | 381.78 |  | 379.5151 | 0.5968 | 378.64 | 371.57 | 0.0786 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.71 |  | 816.7773 | 0.3591 | 846.4 | 813.91 | 2.5375 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 174.63 |  | 174.429 | 0.1152 | 181.24 | 172.395 | 3.2354 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 393.3 |  | 377.6672 | 4.1393 | 402 | 374.02 | 1.5001 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.565 |  | 44.7628 | 1.7921 | 46.19 | 44.33 | 0.0219 | watch_only | none |
| SMCI | ai_server_oem | 28.42 |  | 28.0746 | 1.2305 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 741.12 |  | 739.9641 | 0.1562 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.46 |  | 292.548 | 0.3117 | 293.26 | 291.55 | 0.0034 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.23 |  | 119.0671 | 0.9766 | 117.17 | 115.25 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 67.18 |  | 66.3517 | 1.2484 | 68.995 | 65.635 | 0.0744 | watch_only | none |
| VRT | data_center_power_cooling | 269.29 |  | 266.5563 | 1.0256 | 273.86 | 266.04 | 0.2228 | watch_only | none |
| ETN | data_center_power_cooling | 386.695 |  | 382.0958 | 1.2037 | 384.565 | 377.43 | 2.511 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 589.12 |  | 584.0285 | 0.8718 | 603.25 | 584.69 | 2.2627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 942.065 |  | 937.9621 | 0.4374 | 955.825 | 935.665 | 0.2123 | watch_only | none |
| TT | data_center_power_cooling | 470.625 |  | 466.5522 | 0.873 | 477.73 | 460.77 | 0.0659 | watch_only | none |
| JCI | data_center_power_cooling | 140.65 |  | 139.3788 | 0.9121 | 139.755 | 137.31 | 0.0284 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 169.09 |  | 165.5285 | 2.1516 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 243.48 |  | 238.8445 | 1.9408 | 256.145 | 236.73 | 4.5918 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 650.58 |  | 635.6011 | 2.3567 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 349.56 |  | 338.8974 | 3.1463 | 354.09 | 338.14 | 0.143 | watch_only | none |
| AAOI | ai_networking_optical | 88.01 |  | 86.2776 | 2.008 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.46 |  | 260.1191 | 0.131 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1584.49 |  | 1579.1967 | 0.3352 | 1586.01 | 1565.95 | 0.0429 | watch_only | none |
| AMAT | semiconductor_equipment | 477.495 |  | 477.1047 | 0.0818 | 494.87 | 477.03 | 0.0817 | watch_only | none |
| LRCX | semiconductor_equipment | 269.56 |  | 267.5821 | 0.7392 | 276.85 | 267.14 | 4.0102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 192.84 |  | 191.4989 | 0.7003 | 194.96 | 189.48 | 0.1037 | watch_only | none |
| TER | semiconductor_test_packaging | 321.68 |  | 311.8834 | 3.1411 | 315.21 | 304.11 | 4.6661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 241.5 |  | 237.5967 | 1.6428 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.785 |  | 46.5971 | -1.7428 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 42.45 |  | 42.4861 | -0.085 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.82 |  | 119.1899 | -0.3104 | 121 | 117.72 | 0.0926 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 284.97 |  | 282.905 | 0.7299 | 296.8 | 283.22 | 0.3018 | watch_only | none |
| LIN | industrial_gases | 511.59 |  | 517.2475 | -1.0938 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 293.34 |  | 295.3943 | -0.6954 | 297.25 | 293.555 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.64 |  | 26.5419 | 0.3696 | 27 | 25.42 | 0.0751 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.95 |  | 33.7479 | 0.5989 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.7 |  | 20.2408 | 2.2689 | 20.97 | 19.755 | 0.0483 | watch_only | none |
| SNDK | memory_hbm_storage | 1097.63 |  | 1101.2219 | -0.3262 | 1185.19 | 1114.57 | 0.1321 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| WDC | memory_hbm_storage | 463.02 |  | 444.5465 | 4.1556 | 465.04 | 435.22 | 0.067 | watch_only | none |
| STX | memory_hbm_storage | 744.82 |  | 735.0832 | 1.3246 | 774.805 | 719.02 | 0.4283 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.91 |  | 230.6003 | 0.1343 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| META | cloud_ai_capex | 593.84 |  | 593.8254 | 0.0025 | 600.765 | 594.21 | 0.0522 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 245.19 |  | 245.2751 | -0.0347 | 253.38 | 243.72 | 0.0979 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 129.63 |  | 131.4634 | -1.3946 | 136.45 | 131.735 | 0.0617 | below_opening_15m_low | below_opening_15m_low,below_vwap |
