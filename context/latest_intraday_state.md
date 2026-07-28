# Intraday State

- Generated at: `2026-07-28T23:12:11+08:00`
- Market time ET: `2026-07-28T11:12:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 17, 'manual_confirm_candidate': 1, 'below_opening_15m_low': 18, 'price_stale_or_missing': 1, 'below_vwap': 7, 'spread_too_wide_or_missing': 12}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 673.08 |  | 671.7513 | 0.1978 | 677.3 | 670.84 | 0.0802 | watch_only | none |
| SOXX | semiconductor_index | 487.79 |  | 488.4041 | -0.1257 | 497.64 | 485.42 | 0.0554 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.24 |  | 525.4813 | 0.1444 | 533.01 | 523.325 | 0.1083 | watch_only | none |
| SPY | market_regime | 738.72 |  | 737.894 | 0.1119 | 739.42 | 736.57 | 0.023 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.24 |  | 194.7366 | 0.772 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.24 |  | 194.7366 | 0.772 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 526.24 |  | 525.4813 | 0.1444 | 533.01 | 523.325 | 0.1083 | watch_only | none |
| 3 | SPY | market_regime | 738.72 |  | 737.894 | 0.1119 | 739.42 | 736.57 | 0.023 | watch_only | none |
| 4 | QQQ | market_regime | 673.08 |  | 671.7513 | 0.1978 | 677.3 | 670.84 | 0.0802 | watch_only | none |
| 5 | IWM | market_regime | 291.69 |  | 291.6308 | 0.0203 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| 6 | TSM | foundry | 385.445 |  | 384.8193 | 0.1626 | 390.46 | 382.495 | 0.1531 | watch_only | none |
| 7 | SMCI | ai_server_oem | 27.78 |  | 27.689 | 0.3288 | 28.86 | 27.59 | 0.072 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 339.28 |  | 338.48 | 0.2364 | 342.87 | 337.78 | 0.0236 | watch_only | none |
| 9 | AVGO | custom_silicon_networking | 378.07 |  | 376.0251 | 0.5438 | 378.64 | 371.57 | 0.0582 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 397.13 |  | 395.0145 | 0.5355 | 400.09 | 392.355 | 0.0982 | watch_only | none |
| 11 | TT | data_center_power_cooling | 465.955 |  | 464.153 | 0.3882 | 477.73 | 460.77 | 0.2339 | watch_only | none |
| 12 | STX | memory_hbm_storage | 725.61 |  | 722.5511 | 0.4234 | 774.805 | 719.02 | 0.2398 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 329.15 |  | 327.5591 | 0.4857 | 330.21 | 324.97 | 0.2096 | watch_only | none |
| 14 | ETN | data_center_power_cooling | 380.77 |  | 378.7347 | 0.5374 | 384.565 | 377.43 | 0.2416 | watch_only | none |
| 15 | JCI | data_center_power_cooling | 138.13 |  | 137.8321 | 0.2161 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 256.11 |  | 255.2923 | 0.3203 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | HPE | ai_server_oem | 44.54 |  | 44.1742 | 0.8281 | 46.19 | 44.33 | 0.1347 | watch_only | none |
| 18 | IREN | high_beta_ai_infrastructure | 33.75 |  | 33.352 | 1.1933 | 35.08 | 33.52 | 0.0593 | watch_only | none |
| 19 | DELL | ai_server_oem | 375.55 |  | 371.654 | 1.0483 | 402 | 374.02 | 0.3408 | watch_only | none |
| 20 | LITE | ai_networking_optical | 629.02 |  | 624.3641 | 0.7457 | 673.65 | 624.91 | 1.2464 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.24 |  | 194.7366 | 0.772 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | ORCL | cloud_ai_capex | 117.76 |  | 116.2015 | 1.3412 | 117.17 | 115.25 | 2.123 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | TSM | foundry | 385.445 |  | 384.8193 | 0.1626 | 390.46 | 382.495 | 0.1531 | watch_only | none |
| 4 | SMH | semiconductor_index | 526.24 |  | 525.4813 | 0.1444 | 533.01 | 523.325 | 0.1083 | watch_only | none |
| 5 | AVGO | custom_silicon_networking | 378.07 |  | 376.0251 | 0.5438 | 378.64 | 371.57 | 0.0582 | watch_only | none |
| 6 | SPY | market_regime | 738.72 |  | 737.894 | 0.1119 | 739.42 | 736.57 | 0.023 | watch_only | none |
| 7 | QQQ | market_regime | 673.08 |  | 671.7513 | 0.1978 | 677.3 | 670.84 | 0.0802 | watch_only | none |
| 8 | TT | data_center_power_cooling | 465.955 |  | 464.153 | 0.3882 | 477.73 | 460.77 | 0.2339 | watch_only | none |
| 9 | STX | memory_hbm_storage | 725.61 |  | 722.5511 | 0.4234 | 774.805 | 719.02 | 0.2398 | watch_only | none |
| 10 | GOOGL | cloud_ai_capex | 329.15 |  | 327.5591 | 0.4857 | 330.21 | 324.97 | 0.2096 | watch_only | none |
| 11 | ETN | data_center_power_cooling | 380.77 |  | 378.7347 | 0.5374 | 384.565 | 377.43 | 0.2416 | watch_only | none |
| 12 | IWM | market_regime | 291.69 |  | 291.6308 | 0.0203 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 397.13 |  | 395.0145 | 0.5355 | 400.09 | 392.355 | 0.0982 | watch_only | none |
| 14 | HPE | ai_server_oem | 44.54 |  | 44.1742 | 0.8281 | 46.19 | 44.33 | 0.1347 | watch_only | none |
| 15 | DELL | ai_server_oem | 375.55 |  | 371.654 | 1.0483 | 402 | 374.02 | 0.3408 | watch_only | none |
| 16 | SMCI | ai_server_oem | 27.78 |  | 27.689 | 0.3288 | 28.86 | 27.59 | 0.072 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 33.75 |  | 33.352 | 1.1933 | 35.08 | 33.52 | 0.0593 | watch_only | none |
| 18 | AAPL | mega_cap_platform | 339.28 |  | 338.48 | 0.2364 | 342.87 | 337.78 | 0.0236 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 60.88 |  | 60.4804 | 0.6607 | 62.01 | 60.23 | 0.0329 | watch_only | none |
| 20 | SOXX | semiconductor_index | 487.79 |  | 488.4041 | -0.1257 | 497.64 | 485.42 | 0.0554 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 673.08 |  | 671.7513 | 0.1978 | 677.3 | 670.84 | 0.0802 | watch_only | none |
| TQQQ | leveraged_tool | 60.88 |  | 60.4804 | 0.6607 | 62.01 | 60.23 | 0.0329 | watch_only | none |
| NVDA | ai_accelerator | 196.24 |  | 194.7366 | 0.772 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.13 |  | 395.0145 | 0.5355 | 400.09 | 392.355 | 0.0982 | watch_only | none |
| AAPL | mega_cap_platform | 339.28 |  | 338.48 | 0.2364 | 342.87 | 337.78 | 0.0236 | watch_only | none |
| GOOGL | cloud_ai_capex | 329.15 |  | 327.5591 | 0.4857 | 330.21 | 324.97 | 0.2096 | watch_only | none |
| AMD | ai_accelerator | 452.58 |  | 452.8235 | -0.0538 | 472.485 | 453.76 | 0.179 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 385.445 |  | 384.8193 | 0.1626 | 390.46 | 382.495 | 0.1531 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 487.79 |  | 488.4041 | -0.1257 | 497.64 | 485.42 | 0.0554 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.24 |  | 525.4813 | 0.1444 | 533.01 | 523.325 | 0.1083 | watch_only | none |
| AVGO | custom_silicon_networking | 378.07 |  | 376.0251 | 0.5438 | 378.64 | 371.57 | 0.0582 | watch_only | none |
| MU | memory_hbm_storage | 813.555 |  | 811.7893 | 0.2175 | 846.4 | 813.91 | 0.6318 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 174.25 |  | 172.1816 | 1.2013 | 181.24 | 172.395 | 4.0172 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 375.55 |  | 371.654 | 1.0483 | 402 | 374.02 | 0.3408 | watch_only | none |
| HPE | ai_server_oem | 44.54 |  | 44.1742 | 0.8281 | 46.19 | 44.33 | 0.1347 | watch_only | none |
| SMCI | ai_server_oem | 27.78 |  | 27.689 | 0.3288 | 28.86 | 27.59 | 0.072 | watch_only | none |
| SPY | market_regime | 738.72 |  | 737.894 | 0.1119 | 739.42 | 736.57 | 0.023 | watch_only | none |
| IWM | market_regime | 291.69 |  | 291.6308 | 0.0203 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| ORCL | cloud_ai_capex | 117.76 |  | 116.2015 | 1.3412 | 117.17 | 115.25 | 2.123 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 65.73 |  | 65.8838 | -0.2335 | 68.995 | 65.635 | 4.5946 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 265.07 |  | 265.5656 | -0.1866 | 273.86 | 266.04 | 1.4562 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 380.77 |  | 378.7347 | 0.5374 | 384.565 | 377.43 | 0.2416 | watch_only | none |
| PWR | data_center_power_cooling | 579.36 |  | 578.7604 | 0.1036 | 603.25 | 584.69 | 0.4747 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 934.475 |  | 933.0086 | 0.1572 | 955.825 | 935.665 | 5.1066 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 465.955 |  | 464.153 | 0.3882 | 477.73 | 460.77 | 0.2339 | watch_only | none |
| JCI | data_center_power_cooling | 138.13 |  | 137.8321 | 0.2161 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 163.44 |  | 161.991 | 0.8945 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 236.09 |  | 235.7326 | 0.1516 | 256.145 | 236.73 | 3.0751 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 629.02 |  | 624.3641 | 0.7457 | 673.65 | 624.91 | 1.2464 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 339.34 |  | 335.7504 | 1.0691 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 86.42 |  | 84.9176 | 1.7692 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 256.11 |  | 255.2923 | 0.3203 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1563.07 |  | 1571.4719 | -0.5346 | 1586.01 | 1565.95 | 0.4037 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 473.355 |  | 476.9672 | -0.7573 | 494.87 | 477.03 | 1.6394 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 264.54 |  | 265.5841 | -0.3931 | 276.85 | 267.14 | 2.011 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 189.17 |  | 189.9155 | -0.3925 | 194.96 | 189.48 | 0.0581 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 306.825 |  | 305.5636 | 0.4128 | 315.21 | 304.11 | 4.4683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 232.72 |  | 237.4163 | -1.9781 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.225 |  | 47.1956 | -2.0565 | 51.64 | 47.435 | 1.8172 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.3 |  | 42.633 | -0.781 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.295 |  | 119.2816 | 0.8496 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 278.43 |  | 281.7285 | -1.1708 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.59 |  | 518.6504 | -0.0116 | 518.6 | 511.495 | 4.1401 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.48 |  | 296.3931 | -0.3081 | 297.25 | 293.555 | 4.2338 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.85 |  | 26.3486 | 1.9031 | 27 | 25.42 | 0.5214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.75 |  | 33.352 | 1.1933 | 35.08 | 33.52 | 0.0593 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 19.665 |  | 19.9302 | -1.3308 | 20.97 | 19.755 | 0.0509 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1090.17 |  | 1102.7517 | -1.1409 | 1185.19 | 1114.57 | 0.3577 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 439.53 |  | 433.6816 | 1.3485 | 465.04 | 435.22 | 1.4265 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 725.61 |  | 722.5511 | 0.4234 | 774.805 | 719.02 | 0.2398 | watch_only | none |
| AMZN | cloud_ai_capex | 229.08 |  | 229.8596 | -0.3392 | 233.05 | 229.7 | 0.0262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 588.945 |  | 593.1834 | -0.7145 | 600.765 | 594.21 | 0.1511 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 244.51 |  | 244.6232 | -0.0463 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.12 |  | 131.309 | -0.9055 | 136.45 | 131.735 | 0.1844 | below_opening_15m_low | below_opening_15m_low,below_vwap |
