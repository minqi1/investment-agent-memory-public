# Intraday State

- Generated at: `2026-07-29T02:27:04+08:00`
- Market time ET: `2026-07-28T14:27:05-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 20, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 1, 'below_vwap': 8, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.78 |  | 674.0858 | 0.2513 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| SOXX | semiconductor_index | 490.38 |  | 489.9604 | 0.0856 | 497.64 | 485.42 | 0.0632 | watch_only | none |
| SMH | semiconductor_index | 528.475 |  | 527.3298 | 0.2172 | 533.01 | 523.325 | 0.0492 | watch_only | none |
| SPY | market_regime | 740.6 |  | 739.5 | 0.1487 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.93 |  | 196.0287 | 0.4598 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.56 |  | 378.5667 | 0.2624 | 378.64 | 371.57 | 0.0395 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.6 |  | 739.5 | 0.1487 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 168.32 |  | 164.6769 | 2.2122 | 165.975 | 160.51 | 0.2317 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.88 |  | 330.6225 | 1.2877 | 330.21 | 324.97 | 0.2986 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.56 |  | 378.5667 | 0.2624 | 378.64 | 371.57 | 0.0395 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.6 |  | 739.5 | 0.1487 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 196.93 |  | 196.0287 | 0.4598 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 528.475 |  | 527.3298 | 0.2172 | 533.01 | 523.325 | 0.0492 | watch_only | none |
| 5 | SOXX | semiconductor_index | 490.38 |  | 489.9604 | 0.0856 | 497.64 | 485.42 | 0.0632 | watch_only | none |
| 6 | QQQ | market_regime | 675.78 |  | 674.0858 | 0.2513 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1578.925 |  | 1577.212 | 0.1086 | 1586.01 | 1565.95 | 0.133 | watch_only | none |
| 8 | IWM | market_regime | 292.64 |  | 292.3401 | 0.1026 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 231.22 |  | 230.4699 | 0.3254 | 233.05 | 229.7 | 0.0086 | watch_only | none |
| 10 | AAPL | mega_cap_platform | 339.85 |  | 338.9431 | 0.2676 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 11 | META | cloud_ai_capex | 594.41 |  | 593.8437 | 0.0954 | 600.765 | 594.21 | 0.2204 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 397.43 |  | 396.3413 | 0.2747 | 400.09 | 392.355 | 0.1988 | watch_only | none |
| 13 | TT | data_center_power_cooling | 466.86 |  | 465.1447 | 0.3688 | 477.73 | 460.77 | 0.1178 | watch_only | none |
| 14 | PWR | data_center_power_cooling | 585.3 |  | 582.1975 | 0.5329 | 603.25 | 584.69 | 0.0923 | watch_only | none |
| 15 | SMCI | ai_server_oem | 28.21 |  | 27.9945 | 0.77 | 28.86 | 27.59 | 0.0709 | watch_only | none |
| 16 | CIEN | ai_networking_optical | 339.2 |  | 337.3759 | 0.5407 | 354.09 | 338.14 | 0.2064 | watch_only | none |
| 17 | MRVL | custom_silicon_networking | 175.02 |  | 174.1779 | 0.4835 | 181.24 | 172.395 | 0.2343 | watch_only | none |
| 18 | GOOGL | cloud_ai_capex | 334.88 |  | 330.6225 | 1.2877 | 330.21 | 324.97 | 0.2986 | buy_precheck_manual_confirm | none |
| 19 | TER | semiconductor_test_packaging | 308.52 |  | 308.4 | 0.0389 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | LITE | ai_networking_optical | 639.19 |  | 631.8376 | 1.1637 | 673.65 | 624.91 | 0.3051 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.93 |  | 196.0287 | 0.4598 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.56 |  | 378.5667 | 0.2624 | 378.64 | 371.57 | 0.0395 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.6 |  | 739.5 | 0.1487 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 168.32 |  | 164.6769 | 2.2122 | 165.975 | 160.51 | 0.2317 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 334.88 |  | 330.6225 | 1.2877 | 330.21 | 324.97 | 0.2986 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 390.905 |  | 387.6302 | 0.8448 | 390.46 | 382.495 | 1.21 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | JCI | data_center_power_cooling | 139.84 |  | 138.4883 | 0.9761 | 139.755 | 137.31 | 3.3395 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ORCL | cloud_ai_capex | 120.43 |  | 118.382 | 1.73 | 117.17 | 115.25 | 1.2871 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 528.475 |  | 527.3298 | 0.2172 | 533.01 | 523.325 | 0.0492 | watch_only | none |
| 10 | SOXX | semiconductor_index | 490.38 |  | 489.9604 | 0.0856 | 497.64 | 485.42 | 0.0632 | watch_only | none |
| 11 | QQQ | market_regime | 675.78 |  | 674.0858 | 0.2513 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| 12 | ASML | semiconductor_equipment | 1578.925 |  | 1577.212 | 0.1086 | 1586.01 | 1565.95 | 0.133 | watch_only | none |
| 13 | TT | data_center_power_cooling | 466.86 |  | 465.1447 | 0.3688 | 477.73 | 460.77 | 0.1178 | watch_only | none |
| 14 | STX | memory_hbm_storage | 748.97 |  | 730.7815 | 2.4889 | 774.805 | 719.02 | 0.0948 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 585.3 |  | 582.1975 | 0.5329 | 603.25 | 584.69 | 0.0923 | watch_only | none |
| 16 | WDC | memory_hbm_storage | 455.185 |  | 439.3572 | 3.6025 | 465.04 | 435.22 | 0.2175 | watch_only | none |
| 17 | IWM | market_regime | 292.64 |  | 292.3401 | 0.1026 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 18 | LITE | ai_networking_optical | 639.19 |  | 631.8376 | 1.1637 | 673.65 | 624.91 | 0.3051 | watch_only | none |
| 19 | META | cloud_ai_capex | 594.41 |  | 593.8437 | 0.0954 | 600.765 | 594.21 | 0.2204 | watch_only | none |
| 20 | LRCX | semiconductor_equipment | 270.33 |  | 266.5721 | 1.4097 | 276.85 | 267.14 | 0.2589 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.78 |  | 674.0858 | 0.2513 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| TQQQ | leveraged_tool | 61.59 |  | 61.0993 | 0.8032 | 62.01 | 60.23 | 0.0325 | watch_only | none |
| NVDA | ai_accelerator | 196.93 |  | 196.0287 | 0.4598 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.43 |  | 396.3413 | 0.2747 | 400.09 | 392.355 | 0.1988 | watch_only | none |
| AAPL | mega_cap_platform | 339.85 |  | 338.9431 | 0.2676 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.88 |  | 330.6225 | 1.2877 | 330.21 | 324.97 | 0.2986 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.67 |  | 455.5272 | 0.0314 | 472.485 | 453.76 | 4.6876 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 390.905 |  | 387.6302 | 0.8448 | 390.46 | 382.495 | 1.21 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.38 |  | 489.9604 | 0.0856 | 497.64 | 485.42 | 0.0632 | watch_only | none |
| SMH | semiconductor_index | 528.475 |  | 527.3298 | 0.2172 | 533.01 | 523.325 | 0.0492 | watch_only | none |
| AVGO | custom_silicon_networking | 379.56 |  | 378.5667 | 0.2624 | 378.64 | 371.57 | 0.0395 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 814.98 |  | 815.318 | -0.0415 | 846.4 | 813.91 | 0.0724 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 175.02 |  | 174.1779 | 0.4835 | 181.24 | 172.395 | 0.2343 | watch_only | none |
| DELL | ai_server_oem | 383.91 |  | 374.9739 | 2.3831 | 402 | 374.02 | 0.7788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.395 |  | 44.4398 | -0.1008 | 46.19 | 44.33 | 0.0225 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.21 |  | 27.9945 | 0.77 | 28.86 | 27.59 | 0.0709 | watch_only | none |
| SPY | market_regime | 740.6 |  | 739.5 | 0.1487 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.64 |  | 292.3401 | 0.1026 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.43 |  | 118.382 | 1.73 | 117.17 | 115.25 | 1.2871 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.315 |  | 66.2546 | 0.0912 | 68.995 | 65.635 | 2.277 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 264.35 |  | 266.1802 | -0.6876 | 273.86 | 266.04 | 1.6682 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 384.465 |  | 381.1045 | 0.8818 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.3 |  | 582.1975 | 0.5329 | 603.25 | 584.69 | 0.0923 | watch_only | none |
| GEV | data_center_power_cooling | 937.92 |  | 937.5565 | 0.0388 | 955.825 | 935.665 | 0.8231 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.86 |  | 465.1447 | 0.3688 | 477.73 | 460.77 | 0.1178 | watch_only | none |
| JCI | data_center_power_cooling | 139.84 |  | 138.4883 | 0.9761 | 139.755 | 137.31 | 3.3395 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 168.32 |  | 164.6769 | 2.2122 | 165.975 | 160.51 | 0.2317 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 239.54 |  | 237.2892 | 0.9486 | 256.145 | 236.73 | 4.3041 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 639.19 |  | 631.8376 | 1.1637 | 673.65 | 624.91 | 0.3051 | watch_only | none |
| CIEN | ai_networking_optical | 339.2 |  | 337.3759 | 0.5407 | 354.09 | 338.14 | 0.2064 | watch_only | none |
| AAOI | ai_networking_optical | 86.8 |  | 85.7792 | 1.19 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.62 |  | 259.0535 | 0.6047 | 268.265 | 253.05 | 3.7833 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1578.925 |  | 1577.212 | 0.1086 | 1586.01 | 1565.95 | 0.133 | watch_only | none |
| AMAT | semiconductor_equipment | 474.01 |  | 476.4102 | -0.5038 | 494.87 | 477.03 | 0.327 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 270.33 |  | 266.5721 | 1.4097 | 276.85 | 267.14 | 0.2589 | watch_only | none |
| KLAC | semiconductor_equipment | 190.805 |  | 190.7621 | 0.0225 | 194.96 | 189.48 | 0.4874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 308.52 |  | 308.4 | 0.0389 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 238.35 |  | 236.7165 | 0.6901 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.57 |  | 46.7237 | -2.4692 | 51.64 | 47.435 | 0.2414 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 41.965 |  | 42.4646 | -1.1766 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.5 |  | 119.2562 | -0.6341 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.39 |  | 282.3781 | -0.3499 | 296.8 | 283.22 | 0.2381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LIN | industrial_gases | 514.07 |  | 518.2926 | -0.8147 | 518.6 | 511.495 | 0.0642 | below_vwap | below_vwap |
| APD | industrial_gases | 294.69 |  | 295.7818 | -0.3691 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.27 |  | 26.5193 | -0.94 | 27 | 25.42 | 1.0278 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.505 |  | 33.7153 | -0.6238 | 35.08 | 33.52 | 0.0298 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.48 |  | 20.0539 | 2.1249 | 20.97 | 19.755 | 0.0488 | watch_only | none |
| SNDK | memory_hbm_storage | 1074.95 |  | 1100.3866 | -2.3116 | 1185.19 | 1114.57 | 1.5126 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 455.185 |  | 439.3572 | 3.6025 | 465.04 | 435.22 | 0.2175 | watch_only | none |
| STX | memory_hbm_storage | 748.97 |  | 730.7815 | 2.4889 | 774.805 | 719.02 | 0.0948 | watch_only | none |
| AMZN | cloud_ai_capex | 231.22 |  | 230.4699 | 0.3254 | 233.05 | 229.7 | 0.0086 | watch_only | none |
| META | cloud_ai_capex | 594.41 |  | 593.8437 | 0.0954 | 600.765 | 594.21 | 0.2204 | watch_only | none |
| ARM | ai_accelerator | 243.49 |  | 245.2703 | -0.7259 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.04 |  | 131.6119 | -1.1943 | 136.45 | 131.735 | 3.8834 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
