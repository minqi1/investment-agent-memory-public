# Intraday State

- Generated at: `2026-07-28T23:01:36+08:00`
- Market time ET: `2026-07-28T11:01:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 16, 'manual_confirm_candidate': 2, 'below_opening_15m_low': 13, 'price_stale_or_missing': 1, 'below_vwap': 6, 'spread_too_wide_or_missing': 18}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 673.44 |  | 671.6591 | 0.2651 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| SOXX | semiconductor_index | 489.225 |  | 488.4079 | 0.1673 | 497.64 | 485.42 | 0.094 | watch_only | none |
| SMH | semiconductor_index | 528.1 |  | 525.4006 | 0.5138 | 533.01 | 523.325 | 0.125 | watch_only | none |
| SPY | market_regime | 739.1 |  | 737.8427 | 0.1704 | 739.42 | 736.57 | 0.0041 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.98 |  | 194.6072 | 1.2193 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 378.97 |  | 375.8764 | 0.823 | 378.64 | 371.57 | 0.0739 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 489.225 |  | 488.4079 | 0.1673 | 497.64 | 485.42 | 0.094 | watch_only | none |
| 2 | SPY | market_regime | 739.1 |  | 737.8427 | 0.1704 | 739.42 | 736.57 | 0.0041 | watch_only | none |
| 3 | QQQ | market_regime | 673.44 |  | 671.6591 | 0.2651 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| 4 | IWM | market_regime | 291.75 |  | 291.6323 | 0.0403 | 293.26 | 291.55 | 0.0069 | watch_only | none |
| 5 | AMD | ai_accelerator | 453.85 |  | 452.8856 | 0.213 | 472.485 | 453.76 | 0.0485 | watch_only | none |
| 6 | TSM | foundry | 387.1 |  | 384.7511 | 0.6105 | 390.46 | 382.495 | 0.1395 | watch_only | none |
| 7 | SMH | semiconductor_index | 528.1 |  | 525.4006 | 0.5138 | 533.01 | 523.325 | 0.125 | watch_only | none |
| 8 | AVGO | custom_silicon_networking | 378.97 |  | 375.8764 | 0.823 | 378.64 | 371.57 | 0.0739 | buy_precheck_manual_confirm | none |
| 9 | GOOGL | cloud_ai_capex | 329.77 |  | 327.4261 | 0.7159 | 330.21 | 324.97 | 0.0455 | watch_only | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.04 |  | 19.9527 | 0.4378 | 20.97 | 19.755 | 0.0998 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 397.1 |  | 394.9286 | 0.5498 | 400.09 | 392.355 | 0.2317 | watch_only | none |
| 12 | NVDA | ai_accelerator | 196.98 |  | 194.6072 | 1.2193 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 13 | JCI | data_center_power_cooling | 138.185 |  | 137.8145 | 0.2689 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | HPE | ai_server_oem | 44.53 |  | 44.1562 | 0.8466 | 46.19 | 44.33 | 0.1347 | watch_only | none |
| 15 | SMCI | ai_server_oem | 27.96 |  | 27.6855 | 0.9914 | 28.86 | 27.59 | 0.0715 | watch_only | none |
| 16 | ASML | semiconductor_equipment | 1573.27 |  | 1571.723 | 0.0984 | 1586.01 | 1565.95 | 0.5988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 465.86 |  | 464.0882 | 0.3818 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ANET | ai_networking_optical | 163.165 |  | 161.9159 | 0.7714 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 379.87 |  | 378.6754 | 0.3155 | 384.565 | 377.43 | 4.341 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ARM | ai_accelerator | 244.91 |  | 244.616 | 0.1202 | 253.38 | 243.72 | 4.4261 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.98 |  | 194.6072 | 1.2193 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 378.97 |  | 375.8764 | 0.823 | 378.64 | 371.57 | 0.0739 | buy_precheck_manual_confirm | none |
| 3 | ORCL | cloud_ai_capex | 117.71 |  | 116.1141 | 1.3744 | 117.17 | 115.25 | 2.5996 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | TSM | foundry | 387.1 |  | 384.7511 | 0.6105 | 390.46 | 382.495 | 0.1395 | watch_only | none |
| 5 | SMH | semiconductor_index | 528.1 |  | 525.4006 | 0.5138 | 533.01 | 523.325 | 0.125 | watch_only | none |
| 6 | SOXX | semiconductor_index | 489.225 |  | 488.4079 | 0.1673 | 497.64 | 485.42 | 0.094 | watch_only | none |
| 7 | SPY | market_regime | 739.1 |  | 737.8427 | 0.1704 | 739.42 | 736.57 | 0.0041 | watch_only | none |
| 8 | QQQ | market_regime | 673.44 |  | 671.6591 | 0.2651 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| 9 | GOOGL | cloud_ai_capex | 329.77 |  | 327.4261 | 0.7159 | 330.21 | 324.97 | 0.0455 | watch_only | none |
| 10 | IWM | market_regime | 291.75 |  | 291.6323 | 0.0403 | 293.26 | 291.55 | 0.0069 | watch_only | none |
| 11 | AMD | ai_accelerator | 453.85 |  | 452.8856 | 0.213 | 472.485 | 453.76 | 0.0485 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 397.1 |  | 394.9286 | 0.5498 | 400.09 | 392.355 | 0.2317 | watch_only | none |
| 13 | HPE | ai_server_oem | 44.53 |  | 44.1562 | 0.8466 | 46.19 | 44.33 | 0.1347 | watch_only | none |
| 14 | DELL | ai_server_oem | 379.36 |  | 371.4073 | 2.1412 | 402 | 374.02 | 0.3427 | watch_only | none |
| 15 | SMCI | ai_server_oem | 27.96 |  | 27.6855 | 0.9914 | 28.86 | 27.59 | 0.0715 | watch_only | none |
| 16 | IREN | high_beta_ai_infrastructure | 34.19 |  | 33.3314 | 2.5759 | 35.08 | 33.52 | 0.0877 | watch_only | none |
| 17 | CORZ | high_beta_ai_infrastructure | 20.04 |  | 19.9527 | 0.4378 | 20.97 | 19.755 | 0.0998 | watch_only | none |
| 18 | APLD | high_beta_ai_infrastructure | 26.74 |  | 26.3259 | 1.573 | 27 | 25.42 | 0.1122 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 60.94 |  | 60.4602 | 0.7935 | 62.01 | 60.23 | 0.0164 | watch_only | none |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 673.44 |  | 671.6591 | 0.2651 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| TQQQ | leveraged_tool | 60.94 |  | 60.4602 | 0.7935 | 62.01 | 60.23 | 0.0164 | watch_only | none |
| NVDA | ai_accelerator | 196.98 |  | 194.6072 | 1.2193 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.1 |  | 394.9286 | 0.5498 | 400.09 | 392.355 | 0.2317 | watch_only | none |
| AAPL | mega_cap_platform | 336.76 |  | 338.5028 | -0.5149 | 342.87 | 337.78 | 0.0178 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 329.77 |  | 327.4261 | 0.7159 | 330.21 | 324.97 | 0.0455 | watch_only | none |
| AMD | ai_accelerator | 453.85 |  | 452.8856 | 0.213 | 472.485 | 453.76 | 0.0485 | watch_only | none |
| TSM | foundry | 387.1 |  | 384.7511 | 0.6105 | 390.46 | 382.495 | 0.1395 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 489.225 |  | 488.4079 | 0.1673 | 497.64 | 485.42 | 0.094 | watch_only | none |
| SMH | semiconductor_index | 528.1 |  | 525.4006 | 0.5138 | 533.01 | 523.325 | 0.125 | watch_only | none |
| AVGO | custom_silicon_networking | 378.97 |  | 375.8764 | 0.823 | 378.64 | 371.57 | 0.0739 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 815.93 |  | 811.6519 | 0.5271 | 846.4 | 813.91 | 1.2084 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 174.28 |  | 171.9568 | 1.3511 | 181.24 | 172.395 | 1.8706 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 379.36 |  | 371.4073 | 2.1412 | 402 | 374.02 | 0.3427 | watch_only | none |
| HPE | ai_server_oem | 44.53 |  | 44.1562 | 0.8466 | 46.19 | 44.33 | 0.1347 | watch_only | none |
| SMCI | ai_server_oem | 27.96 |  | 27.6855 | 0.9914 | 28.86 | 27.59 | 0.0715 | watch_only | none |
| SPY | market_regime | 739.1 |  | 737.8427 | 0.1704 | 739.42 | 736.57 | 0.0041 | watch_only | none |
| IWM | market_regime | 291.75 |  | 291.6323 | 0.0403 | 293.26 | 291.55 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 117.71 |  | 116.1141 | 1.3744 | 117.17 | 115.25 | 2.5996 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.18 |  | 65.8885 | 0.4425 | 68.995 | 65.635 | 4.7597 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 264.8 |  | 265.5831 | -0.2949 | 273.86 | 266.04 | 0.4532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 379.87 |  | 378.6754 | 0.3155 | 384.565 | 377.43 | 4.341 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 577.77 |  | 578.7866 | -0.1756 | 603.25 | 584.69 | 0.611 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 931.29 |  | 933.0484 | -0.1885 | 955.825 | 935.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 465.86 |  | 464.0882 | 0.3818 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 138.185 |  | 137.8145 | 0.2689 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 163.165 |  | 161.9159 | 0.7714 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 237.99 |  | 235.6817 | 0.9794 | 256.145 | 236.73 | 4.2313 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 636.67 |  | 624.124 | 2.0102 | 673.65 | 624.91 | 2.6921 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.81 |  | 335.6339 | 1.5422 | 354.09 | 338.14 | 4.3983 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.23 |  | 84.8338 | 2.8246 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 254.495 |  | 255.2975 | -0.3143 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1573.27 |  | 1571.723 | 0.0984 | 1586.01 | 1565.95 | 0.5988 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 474.66 |  | 477.1908 | -0.5303 | 494.87 | 477.03 | 4.5949 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 264.43 |  | 265.6868 | -0.473 | 276.85 | 267.14 | 1.1686 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 189.65 |  | 189.9662 | -0.1665 | 194.96 | 189.48 | 0.0685 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 308.38 |  | 305.4798 | 0.9494 | 315.21 | 304.11 | 4.7701 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 232.9 |  | 237.5221 | -1.946 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.93 |  | 47.2242 | -0.6231 | 51.64 | 47.435 | 0.1918 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.525 |  | 42.6543 | -0.3032 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.38 |  | 119.1896 | 0.9987 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 279.33 |  | 281.8549 | -0.8958 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.29 |  | 518.6762 | -0.0745 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.71 |  | 296.4205 | -0.2397 | 297.25 | 293.555 | 0.5715 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.74 |  | 26.3259 | 1.573 | 27 | 25.42 | 0.1122 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.19 |  | 33.3314 | 2.5759 | 35.08 | 33.52 | 0.0877 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.04 |  | 19.9527 | 0.4378 | 20.97 | 19.755 | 0.0998 | watch_only | none |
| SNDK | memory_hbm_storage | 1100.01 |  | 1103.5205 | -0.3181 | 1185.19 | 1114.57 | 1.5909 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 437.97 |  | 433.4995 | 1.0312 | 465.04 | 435.22 | 0.8745 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 729.185 |  | 722.4101 | 0.9378 | 774.805 | 719.02 | 3.9345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 229.285 |  | 229.9464 | -0.2876 | 233.05 | 229.7 | 0.0174 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 589.385 |  | 594.243 | -0.8175 | 600.765 | 594.21 | 0.1663 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 244.91 |  | 244.616 | 0.1202 | 253.38 | 243.72 | 4.4261 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 131.6 |  | 131.4304 | 0.129 | 136.45 | 131.735 | 0.6155 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
