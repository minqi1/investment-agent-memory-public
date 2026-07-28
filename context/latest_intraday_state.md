# Intraday State

- Generated at: `2026-07-29T02:42:23+08:00`
- Market time ET: `2026-07-28T14:42:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 15, 'manual_confirm_candidate': 7, 'below_vwap': 8, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 1, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.83 |  | 674.1228 | 0.2532 | 677.3 | 670.84 | 0.0488 | watch_only | none |
| SOXX | semiconductor_index | 490.46 |  | 489.97 | 0.1 | 497.64 | 485.42 | 0.0449 | watch_only | none |
| SMH | semiconductor_index | 528.89 |  | 527.3522 | 0.2916 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| SPY | market_regime | 740.67 |  | 739.5284 | 0.1544 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.93 |  | 196.0664 | 0.4405 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.305 |  | 378.5997 | 0.4504 | 378.64 | 371.57 | 0.0841 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.67 |  | 739.5284 | 0.1544 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 168.6 |  | 164.9159 | 2.2339 | 165.975 | 160.51 | 0.1957 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.1 |  | 330.782 | 1.3054 | 330.21 | 324.97 | 0.0448 | buy_precheck_manual_confirm | none |
| 6 | ETN | data_center_power_cooling | 384.74 |  | 381.2244 | 0.9222 | 384.565 | 377.43 | 0.1715 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.8 |  | 118.4866 | 1.9525 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.67 |  | 739.5284 | 0.1544 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 196.93 |  | 196.0664 | 0.4405 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 380.305 |  | 378.5997 | 0.4504 | 378.64 | 371.57 | 0.0841 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 528.89 |  | 527.3522 | 0.2916 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| 5 | SOXX | semiconductor_index | 490.46 |  | 489.97 | 0.1 | 497.64 | 485.42 | 0.0449 | watch_only | none |
| 6 | QQQ | market_regime | 675.83 |  | 674.1228 | 0.2532 | 677.3 | 670.84 | 0.0488 | watch_only | none |
| 7 | IWM | market_regime | 292.81 |  | 292.3703 | 0.1504 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 397.305 |  | 396.3683 | 0.2363 | 400.09 | 392.355 | 0.0629 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 231.24 |  | 230.4824 | 0.3287 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 10 | HPE | ai_server_oem | 44.46 |  | 44.44 | 0.045 | 46.19 | 44.33 | 0.0675 | watch_only | none |
| 11 | MU | memory_hbm_storage | 819.565 |  | 815.3958 | 0.5113 | 846.4 | 813.91 | 0.1123 | watch_only | none |
| 12 | TER | semiconductor_test_packaging | 310.17 |  | 308.5671 | 0.5195 | 315.21 | 304.11 | 0.1064 | watch_only | none |
| 13 | SMCI | ai_server_oem | 28.165 |  | 28.0001 | 0.5891 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 14 | ETN | data_center_power_cooling | 384.74 |  | 381.2244 | 0.9222 | 384.565 | 377.43 | 0.1715 | buy_precheck_manual_confirm | none |
| 15 | MRVL | custom_silicon_networking | 174.9 |  | 174.1909 | 0.4071 | 181.24 | 172.395 | 0.3431 | watch_only | none |
| 16 | GOOGL | cloud_ai_capex | 335.1 |  | 330.782 | 1.3054 | 330.21 | 324.97 | 0.0448 | buy_precheck_manual_confirm | none |
| 17 | ASML | semiconductor_equipment | 1579.2 |  | 1577.2873 | 0.1213 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TT | data_center_power_cooling | 466.47 |  | 465.2061 | 0.2717 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 139.67 |  | 138.5456 | 0.8115 | 139.755 | 137.31 | 0.0931 | watch_only | none |
| 20 | GEV | data_center_power_cooling | 938.52 |  | 937.5544 | 0.103 | 955.825 | 935.665 | 0.5903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.93 |  | 196.0664 | 0.4405 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.305 |  | 378.5997 | 0.4504 | 378.64 | 371.57 | 0.0841 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.67 |  | 739.5284 | 0.1544 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 168.6 |  | 164.9159 | 2.2339 | 165.975 | 160.51 | 0.1957 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.1 |  | 330.782 | 1.3054 | 330.21 | 324.97 | 0.0448 | buy_precheck_manual_confirm | none |
| 6 | ETN | data_center_power_cooling | 384.74 |  | 381.2244 | 0.9222 | 384.565 | 377.43 | 0.1715 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.8 |  | 118.4866 | 1.9525 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |
| 8 | TSM | foundry | 391.48 |  | 387.7397 | 0.9646 | 390.46 | 382.495 | 1.1239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MU | memory_hbm_storage | 819.565 |  | 815.3958 | 0.5113 | 846.4 | 813.91 | 0.1123 | watch_only | none |
| 10 | SMH | semiconductor_index | 528.89 |  | 527.3522 | 0.2916 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| 11 | SOXX | semiconductor_index | 490.46 |  | 489.97 | 0.1 | 497.64 | 485.42 | 0.0449 | watch_only | none |
| 12 | QQQ | market_regime | 675.83 |  | 674.1228 | 0.2532 | 677.3 | 670.84 | 0.0488 | watch_only | none |
| 13 | JCI | data_center_power_cooling | 139.67 |  | 138.5456 | 0.8115 | 139.755 | 137.31 | 0.0931 | watch_only | none |
| 14 | WDC | memory_hbm_storage | 456.28 |  | 439.8547 | 3.7343 | 465.04 | 435.22 | 0.2827 | watch_only | none |
| 15 | IWM | market_regime | 292.81 |  | 292.3703 | 0.1504 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 16 | TER | semiconductor_test_packaging | 310.17 |  | 308.5671 | 0.5195 | 315.21 | 304.11 | 0.1064 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 397.305 |  | 396.3683 | 0.2363 | 400.09 | 392.355 | 0.0629 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.24 |  | 230.4824 | 0.3287 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.46 |  | 44.44 | 0.045 | 46.19 | 44.33 | 0.0675 | watch_only | none |
| 20 | MRVL | custom_silicon_networking | 174.9 |  | 174.1909 | 0.4071 | 181.24 | 172.395 | 0.3431 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.83 |  | 674.1228 | 0.2532 | 677.3 | 670.84 | 0.0488 | watch_only | none |
| TQQQ | leveraged_tool | 61.62 |  | 61.1074 | 0.8389 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 196.93 |  | 196.0664 | 0.4405 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.305 |  | 396.3683 | 0.2363 | 400.09 | 392.355 | 0.0629 | watch_only | none |
| AAPL | mega_cap_platform | 338.36 |  | 338.9649 | -0.1785 | 342.87 | 337.78 | 0.1566 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 335.1 |  | 330.782 | 1.3054 | 330.21 | 324.97 | 0.0448 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.8 |  | 455.5346 | 0.0583 | 472.485 | 453.76 | 2.4989 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.48 |  | 387.7397 | 0.9646 | 390.46 | 382.495 | 1.1239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.46 |  | 489.97 | 0.1 | 497.64 | 485.42 | 0.0449 | watch_only | none |
| SMH | semiconductor_index | 528.89 |  | 527.3522 | 0.2916 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| AVGO | custom_silicon_networking | 380.305 |  | 378.5997 | 0.4504 | 378.64 | 371.57 | 0.0841 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.565 |  | 815.3958 | 0.5113 | 846.4 | 813.91 | 0.1123 | watch_only | none |
| MRVL | custom_silicon_networking | 174.9 |  | 174.1909 | 0.4071 | 181.24 | 172.395 | 0.3431 | watch_only | none |
| DELL | ai_server_oem | 385.88 |  | 375.1218 | 2.8679 | 402 | 374.02 | 3.6099 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.46 |  | 44.44 | 0.045 | 46.19 | 44.33 | 0.0675 | watch_only | none |
| SMCI | ai_server_oem | 28.165 |  | 28.0001 | 0.5891 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| SPY | market_regime | 740.67 |  | 739.5284 | 0.1544 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.81 |  | 292.3703 | 0.1504 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.8 |  | 118.4866 | 1.9525 | 117.17 | 115.25 | 0.0579 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.34 |  | 66.2555 | 0.1275 | 68.995 | 65.635 | 2.0802 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.36 |  | 266.128 | -0.2886 | 273.86 | 266.04 | 2.2422 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 384.74 |  | 381.2244 | 0.9222 | 384.565 | 377.43 | 0.1715 | buy_precheck_manual_confirm | none |
| PWR | data_center_power_cooling | 586.175 |  | 582.333 | 0.6598 | 603.25 | 584.69 | 2.559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 938.52 |  | 937.5544 | 0.103 | 955.825 | 935.665 | 0.5903 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.47 |  | 465.2061 | 0.2717 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.67 |  | 138.5456 | 0.8115 | 139.755 | 137.31 | 0.0931 | watch_only | none |
| ANET | ai_networking_optical | 168.6 |  | 164.9159 | 2.2339 | 165.975 | 160.51 | 0.1957 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 241.495 |  | 237.3879 | 1.7301 | 256.145 | 236.73 | 4.8324 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 643.455 |  | 632.0968 | 1.7969 | 673.65 | 624.91 | 4.7882 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.42 |  | 337.4238 | 0.888 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87 |  | 85.8101 | 1.3867 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 259.645 |  | 259.0787 | 0.2186 | 268.265 | 253.05 | 3.5741 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1579.2 |  | 1577.2873 | 0.1213 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 474.37 |  | 476.3603 | -0.4178 | 494.87 | 477.03 | 0.9929 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.17 |  | 266.6431 | 1.3227 | 276.85 | 267.14 | 4.4416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.85 |  | 190.7673 | 0.0433 | 194.96 | 189.48 | 0.5449 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 310.17 |  | 308.5671 | 0.5195 | 315.21 | 304.11 | 0.1064 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.47 |  | 236.7558 | 0.724 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.29 |  | 46.7106 | -3.0412 | 51.64 | 47.435 | 0.3312 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.09 |  | 42.4456 | -0.8378 | 44.155 | 41.78 | 0.2376 | below_vwap | below_vwap |
| ENTG | semiconductor_materials | 118.65 |  | 119.1765 | -0.4418 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.55 |  | 282.3654 | -0.2888 | 296.8 | 283.22 | 4.4504 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.85 |  | 518.1235 | -0.4388 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.17 |  | 295.7561 | -0.1982 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.45 |  | 26.5158 | -0.2483 | 27 | 25.42 | 0.0756 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.465 |  | 33.7102 | -0.7273 | 35.08 | 33.52 | 0.0299 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.675 |  | 20.0802 | 2.9619 | 20.97 | 19.755 | 0.0484 | watch_only | none |
| SNDK | memory_hbm_storage | 1084.96 |  | 1099.8628 | -1.355 | 1185.19 | 1114.57 | 2.3337 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.28 |  | 439.8547 | 3.7343 | 465.04 | 435.22 | 0.2827 | watch_only | none |
| STX | memory_hbm_storage | 750.83 |  | 731.5567 | 2.6346 | 774.805 | 719.02 | 4.4111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.24 |  | 230.4824 | 0.3287 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.38 |  | 593.82 | -0.0741 | 600.765 | 594.21 | 0.3792 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.53 |  | 245.234 | -0.2871 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.715 |  | 131.548 | -1.3934 | 136.45 | 131.735 | 3.7775 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
