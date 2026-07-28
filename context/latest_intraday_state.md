# Intraday State

- Generated at: `2026-07-28T23:32:56+08:00`
- Market time ET: `2026-07-28T11:32:57-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 18, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 2, 'below_vwap': 3, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.32 |  | 672.4255 | 0.5792 | 677.3 | 670.84 | 0.0547 | watch_only | none |
| SOXX | semiconductor_index | 490.51 |  | 488.604 | 0.3901 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| SMH | semiconductor_index | 529.39 |  | 525.9766 | 0.649 | 533.01 | 523.325 | 0.0888 | watch_only | none |
| SPY | market_regime | 741.105 |  | 738.3046 | 0.3793 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.77 |  | 195.0268 | 0.8938 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.225 |  | 376.709 | 0.9334 | 378.64 | 371.57 | 0.0947 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.105 |  | 738.3046 | 0.3793 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 332.41 |  | 328.1908 | 1.2856 | 330.21 | 324.97 | 0.0241 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.105 |  | 738.3046 | 0.3793 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 230.23 |  | 229.8881 | 0.1487 | 233.05 | 229.7 | 0.0565 | watch_only | none |
| 3 | ASML | semiconductor_equipment | 1573.22 |  | 1571.8141 | 0.0894 | 1586.01 | 1565.95 | 0.2873 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.315 |  | 338.5642 | 0.2217 | 342.87 | 337.78 | 0.0766 | watch_only | none |
| 5 | SMH | semiconductor_index | 529.39 |  | 525.9766 | 0.649 | 533.01 | 523.325 | 0.0888 | watch_only | none |
| 6 | SOXX | semiconductor_index | 490.51 |  | 488.604 | 0.3901 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| 7 | QQQ | market_regime | 676.32 |  | 672.4255 | 0.5792 | 677.3 | 670.84 | 0.0547 | watch_only | none |
| 8 | IWM | market_regime | 293.105 |  | 291.8602 | 0.4265 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 9 | KLAC | semiconductor_equipment | 190.66 |  | 189.9639 | 0.3664 | 194.96 | 189.48 | 0.0682 | watch_only | none |
| 10 | NVDA | ai_accelerator | 196.77 |  | 195.0268 | 0.8938 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 11 | AVGO | custom_silicon_networking | 380.225 |  | 376.709 | 0.9334 | 378.64 | 371.57 | 0.0947 | buy_precheck_manual_confirm | none |
| 12 | GOOGL | cloud_ai_capex | 332.41 |  | 328.1908 | 1.2856 | 330.21 | 324.97 | 0.0241 | buy_precheck_manual_confirm | none |
| 13 | TSM | foundry | 389.4 |  | 385.3378 | 1.0542 | 390.46 | 382.495 | 0.0847 | watch_only | none |
| 14 | HPE | ai_server_oem | 44.71 |  | 44.2576 | 1.0223 | 46.19 | 44.33 | 0.0671 | watch_only | none |
| 15 | CORZ | high_beta_ai_infrastructure | 20.19 |  | 19.93 | 1.3046 | 20.97 | 19.755 | 0.0991 | watch_only | none |
| 16 | STX | memory_hbm_storage | 724.24 |  | 722.8236 | 0.196 | 774.805 | 719.02 | 4.4557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TER | semiconductor_test_packaging | 308.73 |  | 305.8876 | 0.9292 | 315.21 | 304.11 | 0.3142 | watch_only | none |
| 18 | MSFT | cloud_ai_capex | 400.06 |  | 395.4452 | 1.167 | 400.09 | 392.355 | 0.1575 | watch_only | none |
| 19 | JCI | data_center_power_cooling | 138.65 |  | 137.9529 | 0.5053 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 455.19 |  | 452.9693 | 0.4903 | 472.485 | 453.76 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.77 |  | 195.0268 | 0.8938 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.225 |  | 376.709 | 0.9334 | 378.64 | 371.57 | 0.0947 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.105 |  | 738.3046 | 0.3793 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 332.41 |  | 328.1908 | 1.2856 | 330.21 | 324.97 | 0.0241 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.57 |  | 116.5938 | 3.4103 | 117.17 | 115.25 | 0.5308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | TSM | foundry | 389.4 |  | 385.3378 | 1.0542 | 390.46 | 382.495 | 0.0847 | watch_only | none |
| 7 | SMH | semiconductor_index | 529.39 |  | 525.9766 | 0.649 | 533.01 | 523.325 | 0.0888 | watch_only | none |
| 8 | SOXX | semiconductor_index | 490.51 |  | 488.604 | 0.3901 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| 9 | QQQ | market_regime | 676.32 |  | 672.4255 | 0.5792 | 677.3 | 670.84 | 0.0547 | watch_only | none |
| 10 | ASML | semiconductor_equipment | 1573.22 |  | 1571.8141 | 0.0894 | 1586.01 | 1565.95 | 0.2873 | watch_only | none |
| 11 | IWM | market_regime | 293.105 |  | 291.8602 | 0.4265 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 12 | KLAC | semiconductor_equipment | 190.66 |  | 189.9639 | 0.3664 | 194.96 | 189.48 | 0.0682 | watch_only | none |
| 13 | TER | semiconductor_test_packaging | 308.73 |  | 305.8876 | 0.9292 | 315.21 | 304.11 | 0.3142 | watch_only | none |
| 14 | MSFT | cloud_ai_capex | 400.06 |  | 395.4452 | 1.167 | 400.09 | 392.355 | 0.1575 | watch_only | none |
| 15 | AMZN | cloud_ai_capex | 230.23 |  | 229.8881 | 0.1487 | 233.05 | 229.7 | 0.0565 | watch_only | none |
| 16 | HPE | ai_server_oem | 44.71 |  | 44.2576 | 1.0223 | 46.19 | 44.33 | 0.0671 | watch_only | none |
| 17 | MRVL | custom_silicon_networking | 176.41 |  | 172.8817 | 2.0409 | 181.24 | 172.395 | 0.2154 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.44 |  | 27.7603 | 2.4484 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34.36 |  | 33.4373 | 2.7596 | 35.08 | 33.52 | 0.0291 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.315 |  | 338.5642 | 0.2217 | 342.87 | 337.78 | 0.0766 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.32 |  | 672.4255 | 0.5792 | 677.3 | 670.84 | 0.0547 | watch_only | none |
| TQQQ | leveraged_tool | 61.775 |  | 60.5878 | 1.9594 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 196.77 |  | 195.0268 | 0.8938 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 400.06 |  | 395.4452 | 1.167 | 400.09 | 392.355 | 0.1575 | watch_only | none |
| AAPL | mega_cap_platform | 339.315 |  | 338.5642 | 0.2217 | 342.87 | 337.78 | 0.0766 | watch_only | none |
| GOOGL | cloud_ai_capex | 332.41 |  | 328.1908 | 1.2856 | 330.21 | 324.97 | 0.0241 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.19 |  | 452.9693 | 0.4903 | 472.485 | 453.76 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TSM | foundry | 389.4 |  | 385.3378 | 1.0542 | 390.46 | 382.495 | 0.0847 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.51 |  | 488.604 | 0.3901 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| SMH | semiconductor_index | 529.39 |  | 525.9766 | 0.649 | 533.01 | 523.325 | 0.0888 | watch_only | none |
| AVGO | custom_silicon_networking | 380.225 |  | 376.709 | 0.9334 | 378.64 | 371.57 | 0.0947 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 817.505 |  | 812.1501 | 0.6593 | 846.4 | 813.91 | 0.3963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.41 |  | 172.8817 | 2.0409 | 181.24 | 172.395 | 0.2154 | watch_only | none |
| DELL | ai_server_oem | 377.55 |  | 372.1091 | 1.4622 | 402 | 374.02 | 0.8714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.71 |  | 44.2576 | 1.0223 | 46.19 | 44.33 | 0.0671 | watch_only | none |
| SMCI | ai_server_oem | 28.44 |  | 27.7603 | 2.4484 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 741.105 |  | 738.3046 | 0.3793 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.105 |  | 291.8602 | 0.4265 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.57 |  | 116.5938 | 3.4103 | 117.17 | 115.25 | 0.5308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.54 |  | 65.9169 | 0.9453 | 68.995 | 65.635 | 4.5386 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.04 |  | 265.6542 | 0.8981 | 273.86 | 266.04 | 0.7611 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 383.43 |  | 379.0303 | 1.1608 | 384.565 | 377.43 | 0.4382 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 580.995 |  | 579.2513 | 0.301 | 603.25 | 584.69 | 4.3546 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 941 |  | 933.2447 | 0.831 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.52 |  | 464.3677 | 0.8942 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 138.65 |  | 137.9529 | 0.5053 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.56 |  | 162.5083 | 1.8779 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 236.04 |  | 235.7611 | 0.1183 | 256.145 | 236.73 | 0.2161 | below_opening_15m_low | below_opening_15m_low |
| LITE | ai_networking_optical | 631.45 |  | 624.9966 | 1.0326 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 338.21 |  | 335.9396 | 0.6758 | 354.09 | 338.14 | 4.7278 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.21 |  | 85.0361 | 2.5564 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 259.93 |  | 255.8194 | 1.6068 | 268.265 | 253.05 | 4.9013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1573.22 |  | 1571.8141 | 0.0894 | 1586.01 | 1565.95 | 0.2873 | watch_only | none |
| AMAT | semiconductor_equipment | 474.995 |  | 476.6604 | -0.3494 | 494.87 | 477.03 | 0.8842 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 264.475 |  | 265.5248 | -0.3954 | 276.85 | 267.14 | 0.0983 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 190.66 |  | 189.9639 | 0.3664 | 194.96 | 189.48 | 0.0682 | watch_only | none |
| TER | semiconductor_test_packaging | 308.73 |  | 305.8876 | 0.9292 | 315.21 | 304.11 | 0.3142 | watch_only | none |
| ONTO | semiconductor_test_packaging | 234.05 |  | 236.7866 | -1.1557 | 248.8 | 236.42 | 0.4614 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 46.04 |  | 47.0987 | -2.2478 | 51.64 | 47.435 | 0.3041 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.41 |  | 42.5604 | -0.3535 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.41 |  | 119.3677 | 0.0354 | 121 | 117.72 | 4.7065 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 279.95 |  | 281.5197 | -0.5576 | 296.8 | 283.22 | 0.7716 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 518.5 |  | 518.6407 | -0.0271 | 518.6 | 511.495 | 4.3452 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.95 |  | 296.3217 | -0.4629 | 297.25 | 293.555 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| APLD | high_beta_ai_infrastructure | 26.91 |  | 26.4161 | 1.8698 | 27 | 25.42 | 0.0743 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.36 |  | 33.4373 | 2.7596 | 35.08 | 33.52 | 0.0291 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.19 |  | 19.93 | 1.3046 | 20.97 | 19.755 | 0.0991 | watch_only | none |
| SNDK | memory_hbm_storage | 1091.63 |  | 1101.9773 | -0.939 | 1185.19 | 1114.57 | 2.0611 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 439.09 |  | 434.0792 | 1.1544 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 724.24 |  | 722.8236 | 0.196 | 774.805 | 719.02 | 4.4557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.23 |  | 229.8881 | 0.1487 | 233.05 | 229.7 | 0.0565 | watch_only | none |
| META | cloud_ai_capex | 594.34 |  | 593.1513 | 0.2004 | 600.765 | 594.21 | 1.097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 246.45 |  | 244.7249 | 0.7049 | 253.38 | 243.72 | 2.183 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 132.13 |  | 131.3074 | 0.6264 | 136.45 | 131.735 | 1.9451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
